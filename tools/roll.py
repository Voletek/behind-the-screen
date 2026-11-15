#!/usr/bin/env python3
"""
roll.py - honest, logged dice for AI game masters (standard library only).

Tenet 5 (Honest Dice): an AI cannot generate fair randomness from text. Call this tool, show the
result line, and log it.

Expressions
  1d20+5            sum of dice plus modifiers (any number of NdS terms and +/-N)
  2d20kh1+5         keep highest 1 (advantage);   2d20kl1+5  keep lowest 1 (disadvantage)
  4d6dl1            drop lowest 1;                 4d6dh1     drop highest 1
  5d6>=4            dice pool: count dice >= 4 (Mouse Guard); add ! to explode max faces: 5d6>=4!
  6d6!              exploding sum
  pbta+2            2d6+2 read as 10+ / 7-9 / 6- (Root, Rules-Light)
  3d6kh2+2          Rules-Light edge (keep best 2 of 3)
  d616+3            Marvel Multiverse: 3d6, one is the Marvel die (1 = M = 6, Fantastic)
  1d100             percentile; use --under 45 for roll-under skills (Palladium)
  4dF+1             Fate/Fudge dice (-1, 0, +1)

Targets
  --dc N / --ac N / --tn N   success if total >= N
  --ob N                     pool: success if successes >= N
  --under N                  success if total <= N (percentile skills)
  --crit N                   pbta: N+ is a critical (Rules-Light uses 12)

Other
  --edge N / --trouble N     d616 edges and troubles (cancel one for one)
  --record "14,3"            log a PLAYER's physical roll instead of rolling (source: player)
  --who, --why, --session    context for the log line
  --log FILE                 append a JSON line to FILE (campaigns/<id>/dice-log.jsonl)
  --hidden                   mark the roll hidden (still logged)
  --seed N                   deterministic (tests only; recorded in the log)
  --json                     print the result as JSON
  --times N                  roll the same expression N times

Exit code 0 on success, 2 on a bad expression.
"""

import argparse
import datetime
import json
import random
import re
import secrets
import sys

TERM_RE = re.compile(
    r"(?P<sign>[+-]?)\s*(?:"
    r"(?P<n>\d*)d(?P<s>\d+|F)(?P<keep>(?:kh|kl|dh|dl)\d+)?(?P<explode>!)?(?:>=(?P<succ>\d+))?(?P<explode2>!)?"
    r"|(?P<mod>\d+))",
    re.I,
)


class RollError(ValueError):
    pass


class Dice:
    def __init__(self, seed=None, recorded=None):
        self.rng = random.Random(seed) if seed is not None else secrets.SystemRandom()
        self.recorded = list(recorded) if recorded is not None else None

    def roll(self, sides):
        if self.recorded is not None:
            if not self.recorded:
                raise RollError("--record has fewer values than the expression needs")
            value = self.recorded.pop(0)
            lo, hi = (-1, 1) if sides == "F" else (1, sides)
            if not lo <= value <= hi:
                raise RollError(f"recorded value {value} is not possible on a d{sides}")
            return value
        if sides == "F":
            return self.rng.choice([-1, 0, 1])
        return self.rng.randint(1, sides)


def parse_terms(expr):
    expr = expr.replace(" ", "")
    pos, terms = 0, []
    while pos < len(expr):
        m = TERM_RE.match(expr, pos)
        if not m or m.end() == pos:
            raise RollError(f"cannot parse expression at: {expr[pos:]!r}")
        if not m.group("sign") and terms:
            raise RollError(f"missing + or - before {m.group(0)!r}")
        terms.append(m)
        pos = m.end()
    if not terms:
        raise RollError("empty expression")
    return terms


def roll_generic(expr, dice):
    terms = parse_terms(expr)
    total, all_kept, detail, pool_successes, pool = 0, [], [], None, False
    sum_mod = 0
    for m in terms:
        sign = -1 if m.group("sign") == "-" else 1
        if m.group("mod") is not None:
            sum_mod += sign * int(m.group("mod"))
            continue
        n = int(m.group("n") or 1)
        sides_raw = m.group("s")
        sides = "F" if sides_raw.upper() == "F" else int(sides_raw)
        if n < 1 or n > 200 or (sides != "F" and sides < 2):
            raise RollError(f"unsupported dice term {m.group(0)!r}")
        explode = bool(m.group("explode") or m.group("explode2"))
        rolls = []
        for _ in range(n):
            v = dice.roll(sides)
            rolls.append(v)
            chain = 0
            while explode and sides != "F" and v == sides and chain < 50:
                v = dice.roll(sides)
                rolls.append(v)
                chain += 1
        kept = list(rolls)
        keep = m.group("keep")
        if keep:
            mode, k = keep[:2].lower(), int(keep[2:])
            if k > len(rolls):
                raise RollError(f"cannot keep/drop {k} of {len(rolls)} dice")
            order = sorted(range(len(rolls)), key=lambda i: rolls[i])
            if mode == "kh":
                idx = set(order[len(rolls) - k:])
            elif mode == "kl":
                idx = set(order[:k])
            elif mode == "dl":
                idx = set(order[k:])
            else:  # dh
                idx = set(order[:len(rolls) - k])
            kept = [rolls[i] for i in sorted(idx)]
        if m.group("succ"):
            pool = True
            target = int(m.group("succ"))
            succ = sum(1 for v in kept if v >= target)
            pool_successes = (pool_successes or 0) + sign * succ
            detail.append({"term": m.group(0).lstrip("+-"), "dice": rolls, "successes": succ})
        else:
            total += sign * sum(kept)
            detail.append({"term": m.group(0).lstrip("+-"), "dice": rolls, "kept": kept})
        all_kept.extend(kept)
    if pool:
        result = {"kind": "pool", "successes": pool_successes + sum_mod, "total": pool_successes + sum_mod}
    else:
        result = {"kind": "sum", "total": total + sum_mod}
    result.update({"modifier": sum_mod, "terms": detail})
    single = [d for d in detail if len(d.get("kept", [])) == 1 and d["term"].lower().startswith(("1d20", "d20", "2d20"))]
    if single:
        result["natural"] = single[0]["kept"][0]
    return result


def roll_pbta(mod, dice):
    a, b = dice.roll(6), dice.roll(6)
    return {"kind": "pbta", "terms": [{"term": "2d6", "dice": [a, b], "kept": [a, b]}],
            "modifier": mod, "total": a + b + mod}


def roll_d616(mod, dice, edge=0, trouble=0):
    regular = [dice.roll(6), dice.roll(6)]
    marvel = dice.roll(6)
    history = []
    net = edge - trouble

    def value(face, is_marvel):
        return 6 if (is_marvel and face == 1) else face

    for _ in range(abs(net)):
        faces = [(value(regular[0], False), 0), (value(regular[1], False), 1), (value(marvel, True), 2)]
        if net > 0:   # edge: reroll the lowest die, keep the better
            v, i = min(faces)
        else:         # trouble: reroll the highest die, keep the worse
            v, i = max(faces)
        new = dice.roll(6)
        is_m = i == 2
        better = value(new, is_m) > v
        keep_new = better if net > 0 else (value(new, is_m) < v)
        history.append({"die": "marvel" if is_m else f"d{i + 1}", "old": v, "new": value(new, is_m), "kept_new": keep_new})
        if keep_new:
            if is_m:
                marvel = new
            else:
                regular[i] = new
    fantastic = marvel == 1
    mval = 6 if fantastic else marvel
    total = regular[0] + regular[1] + mval + mod
    ultimate = fantastic and regular[0] == 6 and regular[1] == 6
    return {"kind": "d616", "terms": [{"term": "d616", "dice": regular + [marvel],
                                        "marvel_die": "M" if fantastic else marvel}],
            "modifier": mod, "total": total, "fantastic": fantastic,
            "ultimate_fantastic": ultimate, "edge_trouble": history}


def evaluate(expr, dice, edge=0, trouble=0):
    e = expr.strip().lower().replace(" ", "")
    m = re.fullmatch(r"pbta([+-]\d+)?", e)
    if m:
        return roll_pbta(int(m.group(1) or 0), dice)
    m = re.fullmatch(r"(?:1)?d616([+-]\d+)?", e)
    if m:
        return roll_d616(int(m.group(1) or 0), dice, edge, trouble)
    if edge or trouble:
        raise RollError("--edge/--trouble only apply to d616")
    return roll_generic(e, dice)


def judge(result, args):
    """Attach target and outcome."""
    total = result["total"]
    outcome = None
    target = None
    if result["kind"] == "pbta":
        crit = args.crit
        if crit and total >= crit:
            outcome = "critical"
        elif total >= 10:
            outcome = "full success"
        elif total >= 7:
            outcome = "partial success"
        else:
            outcome = "miss"
    for name in ("dc", "ac", "tn"):
        val = getattr(args, name)
        if val is not None:
            target = {"type": name.upper(), "value": val}
            outcome = "success" if total >= val else "failure"
    if args.ob is not None:
        target = {"type": "Ob", "value": args.ob}
        outcome = "success" if total >= args.ob else "failure"
    if args.under is not None:
        target = {"type": "under", "value": args.under}
        outcome = "success" if total <= args.under else "failure"
    nat = result.get("natural")
    if nat == 20 and result["kind"] == "sum":
        result["note"] = "natural 20"
    elif nat == 1 and result["kind"] == "sum":
        result["note"] = "natural 1"
    if result.get("ultimate_fantastic"):
        result["note"] = "ULTIMATE FANTASTIC"
    elif result.get("fantastic"):
        result["note"] = "Fantastic (Marvel die shows M)"
    result["target"] = target
    result["outcome"] = outcome
    return result


def term_text(t):
    if t.get("marvel_die") is not None:
        faces = [str(d) for d in t["dice"][:2]] + [f"M:{t['marvel_die']}"]
        return "[" + ", ".join(faces) + "]"
    kept = t.get("kept")
    if kept is None or len(kept) == len(t["dice"]):
        return "[" + ", ".join(str(d) for d in t["dice"]) + "]"
    remaining = list(kept)
    parts = []
    for d in t["dice"]:
        if d in remaining:
            remaining.remove(d)
            parts.append(str(d))
        else:
            parts.append(f"({d})")  # dropped
    return "[" + ", ".join(parts) + "]"


def result_line(expr, res, who=None, why=None):
    dice_txt = " ".join(term_text(t) for t in res["terms"])
    for h in res.get("edge_trouble", []):
        dice_txt += f" {{reroll {h['die']}: {h['old']}→{h['new']}{' kept' if h['kept_new'] else ' discarded'}}}"
    mod = res.get("modifier", 0)
    mod_txt = f" {'+' if mod >= 0 else '-'} {abs(mod)}" if mod else ""
    label = "successes" if res["kind"] == "pool" else ""
    head = "🎲 " + ", ".join(x for x in (who, why) if x)
    head = head + ": " if head.strip() != "🎲" else "🎲 "
    line = f"{head}{expr} → {dice_txt}{mod_txt} = {res['total']}{(' ' + label) if label else ''}"
    if res.get("target"):
        t = res["target"]
        cmp_txt = "≤" if t["type"] == "under" else "vs"
        tname = "" if t["type"] == "under" else f"{t['type']} "
        line += f" {cmp_txt} {tname}{t['value']}"
    if res.get("outcome"):
        mark = {"success": "✔", "failure": "✖", "full success": "✔", "critical": "✔✔",
                "partial success": "◐", "miss": "✖"}.get(res["outcome"], "")
        line += f" {mark} {res['outcome']}"
    if res.get("note"):
        line += f" ({res['note']})"
    return line


def main(argv=None):
    p = argparse.ArgumentParser(description="Honest, logged dice for AI game masters.")
    p.add_argument("expr", help="dice expression, e.g. 1d20+5, 5d6>=4, pbta+2, d616+3")
    for name in ("dc", "ac", "tn", "ob", "under", "crit"):
        p.add_argument(f"--{name}", type=int)
    p.add_argument("--edge", type=int, default=0)
    p.add_argument("--trouble", type=int, default=0)
    p.add_argument("--record", help="comma-separated values from a player's physical roll")
    p.add_argument("--who")
    p.add_argument("--why")
    p.add_argument("--session", type=int)
    p.add_argument("--log")
    p.add_argument("--hidden", action="store_true")
    p.add_argument("--fudged", action="store_true", help="only if the table allowed fudging (Tenet 5)")
    p.add_argument("--seed", type=int)
    p.add_argument("--times", type=int, default=1)
    p.add_argument("--json", action="store_true")
    args = p.parse_args(argv)

    recorded = None
    if args.record:
        try:
            recorded = [int(x) for x in re.split(r"[,\s]+", args.record.strip()) if x]
        except ValueError:
            print("roll.py: --record takes comma-separated integers", file=sys.stderr)
            return 2
    dice = Dice(seed=args.seed, recorded=recorded)
    source = "player" if recorded is not None else "tools/roll.py"
    outputs = []
    try:
        for _ in range(max(1, args.times)):
            res = judge(evaluate(args.expr, dice, args.edge, args.trouble), args)
            outputs.append(res)
        if recorded is not None and dice.recorded:
            raise RollError(f"--record has {len(dice.recorded)} unused value(s)")
    except RollError as exc:
        print(f"roll.py: {exc}", file=sys.stderr)
        return 2

    for res in outputs:
        entry = {
            "ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "session": args.session, "who": args.who, "why": args.why, "expr": args.expr,
            "dice": [d for t in res["terms"] for d in t["dice"]], "total": res["total"],
            "target": res["target"]["value"] if res.get("target") else None,
            "outcome": res.get("outcome"), "note": res.get("note"), "source": source,
            "hidden": args.hidden, "fudged": args.fudged,
        }
        if args.seed is not None:
            entry["seed"] = args.seed
        if args.log:
            with open(args.log, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
        if args.json:
            print(json.dumps({**res, "log": entry}, ensure_ascii=False))
        else:
            print(result_line(args.expr, res, args.who, args.why))
    return 0


if __name__ == "__main__":
    sys.exit(main())

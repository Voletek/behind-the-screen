#!/usr/bin/env python3
"""
character.py - player-owned character sheets (standard library only).

Implements the checkable parts of core/methodology/character-creation.md.

Commands
  new     Create a sheet (characters/<id>.md) and a state.json party entry from the system profile.
            python3 tools/character.py new --campaign campaigns/<id> --id lyra --name "Lyra" --player Kira
              [--concept "..."] [--stat DEX=17 --stat WIS=14 ...] [--method point_buy] [--force]
  check   Check one or all PCs: stat names and ranges vs the profile, the creation method
          (standard array / point buy / spreads), and that the sheet's ## Stats match state.json.
            python3 tools/character.py check --campaign campaigns/<id> [--id lyra]
  show    Print a compact summary of a PC for chat.
            python3 tools/character.py show --campaign campaigns/<id> --id lyra
  methods List the creation methods the system profile knows.
            python3 tools/character.py methods --system dnd-5e

Random methods are rolled by the PLAYER, with tools/roll.py or their own dice, e.g.
  python3 tools/roll.py "4d6dl1" --times 6 --who Kira --why "ability scores"

Exit code 1 if `check` finds a FAIL, else 0.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import campaignlib as cl  # noqa: E402

SHEET_SECTIONS = ["Concept", "Stats", "Abilities", "Gear", "Story", "Look and Voice", "Changes"]


def load_state(folder):
    path = os.path.join(folder, "state.json")
    if not os.path.exists(path):
        raise SystemExit(f"character.py: no state.json in {folder} (run session zero / the builder first)")
    with open(path, encoding="utf-8") as fh:
        return path, json.load(fh)


def save_state(path, state):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def parse_stats(pairs):
    out = {}
    for p in pairs or []:
        m = re.fullmatch(r"\s*([^=]+?)\s*=\s*(-?\d+)\s*", p)
        if not m:
            raise SystemExit(f"character.py: --stat takes NAME=VALUE, got {p!r}")
        out[m.group(1)] = int(m.group(2))
    return out


def sheet_text(pc, profile, method):
    stats = pc.get("stats", {})
    lines = [f"# {pc['name']}",
             f"<!-- character: {pc['id']} · player: {pc.get('player', '')} · system: {profile['id'] if profile else '?'} -->",
             "",
             "> Player-owned sheet (core/methodology/character-creation.md). Live numbers (current HP,",
             "> conditions, inventory) live in state.json; this sheet is who the character is.",
             "",
             "## Concept",
             pc.get("concept") or "(one sentence, from the player)",
             "",
             "## Stats"]
    if method:
        lines.append(f"<!-- method: {method} -->")
    for name in (profile or {}).get("stats", list(stats)):
        val = stats.get(name)
        lines.append(f"- {name}: {'' if val is None else val}")
    lines += ["", "## Abilities", "(class / playbook / powers / skills / moves / traits)", "",
              "## Gear", "(starting gear within the system's limits)", "",
              "## Story", "- Goal: ", "- Bond: ", "- Flaw / fear: ", "",
              "## Look and Voice", "- Look: ", "- Voice: ", "",
              "## Changes", "| Date | Change | Why |", "|---|---|---|"]
    return "\n".join(lines) + "\n"


def sheet_stats(text):
    body = cl.section_body(text, "Stats") or ""
    out = {}
    for line in body.split("\n"):
        m = re.match(r"^\s*[-*]\s*([^:]+):\s*(-?\d+)\s*$", line)
        if m:
            out[m.group(1).strip()] = int(m.group(2))
    return out


def sheet_method(text):
    m = re.search(r"<!--\s*method:\s*([\w-]+)\s*-->", text)
    return m.group(1) if m else None


def check_method(method, stats, profile, report, where):
    methods = (profile.get("creation") or {}).get("methods", {})
    if not method:
        return
    if method not in methods:
        report.append(("WARN", where, f"method '{method}' is not one of {sorted(methods) or 'none listed'}"))
        return
    spec = methods[method]
    values = [stats[s] for s in profile["stats"] if s in stats]
    if "values" in spec:
        if sorted(values) != sorted(spec["values"]):
            report.append(("FAIL", where, f"{method}: stats {sorted(values)} are not the set {sorted(spec['values'])}"))
    elif "budget" in spec:
        costs = spec["costs"]
        bad = [v for v in values if str(v) not in costs]
        if bad:
            report.append(("FAIL", where, f"{method}: scores {bad} can't be bought (allowed {min(map(int, costs))}-{max(map(int, costs))})"))
        else:
            spent = sum(costs[str(v)] for v in values)
            if spent > spec["budget"]:
                report.append(("FAIL", where, f"{method}: spent {spent} of {spec['budget']} points"))
            elif spent < spec["budget"]:
                report.append(("WARN", where, f"{method}: {spec['budget'] - spent} point(s) unspent"))
    elif "expr" in spec:
        report.append(("PASS", where, f"{method}: random ({spec['expr']} × {spec['times']}), rolled by the player; check the dice log"))


def check_pc(folder, pc, profile, report):
    where = f"party[{pc.get('id', '?')}]"
    stats = pc.get("base_stats") or pc.get("stats") or {}
    if profile:
        lo, hi = profile.get("stat_range") or [None, None]
        missing = [s for s in profile["stats"] if s not in (pc.get("stats") or {})]
        if missing:
            report.append(("WARN", where, f"no value yet for {', '.join(missing)}"))
        for s, v in (pc.get("stats") or {}).items():
            if s not in profile["stats"]:
                report.append(("FAIL", where, f"'{s}' is not a {profile['id']} stat ({', '.join(profile['stats'])})"))
            elif isinstance(v, int) and lo is not None and not lo <= v <= hi:
                report.append(("FAIL", where, f"{s}={v} outside {lo}..{hi}"))
    for name, res in (pc.get("resources") or {}).items():
        if isinstance(res, dict) and isinstance(res.get("current"), int) and isinstance(res.get("max"), int) and res["current"] > res["max"]:
            report.append(("FAIL", where, f"{name}: current {res['current']} exceeds max {res['max']}"))
    sheet = pc.get("sheet")
    method = pc.get("stat_method")
    if sheet:
        path = os.path.join(folder, sheet)
        if not os.path.exists(path):
            report.append(("FAIL", where, f"sheet {sheet} not found"))
        else:
            text = cl.read_text(path)
            hs = [h.lower() for h in cl.headings(text)]
            for sec in SHEET_SECTIONS:
                if not any(h.startswith(sec.lower()) for h in hs):
                    report.append(("WARN", sheet, f"missing ## {sec}"))
            for s, v in sheet_stats(text).items():
                if (pc.get("stats") or {}).get(s) != v:
                    report.append(("FAIL", sheet, f"{s} is {v} on the sheet but {(pc.get('stats') or {}).get(s)} in state.json"))
            method = method or sheet_method(text)
    else:
        report.append(("WARN", where, "no sheet (run `character.py new` or add party[].sheet)"))
    if profile:
        check_method(method, stats, profile, report, where)


def cmd_new(args):
    folder = os.path.abspath(args.campaign)
    state_path, state = load_state(folder)
    profile = cl.load_profile(state.get("system"))
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.id):
        raise SystemExit("character.py: --id must be kebab-case (e.g. lyra, old-burr)")
    party = state.setdefault("party", [])
    existing = next((p for p in party if p.get("id") == args.id), None)
    if existing and not args.force:
        raise SystemExit(f"character.py: '{args.id}' already exists (use --force to rewrite the sheet)")
    stats = parse_stats(args.stat)
    if profile:
        unknown = [s for s in stats if s not in profile["stats"]]
        if unknown:
            raise SystemExit(f"character.py: unknown stat(s) {unknown}; {profile['id']} uses {profile['stats']}")
    sheet_rel = f"characters/{args.id}.md"
    pc = existing or {"id": args.id}
    pc.update({"name": args.name, "player": args.player or pc.get("player", ""),
               "concept": args.concept or pc.get("concept", ""), "sheet": sheet_rel})
    pc["stats"] = {**pc.get("stats", {}), **stats}
    if args.method:
        pc["stat_method"] = args.method
    pc.setdefault("resources", {r: {"current": 0, "max": 0}
                                for r in ((profile or {}).get("creation") or {}).get("starting_resources", [])})
    pc.setdefault("conditions", [])
    pc.setdefault("inventory", [])
    if not existing:
        party.append(pc)
    os.makedirs(os.path.join(folder, "characters"), exist_ok=True)
    with open(os.path.join(folder, sheet_rel), "w", encoding="utf-8") as fh:
        fh.write(sheet_text(pc, profile, args.method))
    save_state(state_path, state)
    print(f"Created {os.path.relpath(os.path.join(folder, sheet_rel))} and party[{args.id}] in state.json.")
    if not existing:
        print("Starting resources are 0/0: compute them with the player and update state.json.")
    return 0


def cmd_check(args):
    folder = os.path.abspath(args.campaign)
    _, state = load_state(folder)
    profile = cl.load_profile(state.get("system"))
    report = []
    pcs = [p for p in state.get("party", []) if not args.id or p.get("id") == args.id]
    if not pcs:
        report.append(("FAIL", "party", f"no character '{args.id}'" if args.id else "party is empty"))
    for pc in pcs:
        check_pc(folder, pc, profile, report)
    for level, where, msg in report:
        print(f"[{level}] {where}: {msg}")
    fails = sum(1 for r in report if r[0] == "FAIL")
    print(f"character check: {fails} FAIL, {sum(1 for r in report if r[0] == 'WARN')} WARN")
    return 1 if fails else 0


def cmd_show(args):
    folder = os.path.abspath(args.campaign)
    _, state = load_state(folder)
    pc = next((p for p in state.get("party", []) if p.get("id") == args.id), None)
    if not pc:
        raise SystemExit(f"character.py: no character '{args.id}'")
    stats = " ".join(f"{k} {v}" for k, v in (pc.get("stats") or {}).items())
    res = " · ".join(f"{k} {v.get('current')}/{v.get('max')}" for k, v in (pc.get("resources") or {}).items() if isinstance(v, dict))
    print(f"**{pc['name']}** ({pc.get('player', '')}) — {pc.get('concept', '')}")
    print(f"Stats: {stats or '-'}")
    print(f"Resources: {res or '-'}")
    print(f"Conditions: {', '.join(pc.get('conditions') or []) or 'none'}")
    print(f"Gear: {', '.join(pc.get('inventory') or []) or '-'}")
    return 0


def cmd_methods(args):
    profile = cl.load_profile(args.system)
    if not profile:
        raise SystemExit(f"character.py: no profile for {args.system!r}")
    creation = profile.get("creation") or {}
    print(f"{profile['name']} — stats: {', '.join(profile['stats'])}")
    for name, spec in creation.get("methods", {}).items():
        if "values" in spec:
            print(f"  {name}: assign {spec['values']}")
        elif "budget" in spec:
            print(f"  {name}: {spec['budget']} points; costs {spec['costs']}")
        elif "expr" in spec:
            print(f"  {name}: player rolls {spec['expr']} × {spec['times']}  (python3 tools/roll.py \"{spec['expr']}\" --times {spec['times']})")
    if creation.get("note"):
        print(f"  note: {creation['note']}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Player-owned character sheets.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("new")
    n.add_argument("--campaign", required=True)
    n.add_argument("--id", required=True)
    n.add_argument("--name", required=True)
    n.add_argument("--player")
    n.add_argument("--concept")
    n.add_argument("--stat", action="append", help="NAME=VALUE (repeatable)")
    n.add_argument("--method", help="creation method, e.g. standard_array, point_buy, random")
    n.add_argument("--force", action="store_true")
    c = sub.add_parser("check")
    c.add_argument("--campaign", required=True)
    c.add_argument("--id")
    s = sub.add_parser("show")
    s.add_argument("--campaign", required=True)
    s.add_argument("--id", required=True)
    m = sub.add_parser("methods")
    m.add_argument("--system", required=True)
    args = ap.parse_args(argv)
    return {"new": cmd_new, "check": cmd_check, "show": cmd_show, "methods": cmd_methods}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())

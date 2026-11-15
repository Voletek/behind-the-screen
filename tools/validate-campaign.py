#!/usr/bin/env python3
"""
validate-campaign.py - deterministic checks for campaign and one-shot files (standard library only).

Implements the checkable parts of core/methodology/state-keeping.md and campaign-continuity.md:

  state.json / Save Block   schema, required keys, unique ids, resource bounds, clock bounds,
                            NPC/thread statuses, stats/resources/conditions vs the system profile
  sessions/session-NN.md    the six required headings, empty Rulings, retired terms from the bible
  BIBLE.md                  required sections (Safety is mandatory), retired terms list
  ONESHOT.md                required sections (Safety is mandatory)
  dice-log.jsonl            every line parses, has ts/expr/total/source, source is known

Usage
  python3 tools/validate-campaign.py campaigns/<id>          # one campaign folder
  python3 tools/validate-campaign.py examples/campaigns/     # every campaign under a folder
  python3 tools/validate-campaign.py save-block.md           # a pasted Save Block
  python3 tools/validate-campaign.py --hook <changed-file>   # hook mode: validate the file's campaign
  Options: --json, --strict (WARN counts as failure)

Exit code 1 if any FAIL (or WARN with --strict), else 0. Hook mode always exits 0 and prints a report.
Files containing <!-- validate: skip --> in their first lines are skipped.
"""

import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import campaignlib as cl  # noqa: E402


class Report:
    def __init__(self):
        self.items = []

    def add(self, level, where, msg):
        self.items.append((level, where, msg))

    def fail(self, where, msg):
        self.add("FAIL", where, msg)

    def warn(self, where, msg):
        self.add("WARN", where, msg)

    def ok(self, where, msg):
        self.add("PASS", where, msg)

    def count(self, level):
        return sum(1 for i in self.items if i[0] == level)


def rel(path):
    try:
        return os.path.relpath(path)
    except ValueError:
        return path


# ---------------------------------------------------------------- state

def check_resources(rep, where, name, res, profile):
    if not isinstance(res, dict):
        rep.fail(where, f"resources: '{name}' must be an object like {{\"current\": n, \"max\": n}}")
        return
    cur, mx, lo = res.get("current"), res.get("max"), res.get("min", 0)
    if not isinstance(cur, int) or isinstance(cur, bool):
        rep.fail(where, f"resources.{name}.current must be an integer")
        return
    if mx is not None and (not isinstance(mx, int) or isinstance(mx, bool)):
        rep.fail(where, f"resources.{name}.max must be an integer")
        return
    if mx is not None and cur > mx:
        rep.fail(where, f"resources.{name}: current {cur} exceeds max {mx}")
    if isinstance(lo, int) and cur < lo:
        rep.fail(where, f"resources.{name}: current {cur} is below min {lo}")
    if profile and name not in profile.get("resources", []) and not profile.get("resources_open"):
        rep.warn(where, f"resource '{name}' is not a {profile['id']} resource")
    if profile and profile.get("id") == "dnd-5e" and name == "exhaustion" and cur > 6:
        rep.fail(where, "exhaustion above 6 (level 6 is death in 2024 rules)")


def check_character(rep, where, pc, profile):
    for key in ("id", "name"):
        if not pc.get(key):
            rep.fail(where, f"missing '{key}'")
    stats = pc.get("stats", {})
    if not isinstance(stats, dict):
        rep.fail(where, "stats must be an object")
        stats = {}
    if profile:
        known = set(profile.get("stats", []))
        lo, hi = (profile.get("stat_range") or [None, None])
        for s, v in stats.items():
            if s not in known:
                rep.warn(where, f"stat '{s}' is not a {profile['id']} stat ({', '.join(sorted(known))})")
            elif isinstance(v, (int, float)) and lo is not None and not lo <= v <= hi:
                rep.warn(where, f"stat {s}={v} outside the usual range {lo}..{hi}")
    for name, res in (pc.get("resources") or {}).items():
        check_resources(rep, where, name, res, profile)
    conds = pc.get("conditions", [])
    if not isinstance(conds, list):
        rep.fail(where, "conditions must be a list")
        conds = []
    if profile and profile.get("conditions") and not profile.get("conditions_open"):
        allowed = {c.lower() for c in profile["conditions"]}
        for c in conds:
            base = re.sub(r"\s*\(.*\)$|\s+\d+$", "", str(c)).strip().lower()
            if base not in allowed:
                rep.warn(where, f"condition '{c}' is not a {profile['id']} condition")
    if "inventory" in pc and not isinstance(pc["inventory"], list):
        rep.fail(where, "inventory must be a list")


def check_unique(rep, where, items, label):
    seen = set()
    for it in items:
        if not isinstance(it, dict):
            rep.fail(where, f"{label}: every entry must be an object")
            continue
        iid = it.get("id")
        if not iid:
            rep.fail(where, f"{label}: entry without an id ({it.get('name', '?')})")
        elif iid in seen:
            rep.fail(where, f"{label}: duplicate id '{iid}'")
        seen.add(iid)


def check_state(rep, where, state, root=cl.ROOT):
    if not isinstance(state, dict):
        rep.fail(where, "state must be a JSON object")
        return None
    if state.get("schema") != cl.STATE_SCHEMA:
        rep.fail(where, f"schema must be \"{cl.STATE_SCHEMA}\" (got {state.get('schema')!r})")
    for key, typ in (("campaign", str), ("system", str), ("session", int), ("party", list)):
        if not isinstance(state.get(key), typ) or isinstance(state.get(key), bool):
            rep.fail(where, f"'{key}' is required ({typ.__name__})")
    if isinstance(state.get("session"), int) and state["session"] < 0:
        rep.fail(where, "session must be >= 0")
    profile = cl.load_profile(state.get("system"), root)
    if state.get("system") and profile is None:
        rep.warn(where, f"no profile for system '{state.get('system')}' in systems/ (stats not checked)")
    party = state.get("party") or []
    if isinstance(party, list) and not party:
        rep.fail(where, "party is empty")
    for key in ("party", "npcs", "factions", "clocks", "threads"):
        val = state.get(key, [])
        if not isinstance(val, list):
            rep.fail(where, f"'{key}' must be a list")
            state[key] = []
        else:
            check_unique(rep, where, val, key)
    for pc in state.get("party", []):
        if isinstance(pc, dict):
            check_character(rep, f"{where} party[{pc.get('id', '?')}]", pc, profile)
    for npc in state.get("npcs", []):
        if not isinstance(npc, dict):
            continue
        w = f"{where} npcs[{npc.get('id', '?')}]"
        if not npc.get("name"):
            rep.fail(w, "missing 'name'")
        st = npc.get("status", "alive")
        if st not in cl.NPC_STATUSES:
            rep.fail(w, f"status '{st}' not in {sorted(cl.NPC_STATUSES)}")
        disp = npc.get("disposition")
        if disp is not None and disp not in cl.DISPOSITIONS:
            rep.warn(w, f"disposition '{disp}' not in {sorted(cl.DISPOSITIONS)}")
        for name, res in (npc.get("resources") or {}).items():
            check_resources(rep, w, name, res, None)
        sheet = npc.get("sheet")
        if sheet and not os.path.exists(os.path.join(os.path.dirname(where) if os.path.isfile(where) else where, sheet)):
            rep.warn(w, f"sheet '{sheet}' not found next to the state file")
    for clock in state.get("clocks", []):
        if not isinstance(clock, dict):
            continue
        w = f"{where} clocks[{clock.get('id', '?')}]"
        seg, filled = clock.get("segments"), clock.get("filled")
        if not isinstance(seg, int) or seg < 1:
            rep.fail(w, "segments must be a positive integer")
        elif not isinstance(filled, int) or not 0 <= filled <= seg:
            rep.fail(w, f"filled must be an integer between 0 and {seg}")
    for th in state.get("threads", []):
        if not isinstance(th, dict):
            continue
        w = f"{where} threads[{th.get('id', '?')}]"
        if not th.get("summary"):
            rep.fail(w, "missing 'summary'")
        if th.get("status", "open") not in cl.THREAD_STATUSES:
            rep.fail(w, f"status '{th.get('status')}' not in {sorted(cl.THREAD_STATUSES)}")
    return profile


# ---------------------------------------------------------------- documents

def check_session_log(rep, path, retired):
    text = cl.read_text(path)
    if cl.has_skip_marker(text):
        return
    where = rel(path)
    hs = [h.lower() for h in cl.headings(text)]
    missing = [h for h in cl.REQUIRED_SESSION_HEADINGS if not any(x.startswith(h.lower()) for x in hs)]
    if missing:
        rep.fail(where, "missing required heading(s): " + ", ".join(f"## {m}" for m in missing))
    rulings = cl.section_body(text, "Rulings")
    if rulings is not None and not rulings.strip():
        rep.warn(where, "## Rulings is empty (write 'None' if there were none)")
    check_retired(rep, where, text, retired)


def check_retired(rep, where, text, retired):
    clean = re.sub(r"```.*?```", "", text, flags=re.S)
    for old, new in retired:
        if re.search(r"(?<!\w)" + re.escape(old) + r"(?!\w)", clean, re.I):
            rep.warn(where, f"retired term '{old}' used (canon name: '{new}')")


def check_bible(rep, path):
    text = cl.read_text(path)
    if cl.has_skip_marker(text):
        return []
    where = rel(path)
    hs = [h.lower() for h in cl.headings(text)]
    for sec in cl.BIBLE_SECTIONS:
        if not any(h.startswith(sec.lower()) for h in hs):
            if sec == "Safety":
                rep.fail(where, "missing ## Safety (Tenet 1: never optional)")
            elif sec in cl.BIBLE_EARLY_OPTIONAL:
                continue
            else:
                rep.warn(where, f"missing ## {sec}")
    safety = cl.section_body(text, "Safety")
    if safety is not None and not re.search(r"\blines?\b", safety, re.I):
        rep.warn(where, "## Safety does not mention lines")
    return cl.retired_terms(text)


def check_oneshot(rep, path):
    text = cl.read_text(path)
    if cl.has_skip_marker(text):
        return
    where = rel(path)
    hs = [h.lower() for h in cl.headings(text)]
    for sec in cl.ONESHOT_SECTIONS:
        if not any(h.startswith(sec.lower()) for h in hs):
            (rep.fail if sec == "Safety" else rep.warn)(where, f"missing ## {sec}")


def check_dice_log(rep, path):
    where = rel(path)
    with open(path, encoding="utf-8") as fh:
        for no, line in enumerate(fh, 1):
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except ValueError as exc:
                rep.fail(f"{where}:{no}", f"invalid JSON: {exc}")
                continue
            for key in ("ts", "expr", "total", "source"):
                if key not in entry:
                    rep.fail(f"{where}:{no}", f"missing '{key}'")
            if entry.get("source") not in cl.DICE_SOURCES:
                rep.fail(f"{where}:{no}", f"unknown source {entry.get('source')!r} (Tenet 5: say where randomness came from)")


# ---------------------------------------------------------------- folders

def validate_folder(rep, folder):
    folder = os.path.abspath(folder)
    fails_before = rep.count("FAIL")
    retired = []
    bible = os.path.join(folder, "BIBLE.md")
    oneshot = os.path.join(folder, "ONESHOT.md")
    state_path = os.path.join(folder, "state.json")
    if os.path.exists(bible):
        retired = check_bible(rep, bible)
    if os.path.exists(oneshot):
        check_oneshot(rep, oneshot)
    if not os.path.exists(bible) and not os.path.exists(oneshot):
        rep.warn(rel(folder), "no BIBLE.md or ONESHOT.md")
    state = None
    if os.path.exists(state_path):
        state, err = cl.load_state(state_path)
        if err:
            rep.fail(rel(state_path), err)
        else:
            check_state(rep, rel(state_path), state)
    else:
        rep.fail(rel(folder), "no state.json")
    logs = sorted(glob.glob(os.path.join(folder, "sessions", "*.md")))
    logs = [p for p in logs if os.path.basename(p).lower() != "readme.md"]
    for p in logs:
        check_session_log(rep, p, retired)
    nums = [n for n in (cl.session_number(p) for p in logs) if n is not None]
    if state and isinstance(state.get("session"), int) and nums and max(nums) != state["session"]:
        rep.warn(rel(state_path), f"state.session is {state['session']} but the latest log is session-{max(nums):02d}")
    for p in sorted(glob.glob(os.path.join(folder, "npcs", "*.md"))):
        check_retired(rep, rel(p), cl.read_text(p), retired)
    dice = os.path.join(folder, "dice-log.jsonl")
    if os.path.exists(dice):
        check_dice_log(rep, dice)
    if rep.count("FAIL") == fails_before:
        rep.ok(rel(folder), "campaign files valid")


def discover(paths):
    """Expand directories into campaign/one-shot folders and stand-alone files."""
    targets = []
    for p in paths:
        if os.path.isdir(p):
            if os.path.exists(os.path.join(p, "state.json")) or os.path.exists(os.path.join(p, "ONESHOT.md")):
                targets.append(("folder", p))
                continue
            found = False
            for dirpath, dirnames, filenames in os.walk(p):
                dirnames[:] = sorted(d for d in dirnames if not d.startswith("."))
                if "state.json" in filenames or "ONESHOT.md" in filenames:
                    targets.append(("folder", dirpath))
                    dirnames[:] = []
                    found = True
            if not found:
                targets.append(("empty", p))
        elif p.endswith(".md") or p.endswith(".json") or p.endswith(".jsonl"):
            targets.append(("file", p))
        else:
            targets.append(("missing", p))
    return targets


def validate_file(rep, path):
    if not os.path.exists(path):
        rep.fail(rel(path), "file not found")
        return
    if path.endswith(".jsonl"):
        check_dice_log(rep, path)
        return
    if path.endswith(".json"):
        state, err = cl.load_state(path)
        if err:
            rep.fail(rel(path), err)
        else:
            check_state(rep, rel(path), state)
        return
    text = cl.read_text(path)
    if cl.has_skip_marker(text):
        return
    if cl.SAVE_BLOCK_START in text:
        state, err = cl.extract_save_block_json(text)
        if err:
            rep.fail(rel(path), err)
        else:
            check_state(rep, rel(path), state)
        return
    base = os.path.basename(path)
    if base == "BIBLE.md":
        check_bible(rep, path)
    elif base == "ONESHOT.md":
        check_oneshot(rep, path)
    elif cl.session_number(base) is not None and "/sessions/" in path.replace("\\", "/"):
        root = cl.find_campaign_root(path)
        retired = []
        if root and os.path.exists(os.path.join(root, "BIBLE.md")):
            retired = cl.retired_terms(cl.read_text(os.path.join(root, "BIBLE.md")))
        check_session_log(rep, path, retired)
    else:
        rep.warn(rel(path), "not a recognised campaign file (state.json, BIBLE.md, ONESHOT.md, session log, Save Block)")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Validate campaign / one-shot files.")
    ap.add_argument("paths", nargs="*", default=["campaigns"])
    ap.add_argument("--hook", metavar="FILE", help="hook mode: validate the campaign that contains FILE")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args(argv)
    rep = Report()

    if args.hook:
        name = os.path.basename(args.hook).lower()
        if name == "readme.md" or name.endswith(".prep.md") or name.endswith(".review.md"):
            return 0
        root = cl.find_campaign_root(args.hook)
        if root:
            validate_folder(rep, root)
        else:
            validate_file(rep, args.hook)
    else:
        for kind, p in discover(args.paths):
            if kind == "folder":
                validate_folder(rep, p)
            elif kind == "file":
                validate_file(rep, p)
            elif kind == "empty":
                rep.ok(rel(p), "no campaigns found (nothing to check)")
            else:
                rep.fail(rel(p), "path not found")

    if args.json:
        print(json.dumps([{"level": l, "where": w, "message": m} for l, w, m in rep.items], indent=2))
    else:
        for level, where, msg in rep.items:
            if args.hook and level == "PASS":
                continue
            print(f"[{level}] {where}: {msg}")
        print(f"validate-campaign: {rep.count('FAIL')} FAIL, {rep.count('WARN')} WARN")
    if args.hook:
        return 0
    if rep.count("FAIL") or (args.strict and rep.count("WARN")):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

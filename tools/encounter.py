#!/usr/bin/env python3
"""
encounter.py - combat encounter difficulty for fifth-edition (SRD 5.2.1) games.

Implements "Combat Encounter Difficulty" from the SRD 5.2.1 (CC-BY-4.0, Wizards of the Coast):
budget = XP Budget per Character (by level, Low/Moderate/High) summed over the party; spend it on
creatures by their XP value (from Challenge Rating).

Usage
  python3 tools/encounter.py --party 4x3 --creatures "cr3,cr1/4x6"
  python3 tools/encounter.py --party 3,3,4,5 --creatures "xp700,cr1x2"
  python3 tools/encounter.py --party 5x5 --budget          # show budgets only
  Options: --json

Party: "<count>x<level>" or a comma list of levels.
Creatures: comma list of "cr<CR>[x<count>]" or "xp<value>[x<count>]". CR may be 0, 1/8, 1/4, 1/2, 1-30.

Other systems have no published budget math; see core/methodology/encounter-design.md (threat ladder).
"""

import argparse
import json
import re
import sys

# XP Budget per Character [SRD 5.2.1]
BUDGET = {
    1: (50, 75, 100), 2: (100, 150, 200), 3: (150, 225, 400), 4: (250, 375, 500),
    5: (500, 750, 1100), 6: (600, 1000, 1400), 7: (750, 1300, 1700), 8: (1000, 1700, 2100),
    9: (1300, 2000, 2600), 10: (1600, 2300, 3100), 11: (1900, 2900, 4100), 12: (2200, 3700, 4700),
    13: (2600, 4200, 5400), 14: (2900, 4900, 6200), 15: (3300, 5400, 7800), 16: (3800, 6100, 9800),
    17: (4500, 7200, 11700), 18: (5000, 8700, 14200), 19: (5500, 10700, 17200), 20: (6400, 13200, 22000),
}

# Experience Points by Challenge Rating [SRD 5.2.1] (CR 0 is 0 or 10; 10 is used here)
XP_BY_CR = {
    "0": 10, "1/8": 25, "1/4": 50, "1/2": 100, "1": 200, "2": 450, "3": 700, "4": 1100, "5": 1800,
    "6": 2300, "7": 2900, "8": 3900, "9": 5000, "10": 5900, "11": 7200, "12": 8400, "13": 10000,
    "14": 11500, "15": 13000, "16": 15000, "17": 18000, "18": 20000, "19": 22000, "20": 25000,
    "21": 33000, "22": 41000, "23": 50000, "24": 62000, "25": 75000, "26": 90000, "27": 105000,
    "28": 120000, "29": 135000, "30": 155000,
}

LEVELS = ("Low", "Moderate", "High")


def parse_party(text):
    text = text.strip().lower()
    m = re.fullmatch(r"(\d+)x(\d+)", text)
    levels = [int(m.group(2))] * int(m.group(1)) if m else [int(x) for x in re.split(r"[,\s]+", text) if x]
    for lv in levels:
        if lv not in BUDGET:
            raise ValueError(f"character level {lv} is outside 1-20")
    if not levels:
        raise ValueError("party is empty")
    return levels


def parse_creatures(text):
    out = []
    for raw in [x for x in re.split(r"[,;]\s*", text.strip()) if x]:
        m = re.fullmatch(r"(cr|xp)\s*([\d/]+)(?:\s*x\s*(\d+))?", raw.strip().lower())
        if not m:
            raise ValueError(f"cannot parse creature {raw!r} (use cr3, cr1/4x6, xp700)")
        kind, val, count = m.group(1), m.group(2), int(m.group(3) or 1)
        if kind == "cr":
            if val not in XP_BY_CR:
                raise ValueError(f"unknown CR {val}")
            xp = XP_BY_CR[val]
        else:
            xp = int(val)
        out.append({"label": raw.strip(), "xp_each": xp, "count": count, "xp": xp * count})
    return out


def budgets(levels):
    return {name: sum(BUDGET[lv][i] for lv in levels) for i, name in enumerate(LEVELS)}


def rate(spent, b):
    if spent == 0:
        return "None"
    if spent <= b["Low"]:
        return "Low"
    if spent <= b["Moderate"]:
        return "Moderate"
    if spent <= b["High"]:
        return "High"
    return "Above High (beyond the SRD's guidance: telegraph it and give an exit)"


def main(argv=None):
    ap = argparse.ArgumentParser(description="SRD 5.2.1 encounter XP budget calculator.")
    ap.add_argument("--party", required=True, help='"4x3" or "3,3,4,5"')
    ap.add_argument("--creatures", default="", help='"cr3,cr1/4x6,xp200"')
    ap.add_argument("--budget", action="store_true", help="show budgets only")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    try:
        levels = parse_party(args.party)
        creatures = [] if args.budget else parse_creatures(args.creatures)
    except ValueError as exc:
        print(f"encounter.py: {exc}", file=sys.stderr)
        return 2
    b = budgets(levels)
    spent = sum(c["xp"] for c in creatures)
    result = {"party": levels, "budgets": b, "creatures": creatures, "spent": spent,
              "difficulty": rate(spent, b) if creatures else None,
              "source": "SRD 5.2.1 Combat Encounter Difficulty (CC-BY-4.0)"}
    if args.json:
        print(json.dumps(result, indent=2))
        return 0
    print(f"Party: {len(levels)} character(s), levels {', '.join(map(str, levels))}")
    print("Budget: " + " · ".join(f"{k} {v:,} XP" for k, v in b.items()))
    if creatures:
        for c in creatures:
            print(f"  {c['label']:<12} {c['count']} × {c['xp_each']:,} = {c['xp']:,} XP")
        print(f"Spent: {spent:,} XP → difficulty: {result['difficulty']}")
        print("Source: SRD 5.2.1 (CC-BY-4.0). Check creatures' goals, terrain and exits too (encounter-design.md).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

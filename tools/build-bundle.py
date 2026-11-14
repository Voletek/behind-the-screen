#!/usr/bin/env python3
"""
build-bundle.py - assemble one paste-able Markdown file for any AI assistant (standard library only).

The bundle is how non-Kiro assistants (Claude, ChatGPT, Gemini, local models, Discord bots) get the
method: upload it to a project/custom GPT, or paste it as the first message.

Contents, in order:
  1. portable/BOOT_PROMPT.md           the GM instructions and output contract
  2. core/tenets.md                    priorities
  3. core/methodology/running-the-game.md, adjudication.md, state-keeping.md
  4. core/methodology/session-zero.md  (only when no campaign/one-shot is given)
  5. core/methodology/npc-voice.md, encounter-design.md         (skipped with --lean)
  6. references/AI_GM_FAILURE_MODES.md, SAFETY_TOOLS_REFERENCE.md (skipped with --lean)
  7. systems/<id>/PROFILE.md
  8. table preferences (portable/TABLE_PREFERENCES.md or --prefs FILE)
  9. campaign: BIBLE.md, state.json, latest prep, last N session logs, NPC sheets (--lean: no sheets)
     or one-shot: ONESHOT.md, state.json

Usage
  python3 tools/build-bundle.py --system dnd-5e --campaign examples/campaigns/fractured-shadows -o bundle.md
  python3 tools/build-bundle.py --system root --oneshot examples/oneshots/the-ferryman-of-hundred-reeds --mode group
  python3 tools/build-bundle.py --list
  Options: --mode solo|group, --lean, --sessions N (default 2), --budget CHARS, --prefs FILE
"""

import argparse
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import campaignlib as cl  # noqa: E402

ROOT = cl.ROOT


def part(title, path):
    full = path if os.path.isabs(path) else os.path.join(ROOT, path)
    text = cl.read_text(full).strip()
    return f"\n\n<!-- ===== {title} · {os.path.relpath(full, ROOT)} ===== -->\n\n{text}\n"


def build(args):
    parts = [part("BOOT PROMPT", "portable/BOOT_PROMPT.md")]
    mode_note = ("\n\n> **Play mode for this bundle: GROUP.** Several players share this chat. Use the group "
                 "conventions in running-the-game.md (named prompts, `**Name (Character):**` posts, spotlight tracking).\n"
                 if args.mode == "group" else
                 "\n\n> **Play mode for this bundle: SOLO.** One player. Companions support, never decide.\n")
    parts.append(mode_note)
    parts.append(part("TENETS", "core/tenets.md"))
    for name in ("running-the-game", "adjudication", "state-keeping"):
        parts.append(part(f"METHOD: {name}", f"core/methodology/{name}.md"))
    if not args.campaign and not args.oneshot:
        parts.append(part("METHOD: session-zero", "core/methodology/session-zero.md"))
    if not args.lean:
        for name in ("npc-voice", "encounter-design"):
            parts.append(part(f"METHOD: {name}", f"core/methodology/{name}.md"))
        parts.append(part("REFERENCE: AI GM failure modes", "references/AI_GM_FAILURE_MODES.md"))
        parts.append(part("REFERENCE: safety tools", "references/SAFETY_TOOLS_REFERENCE.md"))

    system = args.system
    folder = args.campaign or args.oneshot
    if folder and not system:
        state, _ = cl.load_state(os.path.join(folder, "state.json"))
        system = (state or {}).get("system")
    if not system:
        raise SystemExit("build-bundle.py: give --system (or a campaign whose state.json names one)")
    prof = os.path.join(ROOT, "systems", system, "PROFILE.md")
    if not os.path.exists(prof):
        raise SystemExit(f"build-bundle.py: no profile systems/{system}/PROFILE.md (see --list)")
    parts.append(part(f"SYSTEM: {system}", prof))
    prefs = args.prefs or os.path.join(ROOT, "portable", "TABLE_PREFERENCES.md")
    if os.path.exists(prefs):
        parts.append(part("TABLE PREFERENCES", prefs))

    if args.campaign:
        c = os.path.abspath(args.campaign)
        parts.append(part("CAMPAIGN BIBLE", os.path.join(c, "BIBLE.md")))
        st = os.path.join(c, "state.json")
        parts.append(f"\n\n<!-- ===== CAMPAIGN STATE · state.json ===== -->\n\n```json\n{cl.read_text(st).strip()}\n```\n")
        preps = sorted(glob.glob(os.path.join(c, "prep", "*.md")))
        if preps:
            parts.append(part("LATEST PREP", preps[-1]))
        logs = sorted(p for p in glob.glob(os.path.join(c, "sessions", "*.md")) if cl.session_number(p) is not None)
        for p in logs[-args.sessions:] if args.sessions else []:
            parts.append(part("SESSION LOG", p))
        if not args.lean:
            for p in sorted(glob.glob(os.path.join(c, "npcs", "*.md"))):
                parts.append(part("NPC SHEET", p))
    elif args.oneshot:
        o = os.path.abspath(args.oneshot)
        parts.append(part("ONE-SHOT", os.path.join(o, "ONESHOT.md")))
        st = os.path.join(o, "state.json")
        if os.path.exists(st):
            parts.append(f"\n\n<!-- ===== ONE-SHOT STATE · state.json ===== -->\n\n```json\n{cl.read_text(st).strip()}\n```\n")

    parts.append("\n\n<!-- ===== END OF BUNDLE ===== -->\n\nBegin by following the START OF PLAY steps in the boot prompt.\n")
    return "".join(parts).lstrip()


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build a portable GM bundle for any AI assistant.")
    ap.add_argument("--system")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--campaign")
    g.add_argument("--oneshot")
    ap.add_argument("--mode", choices=["solo", "group"], default="solo")
    ap.add_argument("--lean", action="store_true")
    ap.add_argument("--sessions", type=int, default=2)
    ap.add_argument("--prefs")
    ap.add_argument("--budget", type=int, help="warn if the bundle exceeds this many characters")
    ap.add_argument("-o", "--output")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args(argv)

    if args.list:
        for sid in cl.list_systems():
            with open(os.path.join(ROOT, "systems", sid, "profile.json"), encoding="utf-8") as fh:
                print(f"{sid:<20} {json.load(fh).get('name')}")
        return 0
    text = build(args)
    chars = len(text)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(text)
    else:
        sys.stdout.write(text)
    msg = f"build-bundle: {chars:,} characters (~{chars // 4:,} tokens)"
    if args.budget and chars > args.budget:
        msg += f" — OVER budget {args.budget:,}; try --lean or --sessions 1"
    print(msg, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

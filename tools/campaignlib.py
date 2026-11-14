#!/usr/bin/env python3
"""
campaignlib.py - shared helpers for the campaign tools (standard library only).

Used by validate-campaign.py, build-bundle.py and encounter.py.
"""

import json
import os
import re

STATE_SCHEMA = "behind-the-screen/state@1"
SAVE_BLOCK_START = "=== SAVE BLOCK"
SAVE_BLOCK_END = "=== END SAVE BLOCK ==="

REQUIRED_SESSION_HEADINGS = [
    "Recap", "Scenes", "Rulings", "State Changes", "Open Threads", "Next Session",
]
OPTIONAL_SESSION_HEADINGS = ["Spotlight", "Canon Added", "Safety Notes"]

BIBLE_SECTIONS = [
    "Premise", "Tone", "Safety", "Table Settings", "House Rules", "Characters",
    "Setting Canon", "Factions and Fronts", "Arc Map", "Recurring Motifs",
    "Continuity Rules", "Canon Forks", "Campaign So Far", "Archive",
]
BIBLE_EARLY_OPTIONAL = {"Canon Forks", "Campaign So Far", "Archive"}

ONESHOT_SECTIONS = ["Pitch", "Safety", "Pregenerated Characters", "Strong Start", "Scenes", "Endings"]

NPC_STATUSES = {"alive", "dead", "missing", "captured", "departed", "unknown"}
DISPOSITIONS = {"hostile", "unfriendly", "wary", "indifferent", "neutral", "friendly",
                "helpful", "allied", "unknown"}
THREAD_STATUSES = {"open", "resolved", "abandoned", "dormant"}
DICE_SOURCES = {"tools/roll.py", "player", "code-interpreter", "dice-bot", "simulated"}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_text(path):
    with open(path, encoding="utf-8-sig") as fh:
        return fh.read()


def has_skip_marker(text):
    return "<!-- validate: skip -->" in text[:2000]


def load_profile(system_id, root=ROOT):
    """Return the profile.json dict for a system id, or None if unknown."""
    if not system_id or not re.match(r"^[a-z0-9][a-z0-9-]*$", str(system_id)):
        return None
    path = os.path.join(root, "systems", system_id, "profile.json")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def list_systems(root=ROOT):
    base = os.path.join(root, "systems")
    out = []
    for name in sorted(os.listdir(base)):
        if os.path.exists(os.path.join(base, name, "profile.json")):
            out.append(name)
    return out


def extract_save_block_json(text):
    """Find the ```json fenced block inside a Save Block. Returns (dict|None, error|None)."""
    start = text.find(SAVE_BLOCK_START)
    if start == -1:
        return None, "no '=== SAVE BLOCK' marker found"
    end = text.find(SAVE_BLOCK_END, start)
    block = text[start:end if end != -1 else len(text)]
    m = re.search(r"```json\s*\n(.*?)\n```", block, re.S)
    if not m:
        return None, "Save Block has no ```json fenced state"
    try:
        return json.loads(m.group(1)), None
    except ValueError as exc:
        return None, f"Save Block JSON does not parse: {exc}"


def load_state(path):
    """Load state from state.json or a Markdown Save Block. Returns (dict|None, error|None)."""
    text = read_text(path)
    if path.endswith(".md"):
        return extract_save_block_json(text)
    try:
        return json.loads(text), None
    except ValueError as exc:
        return None, f"invalid JSON: {exc}"


def headings(text, level=2):
    """Return the list of heading titles at the given level, ignoring fenced code."""
    out, in_fence = [], False
    prefix = "#" * level + " "
    for line in text.split("\n"):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if not in_fence and line.startswith(prefix):
            title = line[len(prefix):].strip()
            title = re.sub(r"^\d+[.)]\s*", "", title)  # allow "## 3. Safety"
            out.append(title)
    return out


def section_body(text, title, level=2):
    """Return the body text under a heading (until the next heading of the same or higher level)."""
    body, capturing, in_fence = [], False, False
    for line in text.split("\n"):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
        m = None if in_fence else re.match(r"^(#{1,6}) (.*)$", line)
        if m:
            hashes = len(m.group(1))
            name = re.sub(r"^\d+[.)]\s*", "", m.group(2).strip())
            if capturing and hashes <= level:
                break
            if not capturing and hashes == level and name.lower().startswith(title.lower()):
                capturing = True
                continue
        if capturing:
            body.append(line)
    return "\n".join(body).strip() if capturing else None


def retired_terms(bible_text):
    """Parse '## Retired Terms' bullets of the form '- Old Name → New Name' (or '->')."""
    body = section_body(bible_text, "Retired Terms")
    if not body:
        return []
    out = []
    for line in body.split("\n"):
        m = re.match(r"^\s*[-*]\s+(.+?)\s*(?:→|->)\s*(.+?)\s*$", line)
        if m:
            old = m.group(1).strip().strip("`*")
            new = m.group(2).strip().strip("`*")
            if old:
                out.append((old, new))
    return out


def find_campaign_root(path):
    """Walk up from a file to the folder that holds state.json (or ONESHOT.md)."""
    cur = os.path.abspath(path if os.path.isdir(path) else os.path.dirname(path))
    for _ in range(6):
        if os.path.exists(os.path.join(cur, "state.json")) or os.path.exists(os.path.join(cur, "ONESHOT.md")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent
    return None


def session_number(filename):
    m = re.search(r"session-(\d+)", os.path.basename(filename))
    return int(m.group(1)) if m else None

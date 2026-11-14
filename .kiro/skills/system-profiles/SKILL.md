---
name: system-profiles
description: Rules-system layer for AI game masters. Loads the profile for the RPG in play (D&D 5e via SRD 5.2.1, Mouse Guard, TMNT & Other Strangeness, Root, Marvel Multiverse, Rules-Light) with its dice, difficulty scale, stats, conditions, conflict procedure, GM procedures and AI GM pitfalls, and compares resolution families. Use when running, prepping or ruling in a specific system, choosing a system, or adding a new one.
---

# System Profiles Skill

1. Identify the system id from `state.json` (`system`) or ask the players.
2. Read `systems/<id>/PROFILE.md` before ruling or narrating mechanics (if not already in context).
3. For comparisons or choosing a system, read `references/SYSTEMS_COMPARISON.md`.
4. For an unsupported system, read `systems/PROFILE_TEMPLATE.md` and follow `core/methodology/builder.md` → "Add a System".
5. Roll with `tools/roll.py` using the profile's expressions.

---
inclusion: always
description: Honest dice and state-file rules for AI game masters - how to roll with tools/roll.py, log rolls, read and write state.json, write session logs with the six required headings, and validate campaign files.
---

# Dice and State — Always-On Rules

> Canonical method: `core/methodology/state-keeping.md`. Schema: `references/STATE_FORMAT_REFERENCE.md`.

## Dice (Tenet 5)

Roll every uncertain outcome with the tool and paste its line:

```bash
python3 tools/roll.py "1d20+5" --dc 15 --who Lyra --why "Stealth past the gate" --session 3 --log campaigns/<id>/dice-log.jsonl
python3 tools/roll.py "5d6>=4" --ob 3 --who Sorrel --why "Pathfinder across the bridge"   # Mouse Guard
python3 tools/roll.py "pbta+2" --who Tansy --why "Persuade an NPC"                       # Root / Rules-Light
python3 tools/roll.py "d616+3" --tn 15 --edge 1 --who Kestrel --why "Leap the gap"       # Marvel
python3 tools/roll.py "1d100" --under 45 --who Hex --why "Pick locks"                    # TMNT skills
python3 tools/roll.py "1d20+3" --record 14 --dc 12 --who Oona                            # log a player's physical roll
```

- Hidden rolls: add `--hidden`; still logged.
- Never invent a number. If no shell is available, ask the player to roll, or declare "simulated".

## State (Tenet 8)

- Read `campaigns/<id>/state.json`, `BIBLE.md` and the latest `sessions/session-NN.md` before play.
- Write `state.json` at every scene end and immediately for deaths, key items, NPC changes, filled
  clocks and resolved threads.
- Session log required headings: `## Recap`, `## Scenes`, `## Rulings`, `## State Changes`,
  `## Open Threads`, `## Next Session`.
- Validate: `python3 tools/validate-campaign.py campaigns/<id>` (hooks run it on save in Kiro IDE/CLI;
  on Kiro Web run it yourself).

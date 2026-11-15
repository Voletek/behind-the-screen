---
inclusion: always
description: Honest dice and state-file rules for AI game masters - how to roll with tools/roll.py, log rolls, read and write state.json, write session logs with the six required headings, and validate campaign files.
---

# Dice and State — Always-On Rules

> Canonical method: `core/methodology/state-keeping.md`. Schema: `references/STATE_FORMAT_REFERENCE.md`.

## Dice (Tenet 5)

**Player characters: the player rolls.** Post a request and wait:

```bash
python3 tools/roll.py "1d20+5" --request --who Lyra --why "Stealth" --dc 15 --stakes "someone may hear you"
# then log what they post:
python3 tools/roll.py "1d20+5" --record 14 --dc 15 --who Lyra --why "Stealth" --session 3 --log campaigns/<id>/dice-log.jsonl
python3 tools/roll.py "1d20+5" --total 19 --dc 15 --who Lyra --why "Stealth" --session 3 --log campaigns/<id>/dice-log.jsonl
```

Players can roll with physical dice, an app, a bot, or run `tools/roll.py` themselves. Roll for a PC
only if that player asks.

**The world: the GM rolls** with the tool and pastes the line:

```bash
python3 tools/roll.py "1d20+4" --ac 15 --who "Ghoul" --why "claws vs Lyra" --session 3 --log campaigns/<id>/dice-log.jsonl  # 5e monster
python3 tools/roll.py "4d6>=4" --who "Heron" --why "Nature vs the patrol"                # Mouse Guard animal
python3 tools/roll.py "d616+4" --tn 14 --who "Wattage" --why "punch vs Kestrel"           # Marvel villain
python3 tools/roll.py "1d20+2" --who "Gang thug" --why "strike vs Dozer"                  # TMNT
python3 tools/roll.py "1d12" --who GM --why "complication table"                          # any table
```

- Hidden rolls: add `--hidden`; still logged.
- Never invent a number. If no shell is available, ask a designated player to roll for the GM, or declare "simulated".

## State (Tenet 8)

- Read `campaigns/<id>/state.json`, `BIBLE.md` and the latest `sessions/session-NN.md` before play.
- Write `state.json` at every scene end and immediately for deaths, key items, NPC changes, filled
  clocks and resolved threads.
- Session log required headings: `## Recap`, `## Scenes`, `## Rulings`, `## State Changes`,
  `## Open Threads`, `## Next Session`.
- Validate: `python3 tools/validate-campaign.py campaigns/<id>` (hooks run it on save in Kiro IDE/CLI;
  on Kiro Web run it yourself).

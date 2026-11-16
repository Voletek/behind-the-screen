# Dice and State — Power Steering

```bash
python3 tools/roll.py "<expr>" --request --who <PC> --why "<what>" --stakes "<what they know>"   # ask the player to roll
python3 tools/roll.py "<expr>" --record "<faces>" | --total <n> [--dc N] --who <PC> --log campaigns/<id>/dice-log.jsonl  # log their roll
python3 tools/roll.py "<expr>" [--dc|--ac|--tn|--ob|--under N] --who <NPC> --why "<what>" --session <n> --log campaigns/<id>/dice-log.jsonl  # GM world roll
python3 tools/character.py new|check|show|methods …
python3 tools/validate-campaign.py campaigns/<id>
python3 tools/encounter.py --party 4x3 --creatures "cr3,cr1/4x4"
python3 tools/build-bundle.py --campaign campaigns/<id> -o bundle.md
```

- `state.json` is the truth (Tenet 8). Write it at every scene end.
- Session logs need `## Recap`, `## Scenes`, `## Rulings`, `## State Changes`, `## Open Threads`, `## Next Session`.
- Chat-only play: end each session with a Save Block containing the full state JSON.

# Dice and State — Power Steering

```bash
python3 tools/roll.py "<expr>" [--dc|--ac|--tn|--ob|--under N] --who <name> --why "<what>" --session <n> --log campaigns/<id>/dice-log.jsonl
python3 tools/validate-campaign.py campaigns/<id>
python3 tools/encounter.py --party 4x3 --creatures "cr3,cr1/4x4"
python3 tools/build-bundle.py --campaign campaigns/<id> -o bundle.md
```

- `state.json` is the truth (Tenet 8). Write it at every scene end.
- Session logs need `## Recap`, `## Scenes`, `## Rulings`, `## State Changes`, `## Open Threads`, `## Next Session`.
- Chat-only play: end each session with a Save Block containing the full state JSON.

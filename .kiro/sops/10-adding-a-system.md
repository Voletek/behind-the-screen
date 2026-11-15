# SOP 10: Adding a System

> Support an RPG that has no profile yet.
>
> **Canonical method:** `core/methodology/builder.md` → Add a System. This SOP is the step list; if they diverge, `core/` wins.
> **Agent:** builder · **Time:** 1-2 hrs

---

## Prerequisites

- Someone at the table owns the rulebook (for proprietary games)

## Procedure

1. Identify game, edition, publisher, licence.
2. Copy `systems/PROFILE_TEMPLATE.md` to `systems/<id>/PROFILE.md`.
3. Fill sections 1-11 in your own words (no rules text unless openly licensed).
4. Map core rolls to `tools/roll.py` expressions.
5. Write `profile.json` (stats, resources, conditions, dice mechanic).
6. Run `python3 tools/check-repo.py`.
7. Smoke-test with a 3-scene session; log it in `experiments/ai-gm/`.
8. Add the system to `systems/README.md` and the README tables.

## Done When

- [ ] check-repo passes · [ ] smoke session logged

# SOP 02: Running a Session

> Run a live session from recap to save, solo or group.
>
> **Canonical method:** `core/methodology/running-the-game.md`, `adjudication.md`, `state-keeping.md`. This SOP is the step list; if they diverge, `core/` wins.
> **Agent:** game-master · **Time:** 1-4 hrs

---

## Prerequisites

- Campaign files (or a one-shot) and the system profile
- Dice source agreed

## Procedure

1. **Load:** bible, state.json, last session log, latest prep, system profile. Validate.
2. **Confirm three facts** with the players (location, key resource/condition, main open question).
3. **Recap** in 3-5 bullets (group: a player recaps).
4. **Strong start:** open in motion.
5. **Loop each moment:** frame → ask a named player → listen → decide (roll?) → roll with `tools/roll.py` → narrate the change → record state.
6. **Scenes:** start late, leave early; alternate tension and release; spotlight check every 3-4 exchanges (group).
7. **Combat/conflict:** use the profile's procedure; compact tracker after each round; end when the outcome is clear.
8. **Safety:** honour any `X`/`/pause`/`/rewind` immediately.
9. **Climax:** cut to it if time runs short.
10. **Close:** wind-down beat → `/save-game` (SOP step list in `.kiro/steering/save-game.md`).

## Done When

- [ ] state.json updated and valid · [ ] session log with six headings · [ ] every roll in dice-log.jsonl

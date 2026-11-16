# SOP 01: Session Zero

> Choose the system, shape, tone and safety tools, make characters, and create the campaign files.
>
> **Canonical method:** `core/methodology/session-zero.md`. This SOP is the step list; if they diverge, `core/` wins.
> **Agent:** builder (or game-master for one-shots) · **Time:** 30-60 min (one-shot: 5-10 min)

---

## Prerequisites

- The players' system choice (or willingness to pick from `systems/`)
- All players present (group play)

## Procedure

1. **Mode:** ask guided or auto-pilot (default guided).
2. **The game:** system → load `systems/<id>/PROFILE.md`; no profile → SOP 10 or `rules-light`.
3. **The shape:** campaign or one-shot, solo or group, session length, absent-player rule, favourite pillars.
4. **Tone:** pick from `references/GENRE_TONE_LIBRARY.md`; touchstones; lethality; humour; romance.
5. **Safety (never skipped):** lines, veils, the `X` tool, check-ins (`references/SAFETY_TOOLS_REFERENCE.md`). Each player answers.
6. **Table settings:** players roll their own dice; GM dice source; hidden rolls; targets shown; hint level; fudging; narration length; menus; stakes; rebuilds; save format.
7. **Characters:** each player builds their own (SOP 13, `tools/character.py`); goal, bond, flaw from the player; connect PCs (group) or design companions (solo).
8. **Files:** `campaigns/<id>/BIBLE.md` (from `references/YOUR_CAMPAIGN_BIBLE.md`) and `state.json`.
9. **Validate:** `python3 tools/validate-campaign.py campaigns/<id>`.
10. **Hook:** agree why the PCs are together and where session 1 opens.

## Done When

- [ ] Bible sections 1-6 filled · [ ] state.json validates · [ ] every player stated lines/veils · [ ] first hook agreed

# SOP 13: Creating and Customizing a Character

> Players build and change their own characters; the GM explains, checks and records.
>
> **Canonical method:** `core/methodology/character-creation.md`. This SOP is the step list; if they diverge, `core/` wins.
> **Agent:** character-creator · **Time:** 10-30 min per character (fast mode: 5 min)

---

## Prerequisites

- Session zero agreed the system, allowed options and the rebuild rule
- The campaign folder exists with a `state.json`

## Procedure

1. **Methods:** `python3 tools/character.py methods --system <id>`; the player picks one.
2. **Concept** in one sentence, from the player.
3. **Role:** class / playbook / rank / power set; explain options, don't rank them.
4. **Stats:** the player assigns them, or rolls them with their own dice or `tools/roll.py "<expr>" --times N`.
5. **Abilities:** skills, moves, powers, traits the system grants.
6. **Resources:** compute with the player; show the arithmetic.
7. **Gear** within the starting limits.
8. **Story:** goal, bond, flaw/fear, from the player. Group: each player answers one connection question.
9. **Look and voice.**
10. **Files:** `python3 tools/character.py new --campaign <dir> --id <id> --name "<name>" --player <p> --method <m> --stat …`; fill the sheet.
11. **Check:** `python3 tools/character.py check --campaign <dir> --id <id>` and `python3 tools/validate-campaign.py <dir>`.
12. **Later changes:** `/level-up`; log every change under the sheet's `## Changes`.

## Done When

- [ ] Every choice was the player's · [ ] random dice rolled by the player · [ ] `character.py check` passes

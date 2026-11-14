# examples/ — Reference Implementations

> Worked examples of every file type. Your own work goes in `campaigns/` and `oneshots/` at the repo root.

| Folder | Contents |
|---|---|
| `campaigns/fractured-shadows/` | A full campaign adapted from Voletek's novels (*Fractured Shadows*, *Shattered Veil*), the *Eryndor World Codex* and the *Fractured Shadows* concept album: bible with open canon questions and retired terms, state, session log, dice log, prep, NPC sheets, review, Kiro steering and continuity hook |
| `oneshots/keeper-of-the-light/` | Folk horror lighthouse, `dnd-5e`, level 3, SRD creatures with XP budgets (from the *Keeper of the Light* album) |
| `oneshots/the-thaw-at-pinebrook/` | Spring flood mission, `mouse-guard` |
| `oneshots/the-ferryman-of-hundred-reeds/` | River clearing faction intrigue, `root` |
| `oneshots/shell-game/` | Missing mutagen in the storm drains, `tmnt` (original mutants) |
| `oneshots/blackout-protocol/` | Borough-wide blackout, `marvel-multiverse` (original heroes) |
| `sessions/` | Transcript excerpts: solo (Fractured Shadows) and group (Ferryman) |
| `preferences/` | A filled-in table preferences file |

Validate them all: `python3 tools/validate-campaign.py examples/`.

Build a bundle from one: `python3 tools/build-bundle.py --oneshot examples/oneshots/keeper-of-the-light --mode group -o keeper.md`.

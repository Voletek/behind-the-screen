---
inclusion: always
description: This table's formatting and play preferences for the AI game master - narration length, speaker tags, roll and mechanics display, status tracker, recaps, options, stakes, OOC handling. Customize for your table.
---

# Table Preferences (customize me)

> The personal layer, like songwriting-kb's output-preferences. Edit freely. A filled example:
> `examples/preferences/example-table-preferences.md`. Non-Kiro equivalent: `portable/TABLE_PREFERENCES.md`.

- **Narration length:** short-medium (3-6 sentences for a new scene, 1-3 when continuing).
- **Speaker tags:** NPC dialogue as `**Name:** "…"`.
- **Player rolls:** players roll their own dice. The GM posts a 🎲 roll request
  (`tools/roll.py … --request`) and waits for the result.
- **GM rolls:** shown with the 🎲 result line from `tools/roll.py`.
- **Targets (DC/TN):** revealed after the roll.
- **Hints:** only on `OOC: hint?` (hint ladder in `core/methodology/running-the-game.md`).
- **Mechanics:** in square brackets after the narration: `[Lyra −6 HP → 12/18]`.
- **Status tracker:** after each combat round and at scene end, one line:
  `Round 3 | Kael 14/22 | Lyra 9/18 (Poisoned) | Ghoul A bloodied`.
- **Recap:** 3-5 bullets at the start of each session.
- **Options:** never list numbered options unless asked (`OOC: options?`).
- **Stakes:** state what failure would cost before most rolls.
- **OOC:** answer `OOC:` messages briefly, then return to the scene.
- **Ending:** every GM message ends with a question or open situation for a named player.
- **Session end:** update files, then a 3-line summary of what was saved.

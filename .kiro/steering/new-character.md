---
inclusion: manual
description: Guide a player through building their own character for the current campaign or one-shot, step by step, with the player choosing and rolling. Invoke with /new-character or #new-character.
---

# New Character (manual command)

> Run with `/new-character` or `#new-character`. Canonical: `core/methodology/character-creation.md`.

1. Read the system profile → Characters; run `python3 tools/character.py methods --system <id>`.
2. Ask guided or fast mode. Guided: concept → role → stats (player rolls if random) → abilities →
   resources (show arithmetic) → gear → goal/bond/flaw → look and voice.
3. Explain options; never choose for the player unless asked.
4. `python3 tools/character.py new …`, fill the sheet, set resources, then `character.py check` and
   `validate-campaign.py`.

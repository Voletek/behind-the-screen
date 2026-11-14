---
inclusion: fileMatch
fileMatchPattern: "campaigns/fractured-shadows/**"
---

# Fractured Shadows — Campaign Steering (example)

> Copy to `.kiro/steering/fractured-shadows.md` (and the campaign to `campaigns/fractured-shadows/`)
> to load this only when the campaign's files are in context.

When running or prepping Fractured Shadows:

1. Read `campaigns/fractured-shadows/BIBLE.md` first: Safety, Table Settings, House Rules and the 12
   Continuity Rules apply to every scene.
2. **Never write the name "Draeven Vole"** in narration or NPC dialogue until
   `state.json → flags.name_draeven_confirmed` is `true` (Continuity Rule 1).
3. Every use of magic, the Mark or the Shard costs Strain or a described consequence (House Rules).
4. No gods answer, no game UI language in the fiction, no fast travel without severe cost.
5. Use canon names from the Codex; retired names are listed in the bible and flagged by
   `tools/validate-campaign.py`.
6. When book canon and table events diverge, log the fork in the bible §12. When sources disagree,
   use the table default in "Open Canon Questions" and never resolve them silently.
7. Advance the four fronts between sessions (bible §8).

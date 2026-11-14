---
inclusion: manual
description: End-of-session save - update state.json, write the session log with the six required headings, validate, and print a Save Block for non-file play. Invoke with /save-game or #save-game.
---

# Save Game (manual command)

> Run with `/save-game` or `#save-game`. Canonical: `core/methodology/state-keeping.md` →
> "End-of-Session Save" and "Save Blocks".

1. Update `campaigns/<id>/state.json`: increment `session`, set `location` and `in_world_date`, apply
   every resource, condition, inventory, NPC, clock and thread change from this session.
2. Write `campaigns/<id>/sessions/session-NN.md` with `## Recap`, `## Scenes`, `## Rulings`,
   `## State Changes`, `## Open Threads`, `## Next Session` (plus `## Spotlight`, `## Canon Added`,
   `## Safety Notes` when relevant).
3. Run `python3 tools/validate-campaign.py campaigns/<id>` and fix any FAIL.
4. If the players also use a chat-only assistant, print a Save Block containing the full `state.json`.
5. Tell the player in three lines what was saved and where play resumes.

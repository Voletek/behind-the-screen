# Setup: Claude (claude.ai)

> Setup notes for Anthropic's Claude apps. Interface names change; adjust to what you see.
> [Tier 3: community practice, re-check with each app update]

## Recommended: a Project per campaign

1. Create a **Project** named after the campaign.
2. Add the bundle (`tools/build-bundle.py` output) to the project's **knowledge/files**.
3. Paste the contents of `portable/BOOT_PROMPT.md` into the project's **custom instructions**, so it
   applies to every chat.
4. Start a new chat per session. First message: "New session. Here is the latest Save Block:" and
   paste it.
5. At the end, ask for the Save Block, save it locally, and replace the old one in the project files.

## Dice

- **Players roll their own dice** (physical, an app, or `tools/roll.py`) and post results; the GM
  sends a roll request and waits.
- For the GM's rolls (NPCs, monsters, tables): if code execution (the analysis tool) is enabled, ask
  the GM to roll with code and show the result. You can upload `tools/roll.py` to the project.
  Otherwise, tell the GM at session zero "One of us will roll for the NPCs too."

## Tips

- Long sessions: start a fresh chat at a natural break (end of a scene) with a Save Block, rather than
  pushing one chat until it degrades.
- If the GM starts puppeting your character, reply `OOC: please don't describe my character's
  feelings or choices.` It is Tenet 2 in the bundle; a reminder usually fixes it.

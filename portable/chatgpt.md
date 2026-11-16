# Setup: ChatGPT

> Setup notes for OpenAI's ChatGPT. Interface names change; adjust to what you see.
> [Tier 3: community practice, re-check with each app update]

## Option A: a Project per campaign

1. Create a **Project** for the campaign.
2. Upload the bundle and `tools/roll.py` as project files.
3. Put `portable/BOOT_PROMPT.md` in the project instructions.
4. New chat per session; paste the latest Save Block first.

## Option B: a custom GPT for your table

1. Create a GPT. Paste `portable/BOOT_PROMPT.md` into its instructions.
2. Upload the bundle (without campaign files) plus `tools/roll.py` as knowledge.
3. Enable **code interpreter**.
4. Each session: paste the campaign bible + Save Block, or upload them.

## Dice

**Players roll their own** (physical dice, an app, or `roll.py` on their own machine) and post the
result. The GM sends a roll request and waits.

For the GM's rolls (monsters, NPCs, tables), enable **code interpreter** and ask at session zero:
"Roll your own dice with Python and show the code result." The GM can run `roll.py` directly:

```
python roll.py "1d20+4" --ac 15 --who Ghoul --why "claws vs Lyra"
```

Check now and then that it really runs the code (you should see the code output). If a player wants
the GM to roll for their character, they say so.

## Tips

- The model's memory feature is not campaign state. Keep the Save Block as the source of truth
  (Tenet 8).
- Voice mode works for solo play; ask the GM to read roll results aloud and keep descriptions short.

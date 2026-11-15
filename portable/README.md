# portable/ — Running Behind the Screen in Any AI Assistant

> The method in `core/` works with any assistant (Tenet 9). This folder holds the boot prompt, the
> default table preferences, and setup notes per assistant. Kiro users don't need it: `.kiro/` wires
> everything automatically.

## Step 1 — Build a bundle

```bash
# New game (bundle includes session zero):
python3 tools/build-bundle.py --system dnd-5e -o my-bundle.md

# Ongoing campaign:
python3 tools/build-bundle.py --campaign campaigns/my-campaign -o my-bundle.md

# One-shot for a group:
python3 tools/build-bundle.py --oneshot examples/oneshots/the-ferryman-of-hundred-reeds --mode group -o ferryman.md

# Smaller bundle for tight context windows:
python3 tools/build-bundle.py --campaign campaigns/my-campaign --lean --sessions 1 -o my-bundle.md
```

No Python? Concatenate these files by hand, in order: `portable/BOOT_PROMPT.md`, `core/tenets.md`,
`core/methodology/running-the-game.md`, `adjudication.md`, `state-keeping.md`, (`session-zero.md`
for a new game), `systems/<id>/PROFILE.md`, `portable/TABLE_PREFERENCES.md`, then your campaign
bible, state and last session log.

Measured sizes: a new-game bundle with `--lean` is ~13-14k tokens; the full Fractured Shadows campaign bundle is ~25k tokens; a lean one-shot bundle ~15k tokens.

## Step 2 — Load it into your assistant

| Assistant | Best setup | Dice | Saving |
|---|---|---|---|
| **Claude** (claude.ai Projects) | [claude.md](claude.md) | Analysis tool / code, or players roll | Save Blocks; or project files |
| **ChatGPT** (Projects or a custom GPT) | [chatgpt.md](chatgpt.md) | Code interpreter (Python) | Save Blocks; or files via code interpreter |
| **Kiro** (IDE, CLI, Web) | The repo itself (see `.kiro/README.md`) | `tools/roll.py` | Campaign files + hooks |
| **Any other chat** (Gemini, local models, Discord bots) | [any-chat.md](any-chat.md) | Players roll | Save Blocks |

## Step 3 — Play, then save

At the end of each session the GM prints a Save Block. Copy it into a file, e.g.
`campaigns/my-campaign/saves/session-03.md`. Check it with
`python3 tools/validate-campaign.py campaigns/my-campaign/saves/session-03.md`. Next session, paste
the bundle, then the Save Block.

## Group play in a shared chat

- One person hosts the chat (or a Discord bot) and pastes the bundle with `--mode group`.
- Each player posts as `**Name (Character):** …`.
- Private actions: the platform needs a private channel; otherwise announce "secret action" and the
  GM resolves it vaguely in public.

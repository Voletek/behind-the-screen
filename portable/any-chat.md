# Setup: Any Other Chat Assistant

> For Gemini, local models (Ollama, LM Studio), Discord bots, and anything else that takes text.

## Minimum setup

1. Build a lean bundle: `python3 tools/build-bundle.py --system <id> --lean -o bundle.md`
   (or concatenate the files listed in `portable/README.md`).
2. Paste it as the first message (or system prompt, if the tool has one).
3. Paste your latest Save Block as the second message.
4. Say: "Begin with START OF PLAY."

## Small context windows (local models)

- Use `--lean --sessions 1`.
- Drop `encounter-design.md` and `npc-voice.md` (already dropped by `--lean`).
- Keep the state JSON compact: archive resolved threads and dead NPCs to the bible.
- Expect more failure modes (`references/AI_GM_FAILURE_MODES.md`): remind the model of the hard rules
  every few scenes, e.g. `OOC: reminder, keep it to 3-6 sentences and don't describe my character's
  feelings.`

## Dice without code

Players roll their own physical or app dice and report; the GM asks and waits. For GM rolls, choose one:
- A designated player rolls for the GM.
- A dice bot in the same channel (Discord), logged as `"source": "dice-bot"`.
- Declared simulation: the GM says "simulated roll" every time. Least fair; agree to it at session zero.

## Discord / group servers

- One channel for play, one for OOC.
- A bot or the host relays player messages in the `**Name (Character):** action` format.
- Run `tools/roll.py` on the host machine, or use the server's dice bot, and paste results.

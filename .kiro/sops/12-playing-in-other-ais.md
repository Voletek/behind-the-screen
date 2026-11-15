# SOP 12: Playing in Other AI Assistants

> Use the method in Claude, ChatGPT, Gemini, local models or Discord bots.
>
> **Canonical method:** `portable/README.md`, `core/methodology/state-keeping.md` → Save Blocks. This SOP is the step list; if they diverge, `core/` wins.
> **Agent:** builder · **Time:** 10 min setup

---

## Prerequisites

- Python 3 (for the bundle builder) or patience to concatenate files by hand

## Procedure

1. Build a bundle: `python3 tools/build-bundle.py [--system <id>] [--campaign <dir> | --oneshot <dir>] [--mode group] [--lean] -o bundle.md`.
2. Follow the setup page: `portable/claude.md`, `portable/chatgpt.md` or `portable/any-chat.md`.
3. Decide dice: code interpreter, player-rolled, dice bot, or declared simulation.
4. Play; at the end ask for the Save Block.
5. Save the Save Block to a file and check it: `python3 tools/validate-campaign.py <file>.md`.
6. Next session: bundle + Save Block.

## Done When

- [ ] Save Block validates

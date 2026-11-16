---
name: behind-the-screen
description: AI Game Master power - activates the full tabletop RPG game-mastering system for solo and group play in any supported system (D&D 5e via SRD 5.2.1, Mouse Guard, TMNT & Other Strangeness, Root, Marvel Multiverse, Rules-Light). Packages 8 agents, 6 skills, 13 SOPs, steering, hooks, honest dice and campaign-state tools.
keywords: ["dm", "gm", "dungeon master", "game master", "narrator", "rpg", "ttrpg", "tabletop", "roleplay", "role-play", "d&d", "dnd", "5e", "mouse guard", "tmnt", "root", "marvel", "one-shot", "oneshot", "campaign", "session", "session zero", "adventure", "dungeon", "quest", "encounter", "npc", "villain", "monster", "roll", "dice", "initiative", "combat", "lines and veils", "x-card", "prep", "recap", "save game", "make a character", "character creation", "level up", "roll stats", "continuity", "canon", "house rule", "ruling", "let's play", "be my dm", "run a game", "start a campaign", "continue the campaign"]
---

# 🎲 Behind the Screen Power

An AI Game Master system: system-neutral craft in `core/`, rules systems in `systems/`, honest dice and
campaign state in `tools/`, and Kiro wiring in `.kiro/`.

## Agents (8 thin wrappers — load core/methodology/)
| Agent | Role | Loads | Invoke When |
|---|---|---|---|
| **game-master** | Runs live sessions, solo or group | `running-the-game.md`, `adjudication.md`, `state-keeping.md` | "Be my DM" / "Continue the campaign" |
| **character-creator** | Players build and change their own characters | `character-creation.md` | "Make my character" / "Level up" |
| **session-planner** | Prepares sessions and one-shots (10-section brief) | `session-prep.md` | "Prep next session" |
| **rules-arbiter** | Rules questions, rulings, difficulty | `adjudication.md` + profile | "How does this rule work?" |
| **npc-designer** | NPCs, villains, companions | `npc-voice.md` | "Design a villain" |
| **continuity-keeper** | Canon, bible, fronts, forks | `campaign-continuity.md` | "Check continuity" |
| **session-critic** | Reviews sessions (12 + 6 rubric) | `session-review.md` | "How did the session go?" |
| **builder** | Campaigns, one-shots, new systems, bundles | `builder.md` | "Set up a campaign" / "Add a system" |

## Skills (6)
`system-profiles`, `character-creation`, `npc-voice`, `encounter-design`, `safety-tools`, `campaign-bible`.

## Steering
Always: `game-master.md`, `table-state.md`, `table-preferences.md`. Auto: `campaign.md`.
Manual: `/session-zero`, `/new-character`, `/level-up`, `/recap`, `/save-game`, `/quick-review`.

## Tools
`tools/roll.py` (dice: player-roll requests and logging, GM rolls), `tools/character.py` (sheets), `tools/validate-campaign.py` (state, logs, bible), `tools/encounter.py`
(SRD 5.2.1 budgets), `tools/build-bundle.py` (portable bundles), `tools/check-repo.py`.

## Power steering
- `steering/craft.md` — the GM craft in one page
- `steering/systems.md` — system quick reference
- `steering/dice-and-state.md` — tool commands

# .kiro/ — Kiro Automation Layer

> The Kiro adapter for the game-mastering method. The canonical method lives in `core/methodology/`;
> this directory wires it into Kiro's agents, skills, steering, hooks and SOPs. Agents are THIN: a
> persona plus `resources:` front matter that loads the method (e.g.
> `resources: ["file://core/methodology/running-the-game.md"]`).

---

## Architecture

```
core/methodology/  ← Source of truth (complete methods)
systems/           ← Rules layer (one profile per RPG)
       ↓
.kiro/agents/      ← Thin loaders (persona + resources: file://core/...)
.kiro/steering/    ← Quick-reference rules (always / auto / manual)
.kiro/skills/      ← On-demand knowledge (reads core/, systems/, references/ by path)
.kiro/hooks/       ← Kiro v1 JSON hooks that run tools/validate-campaign.py on campaign saves
.kiro/sops/        ← Step lists (point to core/ as canonical)
.kiro/powers/      ← Activatable bundle
```

## Steering (10)

| File | Inclusion | What It Does | Customize? |
|---|---|---|---|
| `game-master.md` | `always` | Tenets, conversation loop, output contract, quality gates | No |
| `table-state.md` | `always` | Dice commands, state-file rules, session-log headings | No |
| `table-preferences.md` | `always` | How the GM formats play for your table | **Yes** |
| `campaign.md` | `auto` | Campaign bible / continuity framework | No |
| `session-zero.md` | `manual` | `/session-zero` | No |
| `recap.md` | `manual` | `/recap` | No |
| `save-game.md` | `manual` | `/save-game` | No |
| `quick-review.md` | `manual` | `/quick-review` | No |
| `new-character.md` | `manual` | `/new-character` | No |
| `level-up.md` | `manual` | `/level-up` | No |

Front matter must be the very first bytes of a steering file.

## Agents (8 thin wrappers)

| Agent | Invoke With | Loads |
|---|---|---|
| `game-master` | "Be my DM", "let's play", "continue the campaign" | `running-the-game.md`, `adjudication.md`, `state-keeping.md` |
| `character-creator` | "Make my character", "level up", "tweak the pregen" | `character-creation.md` |
| `session-planner` | "Prep the next session", "plan a one-shot" | `session-prep.md`, `encounter-design.md` |
| `rules-arbiter` | "How does this rule work?", "what's the DC?" | `adjudication.md`, `SYSTEMS_COMPARISON.md` |
| `npc-designer` | "Design a villain", "make an NPC" | `npc-voice.md` |
| `continuity-keeper` | "Check continuity", "new arc" | `campaign-continuity.md`, `state-keeping.md` |
| `session-critic` | "Review the session" | `session-review.md` |
| `builder` | "Set up a campaign", "add a system", "make a ChatGPT bundle" | `builder.md`, `session-zero.md` |

On Kiro Web, project agents are available for sub-agent delegation only; the steering files carry the
core rules into the main chat.

## Hooks (2 files)

| Hook file | Trigger | Runs |
|---|---|---|
| `campaign-validate.json` | `PostFileCreate` + `PostFileSave` on `campaigns/**.json|jsonl|md` | `python3 tools/validate-campaign.py --hook {{filePath}}` |
| `session-continuity.json` | `PostFileSave` on `campaigns/<id>/sessions/session-NN.md` | Agent prompt: continuity PASS/FAIL table |

- File-event hooks fire only for agent-made file changes. They run in Kiro IDE 1.0+ and Kiro CLI V3.
  **Kiro Web sessions do not run hooks**: run the tools yourself (the steering tells the agent to).
- Campaign-specific hooks: copy `examples/campaigns/<id>/continuity-hook.json` to
  `.kiro/hooks/<id>-continuity.json`.

## Skills (6)

`system-profiles`, `character-creation`, `npc-voice`, `encounter-design`, `safety-tools`, `campaign-bible`.

## SOPs (13)

01 Session Zero · 02 Running a Session · 03 Prepping a Session · 04 Setting Up a Campaign ·
05 Extending a Campaign · 06 Designing an NPC · 07 Reviewing a Session · 08 Contributing ·
09 Running a One-Shot · 10 Adding a System · 11 Group Play · 12 Playing in Other AIs ·
13 Creating and Customizing a Character

## Customization Priority

1. `steering/table-preferences.md`: your table's format.
2. Your campaign under `campaigns/<id>/` (SOP 01, SOP 04).
3. Campaign steering (`inclusion: fileMatch`) and a continuity hook, copied from `examples/campaigns/fractured-shadows/`.

**To change the method:** edit `core/methodology/`. Agents pick it up through `resources:`.

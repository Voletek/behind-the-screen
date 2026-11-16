# core/ — Canonical Methodology (Single Source of Truth)

> These files ARE the game-mastering system. Everything else references them (Tenet 8).

| File | What It Is |
|---|---|
| `tenets.md` | 9 priority-ordered tenets: which rule wins when rules conflict |
| `methodology/running-the-game.md` | The conversation loop, session structure, solo vs group, combat craft, improvisation, output contract |
| `methodology/adjudication.md` | When to roll, stakes, difficulty, honest rolling, degrees of success, the Failure Menu, clues, rulings |
| `methodology/state-keeping.md` | Campaign folder, state.json, session logs, dice log, Save Blocks, canon discipline, context budget |
| `methodology/session-zero.md` | System choice, shape, tone, safety, table settings, characters |
| `methodology/character-creation.md` | Player-owned character creation, sheets, customization, advancement |
| `methodology/session-prep.md` | The 10-section Session Brief; one-shot prep |
| `methodology/npc-voice.md` | NPC tiers, the 11-step voice sheet, performing NPCs as an AI, villains, non-verbal entities |
| `methodology/encounter-design.md` | Encounter cards, principles, difficulty by system family, combat/social/exploration/heists |
| `methodology/campaign-continuity.md` | Campaign bible, fronts and clocks, arc extension, canon forks, the continuity check |
| `methodology/session-review.md` | 12-category craft rubric + 6 AI-GM assessments + continuity layer, decision gate, flags |
| `methodology/builder.md` | Setting up campaigns, one-shots, new systems, bundles, preferences, experiment logs |

Each file is self-contained and followable without Kiro, by any AI assistant or by a human GM.

## How These Are Used

- **Kiro:** `.kiro/agents/` list them under `resources:`; steering summarises them.
- **Other AI assistants:** `tools/build-bundle.py` concatenates them with the boot prompt and a system profile (`portable/`).
- **Humans:** read them as a GM guide.
- **Tools:** `tools/validate-campaign.py` implements the checkable parts of `state-keeping.md` and
  `campaign-continuity.md`; `tools/roll.py` implements Tenet 5; `tools/encounter.py` implements the
  SRD 5.2.1 budget used in `encounter-design.md`.

## The Rule

> When the method changes, update `core/methodology/`. Everything downstream inherits.
> System-specific rules go in `systems/<id>/`, never here (Tenet 9).

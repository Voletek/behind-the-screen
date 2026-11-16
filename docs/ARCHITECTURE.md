# Architecture

> How Behind the Screen is organised, and how it maps to its sibling,
> [songwriting-kb](https://github.com/Voletek/songwriting-kb).

## Layers

```
               ┌──────────────────────────────┐
               │ core/tenets.md               │  priorities
               │ core/methodology/*.md        │  THE METHOD (system- and platform-neutral)
               └──────────────┬───────────────┘
        ┌─────────────────────┼──────────────────────┐
        ▼                     ▼                      ▼
 systems/<id>/          references/              tools/
 rules layer            data tables              deterministic checks
 (one per RPG)          (rubrics, safety,        (dice, validator,
                         voice, tone, state)      encounters, bundles)
        └─────────────────────┼──────────────────────┘
        ┌─────────────────────┴──────────────────────┐
        ▼                                            ▼
 .kiro/  (Kiro adapter)                        portable/ (any other AI)
 agents · steering · skills · hooks · SOPs     boot prompt · preferences · setup pages
        │                                            │
        ▼                                            ▼
 campaigns/ · oneshots/  (your work)          Save Blocks (state in chat)
 examples/               (reference implementations)
```

## Mapping from songwriting-kb

| songwriting-kb | behind-the-screen | Notes |
|---|---|---|
| `core/methodology/songwriting.md` | `running-the-game.md` | The core craft |
| `song-planning.md` (Song Brief) | `session-prep.md` (Session Brief) | Guided vs auto-pilot, stop-or-flow |
| `critique.md` (12 + 5 + Suno + album) | `session-review.md` (12 + 6 + continuity) | Decision gate, flags, hard caps |
| `character-voice.md` | `npc-voice.md` | Voice sheet, light-touch dialect, non-verbal entities |
| `album-continuity.md` + blueprint | `campaign-continuity.md` + bible | Registry → state; rules → continuity rules; extension protocol → arcs; plus canon forks |
| `suno-optimization.md` (platform layer) | `systems/` + `adjudication.md` | The rules system is the volatile layer, separate from craft |
| — | `state-keeping.md`, `session-zero.md`, `encounter-design.md`, `adjudication.md` | New: problems songs don't have |
| `builder.md` | `builder.md` | Plus "Add a System" and portable bundles |
| `tenets.md` (7) | `tenets.md` (9) | Safety first; honest dice; state over memory |
| `validate-song.py` | `validate-campaign.py` | Deterministic format checks, hook mode |
| `lyric-lint.py` | `roll.py` | The deterministic tool the domain most needs |
| — | `encounter.py`, `build-bundle.py` | Budget math; portability |
| `check-repo.py` | `check-repo.py` | Plus system profile checks |
| `experiments/suno/` | `experiments/ai-gm/` | Tier 3 evidence logs |
| `references/V6_TAG_DISCOVERY.md` | `references/AI_GM_FAILURE_MODES.md` | Platform-behaviour evidence |
| `references/STYLE_LIBRARY.md` | `references/GENRE_TONE_LIBRARY.md` | Ready-made packages |
| `examples/albums/*` | `examples/campaigns/*` | Fractured Shadows in both |
| `songs/`, `analysis/` | `campaigns/`, `oneshots/` | Empty user workspaces |
| "Using Without Kiro" | `portable/` + `tools/build-bundle.py` | One paste-able file |

## Design decisions

- **Rules systems are a layer** (Tenet 9). The core never says "DC". Each profile translates the core's
  stakes/difficulty/failure ideas into its own terms.
- **Proprietary systems are summarised.** Only the SRD 5.2.1 (CC-BY-4.0) is quoted.
- **State lives in files** (JSON + Markdown), because AI memory is unreliable; Save Blocks carry the
  same JSON through chat-only assistants, and the validator checks both.
- **Dice are a tool**, because language models can't roll fairly.
- **Hooks run the validator** on agent saves in Kiro IDE/CLI; Kiro Web and other assistants run it
  manually or not at all, and nothing breaks.

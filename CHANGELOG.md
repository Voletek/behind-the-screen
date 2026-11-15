# Changelog

All notable changes to this project are documented here.

## [0.1.0] — 2026-11-14

### Added
- **Core method** (`core/`): 9 tenets and 10 methodology files: running the game, adjudication,
  state keeping, session zero, session prep, NPC voice, encounter design, campaign continuity,
  session review, builder.
- **System profiles** (`systems/`): `dnd-5e` (SRD 5.2.1, full), `mouse-guard`, `root`,
  `marvel-multiverse`, `tmnt` (summaries), `rules-light` (complete house system), each with
  `PROFILE.md` + `profile.json`; profile template.
- **References**: AI GM failure modes, safety tools, NPC voice, pacing and tension, genre and tone
  library, improv tables, state format, systems comparison, session review rubric and template,
  campaign bible template.
- **Tools**: `roll.py` (d20/keep/drop, pools with exploding dice, PbtA, d616 with edges/troubles,
  percentile, Fate; logging; player-roll recording), `validate-campaign.py` (state schema, session
  logs, bibles, one-shots, dice logs, Save Blocks, retired terms; hook mode), `encounter.py`
  (SRD 5.2.1 XP budgets), `build-bundle.py` (portable bundles), `check-repo.py`.
- **Portable layer** (`portable/`): boot prompt, default table preferences, setup pages for Claude,
  ChatGPT and other assistants.
- **Kiro layer** (`.kiro/`): 7 agents, 8 steering files (3 always, 1 auto, 4 manual commands),
  5 skills, 2 hooks, 12 SOPs, a power.
- **Examples**: the Fractured Shadows campaign (from the novels, the Eryndor World Codex and the
  concept album, with open canon questions), five one-shots (one per system), two transcript
  excerpts (solo, group), a session review, a preferences example.
- **Tests and CI**: 33 unit tests; CI runs tests, repo integrity, example validation, bundle and dice
  smoke tests.

# Changelog

All notable changes to this project are documented here.

## [0.2.0] — 2026-11-15

### Added
- **Player-owned characters:** `core/methodology/character-creation.md` (ownership rule, guided and
  fast creation, group connections, pregen tweaks, sheets, customization table, advancement);
  `tools/character.py` (`new`, `check`, `show`, `methods`: creates the sheet and state entry, checks
  stat names and ranges, standard array / point buy / spreads, and sheet-vs-state agreement);
  `creation` blocks in every `profile.json`; character-creator agent, `/new-character` and
  `/level-up` commands, character-creation skill, SOP 13; a sheet for Rikan in the example campaign.
- **Players roll their own dice:** Tenet 5 rewritten (players roll for their characters, GM rolls
  only the world); roll requests and "wait for the result" in the conversation loop, adjudication
  and output contract; `roll.py --request` (prints a roll request, keeps the target with the GM) and
  `--total` (logs a total the player reported). New table settings: who rolls, targets shown, hint level, rebuilds.
- **No leading:** Information Discipline section in `running-the-game.md` (describe evenly, open
  prompts, only what PCs know, answer what was asked, no meta-signals, stakes from PC knowledge,
  NPCs don't solve it) and a hint ladder used only on `OOC: hint?`; Tenet 2 updated.
- **Review:** A6 No Leading assessment; `LEAD` and `ROLL` flags; Dice Honesty now checks that
  players rolled their own dice (cap 5 when the GM rolled for them). Failure modes 21-24.

### Changed
- Example transcripts show players rolling and non-leading descriptions; the solo transcript's
  leading hint and a puppeting line were removed. Example dice log, bible table settings and review updated.
- Validator FAILs when a `party[].sheet` file is missing. Bundles include the character method and sheets.

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

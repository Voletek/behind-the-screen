# Behind the Screen

**A knowledge base for AI Game Masters.** Let an AI run your tabletop RPG, solo or with a group, in
the system you choose: D&D 5e, Mouse Guard, TMNT & Other Strangeness, Root, Marvel Multiverse, or a
built-in rules-light engine. It works in Kiro, Claude, ChatGPT or any chat assistant.

It is built like its sibling, [songwriting-kb](https://github.com/Voletek/songwriting-kb): one canonical
method, thin automation on top, deterministic tools underneath, and worked examples.

---

## What it fixes

AI game masters have predictable problems. Each one has an answer here:

| Problem | Answer |
|---|---|
| The AI "rolls" a number it made up, or rolls for you | **Players roll their own dice**; the GM sends a roll request and waits. GM rolls use `tools/roll.py` (Tenet 5) |
| The AI builds your character for you | Guided creation where the player chooses and rolls; `tools/character.py` for sheets, checks and levelling |
| The AI leads you to the answer | Information Discipline: even descriptions, open prompts, no suggested actions, hints only on `OOC: hint?` |
| It forgets HP, NPCs and plot after a long chat | `state.json` + session logs + Save Blocks, and a validator (Tenet 8) |
| It decides what your character feels and does | Player agency rule, and a review category that counts violations (Tenet 2) |
| Every plan works | Stakes before rolls and a Failure Menu where failure moves the story |
| Walls of text and "1. Fight 2. Flee 3. Talk" menus | An output contract and table preferences |
| It mixes up D&D rules with other games | One profile per system, each with notes on what AIs get wrong |
| Dark content without consent | Safety tools come first: lines, veils, the X-card (Tenet 1) |
| The fastest typist runs the game | Group-chat conventions and spotlight tracking |

## Quick start

**Kiro** (IDE, CLI or Web): open this repo and talk naturally.

```
"Be my DM. Let's play Mouse Guard."          → game-master (runs session zero first)
/session-zero                                → new campaign, guided
"Run the Keeper of the Light one-shot"       → game-master with examples/oneshots/keeper-of-the-light
"Continue Fractured Shadows"                 → game-master loads the campaign files
"Make my character" / "Level up Lyra"        → character-creator (you choose, you roll)
"Prep the next session"                      → session-planner (10-section brief)
"Design a villain"                           → npc-designer
"What does a 7-9 mean in Root?"              → rules-arbiter
"Check continuity"                           → continuity-keeper
"How did that session go?"                   → session-critic
"We want to play Blades in the Dark"         → builder → Add a System
/new-character · /level-up · /recap · /save-game · /quick-review   → manual commands
```

**Claude, ChatGPT, Gemini, local models, Discord:** build one paste-able file, then follow the page
for your assistant in [`portable/`](portable/README.md).

```bash
python3 tools/build-bundle.py --system dnd-5e -o bundle.md                       # new game
python3 tools/build-bundle.py --campaign campaigns/my-campaign -o bundle.md      # ongoing campaign
python3 tools/build-bundle.py --oneshot examples/oneshots/shell-game --mode group -o shell.md
```

**Dice and checks (any platform, Python 3.9+, no dependencies):**

```bash
python3 tools/roll.py "1d20+5" --dc 15 --who Lyra --why "Stealth"     # D&D 5e
python3 tools/roll.py "5d6>=4" --ob 3                                  # Mouse Guard
python3 tools/roll.py "pbta+2"                                         # Root / Rules-Light
python3 tools/roll.py "d616+3" --tn 15 --edge 1                        # Marvel Multiverse
python3 tools/roll.py "1d100" --under 45                               # TMNT skills
python3 tools/roll.py "1d20+5" --total 19 --dc 15 --who Lyra          # log a roll the player made
python3 tools/character.py new --campaign campaigns/my-campaign --id lyra --name Lyra --player Kira
python3 tools/character.py check --campaign campaigns/my-campaign       # stats, method, sheet vs state
python3 tools/validate-campaign.py campaigns/my-campaign                 # state, logs, bible
python3 tools/encounter.py --party 4x3 --creatures "cr3,cr1/4x4"         # SRD 5.2.1 budget
```

## Supported systems

| id | Game | Dice | Profile |
|---|---|---|---|
| `dnd-5e` | Fifth edition (2024 rules via SRD 5.2.1) | d20 + mod vs DC | Full (open licence) |
| `mouse-guard` | Mouse Guard RPG, 2nd ed. | d6 pool vs Obstacle | Summary |
| `tmnt` | TMNT & Other Strangeness (Palladium) | d20 combat, d100 skills | Summary |
| `root` | Root: The RPG (PbtA) | 2d6 + stat: 10+ / 7-9 / 6- | Summary |
| `marvel-multiverse` | Marvel Multiverse RPG (d616) | 3d6 with the Marvel die vs TN | Summary |
| `rules-light` | Built-in house system; fallback for anything else | 2d6 + approach | Full |

"Summary" profiles describe mechanics in our own words for tables that own the book; the book is the
authority. Add any other game with the builder ("Add a System", SOP 10).

## Repository structure

```
behind-the-screen/
├── core/
│   ├── tenets.md                9 priorities (which rule wins)
│   └── methodology/             11 canonical methods (SINGLE SOURCE OF TRUTH)
├── systems/                     6 system profiles (PROFILE.md + profile.json) + template
├── references/                  11 data references (failure modes, safety, NPC voice, pacing,
│                                tone library, improv tables, state format, systems comparison,
│                                review rubric + template, campaign bible template)
├── tools/                       roll.py · character.py · validate-campaign.py · encounter.py · build-bundle.py · check-repo.py
├── portable/                    boot prompt, table preferences, Claude / ChatGPT / any-chat setup
├── .kiro/                       8 agents · 10 steering · 6 skills · 2 hooks · 13 SOPs · 1 power
├── examples/
│   ├── campaigns/fractured-shadows/   full campaign from the novels, codex and album
│   ├── oneshots/                5 one-shots, one per system
│   ├── sessions/                solo and group transcript excerpts
│   └── preferences/
├── campaigns/  oneshots/        YOUR work (empty)
├── experiments/ai-gm/           evidence logs for AI-behaviour claims
├── tests/  .github/workflows/   42 unit tests + CI
├── docs/ARCHITECTURE.md         layers, and the mapping from songwriting-kb
└── GAMEMASTERING_KNOWLEDGE_BASE.md   the craft behind the method (16 sections)
```

## The method in brief

**Tenets** (priority order, `core/tenets.md`): 1 Safety and consent first · 2 Player agency over plot ·
3 The table owns the rules · 4 Fiction first · 5 Honest dice · 6 A consistent, living world ·
7 Shared spotlight · 8 State over memory · 9 System-neutral craft.

**The conversation loop** (`running-the-game.md`): FRAME → ASK → LISTEN → DECIDE → RESOLVE → NARRATE → RECORD.

**Session shape:** recap → strong start → 3-6 scenes → climax → wind-down → save.

**Prep** (`session-prep.md`): characters · strong start · potential scenes · 10 secrets and clues ·
locations · NPCs · threats · fronts and clocks · rewards · safety and tone.

**Review** (`session-review.md`): 12 craft categories (agency, pacing, framing, adjudication, rules
fidelity, dice honesty, NPC voice, world consistency, spotlight, tone, safety, fun) + 6 AI-GM
assessments (no puppeting, concision, anti-sycophancy, state discipline, prep use, no leading).

## Solo and group play

| | Solo | Group (one shared chat) |
|---|---|---|
| Posting | Free text | `**Name (Character):** action` |
| GM prompts | Continuous | One named player at a time; declarations collected for shared moments |
| Risk | Companions out-shining the PC | Fastest typist dominating |
| Tools | Companions suggest, PC decides | Spotlight counts in every session log |

## Examples

- **[Fractured Shadows](examples/campaigns/fractured-shadows/BIBLE.md)**: a campaign adapted from
  Voletek's novels *Fractured Shadows* and *Shattered Veil*, the *Eryndor World Codex*, and the
  concept album. It shows canon authority, retired names, canon forks, and the places where the
  sources disagree (open canon questions), plus a played session 1 with dice log, prep, NPC sheets
  and a review. Two modes: solo as Rikan, or a group of original survivors.
- **One-shots:** [Keeper of the Light](examples/oneshots/keeper-of-the-light/ONESHOT.md) (5e folk horror) ·
  [The Thaw at Pinebrook](examples/oneshots/the-thaw-at-pinebrook/ONESHOT.md) (Mouse Guard) ·
  [The Ferryman of Hundred Reeds](examples/oneshots/the-ferryman-of-hundred-reeds/ONESHOT.md) (Root) ·
  [Shell Game](examples/oneshots/shell-game/ONESHOT.md) (TMNT) ·
  [Blackout Protocol](examples/oneshots/blackout-protocol/ONESHOT.md) (Marvel).

## Evidence tiers

`[Tier 1]` published rules text or scholarship · `[Tier 2]` named, widely used GM craft heuristic ·
`[Tier 3]` AI-GM observation, unverified until logged in `experiments/ai-gm/` across 3+ sessions.

## Hooks

In Kiro IDE 1.0+ and Kiro CLI V3, `.kiro/hooks/campaign-validate.json` runs the validator whenever an
agent saves a campaign file, and `session-continuity.json` checks each saved session log against the
bible. Kiro Web sessions don't run hooks; the steering tells the agent to run the validator itself.

## Contributing and credits

See [CONTRIBUTING.md](CONTRIBUTING.md) (rulebook copyright rules included) and [CREDITS.md](CREDITS.md).

This work includes material from the System Reference Document 5.2.1 ("SRD 5.2.1") by Wizards of the
Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed under the Creative
Commons Attribution 4.0 International License, available at
https://creativecommons.org/licenses/by/4.0/legalcode.

# Builder — Interactive Setup

> Canonical method for setting things up: new campaigns, one-shots, new system profiles, portable
> bundles, table preferences and experiment logs. Guided by default: one question at a time, a
> suggested default for each, confirm before writing.

---

## What the Builder Sets Up

| Task | Produces | Uses |
|---|---|---|
| New campaign | `campaigns/<id>/BIBLE.md`, `state.json`, folders | `session-zero.md`, `campaign-continuity.md` |
| New one-shot | `oneshots/<id>/ONESHOT.md`, `state.json` with pregens | `session-prep.md` → One-Shot Prep |
| Add a System | `systems/<id>/PROFILE.md`, `systems/<id>/profile.json` | `systems/PROFILE_TEMPLATE.md` |
| Portable bundle | One paste-able Markdown file | `tools/build-bundle.py`, `portable/` |
| Table preferences | `.kiro/steering/table-preferences.md` (or bundle header) | `examples/preferences/` |
| Campaign steering + hook (Kiro) | `campaigns/<id>/steering.md`, `.kiro/hooks/<id>-continuity.json` | `examples/campaigns/*/` |
| Experiment log | `experiments/ai-gm/YYYY-MM-DD-<slug>.yml` | `experiments/ai-gm/TEMPLATE.yml` |

---

## New Campaign (10 steps)

1. **Choose an id** (kebab-case, e.g. `ashes-of-hollowmere`).
2. **Run session zero** (`core/methodology/session-zero.md`), guided or auto-pilot.
3. **Create the folder** `campaigns/<id>/` with `sessions/`, `prep/`, `npcs/`, `reviews/`.
4. **Write `BIBLE.md`** from `references/YOUR_CAMPAIGN_BIBLE.md` (sections 1-11 now).
5. **Write `state.json`**: `schema`, `campaign`, `system`, `session: 0`, party, starting NPCs,
   factions, clocks, threads. See `references/STATE_FORMAT_REFERENCE.md`.
6. **NPC sheets** for pillar NPCs (`core/methodology/npc-voice.md`).
7. **Validate:** `python3 tools/validate-campaign.py campaigns/<id>`.
8. **Prep session 1** (`core/methodology/session-prep.md`).
9. **(Kiro, optional)** add `campaigns/<id>/steering.md` (`inclusion: fileMatch`) and a continuity
   hook (copy from `examples/campaigns/fractured-shadows/`).
10. **(Other AI)** build a bundle: `python3 tools/build-bundle.py --campaign campaigns/<id> -o <file>`.

---

## Add a System (12 steps)

Use when the players pick a game with no profile in `systems/`.

1. **Identify** the game, edition, publisher, and the licence of its rules text. If the rules are
   not openly licensed, the profile **summarises in your own words** and points to the book; it
   never copies rules text, tables or setting prose (CONTRIBUTING.md).
2. **Copy** `systems/PROFILE_TEMPLATE.md` to `systems/<id>/PROFILE.md`.
3. **Core resolution:** dice, how a roll is read, degrees of success. Map it to a `tools/roll.py`
   expression or mechanic (`d20`, pool `Nd6>=4`, `pbta`, `d616`, `d100<=X`).
4. **Difficulty scale** in the system's own terms.
5. **Character stats and resources:** names of attributes, skills, resource tracks (HP, health,
   harm boxes, conditions).
6. **Conditions/status effects** list.
7. **Structured conflict:** initiative, turns, actions, or the system's conflict procedure.
8. **GM procedures** the system requires (GM turn/players' turn, GM moves, doom pools, clocks).
9. **Advancement and rewards.**
10. **AI GM notes:** what an AI is likely to get wrong in this system, and how to avoid it.
11. **Write `profile.json`** (stats, resources, conditions, dice mechanic) so
    `tools/validate-campaign.py` can check character sheets.
12. **Test** with a 3-scene smoke session; log it in `experiments/ai-gm/`.

---

## Portable Bundle

1. Ask: which system, which campaign or one-shot, solo or group, and the target assistant.
2. Run `python3 tools/build-bundle.py --system <id> [--campaign <dir> | --oneshot <dir>] --mode <solo|group> -o bundle.md`.
3. Report the size. If it exceeds the target's comfortable context (see `portable/README.md`),
   use `--lean` (drops reference appendices) or trim older session logs.
4. Point the user to the setup page for their assistant in `portable/`.

---

## Table Preferences

Ask about: narration length, message format (bold speaker tags, emoji dice line on/off), status
tracker frequency, recap style, whether to state stakes, OOC handling, and anything the user always
corrects. Write them to `.kiro/steering/table-preferences.md` (Kiro) or the bundle header (other AI).

---

## Experiment Logs

When the user discovers something about AI GM behaviour ("Claude stops puppeting when told X",
"the model forgets HP after ~40 messages"), log it:
1. Copy `experiments/ai-gm/TEMPLATE.yml` to `experiments/ai-gm/YYYY-MM-DD-<slug>.yml`.
2. Record assistant, model, setup, observation, sessions tested.
3. Tier 3 until reproduced across 3+ sessions; then promote into `references/AI_GM_FAILURE_MODES.md`
   with the evidence link.

---

## Quality Gates

- [ ] Every file written was confirmed by the user (guided mode)
- [ ] `tools/validate-campaign.py` passes on new campaigns/one-shots
- [ ] New system profiles summarise, never copy, non-open rules text
- [ ] `tools/check-repo.py` passes after adding Kiro files

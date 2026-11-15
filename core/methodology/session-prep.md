# Session Prep — The Session Brief

> Canonical method for preparing a session (the GM's equivalent of a song brief). Produces
> `campaigns/<id>/prep/session-NN.prep.md`. Prep situations, not plots (Tenet 2).
>
> Based on the eight-step structure of Mike Shea's *Return of the Lazy Dungeon Master* [Tier 2],
> extended with fronts/clocks [Tier 2, Apocalypse World; Blades in the Dark] and the Three Clue Rule
> [Tier 2, Justin Alexander].

---

## Guided vs Auto-Pilot

- **Guided:** walk the 10 sections one at a time; suggest a default for each from the bible, state
  and last session; wait for the user's confirm or override. Stop-or-flow: after each section, the
  user can stop ("that's enough, let's play") and the brief is saved as-is.
- **Auto-pilot:** draft all sections, then present the brief for edits.

Prep should take the AI one pass. Prep for a human GM using this repo should take 15-45 minutes.

---

## Inputs (read first)

- `BIBLE.md` (tone, safety, factions, characters' goals/bonds/flaws)
- `state.json` (location, clocks, threads)
- Last session log (`## Open Threads`, `## Next Session`)
- Last session review, if any (what to improve)

---

## The 10 Sections of the Session Brief

### 1. Review the Characters
For each PC: current goal, one thing from their backstory or bond to touch this session, current
resources (wounded? low on spells? out of rations?). Group: note spotlight counts from last time.

### 2. Strong Start
One opening scene that starts in motion and relates to an open thread. Write 2-4 sentences of
opening narration.

### 3. Potential Scenes (3-6)
Short list of situations the PCs might encounter. Each is one line: **where · who · what's at
stake · the scene question**. Expect to use about half. Do not sequence them.

### 4. Secrets and Clues (10)
Ten short facts the PCs could learn, each one sentence. Not tied to a specific scene: drop them
wherever the PCs look. For any conclusion the PCs must reach, at least three clues point to it.

### 5. Fantastic Locations (2-4)
Each: name, three sensory details, one interactive feature (a collapsing bridge, a shrine that
answers questions, a river that runs uphill).

### 6. NPCs (2-5)
Each: name, want, how they talk (one line), what they know (link to clues), how they react if
threatened. Full sheets for important NPCs: `core/methodology/npc-voice.md`.

### 7. Threats and Encounters
Monsters, rivals, hazards and social opposition. Use `core/methodology/encounter-design.md`. For each
combat encounter: who, what they want, difficulty in system terms, an exit (flee, parley, surrender).

### 8. Fronts and Clocks
Which factions or dangers advance this session if the PCs don't intervene. List each clock with its
current value and what happens at each tick. Advance off-screen clocks now (Tenet 6) and note it.

### 9. Rewards
Treasure, advancement, information, allies, reputation. Use the system profile's reward guidance.
Tie at least one reward to a PC's goal.

### 10. Safety and Tone Check
Re-read the bible's `## Safety`. Does any scene, NPC or threat brush a line or veil? Adjust now.
Note the intended tone of the session in one line.

---

## Brief Template

```markdown
# Session NN Prep — <Campaign>
<!-- prep: session-NN · system: <id> · date: YYYY-MM-DD -->

## 1. Characters
## 2. Strong Start
## 3. Potential Scenes
## 4. Secrets and Clues
## 5. Fantastic Locations
## 6. NPCs
## 7. Threats and Encounters
## 8. Fronts and Clocks
## 9. Rewards
## 10. Safety and Tone
```

---

## One-Shot Prep

A one-shot brief adds:
- **Pitch** (one sentence) and **expected length** (scenes or hours).
- **Pregenerated characters** with built-in connections and a reason to be on the mission.
- **A guaranteed climax**: the one scene that must be reachable from anywhere, and a way to cut to
  it when time runs out.
- **Endings** (2-3): what success, partial success and failure look like.

Template: `examples/oneshots/*/ONESHOT.md`.

---

## Quality Gates

- [ ] Strong start is in motion and tied to an open thread
- [ ] Scenes are situations, not a sequence
- [ ] Every required conclusion has 3+ clues
- [ ] Every combat has an exit other than death
- [ ] At least one scene or reward per PC's goal/bond
- [ ] Clocks advanced off-screen and recorded
- [ ] Safety and tone check done

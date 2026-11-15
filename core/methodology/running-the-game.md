# Running the Game — The Core Method

> Canonical method for running a live session as an AI Game Master (GM), in any system, solo or
> group. Platform-neutral: follow it in Kiro, Claude, ChatGPT, any other assistant, or by hand.
>
> Companion files: `core/tenets.md` (priorities), `core/methodology/adjudication.md` (when and how
> to roll), `core/methodology/state-keeping.md` (files, dice log, save blocks),
> `systems/<id>/PROFILE.md` (the rules layer for the chosen game).

---

## Evidence Tiers

Claims in this repository carry a tier:

| Tier | Meaning | Example |
|---|---|---|
| `[Tier 1]` | Published rules text or peer-reviewed scholarship, cited | SRD 5.2.1 DC table; Fine, *Shared Fantasy* (1983) |
| `[Tier 2]` | Widely used GM craft heuristic from a named published source | Three Clue Rule (Justin Alexander) |
| `[Tier 3]` | Observation about AI GM behaviour or community practice, unverified | "Models drift toward letting the player win" |

Tier 3 claims are promoted only after they are logged in `experiments/ai-gm/` across 3+ sessions.

---

## Prerequisites (before the first scene)

1. **Session zero is done** (`core/methodology/session-zero.md`): system chosen, tone agreed, lines
   and veils recorded, characters made, play mode (solo or group) set.
2. **The system profile is loaded:** `systems/<id>/PROFILE.md`. If the players chose a system with
   no profile, run `core/methodology/builder.md` → "Add a System" first, or run with the
   `rules-light` profile and the player's own rulebook knowledge.
3. **State is loaded:** the campaign's `state.json`, campaign bible, and the last session log.
   For one-shots: the one-shot file and the pregenerated characters.
4. **Dice are decided** (Tenet 5): players roll for their own characters (default); the GM's
   source for world rolls is a tool, a designated player, or declared simulation.
5. **Characters exist** and were made by their players (`core/methodology/character-creation.md`).

If any of these is missing, say which and fix it before narrating. Do not improvise around a missing
state file in an ongoing campaign.

---

## The Conversation Loop

Every moment of play is this loop [Tier 2, after Apocalypse World's "the conversation"]:

```
  ┌──────────────────────────────────────────────────────────────┐
  │ 1. FRAME   Describe the situation: what the PCs perceive,    │
  │            what is at stake, what is moving.                 │
  │ 2. ASK     "What do you do?" (to a named player in groups)   │
  │ 3. LISTEN  Take the declared action. Clarify intent + method │
  │            if unclear ("What are you hoping happens?")        │
  │ 4. DECIDE  Say yes / say yes-at-a-cost / call for a roll      │
  │            (see adjudication.md). State stakes if useful.     │
  │ 5. RESOLVE Ask the player to roll (their dice) and WAIT; the   │
  │            GM rolls only for the world. Read the result.      │
  │ 6. NARRATE Describe the consequence. The fiction changes.     │
  │ 7. RECORD  Update state if anything persistent changed.       │
  └──────────────────────── back to 1 ───────────────────────────┘
```

### Rules for each step

**1. FRAME**
- Lead with the most important thing, then two or three sensory details. Not five.
- End with something the PCs can act on: a door, a person, a threat, a choice.
- Keep descriptions short: 3-6 sentences for a new scene, 1-3 for a continuing one. [Tier 3: AI GMs
  over-narrate; long blocks bury the hook.]
- Give **perceivable** information freely: what the characters can see, hear, smell and already
  know. Don't interpret it, rank it, or suggest what to do with it (see Information Discipline). If
  the characters look in the right place, they find what's there; the GM doesn't point to the place.

**2. ASK**
- End your turn with a question or an open situation, never with a list of numbered options unless
  the player asked for options. Numbered menus shrink player imagination. [Tier 3]
- In group play, name who you are asking: "Kael, the door is splintering. What do you do?"

**3. LISTEN**
- Never assume an action the player did not state. If a player writes "I search the room", ask what
  for or where only if it matters. Otherwise resolve the obvious version.
- If an action is impossible, say so and say why before they commit, and offer what is possible.

**4. DECIDE** — see `core/methodology/adjudication.md`. Short version:
- Is the outcome uncertain? Would failure be interesting? If both: roll. If not: say yes, or tell
  them the cost.

**5. RESOLVE**
- **Player characters: the player rolls.** Send a roll request and stop:
  `🎲 Lyra, roll Stealth: 1d20+5 · at stake: the gate guard hears you — roll and post the result.`
  Wait for their post (`🎲 17` or `1d20+5 → 22`). Don't continue the narration in the same message.
- Tell the player the dice, the modifier and anything they could add (advantage, help, a trait, a
  fate point), and let them decide. Hide the target only if the table setting says so.
- **The world:** the GM rolls NPC, monster and table rolls with a real source and shows the line.
- Log every roll that mattered (`tools/roll.py --record` / `--total` for player rolls).
- One roll per uncertain outcome. Do not make players roll repeatedly for the same thing.
- Group: when several PCs roll at once, list every request in one message, then wait for all results.

**6. NARRATE**
- Narrate the result in the fiction, then any mechanical effect in brackets:
  "The bolt clips your shoulder and spins you into the mud. [Lyra: −6 HP, 12/18]"
- On failure, the world moves: complicate, cost, reveal a danger, or advance a clock. "Nothing
  happens" is almost never the right failure. (See "Failing Forward" in adjudication.md.)
- Do not narrate the PC's feelings or next action (Tenet 2).

**7. RECORD** — see `core/methodology/state-keeping.md`. At minimum record: resource changes,
conditions, items gained or lost, NPCs met or changed, clocks advanced, threads opened or closed,
new canon invented at the table.

---

## Session Structure

```
OPENING        Recap → strong start (the first scene starts in motion)
BODY           3-6 scenes, alternating tension and release
CLIMAX         The highest-stakes scene of the session
CLOSING        Wind-down beat → save state → "what did we learn" → next-session hooks
```

### Opening
1. **Recap** (2-5 sentences or 3-5 bullets): what happened last time, where they are, what is
   unresolved. Ask a player to recap instead when in a group; it reveals what they remember and care
   about. Correct only factual errors.
2. **Strong start** [Tier 2, Mike Shea, *Return of the Lazy Dungeon Master*]: open in or near action.
   Not "you wake up in an inn". Something is already happening and needs a response.

### Body: scene framing
- **Start late, leave early.** Enter a scene at the moment something is at stake. Leave the moment
  the question of the scene is answered.
- **Each scene has a question:** "Will they get past the gate unseen?" "Will the ferryman talk?"
  When it is answered, cut.
- **Alternate pillars and pace:** follow combat with a quiet beat; follow investigation with action.
  Pacing tools are in `references/PACING_AND_TENSION_REFERENCE.md`.
- **Use the three pillars by default** (exploration, social, conflict) and lean toward whatever the
  table said they enjoy at session zero.
- **Aggressive scene transitions:** "You reach the river by dusk. The ferry is gone." Skip the walk.

### Climax
- Bring the session's main thread to a decision point: a fight, a confrontation, a revelation, a
  choice with a cost.
- If time (or the chat) is running out, cut directly to it.

### Closing
1. A short release beat: the campfire, the aftermath, a quiet moment.
2. **Save state** (state-keeping.md "End-of-Session Save").
3. Optional quick reflection (stars and wishes, or "what was your favourite moment?").
4. Offer 2-3 hooks for next time, but let the players say what they want to pursue.

---

## Solo Play vs Group Play

| Concern | Solo (one player + AI GM) | Group (2+ players in one chat) |
|---|---|---|
| Turn order outside combat | Continuous back-and-forth | Round-robin by name; collect simultaneous declarations for shared moments |
| Message format | Free text | `**Name (Character):** action` per message (see below) |
| Spotlight risk | NPC companions out-shining the PC | Fastest typist dominates |
| Pacing | Faster, more scenes per hour | Slower; cut harder, frame tighter |
| Companions | GM-run NPC allies fill party roles; they suggest, the PC decides | Usually unnecessary |
| Party split | Not applicable | Cut between groups every 1-2 exchanges; end each cut on a hook |
| Out-of-character talk | `OOC:` prefix | `OOC:` prefix; the GM waits for table consensus on OOC decisions |
| Safety tools | Same tools; check in more often in horror | Any player can invoke; the GM never asks who or why |

### Group chat conventions
- Players post as `**Kira (Lyra):** I nock an arrow and watch the treeline.`
- `OOC:` for out-of-character talk. `(whisper to GM)` for secrets. In a shared chat the GM answers
  secrets vaguely in public ("Lyra's player knows something you don't") or asks the player to use a
  private channel, if the platform allows one.
- When several players act at once, the GM replies: "Got Lyra and Kael. Elara, you too?" then
  resolves all declared actions in one message, in a sensible fictional order.
- If a player is absent, their PC fades into the background (agreed at session zero): the PC is
  present but takes no risky actions, or is "elsewhere" in the fiction.

### Spotlight tracking (group)
Keep a running count per player per session in the session log's `## Spotlight` section. Before
framing a new scene, check who is lowest and aim the scene at their PC's goals.

### Solo companions
- Give each GM-run companion a want, a flaw and a voice (`core/methodology/npc-voice.md`).
- Companions offer opinions and help when asked. They never take the decisive action.
- Companions can disagree with the PC. That is drama, not a block.

---

## Combat and Other Structured Conflict

The system profile defines the procedure (initiative, action economy, conflict scripts). The craft
on top of it:

1. **Before:** know what each side wants. Monsters that want something other than "kill everyone"
   flee, bargain, take hostages, grab the relic.
2. **Opening frame:** where everyone is, cover, hazards, one interesting feature of the terrain.
3. **Turns:** keep the GM's turns short. Describe enemy actions in one or two sentences with the
   mechanical result. Give the player the next decision quickly.
4. **Track state visibly:** after each round (or when asked), show a compact tracker:
   ```
   Round 3 | Kael 14/22 | Lyra 9/18 (Poisoned) | Elara 17/17 | Ghoul A bloodied | Ghoul B down
   ```
5. **End early:** when the outcome is clear, offer surrender, flight, or narrate the mop-up.
6. **After:** a breath. Loot, wounds, what the fight revealed.

For theatre-of-the-mind positioning, use zones ("near", "close", "far", or named areas such as
"the altar", "the doorway") unless the system needs a grid. If it needs a grid and the platform has
no map, describe distances in the system's units and keep a text map in the state file.

---

## Information Discipline (Don't Lead)

The players solve the problems. The GM's job is to make the world clear, not to make the answer
obvious. Leading is the AI GM habit of steering players toward "the right" choice. It takes away the
satisfaction of figuring things out and quietly turns play into a guided tour. [Tier 3]

### The rules

1. **Describe, don't prescribe.** Say what is there. Never say what the PCs could, should or might do.
   - ✖ "You could try climbing the vines, or perhaps search the desk."
   - ✔ "Ivy covers the north wall up to the broken window. A desk stands by the door, one drawer ajar."
2. **Open prompts only.** End with "What do you do?" (to a named player in groups), not a question
   that contains a plan.
   - ✖ "Do you follow the footprints toward the mill?" · ✔ "Kael, what do you do?"
3. **Even salience.** In a description, the important detail gets the same weight as the others
   unless it is truly conspicuous in the fiction. Don't single out the clue with extra adjectives,
   a separate sentence, or "something catches your eye".
4. **Only what the characters know.** No narrator labels the PCs haven't earned: not "the
   treacherous innkeeper", not "a trap", not "this seems important", not "you sense a hidden door".
   Reveal motives, traps and secrets through play, rolls (Insight, Investigation, Wises,
   Recall-Knowledge moves) or the PCs' own conclusions.
5. **Answer what was asked.** Answer questions truthfully and only as far as the character could
   know. "You don't know" and "You'd have to get closer" are good answers. Don't add the answer to
   the next question.
6. **No meta-signals.** Don't call for a roll that reveals something exists (use passive values or a
   hidden GM roll); don't comment on whether a choice is good; don't reveal exact enemy HP or secret
   DCs unless the table chose open targets; don't react to wrong theories with hints.
7. **Stakes from what the PC knows.** When stating stakes, use only information the character has
   ("if you fail, someone may hear you"), not hidden facts ("the guard behind the door hears you").
8. **NPCs and companions don't solve it.** An NPC may share what they know when asked and it suits
   their want; they don't hand over the plan. A solo companion may offer an opinion only when asked,
   and it's an opinion, not the answer.
9. **Let them miss things and be wrong.** A missed clue is fine: the Three Clue Rule
   (`core/methodology/adjudication.md` → Clues) means there are others. A wrong theory acted on is
   drama, corrected by consequences, never by the GM hinting.

### Hints — only when the table asks

Hint level is a session-zero table setting (`core/methodology/session-zero.md` Step 5):

| Setting | Behaviour |
|---|---|
| **Off** | No hints. The world reacts on its own (fronts, clocks, proactive NPCs). |
| **On request** (default) | Only after a player types `OOC: hint?` |
| **When stuck** | The GM may offer, OOC, after the table has made no progress for ~10 exchanges: "OOC: want a hint?" Only if they say yes. |

When a hint is given, use the **hint ladder**, one rung at a time:
1. **Recap** what the characters already know (facts only, no conclusions).
2. **Point back** to a lead they already found but haven't followed.
3. **In-world nudge:** a proactive clue arrives through the fiction (a witness talks, the villain
   acts). This is the Three Clue Rule's proactive clue, not the answer.

Never jump to rung 3 without the table asking for more.

### Not leading is not withholding

Don't hide perceivable things to avoid "leading". If a door is visible, mention the door. If a PC
looks under the rug, the trapdoor is there. The rule is about **pointing**, not about **seeing**.

---

## Improvisation

When players go somewhere unprepped:
1. **Ask yourself:** who is here, what do they want, what is about to happen?
2. **Steal from your prep:** reuse an unused NPC, location or secret (prep is portable).
3. **Use tables:** `references/IMPROV_TABLES.md` (names, complications, rumours, locations).
4. **Ask the players** when the system or tone allows it: "You've been to this town before. What's
   the one thing everyone there knows about the mayor?" Record their answer as canon.
5. **Record everything you invent** (Tenet 6).

---

## Common AI GM Failure Modes (watch list)

Full list with fixes: `references/AI_GM_FAILURE_MODES.md` [Tier 3].

| Failure | Symptom | Fix |
|---|---|---|
| Sycophancy | Every plan works; no real failure | Honest dice; failure moves the world |
| Puppeting PCs | "You feel…", "You decide to…" | Describe the world only |
| Over-narration | 400-word scene descriptions | 3-6 sentences, end on a hook |
| Option menus | "1. Fight 2. Flee 3. Talk" every turn | Ask an open question |
| Forgetting | NPC names change, dead enemies return | Read and write the state file |
| Railroading | Every path leads to the prepared scene | Prep situations; let scenes be skipped |
| Fake dice | "You rolled a 17!" with no roll | The player rolls; GM rolls use a tool or are declared simulated |
| Rolling for the player | GM rolls the PC's Stealth and narrates the result | Roll request, then wait |
| Leading | "You could try the loose stone…", "Do you check the altar?" | Describe, ask "what do you do?", hints only on request |
| Power creep | Free magic items, easy wins | Use the system's reward guidance |
| Monologuing NPCs | Villain speeches of 200 words | NPC lines ≤ 3 sentences, then a beat |
| Tone drift | Gothic horror becomes a sitcom | Re-read the tone notes in the bible |

---

## Output Contract (each GM turn)

A GM message during play contains, in this order:
1. Narration (in the fiction).
2. Mechanical results in brackets, only when something mechanical happened.
3. A visible roll line for every GM roll: `🎲 Ghoul, claws vs Lyra: 1d20+4 → [14] +4 = 18 vs AC 15 ✔`
4. Either the prompt to act (to a named player in groups) **or** a roll request for a player, never
   both, and never a roll request plus its outcome in the same message.
5. Nothing that leads (Information Discipline): no suggested actions, no option menus unless asked.

Optional, at scene ends or on request: a compact status tracker. Preferences for formatting live in
`.kiro/steering/table-preferences.md` (or the equivalent block in a portable bundle).

---

## Quality Gates (self-check every scene)

- [ ] Did I describe the world and not the PCs' choices?
- [ ] Did the players roll their own dice, and did I wait for the result?
- [ ] Did I avoid leading (no suggested actions, pointed questions, or unearned knowledge)?
- [ ] Did every roll have stakes, and did every result change the fiction?
- [ ] Did I end on something the players can act on?
- [ ] (Group) Is anyone's spotlight count far below the others?
- [ ] Did anything persistent change, and is it recorded?
- [ ] Is the scene inside the agreed lines, veils and tone?

---

## References

- Gary Alan Fine, *Shared Fantasy: Role-Playing Games as Social Worlds* (1983) [Tier 1]
- Vincent & Meguey Baker, *Apocalypse World* (2010, 2016) — the conversation, principles [Tier 2]
- Mike Shea, *Return of the Lazy Dungeon Master* (2018) — strong start, eight-step prep [Tier 2]
- John Harper, *Blades in the Dark* (2017) — clocks, position and effect [Tier 2]
- Justin Alexander, *So You Want to Be a Game Master* (2023) and The Alexandrian blog [Tier 2]
- Full credits: `CREDITS.md`

# Adjudication — Calling for Rolls, Setting Stakes, Making Rulings

> Canonical method for deciding outcomes, in any system. The system profile
> (`systems/<id>/PROFILE.md`) supplies the dice and the numbers; this file supplies the judgment.
> Priorities: `core/tenets.md` (Tenets 3, 4 and 5 especially).

---

## Step 1 — Is a Roll Needed?

Ask two questions [Tier 2, common to Apocalypse World, Blades in the Dark and the SRD's "the GM
calls for checks"]:

1. **Is the outcome uncertain?** Could a competent character fail here, given the circumstances?
2. **Would failure be interesting?** Does failing create a new situation, cost or danger?

| Uncertain? | Failure interesting? | Do this |
|---|---|---|
| No | — | Say yes. Narrate success. |
| Yes | No | Say yes, but it costs time, a resource, noise, or a small harm. Or let them succeed slowly. |
| Yes | Yes | Roll. |
| The system says roll (a move triggers, an obstacle is set) | — | Roll; the system's trigger wins (Tenet 3). |

Also do not roll when:
- The player describes an approach that obviously works in the fiction (Tenet 4: good play is rewarded).
- A roll would only gate information the plot needs (see Clues below).
- The same task was just rolled and nothing changed.

---

## Step 2 — Set the Stakes

Before rolling, decide (and usually say):
- **What success gets:** the intent the player stated.
- **What failure costs:** pick one from the Failure Menu below.
- **The difficulty:** in the system's language (DC, Obstacle, Target Number, move, percentile).

Saying stakes up front lets the player change approach. It also stops "rolling until it works".
Hide stakes only when the uncertainty is the point (a perception roll against an ambush).

State stakes **only from what the character knows** ("someone might hear you"), never from hidden
facts ("the guard behind the door hears you"). Stakes that reveal secrets are leading
(`running-the-game.md` → Information Discipline).

Whether the player sees the target number (DC, Ob, TN) before rolling is a table setting
(session-zero.md Step 5). Default: systems with fixed bands (PbtA) have nothing to hide; d20 and
d616 targets are revealed **after** the roll; Mouse Guard obstacles are stated before the roll, as
the book does.

### Difficulty in system terms

Each profile gives its own scale. Rough cross-system equivalence for quick rulings [Tier 2,
approximate, do not treat as conversion math]:

| Feel | d20 DC (SRD 5.2.1) | Dice-pool Obstacle (successes on d6 4+) | d616 TN | PbtA |
|---|---|---|---|---|
| Trivial (don't roll) | 5 | Ob 1 | — | no move |
| Easy | 10 | Ob 2 | ~10 | (roll, low risk) |
| Medium | 15 | Ob 3 | ~13-16 | (roll, real risk) |
| Hard | 20 | Ob 4-5 | ~17-20 | (roll, worse position) |
| Very hard | 25 | Ob 6+ | 20+ | (desperate) |
| Nearly impossible | 30 | — | — | — |

The d20 column is the SRD 5.2.1 Typical Difficulty Classes table [Tier 1]. The other columns are
heuristics; use the profile's own guidance first.

---

## Step 3 — Roll Honestly (players roll their own)

**A player character's roll is the player's roll** (Tenet 5).
1. Send a **roll request** and stop:
   ```
   🎲 <PC>, roll <what>: <expression> [advantage/edge/bonus dice] · at stake: <what they know> — roll and post the result.
   ```
   `tools/roll.py "<expr>" --request --who <PC> --why "<what>" [--dc N]` prints one (the target goes to
   the GM only).
2. Tell them about modifiers and options they have (help, advantage, a trait, fate, karma); they decide.
3. **Wait** for their result. Don't narrate the outcome in the same message as the request.
4. Read their post (faces or a total), apply the target, and log it:
   `tools/roll.py "<expr>" --record "<faces>" …` or `--total <n>` (source `player`).
5. If they ask "roll for me", roll with a real source and say so.

**World rolls** (NPCs, monsters, weather, tables) are the GM's: real source, shown in this format:
```
🎲 <Who>, <What>: <expression> → [<dice>] <mods> = <total> vs <target> <✔|✖|partial>
```
- Log every roll that mattered in the dice log (`core/methodology/state-keeping.md`).
- Advantage, edges, help, gear and conditions are applied before the roll, not after.
- Contested rolls (PC vs NPC): the player rolls theirs, the GM rolls the NPC's; reveal both.

---

## Step 4 — Read the Result and Narrate

### Degrees of success

Most systems have them even if the rules don't say so. Use them:

| Result | Narrate |
|---|---|
| Critical / exceptional | Success plus a bonus: extra effect, information, position |
| Clear success | They get what they intended |
| Partial / success at a cost | They get it, plus a complication from the Failure Menu |
| Failure | The world moves: pick from the Failure Menu |
| Critical failure / snake eyes | Failure plus a twist, never humiliation of the PC |

PbtA systems (Root) build partials into the roll (7-9). Mouse Guard builds them into "twist or
condition". d20 systems often don't: you may offer "succeed at a cost" when a roll misses by a little,
if the table agreed to that house rule.

### The Failure Menu (fail forward)

When a roll fails, pick one that fits the fiction and the stakes stated [Tier 2, adapted from
Apocalypse World GM moves and Mouse Guard twists/conditions]:

1. **Harm:** deal damage or a condition per the system.
2. **Cost:** they succeed but lose something: a resource, an item, time, reputation.
3. **Complication:** a new problem appears (guards arrive, the rope frays, the NPC gets suspicious).
4. **Worse position:** the next action becomes harder or riskier.
5. **Reveal a threat:** show something bad coming. Give them a chance to react.
6. **Advance a clock:** tick a danger or faction clock.
7. **Separate them:** split the party or cut them off from a resource.
8. **Offer a hard bargain:** "You can make it, if you leave the pack behind."
9. **Turn their move back on them:** the plan works, against them.
10. **Plain failure:** only when the fiction is already tense and the failure itself bites.

Never: "nothing happens", "you don't find anything" (when the plot needs it), or a failure that
makes the PC look incompetent at their core competence. A master thief fails because the lock is
warded, not because they fumbled.

---

## Clues and Information

- **Never gate essential information behind a single roll** [Tier 2, Justin Alexander, the Three
  Clue Rule: for every conclusion the players must reach, prepare at least three clues].
- If a clue is essential and the PCs look in the right place, they find it. Rolls decide *extra*
  information, how long it takes, or what it costs to get.
- Passive perception (or the system's equivalent) means you don't need to ask for a roll to notice
  the obvious.

---

## Rulings

When the rules don't cover something, or the players propose something unexpected:

1. **Decide fast** (under 30 seconds of table time). Use the closest analogous rule in the profile.
2. **Favour the fiction:** if the plan is clever and makes sense in the world, it should be possible.
3. **State the ruling** in one sentence: "Swinging from the chandelier is an Athletics check, DC 12;
   on a success you land behind the cultists with advantage on your next attack."
4. **Log it** under `## Rulings` in the session log with a one-line reason.
5. **Review after the session:** check the actual rule. If your ruling differed, decide with the
   table whether to keep it as a house rule (Tenet 3). Recurring rulings go in the campaign bible.

### Rules disputes with players
- Hear the player's reading once. If it's plausible and keeps play moving, accept it for now.
- Never argue rules for more than a minute of table time. "Let's go with X tonight and check after."
- In group play, a player who knows the system well can be asked to be the table's rules
  reference. The GM still decides.

---

## Hidden vs Open Rolls

| Roll type | Default | Why |
|---|---|---|
| Player character actions | Rolled by the player, open | Players own their luck and their results |
| Enemy attacks and saves | Open, unless the table prefers hidden | Honest dice; builds trust in AI GMs |
| Perception/insight where *asking for* the roll leaks information | Use passive values, or a hidden GM roll if the table agreed; logged | Calling for a roll signals something is there (leading) |
| Random encounters, weather, loot tables | Open or hidden, logged | Either is fine |

Hidden rolls are still tool-rolled and still logged. A player may ask to see the log after the scene.
A table that wants players to roll everything (including noticing) can ask the whole party to roll
perception at random moments, so a request never signals that something is there.

---

## Adjudicating Under Uncertainty About the Rules

An AI GM may not know a system's rules exactly. Rules of thumb [Tier 3]:
- Prefer the profile's summary over memory. If the profile is silent, say "I'm not sure of the exact
  rule; I'll rule X for now" and log it.
- Never invent a precise rule and state it as rules-as-written. Label it as a ruling.
- If a player has the rulebook, ask them to check while play continues.

---

## Quality Gates

- [ ] Was the roll needed (uncertain + interesting failure)?
- [ ] Were the stakes clear before the roll (unless deliberately hidden), and based only on what the PC knows?
- [ ] Did the player roll their own character's dice, and did the GM wait for the result?
- [ ] Was the difficulty set before the roll and not changed after?
- [ ] Did failure move the world forward?
- [ ] Were essential clues available without a lucky roll?
- [ ] Were rulings labelled as rulings and logged?

# Encounter Design — Combat, Social, Exploration and Hazards

> Canonical, system-neutral method for building encounters. System math (XP budgets, obstacles,
> threat ranks) comes from `systems/<id>/PROFILE.md`; `tools/encounter.py` implements the
> SRD 5.2.1 XP budget for `dnd-5e`.

---

## The Encounter Card

Every prepared encounter fits on one card:

```markdown
### <Encounter name>  · type: combat | social | exploration | hazard | chase | puzzle
- **Where:** location + 1 interesting terrain or feature
- **Who:** opposition (with system stats or references)
- **They want:** the opposition's goal (not "kill the PCs")
- **Stakes:** what the PCs win or lose
- **Difficulty:** in system terms (XP band, Obstacle, TN, threat)
- **Exits:** flee, parley, surrender, trick, pay, outlast
- **Twist (optional):** what changes halfway (reinforcements, collapse, betrayal)
- **Clues/rewards:** what it reveals or yields
```

---

## Design Principles

1. **Goals over hit points.** Opposition that wants something specific (the relic, a hostage, to
   escape, to delay) creates choices. [Tier 2]
2. **Interesting terrain.** At least one feature to use: height, cover, hazard, moving part. [Tier 2,
   SRD 5.2.1 "Reasons to Move" guidance; Tier 1 rules text for 5e]
3. **Mixed opposition.** Different roles (brute, skirmisher, artillery, controller, leader) make
   tactics matter. [Tier 2]
4. **An exit.** Every encounter can end without total victory or total death.
5. **Morale.** Most creatures flee or surrender at half strength or when the leader falls. [Tier 2,
   classic OSR morale]
6. **Not every encounter is a fight.** Plan the social and exploration versions of the same
   opposition: the bandits can be bribed, avoided or recruited.
7. **Telegraph danger.** Show deadly threats before they strike (tracks, bones, a warning). Players
   should be able to choose to avoid them.

---

## Difficulty by System Family

| Family | How difficulty is set | Where |
|---|---|---|
| d20 roll-over with XP budgets (D&D 5e / SRD 5.2.1) | XP budget per character × party size; Low / Moderate / High | `systems/dnd-5e/PROFILE.md`, `tools/encounter.py` |
| Dice pools vs Obstacle (Mouse Guard) | Obstacle number per test; conflicts use disposition | `systems/mouse-guard/PROFILE.md` |
| PbtA (Root) | No budget: threat comes from moves, harm and position | `systems/root/PROFILE.md` |
| d616 (Marvel Multiverse) | Rank of opposition vs heroes; TN from defense scores | `systems/marvel-multiverse/PROFILE.md` |
| Palladium (TMNT & Other Strangeness) | Opponent level, attacks per melee, SDC/HP pools | `systems/tmnt/PROFILE.md` |

When a system has no budget math, use the **threat ladder**:

| Threat | Means |
|---|---|
| Minor | Costs a resource; nobody is in real danger |
| Standard | Someone gets hurt; poor choices make it dangerous |
| Major | Someone may go down; smart play needed |
| Deadly | Running away is a valid strategy; telegraph it |

---

## Combat Encounters

1. Pick the threat level for the session's pacing (not every fight is Major).
2. Pick opposition with a goal and roles.
3. Pick the arena: 1 feature, 1 hazard, 1 cover option.
4. Write the twist (optional) and the exit.
5. Check the math in the profile (or `tools/encounter.py` for 5e).
6. Write the morale point.

### Running it (AI-specific) [Tier 3]
- Use real dice for monsters (Tenet 5). Track monster HP in the state file or a visible tracker.
- Play monsters at their intelligence: animals flee, cultists cluster around their leader, soldiers
  focus the healer.
- Do not quietly add HP or remove monsters to tune difficulty mid-fight. If the fight is going
  badly, use the exits: the enemy retreats, an ally arrives, a bargain is offered.

---

## Social Encounters

1. **The NPC's want** and **what they will not do**.
2. **Leverage:** what the PCs could offer or threaten (each a lever).
3. **Starting attitude:** hostile / wary / neutral / friendly / helpful.
4. **Roll when** the PC asks for something the NPC is reluctant to give and the approach is
   reasonable. Roleplay sets the difficulty; the roll decides.
5. Never require players to act out persuasion well to succeed (some players are shy). Describe the
   approach; the character's skill does the rest. [Tier 2]

## Exploration Encounters and Hazards

- A hazard is an obstacle with a clear way to engage and a cost to failure (the river, the blizzard,
  the collapsing tunnel).
- Exploration scenes need a reason to look: something hidden, a choice of paths, a resource that
  drains (light, food, time).
- Use the system's travel or exploration procedure if it has one (Mouse Guard weather and wilderness
  obstacles; Root travel between clearings; 5e travel pace).

## Chases, Heists and Puzzles

- **Chase:** a clock for the quarry's escape and one for the pursuers' danger; each round a PC acts
  and the GM throws a complication.
- **Heist:** prep the target, 3 security layers, 3 ways in. Let the plan happen; complications come
  from rolls, not from secret hard counters.
- **Puzzle:** solvable by the players with information they have; the character's skill can buy a
  hint. Never block progress on a puzzle; offer a costly bypass.

---

## Quality Gates

- [ ] Opposition has a goal beyond fighting
- [ ] Arena has a feature, a hazard or cover
- [ ] Difficulty checked in system terms
- [ ] At least one exit and a morale point
- [ ] Deadly threats are telegraphed
- [ ] The encounter connects to a clue, thread or PC goal

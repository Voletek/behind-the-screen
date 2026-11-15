# Mouse Guard Roleplaying Game (2nd edition) — System Profile

> **id:** `mouse-guard` · **Publisher:** Archaia / BOOM! Studios; design by Luke Crane, based on the
> comics by David Petersen · **GM is called:** GM · **Profile depth:** Summary · **Last checked:** 2026-11
>
> **Licence:** proprietary. This profile describes the mechanics in our own words so an AI GM can
> run the game with someone who owns the book. It does not reproduce rules text, tables or setting
> material. The book wins every disagreement.

---

## 1. Core Resolution — Dice Pools vs Obstacle

- Roll a number of six-sided dice equal to the ability or skill rating, plus bonus dice (help, gear,
  traits, wises, persona).
- Each die showing **4, 5 or 6 is a success** ("sword"); 1-3 is a failure ("snake"/"scoundrel").
- **Independent test:** successes ≥ **Obstacle (Ob)** → pass. **Versus test:** both sides roll;
  more successes wins (ties have their own procedure in the book).
- **Beginner's luck:** a mouse without the skill rolls a related ability at reduced dice (see book).
- **Fate:** spend to reroll dice showing 6 (they "explode" into extra dice). **Persona:** spend to add
  dice or tap Nature (see book for limits).

`tools/roll.py`: `5d6>=4` (count successes), with `--ob 3`; Fate reroll of 6s: `5d6>=4!` (exploding 6s).

### Failure: twist or condition
When a mouse fails, the GM either introduces a **twist** (a new obstacle, often from the GM's
categories below) or lets them **succeed but take a condition**. This is the system's built-in
fail-forward (`core/methodology/adjudication.md` Failure Menu).

## 2. Difficulty Scale

Obstacles are counted in successes needed. Ob 1-2 is routine for a trained mouse, Ob 3-4 is a real
challenge, Ob 5+ calls for help, gear and resources. The book lists obstacle guidance per skill and
per weather/wilderness/animal threat. Use it.

## 3. Characters

> Players build their own characters with `core/methodology/character-creation.md`; list this
> system's creation methods with `python3 tools/character.py methods --system mouse-guard`.
> Players roll their own dice for their characters (Tenet 5).

- **Abilities:** Nature, Will, Health; **Resources** and **Circles** (social abilities).
- **Skills:** many (e.g. Fighter, Pathfinder, Scout, Weather Watcher, Healer, Persuader, Survivalist,
  Loremouse, Orator…), rated 1-6. Use the exact list from the book.
- **Traits** (help or hinder), **Wises** (areas of knowledge), **Rank** in the Guard, **Belief**,
  **Goal**, **Instinct**.
- **Rewards tracked in state.json:** `fate`, `persona`, `checks` (earned in the GM's turn, spent in
  the players' turn).
- **Creation (summary):** choose rank and age, home town, skills, wises, traits, Nature, belief,
  goal and instinct, gear, relationships (mentor, friend, enemy).

## 4. Conditions

Healthy, Hungry and Thirsty, Angry, Tired, Injured, Sick, Dead. Conditions penalise tests and are
recovered in the players' turn (see book for recovery tests). Record them in `conditions[]`.

## 5. Structured Conflict

For extended conflicts (fight, chase, argument, war, negotiation, journey, speech, convince crowd…):
1. **State the goal** of each side.
2. **Disposition:** each team rolls to set its total disposition (hit points for this conflict).
3. **Script** three actions per exchange in secret: **Attack, Defend, Feint, Maneuver**.
4. **Reveal** one action at a time; the action pairing decides whether the test is independent or
   versus. Disposition falls; a side at 0 loses.
5. **Compromise:** the winner usually owes the loser something based on remaining disposition.

AI GM: script the GM side before the players reveal and record it in the chat as a hidden note
(or in the dice log with `hidden: true`) so the reveal is honest.

## 6. GM Procedures the System Requires

- **Missions:** each session is a Guard mission with 2 GM-chosen obstacles.
- **GM's turn:** the GM presents obstacles from four categories: **weather, animals, wilderness,
  mice**. The patrol tests what the GM calls for. Failures bring twists or conditions.
- **Players' turn:** the players spend **checks** they earned (by using traits against themselves) to
  act: recover, pursue goals, prepare. When checks run out, the turn ends.
- **Seasons:** spring, summer, autumn, winter shape weather and mission types.
- **End of session:** reward beliefs, goals and instincts with Fate and Persona (book procedure).

## 7. Advancement

Skills and abilities advance by recording passed and failed tests (both are needed); traits change
during winter sessions. Track `advancement` notes per skill in the character's `notes`.

## 8. Encounter / Threat Guidance

Threats are obstacles, not budgets. A mission's danger is set by the Ob numbers and by how many
twists the GM stacks. Animals use their Nature as a pool. For a one-session mission: one weather or
wilderness obstacle, one animal or mice obstacle, plus twists.

## 9. Tone and Default Setting

The Mouse Territories: the Guard protects mouse settlements from predators, weather and each other.
Tone: earnest, perilous, small creatures in a big dangerous world. Sacrifice and duty matter. Combat
with predators is deadly; clever avoidance is heroic.

## 10. AI GM Notes [Tier 3]

- Models treat it like a d20 game ("roll Fighter, DC 12"). Use Ob and successes, never DCs.
- Tell the player the skill, their dice and the Ob before they roll (help, gear, traits and wises
  add dice; the player chooses whether to use them, and whether to spend Fate or Persona).
- Remember the **GM's turn / players' turn** structure; models drift into free-form play.
- Twists must be obstacles from the four categories, not random punishments.
- Track **checks** earned in the GM's turn; they are the players' currency.
- Scale: mice are tiny. A crab or owl is a monster; a stream is a river.

## 11. Sources

- *Mouse Guard Roleplaying Game*, 2nd ed. (Luke Crane with David Petersen). Players should own the book.

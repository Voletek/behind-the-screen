# Root: The Roleplaying Game — System Profile

> **id:** `root` · **Publisher:** Magpie Games (based on Leder Games' board game *Root*) · Powered by
> the Apocalypse (PbtA) · **GM is called:** GM · **Profile depth:** Summary · **Last checked:** 2026-11
>
> **Licence:** proprietary. This profile summarises the mechanics in our own words. It does not
> reproduce moves, playbooks or setting text. The book wins every disagreement.

---

## 1. Core Resolution — Moves

- Play is a conversation. When a character does something that matches a **move's trigger**, the move
  happens and usually calls for a roll.
- Roll **2d6 + stat**: **10+** full success (it goes your way); **7-9** partial success (you get it
  with a cost, complication or choice); **6-** miss (the GM makes a move, often a hard one).
- Some results let the player choose from a list (e.g. on 7-9, pick one).

`tools/roll.py`: `pbta+2` (2d6+2, reads 10+/7-9/6-).

Fiction first (Tenet 4): no move triggers without a fictional action. "I roll Persuade" is not an
action; "I remind the captain the Marquise owes my clan a debt" is.

## 2. Difficulty Scale

There is no DC. Difficulty is set by **position in the fiction** and by what the GM does on 7-9 and
6-. Dangerous situations get harder costs and harsher GM moves. Some moves give bonuses (+1 forward,
+1 ongoing) from gear, help or reputation.

## 3. Characters

- **Stats:** Charm, Cunning, Finesse, Luck, Might (typically −1 to +2, advancing to +3).
- **Harm tracks:** Injury, Exhaustion, Depletion (boxes; when a track fills, the vagabond is taken out
  or suffers a lasting consequence, see book). Items have **Wear**.
- **Reputation** with each faction (prestige and notoriety), which changes what moves are available.
- **Playbooks** (core: Arbiter, Adventurer, Harrier, Ranger, Ronin, Scoundrel, Thief, Tinker,
  Vagrant; more in supplements) with nature, drives, connections, roguish feats, weapon skills, moves.
- **Creation (summary):** pick a playbook, species and look, stats, background, nature and drives,
  connections, moves, feats, weapon skills, equipment.

state.json resources: `injury`, `exhaustion`, `depletion` (`current` = marked boxes, `max` = boxes),
plus `value` (coin/items). Faction reputation goes in `factions[].standing`.

## 4. Conditions

Root uses harm boxes and fictional consequences more than named conditions. Record lasting effects as
free-text conditions (e.g. `"Broken arm"`); `conditions_open` is true.

## 5. Structured Conflict

No initiative. Combat is the conversation with combat moves and weapon moves. The GM keeps the
spotlight moving between vagabonds and makes moves when they miss or look to the GM. Groups of NPCs can
be treated as one threat with shared harm.

## 6. GM Procedures the System Requires

- **Agenda and principles** (PbtA): portray the Woodland as vivid and at war, fill the vagabonds' lives
  with adventure, play to find out what happens. Use the book's exact list.
- **GM moves:** on a miss or when players look to you, make a move: inflict harm, take their stuff,
  announce trouble, put someone in a spot, show the faction war's cost, and similar.
  Soft moves warn; hard moves land.
- **Clearings:** each clearing is a prepared situation with a controlling faction, problems, and
  NPCs who want things.
- **The war:** the Marquisate (cats), the Eyrie Dynasties (birds) and the Woodland Alliance (a
  rebellion of the denizens) contest the clearings. Factions act when the vagabonds don't.

## 7. Advancement

Advancement comes from playbook-specific triggers (drives, nature) and reputation. See book.

## 8. Encounter / Threat Guidance

Prepare clearings, not encounters: who controls it, what is broken, who wants the vagabonds' help or
silence. Threats are judged by how much harm a GM move can inflict and how bad the position is.

## 9. Tone and Default Setting

The Woodland: a forest of clearings in a three-way war, seen from vagabonds, outsiders who take jobs
nobody else will. Tone: storybook art over grim politics. Choices about whom to help have faction
consequences.

## 10. AI GM Notes [Tier 3]

- Models over-roll. Moves trigger only on the fiction; most conversation needs no roll.
- On 7-9, give a real cost or choice. Models drift toward treating 7-9 as full success.
- On 6-, make a GM move that follows from the fiction. "You fail" is not a move.
- Don't pick the player's options from a move's list for them.
- Track reputation. Models forget that helping the Eyrie hurts standing with the Alliance.

## 11. Sources

- *Root: The Roleplaying Game* (Magpie Games, 2021+) and its supplements. Built on *Apocalypse World*
  (Vincent & Meguey Baker).

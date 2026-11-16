# Marvel Multiverse Role-Playing Game — System Profile

> **id:** `marvel-multiverse` · **Publisher:** Marvel (2023 core rulebook; starter set and expansions)
> · d616 system · **GM is called:** Narrator · **Profile depth:** Summary · **Last checked:** 2026-11
>
> **Licence:** proprietary; Marvel characters are Marvel's property. This profile summarises the
> mechanics in our own words for tables that own the book. The book wins every disagreement.

---

## 1. Core Resolution — the d616 Roll

- Roll **three six-sided dice**; one is the **Marvel die** (a different colour). On the Marvel die
  the "1" face is the Marvel logo: it **counts as 6** and makes the roll **Fantastic**.
- Add the three dice + the relevant **ability score** (+ modifiers). Meet or beat the **Target
  Number (TN)** to succeed.
- **Fantastic success:** succeeding with the Marvel logo showing gives a bonus effect (for example,
  doubled damage on attacks; specific powers list their own Fantastic effects).
- **Ultimate Fantastic:** the logo plus 6s on both other dice — an automatic success with extra
  benefits (see book).
- **Edges and troubles:** an edge lets you reroll one die and keep the better result; a trouble forces
  a reroll of one die keeping the worse. Edges and troubles cancel one for one and can stack.

`tools/roll.py`: `d616+3` with `--tn 15`; edges `--edge 1`, troubles `--trouble 1`.
The tool rerolls the lowest die for an edge (keeping the better) and the highest die for a trouble
(keeping the worse); the book lets the player choose which die, so offer the choice when it matters.

## 2. Difficulty Scale

- Against characters, the TN is usually a **defense score** derived from the defender's ability
  (e.g. Melee Defense against a melee attack).
- For tasks, the Narrator sets a TN. Rough feel: ~10 easy, ~15 challenging, ~20 hard; use the book's
  table when available.

## 3. Characters

> Players build their own characters with `core/methodology/character-creation.md`; list this
> system's creation methods with `python3 tools/character.py methods --system marvel-multiverse`.
> Players roll their own dice for their characters (Tenet 5).

- **Abilities (the "MARVEL" acronym):** Melee, Agility, Resilience, Vigilance, Ego, Logic. Each has a
  matching defense score.
- **Rank** (1-6: from street-level to cosmic) sets power budget and **Karma**.
- **Resources tracked in state.json:** `health` (from Resilience), `focus` (from Vigilance),
  `karma` (spent for edges and effects).
- **Powers** are grouped into **power sets**; many cost Focus.
- **Traits** and **tags** describe background and quirks.
- **Creation (summary):** pick a rank, assign ability points, choose origin, occupation, traits,
  tags, powers within the rank's limits.

## 4. Conditions

Many power effects apply conditions (e.g. stunned, blinded, bleeding, ablaze). Record them by name
as listed in the book. `conditions_open` is true.

## 5. Structured Conflict

1. **Initiative:** a Vigilance-based d616 check; order from highest. A Fantastic roll wins ties
   (then the higher modifier).
2. **On a turn:** movement, one standard action, and reactions as granted by powers.
3. **Damage:** on a hit, damage = **Marvel die result × damage multiplier + ability score**
   (multiplier comes from the attacker's rank and powers). A Fantastic success doubles it.
   Damage reduces Health (physical) or Focus (mental) after damage reduction.
4. Characters at 0 Health are knocked out or worse per the book.

## 6. GM Procedures the System Requires

- Run comic-book pacing: big set pieces, cliffhangers, dramatic reveals between "issues" (sessions).
- Use Karma as a reward for heroic, in-character play.
- Villains get a plan, a lair, and a reason to come back.

## 7. Advancement

Characters advance in rank and gain powers through play milestones. See book.

## 8. Encounter / Threat Guidance

Match opposition rank to hero rank. Use **mobs/henchmen** for volume and one or two named villains for
threat. Give every fight an objective (save civilians, stop the device, protect the witness).

## 9. Tone and Default Setting

The Marvel Universe (Earth-616). Tone ranges from street-level crime to cosmic. Heroism, banter,
collateral damage, secret identities, and moral choices.

## 10. AI GM Notes [Tier 3]

- The Marvel die's "1" is **6 and Fantastic**, not a 1. Models get this wrong; use the tool.
- Don't let canonical heroes owned by no player steal the scene. Cameos support; PCs decide.
- Track Focus spending on powers; models forget it.
- Avoid copying comic dialogue or plots verbatim; write original situations.

## 11. Sources

- *Marvel Multiverse Role-Playing Game: Core Rulebook* (Marvel, 2023), the starter set, and
  expansions. Free quick-start rules have been released by Marvel.

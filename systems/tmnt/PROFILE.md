# Teenage Mutant Ninja Turtles & Other Strangeness — System Profile

> **id:** `tmnt` · **Publisher:** Palladium Books (1985 original; *Redux* edition from the 2023
> Kickstarter) · Palladium **Megaversal** system · **GM is called:** Game Master ·
> **Profile depth:** Summary · **Last checked:** 2026-11
>
> **Licence:** proprietary; the TMNT name and characters belong to Paramount. This profile summarises
> mechanics in our own words for tables that own the book. The book wins every disagreement.
>
> **Availability note:** in October 2026 Palladium announced it was not renewing the TMNT licence;
> remaining stock is being sold off with no reprints planned
> ([GeekNative, Oct 2026](https://www.geeknative.com/243618/why-palladium-books-walked-away-from-ninja-turtles-to-double-down-on-rifts/)).
> If your table wants turtles without the book, use `rules-light` with the mutant-animal notes in §9.

---

## 1. Core Resolution

Palladium uses two kinds of roll:
- **Combat:** d20 rolls to **strike**, **parry** and **dodge**, plus bonuses from attributes and
  hand-to-hand training. A strike that beats the defender's parry/dodge roll hits (ties go to the
  defender). A natural 20 is a critical strike (usually double damage).
- **Skills:** **percentile (d100) roll under** the skill's percentage to succeed.
- **Saving throws:** d20 against fixed target numbers (e.g. vs poison, vs psionics) with bonuses.

`tools/roll.py`: strike `1d20+3`; skill `1d100` with `--under 45`.

## 2. Difficulty Scale

Skills have their own percentages; apply bonuses or penalties (±5% to ±30%) for circumstances.
Combat difficulty is set by the defender's bonuses.

## 3. Characters

> Players build their own characters with `core/methodology/character-creation.md`; list this
> system's creation methods with `python3 tools/character.py methods --system tmnt`.
> Players roll their own dice for their characters (Tenet 5).

- **Eight attributes:** I.Q. (intelligence), M.E. (mental endurance), M.A. (mental affinity),
  P.S. (physical strength), P.P. (physical prowess), P.E. (physical endurance), P.B. (physical beauty),
  Spd (speed). Exceptional scores give bonuses.
- **Hit Points** and **S.D.C.** (structural damage capacity): damage comes off S.D.C. first, then
  Hit Points. Track both.
- **Mutant animal creation:** roll or choose the animal, spend **Bio-E** points on human features
  (hands, biped, speech, looks) and animal powers. Plus education, skills and a background.
- **Alignment:** Palladium's seven alignments (Principled, Scrupulous, Unprincipled, Anarchist,
  Miscreant, Aberrant, Diabolic).
- **Hand-to-hand** training type sets attacks per melee and combat bonuses.

state.json stats: `IQ ME MA PS PP PE PB Spd`; resources: `hp`, `sdc`.

## 4. Conditions

Use free-text conditions (stunned, knocked down, unconscious, etc.) as the book describes.
`conditions_open` is true.

## 5. Structured Conflict

- A **melee round** is about 15 seconds. Each character has a number of **attacks per melee**.
- Initiative: d20 (+ bonuses); highest acts first; attacks alternate around the order until everyone's
  attacks for the round are used.
- Defenders may parry (free, with training) or dodge (uses an attack) against each strike.
- Vehicle combat and modern weapons have their own rules in the book.

## 6. GM Procedures

Classic GM-driven adventures: investigation, street fights, travel (the *Truckin' Turtles* road trip
material), and weird science. No mandatory GM moves.

## 7. Advancement

Experience points for actions (good ideas, clever play, survival, defeating opponents) and levels that
raise skills and hit points. See book.

## 8. Encounter / Threat Guidance

No budget math. Use opponent level, attacks per melee and S.D.C./HP pools; street-level gangs come in
numbers, mutants and ninja are individual threats. Use the threat ladder in
`core/methodology/encounter-design.md`.

## 9. Tone and Default Setting

Gritty black-and-white comic roots (the original Eastman & Laird comics) more than the cartoon: urban
vigilantes, ninja clans, mutagen, aliens and road trips. Agree at session zero whether the table wants
gritty-comic or Saturday-morning tone (`references/GENRE_TONE_LIBRARY.md`).

**Mutant animal PCs:** most tables play original mutant animals rather than the four canonical
turtles. Encourage it: it avoids canon clashes and gives players ownership.

**Content note:** the 1985 printing contained insanity tables widely recognised as offensive; the
Redux edition removed them. Do not use the original tables (Tenet 1).

## 10. AI GM Notes [Tier 3]

- Models apply 5e logic (AC, DCs). Use strike vs parry/dodge and percentile skills.
- Track S.D.C. and Hit Points separately.
- Keep attacks-per-melee bookkeeping in the tracker; it is easy to lose.
- Keep canonical characters (the turtles, Splinter, Shredder) as cameos unless a player plays one.

## 11. Sources

- *Teenage Mutant Ninja Turtles & Other Strangeness* (Erick Wujcik, Palladium Books, 1985) and the
  *Redux* edition (2024-25 fulfilment).
- Licence status: GeekNative report linked above.

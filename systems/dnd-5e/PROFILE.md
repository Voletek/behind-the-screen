# Fifth Edition Fantasy (2024 rules, SRD 5.2.1) — System Profile

> **id:** `dnd-5e` · **Rules basis:** System Reference Document 5.2.1 (2024 core rules) ·
> **GM is called:** Game Master (DM by convention) · **Profile depth:** Full · **Last checked:** 2026-11
>
> This work includes material from the System Reference Document 5.2.1 ("SRD 5.2.1") by Wizards of
> the Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed under the
> Creative Commons Attribution 4.0 International License, available at
> https://creativecommons.org/licenses/by/4.0/legalcode.
>
> This profile is "compatible with fifth edition". Content outside the SRD (non-SRD subclasses,
> monsters, settings) is not included; players who own other books are the authority on it.

---

## 1. Core Resolution — the D20 Test

Three kinds of D20 Test [Tier 1, SRD 5.2.1]: **ability checks**, **saving throws**, **attack rolls**.

1. Roll 1d20.
2. Add the relevant ability modifier, plus the Proficiency Bonus if proficient, plus other bonuses
   and penalties.
3. Compare to the target: a **DC** (checks, saves) or **Armor Class** (attacks). Equal or higher succeeds.

- **Advantage:** roll 2d20, use the higher. **Disadvantage:** roll 2d20, use the lower. They don't
  stack; one of each cancels out.
- **Attack rolls:** a natural 20 always hits and is a Critical Hit (roll the attack's damage dice
  twice). A natural 1 always misses.
- **Heroic Inspiration:** a character who has it can expend it to reroll any die immediately after
  rolling it, and must use the new roll.

`tools/roll.py`: `1d20+5`, advantage `2d20kh1+5`, disadvantage `2d20kl1+5`, `--dc 15` or `--ac 14`.

### Degrees of success
RAW has no partial success on checks. Optional house rule (record in the bible if used): on a check
that misses the DC by 1-2, offer "succeed at a cost" (`core/methodology/adjudication.md`).

## 2. Difficulty Scale

Typical Difficulty Classes [Tier 1, SRD 5.2.1]:

| Task | DC |
|---|---|
| Very easy | 5 |
| Easy | 10 |
| Medium | 15 |
| Hard | 20 |
| Very hard | 25 |
| Nearly impossible | 30 |

Don't call for a roll on very easy tasks unless the circumstances make them uncertain.

## 3. Characters

- **Abilities:** Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma (state.json:
  `STR DEX CON INT WIS CHA` scores; modifier = (score − 10) ÷ 2, rounded down).
- **Skills** (ability): Acrobatics (DEX), Animal Handling (WIS), Arcana (INT), Athletics (STR),
  Deception (CHA), History (INT), Insight (WIS), Intimidation (CHA), Investigation (INT),
  Medicine (WIS), Nature (INT), Perception (WIS), Performance (CHA), Persuasion (CHA),
  Religion (INT), Sleight of Hand (DEX), Stealth (DEX), Survival (WIS).
- **Proficiency Bonus by level:** +2 (1-4), +3 (5-8), +4 (9-12), +5 (13-16), +6 (17-20).
- **Resources tracked in state.json:** `hp`, `temp_hp`, `hit_dice`, `spell_slots_<n>` (per level),
  `heroic_inspiration` (0/1), `exhaustion` (0-6), `death_saves_success`, `death_saves_failure`,
  plus class resources by name (e.g. `rage`, `ki`, `channel_divinity`).
- **Creation (summary):** choose class, origin (background + species), ability scores, alignment
  (optional), equipment; details per the SRD.

## 4. Conditions [Tier 1, SRD 5.2.1 names]

Blinded, Charmed, Deafened, Exhaustion, Frightened, Grappled, Incapacitated, Invisible,
Paralyzed, Petrified, Poisoned, Prone, Restrained, Stunned, Unconscious.

**Exhaustion (2024 rules):** cumulative levels. Each level reduces D20 Tests by 2 × level and Speed by
5 ft × level. Level 6 is death. A Long Rest removes 1 level.

## 5. Structured Conflict — Combat

1. **Surprise and positions** established.
2. **Initiative:** everyone rolls a Dexterity check (`1d20+DEX mod`); act from highest to lowest.
3. **On a turn:** move up to Speed, take one action, possibly a Bonus Action (if a feature grants
   one); one Reaction per round (e.g. an Opportunity Attack).
4. **Actions** [Tier 1, SRD action table]: Attack, Dash, Disengage, Dodge, Help, Hide, Influence,
   Magic, Ready, Search, Study, Utilize. Players may improvise; the GM says what D20 Test it needs.
5. **Damage and dying:** at 0 HP a PC falls Unconscious and makes **Death Saving Throws** at the
   start of each turn: 1d20, 10+ success, otherwise failure; three successes = Stable, three failures
   = death. Natural 20 regains 1 HP; natural 1 counts as two failures. Taking damage at 0 HP causes a
   failure (a critical causes two).
6. **Resting:** Short Rest (1 hour, spend Hit Dice); Long Rest (8 hours, regain HP and most
   resources, reduce Exhaustion by 1).

Theatre of the mind: track distance in 5-ft increments or use zones (melee / near ≈30 ft / far ≈60 ft+)
and record them in the tracker.

## 6. GM Procedures

- The GM calls for D20 Tests and sets DCs (`core/methodology/adjudication.md`).
- **Passive checks:** 10 + all modifiers (Passive Perception for noticing without rolling).
- **Group checks:** everyone rolls; if at least half succeed, the group succeeds.
- **Attitude** of NPCs (Friendly, Indifferent, Hostile) changes via the Influence action.

## 7. Advancement and Rewards

- XP from monsters' XP values (by CR) or milestone levelling (record which in the bible).
- XP by CR [Tier 1]: 0 = 0 or 10 · 1/8 = 25 · 1/4 = 50 · 1/2 = 100 · 1 = 200 · 2 = 450 · 3 = 700 ·
  4 = 1,100 · 5 = 1,800 · 6 = 2,300 · 7 = 2,900 · 8 = 3,900 · 9 = 5,000 · 10 = 5,900 (higher CRs in
  `tools/encounter.py`).
- Treasure: follow SRD guidance; magic items are rewards, not shop stock, unless the bible says so.

## 8. Encounter Guidance — XP Budget [Tier 1, SRD 5.2.1 "Combat Encounter Difficulty"]

1. Choose difficulty: **Low**, **Moderate** or **High**.
2. Budget = XP Budget per Character (by party level) × number of characters.
3. Spend it on creatures by their XP value without going over.

| Level | Low | Moderate | High | | Level | Low | Moderate | High |
|---|---|---|---|---|---|---|---|---|
| 1 | 50 | 75 | 100 | | 11 | 1,900 | 2,900 | 4,100 |
| 2 | 100 | 150 | 200 | | 12 | 2,200 | 3,700 | 4,700 |
| 3 | 150 | 225 | 400 | | 13 | 2,600 | 4,200 | 5,400 |
| 4 | 250 | 375 | 500 | | 14 | 2,900 | 4,900 | 6,200 |
| 5 | 500 | 750 | 1,100 | | 15 | 3,300 | 5,400 | 7,800 |
| 6 | 600 | 1,000 | 1,400 | | 16 | 3,800 | 6,100 | 9,800 |
| 7 | 750 | 1,300 | 1,700 | | 17 | 4,500 | 7,200 | 11,700 |
| 8 | 1,000 | 1,700 | 2,100 | | 18 | 5,000 | 8,700 | 14,200 |
| 9 | 1,300 | 2,000 | 2,600 | | 19 | 5,500 | 10,700 | 17,200 |
| 10 | 1,600 | 2,300 | 3,100 | | 20 | 6,400 | 13,200 | 22,000 |

Calculator: `python3 tools/encounter.py --party 4x3 --creatures "cr3,cr1/4x6"`.

Rule of thumb from the SRD: a single monster whose CR equals the level of a party of four is a
low-difficulty fight.

## 9. Tone and Default Setting

Generic heroic fantasy. The SRD has no setting; use the campaign bible.

## 10. AI GM Notes [Tier 3]

- **Advantage misuse:** models stack advantage or add +2 "for flavour". Advantage doesn't stack.
- **Forgotten resources:** track spell slots, Hit Dice and class resources in `state.json`; ask
  before assuming a slot is available.
- **Monster stats:** use SRD stat blocks or ones the players provide. Don't invent precise stat blocks
  and call them official; label homebrew as homebrew.
- **Death saves:** run them openly and log them. They are the most emotionally loaded rolls in 5e.
- **2014 vs 2024 drift:** models mix editions (e.g. old exhaustion rules). This profile uses 2024
  (SRD 5.2.1). Record in the bible if the table plays 2014 rules (SRD 5.1) instead.
- **Concentration:** remind casters of concentration checks when they take damage (CON save, DC 10 or
  half the damage, whichever is higher, max DC 30).

## 11. Sources

- System Reference Document 5.2.1, Wizards of the Coast, CC-BY-4.0 (attribution above).
- Wizards of the Coast's protected marks (e.g. "Dungeons & Dragons") are not part of the SRD.

# Rules-Light Engine — System Profile

> **id:** `rules-light` · **Publisher:** this repository · **GM is called:** GM ·
> **Profile depth:** Full · **Last checked:** 2026-11
>
> A small, complete house system for two uses:
> 1. **Fallback** when the players choose a game with no profile: run that game's fiction and
>    character concepts on this engine, or use it to rule anything the GM doesn't know.
> 2. **Standalone** for quick one-shots, kids' games, and settings without a system (e.g. playing
>    TMNT-style mutants without the Palladium book).

---

## 1. Core Resolution

Roll **2d6 + Approach** when the outcome is uncertain and failure is interesting
(`core/methodology/adjudication.md`).

| Total | Result |
|---|---|
| **12+** | Critical: success plus a bonus |
| **10-11** | Success |
| **7-9** | Success at a cost: the GM picks one from the Failure Menu, or offers a hard choice |
| **6 or less** | Miss: the GM makes the world move (Failure Menu); mark 1 XP |

- **Edge (+1d):** roll 3d6, keep the best 2 (good position, help, perfect tool).
- **Bane (−1d):** roll 3d6, keep the worst 2 (bad position, injury, wrong tool). Edge and bane cancel.

`tools/roll.py`: `pbta+2`; edge `3d6kh2+2`; bane `3d6kl2+2`.

## 2. Difficulty

No target numbers. The **position** sets how bad a 7-9 or 6- can be:
- **Controlled:** failure costs time or a minor setback.
- **Risky (default):** failure brings harm or a complication.
- **Desperate:** failure brings serious harm or loss. A success here deserves extra effect.

## 3. Characters

- **Concept:** one line ("disgraced dwarven siege engineer", "mutant snapping turtle who runs a diner").
- **Approaches (4):** Might, Grace, Wits, Heart. Assign +2, +1, +1, 0 (or +2, +2, 0, −1).
- **Tags (3):** short phrases that justify edges ("Ratfolk tunnel-sense", "Ex-Custodian", "Knows
  every sewer junction").
- **Harm:** 4 boxes. Light harm marks 1, serious 2, deadly 3. At 4 marked the character is taken out
  (the table chooses: dying, captured, broken, or a heroic last act).
- **Strain** (optional): 6 boxes for magic, stress or supernatural cost. At 6, a lasting consequence.
- **Gear:** what makes sense for the concept. Special gear can give an edge.
- **XP:** mark on a miss, and at session end for each "yes": did you pursue your goal? reveal
  something about your character? face danger for someone else? 5 XP = advance (+1 approach, a new
  tag, or a special ability agreed with the GM).

state.json: stats `Might Grace Wits Heart`; resources `harm` (max 4), `strain` (max 6), `xp`.

## 4. Conditions

Free text, each with a mechanical effect agreed at the table ("Poisoned: bane on Might until treated").

## 5. Structured Conflict

No initiative. The GM frames the threat, asks each player in turn what they do, resolves, and has the
opposition act on misses and 7-9 results (and whenever the fiction says they would). Named enemies have
2-4 harm boxes; mooks go down on any success.

## 6. GM Procedures

Use the core methodology as-is: the conversation loop, the Failure Menu, clocks for threats.

## 7. Advancement

See XP above. Every advance should change how the character plays.

## 8. Encounter / Threat Guidance

Use the threat ladder (`core/methodology/encounter-design.md`): Minor (mooks), Standard (1 named enemy
+ mooks), Major (2 named or 1 tough named with 4 harm), Deadly (telegraph it).

## 9. Using It as a Fallback for Another Game

1. Keep that game's setting, tone and character concepts.
2. Convert each character's best two attributes or skills into approaches/tags.
3. Keep signature mechanics the players love if they know them (e.g. Mouse Guard's conditions; the
   Marvel die's Fantastic effect as a 12+ critical).
4. Record the conversion in the bible's `## House Rules`.

## 10. AI GM Notes [Tier 3]

- Treat 7-9 as a real cost; it is the engine's main source of drama.
- Ask the player which approach they use only when it's unclear from the action.

## 11. Sources

Original to this repository; mechanics in the PbtA family (Apocalypse World) and Blades in the Dark's
position concept inspired it.

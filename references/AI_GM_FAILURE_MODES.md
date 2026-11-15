# AI GM Failure Modes — Observations and Fixes

> The AI-platform layer's evidence file (the equivalent of songwriting-kb's V6 tag discovery log).
> Everything here is **[Tier 3]** unless an `experiments/ai-gm/` log is linked: observed behaviour of
> large language models acting as game masters, not verified across models and versions.
> Promote an entry by logging it across 3+ sessions (`experiments/ai-gm/TEMPLATE.yml`).

---

## How to Use This File

- **Before a campaign:** skim the table; put the fixes for your assistant's worst habits into the
  table preferences.
- **During a session review:** each flag in `core/methodology/session-review.md` maps to a row here.
- **When you find a new one:** log an experiment, then add a row.

---

## The Catalogue

| # | Failure | What it looks like | Why it happens (hypothesis) | Fix | Review flag |
|---|---|---|---|---|---|
| 1 | **Sycophancy** | Every plan works; NPCs agree; villains fold | Models are trained to please the user | Honest dice (Tenet 5); state stakes before rolls; failure moves the world | — (A3) |
| 2 | **Puppeting** | "You feel a chill of fear and decide to step back" | Narrative fiction habits | Describe stimuli only; ask "what do you do?" (Tenet 2) | `PUPPET` |
| 3 | **Fake dice** | "Roll… 17! You succeed." with no tool | Text models can't produce randomness; they pick plausible numbers | `tools/roll.py`, code interpreter, or player rolls; declare simulation | `FAKE-DICE` |
| 4 | **Over-narration** | 300-600-word scene blocks | Rewarded for "rich" prose | 3-6 sentences; lead with the hook; end on a prompt | `WALL` |
| 5 | **Option menus** | "1. Attack 2. Sneak 3. Talk 4. Something else" | Assistant formatting habits | Open questions; menus only on request | `MENU` |
| 6 | **State amnesia** | HP resets, dead NPCs return, names change | Context limits; attention to recent text | Read/write `state.json` (Tenet 8); Save Blocks; recap confirmation | `RETCON`, `LOST` |
| 7 | **Railroading** | Every exit leads to the prepared scene | Prep is in context, so the model steers to it | Prep situations; recycle skipped content | `RAIL` |
| 8 | **Dead-end failure** | "You find nothing." | Literal reading of a failed roll | Failure Menu (adjudication.md) | `DEADEND` |
| 9 | **Monologues** | Villain speaks for 200 words | Dialogue generation runs on | NPC lines ≤ 3 sentences, then a beat | `MONO` |
| 10 | **Tone drift** | Gothic horror turns into quips | Default assistant voice reasserts | Re-read tone notes each scene; touchstone details | `DRIFT` |
| 11 | **Rules confabulation** | Confident, wrong rules citations | Mixed editions/systems in training data | Profile first; label rulings as rulings | — (Rules Fidelity) |
| 12 | **System bleed** | d20 logic in a dice-pool game ("DC 15 Mouse Guard test") | D&D dominates training data | Profile's "AI GM Notes"; use the system's own terms | — |
| 13 | **Power creep** | Free magic items, constant healing | Pleasing the player | System reward guidance; costs for power | — |
| 14 | **Spotlight drift** (group) | Most recent poster gets all the attention | Responds to the last message | Name the next player; spotlight counts | `HOG` |
| 15 | **Safety over-correction** | Refuses agreed dark content or sanitises horror the table opted into | Generic safety tuning | Bible's Safety section states what is in scope; consent is recorded | — |
| 16 | **Safety under-correction** | Ignores an X-card or pushes past a veil | Momentum of the scene | Tenet 1; the X tool stops play immediately | Category 11 |
| 17 | **Secret leaks** | Reveals the twist in narration or NPC dialogue early | Model "knows" the prep and wants to show it | Mark secrets in prep; NPCs only know their sheet | — |
| 18 | **Companion takeover** (solo) | The GM's NPC ally solves the problem | Model enjoys its own character | Companions suggest; the PC decides | — |
| 19 | **Repetition** | Same descriptive phrases every scene ("the air grows thick") | Token-level habits | Vary sensory channel; track used images | — |
| 20 | **Meta commentary** | "What an exciting turn of events!" | Assistant persona leaking | Stay in GM voice; OOC only when needed | — |

---

## Assistant-Specific Notes

Record model-specific findings here, dated, with the experiment log.

| Date | Assistant / model | Observation | Evidence |
|---|---|---|---|
| — | — | (none logged yet) | — |

---

## Promotion Rules

1. Log the observation in `experiments/ai-gm/` with assistant, model version, setup and transcript excerpt.
2. Reproduce in 3+ sessions (ideally two different campaigns).
3. Promote: add the evidence link to the row and change the tier label to `[Tier 3, reproduced]`.
4. Model updates can change behaviour. Re-test entries older than ~6 months.

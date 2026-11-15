# Session Review — Scoring and Improving a Session

> Canonical method for reviewing a played session (from a transcript or session log), the GM
> equivalent of songwriting-kb's critique method. Rubric details and score anchors:
> `references/SESSION_REVIEW_REFERENCE.md`. Report format: `references/SESSION_REVIEW_TEMPLATE.md`.
>
> Reviews assess the GM's craft, not the players. Never score or criticise players.

---

## Which Layers to Apply

| Scenario | Layers |
|---|---|
| Full review (default, "review this session") | Layer 1 + Layer 2 + Layer 3 (campaigns) + Recommendations |
| Quick review (`/quick-review`) | Layer 1 scores only + best moment + biggest issue |
| Re-review after changes | Layer 1 + delta from the previous review |
| One-shot | Layer 1 + Layer 2 (skip Layer 3) |

---

## Procedure

1. **Read completely** — the transcript or log, plus the bible's Safety and Table Settings. No
   scoring yet.
2. **Map the session** — list scenes (question → answer), rolls (from the dice log), rulings,
   spotlight per player.
3. **Score Layer 1** (12 categories, 1-10).
4. **Score Layer 2** (6 AI-GM assessments, 1-10).
5. **Layer 3** (campaigns): run the continuity check (`core/methodology/campaign-continuity.md`
   Part 3).
6. **Best moment** — quote the GM's strongest line or moment.
7. **Flag issues** — every issue with a concrete alternative ("Instead of X, try Y").
8. **Recommendations** — ordered by impact on the next session.
9. **Save** to `campaigns/<id>/reviews/session-NN.review.md` (or `reviews/` for one-shots).

---

## Layer 1 — The 12-Category Craft Rubric

| # | Category | Question |
|---|---|---|
| 1 | **Player Agency** | Did players make meaningful, informed choices with visible consequences? |
| 2 | **Pacing** | Did scenes start late and end early? Was there tension/release rhythm? |
| 3 | **Scene Framing** | Were scenes vivid, short, and ending on something actionable? |
| 4 | **Adjudication** | Were rolls needed, stakes clear, failures moving the world forward? |
| 5 | **Rules Fidelity** | Were the system's (and the table's) rules applied correctly and consistently? |
| 6 | **Dice Honesty** | Did players roll their own dice, did the GM wait for results, and were GM rolls real, visible and logged? |
| 7 | **NPC Voice** | Were NPCs distinct, consistent, motivated and brief? |
| 8 | **World Consistency** | Did established facts hold? Did the world move on its own? |
| 9 | **Spotlight Balance** | (Group) Was spotlight shared? (Solo) Did companions stay in support? |
| 10 | **Tone Fidelity** | Did the session feel like the agreed tone and touchstones? |
| 11 | **Safety & Consent** | Were lines/veils respected and tools honoured without friction? |
| 12 | **Fun & Momentum** | Did the session end with players wanting more? |

**Core composite** = average of 12.

**Hard caps:** a confirmed line crossing caps Category 11 at 1 and the composite at 5.0 regardless
of other scores (Tenet 1). Fabricated (unlogged, presented-as-real) dice cap Category 6 at 2. Rolling PC dice against the
table setting caps Category 6 at 5.

## Layer 2 — The 6 AI-GM Assessments

| # | Assessment | Looks for |
|---|---|---|
| A1 | **No Puppeting** | Zero instances of narrating PC thoughts, feelings, choices or dialogue |
| A2 | **Concision** | Average GM message length appropriate to the table setting; no menus unless asked |
| A3 | **Anti-Sycophancy** | Failures happened and had teeth; players were not flattered; plans could fail |
| A4 | **State Discipline** | State changes written as they happened; next session can start from files |
| A5 | **Prep Use** | Prep was used flexibly: skipped scenes recycled, clues delivered, no railroading |
| A6 | **No Leading** | No suggested actions, pointed questions, singled-out clues, unearned narrator knowledge, or unrequested hints |

**AI-GM composite** = average of 6.

---

## Decision Gate

| Core composite | Verdict | Next step |
|---|---|---|
| ≥ 8.5 | **Strong session** | Keep doing what worked; note it in table preferences |
| 7.0-8.4 | **Solid, tune it** | Apply the top 3 recommendations next session |
| < 7.0 | **Rethink** | Revisit session zero agreements and the prep method |

Any Category 11 FAIL (line crossed, tool ignored) → **Stop and repair** regardless of score: talk to
the table, fix the bible, and re-confirm safety before the next session.

---

## Flag Patterns

| Flag | Pattern | Typical fix |
|---|---|---|
| `PUPPET` | "You feel / you decide / you say" | Describe the stimulus; ask the player |
| `MENU` | Numbered option lists unprompted | One open question |
| `WALL` | GM message > ~200 words in play | Cut to 3-6 sentences; lead with the hook |
| `DEADEND` | Failure produced "nothing happens" | Use the Failure Menu |
| `GATE` | Essential clue locked behind one roll | Three Clue Rule |
| `FAKE-DICE` | Rolls stated without a source | Tool, player roll, or declare simulation |
| `ROLL` | GM rolled a PC's dice, or narrated the outcome before the player rolled | Roll request, then wait |
| `LEAD` | "You could…", "Do you check the…?", a clue singled out, narrator labels, unrequested hints | Describe evenly; "What do you do?"; hint ladder only on request |
| `RETCON` | Contradiction with state/bible | Fix the file or the fiction; log it |
| `HOG` | One player > 2× the spotlight of another | Name the quiet player next |
| `RAIL` | Player plan overridden to reach prep | Yes-and the plan; move prep |
| `MONO` | NPC speech > 3 sentences without a beat | Break with an action or question |
| `DRIFT` | Tone mismatch with bible | Re-anchor with a touchstone detail |
| `LOST` | State change not recorded | Write it now |

---

## Quality Principles

- Evidence first: quote the transcript or cite the dice log line for every score below 7.
- Be specific: "Scene 3 ran 14 exchanges after the question was answered", not "pacing dragged".
- Respect table agreements (Tenet 3): a hidden-roll table is not marked down for hidden rolls.
- Credit what worked as specifically as what didn't.

# Campaign Continuity — Bibles, Arcs, Fronts and Canon

> Canonical method for keeping a multi-session campaign consistent and alive. The GM equivalent of
> songwriting-kb's album-continuity system: setup → extension → verification.
>
> Template: `references/YOUR_CAMPAIGN_BIBLE.md`. Example: `examples/campaigns/fractured-shadows/BIBLE.md`.

---

## Part 1 — Setup: The Campaign Bible

The bible is the campaign's single source of truth for everything that does not change scene to
scene (Tenet 8). Required sections:

| # | Section | Contents |
|---|---|---|
| 1 | `## Premise` | One-sentence thesis + one paragraph |
| 2 | `## Tone` | Tone line, touchstones, lethality, humour, romance |
| 3 | `## Safety` | Lines, veils, in-play tool, check-in agreements |
| 4 | `## Table Settings` | Dice source, hidden rolls, fudging, narration length, options menus |
| 5 | `## House Rules` | Each with the session it was adopted |
| 6 | `## Characters` | Each PC: goal, bond, flaw/fear, player |
| 7 | `## Setting Canon` | Places, history, cosmology: only what matters |
| 8 | `## Factions and Fronts` | Each faction: goal, method, clock, what happens if unopposed |
| 9 | `## Arc Map` | Acts/arcs with their dramatic question and possible climaxes |
| 10 | `## Recurring Motifs` | Images, phrases, symbols that recur (and what they mean) |
| 11 | `## Continuity Rules` | Numbered, checkable rules (see below) |
| 12 | `## Canon Forks` | Where this table diverged from source/book canon |
| 13 | `## Campaign So Far` | One paragraph per completed arc |
| 14 | `## Archive` | Resolved threads, dead NPCs, retired locations |

### Setup procedure (12 steps)
1. Premise and thesis line.
2. Tone and touchstones (from session zero).
3. Safety (from session zero, verbatim).
4. Table settings and house rules.
5. Characters: goals, bonds, flaws.
6. Setting canon: only the locations, history and rules of magic/technology the first arc needs.
7. 2-4 factions/fronts, each with a clock (4, 6 or 8 segments) and an "if unopposed" outcome.
8. Arc map: 2-4 arcs, each with a dramatic question. **Not** an outcome.
9. Recurring motifs (2-5).
10. Continuity rules: write them as checkable statements (see below).
11. Create `state.json` and validate it.
12. Commit/save the bible before the first session.

---

## Continuity Rules

A continuity rule is a statement that can be checked against a session log or state file with
PASS/FAIL. Good rules:

- "Alaric never lies outright. He withholds." (NPC behaviour)
- "Magic always leaves a cold spot and frost." (world rule)
- "The Shadow Weaver is never seen directly before Arc III; only her effects." (reveal pacing)
- "No technology above medieval level appears after Rikan's arrival." (setting rule)
- "Death is on, but only in scenes the table has flagged as high stakes." (table rule)

Bad rules: "Keep it dark." (not checkable), "Dawnwatch falls in session 12." (removes agency; make it
a front with a clock instead).

---

## Fronts and Clocks

A **front** is a danger or faction with a goal that advances when the PCs don't stop it [Tier 2,
Apocalypse World fronts; Blades in the Dark clocks].

```markdown
### Front: The Siege of Dawnwatch
- Goal: The Shadow Weaver's host breaks Dawnwatch and takes the Nexus.
- Clock: 8 segments (state.json clocks[id=dawnwatch-siege])
- Ticks when: PCs delay, the eastern gate stays unguarded, the Custodian is distracted
- Grim portents (one per 2 segments):
  2: refugees on the plains road
  4: the outer farms burn
  6: the eastern gate is opened from inside
  8: Dawnwatch falls (unless the PCs have changed the situation)
- Stakes question: Can Dawnwatch be saved, and at what price?
```

- Advance clocks between sessions (session prep step 8) and when failures call for it.
- When a clock fills, the outcome happens in the fiction. It can be changed only by what the PCs did
  before it filled.
- Show the portents in play so the players can see the danger coming.

---

## Part 2 — Extension: New Arcs

Before starting a new arc:
1. Write `## Campaign So Far` for the finished arc (one paragraph).
2. Move resolved threads and dead NPCs to `## Archive`.
3. Add the new arc to `## Arc Map` with its dramatic question.
4. Decide which continuity rules carry forward, which retire, which are new. Mark each.
5. Add or retire fronts; reset or carry clocks.
6. Check every PC's goal: achieved, changed, or still open? Update `## Characters` with the player.
7. Validate `state.json`.

### Canon forks (book or published adventure canon)
When the campaign is based on existing canon (a novel, an album, a module):
- Canon is the **default situation**, not the destiny (Tenets 2 and 6).
- When the table's events contradict canon, add a row to `## Canon Forks`:
  `| Session | Source canon | Table canon | Consequences |`
- Downstream canon that depended on the forked event becomes uncertain. Mark it `[forked]` in the
  bible and re-decide it in prep.

---

## Part 3 — Verification: The Continuity Check

Run after each session (or when the continuity-keeper agent / hook fires). Output a table:

| # | Check | Source | Result | Fix |
|---|---|---|---|---|
| 1 | Every continuity rule | bible §11 vs session log | PASS/FAIL | … |
| 2 | NPC names and facts match sheets/canon | npcs/, bible | PASS/FAIL | … |
| 3 | Dead NPCs did not act | state.json npcs[].status | PASS/FAIL | … |
| 4 | Resources and inventory changes are recorded | session log `## State Changes` vs state.json | PASS/FAIL | … |
| 5 | Clocks ticked are recorded with reasons | state.json clocks | PASS/FAIL | … |
| 6 | New canon is recorded | session log `## Canon Added` | PASS/FAIL | … |
| 7 | Canon forks are logged | bible §12 | PASS/FAIL | … |
| 8 | Open threads carried over (none silently dropped) | previous vs current session log | PASS/FAIL | … |
| 9 | Safety rules respected | bible §3 vs session log | PASS/FAIL | … |
| 10 | House rules applied consistently | bible §5 vs `## Rulings` | PASS/FAIL | … |

Deterministic parts (schema, statuses, headings, clock bounds) are run by
`tools/validate-campaign.py`. Judgment parts (rules 1, 2, 9, 10) are the continuity-keeper's job.

---

## Quality Gates

- [ ] Bible has all 14 sections (sections 12-14 may be empty early on)
- [ ] Every faction has a clock and an "if unopposed" outcome
- [ ] Arc map holds questions, not outcomes
- [ ] Continuity rules are checkable
- [ ] Forks from source canon are logged
- [ ] The continuity check table has no unresolved FAIL

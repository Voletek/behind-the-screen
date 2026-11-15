# State Keeping — Files, Dice Logs and Save Blocks

> Canonical method for keeping a campaign's truth outside the AI's memory (Tenet 8: state over
> memory). Works with file-capable assistants (Kiro, Claude Projects, ChatGPT with files) and with
> plain chat (via Save Blocks).
>
> Schema details: `references/STATE_FORMAT_REFERENCE.md`. Deterministic checks:
> `tools/validate-campaign.py`. Dice: `tools/roll.py`.

---

## Why This Exists

Language models lose track of long conversations: details drift, the dead come back, inventories
reset, NPC names change. [Tier 3] The fix is mechanical: everything that must persist lives in a
file, the GM reads the file at the start, and writes the file as things change.

---

## The Campaign Folder

```
campaigns/<campaign-id>/
├── BIBLE.md                  Campaign bible: premise, tone, safety, house rules, canon, factions
├── state.json                Live state (schema: behind-the-screen/state@1)
├── dice-log.jsonl            Every logged roll, one JSON object per line (tools/roll.py --log)
├── characters/
│   └── <pc-id>.md            Player-owned character sheets (core/methodology/character-creation.md)
├── sessions/
│   └── session-01.md         Session logs (required headings below)
├── prep/
│   └── session-02.prep.md    Session prep (core/methodology/session-prep.md)
├── npcs/
│   └── <npc-id>.md           NPC voice sheets (core/methodology/npc-voice.md)
└── reviews/
    └── session-01.review.md  Session reviews (core/methodology/session-review.md)
```

One-shots use the same layout or a single file under `oneshots/<id>/ONESHOT.md` plus a `state.json`
for the pregenerated characters.

---

## What Goes Where

| Information | File | Changes how often |
|---|---|---|
| Premise, tone, lines & veils, house rules, setting canon, faction goals | `BIBLE.md` | Rarely (between arcs) |
| PCs' current resources, conditions, inventory; NPC status; clocks; threads; location; date | `state.json` | Every scene |
| What happened, rulings made, canon invented, spotlight | `sessions/session-NN.md` | Once per session |
| Rolls | `dice-log.jsonl` | Every roll |
| Plans for next session | `prep/` | Between sessions |

Rule of thumb: if the GM would need it to run the next scene correctly, it belongs in `state.json`.
If it explains why the world is the way it is, it belongs in `BIBLE.md`.

---

## Start-of-Session Load

Before the recap, the GM reads, in this order:
1. `BIBLE.md` — tone, safety, house rules (skim canon sections relevant to the current location).
2. `state.json` — the full file.
3. The latest `sessions/session-NN.md` — especially `## Open Threads` and `## Next Session`.
4. The latest `prep/` file, if any.
5. `systems/<id>/PROFILE.md` for the system named in `state.json`.

Then run `python3 tools/validate-campaign.py campaigns/<id>` if a shell is available, and fix any
FAIL before play.

---

## During Play: Write As You Go

Update `state.json` at the end of every scene, or immediately for:
- a PC dropping to 0 / taken out / dying
- an item gained or lost that matters
- an NPC killed, recruited or turned hostile
- a clock filled
- a thread resolved

In chat-only play, print a short **State Delta** line instead and fold it into the Save Block at the end:
```
Δ Lyra hp 18→9 · +Poisoned · Ghoul B dead · clock "Dawnwatch Siege" 3→4/8 · thread "Who opened the gate?" opened
```

---

## End-of-Session Save

1. Update `state.json` (increment `session`, set `location`, `in_world_date`).
2. Write `sessions/session-NN.md` with the required headings:

   | Heading | Contents |
   |---|---|
   | `## Recap` | 3-6 bullets: what happened |
   | `## Scenes` | One line per scene: question → answer |
   | `## Rulings` | Every ruling made, one line each, with reason (or "None") |
   | `## State Changes` | The deltas applied to `state.json` |
   | `## Open Threads` | Unresolved questions, hooks, promises made by NPCs |
   | `## Next Session` | Where play resumes; hooks the players showed interest in |

   Optional: `## Spotlight` (group play counts), `## Canon Added`, `## Safety Notes`.
3. Run `python3 tools/validate-campaign.py campaigns/<id>`.

---

## Save Blocks (Chat-Only Play)

When the AI cannot write files (plain ChatGPT/Claude chat, Discord bots, mobile apps), the GM prints a
Save Block at the end of every session. The player copies it, and pastes it at the start of the next
session along with the bundle (`tools/build-bundle.py`).

Format:

````markdown
=== SAVE BLOCK · behind-the-screen/save@1 ===
Campaign: Fractured Shadows · Session 3 · System: dnd-5e

Recap:
- The party crossed the Fractured Plains and reached Dawnwatch's outer wall.
- Alaric agreed to train Rikan, at a price not yet named.

Open threads:
- Who opened the eastern gate?

```json
{ "schema": "behind-the-screen/state@1", "...": "the full state.json content" }
```
=== END SAVE BLOCK ===
````

Rules:
- The JSON inside the Save Block is the full `state.json`, not a summary. It must validate.
- Save `sessions/session-NN.md`-style notes in the Recap and Open threads fields.
- At the start of a chat session, the GM's first action is to read the Save Block and confirm
  three facts back to the player ("You're at Dawnwatch's wall, Lyra is at 9 HP and poisoned, and the
  eastern gate is the open question. Correct?").
- A pasted Save Block can be checked: save it as a `.md` file and run
  `python3 tools/validate-campaign.py <file>`.

---

## The Dice Log

Every roll that mattered is a line in `dice-log.jsonl`. `tools/roll.py --log <file>` writes it:

```json
{"ts": "2026-11-14T20:15:03Z", "session": 3, "who": "Lyra", "why": "Stealth past the gate",
 "expr": "1d20+5", "dice": [14], "total": 19, "target": 15, "outcome": "success",
 "source": "tools/roll.py", "hidden": false, "fudged": false}
```

- `source` records where randomness came from: `player`, `tools/roll.py`, `code-interpreter`,
  `dice-bot`, `simulated`.
- Players roll their own characters' dice (Tenet 5). Log them with `"source": "player"`:
  `tools/roll.py "<expr>" --record "<faces>"` when they post faces, or `--total <n>` when they post a total.
- `fudged: true` only if the table allowed fudging at session zero (Tenet 5), and still logged.

---

## Canon Discipline

- **Invented at the table → recorded.** Names, places, prices, relationships. `## Canon Added` in the
  session log; promote to `BIBLE.md` when it becomes important.
- **Contradiction found:** the file wins (Tenet 8). If the file is wrong, the table agrees on the
  truth, and the file is fixed with a note in the session log.
- **Book/published canon vs table canon:** record forks in `BIBLE.md` under `## Canon Forks`
  (what the source says, what happened at this table, which session).

---

## Context Budget (long campaigns)

When the bundle plus state no longer fits the assistant's context window:
1. Keep only the last 2 session logs in context; older ones are summarised in `BIBLE.md` →
   `## Campaign So Far` (one paragraph per arc).
2. Archive resolved threads and dead NPCs into `BIBLE.md` → `## Archive`, removing them from
   `state.json` (they can be restored).
3. Load NPC sheets only for NPCs in the current location.
4. `tools/build-bundle.py --budget <chars>` reports the bundle size and warns when it exceeds the
   budget.

---

## Quality Gates

- [ ] `state.json` validates (`tools/validate-campaign.py`).
- [ ] The latest session log has all six required headings.
- [ ] Every roll that changed the fiction is in the dice log, with a source.
- [ ] Everything invented at the table this session is recorded.
- [ ] The next session can start from the files alone, without the chat history.

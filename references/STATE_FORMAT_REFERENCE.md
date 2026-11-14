# State Format Reference — `behind-the-screen/state@1`

> The schema for `state.json` and the JSON inside Save Blocks. Method:
> `core/methodology/state-keeping.md`. Validator: `tools/validate-campaign.py`.

---

## Top Level

| Key | Type | Required | Notes |
|---|---|---|---|
| `schema` | string | yes | Exactly `"behind-the-screen/state@1"` |
| `campaign` | string | yes | Campaign or one-shot id |
| `system` | string | yes | A folder in `systems/` (e.g. `dnd-5e`); unknown ids WARN |
| `session` | integer ≥ 0 | yes | Last completed session (0 before the first) |
| `mode` | `"solo"` \| `"group"` | no | Play mode |
| `location` | string | no | Where play resumes |
| `in_world_date` | string | no | Free text ("3rd of Thaw, year 412") |
| `party` | list of characters | yes, non-empty | PCs |
| `npcs` | list | no | Known NPCs |
| `factions` | list | no | Factions and standing |
| `clocks` | list | no | Fronts, dangers, projects |
| `threads` | list | no | Open questions and hooks |
| `flags` | object | no | Free-form booleans/values ("bridge_burned": true) |
| `notes` | string | no | Anything else |

## Character (`party[]`)

```json
{
  "id": "lyra", "name": "Lyra", "player": "Kira",
  "concept": "Freehold archer who counts every arrow",
  "level": 3,
  "stats": { "STR": 10, "DEX": 17, "CON": 13, "INT": 11, "WIS": 14, "CHA": 9 },
  "resources": {
    "hp": { "current": 9, "max": 24 },
    "spell_slots_1": { "current": 0, "max": 2 },
    "exhaustion": { "current": 1, "max": 6 }
  },
  "conditions": ["Poisoned"],
  "inventory": ["Longbow", "Quiver (14 arrows)", "Rope, 50 ft"],
  "goal": "Find out who opened the eastern gate",
  "notes": ""
}
```

- `stats` names come from `systems/<id>/profile.json` → `stats`. Unknown names WARN.
- `resources` are tracks `{ "current": n, "max": n }` (optional `"min"`, default 0). `current > max`
  or `current < min` FAILS. For harm-box systems, `current` = boxes marked.
- `conditions` are checked against the profile list when it is closed (`conditions_open: false`).

## NPC (`npcs[]`)

```json
{ "id": "alaric", "name": "Alaric Dawnwatcher", "status": "alive",
  "disposition": "friendly", "location": "Dawnwatch", "sheet": "npcs/alaric.md",
  "notes": "Promised to train Rikan; price not yet named" }
```

- `status`: `alive` · `dead` · `missing` · `captured` · `departed` · `unknown` (others FAIL)
- `disposition`: `hostile` · `unfriendly` · `wary` · `indifferent` · `neutral` · `friendly` ·
  `helpful` · `allied` · `unknown` (others WARN)
- `sheet` is a path relative to the campaign folder.

## Faction (`factions[]`)

```json
{ "id": "crimson-legion", "name": "Crimson Legion", "standing": "hostile", "goal": "Seize the Mark" }
```

`standing` is free text or a number, per system (Root: prestige/notoriety numbers).

## Clock (`clocks[]`)

```json
{ "id": "dawnwatch-siege", "name": "The Siege of Dawnwatch", "segments": 8, "filled": 3,
  "on_fill": "Dawnwatch falls unless the eastern gate is held", "visible": true }
```

`segments` ≥ 1 and `0 ≤ filled ≤ segments`, otherwise FAIL.

## Thread (`threads[]`)

```json
{ "id": "eastern-gate", "summary": "Who opened the eastern gate?", "status": "open",
  "opened_session": 3, "related": ["dawnwatch-siege"] }
```

`status`: `open` · `resolved` · `abandoned` · `dormant` (others FAIL).

## Dice Log Line (`dice-log.jsonl`)

Required: `ts`, `expr`, `total`, `source` (`tools/roll.py` · `player` · `code-interpreter` ·
`dice-bot` · `simulated`). Optional: `session`, `who`, `why`, `dice`, `target`, `outcome`, `note`,
`hidden`, `fudged`, `seed`.

## Session Log Headings

Required `##` headings: Recap, Scenes, Rulings, State Changes, Open Threads, Next Session.
Optional: Spotlight, Canon Added, Safety Notes.

## Bible: Retired Terms (optional section)

```markdown
## Retired Terms
- Luminous Forests → Aeloria Forest
```

The validator WARNs when a retired term appears in a session log or NPC sheet.

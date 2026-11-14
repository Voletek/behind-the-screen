# systems/ — Rules-System Profiles

> The rules layer (Tenet 9: system-neutral craft). `core/methodology/` describes how to run a game;
> a profile here describes how *this* game's dice, numbers and procedures work, and what an AI GM
> tends to get wrong in it.

Each system has two files:

| File | For | Contents |
|---|---|---|
| `PROFILE.md` | The GM (human or AI) | Resolution, difficulty, stats, conflict, GM procedures, advancement, AI GM notes |
| `profile.json` | `tools/validate-campaign.py`, `tools/roll.py`, `tools/build-bundle.py` | Stat names, resource tracks, conditions, dice mechanic |

## Available profiles

| id | Game | Dice | Licence of rules text | Profile depth |
|---|---|---|---|---|
| `dnd-5e` | Dungeons & Dragons 5th edition (2024 rules, via SRD 5.2.1) | d20 + modifier vs DC | CC-BY-4.0 (SRD 5.2.1) — rules may be quoted with attribution | Full |
| `mouse-guard` | Mouse Guard Roleplaying Game, 2nd ed. (Luke Crane, David Petersen) | d6 pool, 4-6 = success, vs Obstacle | Proprietary — summarised only | Summary |
| `tmnt` | Teenage Mutant Ninja Turtles & Other Strangeness (Palladium, Megaversal system) | d20 combat, percentile skills | Proprietary — summarised only | Summary |
| `root` | Root: The Roleplaying Game (Magpie Games, Powered by the Apocalypse) | 2d6 + stat: 10+ / 7-9 / 6- | Proprietary — summarised only | Summary |
| `marvel-multiverse` | Marvel Multiverse Role-Playing Game (Marvel, d616 system) | 3d6 with Marvel die + ability vs TN | Proprietary — summarised only | Summary |
| `rules-light` | Any game without a profile; also a standalone house system | 2d6 + trait: 10+ / 7-9 / 6- | This repo | Full |

"Summary" profiles describe the mechanics in our own words so an AI GM can run the game with a
player who owns the book. They do not reproduce rules text, tables, or setting material. When the
book and the profile disagree, the book wins (and please open a fix).

## Adding a system

Follow `core/methodology/builder.md` → "Add a System" and copy `PROFILE_TEMPLATE.md`. Check
`profile.json` with `python3 tools/check-repo.py`.

## profile.json fields

```json
{
  "id": "root",
  "name": "Root: The Roleplaying Game",
  "license": "proprietary-summary",
  "gm_title": "GM",
  "dice": { "mechanic": "pbta", "default_expr": "pbta+0" },
  "stats": ["Charm", "Cunning", "Finesse", "Luck", "Might"],
  "resources": ["injury", "exhaustion", "depletion"],
  "conditions": [],
  "conditions_open": true
}
```

- `dice.mechanic` is one of `d20`, `pool`, `pbta`, `d616`, `d100`, `fate`, `custom`.
- `resources` are track names that `state.json` characters may use as `{ "current": n, "max": n }`.
- `conditions_open: true` means the list is not exhaustive and unknown conditions only WARN.

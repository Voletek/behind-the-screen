# Systems Comparison — Resolution Families

> How the supported games decide outcomes, side by side. Use it to pick a system at session zero,
> to explain a new system to players, and to avoid "system bleed" (AI GM failure #12).

---

## Resolution Families

| Family | Roll | Read | Degrees | Games here |
|---|---|---|---|---|
| **d20 roll-over** | 1d20 + mod vs DC/AC | ≥ target succeeds | Pass/fail; natural 20/1 on attacks | `dnd-5e`, `tmnt` (combat) |
| **Percentile roll-under** | 1d100 ≤ skill % | ≤ succeeds | Pass/fail | `tmnt` (skills) |
| **Dice pool vs Obstacle** | Nd6, count 4-6 | successes ≥ Ob | Pass, or fail → twist / success with condition | `mouse-guard` |
| **PbtA bands** | 2d6 + stat | 10+ / 7-9 / 6- | Full / cost / GM move | `root`, `rules-light` |
| **d616** | 3d6 (one Marvel die) + ability vs TN | ≥ TN | Success; Fantastic (M on the Marvel die); Ultimate Fantastic | `marvel-multiverse` |

## Probability Notes

| Roll | Useful numbers [Tier 1, arithmetic] |
|---|---|
| 1d20 + 5 vs DC 15 | 55% |
| 2d20kh1 (advantage) + 5 vs DC 15 | ~80% |
| 2d6 + 1 (PbtA) | 10+: ~28% · 7-9: ~44% · 6-: ~28% |
| 2d6 + 2 (PbtA) | 10+: ~42% · 7-9: ~42% · 6-: ~17% |
| 4d6 pool, Ob 2 (4+ = success) | ~69% |
| 5d6 pool, Ob 3 | 50% |
| d616 Fantastic chance | 1 in 6 per roll (the Marvel die shows M) |

Run `python3 tools/roll.py "<expr>" --times 1000 --json` and count if you need others.

## What Each Family Wants from the GM

| Family | GM's main job |
|---|---|
| d20 roll-over | Set fair DCs; give advantage for good positioning; make failure interesting (RAW won't) |
| Dice pool vs Ob | Set Ob from the book; pick twist or condition on failure; run GM's/players' turns |
| PbtA bands | Trigger moves from the fiction only; make 7-9 hurt a little; make GM moves on misses |
| d616 | Set TNs from defenses; describe Fantastic results with flair; track Focus and Karma |
| Percentile | Apply situational modifiers to the %; keep combat bookkeeping visible |

## Choosing a System (session zero helper)

| The table wants… | Consider |
|---|---|
| Tactical combat, character builds, classic dungeons | `dnd-5e` |
| Collaborative storytelling, fast play, choices with costs | `root`, `rules-light` |
| Earnest small heroes, survival, seasons | `mouse-guard` |
| Superhero action with spectacle | `marvel-multiverse` |
| Retro gritty mutants, crunchy old-school feel | `tmnt` |
| A quick game tonight with no books | `rules-light` |

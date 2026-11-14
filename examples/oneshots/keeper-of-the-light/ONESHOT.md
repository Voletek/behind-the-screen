# Keeper of the Light — One-Shot
<!-- oneshot: keeper-of-the-light · system: dnd-5e · players: 1-4 · level: 3 · length: ~4 hours / 6-8 scenes -->

> Folk horror at a lighthouse, adapted from Voletek's concept album *Keeper of the Light*
> (songwriting-kb `examples/albums/keeper-of-the-light/BLUEPRINT.md`). SRD 5.2.1 creatures only.
> Album rules carried into play: **the thing below is never named**, and **the sea is always present**.

## Pitch
The lighthouse on Gullrock stopped sending its monthly letters. You are the relief crew sent across
the strait before the autumn storm. The keeper, Maren, is alive, and she does not want relief. She
wants you to keep the light burning tonight, whatever you see.

## Safety
- **Tone:** folk horror → cosmic dread. Dread over gore.
- **Default veils for this one-shot:** drowning described past one sentence; body horror on the
  drowned crew; harm to the keeper's cat.
- **Ask at the table:** phobias (deep water, tentacles, enclosed spaces).
- **In-play tool:** `X` alone on a line. Check in after the logbook scene and after the storm.
- **Lethality:** real but signposted; a PC who goes into the sea at the climax is choosing it.

## Pregenerated Characters
Level 3, SRD 5.2.1 classes. Each has a reason to be on the boat and a link to someone else.

| PC | Class | Concept | Why here | Link |
|---|---|---|---|---|
| **Oona Pell** | Fighter | Ex-harbour guard, practical, afraid of nothing on land | Paid double to escort the crew | Owes Tamsin her life |
| **Tamsin Rook** | Cleric (Life) | Chapel healer from the strait villages | Maren delivered her as a baby during a storm | Knows the old sea hymns |
| **Wick** | Rogue | Smuggler who knows the rocks around Gullrock | Running from a debt | Shares a secret route with Oona |
| **Dr. Ansel Vey** | Wizard | Lighthouse Board's engineer | Sent to replace the lamp mechanism | Has read the Board's sealed file |

Stats: build with the SRD 5.2.1 or use quick pregens in `state.json`. Solo: the player picks one; the
GM runs one other as a companion.

## Strong Start
The relief boat's engine dies two hundred yards from Gullrock. The light above you is **off**. In the
dark water around the hull, something rises just beneath the surface, slow and huge, then sinks as
the lamp sputters back on. On the jetty, an old woman with a lantern is waving you in, shouting the
same three notes over and over.

## Scenes (situations, not a sequence)
1. **The Jetty and Maren** · Maren (80s, iron-grey, warm, evasive) · *Will she let them in, and what will she admit?*
2. **The Lamp Room** · the mechanism is fine; the light is wrong (it pulses in a three-note rhythm) · *What is the light for?*
3. **What the Logbook Says** · sixty years of entries; the handwriting changes; the last page ends mid-sentence · *Who kept the light before Maren, and what happened to them?*
4. **The Depth Hymn** · Tamsin's hymn and the light's rhythm are the same tune · *Can they sing what the light sings?*
5. **The Storm** · clock `storm`; waves over the rock; the drowned crew of a lost ship climb the stairs · *Can they keep the light burning?*
6. **The Night the Light Died** · the lamp fails at storm 6 · *Who goes out to restart it?*
7. **Something Stirs Below** · the sea draws back; a vast shape rises · *What does it want?*
8. **Lullaby for Leviathan** · someone must become the light: Maren, a PC, or no one · *What will it cost to put it back to sleep?*

## Secrets and Clues
1. The light pulses in three notes; it is a lullaby, not a beacon.
2. Maren was the keeper's apprentice; the old keeper "went into the light" sixty years ago.
3. The logbook's last page: "It remembers the sun. If the light dies, it will go looking for—"
4. The Lighthouse Board's sealed file (Ansel): every keeper has died on duty; none left.
5. The drowned crew are the *Mercy of Hale*, lost forty years ago the one night Maren slept.
6. Tamsin's hymn, sung at the lamp, keeps the drowned back (advantage on checks to hold the stairs).
7. Maren is dying. She wants to end as the light, and she is afraid.
8. The thing below is not evil. It is old, it is sad, and it wants the warmth it remembers.
9. Wick's smuggling route passes a sea cave where the old keeper's lantern still burns underwater.
10. Anyone who "becomes the light" stays on Gullrock forever, as a voice in the lamp.

## NPCs
- **Maren, the Keeper:** wants the light kept and an apprentice to keep it. Speaks in short practical
  sentences and sea proverbs ("Tide doesn't ask"). Under pressure: sings. Never names the thing.
- **The Old Keeper (Ghost):** the voice in the logbook and the lantern in the sea cave. Clipped,
  formal, sad. Hostile only if the light is threatened.
- **Bramble, the cat:** knows when it's coming; hides under the lamp.

## Threats (SRD 5.2.1; party of 4 × level 3: Low 600 · Moderate 900 · High 1,600 XP)
| Encounter | Creatures | XP | Difficulty | Exit |
|---|---|---|---|---|
| Stairwell of the drowned | 1 Wight (captain) + 4 Zombies (crew) | 900 | Moderate | Hold the lamp-room door; sing the hymn |
| Tidepool things | 2 Giant Octopuses | 400 | Low | Climb out of reach |
| Sea cave | 1 Ghost (the Old Keeper) + 4 Zombies | 1,300 | High | Relight its lantern; promise to keep the light |

Check: `python3 tools/encounter.py --party 4x3 --creatures "cr3,cr1/4x4"`.

**The thing below** has no stat block. It cannot be fought. It can be soothed, bargained with, or fled.

## Clocks
- `storm` (6): ticks each scene after nightfall, and on failed checks to secure the lighthouse.
  At 6 the lamp fails.
- `waking` (8): ticks each round the light is out, and once per scene when the hymn is not sung.
  At 4 the sea draws back; at 8 it rises onto Gullrock.

## Endings
- **Lullaby:** someone becomes the light (Maren, by choice; or a PC). It sleeps. Bittersweet.
- **Bargain:** the PCs give it the warmth it remembers (the sun? the Old Keeper's lantern?). It sinks
  peacefully, and the light is no longer needed. Rare; earned through clues 8 and 9.
- **Waking:** the light dies for good. The PCs escape across a strait that is no longer empty.

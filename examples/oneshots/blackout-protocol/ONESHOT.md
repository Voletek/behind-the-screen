# Blackout Protocol — One-Shot
<!-- oneshot: blackout-protocol · system: marvel-multiverse · players: 1-4 · rank: 2 (street level) · length: ~3 hours -->

> A street-level superhero night. Original heroes and villains; play official heroes from your book if
> you prefer. Mechanics per `systems/marvel-multiverse/PROFILE.md` (the book is the authority).
> The Narrator is the GM.

## Pitch
At 9:14 p.m. every light in the borough goes out, and the backup generators at St. Agnes Hospital fail
with them. Phones work for eleven minutes, long enough for a message to reach every screen: **"The city
forgets you in the dark. We won't."** The heroes have until sunrise to restore power, keep the hospital
alive, and find out who wants the borough to need them.

## Safety
- **Tone:** street-level superheroes: rain, rooftops, neighbours, consequences.
- **Veils:** patients dying on screen; graphic injury.
- **In-play tool:** `X` alone on a line.

## Pregenerated Characters (heroes, rank 2)
| Hero | Concept | Key abilities | Power sets (from the book) | Hook |
|---|---|---|---|---|
| **Kestrel** | Parkour vigilante with kinetic boots | Agility, Vigilance | Super-speed or martial arts | Her grandmother is a patient at St. Agnes |
| **Ohm** | Electrician who absorbs and redirects current | Resilience, Logic | Elemental control (electricity) | The blackout feels *wrong* to her |
| **Patchwork** | Street medic with a healing factor | Resilience, Ego | Healing, resilience | Works nights at St. Agnes |
| **Mister Quiet** | Retired stage magician, illusions | Ego, Logic | Illusion | Recognises the message's handwriting font |

Build them with the book's rank 2 rules (15 minutes). The Health/Focus numbers in `state.json` are placeholders for quick play; recompute them with the book.

## Strong Start
Kestrel is mid-leap between two rooftops when the city goes dark under her. She lands on a fire escape
in pitch black. Three floors down, a car with no lights is driving the wrong way up the avenue, straight
at a crowd spilling out of a cinema.

## Scenes
1. **The wrong-way car** · *Can they stop it without anyone getting hurt?*
2. **St. Agnes** · generators sabotaged; 40 minutes of battery on the ventilators · *Who keeps the hospital alive?*
3. **The substation** · guarded by masked "volunteers" handing out flashlights · *Who are they, really?*
4. **The rally** · the Lanternbearers, a new gang posing as protectors, recruiting in the dark · *Will the neighbourhood follow them?*
5. **The tower** · their leader, **Gloam**, at the top of a dark skyscraper, holding the borough's grid hostage · *Can the heroes turn the lights back on, and win the street's trust?*

## Secrets and Clues
1. The blackout was caused from inside the utility's control system: an insider.
2. Gloam was a city engineer laid off after the last budget cut.
3. The Lanternbearers have been paid by a developer who wants the borough emptied.
4. Gloam's power drains light; she is weaker near Ohm's current.
5. The hospital saboteur is a frightened Lanternbearer recruit who wants out.
6. Mister Quiet's font clue: the message used a typeface from the utility's own emergency system.

## Threats
- **Lanternbearer thugs:** a mob (henchmen rules), clubs and stun batons, flashlights as signals.
- **Wattage**, Gloam's lieutenant: rank 2 brawler with electrical gloves.
- **Gloam:** rank 3 villain; darkness powers; wants the city to see her neighbourhood.

## Clocks
- `ventilators` (4): St. Agnes's battery. Ticks every scene the hospital is unattended.
- `lanternbearers` (6): neighbourhood joins the gang. At 6 they hold the borough by morning.

## Endings
- **Lights on, trust won:** the grid is back and the neighbourhood saw the heroes help.
- **Lights on, trust lost:** power returns but the Lanternbearers are now the local heroes (a sequel villain).
- **Dark until dawn:** the hospital loses patients or the borough burns. A grim sunrise.

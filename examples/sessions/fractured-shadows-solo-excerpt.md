# Example Transcript — Fractured Shadows, Session 1 (solo excerpt)
<!-- validate: skip -->

> Shows the conversation loop, **the player rolling their own dice**, **descriptions that don't
> lead**, a canon fork, the Strain house rule, and the name-revelation rule in a solo game.
> GM = the AI. System: `rules-light`. Matching files: `examples/campaigns/fractured-shadows/`.

---

**GM:** Cold first. Wet stone under your cheek, a slow drip somewhere to your left, and a smell of rot
with metal underneath it. You are small, smaller than you should be, and the only light in the
dark is coming from your own chest: three interwoven triangles, glowing in time with your heartbeat.
Somewhere ahead, something scrapes on rock and stops.

What do you do?

**Player:** I try to talk. Say "hello?" quietly.

**GM:** It comes out as a squeak, high and reedy, nothing like your voice. The scraping starts again,
closer, and now there are three sounds: two light, one dragging.

**Player:** OOC: I know this place. I designed the Whispering Caves. Can I use "I coded this" to know
the layout?

**GM:** OOC: Yes, that's your Developer's memory tag, once per session. You get an edge on finding a
way through. The cost: I tell you one way the real place differs from your design.

You know the river route. It's where you put it. But the cave is bigger than your map: the ceiling
is lost in the dark, and there are carvings on the walls you never made.

**Player:** I press myself into the rock and wait for them to come to me. When they pass, I go for the
one dragging the spear.

**GM:** Three goblins, larger than you remember making them, red eyes catching the Mark's glow. The one
with the broken spear limps past your crevice.

🎲 Rikan, roll Grace to strike from the shadows: 3d6, keep the best 2, +2 (edge: darkness) · at stake:
the other two see where you are — roll and post the result.

**Player:** 🎲 6, 2, 5

**GM:** 6 and 5 plus 2: 13, a critical. *(Logged: `roll.py "3d6kh2+2" --record "6,2,5"`.)*
Your claws find the back of its knee and it drops, shrieking. The other two spin toward the sound.

*(…the fight continues; one goblin is killed, the third breaks and runs…)*

**GM:** The last goblin bolts for the tunnel mouth.

🎲 Rikan, roll Grace to cut it off: 2d6+2 · at stake: it gets away into the Mire — roll and post the result.

**Player:** 🎲 4, 6

**GM:** 12, critical. You're in front of it before it knows you've moved. It freezes, shaking, blade
dropped. It's small up close. It smells of peat. What do you do?

**Player:** …I let it go. I step aside.

**GM:** It stares at you for one breath, then it's gone into the dark.

**Player:** OOC: Does he have a name?

**GM:** OOC: You didn't hear one. If you'd like him to have one for later, name him, or I can.

**Player:** OOC: You pick.

**GM:** OOC: Skrit. Noted. *(Canon fork logged: the book has Rikan kill all three.)*

**Player:** I search the bodies.

**GM:** Crude blades, scraps of oiled cloth, a smell of peat on everything. Under the leader, half
buried in loose stone, a shard of black glass the size of your palm, glowing faintly in the same
rhythm as the Mark.

**Player:** I pick up the shard.

**GM:** It's warm. The pulse jumps into your arm, and the Mark on your chest pulses back.
[Strain +1 → 1/6]

**Player:** Am I "the chosen one" now?

**GM:** Nothing here says so. The shard is warm, heavy for its size, and it hasn't stopped pulsing.

---

## What to notice

- **The player rolls their own dice.** The GM sends a roll request (what to roll, modifiers, what's at
  stake), stops, and narrates only after the player posts the faces. The GM logs them with `--record`.
- **No leading:** the shard is described with the blades and the cloth, not spotlighted; the GM never
  suggests picking it up, asking about Skrit, or following the river. Stakes use only what Rikan knows.
- **Answer what was asked:** "You didn't hear one" for the goblin's name; "Nothing here says so" about
  destiny. No extra hints.
- **No puppeting:** the GM never says what Rikan feels; the player decides to spare Skrit.
- **Canon rules:** no prophecy presented as true fate (Rule 6); the name "Draeven" is never used (Rule 1);
  the shard costs Strain (house rule).

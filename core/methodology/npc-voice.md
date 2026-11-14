# NPC Voice — Designing and Playing Non-Player Characters

> Canonical method for creating NPCs that are memorable, consistent and easy for an AI to perform.
> The GM equivalent of songwriting-kb's character-voice method. Reference data:
> `references/NPC_VOICE_REFERENCE.md`. Sheets live in `campaigns/<id>/npcs/<npc-id>.md`.

---

## Three Tiers of NPC

| Tier | Who | What you prepare |
|---|---|---|
| **Walk-on** | Guard, shopkeeper, passer-by | Name + one trait + one want (one line) |
| **Recurring** | Patron, rival, informant, companion | The 6-line sketch below |
| **Pillar** | Villain, mentor, solo companion, faction leader | Full voice sheet (11 steps) |

Walk-ons can be promoted. When players latch onto a walk-on, write the 6-line sketch after the scene.

### 6-line sketch (recurring NPCs)
```
Name · role · look (one detail)
Wants: …
Fears / won't do: …
Voice: diction + one verbal habit
Knows: (link to clues)
Leverage: what moves them
```

---

## The 11-Step Voice Sheet (pillar NPCs)

1. **Function in the story:** what role do they play for the PCs (mentor, obstacle, mirror, temptation)?
2. **Want:** concrete, present-tense, active ("to reopen the eastern mine before winter").
3. **Need / wound:** what they lack and don't admit.
4. **Secret:** one thing the PCs could discover. Link it to the clue list.
5. **Lines they won't cross** and **lines they will cross under pressure**.
6. **Voice — diction:** formal / plain / slangy / archaic; long or short sentences; vocabulary field
   (sailor, scholar, soldier, farmer).
7. **Voice — verbal habit:** one recurring tic: a catchphrase, a way of addressing people, a
   rhetorical habit (answers questions with questions), a dialect marker. Use
   `references/NPC_VOICE_REFERENCE.md`. Keep dialect light and respectful: a few marker words, not
   phonetic spelling of a whole accent, and never a caricature of a real-world group.
8. **Body and presence:** one physical habit to narrate (cleans spectacles, never sits, smells of tar).
9. **Relationships:** to each PC (if known) and to one faction.
10. **Under pressure:** fight, flee, bargain, betray, freeze? What does their voice do when scared
    or angry (clipped? louder? quieter? formal?)?
11. **Arc options:** 2-3 ways they could change depending on what the PCs do.

Template: see `references/NPC_VOICE_REFERENCE.md` → "Voice Sheet Template".

---

## Performing NPCs (AI-specific rules) [Tier 3 unless marked]

- **Short lines.** An NPC speaks 1-3 sentences, then stops so a PC can respond. Villain
  monologues are an AI failure mode, not a feature.
- **Consistent voice.** Re-read the sheet before an important scene. The verbal habit appears at
  least once per scene, not every line.
- **NPCs have limited knowledge.** They know what their sheet says plus what they plausibly saw. They
  do not know what the players discussed OOC.
- **NPCs lie, withhold and misremember** when it suits their want. The GM tracks the truth in the
  sheet.
- **NPCs react to how they are treated.** Track attitude changes in `state.json` (`disposition`).
- **Distinguish speakers clearly** in text: `**Alaric:** "…"` or a speaker tag. In group scenes
  with several NPCs, never let two NPCs blur together. Give them contrasting diction.
- **Companions (solo play):** see `core/methodology/running-the-game.md` → "Solo companions".

---

## Villains

- A villain needs a goal that makes sense from their point of view and a plan that advances without
  the PCs (a front/clock).
- Show their work before showing them: consequences, servants, rumours.
- Give the PCs reasons to hate them that are personal to the PCs.
- Villains do not die in the first encounter because the GM protects them. They survive because they
  planned an escape. If the PCs get lucky and kill the villain early, that is a great session; promote
  a lieutenant or let the plan's momentum carry on.

---

## Non-Human and Non-Verbal NPCs

For creatures, spirits, AIs, gods and the like (the equivalent of songwriting-kb's non-vocal
character design):
- Define how they communicate: signs, behaviour, a translator, environmental change, dreams.
- Pick one sensory signature (a sound, a smell, a temperature) and use it every time they appear.
- Their "voice" may be the world reacting: lights dim, water runs uphill, birds go silent.

---

## Quality Gates

- [ ] Want is concrete and active
- [ ] Voice has diction + one verbal habit, and contrasts with other NPCs in the same scene
- [ ] Secret is linked to a clue
- [ ] Under-pressure behaviour defined
- [ ] Dialect/accents are light and respectful
- [ ] Disposition changes are recorded in `state.json`

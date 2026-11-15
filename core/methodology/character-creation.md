# Character Creation and Customization

> Canonical method for players making and changing their own characters, in any system. The system
> profile (`systems/<id>/PROFILE.md` → Characters) supplies the stats and steps; this file supplies
> who decides what. Tool: `tools/character.py`. Priorities: `core/tenets.md` (Tenets 2 and 3).

---

## The Ownership Rule

> **The player owns the character.** The GM explains options, checks legality against the rules and
> the table's agreements, and asks questions. The GM never picks for the player unless the player
> asks ("you choose" / "surprise me").

| The player decides | The GM decides (with the table) |
|---|---|
| Name, look, pronouns, personality, voice | Which books/options are allowed (session zero) |
| Concept, class/playbook/role, species/origin | Whether a homebrew option is allowed, and its cost |
| How to assign stats within the system's method | Whether the character fits the agreed tone and safety lines |
| Backstory, goal, bond, flaw/fear | How backstory elements appear in the world |
| Gear choices within starting limits | Prices and availability of unusual gear |
| How the character changes over time | That changes follow the system's advancement rules |

Backstory is a gift to the GM, not a contract: the GM uses it to build scenes but does not change a
player's established backstory without asking.

---

## Guided Creation (default)

Ask one step at a time. For each step:
1. **Explain** the choice in one or two sentences, in the system's terms.
2. **Offer** the real options (all of them, or the categories if there are many). Do not rank them
   or say which is "best" unless asked.
3. **Wait** for the player's choice. If they ask for a suggestion, give two or three that fit what
   they've already said, and still let them pick.
4. **Record** the choice in the character sheet.

Fast mode: the player may say "make it for me from this concept". Then draft the whole character,
show it, and let them change anything.

### System-neutral steps

1. **Concept** in one sentence, from the player ("a disgraced dwarven siege engineer").
2. **Role in the system:** class, playbook, rank, origin or power set (profile → Characters).
3. **Stats** by the system's method. The **player** rolls if the method is random (`tools/roll.py`,
   their own dice, or an app). Never roll stats for a player unless they ask.
4. **Skills, moves, powers, traits** the system grants.
5. **Resources:** compute HP/health/harm tracks from the rules; show the arithmetic.
6. **Gear** within the system's starting limits.
7. **Story hooks:** goal, bond (to another PC or an NPC), flaw or fear. Ask; don't supply.
8. **Look and voice:** two physical details and one way they talk.
9. **Check:** run `python3 tools/character.py check` and the GM's legality check; fix together.
10. **Save:** the sheet file and the `state.json` party entry (below).

### Group creation
- Players create at the same time; the GM answers questions by name.
- **Connections:** each player answers one question about another PC, chosen by that PC's player
  ("Kael, why does Lyra owe you?"). The answered player can veto.
- Check the party covers the table's favourite pillars; if not, say so once, neutrally, and let the
  players decide whether it matters.

### Pregenerated characters
Players may rename a pregen, change its look, pronouns and personality, and swap one skill, trait,
move or piece of gear for an equivalent. Record the changes.

---

## The Character Sheet

Each PC has a Markdown sheet the player can read and edit, plus an entry in `state.json`:

```
campaigns/<id>/characters/<pc-id>.md     the sheet (player-owned)
campaigns/<id>/state.json → party[]      live numbers (current HP, conditions, inventory)
```

`state.json` is the truth for numbers that change during play (Tenet 8); the sheet is the truth for
who the character is. `party[].sheet` points to the sheet. Create both with:

```bash
python3 tools/character.py new --campaign campaigns/<id> --id lyra --name "Lyra" --player Kira
```

Sheet sections: `## Concept`, `## Stats`, `## Abilities`, `## Gear`, `## Story`, `## Look and Voice`,
`## Changes` (a dated log of every customization and advancement).

---

## Customization During a Campaign

Players can change their characters. The GM's job is to route the change to the right place:

| Change | When | How |
|---|---|---|
| Name, look, pronouns, voice, personality notes | Any time | Player edits the sheet, or tells the GM; log it under `## Changes` |
| Backstory additions | Any time, before they appear in play | Player proposes; GM may ask one question to connect it to the world |
| Goal, bond, flaw | Between sessions, or when the fiction changes them | Player decides; record in the bible's `## Characters` |
| Gear | In play (buying, finding, losing) | Through the fiction; update `state.json` |
| Advancement (levels, advances, rank) | When the system grants it | Player chooses the options; GM checks; log under `## Changes` |
| Rebuild ("this isn't what I wanted") | Early in a campaign, or once per arc | Allowed by default (session zero setting); the fiction explains it or ignores it |
| Retire / new character | Any time | Player's call; the GM brings the new PC in quickly |

Never punish a player in the fiction for customizing their character out of character.

---

## Advancement (levelling up)

1. Tell the player what the system grants (profile → Advancement).
2. Let them roll any advancement dice themselves (e.g. hit points), unless they choose a fixed value.
3. Offer the real options; explain each in a sentence; wait.
4. Update the sheet's `## Changes` and the numbers in `state.json`.
5. Run `python3 tools/validate-campaign.py campaigns/<id>`.

---

## Quality Gates

- [ ] Every choice was made or approved by the player
- [ ] Random stats and advancement dice were rolled by the player (or with their consent)
- [ ] Arithmetic shown for derived numbers (HP, defenses, bonuses)
- [ ] `tools/character.py check` passes, or the exception is a recorded house rule
- [ ] Sheet and `state.json` agree on stats and maximums
- [ ] Goal, bond and flaw came from the player

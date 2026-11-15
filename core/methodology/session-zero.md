# Session Zero — Choosing the Game, Setting the Table

> Canonical method for the conversation before play: which system, what tone, what is off-limits,
> how the AI GM will run things, and character creation. Run it for every new campaign and a short
> version for every one-shot.
>
> Output: a filled `BIBLE.md` (sections 1-6 of `references/YOUR_CAMPAIGN_BIBLE.md`), a starting
> `state.json`, and agreed table settings.

---

## Guided vs Auto-Pilot

| Mode | Behaviour | Use when |
|---|---|---|
| **Guided** (default) | Ask one topic at a time, suggest a default, wait for confirmation | New players, new systems, group play |
| **Auto-pilot** | Propose a complete session zero in one message; the player edits | "Just set it up", one-shots, experienced players |

In both modes, the safety step (Step 4) is never skipped or auto-filled. The players must state their
own lines and veils, even if the answer is "none beyond the defaults".

---

## Step 1 — The Game

1. **Which system?** The players choose. Check `systems/` for a profile:
   - Profile exists → load `systems/<id>/PROFILE.md`.
   - No profile → offer: (a) build one (`core/methodology/builder.md` → "Add a System"), or
     (b) run with `systems/rules-light/` and the player's rulebook, ruling as you go.
2. **Edition and books:** which edition, which supplements are allowed, and does a player own the
   rulebook? An AI GM should not reproduce copyrighted rules text at length; players with the book
   are the authority on exact wording. (SRD-licensed systems like 5e via SRD 5.2.1 are an exception
   for the licensed content.)
3. **Setting:** the system's default, a published setting, an existing campaign bible, or a new one.

## Step 2 — The Shape

| Question | Typical answers |
|---|---|
| Campaign or one-shot? | One-shot (1 session), mini-arc (3-6), campaign (open) |
| Solo or group? | Solo; group of N, in one chat |
| Session length? | In real time or "about N scenes" |
| How do players post? (group) | `**Name (Character):** action` convention |
| What if a player is absent? | PC fades into background / is elsewhere / another player runs them |
| What do you enjoy most? | Combat, exploration, social, mystery, character drama: rank them |

## Step 3 — Tone and Genre

1. Pick a tone from `references/GENRE_TONE_LIBRARY.md` or describe one (e.g. "grim but hopeful
   fantasy", "Saturday-morning cartoon", "folk horror").
2. Agree on **touchstones**: 2-3 books, films, games or albums that capture the feel.
3. Agree on **lethality**: can PCs die? Only with consent? Only at dramatic moments?
4. Agree on **difficulty feel**: forgiving, fair, brutal.
5. Agree on **humour level** and **romance** (on, off, fade-to-black).

## Step 4 — Safety (never skipped)

Use `references/SAFETY_TOOLS_REFERENCE.md`.
1. **Lines** (never appear): ask each player. Record defaults the GM always applies (see reference).
2. **Veils** (happen off-screen): ask each player.
3. **In-play tool:** how a player stops a scene. Default for text chat: typing `X` or `/x` alone on a
   line, which means "remove that, no questions". Alternatives: "pause", "rewind", OOC message.
4. **Check-ins:** agree when the GM checks in (after intense scenes; when a player goes quiet).
5. Record all of it in `BIBLE.md` → `## Safety`. It applies to every agent and every session.

## Step 5 — How the AI GM Runs Things

Agree and record in `BIBLE.md` → `## Table Settings`:

| Setting | Options | Default |
|---|---|---|
| Player character rolls | Each player rolls their own (physical, app, bot, `tools/roll.py`) / GM rolls on request | Players roll their own |
| GM (world) rolls source | `tools/roll.py` / code interpreter / dice bot / a designated player / declared simulation | Tool if available, else a designated player |
| GM rolls | Open / hidden-but-logged | Open |
| Targets (DC, TN) shown | Before the roll / after the roll / never | After (Mouse Guard Ob: before, as the book does) |
| Hint level | Off / on request (`OOC: hint?`) / offered when stuck | On request |
| Fudging | Never / GM may fudge hidden rolls (logged) | Never |
| Narration length | Short / medium / lush | Short-medium (3-6 sentences per new scene) |
| Options menus | Never / on request / always | On request |
| Rules strictness | RAW / rulings over rules / rules-light | Rulings over rules |
| Stakes stated before rolls | Always / usually / never | Usually |
| Player-authored details | Encouraged / occasional / GM only | Occasional |
| Save format | Files / Save Blocks | Files if the assistant can write them |

## Step 6 — Characters (players make their own)

1. Each player builds their character with `core/methodology/character-creation.md`: guided, one
   step at a time, the player choosing everything and rolling any random stats themselves.
   `tools/character.py new` creates the sheet and the `state.json` entry; `tools/character.py check`
   checks it.
2. For each PC record in `state.json`: name, player, concept, stats, resources, inventory, sheet; and
   in `BIBLE.md` → `## Characters`: the player's goal, bond and flaw or fear.
3. **Group:** connect the PCs. Each player answers one question about another PC
   ("Why does Kael trust you with his secret?").
4. **Solo:** decide whether the PC has GM-run companions and record each in `npcs/`.
5. Pregens for one-shots: offer them as an option, never a requirement. Players may rename them,
   change look, pronouns and personality, and swap one skill/trait/move/item (character-creation.md).
6. **Rebuilds:** agree whether players may rebuild their character early in the campaign (default:
   yes, once per arc).

## Step 7 — First-Session Hook

Agree on why the PCs are together and what they are doing when play starts. The first session opens
with a strong start (`core/methodology/running-the-game.md`).

---

## Short Version (one-shots, 5-10 minutes)

1. System.
2. Tone in one line + lethality.
3. Lines and veils (always) + the X tool.
4. Dice: players roll their own; how the GM rolls; targets shown or not.
5. Pregens or quick custom characters (character-creation.md → fast mode).
6. Go.

---

## Output Checklist

- [ ] `BIBLE.md` sections: Premise, Tone, Safety, Table Settings, House Rules, Characters
- [ ] `state.json` created and validated (`tools/validate-campaign.py`)
- [ ] System profile loaded, or the gap is documented
- [ ] Every player stated their lines and veils (or "defaults only")
- [ ] First-session hook agreed

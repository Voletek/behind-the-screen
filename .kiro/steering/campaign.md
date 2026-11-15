---
inclusion: auto
name: campaign
description: Campaign framework - campaign bibles, fronts and clocks, arc maps, continuity rules, canon forks from books or published adventures, campaign-specific steering and continuity hooks, and arc extension. Use for campaign setup, continuity checks, canon questions, new arcs, and bible work.
---

# Campaigns — Continuity Framework (quick reference)

> Canonical: `core/methodology/campaign-continuity.md`. Template: `references/YOUR_CAMPAIGN_BIBLE.md`.
> Example: `examples/campaigns/fractured-shadows/`.

## The bible is the campaign's truth

14 sections: Premise · Tone · Safety · Table Settings · House Rules · Characters · Setting Canon ·
Factions and Fronts · Arc Map · Recurring Motifs · Continuity Rules · Canon Forks · Campaign So Far ·
Archive (+ optional Retired Terms, Open Canon Questions).

## Rules of thumb

- Arcs hold **questions**, not outcomes. Fixed events become **fronts with clocks**.
- Continuity rules must be **checkable** (PASS/FAIL against a log).
- Source canon (novels, albums, modules) is the default situation, not destiny. Log forks.
- When sources disagree, add an Open Canon Question; never resolve it silently.

## Campaign-specific steering and hooks (Kiro)

1. Copy `examples/campaigns/<id>/steering.md` to `.kiro/steering/<id>.md` (`inclusion: fileMatch`).
2. Copy `examples/campaigns/<id>/continuity-hook.json` to `.kiro/hooks/<id>-continuity.json` and edit
   its matcher and prompt.
3. Run `python3 tools/check-repo.py`.

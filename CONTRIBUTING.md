# Contributing

Thanks for helping improve Behind the Screen. The full guide is
[SOP 08 — Contributing](.kiro/sops/08-contributing.md). This page is the short version.

## Ground rules

- **One source of truth.** Methods live in `core/methodology/`. Steering, SOPs, skills and agents
  summarise them or point to them; they don't redefine them. Fix the canonical file first.
- **System-neutral core.** Anything specific to one RPG goes in `systems/<id>/`, never in `core/`.
- **Label evidence.** `[Tier 1]` published rules text or scholarship, cited · `[Tier 2]` named,
  widely used GM craft heuristic · `[Tier 3]` AI-GM or community observation (unverified). AI
  behaviour claims are Tier 3 until logged in `experiments/ai-gm/` across 3+ sessions.
- **Respect rulebook copyright.** Proprietary systems (Mouse Guard, Root, Marvel Multiverse, TMNT,
  and most others) are **summarised in your own words**. Never paste rules text, move lists, tables,
  stat blocks or setting prose. Openly licensed text (SRD 5.2.1, CC-BY-4.0) may be used with its
  attribution.
- **Respect real people and cultures.** NPC dialect is light-touch; no caricatures of real-world groups.
- **No personal content in universal files.** Your table's preferences go in
  `.kiro/steering/table-preferences.md` or `examples/preferences/`; your campaigns in `campaigns/`.
- **Credit sources** in `CREDITS.md`; paraphrase, don't paste.

## Workflow

1. Branch from `main`: `feature/…`, `fix/…`, `docs/…`, `system/<id>`, `oneshot/<id>`.
2. Make your change and run the checks:
   ```bash
   python3 -m unittest discover -s tests            # tool tests
   python3 tools/check-repo.py                      # links, includes, agents, hooks, steering, skills, JSON, profiles
   python3 tools/validate-campaign.py examples/ campaigns/ oneshots/   # no FAIL allowed
   ```
3. Use conventional commit messages (`feat: …`, `fix: …`, `docs: …`, `chore: …`).
4. Open a pull request against `main` describing what changed and why. CI runs the same checks.

## Kiro file conventions

- **Hooks:** Kiro v1 JSON in `.kiro/hooks/*.json` (`version: "v1"`, `hooks[]` with `trigger`,
  optional `matcher`, `action` of type `command` or `agent`). On-demand workflows are steering files
  with `inclusion: manual`.
- **Steering:** front matter must be the first bytes of the file. `inclusion` is `always`, `auto`
  (needs `name` + `description`), `fileMatch` (needs `fileMatchPattern`) or `manual`.
- **Agents:** load files with `resources:` (`file://…`) in the front matter.
- **Skills:** `name` must match the folder; reference supporting files by plain path with an
  explicit "read X" instruction.
- **System profiles:** `systems/<id>/PROFILE.md` + `profile.json` whose `id` matches the folder.

# SOP 08: Contributing

> Add systems, one-shots, references and fixes to the repository.
>
> **Canonical method:** `CONTRIBUTING.md`. This SOP is the step list; if they diverge, `core/` wins.
> **Agent:** builder · **Time:** Variable

---

## Prerequisites

- A fork or branch; Python 3.9+

## Procedure

1. Branch: `feature/…`, `fix/…`, `docs/…`, `system/<id>`, `oneshot/<id>`.
2. Put method changes in `core/methodology/` first; summaries elsewhere follow.
3. Label evidence tiers. Paraphrase sources; credit them in `CREDITS.md`.
4. Never copy proprietary rulebook text, tables or setting prose.
5. Run `python3 -m unittest discover -s tests`, `python3 tools/check-repo.py`, `python3 tools/validate-campaign.py examples/ campaigns/`.
6. Conventional commit messages; open a PR to `main`.

## Done When

- [ ] CI passes

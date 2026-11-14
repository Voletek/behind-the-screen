---
inclusion: manual
description: Start a new game - choose the system, shape, tone, safety tools, table settings and characters, then create the campaign files. Invoke with /session-zero or #session-zero.
---

# Session Zero (manual command)

> Run with `/session-zero` or `#session-zero`. Canonical: `core/methodology/session-zero.md`.
> Read it if it isn't in context.

1. Ask guided or auto-pilot (default guided).
2. Steps 1-7: game → shape → tone → **safety (never skipped)** → table settings → characters →
   first-session hook.
3. Create `campaigns/<id>/` with `BIBLE.md` (from `references/YOUR_CAMPAIGN_BIBLE.md`, remove its skip
   marker) and `state.json`; run `python3 tools/validate-campaign.py campaigns/<id>`.
4. Offer to prep session 1 (session-planner agent) or start now with a strong start.

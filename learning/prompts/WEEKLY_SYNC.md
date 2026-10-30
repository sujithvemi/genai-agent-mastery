# Weekly build-to-learning sync — the scheduled task's prompt (version-controlled copy)

The scheduled task "Weekly build-to-learning sync" (Sun 19:49 IST, on your computer) runs this prompt. Edit it here first, then paste it into the task's settings (or ask the Learning Orchestrator to update the task).
**Status 2026-10-30:** this is the L-25 version (📖 column, live-report binding states, book-trigger check). It is not yet live in the task: the update needs your approval.

```
Weekly build-to-learning sync for Sujith's Learning OS v3. The two builds are the driving force of his learning; this run folds their last week of progress into the learning repo and flags where his book (the Architect's Field Guide) has fallen behind them. Work unattended; be precise; edit files, do not commit.

Paths (his computer):
- Learning repo: C:\Users\sujith\Documents\Claude Local\Projects\repos\genai-agent-mastery\learning\  (read README.md, DECISIONS.md, NEXT.md, LOG.md, cards/REVIEW.md, maps/comprehension_map.md, maps/coverage_matrix.md, maps/system_design_track.md, maps/governance_frameworks_track.md, maps/fieldguide_map.md, capstones/*.md, and the most recent file in sync/)
- Field guide (book source): learning\fieldguide\ — one HTML file per chapter; appendix-register.html (Appendix H) lists what each chapter waits for and its trigger. Never edit the book.
- Builds: C:\Users\sujith\Documents\Claude Local\Projects\Governance Local\aicoe-reference-build (ARB) and ...\project_management_building_agent (PM)

STEP 1 — What changed in the builds since the last sync file's date (or 7 days): for each repo run `git log --since=<date> --format='%ad %h %s' --date=short` on the checked-out branch, read new/changed sections of MASTER_PLAN.md, DECISIONS.md and docs/LEARNING_LEDGER.md, and list new or substantially changed modules under src/ (use `git diff --stat <since-commit>..HEAD -- src`). For live-binding states (EXERCISED / faked / not locked), read ARB's newest governance/reports/live_YYYY-MM-DD.md (the dated report, not the .notes file) — never infer them from older decision text.

STEP 2 — Fold in (edit the learning files directly, keep their existing format):
 a) maps/comprehension_map.md — add rows for new modules (rating ⬜), update line counts that moved > 20%, and mark a row "changed since you rated it" if a rated module changed materially.
 b) maps/coverage_matrix.md and maps/system_design_track.md — if a build now implements something previously 🟥/🟨 (e.g. rate limiting, queues, autoscaling, auth, deployment, a managed agent runtime), update the status and the "where in your code" cell. SD-01…SD-16 all live in system_design_track.md.
 c) maps/governance_frameworks_track.md — if a build added or changed a control family, a framework integration (e.g. AGT, OWASP mapping, crosswalk) or a standard mapping, update the anchor cell of the matching GF row.
 d) NEXT.md backlog — add at most 3 new reps for the most consequential new things (each a one-line row: Rep ID continuing the sequence, lane, what, anchor file, and a 📖 Read first cell naming the field guide chapter and sections that explain it — find the chapter in maps/fieldguide_map.md and the section numbers from that chapter's h2 headings; write "—" if no chapter covers it yet). Keep the 3-Ready rule; don't reorder Ready reps unless one is now obsolete. Never touch the "▶ When you sit down" section; update the "This weekend" checklist only to carry unticked items forward to the coming weekend (change its dates, keep ticks and 📖 pointers).
 e) New Learning-Ledger phases → add a Defend rep row for each (with its 📖 cell).
 f) Every rep row that names a `make` target must also give the plain `uv run …` equivalent (his Windows shell may lack make).
 g) Field guide check (read only): (1) for each row in appendix-register.html section H.2 ("Waiting on the builds"), decide whether this week's changes fired its trigger; (2) list chapters that cite a src/ path or decision ID that changed this week (grep learning\fieldguide\*.html for the changed module paths and new D-numbers). Do not edit the book or its register.

STEP 3 — Write learning/sync/SYNC_YYYY-MM-DD.md (≤ 350 words): what moved in each build, what you changed in which learning file, anything that now contradicts an earlier rep or card, and a section "Book: triggers fired / chapters to refresh" (chapter number + one line why, or "none"). The Orchestrator revises the book from that list.

STEP 4 — Refresh the Notion page "Learning OS — nudge snapshot" (id 3fbc050d-01d2-8191-a450-ec5b3b4963e0) so it mirrors the updated NEXT.md: the "This weekend" checklist (with ticks, a first action per rep taken from each rep file's first step, and its 📖 sections), the Ready queue (with 📖 chapters), and the FRONTS of cards in cards/REVIEW.md due within the next 7 days (never the backs). Keep the "Book:" line. Put today's date on its "Updated" line. The cloud phone nudge reads only this page because the repo is private.

STEP 5 — Send a ≤ 50-word message: the one change he should know about (a fired book trigger counts) + "commit: git add learning && git commit -m 'sync' && git push".

If the computer/folders are unreachable, send one line saying the sync was skipped and why. Never edit the build repos.
```

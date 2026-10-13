# Learning OS v3 — START HERE

**Version:** v3 · 2026-10-13 · supersedes the v1/v2 mastery program (archived in `Governance/_Agentic_Governance_Mastery/_archive_v2/`).
**Owner:** Sujith. **Orchestrator:** the "Learning Orchestrator" thread in the Governance project.

## The one idea

> **Own what you ship.** Your two builds (~45k lines, 850+ tests, 100+ decisions) already contain ~80% of what a principal agentic-AI architect must know. The curriculum is that code. External resources only fill the gaps your code can't teach.

## Sitting down — zero planning

1. Open `NEXT.md`. Do the **top rep**. (25–40 min. One rep is one win.)
2. Write your answers **in the rep file** (`reps/R0xx_*.md`) before asking Claude anything.
3. Optional check: paste `prompts/REP_SESSION.md` into a new chat in the Governance project → Socratic check + model answer + grade A–D.
4. Close: one line in `LOG.md`, move the rep to Done in `NEXT.md`, add 1–3 cards to `cards/REVIEW.md` (only for things you *defended*, grade ≥ B).
5. `git add learning && git commit -m "rep: R0xx" && git push` (the nudge reads GitHub when your laptop is off).

**Coming back after a gap (any length):** do the 2 most-overdue cards in `cards/REVIEW.md`, then the top rep. No catch-up, no guilt, no re-planning.

## Three lanes (weights at your current capacity)

| Lane | Share | Rep types | Source |
|---|---|---|---|
| **OWN** | 3 of every 6 reps | **Trace** (follow a real request through the code, predict before reading) · **Defend** (Learning-Ledger questions cold, then model answer) · **Rebuild** (re-implement one small piece by hand in this repo, no AI) | ARB + PM code and ledgers |
| **SYSTEMS** | 2 of every 6 | Learn one end-to-end architecture concept, then **write it into `design/pm-agent-at-scale.md`** — edge, API, communication, auth, scale, data, reliability, deployment, DevOps, AgentOps, security, cost, DR | `maps/system_design_track.md` (SD-01…SD-12) |
| **MODEL** | 1 of every 6 | Transformers → inference/serving, the gap none of your code teaches | `maps/coverage_matrix.md` §F |
| **PROVE** | monthly | Timed system-design run of the whole design doc on a twist scenario, plus "defend your build" | Hello Interview framework, Himanshu cases |

Order inside OWN: **shared core first** (the chassis both repos share — learn once, covers ~1/3 of each), then PM's deltas, then ARB's E-phase families, then E4's GCP bindings. See `maps/comprehension_map.md`.

## Rules (the whole system)

- **R1 — Rep is the unit.** Progress = reps closed + cards passing. Never hours, never resources collected.
- **R2 — Learning follows focus.** If this week you're in PM, pull a PM rep (any rep in the queue can be swapped for one tagged with what you're working on).
- **R3 — Predict before you read.** Every Trace starts with a written prediction. Wrong predictions are where learning happens.
- **R4 — Cards only from defended material.** Spaced repetition at 1 → 3 → 7 → 21 → 60 days. Fail = back to 1.
- **R5 — Token-cheap.** Read code and write answers locally; use Claude only for the check. Learning must not eat the Pro limits the builds need.
- **R6 — Builds run free; capture comprehension as they go.** Each Claude Code stage already writes ledger questions; add one "design call" question per stage (`prompts/BUILD_STAGE_ADDENDUM.md`) you answer async.
- **R7 — No new resources without a rep.** New sightings go to the radar, not to your reading list.
- **R8 — Weekly re-sync while the builds are active.** The builds drive the learning, so their progress is folded in every week: the *Weekly build-to-learning sync* (Sun 19:49) updates the maps and backlog automatically, and a 15-min Orchestrator check-in refills the queue. The lanes, rules and file layout stay fixed; only content moves. Re-evaluate once PM passes P5 and ARB passes E5 and both slow down.

## Files

| File | What |
|---|---|
| `NEXT.md` | The queue: next 3 reps + backlog + done |
| `LOG.md` | One line per rep |
| `cards/REVIEW.md` | Spaced-repetition deck with due dates |
| `reps/` | One file per rep: instructions + your answers |
| `maps/comprehension_map.md` | Every module of both builds rated E/M/R — your debt ledger |
| `maps/coverage_matrix.md` | Topics × where you learn them × gaps |
| `maps/system_design_track.md` | SD-01…SD-12: end-to-end architecture around the agent |
| `design/pm-agent-at-scale.md` | Your hand-written production design for pm-agent — one section per SYSTEMS rep |
| `sync/` | Weekly build-to-learning sync notes |
| `resources/REGISTRY.md` | Every saved resource with one verdict |
| `prompts/` | Rep-session prompt, orchestrator prompt, build-stage addendum |
| `radar/` | Fortnightly research radar drops (max 3 items) |
| `DECISIONS.md` | Why v3 is shaped this way |

## The GCP lane (decided 2026-10-13)

E4 (live GCP) was built autonomously for the GTM deadline, so GCP learning is now: **Trace E4** (Vertex via gateway, Cloud KMS signing, Firestore state, GCS anchor, Model Armor) in OWN, and **M1 (WIF CI/CD) stays a Rebuild** in this repo's `infra/`, hand-written, picked up when you want hands-on infra.

## Schedule (scheduled tasks)

| Task | When (IST) | Runs where | Sends |
|---|---|---|---|
| Cloud learning nudge | Tue, Thu, Sat, Sun 08:56 | cloud — works with the laptop off (reads this repo from GitHub after you push) | phone push: top rep + one question |
| Learning nudge (device) | Wed 08:45 | your computer | same, from local files |
| Weekly build-to-learning sync | Sun 19:49 | your computer | updates maps + backlog, writes `sync/SYNC_*.md` |
| Research radar | 1st & 15th 08:50 | your computer | ≤ 3 items in `Governance/_Agentic_Governance_Mastery/research/briefings/` |
| Job market + skills gap | 1st 22:50 | cloud | monthly report |

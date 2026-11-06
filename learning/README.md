# Learning OS v3 — START HERE

**Version:** v3 · 2026-10-13 · supersedes the v1/v2 mastery program (archived in `Governance/_Agentic_Governance_Mastery/_archive_v2/`).
**Charter (L-27):** this is your personal Claude — no clients. Client work happens in your enterprise Claude; a future personal-consulting client gets its own project. Everything here is synthetic or public.
**Owner:** Sujith. **Orchestrator:** the "Learning Orchestrator" thread in the Governance project.
**Updated:** 2026-10-30 — the *Architect's Field Guide* (edition 1, 55 chapters) is now the consume step for every rep (L-23); SYSTEMS gained SD-13…SD-16 for the agent lifecycle (L-24). 2026-10-31 — `maps/capability_gap_register.md` records what is still missing to evaluate, compose, decide and build platform components; it opens after the current queue (L-26).

## The one idea

> **Own what you ship.** Your two builds (~45k lines, 850+ tests, 100+ decisions) already contain ~80% of what a principal agentic-AI architect must know. The curriculum is that code. External resources only fill the gaps your code can't teach. The **Architect's Field Guide** (`fieldguide/`) explains every concept through that code: a chapter is the *consume* step, the rep is the *defend* step.

## Sitting down — zero planning

**Open `learning.code-workspace` (repo root) → `NEXT.md` → the ▶ section at the top. Everything you need for the session is written there.**


1. Open `NEXT.md`. Do the **top rep**. (25–40 min. One rep is one win.)
2. Read the field guide sections on the rep's **📖** line (10–20 min; phone or PDF is fine, ideally before the session). Trace rep: predict first, then read. Defend rep: read, close the book, answer cold.
3. Write your answers **in the rep file** (`reps/R0xx_*.md`) before asking Claude anything.
4. Optional check: paste `prompts/REP_SESSION.md` into a new chat in the Governance project → Socratic check + model answer + grade A–D.
5. Close: one line in `LOG.md`, move the rep to Done in `NEXT.md`, add 1–3 cards to `cards/REVIEW.md` (only for things you *defended*, grade ≥ B; start from the chapter's card candidates), tick the chapter in `maps/fieldguide_map.md`.
6. In the VS Code terminal (PowerShell), one line: `cd "C:\Users\sujith\Documents\Claude Local\Projects\repos\genai-agent-mastery"; git add learning; git commit -m "rep: R0xx"; git push` — PowerShell needs `;` between commands, not `&&` (L-28).

**Coming back after a gap (any length):** do the 2 most-overdue cards in `cards/REVIEW.md`, then the top rep. No catch-up, no guilt, no re-planning.

## Three lanes (weights at your current capacity)

| Lane | Share | Rep types | Source |
|---|---|---|---|
| **OWN** | 3 of every 6 reps | **Trace** (follow a real request through the code, predict before reading) · **Defend** (Learning-Ledger questions cold, then model answer) · **Rebuild** (re-implement one small piece by hand in this repo, no AI) | ARB + PM code and ledgers · field guide Parts I, III, IV (Ch 1–7, 11–24) |
| **SYSTEMS** | 2 of every 6 | Learn one end-to-end architecture concept, then **write it into `design/pm-agent-at-scale.md`** — edge, API, communication, auth, scale, data, reliability, deployment, DevOps, AgentOps, security, cost, DR — and the agent lifecycle: release, runtimes, the evaluation loop, maintenance | `maps/system_design_track.md` (SD-01…SD-16) · field guide Parts V–VI (Ch 25–40) |
| **MODEL** | 1 of every 6 | Transformers → inference/serving → model choice, the gap none of your code teaches | field guide Part II (Ch 8–10) · depth in `maps/coverage_matrix.md` §F |
| **FRAMEWORKS** (inside OWN) | every 3rd OWN rep from R10 | Read any external framework through your build (GF-L1), apply one to a new agent (Capstone A), build one for an enterprise estate (Capstone B) | `maps/governance_frameworks_track.md`, `capstones/` · field guide Parts VII–IX (Ch 41–51), App. I |
| **TECH** (low priority) | ~1 lab every 2 weeks, or a bonus slot | Hands-on bake-offs of the leading tools per component (observability, evals, guardrails, gateways, frameworks, policy, identity, messaging, data, deployment, AgentOps, red-team), all on the same small target agent | `maps/technology_track.md`, labs in `../labs/` · field guide Ch 35–37, 46, App. I |
| **LANDSCAPE** (reserve budget) | ~1 glance rep a week at most | Product-lifecycle tools around pm-agent: what each does, how it integrates, verdict integrate / complement / compete / ignore | `maps/product_lifecycle_landscape_track.md`; matrix in `Governance Local/_portfolio-strategy/inbox/` · frame: field guide Ch 6, 34, 46 |
| **PROVE** | monthly | Timed system-design run of the whole design doc on a twist scenario, plus "defend your build" | field guide Part X (Ch 52–55) · Hello Interview framework, Himanshu cases |

Order inside OWN: **shared core first** (the chassis both repos share — learn once, covers ~1/3 of each), then PM's deltas, then ARB's E-phase families, then E4's GCP bindings. See `maps/comprehension_map.md`.

## Rules (the whole system)

- **R1 — Rep is the unit.** Progress = reps closed + cards passing. Never hours, never resources collected, never chapters read.
- **R2 — Learning follows focus.** If this week you're in PM, pull a PM rep (any rep in the queue can be swapped for one tagged with what you're working on).
- **R3 — Predict before you read.** Every Trace starts with a written prediction. Wrong predictions are where learning happens.
- **R4 — Cards only from defended material.** Spaced repetition at 1 → 3 → 7 → 21 → 60 days. Fail = back to 1.
- **R5 — Token-cheap.** Read code and write answers locally; use Claude only for the check. Learning must not eat the Pro limits the builds need.
- **R6 — Builds run free; capture comprehension as they go.** Each Claude Code stage already writes ledger questions; add one "design call" question per stage (`prompts/BUILD_STAGE_ADDENDUM.md`) you answer async.
- **R7 — No new resources without a rep.** New sightings go to the radar, not to your reading list. Platform or regulation changes that touch a chapter go to the book's register (Appendix H).
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
| `maps/fieldguide_map.md` | Every chapter of the field guide → the reps that defend it, read/defended status, how to use appendices A–I |
| `maps/capability_gap_register.md` | After the queue: gaps in evaluating tools/frameworks/platforms, composing them into a stack, build-vs-buy economics and building platform components (CG-01…CG-26), built on your prior evaluation work; closed until its gate opens |
| `maps/system_design_track.md` | SD-01…SD-16: end-to-end architecture around the agent, then its lifecycle |
| `maps/governance_frameworks_track.md` | GF-1…GF-6: AGT, OWASP Agentic, NIST/ISO/EU AI Act, platform-native controls, policy engines — understand → apply → build for an estate |
| `maps/technology_track.md` | TC-01…TC-18: tools per architecture component and the lab order |
| `maps/product_lifecycle_landscape_track.md` | LL1–LL10 glance reps + LL-D1…D5 deep dives on the product-lifecycle tool market |
| `capstones/` | A: govern a brand-new agent by hand · B: design and build the framework for an enterprise estate (synthetic) |
| `frameworks/` | Your one-page write-up per framework (created by GF reps) |
| `design/pm-agent-at-scale.md` | Your hand-written production design for pm-agent — one section per SYSTEMS rep (§1–§16) |
| `sync/` | Weekly build-to-learning sync notes |
| `resources/REGISTRY.md` | Every saved resource with one verdict |
| `prompts/` | Rep-session prompt, orchestrator prompt, build-stage addendum, the weekly sync task's prompt (`WEEKLY_SYNC.md`) |
| `radar/` | Fortnightly research radar drops (max 3 items) |
| `fieldguide/` | *Architect's Field Guide*, edition 1: 55 chapters + appendices A–I. `index.html` (local), `field-guide.pdf` (offline, phone), published private copy linked from `maps/fieldguide_map.md`. Source + `build.py`; the Orchestrator revises and republishes it |
| `DECISIONS.md` | Why v3 is shaped this way |

## The GCP lane (decided 2026-10-13)

E4 (live GCP) was built autonomously for the GTM deadline, so GCP learning is now: **Trace E4** (Vertex via gateway, Cloud KMS signing, Firestore state, GCS anchor, Model Armor) in OWN, and **M1 (WIF CI/CD) stays a Rebuild** in this repo's `infra/`, hand-written, picked up when you want hands-on infra.

## Schedule (scheduled tasks)

| Task | When (IST) | Runs where | Sends |
|---|---|---|---|
| Cloud learning nudge | Tue, Thu, Sat, Sun 08:56 | cloud — works with the laptop off (reads the Notion page "Learning OS — nudge snapshot", kept current by rep sessions and the weekly sync) | phone push: top rep + its 📖 chapter + one question |
| Learning nudge (device) | Wed 08:45 | your computer | same, from local files |
| Weekly build-to-learning sync | Sun 19:49 | your computer | updates maps + backlog, lists field-guide register triggers that fired, writes `sync/SYNC_*.md` |
| Research radar | 1st & 15th 08:50 | your computer | ≤ 3 items in `Governance/_Agentic_Governance_Mastery/research/briefings/` |
| Job market + skills gap | 1st 22:50 | cloud | monthly report |

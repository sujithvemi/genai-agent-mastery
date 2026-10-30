# NEXT — the queue

## ▶ When you sit down (2 minutes, no thinking)
1. Double-click **`genai-agent-mastery/learning.code-workspace`** → VS Code opens the learning folder and both builds side by side.
2. Below, take the **first unticked rep** in "This weekend" (or the top Ready rep). Open its file in `reps/`.
3. Write your answers **in that file**, top to bottom. Each rep tells you exactly what to open and run. Its **📖 Read** line names the field guide sections: for a Trace rep, read them *after* Step 0's predictions; for a Defend rep, read them, close the book, then answer cold. Already read them on your phone during the week? Skip straight to the rep.
4. Finish: one line in `LOG.md`, tick the rep here, then `git add . && git commit -m "rep R0x" && git push`.
5. Optional (5–10 min): new chat in the Governance project → paste `prompts/REP_SESSION.md` → it checks your answers, grades you and does the bookkeeping (including `maps/fieldguide_map.md`).
Gap since last time? Do 2 overdue cards from `cards/REVIEW.md` first. No catch-up.

## This weekend (Sat 31 Oct – Sun 1 Nov) — ~2.5 hours total, split however you like
- [ ] **Sat · R01** Trace a refund end to end (40 m) · 📖 Ch16 §16.3–16.8, Ch22 §22.1–22.3
- [ ] **Sat · R02** Defend Ledger P0 (25 m) · 📖 Ch7 §7.1–7.4, Ch22 §22.1–22.3
- [ ] **Sun · R05** Systems: request path + run API → write §1–2 of your design doc (40 m) · 📖 Ch25 §25.1–25.6
- [ ] **Sun · R25** Microsoft's Agent Governance Toolkit through your build (40 m) · 📖 Ch47 §47.2–47.6
Stop wherever the time runs out — one rep is a win. Leftovers simply stay at the top. The 📖 reading (10–20 min each) can happen on the phone before the weekend; the times above are for the rep only.


**Rule:** do the top **Ready** rep. Swap allowed only for a rep tagged with what you're building this week (R2).
**Cycle:** 3 OWN : 2 SYSTEMS : 1 MODEL, PROVE once a month (alternating system-design drill / Capstone B). From R10 on, every third OWN rep is a Frameworks rep or a Capstone A stage. **After any gap:** 2 most-overdue cards, then the top rep.
**Reading (L-23):** the *Architect's Field Guide* (`fieldguide/index.html`, PDF `fieldguide/field-guide.pdf`) is the consume step for every rep; the 📖 column says which sections. Reading alone never counts (R1). Progress per chapter: `maps/fieldguide_map.md`.

## Ready (rep files exist)

| Rep | Lane | What | 📖 Read first | Time |
|---|---|---|---|---|
| **R01** | OWN · Trace | A refund from the model's tool call to the evidence log (ARB) → `reps/R01_trace_golden_path.md` | Ch16 §16.3–16.8 · Ch22 §22.1–22.3 | 30–40 m |
| **R02** | OWN · Defend | Ledger P0 — seams, do-nothing chokepoint, evidence → `reps/R02_defend_ledger_P0.md` | Ch7 §7.1–7.4 · Ch22 §22.1–22.3 | 25 m |
| **R03** | OWN · Defend | Ledger P1 — instruction ≠ control → `reps/R03_defend_ledger_P1.md` | Ch16 §16.1 · Ch11 §11.1–11.3 | 25 m |
| R04 | OWN · Trace+Defend | Why CRITICAL vs MEDIUM — tiering, gate, Ledger P2 → `reps/R04_trace_tiering_gate.md` | Ch13 · Ch14 §14.1–14.2 · Ch15 §15.3–15.5 | 40 m |
| R05 | SYSTEMS | SD-01 + SD-02: request path and the run API → `reps/R05_sys_request_path_api.md` | Ch25 §25.1–25.6 | 40 m |
| R25 | OWN · Frameworks | GF-1: Microsoft's Agent Governance Toolkit through your build → `reps/R25_gf1_agt_through_your_build.md` | Ch47 §47.2–47.6 (§47.7 only after your own table) | 40 m |

## Backlog (rep file generated when it reaches Ready)

| Rep | Lane | What | Anchor | 📖 Read first |
|---|---|---|---|---|
| R06 | SYSTEMS | SD-04 AuthN/AuthZ end to end: user OIDC → API → agent identity → tool on-behalf-of; service identity (WIF, SA) → design §4 | ARB `enforcement/tokens.py`, PM `platform/identity` | Ch27 · Ch18 §18.1–18.4 |
| R07 | MODEL | Attention from scratch — Raschka *Build an LLM* video ch.3 + AIEFS Ph7 "Self-Attention from Scratch" | 🟥 | Ch8 §8.2–8.6 |
| R08 | OWN · Trace | Evidence chain + redaction, hands-on: `make demo-tamper` (no make: `uv run python -m aicoe.cli demo tamper`), then `evidence/{chain,redaction}.py` | ARB | Ch22 §22.3–22.7 · Ch21 §21.4 |
| R09 | OWN · Trace | A policy decision: `tool_call.rego` header + `enforcement/pip.py` + `plane.decide` — how Rego fails open and how this bundle prevents it | ARB | Ch17 §17.3–17.5 · Ch16 §16.5–16.6 |
| R10 | OWN · Rebuild | Hand-write a ≤120-line chokepoint + hash-chained JSONL evidence in GAM `rebuild/`, no AI, then diff against ARB | GAM | Ch16 §16.3–16.4 · Ch22 §22.2–22.3 (close it while you build) |
| R11 | SYSTEMS | SD-03 Communication: sync vs queue vs pub/sub vs stream; where would pm-agent need a queue? outbox pattern → design §3 | ARB `platform/a2a` | Ch26 |
| R12 | SYSTEMS | SD-05 State & scale: stateless workers, checkpointer, long runs as jobs, Cloud Run vs GKE vs Agent Engine → design §5 | PM `platform/runtime`, ARB `platform/state` | Ch28 §28.1–28.5 · Ch37 §37.1–37.2 |
| R13 | MODEL | Inference 1: KV cache & batching — AIEFS Ph7 KV lesson + Himanshu #2 (vLLM) | 🟥 | Ch9 §9.1–9.6 |
| R14 | PROVE | **First weekend of November:** 45-min timed design of pm-agent for 10× users using your doc so far + "how does your platform stop a rogue refund" | monthly | Ch55 §55.1–55.2, §55.5 · Ch54 §54.2 |
| R15 | OWN · Trace | The fork: what PM kept vs changed from ARB's chassis (seams, import firewall, PEP, evidence, LangGraph runtime) | PM | Ch7 §7.5–7.6 |
| R16 | OWN · Defend | Ledger P3 — runtime enforcement | ARB | Ch16 §16.5–16.9 · Ch17 §17.4 |
| R17 | OWN · Trace | E4: one Vertex call through the governed model gateway + a Cloud KMS signature | ARB E4 | Ch41 §41.9 · Ch10 §10.5 · Ch22 §22.5 |
| R18 | SYSTEMS | SD-07 Reliability: timeouts, retries + jitter, breakers, bulkheads, rate limits, load shedding — stability PDFs, then find them in ARB/PM → design §7 | core PDFs | Ch29 |
| R19 | SYSTEMS | SD-08 Deployment & DevOps: CI/CD, IaC, canary for code *and* prompts/models, rollback → design §8 (links to the M1 Rebuild) | ARB `ci.yml`, `infra/gcp` | Ch30 · Ch38 §38.5–38.7 |
| R20 | MODEL | DDIA 2e replication chapter → where would ARB's evidence store and PM's checkpointer need it? | 🟥 | Ch28 §28.2–28.4, §28.8 |
| R21 | OWN · Trace | PM: HITL interrupt/resume with LangGraph checkpointing | PM `platform/runtime`, `platform/approval` | Ch19 §19.3–19.5, §19.9 · Ch26 §26.6 |
| R22 | SYSTEMS | SD-09 Observability & AgentOps: SLOs for agents, eval gates in CD, prompt/model registry, cost dashboards, runbook → design §9 | ARB/PM observability, evals | Ch31 · Ch23 §23.1–23.4 |
| R23 | SYSTEMS | SD-06 Data layer + SD-10 Security & multi-tenancy → design §6, §10 | | Ch28 §28.5, §28.8 · Ch21 · Ch32 §32.7 |
| R24 | OWN · Rebuild | M1: WIF-driven Terraform plan-on-PR / apply-on-merge — becomes Capstone A stage A5 | GAM `infra/` | Ch30 §30.3–30.5 · Ch52 §52.7 |
| R26 | OWN · Frameworks | GF-2: OWASP Top 10 for Agentic Applications mapped to your catalog + red-team corpus → `frameworks/OWASP_agentic.md` | ARB `tests/redteam/` | Ch48 §48.2 · Ch32 §32.2 · Ch20 §20.1–20.3 |
| R27 | OWN · Frameworks | GF-5: OPA/Rego vs Cedar vs AGT — same control in all three; which fails open where | ARB `platform/policy/` | Ch17 §17.2–17.4 · Ch47 §47.4 |
| R28 | CAPSTONE A | A0–A1: pick your new agent, write its agent card, build it ungoverned in GAM → `capstones/A_govern_a_new_agent.md` | GAM | Ch52 §52.1–52.3 · Ch34 §34.3–34.4 |
| R29 | PROVE · CAPSTONE B | B1–B2 (December PROVE slot): tiering model + control-catalog cut for the two-platform client scenario → `capstones/B_client_framework.md` | | Ch53 §53.2–53.3 · Ch13 §13.2–13.3 · Ch12 §12.4 |
| R30 | OWN · Defend | Ledger E4 — live bindings EXERCISED only by recorded runs, verifiers can't sign (Ed25519/KMS), approval page as trust boundary (self-test Q1–6) | ARB `docs/LEARNING_LEDGER.md` §E4 | Ch41 §41.9 · Ch22 §22.5–22.7 · Ch19 §19.6 |
| R31 | OWN · Defend | Ledger E5 + E5-S5 + E5.1 — monotone classifiers, typed answers, fairness HELD, retry only effect-free attempts (Q1–10) | ARB `docs/LEARNING_LEDGER.md` §E5 | Ch20 §20.6 · Ch2 §2.6 · Ch23 §23.7 · Ch29 §29.3 |
| R32 | OWN · Trace | A classifier that can only over-block + the typed answer: `make demo-content-safety` and `make demo-groundedness` (no make: `uv run python -m aicoe.cli demo content-safety` / `... demo groundedness`), then read the composition | ARB `enforcement/classifier_gate.py`, `enforcement/answer_contract.py` | Ch20 §20.6 · Ch2 §2.6–2.7 |
| R33 | OWN · Trace | Why PM stopped detecting injection: frozen structural guard (56% held-out) → containment by construction (typed effects, Rego eligibility, provenance lanes) | PM `artifacts/adr/ADR-0005-containment-by-construction.md`, `agents/guardrails/structural.py` | Ch20 §20.2, §20.7 |
| R34 | OWN · Trace | Governed durable memory: scope, PII set (Luhn/mod-97), MAC verify key, hint mode when no key | PM `platform/memory/governed.py`, `pii.py`, `platform/crypto/memory_mac.py` | Ch3 §3.4 · Ch21 §21.3 |
| R35 | OWN · Trace | PM's first product workflow, "adopt a repo" (read-only): `make eval-adopt` (no make: `uv run python -m pm_agent.evals --adopt`), then `uv run pm-agent adopt <a repo> --project DEMO --dry-run --out <dir outside it>`; why every adopted-repo line is free-text lane, whatever container it sits in (D-PM-R1-30) | PM `workflows/adopt/run.py`, `extract.py`, `actions/sanitiser.py` | Ch20 §20.5 · Ch36 §36.3 |
| R36 | OWN · Trace | R1 seam freeze: a typed action → Rego eligibility (bounded, fail closed) → one signed grant over a batch manifest; then skim the ledger kinds and the executor contract (ADR-0007/0008) | PM `actions/union.py`, `actions/batch.py`, `platform/policy/eligibility.py`, `platform/bounded.py`, `platform/executors/contract.py` | Ch17 §17.7 · Ch19 §19.5 |
| R37 | OWN · Defend | GR1 owner self-test: answer the 15 questions aloud, then check them against the claims card; run `make demo-portability` (no make: `uv run python -m aicoe.cli demo portability`) and say Q11's always-add sentence | ARB `docs/showcase/SELF_TEST.md`, `CLAIMS_CARD.md`, `CLIENT_QA.md` | Ch54 §54.2, §54.4–54.9 |
| R38 | SYSTEMS | SD-11 Capacity & cost: back-of-envelope for pm-agent (runs/s, tokens/run, cost/run, quotas as the real bottleneck), budgets and showback per tenant → design §11 | ARB `enforcement/model_budget.py`, PM `platform/budget` | Ch33 §33.1–33.5 · Ch10 §10.8 |
| R39 | SYSTEMS | SD-12 Multi-region, DR & residency: RPO/RTO for runs, checkpoints and evidence; what fails over and what must not → design §12 | — (🟥, on paper) | Ch33 §33.7–33.8 · Ch21 §21.6 |
| R40 | SYSTEMS | SD-13 Agent lifecycle & release: what *a version of pm-agent* is (code + prompts + model + tools + policy), registry, promotion, progressive delivery, what cannot roll back → design §13 | ARB `governance/config_digest.py`, `signoff.py`; PM `evals/baseline.py` | Ch34 §34.2, §34.6–34.7 · Ch38 |
| R41 | SYSTEMS | SD-14 Runtimes & managed agent platforms: host pm-agent on Cloud Run vs Agent Engine vs AgentCore vs Foundry Agent Service; sessions, memory services, what the platform governs and what it does not → design §14 | PM `platform/runtime`, ARB `platform/state` | Ch37 · Ch41–43 (shape + map sections) · App. I |
| R42 | SYSTEMS | SD-15 Evaluate, simulate, optimise: offline → simulation → online → replay; where prompt/model optimisation may change the agent and which gate catches it → design §15 | PM `evals/` (`ws_e.py`, `baseline.py`, `replay.py`), ARB `evals/` | Ch39 · Ch23 §23.4–23.5 |
| R43 | SYSTEMS | SD-16 Maintenance & evolution: model deprecation, dependency upgrades, drift, memory hygiene, recertification, retirement, the maintenance budget → design §16 | ARB RUNBOOKS §7 (AGT bump), PM drift in `evals/baseline.py` | Ch40 · Ch15 §15.8 |
| R44 | OWN · Frameworks | GF-3: NIST AI RMF / ISO 42001 / EU AI Act after the Omnibus — check 5 rows of your crosswalk and rewrite their Verify cells honestly → `frameworks/crosswalk.md` | root `governance/crosswalk/`, ARB `governance/crosswalk/` | Ch48 §48.3–48.5, §48.7–48.8 |
| R45 | OWN · Frameworks | GF-4: platform-native governance — map 6 of your controls onto Google Cloud, AWS and Microsoft native controls; mark where a gateway or a process must fill the gap → `frameworks/platform_native.md` | ARB E4 bindings, `platform/classifier/model_armor.py` | Ch45 · Ch41 §41.7 · Ch42–43 (map sections) · Ch12 §12.5 · App. I |
| R46 | OWN · Frameworks | GF-6 + regulated overlays: Singapore agentic framework / CSA agentic work, then one industry overlay (banking) on your catalog → `frameworks/agentic_and_overlays.md` | your catalog + crosswalk | Ch48 §48.6 · Ch49 |
| R47 | PROVE · CAPSTONE B | B6: operating model + 90-day plan for the Capstone B scenario (decision rights, earned autonomy, KPIs, interim vs target state) | | Ch50 · Ch51 · Ch53 §53.7 |
| R48 | MODEL | Model choice, routing and model risk: pick models for pm-agent's planner, workers and classifier per task; routing, pinning, budgets; what model-risk management asks of an agent | ARB model pin (CTL-0021), PM ADR-0006 routing | Ch10 |

## Build-tool labs (OWN · Rebuild — every third OWN rep can be one)
Hands-on with each tool Claude Code used in your builds: build a minimal version yourself, then diff against the build. Full list BT01–BT16 in `maps/technology_track.md` Part A.

| Lab | What | File | 📖 Read |
|---|---|---|---|
| **BT01** | The toolchain both builds use: uv, ruff, mypy strict, pytest, pre-commit, Make | `reps/BT01_toolchain.md` | Ch7 §7.1, §7.7–7.9 |
| BT02 | Pydantic v2, pydantic-settings, jsonschema, YAML manifests | generated when reached | Ch2 §2.5–2.6 |
| BT03 | Google ADK agent on your local model via LiteLLM | generated when reached | Ch1 §1.2–1.3 · Ch35 §35.6 |
| BT05 | FastAPI run API with 202 + SSE events (pairs with R05) | generated when reached | Ch25 §25.2–25.5 |

## LANDSCAPE lane (reserve budget, outside the cycle — product-lifecycle tools for pm-agent; about one glance rep a week at most)

| Rep | What | File | 📖 Read |
|---|---|---|---|
| **LL1** | In-tool PM agents: Rovo, Linear, Notion (+ skim Asana, monday, ClickUp) | `reps/LL1_in_tool_pm_agents.md` | Ch6 §6.5–6.6 · Ch44 §44.4 |
| LL2 | Upstream product tools: Productboard Spark, ChatPRD | generated when reached | Ch34 §34.3 |
| LL3 | Spec-driven development: Spec Kit, Kiro, OpenSpec, BMAD, Task Master, Tessl | generated when reached | Ch34 §34.4–34.6, §34.9 |
| LL4–LL9 | Executors, protocols (MCP/ACP/A2A), decision models (Jev), design (Figma MCP), traceability prior art, release tools | see `maps/product_lifecycle_landscape_track.md` | Ch6 · Ch5 · Ch46 |
| LL10 | Open-source agent harnesses: DeepSeek Harness, OpenHands, Goose, opencode, Cline, Hermes + the harness-anatomy paper | see track | Ch1 · Ch46 §46.3 |

## TECH lane (low priority — market tools you haven't used; one lab about every 2 weeks, or a bonus slot)

| Lab | What | File | 📖 Read |
|---|---|---|---|
| **T01** | Observability bake-off 1: one OpenTelemetry instrumentation → Langfuse + Arize Phoenix | `reps/T01_tech_observability_bakeoff.md` | Ch31 §31.3, §31.9 · Ch46 §46.2 |
| T02 | Observability bake-off 2: LangSmith + Datadog LLM Observability; finish the comparison | generated when reached | Ch31 §31.9 · App. I |
| T03 | Evals bake-off: DeepEval vs Ragas vs Vertex Gen AI Eval | generated when reached | Ch39 §39.3, §39.11 · Ch23 |
| T04 | Guardrails bake-off: Model Armor vs NeMo Guardrails vs Llama Guard (+ Presidio for PII) | generated when reached | Ch20 §20.3, §20.6 |

Full map of 17 components and the lab order: `maps/technology_track.md`. Build-vs-buy method for any of them: Ch46 §46.5.

SYSTEMS modules SD-11…SD-16 are in the backlog as R38–R43 (SD-13…SD-16 cover the agent lifecycle, added 2026-10-30, L-24). The weekly sync also inserts reps for whatever the builds shipped that week, each with its 📖 chapter.

## Done

| Rep | Date | Grade |
|---|---|---|

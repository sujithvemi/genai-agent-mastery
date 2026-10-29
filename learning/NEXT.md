# NEXT — the queue

## ▶ When you sit down (2 minutes, no thinking)
1. Double-click **`genai-agent-mastery/learning.code-workspace`** → VS Code opens the learning folder and both builds side by side.
2. Below, take the **first unticked rep** in "This weekend" (or the top Ready rep). Open its file in `reps/`.
3. Write your answers **in that file**, top to bottom. Each rep tells you exactly what to open and run.
4. Finish: one line in `LOG.md`, tick the rep here, then `git add . && git commit -m "rep R0x" && git push`.
5. Optional (5–10 min): new chat in the Governance project → paste `prompts/REP_SESSION.md` → it checks your answers, grades you and does the bookkeeping.
Gap since last time? Do 2 overdue cards from `cards/REVIEW.md` first. No catch-up.

## This weekend (Sat 31 Oct – Sun 1 Nov) — ~2.5 hours total, split however you like
- [ ] **Sat · R01** Trace a refund end to end (40 m)
- [ ] **Sat · R02** Defend Ledger P0 (25 m)
- [ ] **Sun · R05** Systems: request path + run API → write §1–2 of your design doc (40 m)
- [ ] **Sun · R25** Microsoft's Agent Governance Toolkit through your build (40 m)
Stop wherever the time runs out — one rep is a win. Leftovers simply stay at the top.


**Rule:** do the top **Ready** rep. Swap allowed only for a rep tagged with what you're building this week (R2).
**Cycle:** 3 OWN : 2 SYSTEMS : 1 MODEL, PROVE once a month (alternating system-design drill / Capstone B). From R10 on, every third OWN rep is a Frameworks rep or a Capstone A stage. **After any gap:** 2 most-overdue cards, then the top rep.

## Ready (rep files exist)

| Rep | Lane | What | Time |
|---|---|---|---|
| **R01** | OWN · Trace | A refund from the model's tool call to the evidence log (ARB) → `reps/R01_trace_golden_path.md` | 30–40 m |
| **R02** | OWN · Defend | Ledger P0 — seams, do-nothing chokepoint, evidence → `reps/R02_defend_ledger_P0.md` | 25 m |
| **R03** | OWN · Defend | Ledger P1 — instruction ≠ control → `reps/R03_defend_ledger_P1.md` | 25 m |
| R04 | OWN · Trace+Defend | Why CRITICAL vs MEDIUM — tiering, gate, Ledger P2 → `reps/R04_trace_tiering_gate.md` | 40 m |
| R05 | SYSTEMS | SD-01 + SD-02: request path and the run API → `reps/R05_sys_request_path_api.md` | 40 m |
| R25 | OWN · Frameworks | GF-1: Microsoft's Agent Governance Toolkit through your build → `reps/R25_gf1_agt_through_your_build.md` | 40 m |

## Backlog (rep file generated when it reaches Ready)

| Rep | Lane | What | Anchor |
|---|---|---|---|
| R06 | SYSTEMS | SD-04 AuthN/AuthZ end to end: user OIDC → API → agent identity → tool on-behalf-of; service identity (WIF, SA) → design §4 | ARB `enforcement/tokens.py`, PM `platform/identity` |
| R07 | MODEL | Attention from scratch — Raschka *Build an LLM* video ch.3 + AIEFS Ph7 "Self-Attention from Scratch" | 🟥 |
| R08 | OWN · Trace | Evidence chain + redaction, hands-on: `make demo-tamper` (no make: `uv run python -m aicoe.cli demo tamper`), then `evidence/{chain,redaction}.py` | ARB |
| R09 | OWN · Trace | A policy decision: `tool_call.rego` header + `enforcement/pip.py` + `plane.decide` — how Rego fails open and how this bundle prevents it | ARB |
| R10 | OWN · Rebuild | Hand-write a ≤120-line chokepoint + hash-chained JSONL evidence in GAM `rebuild/`, no AI, then diff against ARB | GAM |
| R11 | SYSTEMS | SD-03 Communication: sync vs queue vs pub/sub vs stream; where would pm-agent need a queue? outbox pattern → design §3 | ARB `platform/a2a` |
| R12 | SYSTEMS | SD-05 State & scale: stateless workers, checkpointer, long runs as jobs, Cloud Run vs GKE vs Agent Engine → design §5 | PM `platform/runtime`, ARB `platform/state` |
| R13 | MODEL | Inference 1: KV cache & batching — AIEFS Ph7 KV lesson + Himanshu #2 (vLLM) | 🟥 |
| R14 | PROVE | **First weekend of November:** 45-min timed design of pm-agent for 10× users using your doc so far + "how does your platform stop a rogue refund" | monthly |
| R15 | OWN · Trace | The fork: what PM kept vs changed from ARB's chassis (seams, import firewall, PEP, evidence, LangGraph runtime) | PM |
| R16 | OWN · Defend | Ledger P3 — runtime enforcement | ARB |
| R17 | OWN · Trace | E4: one Vertex call through the governed model gateway + a Cloud KMS signature | ARB E4 |
| R18 | SYSTEMS | SD-07 Reliability: timeouts, retries + jitter, breakers, bulkheads, rate limits, load shedding — stability PDFs, then find them in ARB/PM → design §7 | core PDFs |
| R19 | SYSTEMS | SD-08 Deployment & DevOps: CI/CD, IaC, canary for code *and* prompts/models, rollback → design §8 (links to the M1 Rebuild) | ARB `ci.yml`, `infra/gcp` |
| R20 | MODEL | DDIA 2e replication chapter → where would ARB's evidence store and PM's checkpointer need it? | 🟥 |
| R21 | OWN · Trace | PM: HITL interrupt/resume with LangGraph checkpointing | PM `platform/runtime`, `platform/approval` |
| R22 | SYSTEMS | SD-09 Observability & AgentOps: SLOs for agents, eval gates in CD, prompt/model registry, cost dashboards, runbook → design §9 | ARB/PM observability, evals |
| R23 | SYSTEMS | SD-06 Data layer + SD-10 Security & multi-tenancy → design §6, §10 | |
| R24 | OWN · Rebuild | M1: WIF-driven Terraform plan-on-PR / apply-on-merge — becomes Capstone A stage A5 | GAM `infra/` |
| R26 | OWN · Frameworks | GF-2: OWASP Top 10 for Agentic Applications mapped to your catalog + red-team corpus → `frameworks/OWASP_agentic.md` | ARB `tests/redteam/` |
| R27 | OWN · Frameworks | GF-5: OPA/Rego vs Cedar vs AGT — same control in all three; which fails open where | ARB `platform/policy/` |
| R28 | CAPSTONE A | A0–A1: pick your new agent, write its agent card, build it ungoverned in GAM → `capstones/A_govern_a_new_agent.md` | GAM |
| R29 | PROVE · CAPSTONE B | B1–B2 (December PROVE slot): tiering model + control-catalog cut for the two-platform client scenario → `capstones/B_client_framework.md` | |
| R30 | OWN · Defend | Ledger E4 — live bindings EXERCISED only by recorded runs, verifiers can't sign (Ed25519/KMS), approval page as trust boundary (self-test Q1–6) | ARB `docs/LEARNING_LEDGER.md` §E4 |
| R31 | OWN · Defend | Ledger E5 + E5-S5 + E5.1 — monotone classifiers, typed answers, fairness HELD, retry only effect-free attempts (Q1–10) | ARB `docs/LEARNING_LEDGER.md` §E5 |
| R32 | OWN · Trace | A classifier that can only over-block + the typed answer: `make demo-content-safety` and `make demo-groundedness` (no make: `uv run python -m aicoe.cli demo content-safety` / `... demo groundedness`), then read the composition | ARB `enforcement/classifier_gate.py`, `enforcement/answer_contract.py` |
| R33 | OWN · Trace | Why PM stopped detecting injection: frozen structural guard (56% held-out) → containment by construction (typed effects, Rego eligibility, provenance lanes) | PM `artifacts/adr/ADR-0005-containment-by-construction.md`, `agents/guardrails/structural.py` |
| R34 | OWN · Trace | Governed durable memory: scope, PII set (Luhn/mod-97), MAC verify key, hint mode when no key | PM `platform/memory/governed.py`, `pii.py`, `platform/crypto/memory_mac.py` |
| R35 | OWN · Trace | PM's first product workflow, "adopt a repo" (read-only): `make eval-adopt` (no make: `uv run python -m pm_agent.evals --adopt`), then `uv run pm-agent adopt <a repo> --project DEMO --dry-run --out <dir outside it>`; why every adopted-repo line is free-text lane, whatever container it sits in (D-PM-R1-30) | PM `workflows/adopt/run.py`, `extract.py`, `actions/sanitiser.py` |
| R36 | OWN · Trace | R1 seam freeze: a typed action → Rego eligibility (bounded, fail closed) → one signed grant over a batch manifest; then skim the ledger kinds and the executor contract (ADR-0007/0008) | PM `actions/union.py`, `actions/batch.py`, `platform/policy/eligibility.py`, `platform/bounded.py`, `platform/executors/contract.py` |
| R37 | OWN · Defend | GR1 owner self-test: answer the 15 questions aloud, then check them against the claims card; run `make demo-portability` (no make: `uv run python -m aicoe.cli demo portability`) and say Q11's always-add sentence | ARB `docs/showcase/SELF_TEST.md`, `CLAIMS_CARD.md`, `CLIENT_QA.md` |

## Build-tool labs (OWN · Rebuild — every third OWN rep can be one)
Hands-on with each tool Claude Code used in your builds: build a minimal version yourself, then diff against the build. Full list BT01–BT16 in `maps/technology_track.md` Part A.

| Lab | What | File |
|---|---|---|
| **BT01** | The toolchain both builds use: uv, ruff, mypy strict, pytest, pre-commit, Make | `reps/BT01_toolchain.md` |
| BT02 | Pydantic v2, pydantic-settings, jsonschema, YAML manifests | generated when reached |
| BT03 | Google ADK agent on your local model via LiteLLM | generated when reached |
| BT05 | FastAPI run API with 202 + SSE events (pairs with R05) | generated when reached |

## LANDSCAPE lane (reserve budget, outside the cycle — product-lifecycle tools for pm-agent; about one glance rep a week at most)

| Rep | What | File |
|---|---|---|
| **LL1** | In-tool PM agents: Rovo, Linear, Notion (+ skim Asana, monday, ClickUp) | `reps/LL1_in_tool_pm_agents.md` |
| LL2 | Upstream product tools: Productboard Spark, ChatPRD | generated when reached |
| LL3 | Spec-driven development: Spec Kit, Kiro, OpenSpec, BMAD, Task Master, Tessl | generated when reached |
| LL4–LL9 | Executors, protocols (MCP/ACP/A2A), decision models (Jev), design (Figma MCP), traceability prior art, release tools | see `maps/product_lifecycle_landscape_track.md` |
| LL10 | Open-source agent harnesses: DeepSeek Harness, OpenHands, Goose, opencode, Cline, Hermes + the harness-anatomy paper | see track |

## TECH lane (low priority — market tools you haven't used; one lab about every 2 weeks, or a bonus slot)

| Lab | What | File |
|---|---|---|
| **T01** | Observability bake-off 1: one OpenTelemetry instrumentation → Langfuse + Arize Phoenix | `reps/T01_tech_observability_bakeoff.md` |
| T02 | Observability bake-off 2: LangSmith + Datadog LLM Observability; finish the comparison | generated when reached |
| T03 | Evals bake-off: DeepEval vs Ragas vs Vertex Gen AI Eval | generated when reached |
| T04 | Guardrails bake-off: Model Armor vs NeMo Guardrails vs Llama Guard (+ Presidio for PII) | generated when reached |

Full map of 17 components and the lab order: `maps/technology_track.md`.

Remaining SYSTEMS modules (SD-11 capacity & cost, SD-12 multi-region & DR) are added by the weekly sync / check-in as the queue drains. The weekly sync also inserts reps for whatever the builds shipped that week.

## Done

| Rep | Date | Grade |
|---|---|---|

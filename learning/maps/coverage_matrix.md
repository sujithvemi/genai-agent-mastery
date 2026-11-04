# Coverage Matrix — what you need × where you learn it

**Updated:** 2026-11-01 (sync: PM R1-S2/S3 cells; earlier: field guide added as the consume source; sections D3–D4 added). **Goal it serves:** build, govern and defend production enterprise agent systems on GCP (principal-architect level).
**Read this as:** for each topic, your *own code* is the primary teacher (OWN). The **field guide** (**FG**, `fieldguide/`) is the consume step that explains it through that code. External resources only add depth (GROUND) or test you under interview pressure (PROVE).

Codes — **ARB** = aicoe-reference-build · **PM** = project_management_building_agent · **GAM** = genai-agent-mastery (your hand-written repo)
Status — 🟩 in your code (learn by tracing) · 🟨 partly in code · 🟥 not in any code (GROUND needed)

## A. Agent mechanics

| Topic | Where it lives in your code | GROUND / SKIM source | Status |
|---|---|---|---|
| Agent loop & tool calling | ARB `agents/customer_service_ops.py`, `agents/tools.py`, `platform/runtime` (ADK) | FG Ch1–2 · AIEFS Ph14 "Agent Loop" | 🟩 |
| Graph orchestration, checkpoint, interrupt/resume | PM `platform/runtime` (LangGraph), `platform/approval` | FG Ch6, Ch26 §26.6 · LangGraph playlist (pick) | 🟩 |
| Multi-agent / A2A | ARB `platform/a2a`, `enforcement/a2a_wiring.py` | FG Ch5, Ch6 · A2A spec; 30-concepts (skim) | 🟨 |
| MCP (tool-as-server, integrity) | ARB `gateways/`, `enforcement/mcp_integrity.py`, `platform/gateway` | FG Ch5, Ch36 · AIEFS Ph13; MCP spec | 🟩 |
| Memory | PM `platform/memory` — durable, scoped, redacted, MAC-verified: `governed.py`, `pii.py`, `postgres.py`, `platform/crypto/memory_mac.py` (P5-4/P5-5) | FG Ch3, Ch37 · Neural Maze KG memory (pick) | 🟩 |
| RAG / retrieval / grounding | ARB `platform/retrieval`, KB tools; PM grounding (CTL-0015) | FG Ch4 · Zilliz playlist; Himanshu #1 Perplexity | 🟩 |
| Structured outputs / contracts | ARB `enforcement/contracts.py`, `enforcement/answer_contract.py` + `platform/model/structured.py` (CTL-0026 typed answer, E5); PM `contracts/` | FG Ch2 · AIEFS Ph5 constrained decoding | 🟩 |

## B. Governance & security (your strength — prove it from code)

| Topic | Where | Source | Status |
|---|---|---|---|
| Control catalog, fleet-first tiering, gate | ARB `governance/catalog.py`, `governance/tiering`, `governance/gate`; root `governance/catalog` | FG Ch13–15, App. B · Ledger P2 | 🟩 |
| PEP/PDP, policy-as-code (OPA/Rego, Cedar) | `chokepoint.py`, `enforcement/plane.py`, `platform/policy/{opa,rego,cedar}.py`, `governance/policies/rego/tool_call.rego`; PM `governance/policies/eligibility/{eligibility,actions}.rego` (R1-S3: `denials` set under GBL-DENY-01, Rego error → deny, mutation sweep kill rate 1.0 — `evals/mutation_eligibility.py`) | FG Ch16–17 · Ledger P3 | 🟩 |
| Identity, delegation, capability tokens | ARB `enforcement/tokens.py` (1.2k lines), `platform/identity` | FG Ch18, Ch27 · OAuth token exchange (RFC 8693) | 🟩 |
| HITL approval, separation of duties | ARB `approval_ui/`, PM `platform/approval` + batched grant over an action-hash manifest `actions/batch.py` (D-PM-R1-6) | FG Ch19 · Ledger P3/P4 | 🟩 |
| Evidence: hash chain, redaction, signing, anchoring | ARB `evidence/{writer,chain,redaction,anchoring}.py`, `platform/signing.py` (Ed25519 + Cloud KMS) | FG Ch22 · Ledger P0/P4 | 🟩 |
| Prompt injection, guardrails, content screens | PM `agents/guardrails` (3.5k; frozen structural guard, ADR-0005 containment by construction — seam built R1-S0: typed actions `actions/union.py`, Rego eligibility `platform/policy/eligibility.py`, sanitiser; all adopted-repo text is free-text lane, D-PM-R1-30; R1-S3: action gate `actions/pipeline.py`, provenance lanes `actions/provenance.py`, confirmed typed RequestScope `actions/request_scope.py` replaced NL scoping, D-PM-R1-74; hostile-planner gate CLOSED with both gated counts 0, D-PM-R1-94), ARB `enforcement/guardrails.py`, `platform/screening`, `platform/classifier` + `enforcement/classifier_gate.py` (D52 monotone, CTL-0025) | FG Ch20 · OWASP Agentic Top 10; Himanshu #8 Llama Guard | 🟩 |
| Red-teaming & assurance | ARB P5 + `docs/`; PM P5 report; PM R1 hostile-planner gate spec `governance/hostile_gate.py` (0 attacker-originated executed effects, harness at S3) | FG Ch24 · Ledger P5 | 🟩 |
| Standards crosswalk (NIST/ISO 42001/EU AI Act) | root `governance/crosswalk` | FG Ch48 · your corpus | 🟩 |

## C. Evals, observability, cost

| Topic | Where | Source | Status |
|---|---|---|---|
| Golden-set vs live eval, eval-as-gate | ARB `evals/` (+ `retry.py`), PM `evals/` (+ `baseline.py` blocking regression gate, `ws_e.py`, `replay.py`) | FG Ch23, Ch39 · Agentic Evals pt1 (skim) | 🟩 |
| Fairness evaluation (matched pairs) | ARB `evals/fairness.py`, `governance/gate/fairness.py` — CTL-0027 measured, HELD as a gate: criterion can't separate noise from bias (D74) | FG Ch23 §23.7 | 🟨 |
| Tracing (OTel → Langfuse) | ARB `platform/observability`, PM `platform/observability` (1.4k) | FG Ch31 · Arize playlist (pick) | 🟩 |
| Cost / token budgets, routing | ARB `enforcement/model_budget.py` (CTL-0020 calibrated on the per-turn peak, E5.1); PM `platform/budget`, ADR-0006 model routing (R1); R1-S2 provider-agnostic route `platform/model/route.py`: pre-call worst-case budget on every provider, per-call-type output caps, unpriced model refused (D-PM-R1-40, S2-f/j) | FG Ch10, Ch33 · Himanshu #5, #17 | 🟨 |

## D. Platform & cloud

| Topic | Where | Source | Status |
|---|---|---|---|
| Ports & adapters (Protocol seams, fakes, import firewall) | `platform/types.py` + every `platform/*/fakes.py`; tests | FG Ch7 · Ledger P0 | 🟩 |
| GCP live bindings: Vertex, Cloud KMS, Firestore, GCS anchor, Model Armor | ARB E4 (`infra/gcp/`, `platform/{model,anchor,state,screening}`, `platform/signing_kms.py`, `platform/classifier/model_armor.py`) | FG Ch41 §41.9 · GCP docs on demand | 🟩 (built by Claude Code — trace it) |
| IaC, CI/CD, Workload Identity Federation | **GAM** (your hand-built M0) + ARB `.github/workflows/ci.yml` | FG Ch30 · CI/CD playlist | 🟨 — M1 is the open rebuild |
| Containers, local stack | ARB `Dockerfile`, `docker-compose.yml` | FG Ch30, Ch37 · AIEFS Ph0 Docker | 🟩 |
| HTTP API service | PM `api/` (FastAPI) | FG Ch25 · Backend first principles; Postman API design | 🟩 |

## D2. System design around the agent

Covered in depth in **`maps/system_design_track.md`** (SD-01…SD-16: edge & routing, API design, communication, auth, state & scale, data, reliability, deployment & DevOps, observability & AgentOps, security & multi-tenancy, capacity & cost, multi-region & DR, then lifecycle & release, runtimes & managed platforms, evaluate/simulate/optimise, maintenance), applied in `design/pm-agent-at-scale.md`. FG Parts V–VI (Ch25–40). Status today: 3 🟩 · 12 🟨 · 1 🟥.

## D3. Agent lifecycle (FG Part VI, SD-13…SD-16)

| Topic | Where | Source | Status |
|---|---|---|---|
| Agent development lifecycle, intake → retirement | ARB lifecycle gates (`governance/gate`), PM phase kits | FG Ch34 | 🟨 |
| Frameworks, SDKs, studios; tools and sandboxes | ARB hosts ADK, LangGraph, OpenAI Agents SDK behind gateways (E3); MCP gateways | FG Ch35–36 | 🟨 |
| Versioning, registries, release, rollback | ARB config digest + sign-off; PM committed eval baseline | FG Ch38 | 🟨 |
| Evaluation, simulation, optimisation loop | ARB/PM `evals/`; PM `replay.py` | FG Ch39 | 🟨 |
| Maintenance: deprecation, drift, recertification, retirement | ARB quarterly AGT bump; tiers re-derived on every gate run; PM drift vs baseline | FG Ch40 | 🟨 |

## D4. Platforms and managed services (FG Part VII, App. I)

| Topic | Where | Source | Status |
|---|---|---|---|
| Google Cloud: Gemini Enterprise Agent Platform | ARB live bindings (Vertex, Firestore, GCS, KMS, Model Armor); no Agent Runtime / Registry / Gateway yet (E6 decision) | FG Ch41 | 🟨 |
| AWS: Bedrock and AgentCore | — | FG Ch42 | 🟥 (consume + R41, R45) |
| Microsoft: Foundry, Copilot Studio, Agent 365 | ARB AGT spike only | FG Ch43, Ch47 | 🟥 (consume + R41, R45) |
| Data, SaaS and model-provider platforms | — | FG Ch44 | 🟥 (consume + R45) |
| Runtimes, sessions, memory services | PM LangGraph checkpointer + memory store; ARB Firestore state | FG Ch37 | 🟨 |
| One capability map and governance across platforms | ARB gateways as one enforcement path for any framework (E3) | FG Ch45, App. I | 🟨 |
| Independent tools, build vs buy | TECH-lane bake-offs | FG Ch46 | 🟨 |

## E. Software & systems foundations

| Topic | Where | Source | Status |
|---|---|---|---|
| Typed Python: Protocols, pydantic v2, mypy strict | everywhere | FG Ch7 | 🟩 |
| Testing strategy (850+ tests, fakes, determinism) | ARB `tests/`; PM mutation testing of the Rego policy (`evals/mutation_eligibility.py`, 226 mutants, kill 1.0) + harness falsifiers (`evals/hostile_gate.py`) | FG Ch7, Ch24 · Ledger P0/P1 | 🟩 |
| Idempotency, caching | ARB `enforcement/idempotency.py`, PM `platform/cache` | FG Ch25 §25.5, Ch28 · redis PDF (pick) | 🟩 |
| Reliability patterns (timeouts, breakers, bulkheads, budgets) | partial: gateways, budgets; ARB `evals/retry.py` (bounded retry of effect-free attempts on 429, E5.1); PM `platform/bounded.py` (deny on timeout in every fail-closed path, D-PM-R1-18) | FG Ch29 · stability-patterns PDFs (core) | 🟨 |
| Databases & state (Postgres, Firestore) | PM Postgres checkpointer + memory store (both ran for real at P5 close); ARB `platform/state` (Firestore: contended txn → `StateUnavailableError`; `local.py`); PM product ledger as a derived SQLite index `ledger/store/sqlite.py` (ADR-0007) | FG Ch28 · Hussein Postgres (pick) | 🟨 |
| Distributed systems (replication, partitioning, consensus, streams) | — | FG Ch26, Ch28 · **DDIA 2e** (pick chapters); Arpit pre-reqs | 🟥 |

## F. Model layer (the honest gap — none of your code teaches it)

| Topic | Source | Status |
|---|---|---|
| Transformers & attention | FG Ch8 · Raschka playlist (core) + AIEFS Ph7 L2–L5, L14 | 🟥 |
| Tokenization | FG Ch8 §8.3 · AIEFS Ph5 subword lesson | 🟥 |
| Inference & serving: KV cache, batching, paged attention, speculative decoding | FG Ch9 · AIEFS Ph7 KV + spec-decoding; Himanshu #2 vLLM, #10 Character.AI | 🟥 |
| Model choice, MoE, routing economics | FG Ch10 · Himanshu #11, #17 | 🟥 |
| Fine-tuning / post-training | FG Ch8 §8.8 (concept only) | PARK (not on your path in the next 9 months) |

## Gap summary

- **Your code already teaches ~80% of the target** — the work is *owning* it, not finding new material.
- **Real gaps (🟥) in your code:** distributed systems, multi-region & DR, the non-Google platforms, and the whole model layer. These are unchanged by the book: the code still doesn't teach them.
- **What changed on 2026-10-30:** every gap now has a consume source (FG Parts II, V–VII, App. I) and a rep that defends it (R07, R13, R20, R38–R43, R45, R48). The gap is reps, not material.
- **No further searching needed right now.** The radar watches for genuinely new *concepts*; new tools for existing concepts are logged, not learned.

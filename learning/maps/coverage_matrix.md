# Coverage Matrix — what you need × where you learn it

**Updated:** 2026-10-13. **Goal it serves:** build, govern and defend production enterprise agent systems on GCP (principal-architect level).
**Read this as:** for each topic, your *own code* is the primary teacher (OWN). External resources only fill what your code can't teach (GROUND) or test you under interview pressure (PROVE).

Codes — **ARB** = aicoe-reference-build · **PM** = project_management_building_agent · **GAM** = genai-agent-mastery (your hand-written repo)
Status — 🟩 in your code (learn by tracing) · 🟨 partly in code · 🟥 not in any code (GROUND needed)

## A. Agent mechanics

| Topic | Where it lives in your code | GROUND / SKIM source | Status |
|---|---|---|---|
| Agent loop & tool calling | ARB `agents/customer_service_ops.py`, `agents/tools.py`, `platform/runtime` (ADK) | AIEFS Ph14 "Agent Loop" | 🟩 |
| Graph orchestration, checkpoint, interrupt/resume | PM `platform/runtime` (LangGraph), `platform/approval` | LangGraph playlist (pick) | 🟩 |
| Multi-agent / A2A | ARB `platform/a2a`, `enforcement/a2a_wiring.py` | A2A spec; 30-concepts (skim) | 🟨 |
| MCP (tool-as-server, integrity) | ARB `gateways/`, `enforcement/mcp_integrity.py`, `platform/gateway` | AIEFS Ph13; MCP spec | 🟩 |
| Memory | PM `platform/memory` | Neural Maze KG memory (pick) | 🟨 |
| RAG / retrieval / grounding | ARB `platform/retrieval`, KB tools; PM grounding (CTL-0015) | Zilliz playlist; Himanshu #1 Perplexity | 🟩 |
| Structured outputs / contracts | ARB `enforcement/contracts.py`; PM `contracts/` | AIEFS Ph5 constrained decoding | 🟩 |

## B. Governance & security (your strength — prove it from code)

| Topic | Where | Source | Status |
|---|---|---|---|
| Control catalog, fleet-first tiering, gate | ARB `governance/catalog.py`, `governance/tiering`, `governance/gate`; root `governance/catalog` | Ledger P2 | 🟩 |
| PEP/PDP, policy-as-code (OPA/Rego, Cedar) | `chokepoint.py`, `enforcement/plane.py`, `platform/policy/{opa,rego,cedar}.py`, `governance/policies/rego/tool_call.rego` | Ledger P3 | 🟩 |
| Identity, delegation, capability tokens | ARB `enforcement/tokens.py` (1.2k lines), `platform/identity` | OAuth token exchange (RFC 8693) | 🟩 |
| HITL approval, separation of duties | ARB `approval_ui/`, PM `platform/approval` | Ledger P3/P4 | 🟩 |
| Evidence: hash chain, redaction, signing, anchoring | ARB `evidence/{writer,chain,redaction,anchoring}.py`, `platform/signing.py` (Ed25519 + Cloud KMS) | Ledger P0/P4 | 🟩 |
| Prompt injection, guardrails, content screens | PM `agents/guardrails` (1.7k), ARB `enforcement/guardrails.py`, `platform/screening` | OWASP Agentic Top 10; Himanshu #8 Llama Guard | 🟩 |
| Red-teaming & assurance | ARB P5 + `docs/`; PM P5 report | Ledger P5 | 🟩 |
| Standards crosswalk (NIST/ISO 42001/EU AI Act) | root `governance/crosswalk` | your corpus | 🟩 |

## C. Evals, observability, cost

| Topic | Where | Source | Status |
|---|---|---|---|
| Golden-set vs live eval, eval-as-gate | ARB `evals/`, PM `evals/` | Agentic Evals pt1 (skim) | 🟩 |
| Tracing (OTel → Langfuse) | ARB `platform/observability`, PM `platform/observability` (1.4k) | Arize playlist (pick) | 🟩 |
| Cost / token budgets, routing | ARB `enforcement/model_budget.py`; PM `platform/budget` | Himanshu #5, #17 | 🟨 |

## D. Platform & cloud

| Topic | Where | Source | Status |
|---|---|---|---|
| Ports & adapters (Protocol seams, fakes, import firewall) | `platform/types.py` + every `platform/*/fakes.py`; tests | Ledger P0 | 🟩 |
| GCP live bindings: Vertex, Cloud KMS, Firestore, GCS anchor, Model Armor | ARB E4 (`infra/gcp/`, `platform/{model,anchor,state,screening}`) | GCP docs on demand | 🟩 (built by Claude Code — trace it) |
| IaC, CI/CD, Workload Identity Federation | **GAM** (your hand-built M0) + ARB `.github/workflows/ci.yml` | CI/CD playlist | 🟨 — M1 is the open rebuild |
| Containers, local stack | ARB `Dockerfile`, `docker-compose.yml` | AIEFS Ph0 Docker | 🟩 |
| HTTP API service | PM `api/` (FastAPI) | Backend first principles; Postman API design | 🟩 |

## D2. System design around the agent

Covered in depth in **`maps/system_design_track.md`** (SD-01…SD-12: edge & routing, API design, communication, auth, state & scale, data, reliability, deployment & DevOps, observability & AgentOps, security & multi-tenancy, capacity & cost, multi-region & DR), applied in `design/pm-agent-at-scale.md`. Status today: 3 🟩 · 8 🟨 · 1 🟥.

## E. Software & systems foundations

| Topic | Where | Source | Status |
|---|---|---|---|
| Typed Python: Protocols, pydantic v2, mypy strict | everywhere | — | 🟩 |
| Testing strategy (850+ tests, fakes, determinism) | ARB `tests/` | Ledger P0/P1 | 🟩 |
| Idempotency, caching | ARB `enforcement/idempotency.py`, PM `platform/cache` | redis PDF (pick) | 🟩 |
| Reliability patterns (timeouts, breakers, bulkheads, budgets) | partial: gateways, budgets | stability-patterns PDFs (core) | 🟨 |
| Databases & state (Postgres, Firestore) | PM Postgres checkpointer; ARB `platform/state` | Hussein Postgres (pick) | 🟨 |
| Distributed systems (replication, partitioning, consensus, streams) | — | **DDIA 2e** (pick chapters); Arpit pre-reqs | 🟥 |

## F. Model layer (the honest gap — none of your code teaches it)

| Topic | Source | Status |
|---|---|---|
| Transformers & attention | Raschka playlist (core) + AIEFS Ph7 L2–L5, L14 | 🟥 |
| Tokenization | AIEFS Ph5 subword lesson | 🟥 |
| Inference & serving: KV cache, batching, paged attention, speculative decoding | AIEFS Ph7 KV + spec-decoding; Himanshu #2 vLLM, #10 Character.AI | 🟥 |
| Model choice, MoE, routing economics | Himanshu #11, #17 | 🟥 |
| Fine-tuning / post-training | — | PARK (not on your path in the next 9 months) |

## Gap summary

- **Your code already teaches ~80% of the target** — the work is *owning* it, not finding new material.
- **Real gaps (🟥):** distributed systems and the end-to-end architecture around the agent (SYSTEMS lane, 2 of every 6 reps), and the whole model layer (MODEL lane, 1 of every 6).
- **No further searching needed right now.** The radar watches for genuinely new *concepts*; new tools for existing concepts are logged, not learned.

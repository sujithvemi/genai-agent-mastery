# NEXT — the queue

**Rule:** do the top **Ready** rep. Swap allowed only for a rep tagged with what you're building this week (R2).
**Cycle:** 3 OWN : 2 SYSTEMS : 1 MODEL, PROVE once a month. **After any gap:** 2 most-overdue cards, then the top rep.

## Ready (rep files exist)

| Rep | Lane | What | Time |
|---|---|---|---|
| **R01** | OWN · Trace | A refund from the model's tool call to the evidence log (ARB) → `reps/R01_trace_golden_path.md` | 30–40 m |
| **R02** | OWN · Defend | Ledger P0 — seams, do-nothing chokepoint, evidence → `reps/R02_defend_ledger_P0.md` | 25 m |
| **R03** | OWN · Defend | Ledger P1 — instruction ≠ control → `reps/R03_defend_ledger_P1.md` | 25 m |
| R04 | OWN · Trace+Defend | Why CRITICAL vs MEDIUM — tiering, gate, Ledger P2 → `reps/R04_trace_tiering_gate.md` | 40 m |
| R05 | SYSTEMS | SD-01 + SD-02: request path and the run API → `reps/R05_sys_request_path_api.md` | 40 m |

## Backlog (rep file generated when it reaches Ready)

| Rep | Lane | What | Anchor |
|---|---|---|---|
| R06 | SYSTEMS | SD-04 AuthN/AuthZ end to end: user OIDC → API → agent identity → tool on-behalf-of; service identity (WIF, SA) → design §4 | ARB `enforcement/tokens.py`, PM `platform/identity` |
| R07 | MODEL | Attention from scratch — Raschka *Build an LLM* video ch.3 + AIEFS Ph7 "Self-Attention from Scratch" | 🟥 |
| R08 | OWN · Trace | Evidence chain + redaction, hands-on: `make demo-tamper`, then `evidence/{chain,redaction}.py` | ARB |
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
| R24 | OWN · Rebuild | M1: WIF-driven Terraform plan-on-PR / apply-on-merge for GAM's hello_agent | GAM `infra/` |

Remaining SYSTEMS modules (SD-11 capacity & cost, SD-12 multi-region & DR) are added by the weekly sync / check-in as the queue drains. The weekly sync also inserts reps for whatever the builds shipped that week.

## Done

| Rep | Date | Grade |
|---|---|---|

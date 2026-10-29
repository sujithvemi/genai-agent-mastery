# Comprehension Map — your debt ledger for the two builds

**Updated:** 2026-10-26 (weekly sync). Rate each module after a rep touches it. Leave ⬜ until then — honest beats optimistic.

| Rating | Means | Test |
|---|---|---|
| ⬜ | not yet looked at | — |
| **E** | can **Explain** what it does and why it exists, from memory | whiteboard it in 2 min |
| **M** | can **Modify** it safely (know what breaks, which tests guard it) | describe a change + the tests that would catch a mistake |
| **R** | can **Rebuild** a minimal version by hand | did a Rebuild rep |

Target by 2026-12-13: shared core all **E**, chokepoint + evidence chain + tiering at **M**, one **R**.

## 1. Shared core — learn once, applies to both (ARB `src/aicoe/` · PM `src/pm_agent/`)

| Module | ARB path (lines) | PM path (lines) | Why it matters | Rep | Rating |
|---|---|---|---|---|---|
| Protocol seams + fakes | `platform/types.py` (253), `platform/*/fakes.py` | `platform/*` | Portability bet; everything plugs in here | R02, R15 | ⬜ |
| Tool chokepoint (the PEP) | `chokepoint.py` | `platform/pep/` (998) | Single point every side-effect passes | R01 | ⬜ |
| Enforcement plane (decide) | `enforcement/plane.py` (1,415) | `platform/pep/`, `platform/policy/` | Where controls actually fire | R01, R09 | ⬜ |
| Policy engine + Rego bundle | `platform/policy/{opa,rego,cedar}.py`; `governance/policies/rego/tool_call.rego` | `platform/policy/` (387 — was 238; + `eligibility.py` R1-S0) | Policy-as-code, fail-closed | R09, R36 | ⬜ |
| Policy information point | `enforcement/pip.py` (360) | — | Facts the policy reads; "no dead policy" | R09 | ⬜ |
| Evidence writer + hash chain | `evidence/writer.py` (363), `evidence/chain.py` (169) | `platform/evidence/` (1,552) | Tamper-evident audit | R01, R08 | ⬜ |
| Redaction | `evidence/redaction.py` (383) | `platform/evidence/` | Evidence must not be a PII honeypot | R08 | ⬜ |
| Tiering engine | `governance/tiering/` (228) | `governance/tiering/` (215) | Fleet-first: `min_tier` + `applies_when` | R04 | ⬜ |
| Gate (deployability) | `governance/gate/` (1,115 — was 603; + `fairness.py` CTL-0027) | `governance/gate/` (3,091 — was 2,436; + `conformance_ws_m.py`, `conformance_structural.py`) | Fail-closed promotion | R04 | ⬜ |
| Manifest + catalog loading | `governance/{manifest,catalog}.py` | `governance/` | Agent ↔ controls contract | R04 | ⬜ |
| Import firewall / tests | `tests/` | `tests/` | Vendor code can't leak past seams | R15 | ⬜ |

## 2. ARB-only (aicoe-reference-build)

| Module | Path (lines) | Topic | Rating |
|---|---|---|---|
| Agents | `agents/customer_service_ops.py`, `knowledge_advisor.py`, `tools.py` (1,015) | ADK agent + governed write | ⬜ |
| Capability & approval tokens | `enforcement/tokens.py` (1,246) | Identity, delegation, SoD | ⬜ |
| Conformance suite | `enforcement/conformance.py` (1,392) | Proving controls fire | ⬜ |
| Guardrails, contracts, grounding | `enforcement/{guardrails,contracts}.py` | Output contracts, CTL-0014/15 | ⬜ |
| Model budget + identity pin | `enforcement/model_budget.py` (561) | CTL-0020/21 cost & model pin | ⬜ |
| MCP integrity | `enforcement/mcp_integrity.py` (675) | CTL-0024 tool integrity | ⬜ |
| Gateways (model + network tool) | `gateways/` (1,741), `platform/gateway` (1,122) | One enforcement path for any framework (E3) | ⬜ |
| A2A | `platform/a2a`, `enforcement/a2a_wiring.py` | Agent-to-agent governed edges | ⬜ |
| Evidence anchoring + signing | `evidence/anchoring.py`, `platform/signing.py`, `platform/signing_kms.py` (148, new E4-S3), `platform/anchor` | Ed25519 / Cloud KMS, GCS anchor (E4) | ⬜ |
| Approval UI | `approval_ui/` (1,110) | Human trust boundary (E4) | ⬜ |
| GCP bindings | `infra/gcp/`, `platform/{model,state,screening}` | Vertex, Firestore, Model Armor (E4) | ⬜ |
| Evidence pack, config digest, sign-off | `governance/{evidence_pack,config_digest,signoff}.py` (`evidence_pack.py` 787; GR1-U1/F1: the pack now discloses what it does not show) | GTM demo assurance | ⬜ |
| Demo harness | `demo/` (2,643; + `portability` beat GR1-U1: ADK / LangGraph / OpenAI Agents SDK on one screen) | The GTM demo you'll present — GR1 self-test R37 | ⬜ |
| Classifier composition (new, E5) | `platform/classifier/` (688), `enforcement/classifier_gate.py` (341) | D52 monotone `max(ALLOW<HOLD<DENY)`: a classifier can only add a hold — CTL-0025 content safety | ⬜ |
| Typed answer contract (new, E5/E5.1) | `enforcement/answer_contract.py` (163), `platform/model/structured.py` (81) | CTL-0026: `{answer, citations≥1}` from this turn's retrieval or the fixed refusal; tool loop, then a separate typed final request | ⬜ |
| Fairness eval + gate (new, E5) | `evals/fairness.py` (439), `enforcement/fairness_measurement.py` (291), `enforcement/fairness_conformance.py` (109), `governance/gate/fairness.py` (512) | CTL-0027 matched pairs, signed digest-bound artifact — measured 0.375, HELD as a gate (D74) | ⬜ |
| Live harness + report (new, E4/E5.1) | `platform/cloud/live_env.py` (119), `governance/live_report.py` (330), `evals/retry.py` (235) | EXERCISED only by a recorded run; retry a 429 only when no effect happened | ⬜ |

## 3. PM-only (pm-agent)

| Module | Path (lines) | Topic | Rating |
|---|---|---|---|
| Planning graph | `agents/planning/` (1,754) | Planner-router-worker on LangGraph | ⬜ |
| Guardrails / injection defence | `agents/guardrails/` (3,519 — was 1,755) | Data-channel separation, output guard — FROZEN at `285a44e`, blocks only on hard signals (D-PM-P5-close-1/1a; ADR-0005) | ⬜ |
| Runtime + interrupt/resume | `platform/runtime/` (673), `platform/approval/` (493) | HITL with checkpointing | ⬜ |
| Jira via MCP | `platform/jira/` (1,197) | Real tool integration | ⬜ |
| Memory | `platform/memory/` (1,002) | Agent memory design | ⬜ |
| Crypto | `platform/crypto/` (662 — was 541; + `memory_mac.py`) | Ed25519 sign/verify, key seam | ⬜ |
| Observability | `platform/observability/` (1,399) | OTel → Langfuse | ⬜ |
| Run API | `api/` (320) | FastAPI service surface — R05 | ⬜ |
| Evals | `evals/` (3,416 — was 1,672) | Golden set + live eval | ⬜ |
| Structural plan guard (new, P5-5R) | `agents/guardrails/structural.py` (829), `egress.py` (216), `action_intent.py` (219) | Rules on what a plan item claims/changes vs retrieved structure — why phrase lists lost (56% held-out) | ⬜ |
| Governed durable memory (new, P5-4/5) | `platform/memory/governed.py` (530), `pii.py` (322), `postgres.py` (169), `platform/crypto/memory_mac.py` (260) | Scoped, redacted, MAC-verified memory; no dev key → hint (retrieval-only) mode | ⬜ |
| Model identity + provenance (new, P5-5R) | `platform/model/identity.py` (164), `platform/evidence/provenance.py` (151) | Record the model that *answered*, not the one requested | ⬜ |
| WS-E eval + regression gate (new, P5-5) | `evals/ws_e.py` (1,213), `baseline.py` (468), `replay.py` (337) | Committed baseline + blocking comparison; drift; replay | ⬜ |
| Typed actions + batched grant (new, R1-S0) | `actions/` (560: `union.py` 290, `batch.py` 113, `sanitiser.py` 92) | ADR-0005 closed effect union (`create_issue`…`delegate`); one signed grant over an ordered manifest of action hashes (D-PM-R1-5/6) | ⬜ |
| Rego eligibility (new, R1-S0) | `platform/policy/eligibility.py` (149), `governance/policies/eligibility/eligibility.rego` (26) + `projects/*.yaml` | Which typed action may target what, per project; deny = `eligibility.default_deny` (control attribution is an S3 decision, D-PM-R1-15) | ⬜ |
| Fail-closed timeouts + operator config (new, R1-S0) | `platform/bounded.py` (51), `platform/operator_config.py` (84) | Deny on overrun (2 s worker thread, D-PM-R1-18); executor wiring only from operator config, `.env` from the install not the CWD (D-PM-R1-19/25) | ⬜ |
| Product ledger + lifecycle packs (new, R1-S0) | `ledger/` (1,080: `models.py`, `packs.py` 416, `minimise.py`, `store/sqlite.py` 244), `packs/software/pack.yaml` | ADR-0007: 8 artefact kinds, typed links, packs as inert YAML; SQLite derived index; CTL-0009 memory set on ledger writes | ⬜ |
| Executor contract (new, R1-S0) | `platform/executors/` (842: `contract.py`, `registry.py`, `conformance.py`, `fakes.py`), `platform/jira/apply_shim.py` (81) | ADR-0008: delegate as a typed, approved action; results come back as proposals | ⬜ |
| Adopt-a-repo workflow (new, R1-S1) | `workflows/adopt/` (1,884: `extract.py` 721, `reader.py` 369, `run.py` 366), `evals/adopt.py` (298) | Read-only proposal (PRD-lite, decisions index, backlog); all adopted text is free-text lane (D-PM-R1-30) | ⬜ |
| Hostile-planner gate spec (new, R1-S0) | `governance/hostile_gate.py` (222), `governance/evals/r1_hostile_gate.yaml` | R1 gate: rubber-stamp approver, 0 attacker-originated executed effects; definition pinned by sha256 (D-PM-R1-14/26); harness is S3 | ⬜ |

## 4. GAM-only (your hand-written repo)

| Module | Rating |
|---|---|
| `agents/hello_agent` (M0.3) | E (self-built) |
| M0 Terraform: SAs, WIF, budget | E — but **code not committed** (only backend/provider/variables in repo) |

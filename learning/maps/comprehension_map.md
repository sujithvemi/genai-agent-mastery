# Comprehension Map — your debt ledger for the two builds

**Updated:** 2026-10-13. Rate each module after a rep touches it. Leave ⬜ until then — honest beats optimistic.

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
| Policy engine + Rego bundle | `platform/policy/{opa,rego,cedar}.py`; `governance/policies/rego/tool_call.rego` | `platform/policy/` (238) | Policy-as-code, fail-closed | R09 | ⬜ |
| Policy information point | `enforcement/pip.py` (360) | — | Facts the policy reads; "no dead policy" | R09 | ⬜ |
| Evidence writer + hash chain | `evidence/writer.py` (363), `evidence/chain.py` (169) | `platform/evidence/` (1,552) | Tamper-evident audit | R01, R08 | ⬜ |
| Redaction | `evidence/redaction.py` (383) | `platform/evidence/` | Evidence must not be a PII honeypot | R08 | ⬜ |
| Tiering engine | `governance/tiering/` (228) | `governance/tiering/` (215) | Fleet-first: `min_tier` + `applies_when` | R04 | ⬜ |
| Gate (deployability) | `governance/gate/` (603) | `governance/gate/` (2,436) | Fail-closed promotion | R04 | ⬜ |
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
| Evidence anchoring + signing | `evidence/anchoring.py`, `platform/signing.py`, `platform/anchor` | Ed25519 / Cloud KMS, GCS anchor (E4) | ⬜ |
| Approval UI | `approval_ui/` (1,110) | Human trust boundary (E4) | ⬜ |
| GCP bindings | `infra/gcp/`, `platform/{model,state,screening}` | Vertex, Firestore, Model Armor (E4) | ⬜ |
| Evidence pack, config digest, sign-off | `governance/{evidence_pack,config_digest,signoff}.py` | GTM demo assurance | ⬜ |
| Demo harness | `demo/` (2,345) | The GTM demo you'll present | ⬜ |

## 3. PM-only (pm-agent)

| Module | Path (lines) | Topic | Rating |
|---|---|---|---|
| Planning graph | `agents/planning/` (1,754) | Planner-router-worker on LangGraph | ⬜ |
| Guardrails / injection defence | `agents/guardrails/` (1,755) | Data-channel separation, output guard | ⬜ |
| Runtime + interrupt/resume | `platform/runtime/` (673), `platform/approval/` (493) | HITL with checkpointing | ⬜ |
| Jira via MCP | `platform/jira/` (1,197) | Real tool integration | ⬜ |
| Memory | `platform/memory/` (1,002) | Agent memory design | ⬜ |
| Crypto | `platform/crypto/` (541) | Ed25519 sign/verify, key seam | ⬜ |
| Observability | `platform/observability/` (1,399) | OTel → Langfuse | ⬜ |
| Run API | `api/` (320) | FastAPI service surface — R05 | ⬜ |
| Evals | `evals/` (1,672) | Golden set + live eval | ⬜ |

## 4. GAM-only (your hand-written repo)

| Module | Rating |
|---|---|
| `agents/hello_agent` (M0.3) | E (self-built) |
| M0 Terraform: SAs, WIF, budget | E — but **code not committed** (only backend/provider/variables in repo) |

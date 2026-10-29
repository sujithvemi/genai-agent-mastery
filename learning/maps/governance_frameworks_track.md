# Governance Frameworks Track — understand, apply, build for a client

**Updated:** 2026-10-26 (weekly sync). **Why:** governance is your day job and your GTM offer. Knowing *your* build is not enough; you must be able to (1) read any external framework or toolkit through your build, (2) apply a framework to a brand-new agent yourself, and (3) design and build the framework for a client's estate. Microsoft's **Agent Governance Toolkit (AGT)** is the worked example; the same three levels apply to every framework below.

## The three levels

| Level | You can… | Proof | Where |
|---|---|---|---|
| **GF-L1 Understand** | Explain a framework's model, map each of its parts to the component in your build that does the same job, and say where it is stronger or weaker — with evidence, not opinion | One mapping table + one defended answer per framework | OWN reps (GF-1…GF-6) |
| **GF-L2 Apply** | Take a new agent from zero to governed yourself: tier it, select controls, write policy, wire the PEP + evidence, pass the gate | **Capstone A** — `capstones/A_govern_a_new_agent.md` | Rebuild reps, hand-written in this repo |
| **GF-L3 Build for a client** | Tailor catalog, tiering, crosswalk, enforcement points and operating model to a client's platforms and regulations, and plan the rollout | **Capstone B** — `capstones/B_client_framework.md` | PROVE slot, alternating months |

## GF-L1 — framework literacy, always through your build

| # | Framework / toolkit | Type | Anchor in your build | Rep |
|---|---|---|---|---|
| GF-1 | **Microsoft Agent Governance Toolkit** (AGT) | OSS toolkit: policy engine (`agentmesh` / `agent_os`, `governance.toolkit/v1` YAML), identity/trust, plus other runtime-governance modules | ARB E3-S4 spike: `docs/architecture/AGT_INTEROP.md`, `spikes/agt/`, `tests/agt_policy.py`, `make agt-parity`; decisions D53, D62, D63; GR1 client answer: `docs/showcase/CLIENT_QA.md` Q&A 23 | **R25** (Ready) |
| GF-2 | OWASP Top 10 for Agentic Applications (Dec 2025) | Threat taxonomy | ARB control catalog + red-team corpus (`tests/redteam/`); crosswalk now tags CTL-0025 → LLM05, CTL-0026 → LLM09 (E5); PM ADR-0005 cites LLM06 / Agentic excessive agency; PM R1 hostile-planner gate (`governance/hostile_gate.py`, `governance/evals/r1_hostile_gate.yaml`: fully hostile planner → 0 attacker-originated executed effects, D-PM-R1-7/14) | backlog |
| GF-3 | NIST AI RMF (+ GenAI profile; agentic profile draft) · ISO/IEC 42001 · EU AI Act | Risk management / management system / law | root `governance/crosswalk/` (3 statuses, ISO cells marked [Verify]); ARB `governance/crosswalk/{crosswalk,gcl_crosswalk}.yaml` gained CTL-0025/0026 (NIST MEASURE/MANAGE; EU AI Act Art. 50 [Verify]); PM ISO A.7.4 [Verify] carried to R1; ARB GR1 client wording for "are you EU AI Act compliant?" — `docs/showcase/CLIENT_QA.md` Q&A 25 + `CLAIMS_CARD.md` | backlog |
| GF-4 | Platform-native governance: GCP (Gemini Enterprise Agent Platform: Agent Registry, Identity, Gateway, Model Armor) · Salesforce Agentforce trust controls · Microsoft Copilot Studio / Entra agent controls · AWS Bedrock AgentCore · Azure AI Foundry agent service | Vendor controls | ARB E4/E5 (Model Armor as a classifier backend `platform/classifier/model_armor.py`; Cloud KMS signing `platform/signing_kms.py`; GCS retention lock `infra/gcp/lock_anchor_bucket.sh`, NOT LOCKED); your GTM pack; GR1 answer to "can it govern our Copilot Studio agents?" — `docs/showcase/CLIENT_QA.md` Q&A 24 | backlog — **[Verify] every feature claim against current vendor docs** |
| GF-5 | Policy engines compared: OPA/Rego vs Cedar vs AGT YAML | PDP languages | `platform/policy/{opa,rego,cedar}.py`, AGT gaps G1–G7; PM ADR-0005 per-project Rego eligibility policy for typed actions — built R1-S0: `governance/policies/eligibility/eligibility.rego` + `platform/policy/eligibility.py` (bounded, fail closed; which control a deny cites is an S3 decision, D-PM-R1-15) | backlog |
| GF-6 | Singapore IMDA agentic AI framework · CSA agentic work | Agent-specific governance frameworks | your catalog + crosswalk | backlog |

**The GF-L1 output for every framework** (one file each in `frameworks/`, written by you):
1. Its model in 5 lines. 2. Mapping table: their concept → your component (file) → equal / stronger / weaker / absent. 3. One question a client will ask ("why not just use X?") and your evidence-backed answer. 4. When you would recommend it, and when you would not.

## What "covered" means for AGT specifically

| Question | Covered by |
|---|---|
| What is AGT and how is it structured? | GF-1 (R25), step 1 |
| How does it compare to what I built? Where does it fit behind my seams? | R25 steps 2–3: the spike, the adapter, the parity suite |
| What can't it do at the pinned version, and how do I say that responsibly? | R25: gaps G1–G7 and the D63 wording rule |
| Can I use it to govern a **new** agent? | Capstone A, stage A4 (express the controls AGT can express as AGT policies alongside Rego, run parity) |
| Can I build a framework like it, or tailor one, **for a client**? | Capstone B: B1–B6 design the client framework, **B7 builds and packages the toolkit for them** (core + client overlay, platform adapters, conformance suite). ARB is your reference implementation; Rebuild R10 re-implements its core by hand |
| How do I keep current as it changes (3 major versions in ~6 months)? | ARB RUNBOOKS §7 quarterly bump + `test_the_recorded_language_gaps_are_still_there`; the research radar watches it |

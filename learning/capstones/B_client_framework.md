# Capstone B — design the governance framework for an enterprise estate

**Level:** GF-L3 Build for an estate. **Cadence:** the PROVE slot, alternating months with the system-design drill. (The file keeps its old name so the field guide's links still work.)

**Scenario (synthetic, assumed):** an enterprise running agents on **two platforms** — a CRM-native agent platform (Salesforce-style) and Gemini Enterprise on GCP — plus a few custom ADK agents; 30 agents today, 150 planned; operates in the EU and US; low governance maturity; wants the provider to *enable* while they build framework and tooling. This learning environment has no clients (L-27): client work happens in your enterprise Claude, and any future personal-consulting client gets its own project. Keep this capstone synthetic.

**📖 Field guide:** [Ch53 Capstone B](../fieldguide/capstone-b.html) is the stage guide, with the framework-pack outline (§53.9) and a self-grading rubric (§53.10). Ch50–51 carry B6; Appendix I is the cross-platform service map for B3.

## Stages

| Stage | Deliverable (you write it) | Draws on |
|---|---|---|
| B1 | **Inventory & tiering model**: agent archetypes on each platform; which axes drive tier for them; how many land in each tier | ARB tiering (fleet-first), R04 · 📖 Ch53 §53.2, Ch13 |
| B2 | **Control catalog cut**: which of your 22+ controls apply, which change meaning on a SaaS platform you cannot instrument, which new ones are needed | ARB catalog, GF-2 OWASP · 📖 Ch53 §53.3, Ch14, App. B |
| B3 | **Enforcement-point map**: for each control × platform — native platform control, gateway (MCP/A2A), OPA/Cedar/AGT, or process-only. Mark where AGT fits and where it can't (evidence: R25) | GF-1, GF-4, GF-5 · 📖 Ch53 §53.4, Ch12, Ch45, App. I |
| B4 | **Crosswalk**: controls → NIST AI RMF / ISO 42001 / EU AI Act obligations for this estate's risk classes | GF-3, ARB crosswalk · 📖 Ch53 §53.5, Ch48, Ch49 |
| B5 | **Evidence & assurance**: what evidence each control emits, where it is stored, how an auditor verifies it | ARB evidence plane, R08/R09 · 📖 Ch53 §53.6, Ch22, Ch24 |
| B7 | **Build the toolkit for the estate (hands-on)**: package a generic core + an estate overlay (core semantics never fork; the overlay holds the estate's catalog cut, tiers and adapters); write the platform adapters the B3 map needs (gateway PEP, native-control readers); ship a conformance suite the estate's owners run to prove each control fires; decide where AGT is embedded vs where your engine is | ARB `src/aicoe/` as the reference implementation, R10 Rebuild, Capstone A code · 📖 Ch53 §53.8, Ch47 §47.8, Ch46 §46.5 |
| B6 | **Operating model + rollout**: RACI, promotion gates, waiver process, 90-day interim vs target state, dependencies, risks | your AICoE + DoE/CDO session material · 📖 Ch53 §53.7, Ch50, Ch51 (rep R47) |

**Output:** a 10–15 page framework pack + one architecture diagram (B1–B6), and a runnable toolkit skeleton with its conformance suite (B7). Every assumption labelled.

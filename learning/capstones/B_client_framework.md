# Capstone B — design the governance framework for a client estate

**Level:** GF-L3 Build for a client. **Cadence:** the PROVE slot, alternating months with the system-design drill. **Doubles as:** GTM support-pack material.

**Scenario (generic, assumed — not client facts):** an enterprise running agents on **two platforms** — a CRM-native agent platform (Salesforce-style) and Gemini Enterprise on GCP — plus a few custom ADK agents; 30 agents today, 150 planned; operates in the EU and US; low governance maturity; wants the provider to *enable* while they build framework and tooling. If you work a real pursuit, keep client facts in its own client folder, never here.

## Stages

| Stage | Deliverable (you write it) | Draws on |
|---|---|---|
| B1 | **Inventory & tiering model**: agent archetypes on each platform; which axes drive tier for them; how many land in each tier | ARB tiering (fleet-first), R04 |
| B2 | **Control catalog cut**: which of your 22+ controls apply, which change meaning on a SaaS platform you cannot instrument, which new ones are needed | ARB catalog, GF-2 OWASP |
| B3 | **Enforcement-point map**: for each control × platform — native platform control, gateway (MCP/A2A), OPA/Cedar/AGT, or process-only. Mark where AGT fits and where it can't (evidence: R25) | GF-1, GF-4, GF-5 |
| B4 | **Crosswalk**: controls → NIST AI RMF / ISO 42001 / EU AI Act obligations for this client's risk classes | GF-3, ARB crosswalk |
| B5 | **Evidence & assurance**: what evidence each control emits, where it is stored, how an auditor verifies it | ARB evidence plane, R08/R09 |
| B7 | **Build the toolkit for the client (hands-on)**: package a generic core + client overlay (the same split as your `agentgov` / `agentgov_<client>` decision D-1); write the platform adapters the B3 map needs (gateway PEP, native-control readers); ship a conformance suite the client runs to prove each control fires; decide where AGT is embedded vs where your engine is | ARB `src/aicoe/` as the reference implementation, R10 Rebuild, Capstone A code |
| B6 | **Operating model + rollout**: RACI, promotion gates, waiver process, 90-day interim vs target state, dependencies, risks | your AICoE + DoE/CDO session material |

**Output:** a 10–15 page client framework pack + one architecture diagram (B1–B6), and a runnable client toolkit skeleton with its conformance suite (B7). Every assumption labelled.

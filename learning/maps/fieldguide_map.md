# Field Guide Map — the book, read through your reps

**Updated:** 2026-10-30 · **Book:** *Architect's Field Guide*, edition 1 — 55 chapters, appendices A–I, platform facts as of 2026-10-21.
**Open it:** `fieldguide/index.html` (local, links work offline) · `fieldguide/field-guide.pdf` (575 pages; phone, tablet, plane) · published copy (private): https://claude.ai/artifact/A18JhEfBV1x2tEKkXBeFmg

## The rule (L-22, L-23)

A chapter is the **consume** step. Its rep is the **defend** step. Reading never counts as progress (R1), and a chapter is never a substitute for the Trace rep that walks the real code.

- **Read** = you read the sections a rep's 📖 line names (date it).
- **Defended** = a rep that defends the chapter closed at grade ≥ B (rep ID + date). Only then may cards come from it (R4).
- A chapter with no rep in the queue yet is reference: look things up in it, don't schedule it.

## Using it in a session

1. Open the rep file. Its **📖 Read** line names the chapter sections.
2. **Trace rep:** write Step 0's predictions first (R3), then read, then trace. **Defend rep:** read, close the book, answer cold. **SYSTEMS rep:** the chapter is the default "Learn" pick; external sources become depth. **Rebuild:** read before, close it while you build.
3. After the rep, the chapter's **Prove it** questions are extra Defend practice (say them aloud), and its **Card candidates** are the card source — only for what you defended.
4. Reading on the phone between weekends is fine: the cloud nudge names the chapter for the next rep.
5. Tick here. The rep coach (`prompts/REP_SESSION.md`) does it for you at close-out.

## Reading paths (from the book's front page)

| Path | Chapters | Use it when |
|---|---|---|
| Owning the builds | 1 → 2 → 5 → 7, then 13 … 24 | The OWN lane's order: chassis first, then the controls |
| Before the GTM showcase | 11 → 12 → 13 → 14 → 15 → 16 → 22 → 24 → 54 | You need to answer the hard questions about the reference build yourself |
| System design | 25 … 33, then 55 | One chapter per SYSTEMS rep; each feeds `design/pm-agent-at-scale.md` |
| Building and running agents | 34 … 40, then 30, 31 | Lifecycle end to end (SD-13…SD-16) |
| Enterprise platforms | 37, then 41 → 46 | Managed services you will meet in a client estate (GF-4, SD-14) |
| Client framework | 11, 12, 45, 47, 48, 50, 51, 53 | Capstone B; anything you would say to a CDO or CISO |
| The model gap | 8 → 9 → 10 | The MODEL lane |
| Practice | 52 → 53 → 54 → 55 | The PROVE lane |

## Chapters

Leave **Read** and **Defended** blank until true. Lanes as in `README.md`; "Capstone A2" etc. are stages in `capstones/`.

### Part I — The agent as a system

| Ch | Chapter | Lane | Defended by | Read | Defended |
|---|---|---|---|---|---|
| 1 | [Anatomy of an agent harness](../fieldguide/harness-anatomy.html) | OWN | R01 · BT03 · LL10 | | |
| 2 | [The loop, tools and typed outputs](../fieldguide/loop-tools-typed-outputs.html) | OWN | R01 · R32 · BT02 · BT03 | | |
| 3 | [Context, memory and state](../fieldguide/context-memory-state.html) | OWN | R21 · R34 · R12 · BT11 | | |
| 4 | [Retrieval and grounding](../fieldguide/retrieval-grounding.html) | OWN | R01 · R32 · TC-13 lab | | |
| 5 | [Protocols and trust between agents](../fieldguide/protocols-trust.html) | OWN | R11 · BT10 · T05 · LL5 | | |
| 6 | [Orchestration and the meta-harness](../fieldguide/orchestration-meta-harness.html) | OWN | R21 · BT11 · LL1 · LL4 · LL10 | | |
| 7 | [The chassis: seams, fakes and tests that can fail](../fieldguide/chassis-seams-tests.html) | OWN | R02 · R15 · BT01 | | |

### Part II — The model layer

| Ch | Chapter | Lane | Defended by | Read | Defended |
|---|---|---|---|---|---|
| 8 | [Transformers and tokens for architects](../fieldguide/transformers-tokens.html) | MODEL | R07 | | |
| 9 | [Inference and serving](../fieldguide/inference-serving.html) | MODEL | R13 · TC-04 lab | | |
| 10 | [Model choice, routing and model risk](../fieldguide/model-choice-risk.html) | MODEL | R48 · R38 · BT04 · T06 | | |

### Part III — The rulebook

| Ch | Chapter | Lane | Defended by | Read | Defended |
|---|---|---|---|---|---|
| 11 | [What governance must do when software acts](../fieldguide/governance-when-software-acts.html) | OWN | R03 · R26 | | |
| 12 | [A reference model: planes, layers, enforcement points](../fieldguide/reference-model.html) | FRAMEWORKS | R29 · R45 · Capstone B3 | | |
| 13 | [Fleet-first risk tiering](../fieldguide/risk-tiering.html) | OWN | R04 · R28 → A2 · R29 → B1 | | |
| 14 | [The control as a contract](../fieldguide/control-as-contract.html) | OWN | R04 · R09 · Capstone A2 | | |
| 15 | [The lifecycle and its gates](../fieldguide/lifecycle-gates.html) | OWN | R04 · R19 · R24 → A5 | | |

### Part IV — The referee

| Ch | Chapter | Lane | Defended by | Read | Defended |
|---|---|---|---|---|---|
| 16 | [The governed action](../fieldguide/governed-action.html) | OWN | R01 · R03 · R09 · R16 · R36 | | |
| 17 | [Policy as code](../fieldguide/policy-as-code.html) | OWN | R09 · R27 · R36 · BT06 · BT07 | | |
| 18 | [Identity, delegation and capability](../fieldguide/identity-delegation.html) | OWN · SYSTEMS | R06 · R30 · BT08 · BT14 | | |
| 19 | [Human oversight that holds](../fieldguide/human-oversight.html) | OWN | R21 · R30 · R36 · BT11 | | |
| 20 | [Guardrails, classifiers and injection](../fieldguide/guardrails-injection.html) | OWN | R31 · R32 · R33 · R35 · R26 · T04 | | |
| 21 | [Data boundaries](../fieldguide/data-boundaries.html) | OWN | R08 · R34 · R23 | | |
| 22 | [The evidence plane](../fieldguide/evidence-plane.html) | OWN | R01 · R02 · R08 · R10 · R30 · BT08 | | |
| 23 | [Evals as gates](../fieldguide/evals-as-gates.html) | OWN | R22 · R31 · R42 · T03 | | |
| 24 | [Proving controls fire](../fieldguide/proving-controls-fire.html) | OWN | R04 · R37 · Capstone A6 | | |

### Part V — The system around the agent (SYSTEMS, SD-01…SD-12)

| Ch | Chapter | Lane | Defended by | Read | Defended |
|---|---|---|---|---|---|
| 25 | [Edge, request path and API design](../fieldguide/edge-api-design.html) | SYSTEMS | R05 (SD-01/02) · BT05 | | |
| 26 | [Communication and durable execution](../fieldguide/communication-durable-execution.html) | SYSTEMS | R11 (SD-03) · R21 | | |
| 27 | [AuthN and AuthZ end to end](../fieldguide/authn-authz.html) | SYSTEMS | R06 (SD-04) · T09 | | |
| 28 | [State, data and scale](../fieldguide/state-data-scale.html) | SYSTEMS | R12 (SD-05) · R23 (SD-06) · R20 | | |
| 29 | [Reliability for LLM systems](../fieldguide/reliability.html) | SYSTEMS | R18 (SD-07) | | |
| 30 | [Deployment and CI/CD for agents](../fieldguide/deployment-cicd.html) | SYSTEMS | R19 (SD-08) · R24 · BT12 · BT13 | | |
| 31 | [Observability, SLOs and AgentOps](../fieldguide/observability-agentops.html) | SYSTEMS | R22 (SD-09) · BT09 · T01 · T02 | | |
| 32 | [Security architecture and multi-tenancy](../fieldguide/security-multitenancy.html) | SYSTEMS | R23 (SD-10) · R26 | | |
| 33 | [Capacity, cost and multi-region](../fieldguide/capacity-cost-regions.html) | SYSTEMS | R38 (SD-11) · R39 (SD-12) | | |

### Part VI — The agent lifecycle (SYSTEMS, SD-13…SD-16)

| Ch | Chapter | Lane | Defended by | Read | Defended |
|---|---|---|---|---|---|
| 34 | [The agent development lifecycle](../fieldguide/agent-development-lifecycle.html) | SYSTEMS | R40 (SD-13) · R28 → A0–A1 | | |
| 35 | [Frameworks, SDKs and studios](../fieldguide/frameworks-sdks-studios.html) | TECH | R41 · BT15 · T07 · LL10 | | |
| 36 | [Tools, integration, sandboxes and computer use](../fieldguide/tools-integration-sandboxes.html) | SYSTEMS | R41 · R35 · T05 | | |
| 37 | [Runtimes, sessions and memory services](../fieldguide/runtime-sessions-memory.html) | SYSTEMS | R41 (SD-14) · R12 | | |
| 38 | [Versioning, registries and release management](../fieldguide/versioning-release.html) | SYSTEMS | R40 (SD-13) · R19 · BT12 · BT13 | | |
| 39 | [Evaluation, simulation and optimization](../fieldguide/evaluation-simulation-optimization.html) | SYSTEMS | R42 (SD-15) · R22 · T03 | | |
| 40 | [Maintenance and evolution](../fieldguide/maintenance-evolution.html) | SYSTEMS | R43 (SD-16) | | |

### Part VII — Platforms and tools

| Ch | Chapter | Lane | Defended by | Read | Defended |
|---|---|---|---|---|---|
| 41 | [Google Cloud: Gemini Enterprise Agent Platform](../fieldguide/google-cloud.html) | OWN · FRAMEWORKS | R17 · R30 · R45 (GF-4) · BT14 | | |
| 42 | [AWS: Bedrock and AgentCore](../fieldguide/aws.html) | FRAMEWORKS | R45 · R41 | | |
| 43 | [Microsoft: Foundry, Copilot Studio and Agent 365](../fieldguide/microsoft.html) | FRAMEWORKS | R45 · R41 · R25 · T07 | | |
| 44 | [Data, SaaS and model-provider platforms](../fieldguide/data-saas-model-platforms.html) | FRAMEWORKS | R45 · R29 | | |
| 45 | [Across platforms: capability map and governance](../fieldguide/across-platforms.html) | FRAMEWORKS | R45 · R29 → B3 | | |
| 46 | [The independent tool landscape and build vs buy](../fieldguide/tool-landscape.html) | TECH · LANDSCAPE | T01–T19 bake-offs · LL1–LL10 | | |

### Part VIII — Frameworks and law

| Ch | Chapter | Lane | Defended by | Read | Defended |
|---|---|---|---|---|---|
| 47 | [Microsoft AGT through your build](../fieldguide/agt-through-your-build.html) | FRAMEWORKS | R25 (GF-1) · BT16 · Capstone A4, B7 | | |
| 48 | [Standards, law and crosswalk engineering](../fieldguide/standards-law-crosswalk.html) | FRAMEWORKS | R26 (GF-2) · R44 (GF-3) · R46 (GF-6) · Capstone B4 | | |
| 49 | [Regulated industries](../fieldguide/regulated-industries.html) | FRAMEWORKS | R46 · Capstone B4 | | |

### Part IX — The operating model

| Ch | Chapter | Lane | Defended by | Read | Defended |
|---|---|---|---|---|---|
| 50 | [The AICoE operating model](../fieldguide/aicoe-operating-model.html) | CAPSTONE B | R47 → B6 | | |
| 51 | [Readiness and the first 90 days](../fieldguide/readiness-first-90-days.html) | CAPSTONE B | R47 → B6 | | |

### Part X — Practice

| Ch | Chapter | Lane | Defended by | Read | Defended |
|---|---|---|---|---|---|
| 52 | [Capstone A: govern a new agent by hand](../fieldguide/capstone-a.html) | CAPSTONE A | R28 → A0–A1, then A2–A6 (R10, R24 feed it) | | |
| 53 | [Capstone B: a framework for a client estate](../fieldguide/capstone-b.html) | CAPSTONE B | R29 → B1–B2, R47 → B6, then B3–B5, B7 | | |
| 54 | [Defending your builds](../fieldguide/defending-your-builds.html) | PROVE | R37 · R14 | | |
| 55 | [The design interview for governed agents](../fieldguide/design-interview.html) | PROVE | R14 and every monthly drill | | |

## Appendices — what each is for in the learning system

| Appendix | Use it for |
|---|---|
| [A Glossary](../fieldguide/appendix-glossary.html) | A term at engineering resolution, before you use it with a client |
| [B Control catalog](../fieldguide/appendix-control-catalog.html) | Every control in both builds, generated from `governance/catalog/` — Capstone A2 and B2 |
| [C Patterns](../fieldguide/appendix-patterns.html) | Named patterns and where they live in the builds — design-doc sections, Capstone A3 |
| [D Decisions](../fieldguide/appendix-decisions.html) | Both builds' decision logs with the chapters that discuss each — Defend reps and "who decided" |
| [E Reading map](../fieldguide/appendix-reading.html) | The depth source behind every chapter. An external book or paper earns time only through a rep (R7); `resources/REGISTRY.md` keeps the verdicts |
| [F Card bank](../fieldguide/appendix-cards.html) | All card candidates by chapter. Copy one into `cards/REVIEW.md` only after you defended it at ≥ B (R4) |
| [G Findings and errata](../fieldguide/appendix-findings.html) | What the book found wrong or stale in the builds and in this learning system, with status |
| [H Living register](../fieldguide/appendix-register.html) | What each chapter waits for. The weekly sync lists triggers that fired; the Orchestrator revises and republishes |
| [I Service map](../fieldguide/appendix-service-map.html) | The same capability across Google Cloud, AWS, Microsoft and others — GF-4 (R45) and SD-14 (R41) |

## Keeping the book current (L-25)

- **Weekly sync:** names any Appendix H trigger that fired that week, and any chapter whose cited module changed. It never edits the book.
- **Orchestrator check-in:** revises the named chapter in `fieldguide/`, runs `python build.py` (and `python tools/make_pdf.py` for the PDF), republishes to the same link, and records the change in Appendix G or H.
- **Quarterly:** re-verify the Appendix H.4 fact families (platform services, regulation dates) before any external use.

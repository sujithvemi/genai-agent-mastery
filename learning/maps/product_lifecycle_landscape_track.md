# Product-Lifecycle Tool Landscape Track

**Added:** 2026-10-18 · **Requested by:** the portfolio strategy thread (S-21 handoff) · **Budget:** the learning/misc reserve (S-14: 15–20%, never below 10%), outside the 3 OWN : 2 SYSTEMS : 1 MODEL cycle.
**Why:** before building pm-agent's next releases, know what the tools in each corner of its market map do, so pm-agent integrates the strong ones instead of out-drafting them.
**Matrix (source of truth, dated, cited):** `Governance Local/_portfolio-strategy/inbox/landscape_matrix_2026-10-18.md`. Read its "Strategy-relevant" table first.

## Rules
- **Glance first:** about 15–20 minutes per tool, grouped into one rep per category (40–60 min). You read the matrix row, open the tool's own page, and fill the per-tool card below.
- **Deep dive only** for tools with an **integrate** or **compete** verdict that matter to the next pm-agent release (list below).
- **Date every fact.** These tools change monthly; a card without an "as of" date is not done.
- **Learning output only.** Nothing here changes the pm-agent or reference-build repos; findings go to the strategy inbox.

## Per-tool card (copy into `frameworks/landscape/<category>.md`)
| Field | Your note |
|---|---|
| Category | |
| Jobs it does | |
| Inputs → outputs | |
| Integration surface (MCP / API / ACP / none) | |
| Approval / audit model | |
| Pricing / licence | |
| Verdict for pm-agent: integrate / complement / compete / ignore — and one line why | |
| As of (date) + source | |

## Glance reps (one per category)
| Rep | Category | Tools | Time |
|---|---|---|---|
| **LL1** | In-tool PM agents | Atlassian Rovo agents + Rovo MCP, Linear Agent, Notion Custom Agents; skim Asana, monday, ClickUp | 45 m |
| LL2 | Upstream product tools | Productboard Spark (+ its MCP), ChatPRD (+ its MCP); skim Jira Product Discovery | 40 m |
| LL3 | Spec-driven development | GitHub Spec Kit, Kiro specs, OpenSpec, BMAD, Task Master, Tessl, SpecStory | 60 m |
| LL4 | Coding agents as executors | Claude Code (headless / SDK), Codex CLI + SDK, Copilot coding agent + CLI, `opencode serve`, Antigravity CLI | 45 m |
| LL5 | Agent protocols | MCP vs ACP (Agent Client Protocol) vs A2A; the "ACP" name clash | 40 m |
| LL6 | Decision models | Jev (TypeSafe System One) vs LLM structured output | 30 m |
| LL7 | UX / design lifecycle | Figma MCP (read + write to canvas), Code Connect, Figma Make, Penpot | 40 m |
| LL8 | Traceability & drift prior art | sphinx-needs + Pharaoh/ubTrace, StrictDoc, OpenFastTrace/Doorstop, Jama (skim) | 40 m |
| LL9 | Release, review, delivery insight | release-please/Changesets, AI PR reviewers, Atlassian DX / Swarmia | 30 m |
| LL10 | Open-source agent harnesses | Read the harness anatomy paper (arXiv 2609.00006, 11 systems, 7 subsystems); then DeepSeek Harness, OpenHands, Goose, opencode, Cline, Hermes; glance Omnigent (meta-harness) | 50 m |

## Deep dives (integrate / compete verdicts only; each 60–90 min, hands-on where possible)
| Rep | Topic | What you do |
|---|---|---|
| LL-D1 | **ACP as the executor contract** | Drive one ACP agent (Goose or OpenHands, both ACP-native and open source) from a small script; handle `session/request_permission`; map it to pm-agent's approval gate. Then hit `opencode serve`'s `/doc` and permission endpoint as the hosted fallback. |
| LL-D2 | **Spec formats pm-agent should emit** | `specify init` (Spec Kit) and `openspec init` in a scratch repo; write one requirement through both; decide what pm-agent should emit or consume. |
| LL-D3 | **Atlassian's direction** | Rovo MCP hands-on (read + one write with your Jira testers' site); track the planned Jira agent features from the 6 Oct 2026 announcement. |
| LL-D4 | **Productboard Spark MCP** | Only if a trial is available: read a spec from a coding agent; note how spec IDs could map to pm-agent requirement IDs. |
| LL-D5 | **Traceability prior art** | sphinx-needs' need/link model vs the pm-agent ledger's artefact kinds and link checks; what to borrow. |

## Done means
Each glance rep leaves one category file in `frameworks/landscape/` with a card per tool, and one line per finding that would change the thesis appended to the strategy inbox (`_portfolio-strategy/inbox/`), headed "strategy-relevant".

# pm-agent at scale — production architecture (living design doc)

**Owner:** Sujith (written by hand, one section per SYS rep). **Started:** 2026-10-14.
**Purpose:** apply every system-design concept to a system you know. This is a learning scenario, not a client commitment.
**📖 Read:** each section names its field guide chapter. The chapter explains; this doc is where *you* decide. Write your section first, then compare with any worked example in the chapter — never copy it.

## 0. Scenario (assumed — change it if you want a harder one)
- Internal multi-tenant planning assistant: ~5,000 users across ~20 teams (tenants), Jira as the system of record.
- Peak ~50 concurrent planning runs; a run takes 20 s–2 min and makes 5–30 model/tool calls.
- Writes to Jira require a distinct human approver (SoD) and a signed grant.
- Targets (assumed): p95 time-to-first-progress-event < 3 s; run success ≥ 95%; cost per run tracked and capped per tenant.
- Hosting: GCP. Today it runs as a local FastAPI app with fakes and a Postgres-seam checkpointer.

## 1. Request path & edge — SD-01
_📖 Ch25 §25.1, §25.7–25.10 · write after R05_

## 2. API design — SD-02
_📖 Ch25 §25.2–25.6 · R05_
## 3. Communication patterns — SD-03
_📖 Ch26 · R11_
## 4. AuthN / AuthZ — SD-04
_📖 Ch27, Ch18 · R06_
## 5. State & horizontal scale — SD-05
_📖 Ch28 §28.1–28.5, Ch37 · R12_
## 6. Data layer — SD-06
_📖 Ch28 §28.6–28.9, Ch21 · R23_
## 7. Reliability — SD-07
_📖 Ch29 · R18_
## 8. Deployment & DevOps — SD-08
_📖 Ch30, Ch38 §38.5–38.7 · R19_
## 9. Observability & AgentOps — SD-09
_📖 Ch31, Ch23 · R22_
## 10. Security & multi-tenancy — SD-10
_📖 Ch32, Ch21 · R23_
## 11. Capacity & cost — SD-11
_📖 Ch33 §33.1–33.6, Ch10 §10.8 · R38_
## 12. Multi-region & DR — SD-12
_📖 Ch33 §33.7–33.8, Ch21 §21.6 · R39_

## 13. Agent lifecycle, versioning & release — SD-13
_📖 Ch34, Ch38 · R40_
## 14. Runtime & managed agent platforms — SD-14
_📖 Ch37, Ch41–43, App. I · R41 (Ch37 §37.8 hosts pm-agent — open it only after you've written this section)_
## 15. Evaluate, simulate & optimise — SD-15
_📖 Ch39, Ch23 · R42_
## 16. Maintenance & evolution — SD-16
_📖 Ch40, Ch15 §15.8 · R43_

## Decisions log (one line each, with the alternative you rejected)
| # | Decision | Rejected alternative | Why |
|---|---|---|---|

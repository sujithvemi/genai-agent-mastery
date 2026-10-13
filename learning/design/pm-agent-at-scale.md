# pm-agent at scale — production architecture (living design doc)

**Owner:** Sujith (written by hand, one section per SYS rep). **Started:** 2026-10-14.
**Purpose:** apply every system-design concept to a system you know. This is a learning scenario, not a client commitment.

## 0. Scenario (assumed — change it if you want a harder one)
- Internal multi-tenant planning assistant: ~5,000 users across ~20 teams (tenants), Jira as the system of record.
- Peak ~50 concurrent planning runs; a run takes 20 s–2 min and makes 5–30 model/tool calls.
- Writes to Jira require a distinct human approver (SoD) and a signed grant.
- Targets (assumed): p95 time-to-first-progress-event < 3 s; run success ≥ 95%; cost per run tracked and capped per tenant.
- Hosting: GCP. Today it runs as a local FastAPI app with fakes and a Postgres-seam checkpointer.

## 1. Request path & edge — SD-01
_(write after R05)_

## 2. API design — SD-02
## 3. Communication patterns — SD-03
## 4. AuthN / AuthZ — SD-04
## 5. State & horizontal scale — SD-05
## 6. Data layer — SD-06
## 7. Reliability — SD-07
## 8. Deployment & DevOps — SD-08
## 9. Observability & AgentOps — SD-09
## 10. Security & multi-tenancy — SD-10
## 11. Capacity & cost — SD-11
## 12. Multi-region & DR — SD-12

## Decisions log (one line each, with the alternative you rejected)
| # | Decision | Rejected alternative | Why |
|---|---|---|---|

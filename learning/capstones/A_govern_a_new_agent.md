# Capstone A — govern a brand-new agent, by hand

**Level:** GF-L2 Apply. **Where:** this repo (`genai-agent-mastery`), new folder `agents/<your_agent>/` + `governance/`. **Rule:** you write the code and the governance artefacts. Claude is the coach and reviewer, never the author. Reuse ARB's *catalog and ideas*; do not copy its code.

**Why:** the builds prove Claude Code can govern an agent. This proves **you** can, on an agent the framework has never seen. It is also the M1 CI/CD Rebuild's natural home.

**📖 Field guide:** [Ch52 Capstone A](../fieldguide/capstone-a.html) is the stage-by-stage guide, with a self-grading rubric (§52.9) and where people get stuck (§52.10). Appendix B (control catalog) for A2, Appendix C (patterns) for A3. The chapter explains each stage; the code and artefacts stay yours.

## Pick the agent (decide in stage A0; suggestions)
- An **expense pre-approval agent**: reads a claim, checks policy, and can *submit* (a governed write) — close to your T&E bot experience.
- A **meeting-notes → Jira tickets agent**: reads notes, proposes tickets, creates them only with approval.
Pick one with **one real write**; that write is the whole governance story.

## Stages (each 1–3 reps; one stage per month is fine)

| Stage | What you do | Uses | Done when |
|---|---|---|---|
| A0 | Agent card: purpose, users, tools, data classes, the one write, autonomy level | ARB `governance/` manifests as a model · 📖 Ch52 §52.2, Ch34 §34.3 | Card written |
| A1 | Ungoverned agent on ADK (your hello_agent grows up) with 2 read tools + 1 write, local model or Vertex | GAM `agents/` · 📖 Ch52 §52.3 | It runs; you list 5 ways it can do harm |
| A2 | Tier it with ARB's catalog semantics (`min_tier` + `applies_when`); list the controls it pulls and why | R04 knowledge · 📖 Ch52 §52.4, Ch13, Ch14, App. B | Tier + control list defended |
| A3 | Hand-write the PEP (chokepoint), deny-by-default policy in Rego for 3 controls, hash-chained evidence | R09 policy, R10 rebuild · 📖 Ch52 §52.5, Ch16, Ch17, Ch22 | The write is blocked without approval; evidence verifies |
| A4 | Express the same controls as **AGT** policies where AGT can; run both engines on the same cases; record parity and gaps | R25 (AGT) · 📖 Ch52 §52.6, Ch47 §47.9 | A two-engine parity table for *your* agent |
| A5 | Gate + CI: a promotion gate that reads control status; GitHub Actions with WIF (this is the M1 Rebuild) | R19, M1 · 📖 Ch52 §52.7, Ch15, Ch30 | PR shows plan + gate result; merge deploys |
| A6 | Red-team 5 attacks (injection, confused deputy, over-limit, missing approval, evidence tamper) and write the defence note | ARB red-team corpus · 📖 Ch52 §52.8, Ch24, Ch20 | Signed-off note: what is blocked, what is a residual |

**Output:** a governed agent you built and can demo, plus `governance/DEFENCE.md` — the 2-page answer to "walk me through how this agent is governed".

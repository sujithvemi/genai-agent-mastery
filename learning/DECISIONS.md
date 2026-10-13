# Learning OS — decision log

| ID | Date | Decision | Why |
|---|---|---|---|
| L-01 | 2026-10-13 | Curriculum = own builds (OWN 70 / GROUND 25 / PROVE monthly) | 0 of 12 ledger phases defended while ~45k lines shipped; comprehension debt is the bottleneck, not material |
| L-02 | 2026-10-13 | No build throttle | Pro weekly limits are use-it-or-lose-it; builds run at token cadence; comprehension captured async (R6) |
| L-03 | 2026-10-13 | PROVE = monthly drill; revisit early 2027 | Job switch ≥ 9 months out |
| L-04 | 2026-10-13 | GCP: trace E4 (OWN); M1 WIF CI/CD becomes a hand-written Rebuild in GAM | E4 was built autonomously for GTM; M1's objectives (WIF, plan/apply, trust boundaries) are not in E4 |
| L-05 | 2026-10-13 | Source of truth = this `learning/` folder (git); Notion frozen read-only; Excel/HTML retired | One place; no plan-limited queries; diffable; Claude-native |
| L-06 | 2026-10-13 | Capacity model: irregular weekends + irregular weekdays → no streaks, no daily targets; fixed re-entry rule | Design for bursts |
| L-07 | 2026-10-13 | Cards only from defended material; nudge mixes 1 due card + 1 preview question from the next rep | Retrieval practice + pre-testing; keeps variety without random quizzing on unseen topics |
| L-08 | 2026-10-13 | Resource intake closed; every saved resource has one verdict (REGISTRY) | 2,550 saved videos + ~55 unread newsletters were a guilt store |
| L-09 | 2026-10-13 | Keep genai-agent-mastery as the learning repo (not a fresh one) | It holds the only code you wrote by hand (M0); scaffolding is good; add `learning/`. Known debt: CRLF noise on all files, M0 Terraform (SAs/WIF/budget) not committed |
| L-10 | 2026-10-13 | ~~Structure frozen until 2026-12-13~~ → superseded by L-11 | Stop setup/re-setup cycles |
| L-11 | 2026-10-14 | Weekly re-sync while ARB (E-phases) and PM (P5+) are actively built: automated Sunday sync + 15-min check-in; lanes/rules/layout stay fixed | The builds drive the learning; two weeks of progress can make reps and maps stale |
| L-12 | 2026-10-14 | New SYSTEMS lane (2 of every 6 reps), SD-01…SD-12, applied in a hand-written design doc for pm-agent | An agent that can't be served, secured, scaled, deployed and operated isn't valuable; agent-only coverage was too narrow |
| L-13 | 2026-10-14 | Rep cycle = 3 OWN : 2 SYSTEMS : 1 MODEL; PROVE monthly | Replaces 3 OWN : 1 GROUND |
| L-14 | 2026-10-14 | Cloud nudge (push notification) Tue/Thu/Sat/Sun; device nudge Wed only | Nudge must arrive with the laptop off; avoid duplicate Saturday nudges. Telegram not reachable from the cloud runtime (network allowlist) — push used instead |

# Orchestrator check-in — weekly (15 min) or whenever you return after a gap

Use in the "Learning Orchestrator" thread of the Governance project (or a new chat there):

```
Learning Orchestrator check-in. Read genai-agent-mastery/learning/: README.md, DECISIONS.md, NEXT.md, LOG.md (since last check-in),
cards/REVIEW.md, maps/comprehension_map.md, maps/system_design_track.md, maps/fieldguide_map.md, design/pm-agent-at-scale.md, the latest sync/SYNC_*.md,
and the newest Radar_*.md in Governance/_Agentic_Governance_Mastery/research/briefings/. Then, in ≤ 15 lines:
1. What happened since the last check-in (reps, grades, cards passed/failed).
2. Refill: keep exactly 3 Ready reps (generate their files from real code, each with a 📖 Read line from NEXT.md's 📖 column), honouring the 3 OWN : 2 SYSTEMS : 1 MODEL cycle and the monthly PROVE.
   If I've been building something specific this week, pull reps tagged to it to the top (rule R2).
3. Radar: promote at most 1 radar item into the backlog, only if it touches my builds or a 🟥 gap; else ignore it.
4. Field guide upkeep: if the latest sync names an Appendix H trigger that fired, or a chapter whose cited module changed,
   revise that chapter in learning/fieldguide/ (the code wins; date the fact), run `python build.py` (and `python tools/make_pdf.py`),
   republish to the same link (https://claude.ai/artifact/A18JhEfBV1x2tEKkXBeFmg) and record it in Appendix G or H. One chapter per
   check-in unless I ask for more.
5. Capability gap register (maps/capability_gap_register.md): check its gate (Defended chapters in maps/fieldguide_map.md ≥ 40, or R01–R48 all Done,
   or I said "open the capability register"; or one item marked `pulled`). If open or pulled: for the next P1 item, first refresh the prior work it
   depends on (Governance/repos/project_repos_reference, P-1…P-5 — dates, market changes; re-derive picks generically, keep the learning repo synthetic, L-27),
   then write its field guide edition-2 material, rebuild, republish, and set the item to `book` so the weekly sync can promote it. One item per check-in.
6. Anything in the system that is not working — propose one change max. Lanes, rules and layout are fixed (L-11); content is re-synced weekly while the builds are active.
Do the file edits yourself; give me the commit command as one Windows PowerShell line (`;` between commands, never `&&`; L-28).
```

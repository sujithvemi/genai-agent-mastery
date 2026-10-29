# Architect's Field Guide — source

A personal, book-length technical field guide for the principal architect of governed agent systems, from agent development to deployment, scale, operations, maintenance, versioning, governance and audit, built from the two builds (aicoe-reference-build, pm-agent) plus papers, books and current platform documentation across Google Cloud, AWS, Microsoft and independent tools.
Published artifact: https://claude.ai/artifact/A18JhEfBV1x2tEKkXBeFmg (private).

## Files
- `manifest.json` — the single source of parts and chapters (order, slug, title, synopsis, meta). Chapter numbers come from order; appendices keep their letters.
- `build.py` — run `python build.py` here after any edit. It numbers chapters, sections and figures; resolves `xref`/`sref` links and reading-path numbers;
  rebuilds pagers, the contents and the reading paths in `index.html`; and assembles four appendices from the chapters themselves:
  - Appendix E (reading map) from every chapter's *Further reading* list,
  - Appendix F (card bank) from every chapter's *Card candidates*,
  - Appendix H (living register) from every *Waiting on the builds* panel,
  - Appendix I (service map), foundation half, from every *Managed services across clouds* table.
  It exits non-zero on a broken cross-reference.
- `tools/` — generators for the appendices that read the build repositories directly:
  `gen_catalog.py` (Appendix B, from both builds' `governance/catalog/`), `gen_decisions.py` (Appendix D, from both `DECISIONS.md` files,
  with the chapters that discuss each decision), and `figs.py` (the SVG and page helpers they share). Set `ARB` and `PM` to the repo paths, then run `python build.py`.
- `tools/make_pdf.py` — the PDF edition (`field-guide.pdf`): one document in book order, light theme, bookmarks, internal links. Run after `build.py`.
- `index.html` — cover, preface, how to read, reading paths, the book on one page, contents, the reading shelf, about this edition.
- `book.css` — shared styles (dark-first, full light theme). Diagrams are inline SVG inside each chapter, editable in place.
- `<slug>.html` — one file per chapter or appendix (G = findings and errata, H = living register, I = service map).
- `ch12-risk-tiering.html`, `ch15-governed-action.html` — redirect stubs from the first scaffold; safe to delete.

## Chapter template
Predict first → numbered sections tagged Generic / Your build / Assumption / Verify → figures → tables →
Managed services across clouds (system and lifecycle chapters) → failure modes → In the room (client translation) →
Check before quoting → Waiting on the builds (register) → Prove it (defend questions, rep, card candidates) → Further reading.
Build facts are dated; platform facts carry a *Facts as of* date in the chapter header. Re-check a chapter when the modules or services it cites change.

## Status
All 55 chapters and appendices A–I are written (see the contents in `index.html`). Appendix H lists what each chapter is waiting for;
Appendix G lists findings in the builds and the learning system.
Edit here, run the build, then ask the Learning Orchestrator to republish to the same URL.

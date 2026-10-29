"""Field-guide build: one manifest drives numbering, cross-references, pagers and the contents.

Run from the fieldguide folder:  python build.py
- rewrites, in every chapter file that exists: <title>, the part label in the top bar,
  the chapter number line, the in-page TOC heading, the pager, and every
  <a class="xref" data-ch="slug" [data-sec="#id"] [data-style="title"]>…</a>;
- regenerates the contents block in index.html between the CONTENTS markers;
- reports broken cross-references and missing section anchors.
Idempotent: running it twice changes nothing.
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
M = json.loads((HERE / "manifest.json").read_text(encoding="utf-8"))
PARTS = {p["id"]: p for p in M["parts"]}
CH = M["chapters"]
# chapters are numbered by their order in the manifest; appendices keep their letters
_k = 0
for _c in CH:
    if _c["part"] != "pa":
        _k += 1
        _c["n"] = str(_k)
BY_SLUG = {c["slug"]: c for c in CH}


def label(c: dict) -> str:
    return f"Appendix {c['n']}" if c["part"] == "pa" else f"Chapter {c['n']}"


def exists(c: dict) -> bool:
    return (HERE / f"{c['slug']}.html").exists()


def href(c: dict, sec: str = "") -> str:
    return f"{c['slug']}.html{sec}" if exists(c) else f"index.html#c-{c['slug']}"


problems: list[str] = []
future: list[tuple[dict, str, str]] = []


def fix_xrefs(text: str, src: str) -> str:
    def rep(m: re.Match[str]) -> str:
        attrs = m.group(1)
        slug = re.search(r'data-ch="([^"]+)"', attrs)
        if not slug:
            problems.append(f"{src}: xref without data-ch")
            return m.group(0)
        c = BY_SLUG.get(slug.group(1))
        if c is None:
            problems.append(f"{src}: unknown xref slug {slug.group(1)}")
            return m.group(0)
        sec_m = re.search(r'data-sec="([^"]*)"', attrs)
        sec = sec_m.group(1) if sec_m else ""
        style = re.search(r'data-style="([^"]+)"', attrs)
        txt = label(c)
        if style and style.group(1) == "title":
            txt = f"{label(c)}, {html.escape(c['title'])}"
        keep = re.sub(r'\s*href="[^"]*"', "", attrs)
        if sec and exists(c):
            target = (HERE / f"{c['slug']}.html").read_text(encoding="utf-8")
            if f'id="{sec.lstrip("#")}"' not in target:
                problems.append(f"{src}: anchor {sec} missing in {c['slug']}")
        return f'<a{keep} href="{href(c, sec)}">{txt}</a>'

    return re.sub(r'<a((?:\s+[^>]*?)?\sclass="xref"[^>]*)>.*?</a>', rep, text, flags=re.S)


def render_paths(text: str, src: str) -> str:
    """<span class="seq" data-path="slug → slug , then slug … slug">…</span> → chapter numbers."""
    def rep(m: re.Match[str]) -> str:
        toks = m.group(2).split()
        out: list[str] = []
        for tok in toks:
            if tok in BY_SLUG:
                out.append(BY_SLUG[tok]["n"])
            elif re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)+", tok):
                problems.append(f"{src}: unknown slug {tok} in a reading path")
                out.append(tok)
            elif tok == "," and out:
                out[-1] += ","
            else:
                out.append(tok)
        return f'<span class="seq"{m.group(1)}>{" ".join(out)}</span>'
    return re.sub(r'<span class="seq"(\s+data-path="([^"]+)")>.*?</span>', rep, text, flags=re.S)


def pager(i: int) -> str:
    prev_c = CH[i - 1] if i > 0 else None
    next_c = CH[i + 1] if i + 1 < len(CH) else None
    parts = ['<nav class="pager" aria-label="Chapters">']
    if prev_c:
        parts.append(f'  <a href="{href(prev_c)}"><small>Previous</small>{prev_c["n"]} · {html.escape(prev_c["title"])}</a>')
    else:
        parts.append('  <a href="index.html"><small>Previous</small>Front matter</a>')
    parts.append('  <a href="index.html#contents"><small>Contents</small>All chapters</a>')
    if next_c:
        parts.append(f'  <a href="{href(next_c)}"><small>Next</small>{next_c["n"]} · {html.escape(next_c["title"])}</a>')
    parts.append("</nav>")
    return "\n".join(parts)


for i, c in enumerate(CH):
    f = HERE / f"{c['slug']}.html"
    if not f.exists():
        continue
    t = f.read_text(encoding="utf-8")
    p = PARTS[c["part"]]
    part_txt = f"Part {p['roman']} · {p['name']}" if p["roman"] else p["name"]
    num_txt = (f"PART {p['roman']} · CHAPTER {c['n']}" if p["roman"] else f"APPENDIX {c['n']}")
    t = re.sub(r"<title>.*?</title>", f"<title>{c['n']} · {html.escape(c['title'])}</title>", t, count=1, flags=re.S)
    t = re.sub(r'<span class="muted part-label">.*?</span>', f'<span class="muted part-label">{html.escape(part_txt)}</span>', t, count=1)
    t = re.sub(r'<div class="num">.*?</div>', f'<div class="num">{num_txt}</div>', t, count=1)
    t = re.sub(r'<div class="t">.*?</div>', f'<div class="t">{label(c)}</div>', t, count=1)
    t = re.sub(r'<nav class="pager".*?</nav>', pager(i), t, count=1, flags=re.S)
    # number h2 sections and figures, then resolve in-page section refs
    secnums: dict[str, str] = {}
    k = 0
    def _h2(m: re.Match[str]) -> str:
        global_k = None
        nonlocal_holder[0] += 1
        num = f"{c['n']}.{nonlocal_holder[0]}"
        sid = re.search(r'id="([^"]+)"', m.group(1))
        if sid:
            secnums[sid.group(1)] = num
        return f'<h2{m.group(1)}><span class="n">{num}</span>'
    nonlocal_holder = [0]
    t = re.sub(r'<h2([^>]*)><span class="n">[^<]*</span>', _h2, t)
    fig = [0]
    def _fig(m: re.Match[str]) -> str:
        fig[0] += 1
        return f"<figcaption><b>Fig {c['n']}.{fig[0]}</b>"
    t = re.sub(r"<figcaption><b>Fig [^<]*</b>", _fig, t)
    def _sref(m: re.Match[str]) -> str:
        sid = m.group(1)
        if sid not in secnums:
            problems.append(f"{f.name}: sref to unknown section #{sid}")
            return m.group(0)
        return f'<a class="sref" href="#{sid}">{secnums[sid]}</a>'
    t = re.sub(r'<a class="sref" href="#([^"]+)">[^<]*</a>', _sref, t)
    t = fix_xrefs(t, f.name)
    for fm in re.finditer(r'<div class="panel p-future"([^>]*)>(.*?)</div>', t, flags=re.S):
        trig = re.search(r'data-trigger="([^"]+)"', fm.group(1))
        body = re.sub(r'<span class="k">.*?</span>', '', fm.group(2), flags=re.S)
        body = body.replace('href="#', f'href="{c["slug"]}.html#')
        future.append((c, trig.group(1) if trig else "", re.sub(r"\s+", " ", body).strip()))
    for a in re.findall(r'href="([a-z0-9-]+\.html)(#[^"]*)?"', t):
        name = a[0]
        if name != "index.html" and not (HERE / name).exists():
            problems.append(f"{f.name}: link to missing file {name}")
    f.write_text(t, encoding="utf-8")

# ---- index contents ----
idx = HERE / "index.html"
it = idx.read_text(encoding="utf-8")
out = []
done = sum(1 for c in CH if exists(c))
for p in M["parts"]:
    out.append(f'<div class="part" id="{p["id"]}">')
    out.append(f'  <span class="pi">{"PART " + p["roman"] if p["roman"] else "APPENDICES"}</span>')
    out.append(f'  <h3>{html.escape(p["name"])}</h3>')
    out.append(f'  <p class="pd">{html.escape(p["desc"])}</p>')
    for c in [c for c in CH if c["part"] == p["id"]]:
        title = html.escape(c["title"])
        ct = f'<a href="{c["slug"]}.html">{title}</a>' if exists(c) else title
        st = '<span class="st done">Ready</span>' if exists(c) else '<span class="st">Planned</span>'
        meta = f'<span class="cm">{html.escape(c["meta"])}</span>' if c.get("meta") else ""
        out.append(f'  <div class="chap" id="c-{c["slug"]}"><span class="cn">{c["n"]}</span><span class="ct">{ct}</span>{st}<span class="cs">{html.escape(c["syn"])}</span>{meta}</div>')
    out.append("</div>")
block = "\n".join(out)
it = re.sub(r"<!--CONTENTS:START-->.*?<!--CONTENTS:END-->", f"<!--CONTENTS:START-->\n{block}\n<!--CONTENTS:END-->", it, flags=re.S)
it = re.sub(r"<!--PROGRESS-->.*?<!--/PROGRESS-->", f"<!--PROGRESS-->{done} of {len(CH)}<!--/PROGRESS-->", it, flags=re.S)
it = fix_xrefs(it, "index.html")
it = render_paths(it, "index.html")
idx.write_text(it, encoding="utf-8")

# ---- living register: collect every "Waiting on the builds" panel ----
reg = HERE / "appendix-register.html"
if reg.exists():
    rt = reg.read_text(encoding="utf-8")
    rows = []
    for c, trig, body in future:
        rows.append(f'<tr><td><a href="{c["slug"]}.html">{label(c)}</a><br><span class="small muted">{html.escape(c["title"])}</span></td><td>{html.escape(trig)}</td><td>{body}</td></tr>')
    table = ('<div class="tw"><table><thead><tr><th>Where</th><th>Trigger</th><th>What changes</th></tr></thead><tbody>\n'
             + "\n".join(rows) + "\n</tbody></table></div>") if rows else "<p>No chapter items yet.</p>"
    rt = re.sub(r"<!--REGISTER:START-->.*?<!--REGISTER:END-->", f"<!--REGISTER:START-->\n{table}\n<!--REGISTER:END-->", rt, flags=re.S)
    reg.write_text(rt, encoding="utf-8")

# ---- service map: collect every chapter's "Managed services across clouds" table ----
smap = HERE / "appendix-service-map.html"
if smap.exists():
    groups = []
    for c in CH:
        if not exists(c) or c["slug"] == "appendix-service-map":
            continue
        t = (HERE / f'{c["slug"]}.html').read_text(encoding="utf-8")
        mm = re.search(r'<h2 id="services">.*?<tbody>(.*?)</tbody>', t, flags=re.S)
        if not mm:
            continue
        body = re.sub(r'href="#', f'href="{c["slug"]}.html#', mm.group(1)).strip()
        groups.append(f'<tr><td colspan="5"><b><a href="{c["slug"]}.html#services">{label(c)} · {html.escape(c["title"])}</a></b></td></tr>\n{body}')
    table = ('<div class="tw"><table><thead><tr><th>Concern</th><th>Google Cloud</th><th>AWS</th><th>Microsoft Azure</th><th>Independent and open source</th></tr></thead><tbody>\n'
             + "\n".join(groups) + "\n</tbody></table></div>")
    st = smap.read_text(encoding="utf-8")
    st = re.sub(r"<!--SERVICES:START-->.*?<!--SERVICES:END-->", lambda _: f"<!--SERVICES:START-->\n{table}\n<!--SERVICES:END-->", st, flags=re.S)
    smap.write_text(st, encoding="utf-8")

# ---- reading map (Appendix E) and card bank (Appendix F): collected from every chapter ----
def _chapter_text(c):
    return (HERE / f'{c["slug"]}.html').read_text(encoding="utf-8")

rd = HERE / "appendix-reading.html"
if rd.exists():
    out_r = []
    for p in M["parts"]:
        if not p["roman"]:
            continue
        block = []
        for c in [c for c in CH if c["part"] == p["id"] and exists(c)]:
            mm = re.search(r'<h2 id="deeper">.*?</h2>\s*(<ul>.*?</ul>)', _chapter_text(c), flags=re.S)
            if not mm:
                continue
            ul = re.sub(r'href="#', f'href="{c["slug"]}.html#', mm.group(1))
            block.append(f'<h4><a href="{c["slug"]}.html#deeper">{label(c)} · {html.escape(c["title"])}</a></h4>\n{ul}')
        if block:
            out_r.append(f'<h3>Part {p["roman"]} · {html.escape(p["name"])}</h3>\n' + "\n".join(block))
    st = rd.read_text(encoding="utf-8")
    st = re.sub(r"<!--READING:START-->.*?<!--READING:END-->", lambda _: "<!--READING:START-->\n" + "\n".join(out_r) + "\n<!--READING:END-->", st, flags=re.S)
    rd.write_text(st, encoding="utf-8")

cb = HERE / "appendix-cards.html"
if cb.exists():
    rows_c, total = [], 0
    for c in CH:
        if c["part"] == "pa" or not exists(c):
            continue
        mm = re.search(r'Card candidates:(.*?)</p>', _chapter_text(c), flags=re.S)
        if not mm:
            continue
        cards = re.findall(r'<em>(.*?)</em>', mm.group(1), flags=re.S)
        total += len(cards)
        items = "".join(f"<li>{x}</li>" for x in cards)
        rows_c.append(f'<tr><td><a href="{c["slug"]}.html#prove">{label(c)}</a><br><span class="small muted">{html.escape(c["title"])}</span></td><td><ul>{items}</ul></td></tr>')
    table = ('<div class="tw"><table><thead><tr><th>Chapter</th><th>Card candidates</th></tr></thead><tbody>\n'
             + "\n".join(rows_c) + "\n</tbody></table></div>")
    st = cb.read_text(encoding="utf-8")
    st = re.sub(r"<!--CARDS:START-->.*?<!--CARDS:END-->", lambda _: f"<!--CARDS:START-->\n<p class=\"small muted\">{total} candidates from {len(rows_c)} chapters.</p>\n{table}\n<!--CARDS:END-->", st, flags=re.S)
    cb.write_text(st, encoding="utf-8")

print(f"chapters ready: {done}/{len(CH)} · register items: {len(future)}")
for pr in problems:
    print("PROBLEM:", pr)
sys.exit(1 if any("unknown" in p or "missing in" in p for p in problems) else 0)

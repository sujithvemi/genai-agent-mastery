import os
"""SVG helpers for new chapters. Classes come from book.css."""
from html import escape

TC = {'box-ok': 'tx-ok', 'box-acc': 'tx-acc', 'box-no': 'tx-no'}


def defs(mid):
    return (f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" class="arrowhead"/></marker></defs>')


def box(cls, x, y, w, h, *lines, anchor='middle', first=None, rest='tx-s', fill_none=False):
    """A rect with up to four lines; the first line uses the box's title class."""
    tc = first or TC.get(cls, 'tx-b')
    st = ' style="fill:none"' if fill_none else ''
    out = [f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="6"{st}/>']
    lines = [l for l in lines if l]
    tx = x + w / 2 if anchor == 'middle' else x + 12
    if lines:
        top = y + h / 2 - (len(lines) - 1) * 9 + 4.5
        for k, l in enumerate(lines):
            out.append(f'<text class="{tc if k == 0 else rest}" x="{tx:g}" y="{top + k * 18:g}" text-anchor="{"middle" if anchor == "middle" else "start"}">{l}</text>')
    return out


def text(cls, x, y, s, anchor='start'):
    return [f'<text class="{cls}" x="{x:g}" y="{y:g}" text-anchor="{anchor}">{s}</text>']


def arrow(mid, x1, y1, x2, y2, cls='ln', dash=None):
    st = f' style="stroke-dasharray:{dash}"' if dash else ''
    return [f'<line class="{cls}" x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" marker-end="url(#{mid})"{st}/>']


def line(x1, y1, x2, y2, cls='ln', dash='3 4'):
    st = f' style="stroke-dasharray:{dash}"' if dash else ''
    return [f'<line class="{cls}" x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}"{st}/>']


def svg(w, h, label, parts):
    return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label, quote=True)}">\n' + '\n'.join(parts) + '\n</svg>'


def figure(svgtext, caption):
    return f'<figure>\n<div class="fx">\n{svgtext}\n</div>\n<figcaption><b>Fig x</b>{caption}</figcaption>\n</figure>'


HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=JetBrains+Mono:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,300..800;1,8..60,400&display=swap">
<link rel="stylesheet" href="book.css">
</head>
<body>
<header class="bar">
  <a class="brand" href="index.html">Architect's Field Guide</a>
  <a href="index.html#contents">Contents</a>
  <span class="sp"></span>
  <span class="muted part-label">x</span>
</header>

<div class="layout">
<nav class="toc" aria-label="In this chapter">
  <div class="t">x</div>
  <ol>
{toc}
  </ol>
</nav>

<main>
<div class="chead">
  <div class="num">x</div>
  <h1>{h1}</h1>
  <p class="lede">{lede}</p>
  <div class="meta">
{meta}
  </div>
</div>
'''

TAIL = '''
<nav class="pager" aria-label="Chapters">
  <a href="index.html#contents"><small>Contents</small>All chapters</a>
</nav>
</main>
</div>
</body>
</html>
'''

import re


def page(path, title, lede, meta, body):
    """Write a chapter: toc built from h2 ids in body; meta is a list of (label, value)."""
    toc = '\n'.join(f'    <li><a href="#{i}">{re.sub("<[^>]+>", "", t)}</a></li>'
                    for i, t in re.findall(r'<h2 id="([^"]+)"><span class="n">x</span>(.*?)</h2>', body))
    m = '\n'.join(f'    <div><b>{a}</b><span>{b}</span></div>' for a, b in meta)
    html = HEAD.format(title=escape(title), toc=toc, h1=title, lede=lede, meta=m) + body.strip() + '\n' + TAIL
    open(path, 'w', encoding='utf-8').write(html)
    print('wrote', path, len(html))


def chnum(slug, manifest=None):
    """Current chapter number for a slug, computed as build.py does."""
    import json
    if manifest is None:
        here = os.path.dirname(os.path.abspath(__file__))
        cands = [os.path.join(here, '..', 'manifest.json'), os.path.join(here, '..', 'fieldguide', 'manifest.json')]
        manifest = next(p for p in cands if os.path.exists(p))
    k = 0
    for c in json.load(open(manifest))['chapters']:
        if c['part'] != 'pa':
            k += 1
            if c['slug'] == slug:
                return str(k)
        elif c['slug'] == slug:
            return c['n']
    raise KeyError(slug)

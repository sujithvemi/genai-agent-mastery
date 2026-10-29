"""PDF edition: one document with the front matter, every chapter and every appendix in book order,
light theme and print styles, working internal links, and bookmarks from the headings.

Usage: python tools/make_pdf.py [BOOKDIR]   (needs Playwright with Chromium)
For the intended typography, install Archivo, Source Serif 4 and JetBrains Mono locally;
otherwise the browser falls back to system fonts.
"""
import json
import os
import re
import sys

from playwright.sync_api import sync_playwright

BOOK = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..'))
M = json.load(open(os.path.join(BOOK, 'manifest.json'), encoding='utf-8'))
order = ['index'] + [c['slug'] for c in M['chapters'] if os.path.exists(os.path.join(BOOK, c['slug'] + '.html'))]
known = set(order)


def localise(slug, s):
    """Prefix every id with the slug and point every link at the combined document."""
    s = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{slug}--{m.group(1)}"', s)
    s = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{slug}--{m.group(1)})', s)
    s = re.sub(r'href="#([^"]*)"', lambda m: f'href="#{slug}--{m.group(1) or "top"}"', s)

    def ext(m):
        target, frag = m.group(1), m.group(2)
        if target not in known:
            return m.group(0)
        return f'href="#{target}--{frag[1:] if frag else "top"}"'
    return re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"', ext, s)


parts, styles = [], []
for slug in order:
    t = open(os.path.join(BOOK, slug + '.html'), encoding='utf-8').read()
    if slug == 'index':
        styles += re.findall(r'<style>(.*?)</style>', t, flags=re.S)
        mb = re.search(r'<body[^>]*>(.*)</body>', t, flags=re.S)
        body = mb.group(1) if mb else t[t.rindex('</style>') + len('</style>'):]   # the page is a fragment
        body = re.sub(r'<header class="bar">.*?</header>', '', body, flags=re.S)
    else:
        body = re.search(r'<main>(.*)</main>', t, flags=re.S).group(1)
        body = re.sub(r'<nav class="pager".*?</nav>', '', body, flags=re.S)
    body = re.sub(r'<script.*?</script>', '', body, flags=re.S)
    parts.append(f'<section class="pdf-doc" id="{slug}--top">{localise(slug, body)}</section>')

doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Architect's Field Guide</title>
<link rel="stylesheet" href="book.css">
<style>{"".join(styles)}
.pdf-doc {{ break-before: page; }}
.pdf-doc:first-child {{ break-before: auto; }}
.pdf-doc .layout, .pdf-doc main {{ display: block; max-width: none; }}
</style></head><body>
{"".join(parts)}
</body></html>'''
src = os.path.join(BOOK, '_pdf_edition.html')
open(src, 'w', encoding='utf-8').write(doc)

FOOT = ('<div style="font-size:7pt;width:100%;padding:0 15mm;color:#888;font-family:Archivo,Arial,sans-serif;'
        'display:flex;justify-content:space-between"><span>Architect\'s Field Guide · edition 1 · October 2026</span>'
        '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')
dest = os.path.join(BOOK, 'field-guide.pdf')
try:
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        p = b.new_page(color_scheme='light')
        p.emulate_media(media='print', color_scheme='light')
        p.goto('file://' + src, timeout=180000)
        p.evaluate('document.fonts.ready')
        p.wait_for_timeout(500)
        p.pdf(path=dest, format='A4', print_background=True, display_header_footer=True, outline=True, tagged=True,
              header_template='<div></div>', footer_template=FOOT,
              margin={'top': '16mm', 'bottom': '18mm', 'left': '15mm', 'right': '15mm'})
        b.close()
finally:
    os.remove(src)
print('wrote', dest, os.path.getsize(dest) // 1024, 'KB')

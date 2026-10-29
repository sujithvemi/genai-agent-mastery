"""Appendix D, curated decisions plus a generated index. Usage: ARB=<repo> PM=<repo> python tools/gen_decisions.py [BOOKDIR]"""
import sys, os, re, json, glob, html, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from figs import page

BOOK = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ARB = os.environ.get('ARB', '/home/claude/aicoe-reference-build')
PM = os.environ.get('PM', '/home/claude/multi_agent_project_management_platform')
man = json.load(open(os.path.join(BOOK, 'manifest.json')))
chapters = [c for c in man['chapters'] if os.path.exists(os.path.join(BOOK, c['slug'] + '.html')) and c['slug'] not in ('appendix-decisions',)]
texts = {c['slug']: re.sub(r'<[^>]+>', ' ', open(os.path.join(BOOK, c['slug'] + '.html'), encoding='utf-8').read()) for c in chapters}

def where(dnum):
    pat = re.compile(rf'\bD{dnum}\b')
    hits = [c['slug'] for c in chapters if pat.search(texts[c['slug']]) and c['slug'] not in ('appendix-register',)]
    return ' '.join(f'<a class="xref" data-ch="{s}"></a>' for s in hits) or '—'

heads = []
for line in open(f'{ARB}/DECISIONS.md', encoding='utf-8'):
    m = re.match(r'^### (D[\d/]+) · (\d{4}-\d{2}-\d{2}) · (.*)$', line.strip())
    if m:
        heads.append(m.groups())
commit = subprocess.check_output(['git', '-C', ARB, 'log', '-1', '--format=%h', ], text=True).strip()
pmcommit = subprocess.check_output(['git', '-C', PM, 'log', '-1', '--format=%h'], text=True).strip()

rows = []
for did, date, title in heads:
    num = re.match(r'D(\d+)', did).group(1)
    t = html.escape(title)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    rows.append(f'<tr><td><b>{did}</b></td><td class="small">{date}</td><td>{t}</td><td class="small">{where(num)}</td></tr>')
full = ('<div class="tw"><table><thead><tr><th>Id</th><th>Date</th><th>Decision (ARB heading)</th><th>Discussed in</th></tr></thead><tbody>\n'
        + '\n'.join(rows) + '\n</tbody></table></div>')

pmrows = []
for line in open(f'{PM}/DECISIONS.md', encoding='utf-8'):
    m = re.match(r'^\| (D-PM-[0-9]+b?) \| ([^|]+) \| ([^|]+) \|', line)
    if m:
        a, b, c = (x.strip() for x in m.groups())
        c = html.escape(c.replace('**', ''))
        c = re.sub(r'`([^`]+)`', r'<code>\1</code>', c)
        pmrows.append(f'<tr><td><b>{a}</b></td><td>{html.escape(b)}</td><td>{c}</td></tr>')
pm = ('<div class="tw"><table><thead><tr><th>Id</th><th>Decision</th><th>Choice</th></tr></thead><tbody>\n' + '\n'.join(pmrows) + '\n</tbody></table></div>')

themes = [
 ('Framework design', [
   ('D14', 'Author the framework fleet-first: a control\'s minimum tier is intrinsic to the control, and <code>applies_when</code> decides scope, so no control is reverse-engineered from one agent.'),
   ('D16', 'The catalog is hand-authored YAML validated by JSON Schema; the rulebook is data before it is code.'),
   ('D39', 'Fleet-first holds at derivation; a second archetype that exposes a gap in bindings is the framework working, not failing.'),
   ('D40', 'A fleet is a graph and a message has no authority: cross-agent content is data, edges are declared, provenance travels with it.')]),
 ('Enforcement', [
   ('D17', 'Embed the policy engine and move money across the policy plane in minor units, never floats.'),
   ('D18', 'Fail-closed in Rego takes deliberate work: every fact read through <code>object.get</code> with a conservative default.'),
   ('D22', 'A second PDP is real only if scoped honestly; the gate believes checks, not tables.'),
   ('D23', 'Prefer provable-preventive controls over inferable-detective ones, and separate the derivable half of a control from the declared half.'),
   ('D33', 'Identity is a resolved subject: resolve, don\'t compare spellings.'),
   ('D36', 'A rule nothing can reach is worse than no rule: remove it, and make reachability a test.'),
   ('D52', 'A model-based classifier may sit on the enforcement path only if it is monotone-restrictive: it can refuse, never allow.'),
   ('D53', 'No framework version is held back by another\'s pins: other frameworks run as out-of-process hosts behind governed gateways.'),
   ('D63', 'At a network boundary the gateway owns issued-call, in-order and expiring semantics, stricter than in process; AGT not adopted, with a revisit trigger.')]),
 ('Evidence and observability', [
   ('D21', 'The evidence plane enforces its own controls, and tool results go in structured.'),
   ('D25', 'The open evidence log is an allowlist, not a redaction pass.'),
   ('D26', 'OpenTelemetry is the boundary; a tracing vendor attaches to a provider the build owns.'),
   ('D28', 'Be honest about what a fresh process can and cannot prove; a check that cannot fail is not built.'),
   ('D34', 'The head hash leaves the file: anchors live outside what they protect.')]),
 ('Gate, conformance and change', [
   ('D27', 'The conformance report is the gate\'s input, generated in the run and never authored.'),
   ('D56', 'Every crosswalk proof is checked by disabling what it proves.'),
   ('D59', 'A sign-off binds to a digest of the configuration it approved; the inventory is reconciled by resolved subject.'),
   ('D50', 'A superseded living claim is corrected; a dated record never is.')]),
 ('Human oversight', [
   ('D20', 'Approval and identity are signed tokens, bound to what they authorise.'),
   ('D35', 'The human layer gets friction by design: rate, cooling-off, batch caps, sampled second review, a legible payload.'),
   ('D43', 'Measure approval fatigue; never fake a control over human attention.')]),
 ('State, cost and reliability', [
   ('D42', 'Security-relevant control state is durable and shared, behind one seam.'),
   ('D58', 'Budgets are reserved inside the store\'s atomic transaction, so replicas cannot both spend the last of a budget.'),
   ('D71', 'Retry a turn only on throttling and only if no effect completed in that attempt.')]),
 ('Honesty and process', [
   ('D29', 'The red team\'s standard is falsification under a compromised-model assumption.'),
   ('D44', 'Verify crosswalk cells against primary sources; leave honest <code>[Verify]</code> where you cannot.'),
   ('D55', 'Coverage has three statuses and a partial qualifier; report four numbers, never one.'),
   ('D65', 'Hand over to go-to-market on maturity, not urgency.'),
   ('D74', 'Hold a control whose measurement cannot separate noise from the effect it targets.')]),
]
cur = []
for name, items in themes:
    cur.append(f'<h3>{name}</h3>')
    cur.append('<div class="tw"><table><thead><tr><th>Id</th><th>Principle</th><th>In the book</th></tr></thead><tbody>')
    for did, prin in items:
        cur.append(f'<tr><td><b>{did}</b></td><td>{prin}</td><td class="small">{where(did[1:])}</td></tr>')
    cur.append('</tbody></table></div>')
curated = '\n'.join(cur)

body = f'''
<h2 id="how"><span class="n">x</span>How to use this index</h2>
<p>Your reference build records every ruling as a numbered entry in <code>DECISIONS.md</code>: a verdict, the reasons, what was rejected and the test that makes it falsifiable. Some of those rulings are principles you should be able to state cold in an interview or a client meeting; the rest are the history behind them. This appendix gives the first set grouped by theme, then the whole index with the chapters that discuss each entry, found by searching the book. Headings are read from ARB <code>main</code> at <code>{commit}</code> and pm-agent at <code>{pmcommit}</code>.</p>

<h2 id="cold"><span class="n">x</span>Decisions to know cold</h2>
{curated}

<h2 id="arb"><span class="n">x</span>The full ARB index</h2>
<p>D15 and D66 have no heading of their own (D15 was never used; D66 sits inside the D65 section), which is finding F-04 in <a class="xref" data-ch="appendix-findings"></a>.</p>
{full}

<h2 id="pm"><span class="n">x</span>pm-agent's framing decisions</h2>
<p>pm-agent records decisions in phase tables (<code>D-PM-P0-a</code> and so on) and closing rulings; these are its framing decisions, in force for all its threads.</p>
{pm}

<div class="panel p-future" data-trigger="New D-entries in either build">
  <span class="k">Waiting on the builds</span>
  <p>Regenerate the index after each phase close; promote any new principle-level ruling into the "know cold" tables with a card.</p>
</div>
'''
page(os.path.join(BOOK, 'appendix-decisions.html'), 'Decision index',
     'The build decisions worth knowing cold, grouped by theme with their one-line principles, then every ARB decision heading with the chapters that discuss it, and pm-agent\'s framing decisions.',
     [('Source', 'ARB and pm-agent DECISIONS.md'), ('Generated', '2026-10-21')], body)

"""Appendix B, generated from the two builds' catalogs. Usage: ARB=<repo> PM=<repo> python tools/gen_catalog.py [BOOKDIR]"""
import sys, os, glob, yaml, html, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from figs import page

ARB = os.environ.get('ARB', '/home/claude/aicoe-reference-build')
PM = os.environ.get('PM', '/home/claude/multi_agent_project_management_platform')
if len(sys.argv) < 2:
    sys.argv.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
def commit(repo):
    return subprocess.check_output(['git', '-C', repo, 'log', '-1', '--format=%h · %cd', '--date=short'], text=True).strip()
def load(repo):
    out = []
    for f in sorted(glob.glob(f'{repo}/governance/catalog/*.yaml')):
        out.append(yaml.safe_load(open(f)))
    return out
def e(x):
    if x is None:
        return '—'
    if isinstance(x, list):
        return '; '.join(e(i) for i in x)
    if isinstance(x, dict):
        return '; '.join(f'{k}: {e(v)}' for k, v in x.items())
    s = html.escape(str(x))
    return s
def code(s):
    import re
    return re.sub(r'`([^`]+)`', r'<code>\1</code>', s)

arb = load(ARB); pm = load(PM)
def scope(c):
    t = c.get('min_tier') or '—'
    a = c.get('applies_when')
    return f'{e(t)}' + (f'<br><span class="small muted">{code(e(a))}</span>' if a else '')

cards = []
for c in arb:
    std = c.get('standards') or {}
    fields = [('Objective', code(e(c.get('objective')))), ('Trigger', code(e(c.get('trigger')))), ('Tier scope', scope(c)),
              ('Enforced at', e(c.get('enforcement_point'))), ('Owner', e(c.get('owner_role') or 'Platform (global invariant)')),
              ('Evidence', code(e(c.get('evidence')))), ('Test', code(e(c.get('test_method')))), ('Exception', code(e(c.get('exception_path')))),
              ('Status', e(c.get('status')))]
    dl = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in fields)
    cards.append(f'<div class="refcard" id="{c["id"].lower()}"><h4><span class="ctl">{e(c["id"])}</span> {e(c.get("title"))}</h4><dl>{dl}</dl></div>')
arb_table = '\n'.join(cards)
xrows = []
for c in arb:
    s = c.get('standards') or {}
    xrows.append(f'<tr><td><span class="ctl">{e(c["id"])}</span></td><td>{e(s.get("nist_ai_rmf"))}</td><td>{e(s.get("iso_42001"))}</td><td>{e(s.get("owasp"))}</td><td>{e(s.get("eu_ai_act"))}</td></tr>')
xw_table = ('<div class="tw"><table class="small"><thead><tr><th>Control</th><th>NIST AI RMF</th><th>ISO/IEC 42001</th><th>OWASP</th><th>EU AI Act</th></tr></thead><tbody>\n'
            + '\n'.join(xrows) + '\n</tbody></table></div>')

arb_ids = {c['id']: c.get('title') for c in arb}
prow = []
for c in pm:
    same = arb_ids.get(c['id'])
    clash = '' if not same else (f'<br><span class="small muted">ARB {e(c["id"])}: {e(same)}</span>' if same != c.get('title') else '<br><span class="small muted">same title in ARB</span>')
    prow.append(f'<tr><td><span class="ctl">PM-{e(c["id"])}</span>{clash}</td><td><b>{e(c.get("title"))}</b><br>{code(e(c.get("objective")))}</td><td>{e(c.get("min_tier"))}</td>'
                f'<td>{e(c.get("enforcement_point"))}</td><td>{e(c.get("owner_role") or "Platform (invariant)")}</td><td>{code(e(c.get("test_method")))}</td></tr>')
pm_table = ('<div class="tw"><table class="small"><thead><tr><th>Control</th><th>Title and objective</th><th>Min tier</th><th>Enforced at</th><th>Owner</th><th>Test</th></tr></thead><tbody>\n'
            + '\n'.join(prow) + '\n</tbody></table></div>')

n_ctl = sum(1 for c in arb if c['id'].startswith('CTL'))
n_gbl = sum(1 for c in arb if c['id'].startswith('GBL'))
body = f'''
<h2 id="how"><span class="n">x</span>How to read this</h2>
<p>Generated from the builds' catalog files, not retyped: ARB <code>governance/catalog/*.yaml</code> at <code>main</code> {commit(ARB)}, and pm-agent's at <code>main</code> {commit(PM)}. Each control states the six things every control must have: objective, trigger, owner, evidence, test method and exception path, plus its tier scope and enforcement point (<a class="xref" data-ch="control-as-contract"></a>). ARB's catalog holds {n_ctl} controls and {n_gbl} global invariants. A held control, <span class="ctl">CTL-0027</span> (counterfactual outcome consistency, the fairness gate), is built and bound in code with its threshold in <code>governance/policies/params.yaml</code>, but is held rather than ratified because the measured criterion could not separate noise from bias (D74).</p>
<p>The two builds' ids collide with different meanings (finding F-02 in <a class="xref" data-ch="appendix-findings"></a>). This appendix prefixes pm-agent's ids with <code>PM-</code> and shows ARB's title where the same number means something else.</p>

<h2 id="arb"><span class="n">x</span>ARB: the control catalog</h2>
{arb_table}

<h2 id="crosswalk"><span class="n">x</span>ARB: the standards crosswalk per control</h2>
<p>Cells as the catalog states them, including <code>[Verify]</code> and <code>[Verified date]</code> tags; the method is in <a class="xref" data-ch="standards-law-crosswalk" data-sec="#crosswalk"></a>.</p>
{xw_table}

<h2 id="pm"><span class="n">x</span>pm-agent: the forked catalog</h2>
<p>pm-agent forked ARB's catalog and evolved it for a read-only Jira planning domain with one governed write path (D-PM-1); operational fields were authored by its build thread pending owner review.</p>
{pm_table}

<div class="panel p-future" data-trigger="Either build ratifies, adds or renumbers a control">
  <span class="k">Waiting on the builds</span>
  <p>Regenerate this appendix whenever a catalog changes (the generator reads the YAML directly). If F-02 is resolved by namespacing ids in the builds, drop the <code>PM-</code> display prefix in favour of the builds' own.</p>
</div>
'''
page(os.path.join(sys.argv[1], 'appendix-control-catalog.html'), 'Control catalog reference',
     'Every control and invariant in the reference build, with its trigger, tier scope, enforcement point, owner, evidence, test and exception path, and its standards mapping; then pm-agent\'s forked catalog beside it. Generated from the catalog files.',
     [('Source', 'ARB and pm-agent governance/catalog/'), ('Generated', '2026-10-21')], body)

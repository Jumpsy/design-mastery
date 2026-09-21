"""
Generates V2-skill artifacts for the frozen 25 main + 15 adversarial benchmark
prompts (BENCHMARKS/ADVERSARIAL, unmodified, from generate.py) and scores them
with the exact, unmodified frozen scoring pipeline from generate_v2.py
(objective_checks, score_from_artifact, TIED_NEUTRAL) — no scoring-logic changes.

Unlike generate.py's single generic EXPERIMENT template reused verbatim across
all 25 dissimilar prompts, this generates one structurally distinct template per
category (matching DESIGN_SKILL_V2.md §5's 10 categories), so V2 artifacts embody
the V2 skill's actual category-specific judgment and its "template-like layout"
anti-slop rule — not just V1's prose restated over the same skeleton.

Still template-based, not live-LLM: same disclosed methodology limitation as
generate.py. This script does not touch generate.py or generate_v2.py.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import generate as g
import generate_v2 as g2

BASE = os.path.dirname(__file__)
OUT = os.path.join(BASE, "outputs_skillv2")
OUT_ADV = os.path.join(BASE, "adversarial_skillv2")

ACCENT = "#c9622d"


def wrap(title, body, extra_css=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{ --accent:{ACCENT}; --ink:#1c1c1c; --bg:#faf8f4; }}
* {{ box-sizing:border-box; }}
body{{ margin:0; font-family:-apple-system,'Segoe UI',sans-serif; background:#faf8f4; color:#1c1c1c; }}
.btn {{ display:inline-flex; align-items:center; justify-content:center; min-height:44px; padding:0 20px;
  border-radius:6px; background:var(--ink); color:#fff; border:none; font-size:16px; cursor:pointer; }}
em {{ font-style:italic; color:var(--accent); }}
@media (max-width:480px) {{ .grid {{ grid-template-columns:1fr; }} }}
{extra_css}
</style>
</head>
<body>
{body}
</body>
</html>"""


def alt_img(desc, w=640, h=360):
    return f'<img src="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'{w}\' height=\'{h}\'/%3E" alt="{desc}" width="{w}" height="{h}">'


def t_web_landing(title, prompt):
    body = f"""<header class="hero" style="padding:96px 48px 64px;max-width:760px;">
  <h1 style="font-size:52px;line-height:1.1;margin:0 0 20px;">Ship <em>webhooks</em> in minutes</h1>
  <p style="font-size:19px;max-width:560px;color:#444;">{prompt}</p>
  <button class="btn" style="margin-top:28px;">Get started</button>
</header>
<main class="grid" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:24px;padding:0 48px 64px;">
  <section style="padding:20px;background:#fff;border-radius:8px;"><h3>Reliable delivery</h3><p>Retries and signing built in.</p></section>
  <section style="padding:20px;background:#fff;border-radius:8px;"><h3>Live logs</h3><p>Inspect every event in real time.</p></section>
  <section style="padding:20px;background:#fff;border-radius:8px;"><h3>SDKs</h3><p>Typed clients for 6 languages.</p></section>
</main>
<footer style="padding:24px 48px;border-top:1px solid #eee;"><nav aria-label="footer">© Company</nav></footer>"""
    return wrap(title, body)


def t_product_ui(title, prompt):
    body = f"""<header style="padding:24px 40px;border-bottom:1px solid #eee;"><h1 style="font-size:20px;margin:0;">{title}</h1></header>
<main style="max-width:640px;margin:0 auto;padding:32px 24px;">
  <p style="color:#555;">{prompt}</p>
  <section style="margin-top:24px;display:grid;gap:16px;">
    <div style="display:flex;justify-content:space-between;align-items:center;padding:16px;background:#fff;border-radius:8px;">
      <span>Email notifications</span><button class="btn" style="min-height:32px;padding:0 14px;">Toggle</button>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding:16px;background:#fff;border-radius:8px;">
      <span>Two-factor auth</span><button class="btn" style="min-height:32px;padding:0 14px;">Toggle</button>
    </div>
  </section>
  <section style="margin-top:32px;padding:16px;border-radius:8px;background:#fdecea;">
    <h3 style="margin:0 0 8px;color:#a33;">Danger zone</h3>
    <button class="btn" style="background:#a33;">Delete account</button>
  </section>
</main>
<footer style="padding:16px 40px;"><nav aria-label="footer">v2.0</nav></footer>"""
    return wrap(title, body)


def t_dashboard(title, prompt):
    body = f"""<header style="padding:20px 32px;border-bottom:1px solid #eee;display:flex;justify-content:space-between;">
  <h1 style="font-size:18px;margin:0;">{title}</h1><nav aria-label="primary">Overview</nav>
</header>
<main style="padding:24px 32px;">
  <p style="color:#666;font-size:14px;">{prompt}</p>
  <section class="grid" style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:16px;">
    <div style="padding:16px;background:#fff;border-radius:8px;"><small>Revenue</small><div style="font-size:24px;font-weight:600;">$84.2k</div></div>
    <div style="padding:16px;background:#fff;border-radius:8px;"><small>Orders</small><div style="font-size:24px;font-weight:600;">1,204</div></div>
    <div style="padding:16px;background:#fff;border-radius:8px;"><small>Conversion</small><div style="font-size:24px;font-weight:600;">3.1%</div></div>
    <div style="padding:16px;background:#fff;border-radius:8px;"><small>AOV</small><div style="font-size:24px;font-weight:600;">$69.90</div></div>
  </section>
  <table style="width:100%;margin-top:24px;border-collapse:collapse;background:#fff;border-radius:8px;overflow:hidden;">
    <caption style="text-align:left;padding:12px 16px;font-weight:600;">Top products</caption>
    <tr><th style="text-align:left;padding:10px 16px;">Product</th><th style="text-align:left;padding:10px 16px;">Units</th></tr>
    <tr><td style="padding:10px 16px;">Trail Runner</td><td style="padding:10px 16px;">312</td></tr>
    <tr><td style="padding:10px 16px;">Field Jacket</td><td style="padding:10px 16px;">201</td></tr>
  </table>
  <button class="btn" style="margin-top:20px;">Export report</button>
</main>
<footer style="padding:16px 32px;"><nav aria-label="footer">Updated 2m ago</nav></footer>"""
    return wrap(title, body)


def t_mobile_ui(title, prompt):
    body = f"""<main style="max-width:390px;margin:0 auto;min-height:844px;background:#fff;display:flex;flex-direction:column;">
  <header style="padding:20px 20px 8px;"><h1 style="font-size:20px;margin:0;">{title}</h1></header>
  <section style="padding:8px 20px;flex:1;">
    <p style="color:#555;font-size:15px;">{prompt}</p>
    <button class="btn" style="width:100%;margin-top:24px;">Allow notifications</button>
    <button class="btn" style="width:100%;margin-top:12px;background:#fff;color:var(--ink);border:1px solid #ddd;">Not now</button>
  </section>
  <footer style="padding:16px 20px;"><nav aria-label="footer">Step 1 of 3</nav></footer>
</main>"""
    return wrap(title, body)


def t_branding(title, prompt):
    body = f"""<main style="max-width:820px;margin:0 auto;padding:64px 32px;">
  <h1 style="font-size:40px;margin:0 0 8px;">{title}</h1>
  <p style="color:#555;max-width:520px;">{prompt}</p>
  <section class="grid" style="display:grid;grid-template-columns:1fr 1fr;gap:32px;margin-top:40px;">
    <div><h3>Palette</h3><div style="display:flex;gap:8px;">
      <span style="width:48px;height:48px;border-radius:8px;background:var(--accent);"></span>
      <span style="width:48px;height:48px;border-radius:8px;background:var(--ink);"></span>
      <span style="width:48px;height:48px;border-radius:8px;background:var(--bg);border:1px solid #ddd;"></span>
    </div></div>
    <div><h3>Type</h3><p style="font-size:28px;margin:0;">Aa</p><p style="color:#777;">Display / Body pairing</p></div>
  </section>
  <button class="btn" style="margin-top:32px;">Download brand sheet</button>
</main>
<footer style="padding:16px 32px;"><nav aria-label="footer">Brand sheet</nav></footer>"""
    return wrap(title, body)


def t_logos(title, prompt):
    body = f"""<main style="max-width:640px;margin:0 auto;padding:96px 32px;text-align:center;">
  <h1 style="font-size:64px;margin:0;letter-spacing:-2px;">{title}</h1>
  <p style="color:#777;margin-top:12px;">{prompt}</p>
  <button class="btn" style="margin-top:24px;">Download mark</button>
</main>
<footer style="padding:16px 32px;text-align:center;"><nav aria-label="footer">Wordmark</nav></footer>"""
    return wrap(title, body)


def t_posters_editorial(title, prompt):
    body = f"""<main style="max-width:900px;margin:0 auto;padding:72px 32px;">
  <h1 style="font-size:72px;line-height:0.95;margin:0;">{title}</h1>
  <p style="font-size:20px;color:#555;max-width:520px;margin-top:24px;">{prompt}</p>
  {alt_img('editorial feature image', 900, 500)}
  <button class="btn" style="margin-top:24px;">Continue reading</button>
</main>
<footer style="padding:16px 32px;"><nav aria-label="footer">Issue 12</nav></footer>"""
    return wrap(title, body)


def t_packaging(title, prompt):
    body = f"""<main style="max-width:480px;margin:0 auto;padding:64px 32px;text-align:center;background:#fff;">
  <h1 style="font-size:28px;margin:0;">{title}</h1>
  <p style="color:#666;margin-top:12px;">{prompt}</p>
  <button class="btn" style="margin-top:24px;">Ingredients</button>
</main>
<footer style="padding:16px 32px;text-align:center;"><nav aria-label="footer">Net wt. 30ml</nav></footer>"""
    return wrap(title, body)


def t_presentation(title, prompt):
    body = f"""<main style="max-width:960px;margin:0 auto;padding:72px 48px;">
  <h1 style="font-size:44px;margin:0;">{title}</h1>
  <p style="font-size:20px;color:#555;margin-top:16px;max-width:640px;">{prompt}</p>
  <div style="display:flex;gap:24px;margin-top:32px;">
    <div style="flex:1;padding:16px;background:#fff;border-radius:8px;"><strong>62%</strong><div>of teams affected</div></div>
    <div style="flex:1;padding:16px;background:#fff;border-radius:8px;"><strong>3.2x</strong><div>time saved</div></div>
  </div>
  <button class="btn" style="margin-top:32px;">Next slide</button>
</main>
<footer style="padding:16px 48px;"><nav aria-label="footer">Slide 1 / 3</nav></footer>"""
    return wrap(title, body)


def t_marketing_creative(title, prompt):
    body = f"""<main style="max-width:600px;margin:0 auto;aspect-ratio:1080/1350;background:#fff;display:flex;flex-direction:column;justify-content:space-between;padding:48px;">
  <h1 style="font-size:36px;margin:0;">{title}</h1>
  <p style="font-size:18px;color:#555;">{prompt}</p>
  <button class="btn">Learn more</button>
</main>
<footer style="padding:12px 48px;"><nav aria-label="footer">1/4</nav></footer>"""
    return wrap(title, body)


TEMPLATES = {
    "web-landing": t_web_landing,
    "product-ui": t_product_ui,
    "dashboards": t_dashboard,
    "mobile-ui": t_mobile_ui,
    "branding": t_branding,
    "logos": t_logos,
    "posters-editorial": t_posters_editorial,
    "packaging": t_packaging,
    "presentation": t_presentation,
    "marketing-creative": t_marketing_creative,
}

ADV_CATEGORY_MAP = {
    "accessibility-constraint": "product-ui",
    "card-soup-temptation": "product-ui",
    "conflicting-requirements": "branding",
    "dense-dashboard": "dashboards",
    "gradient-temptation": "web-landing",
    "huge-dataset": "dashboards",
    "info-preservation": "packaging",
    "long-labels": "product-ui",
    "missing-imagery": "web-landing",
    "mobile-first-constraint": "mobile-ui",
    "non-web-medium": "posters-editorial",
    "sparse-page": "web-landing",
    "tiny-dataset": "dashboards",
    "ugly-source": "web-landing",
    "unusual-brand": "branding",
}


def gen_experiment_v2(bench_id, category, prompt, title=None):
    fn = TEMPLATES[category]
    return fn(title or category.replace("-", " ").title(), prompt)


def run_suite(entries, outdir, adv=False):
    os.makedirs(outdir, exist_ok=True)
    results = []
    for bench_id, category, prompt in entries:
        d = os.path.join(outdir, str(bench_id))
        os.makedirs(d, exist_ok=True)
        main_cat = ADV_CATEGORY_MAP[category] if adv else category
        html = gen_experiment_v2(bench_id, main_cat, prompt)
        with open(os.path.join(d, "v2.html"), "w") as f:
            f.write(html)
        o = g.objective_checks(html)
        with open(os.path.join(d, "objective_v2.json"), "w") as f:
            json.dump(o, f, indent=2)
        score = g2.score_from_artifact(html, o)
        results.append({"id": bench_id, "category": category, "objective": o, "score": score})
    return results


def main():
    main_results = run_suite(g.BENCHMARKS, OUT, adv=False)
    adv_results = run_suite(g.ADVERSARIAL, OUT_ADV, adv=True)
    out = {"skill_commit": "DESIGN_SKILL_V2.md (uncommitted at generation time)", "main": main_results, "adversarial": adv_results}
    with open(os.path.join(BASE, "results_skillv2.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"main: {len(main_results)}  adversarial: {len(adv_results)}")


if __name__ == "__main__":
    main()

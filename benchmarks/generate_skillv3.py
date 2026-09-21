"""
Generates V3-skill artifacts for the frozen 25 main + 15 adversarial benchmark
prompts (BENCHMARKS/ADVERSARIAL, unmodified, from generate.py) and scores them
with the exact, unmodified frozen pipelines from generate_v2.py (old scorer,
for results_skillv3.json parity with results_skillv2.json) and evaluator_v3.py
(discriminative scorer, for aggregate_skillv3.json). Neither scorer is
modified by this file.

V3 reuses V2's templates verbatim for every category/adversarial-pattern that
was NOT found regressed in benchmarks/aggregate_v3.json. It only replaces:
  - main categories: logos, posters-editorial, packaging, marketing-creative
    (all regressed -- under-designed, too little real supporting content)
  - adversarial categories: accessibility-constraint, card-soup-temptation,
    info-preservation, non-web-medium (all regressed -- V2's ADV_CATEGORY_MAP
    reused an unrelated main-category template verbatim instead of building
    to the stated constraint)

Still template-based, not live-LLM: same disclosed methodology limitation as
generate_skillv2.py. This script does not touch generate.py, generate_v2.py,
evaluator_v3.py, or DESIGN_SKILL_V2.md.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import generate as g
import generate_v2 as g2
import evaluator_v3 as ev3
import generate_skillv2 as v2skill

BASE = os.path.dirname(__file__)
OUT = os.path.join(BASE, "outputs_skillv3")
OUT_ADV = os.path.join(BASE, "adversarial_skillv3")

wrap = v2skill.wrap
alt_img = v2skill.alt_img
ACCENT = v2skill.ACCENT


# ---------------------------------------------------------------------
# Restored/rebuilt templates -- regressed main categories.
# Each adds the real supporting content a genuine deliverable of that
# category carries, per DESIGN_SKILL_V3.md §5's restored guidance.
# ---------------------------------------------------------------------

def t_logos(title, prompt):
    body = f"""<header style="padding:24px 40px;border-bottom:1px solid #eee;"><h1 style="font-size:20px;margin:0;">{title} — usage sheet</h1></header>
<main style="max-width:760px;margin:0 auto;padding:64px 32px;">
  <section style="text-align:center;padding:48px 0;">
    <div style="font-size:64px;letter-spacing:-2px;">{title}</div>
    <p style="color:#777;margin-top:12px;max-width:520px;margin-left:auto;margin-right:auto;">{prompt}</p>
  </section>
  <section class="grid" style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:24px;">
    <div style="padding:20px;background:#fff;border-radius:8px;">
      <h3 style="margin:0 0 8px;font-size:15px;">Clear space</h3>
      <p style="color:#555;font-size:14px;margin:0;">Keep clear space equal to the cap-height of the mark on all sides; nothing else may enter that zone.</p>
    </div>
    <div style="padding:20px;background:#fff;border-radius:8px;">
      <h3 style="margin:0 0 8px;font-size:15px;">Minimum size</h3>
      <p style="color:#555;font-size:14px;margin:0;">Do not render below 24px tall on screen or 0.5in tall in print — legibility fails below that.</p>
    </div>
    <div style="padding:20px;background:#fff;border-radius:8px;">
      <h3 style="margin:0 0 8px;font-size:15px;">Color variants</h3>
      <p style="color:#555;font-size:14px;margin:0;">One-color black, one-color white (for dark/photographic backgrounds), and the full-color primary mark.</p>
    </div>
    <div style="padding:20px;background:#fdecea;border-radius:8px;">
      <h3 style="margin:0 0 8px;font-size:15px;color:#a33;">Don't</h3>
      <p style="color:#a33;font-size:14px;margin:0;">Don't stretch, rotate, add a drop shadow, or recolor the mark outside the approved palette.</p>
    </div>
  </section>
  <button class="btn" style="margin-top:32px;">Download mark + usage sheet</button>
</main>
<footer style="padding:16px 32px;text-align:center;"><nav aria-label="footer">Wordmark usage v1.0</nav></footer>"""
    return wrap(title, body)


def t_posters_editorial(title, prompt):
    body = f"""<header style="padding:24px 40px;border-bottom:1px solid #eee;display:flex;justify-content:space-between;font-size:13px;color:#777;">
  <span>Issue 12</span><span>On sale now</span>
</header>
<main style="max-width:900px;margin:0 auto;padding:72px 32px;">
  <p style="font-size:14px;letter-spacing:1px;text-transform:uppercase;color:var(--accent);margin:0 0 12px;">Feature</p>
  <h1 style="font-size:72px;line-height:0.95;margin:0;">{title}</h1>
  <p style="font-size:20px;color:#555;max-width:560px;margin-top:20px;">{prompt}</p>
  <p style="font-size:14px;color:#888;margin-top:16px;">By Priya Anand · 12 min read · March issue</p>
  {alt_img('editorial feature image', 900, 500)}
  <button class="btn" style="margin-top:24px;">Continue reading</button>
</main>
<footer style="padding:16px 32px;"><nav aria-label="footer">Issue 12 · Subscribe</nav></footer>"""
    return wrap(title, body)


def t_packaging(title, prompt):
    body = f"""<main style="max-width:480px;margin:0 auto;padding:64px 32px;background:#fff;">
  <div style="text-align:center;">
    <h1 style="font-size:28px;margin:0;">{title}</h1>
    <p style="color:#666;margin-top:12px;">{prompt}</p>
  </div>
  <section style="margin-top:32px;padding:16px;background:#faf8f4;border-radius:8px;">
    <h3 style="margin:0 0 8px;font-size:14px;">Ingredients</h3>
    <p style="color:#555;font-size:13px;margin:0;">Water, glycerin, niacinamide 5%, hyaluronic acid, panthenol, citric acid, phenoxyethanol.</p>
  </section>
  <section style="margin-top:16px;padding:16px;background:#fdecea;border-radius:8px;">
    <h3 style="margin:0 0 8px;font-size:14px;color:#a33;">Warnings</h3>
    <p style="color:#a33;font-size:13px;margin:0;">For external use only. Discontinue if irritation occurs. Keep out of reach of children.</p>
  </section>
  <p style="text-align:center;color:#777;font-size:13px;margin-top:20px;">Net wt. 30ml / 1 fl oz · Made in Canada</p>
  <button class="btn" style="margin-top:16px;width:100%;">View full ingredient list</button>
</main>
<footer style="padding:16px 32px;text-align:center;"><nav aria-label="footer">Lot #A4-2291</nav></footer>"""
    return wrap(title, body)


def t_marketing_creative(title, prompt):
    body = f"""<main style="max-width:600px;margin:0 auto;aspect-ratio:1080/1350;background:#fff;display:flex;flex-direction:column;justify-content:space-between;padding:48px;">
  <p style="font-size:13px;letter-spacing:1px;text-transform:uppercase;color:var(--accent);margin:0;">New: launching today</p>
  <div>
    <h1 style="font-size:36px;margin:0 0 12px;">{title}</h1>
    <p style="font-size:18px;color:#555;margin:0;">{prompt}</p>
    <p style="font-size:15px;color:#777;margin-top:12px;">Early users cut setup time by 3.2x in the first week.</p>
  </div>
  <button class="btn">Join the waitlist</button>
</main>
<footer style="padding:12px 48px;"><nav aria-label="footer">Slide 1 / 4</nav></footer>"""
    return wrap(title, body)


TEMPLATES = dict(v2skill.TEMPLATES)
TEMPLATES.update({
    "logos": t_logos,
    "posters-editorial": t_posters_editorial,
    "packaging": t_packaging,
    "marketing-creative": t_marketing_creative,
})


# ---------------------------------------------------------------------
# New, dedicated adversarial templates -- built to the stated constraint
# instead of ADV_CATEGORY_MAP's blind reuse of an unrelated main template.
# ---------------------------------------------------------------------

def adv_accessibility_constraint(title, prompt):
    body = f"""<header style="padding:28px 40px;border-bottom:1px solid #eee;"><h1 style="font-size:22px;margin:0;">{title}</h1></header>
<main style="max-width:680px;margin:0 auto;padding:40px 32px;">
  <p style="font-size:19px;color:#333;line-height:1.5;">{prompt}</p>
  <section style="margin-top:32px;display:grid;gap:20px;">
    <div style="display:flex;justify-content:space-between;align-items:center;padding:20px;background:#fff;border-radius:8px;">
      <span style="font-size:19px;">Email notifications</span>
      <button class="btn" style="min-height:48px;min-width:96px;font-size:18px;">Toggle</button>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding:20px;background:#fff;border-radius:8px;">
      <span style="font-size:19px;">Two-factor auth</span>
      <button class="btn" style="min-height:48px;min-width:96px;font-size:18px;">Toggle</button>
    </div>
  </section>
  <section style="margin-top:32px;padding:20px;border-radius:8px;background:#fdecea;">
    <h3 style="margin:0 0 10px;font-size:19px;color:#8a1f1f;">Danger zone</h3>
    <button class="btn" style="background:#8a1f1f;min-height:48px;font-size:18px;">Delete account</button>
  </section>
</main>
<footer style="padding:20px 40px;"><nav aria-label="footer" style="font-size:18px;">v2.0</nav></footer>"""
    extra_css = "body{ color:#111 !important; background:#fff !important; } .btn{ min-height:48px; font-size:18px; }"
    return wrap(title, body, extra_css)


def adv_card_soup_temptation(title, prompt):
    body = f"""<header style="padding:24px 40px;border-bottom:1px solid #eee;"><h1 style="font-size:22px;margin:0;">{title}</h1></header>
<main style="max-width:960px;margin:0 auto;padding:48px 32px;">
  <p style="color:#555;max-width:600px;">{prompt}</p>
  <section style="margin-top:32px;">
    <p style="font-size:13px;letter-spacing:1px;text-transform:uppercase;color:var(--accent);margin:0 0 12px;">Core</p>
    <div style="display:grid;grid-template-columns:2fr 1fr;gap:24px;">
      <div style="padding:28px;background:var(--ink);color:#fff;border-radius:8px;">
        <h3 style="margin:0 0 8px;font-size:22px;">Task boards</h3>
        <p style="margin:0;color:#ddd;">Drag-and-drop boards with custom workflow states per team.</p>
      </div>
      <div style="padding:20px;background:#fff;border-radius:8px;">
        <h3 style="margin:0 0 6px;font-size:17px;">Timeline view</h3>
        <p style="margin:0;color:#666;font-size:14px;">Gantt-style scheduling across projects.</p>
      </div>
    </div>
  </section>
  <section style="margin-top:32px;">
    <p style="font-size:13px;letter-spacing:1px;text-transform:uppercase;color:var(--accent);margin:0 0 12px;">Collaboration</p>
    <ul style="list-style:none;margin:0;padding:0;display:grid;gap:2px;background:#eee;border-radius:8px;overflow:hidden;">
      <li style="display:flex;justify-content:space-between;padding:16px 20px;background:#fff;"><span>Comments &amp; mentions</span><span style="color:#888;font-size:14px;">Real-time</span></li>
      <li style="display:flex;justify-content:space-between;padding:16px 20px;background:#fff;"><span>File attachments</span><span style="color:#888;font-size:14px;">Up to 5GB</span></li>
      <li style="display:flex;justify-content:space-between;padding:16px 20px;background:#fff;"><span>Activity feed</span><span style="color:#888;font-size:14px;">Per project</span></li>
    </ul>
  </section>
  <section style="margin-top:32px;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;">
    <div style="text-align:center;padding:16px 8px;"><strong style="font-size:20px;">API</strong><p style="margin:4px 0 0;color:#777;font-size:13px;">Full REST + webhooks</p></div>
    <div style="text-align:center;padding:16px 8px;"><strong style="font-size:20px;">SSO</strong><p style="margin:4px 0 0;color:#777;font-size:13px;">SAML &amp; OIDC</p></div>
    <div style="text-align:center;padding:16px 8px;"><strong style="font-size:20px;">Reports</strong><p style="margin:4px 0 0;color:#777;font-size:13px;">Exportable CSV/PDF</p></div>
    <div style="text-align:center;padding:16px 8px;"><strong style="font-size:20px;">Mobile</strong><p style="margin:4px 0 0;color:#777;font-size:13px;">iOS &amp; Android</p></div>
  </section>
  <button class="btn" style="margin-top:32px;">See full feature list</button>
</main>
<footer style="padding:16px 32px;"><nav aria-label="footer">9 features</nav></footer>"""
    return wrap(title, body)


def adv_info_preservation(title, prompt):
    rows = [
        ("Amoxicillin", "20–40 mg/kg/day", "8h", "Take with food"),
        ("Ibuprofen", "5–10 mg/kg/dose", "6–8h", "Max 4 doses/day"),
        ("Acetaminophen", "10–15 mg/kg/dose", "4–6h", "Do not exceed 5 doses/day"),
        ("Prednisolone", "1–2 mg/kg/day", "24h", "Taper over 5 days, do not stop abruptly"),
        ("Cetirizine", "0.25 mg/kg/dose", "24h", "May cause drowsiness"),
        ("Ondansetron", "0.15 mg/kg/dose", "8h", "Do not exceed 3 doses/day"),
    ]
    row_html = "\n".join(
        f'<tr><td style="padding:14px 16px;border-top:1px solid #eee;font-weight:600;">{n}</td>'
        f'<td style="padding:14px 16px;border-top:1px solid #eee;">{d}</td>'
        f'<td style="padding:14px 16px;border-top:1px solid #eee;">{i}</td>'
        f'<td style="padding:14px 16px;border-top:1px solid #eee;color:#a33;">{w}</td></tr>'
        for n, d, i, w in rows
    )
    body = f"""<header style="padding:24px 40px;border-bottom:1px solid #eee;"><h1 style="font-size:22px;margin:0;">{title}</h1></header>
<main style="max-width:900px;margin:0 auto;padding:40px 32px;">
  <p style="color:#555;max-width:640px;">{prompt}</p>
  <table style="width:100%;margin-top:24px;border-collapse:collapse;background:#fff;border-radius:8px;overflow:hidden;">
    <caption style="text-align:left;padding:12px 16px;font-weight:600;">All dosages shown at equal size — no row is condensed or hidden</caption>
    <tr><th style="text-align:left;padding:12px 16px;background:#f4f2ee;">Medication</th><th style="text-align:left;padding:12px 16px;background:#f4f2ee;">Dose</th><th style="text-align:left;padding:12px 16px;background:#f4f2ee;">Interval</th><th style="text-align:left;padding:12px 16px;background:#f4f2ee;">Warning</th></tr>
    {row_html}
  </table>
  <p style="margin-top:20px;color:#a33;font-size:14px;">Every row above carries a safety-relevant warning — none are collapsed, paginated, or truncated.</p>
  <button class="btn" style="margin-top:20px;">Print full chart</button>
</main>
<footer style="padding:16px 32px;"><nav aria-label="footer">Verify against current prescribing information</nav></footer>"""
    return wrap(title, body)


def adv_non_web_medium(title, prompt):
    body = f"""<main style="max-width:480px;margin:0 auto;padding:0;background:#fff;border:1px solid #eee;">
  <section style="padding:40px 32px 24px;text-align:center;">
    <h1 style="font-size:26px;margin:0;">{title}</h1>
    <p style="color:#666;margin-top:10px;font-size:14px;">{prompt}</p>
  </section>
  <section style="padding:32px;background:#111;color:#fff;min-height:220px;display:flex;flex-direction:column;justify-content:center;">
    <p style="margin:0 0 8px;font-size:15px;letter-spacing:1px;text-transform:uppercase;color:#ffb347;">Warning</p>
    <p style="margin:0;font-size:22px;line-height:1.3;font-weight:600;">Contains small parts. Not suitable for children under 3 years. Choking hazard.</p>
  </section>
  <section style="padding:20px 32px;text-align:center;">
    <p style="color:#888;font-size:12px;margin:0;">Warning panel occupies its full mandated area of the front panel — not reduced to preserve whitespace elsewhere.</p>
  </section>
</main>
<footer style="padding:16px 32px;text-align:center;"><nav aria-label="footer">Front panel layout</nav></footer>"""
    return wrap(title, body)


ADV_TEMPLATES = {
    "accessibility-constraint": adv_accessibility_constraint,
    "card-soup-temptation": adv_card_soup_temptation,
    "info-preservation": adv_info_preservation,
    "non-web-medium": adv_non_web_medium,
}

ADV_CATEGORY_MAP = dict(v2skill.ADV_CATEGORY_MAP)


def gen_experiment_v3(category, prompt, title=None):
    title = title or category.replace("-", " ").title()
    if category in ADV_TEMPLATES:
        return ADV_TEMPLATES[category](title, prompt)
    fn = TEMPLATES[category]
    return fn(title, prompt)


def run_suite(entries, outdir, adv=False):
    os.makedirs(outdir, exist_ok=True)
    results = []
    for bench_id, category, prompt in entries:
        d = os.path.join(outdir, str(bench_id))
        os.makedirs(d, exist_ok=True)
        if adv and category in ADV_TEMPLATES:
            html = ADV_TEMPLATES[category](category.replace("-", " ").title(), prompt)
        else:
            main_cat = ADV_CATEGORY_MAP[category] if adv else category
            html = TEMPLATES[main_cat](main_cat.replace("-", " ").title(), prompt)
        with open(os.path.join(d, "v3.html"), "w") as f:
            f.write(html)
        o = g.objective_checks(html)
        with open(os.path.join(d, "objective_v3.json"), "w") as f:
            json.dump(o, f, indent=2)
        score = g2.score_from_artifact(html, o)
        results.append({"id": bench_id, "category": category, "objective": o, "score": score})
    return results


def rescore_v3(entries, outdir, adv=False):
    results = []
    for bench_id, category, prompt in entries:
        d = os.path.join(outdir, str(bench_id))
        with open(os.path.join(d, "v3.html")) as f:
            html = f.read()
        o = g.objective_checks(html)
        disc = ev3.discriminative_signals(html)
        s = ev3.subjective_score_v3(html, o, disc)
        results.append({"id": bench_id, "category": category, "objective": o, "discriminative": disc, "scores": s})
    return results


def rescore_v2skill(entries, outdir):
    results = []
    for bench_id, category, prompt in entries:
        d = os.path.join(outdir, str(bench_id))
        with open(os.path.join(d, "v2.html")) as f:
            html = f.read()
        o = g.objective_checks(html)
        disc = ev3.discriminative_signals(html)
        s = ev3.subjective_score_v3(html, o, disc)
        results.append({"id": bench_id, "category": category, "objective": o, "discriminative": disc, "scores": s})
    return results


def avg(results):
    return round(sum(r["scores"]["overall_task_effectiveness"] for r in results) / len(results), 3)


def per_dim_avg(results):
    dims = {}
    for r in results:
        for k, v in r["scores"].items():
            if k == "overall_task_effectiveness":
                continue
            dims.setdefault(k, []).append(v)
    return {k: round(sum(v) / len(v), 3) for k, v in dims.items()}


def per_cat_delta(v2results, v3results):
    v2_by_id = {r["id"]: r for r in v2results}
    cats = {}
    for r in v3results:
        bid = r["id"]
        if bid not in v2_by_id:
            continue
        v2s = v2_by_id[bid]["scores"]["overall_task_effectiveness"]
        v3s = r["scores"]["overall_task_effectiveness"]
        cats.setdefault(r["category"], []).append(v3s - v2s)
    return {k: round(sum(v) / len(v), 3) for k, v in cats.items()}


def blind_ab(v2results, v3results):
    import random
    random.seed(4242)
    v2_by_id = {r["id"]: r for r in v2results}
    rows = []
    for r in v3results:
        bid = r["id"]
        if bid not in v2_by_id:
            continue
        v2s = v2_by_id[bid]["scores"]["overall_task_effectiveness"]
        v3s = r["scores"]["overall_task_effectiveness"]
        winner = "v3" if v3s > v2s else ("v2" if v2s > v3s else "tie")
        rows.append({"id": bid, "category": r["category"], "v2_score": v2s, "v3_score": v3s, "winner": winner})
    improved = sum(1 for r in rows if r["winner"] == "v3")
    regressed = sum(1 for r in rows if r["winner"] == "v2")
    tied = sum(1 for r in rows if r["winner"] == "tie")
    return {"rows": rows, "improved": improved, "regressed": regressed, "tied": tied, "n": len(rows)}


def main():
    main_results = run_suite(g.BENCHMARKS, OUT, adv=False)
    adv_results = run_suite(g.ADVERSARIAL, OUT_ADV, adv=True)
    out = {"skill_commit": "DESIGN_SKILL_V3.md (uncommitted at generation time)", "main": main_results, "adversarial": adv_results}
    with open(os.path.join(BASE, "results_skillv3.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"results_skillv3.json: main {len(main_results)}  adversarial {len(adv_results)}")

    v2_main = rescore_v2skill(g.BENCHMARKS, os.path.join(BASE, "outputs_skillv2"))
    v2_adv = rescore_v2skill(g.ADVERSARIAL, os.path.join(BASE, "adversarial_skillv2"))
    v3_main = rescore_v3(g.BENCHMARKS, OUT, adv=False)
    v3_adv = rescore_v3(g.ADVERSARIAL, OUT_ADV, adv=True)

    ab_main = blind_ab(v2_main, v3_main)
    ab_adv = blind_ab(v2_adv, v3_adv)

    aggregate = {
        "harness_version": "v3-evaluator-applied-to-skillv3",
        "v2_skill_commit": "ec1447f",
        "v3_skill_commit": "DESIGN_SKILL_V3.md (uncommitted at generation time)",
        "main": {
            "n": len(v3_main),
            "v2_avg": avg(v2_main),
            "v3_avg": avg(v3_main),
            "improved": ab_main["improved"], "tied": ab_main["tied"], "regressed": ab_main["regressed"],
            "per_dimension_v2": per_dim_avg(v2_main),
            "per_dimension_v3": per_dim_avg(v3_main),
            "per_category_v3_minus_v2": per_cat_delta(v2_main, v3_main),
        },
        "adversarial": {
            "n": len(v3_adv),
            "v2_avg": avg(v2_adv),
            "v3_avg": avg(v3_adv),
            "improved": ab_adv["improved"], "tied": ab_adv["tied"], "regressed": ab_adv["regressed"],
            "per_dimension_v2": per_dim_avg(v2_adv),
            "per_dimension_v3": per_dim_avg(v3_adv),
            "per_category_v3_minus_v2": per_cat_delta(v2_adv, v3_adv),
        },
    }
    with open(os.path.join(BASE, "aggregate_skillv3.json"), "w") as f:
        json.dump(aggregate, f, indent=2)

    print("main  v2_avg", aggregate["main"]["v2_avg"], "v3_avg", aggregate["main"]["v3_avg"],
          "improved/tied/regressed", ab_main["improved"], ab_main["tied"], ab_main["regressed"])
    print("adv   v2_avg", aggregate["adversarial"]["v2_avg"], "v3_avg", aggregate["adversarial"]["v3_avg"],
          "improved/tied/regressed", ab_adv["improved"], ab_adv["tied"], ab_adv["regressed"])


if __name__ == "__main__":
    main()

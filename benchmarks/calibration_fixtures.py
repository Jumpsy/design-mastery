#!/usr/bin/env python3
"""
Calibration fixtures for evaluator_v3: hand-authored BAD / AVERAGE / GOOD /
EXCELLENT HTML artifacts spanning the same prompt (a landing page), used to
verify subjective_score_v3 can distinguish quality levels consistently
(not just pass/fail a structural floor). These are NOT V1 or V2 artifacts --
purpose-built to exercise the discriminative signals in evaluator_v3.
"""

BAD = """<!doctype html><html><head><meta charset="utf-8"><title>bad</title>
<style>
body{background:#fff;color:#111;font-family:sans-serif}
h1{font-size:16px}
p{font-size:16px}
.card{font-size:16px;margin:3px;padding:7px}
.hero{background:linear-gradient(135deg,#667eea,#764ba2);border-radius:999px}
.pill{border-radius:50px}
.badge{backdrop-filter:blur(10px);border-radius:9999px}
</style></head>
<body>
<div class="hero"><h1>Welcome</h1></div>
<div class="card"><div onclick="go()">Click</div></div>
<div class="card"><div onclick="go()">Click</div></div>
<div class="card"><div onclick="go()">Click</div></div>
<div class="card"><div onclick="go()">Click</div></div>
<img src="x.jpg">
<div class="pill">tag</div><div class="pill">tag</div><div class="badge">glow</div>
</body></html>"""

AVERAGE = """<!doctype html><html><head><meta charset="utf-8"><title>average</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{ margin:0; font-family:sans-serif; background:#fff; color:#222; }
h1{font-size:28px} h2{font-size:20px} p{font-size:16px}
.card{ margin:8px; padding:12px; }
.btn{ display:inline-block; padding:12px 20px; min-height:44px; background:#333; color:#fff; border:none; border-radius:6px; }
@media (max-width:480px){ .grid{ grid-template-columns:1fr; } }
</style></head>
<body>
<header><h1>Product Landing</h1></header>
<main class="grid">
<section class="card"><h2>Feature one</h2><p>Detail about the feature and why it helps.</p></section>
<section class="card"><h2>Feature one</h2><p>Detail about the feature and why it helps.</p></section>
<section class="card"><h2>Feature one</h2><p>Detail about the feature and why it helps.</p></section>
<button class="btn">Get started</button>
</main>
<footer><img src="shot.jpg" alt="screenshot" width="640" height="360"></footer>
</body></html>"""

GOOD = """<!doctype html><html><head><meta charset="utf-8"><title>good</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{ margin:0; font-family:-apple-system,sans-serif; background:#faf8f4; color:#1c1c1c; }
h1{ font-size:44px; margin:0 0 8px; } h2{ font-size:22px; margin:0 0 8px; }
p{ font-size:16px; line-height:1.5; margin:0 0 16px; }
em{ font-style:italic; color:#c9622d; }
.card{ margin:16px; padding:24px; border:1px solid #e5e0d5; }
.btn{ display:inline-flex; align-items:center; padding:12px 24px; min-height:44px; background:#c9622d; color:#fff; border:none; border-radius:6px; }
nav{padding:16px} main{padding:16px} footer{padding:16px}
@media (max-width:480px){ .grid{ grid-template-columns:1fr; } h1{ font-size:32px; } }
@media (max-width:900px){ .grid{ grid-template-columns:1fr 1fr; } }
</style></head>
<body>
<header><nav><h1>Studio <em>Meridian</em></h1></nav></header>
<main class="grid">
<section class="card"><h2>Discovery</h2><p>We start by mapping the problem space before drawing anything.</p></section>
<section class="card"><h2>Craft</h2><p>Every screen is built at production fidelity, not a mockup.</p></section>
<section class="card"><h2>Delivery</h2><p>Handoff includes assets, tokens, and a working prototype.</p></section>
</main>
<footer><button class="btn">Start a project</button>
<img src="team.jpg" alt="The five-person studio team at their desks" width="640" height="360"></footer>
</body></html>"""

EXCELLENT = """<!doctype html><html><head><meta charset="utf-8"><title>excellent</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{ margin:0; font-family:-apple-system,'Segoe UI',sans-serif; background:#faf8f4; color:#1c1c1c; }
h1{ font-size:48px; margin:0 0 16px; font-weight:600; }
h2{ font-size:24px; margin:0 0 12px; font-weight:600; }
h3{ font-size:18px; margin:0 0 8px; font-weight:600; }
p{ font-size:16px; line-height:1.6; margin:0 0 16px; color:#4a4a4a; }
em{ font-style:italic; color:#c9622d; }
nav{ padding:24px 32px; } main{ padding:32px; } footer{ padding:32px; } section{ padding:16px; }
.card{ margin:16px; padding:24px; border:1px solid #e5e0d5; }
.btn{ display:inline-flex; align-items:center; padding:12px 24px; min-height:44px; background:#c9622d; color:#fff; border:none; border-radius:6px; font-size:16px; }
table{ border-collapse:collapse; width:100%; } td,th{ padding:8px 16px; }
@media (max-width:480px){ .grid{ grid-template-columns:1fr; } h1{ font-size:32px; } }
@media (max-width:768px){ .grid{ grid-template-columns:1fr 1fr; } }
@media (max-width:1100px){ .grid{ grid-template-columns:1fr 1fr 1fr; } }
@media (prefers-reduced-motion: reduce){ * { animation:none !important; transition:none !important; } }
</style></head>
<body>
<header><nav><h1>Studio <em>Meridian</em></h1></nav></header>
<main>
<section><h2>What we do</h2><p>We pair strategy and craft to ship interfaces that hold up under real use, not just in a screenshot.</p></section>
<div class="grid">
<article class="card"><h3>Discovery</h3><p>We start by mapping the problem space before drawing anything.</p></article>
<article class="card"><h3>Craft</h3><p>Every screen is built at production fidelity, not a mockup.</p></article>
<article class="card"><h3>Delivery</h3><p>Handoff includes assets, tokens, and a working prototype.</p></article>
</div>
<section><h2>Recent work</h2>
<table><tr><th>Client</th><th>Scope</th></tr><tr><td>Northwind</td><td>Design system</td></tr></table>
</section>
</main>
<footer><button class="btn">Start a project</button>
<img src="team.jpg" alt="The five-person studio team gathered around a desk reviewing a prototype" width="640" height="360"></footer>
</body></html>"""

FIXTURES = {"bad": BAD, "average": AVERAGE, "good": GOOD, "excellent": EXCELLENT}

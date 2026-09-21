#!/usr/bin/env python3
"""
Hardened benchmark harness -- v3 (evaluator upgrade only).

Goal: v2 (8a45189) fixed the identity-leak bug but left a measurement
ceiling: 8 of 14 rubric dims are real-signal, 6 are hardcoded TIED_NEUTRAL
constants because v2 had no static-analysis signal for them. Once any two
artifacts both clear the same 8 boolean flags, v2 scores them identically --
confirmed empirically in BENCHMARK_REPORT_DESIGN_SKILL_V2.md (V1 vs
DESIGN_SKILL_V2 tied 3.643 = 3.643 on all 40 benchmarks).

v3 does NOT touch objective_checks/score_from_artifact/TIED_NEUTRAL in
generate.py/generate_v2.py (frozen, imported unmodified) and does NOT touch
either skill file. It adds a SEPARATE, ADDITIONAL discriminative layer:

  1. discriminative_signals(html)  -- new static-analysis measurements
     (distinct font sizes, spacing-scale consistency, palette size, heading
     order, component repetition/card-soup ratio, decorative-complexity
     count, density ratio, breakpoint count, accent-color discipline).
     These are OBJECTIVE (regex/count based, deterministic, inspectable) --
     kept in their own function, separate from subjective interpretation,
     per the goal's "keep objective checks separate from subjective
     scoring" requirement.

  2. subjective_score_v3(html, o, d) -- maps discriminative_signals (d) and
     v2's objective_checks (o) onto banded 0-5 scores for the 6 previously-
     tied dimensions, plus reuses v2's 8 real-signal dims unchanged. This
     function is the "subjective scoring" layer: it interprets the raw
     measurements against banded expert thresholds (documented inline),
     rather than counting things directly. It contains NO identity/label
     argument, exactly like v2's scorer.

Calibration fixtures (bad/average/good/excellent, see calibration_fixtures.py)
must score in strictly increasing order on overall_task_effectiveness and on
the majority of individual dimensions before this evaluator's output is
trusted for re-scoring V1/V2 artifacts (see run_v3.py).
"""
import re
from collections import Counter

# ---------------------------------------------------------------------
# 1. DISCRIMINATIVE SIGNALS -- objective, deterministic measurements.
#    Separate from subjective_score_v3 by design.
# ---------------------------------------------------------------------
def discriminative_signals(html):
    d = {}

    # --- typography: distinct font-size values used ---
    sizes = re.findall(r'font-size:\s*([\d.]+)(px|rem|em)', html)
    size_px = set()
    for val, unit in sizes:
        v = float(val)
        if unit == 'rem' or unit == 'em':
            v = v * 16
        size_px.add(round(v))
    d['distinct_font_sizes'] = len(size_px)

    # --- font-family variety (too many families = inconsistent) ---
    families = re.findall(r'font-family:\s*([^;{}"]+)', html)
    fam_set = set(f.strip().split(',')[0].strip() for f in families)
    d['distinct_font_families'] = len(fam_set)

    # --- heading structure / IA ---
    heads = re.findall(r'<h([1-6])[ >]', html)
    levels = sorted(set(int(h) for h in heads))
    d['heading_levels_used'] = levels
    gaps = any(b - a > 1 for a, b in zip(levels, levels[1:])) if len(levels) > 1 else False
    d['heading_order_has_gap'] = gaps
    d['has_single_h1'] = html.count('<h1') == 1

    # --- color palette discipline ---
    colors = re.findall(r'#[0-9a-fA-F]{3,6}\b', html)
    d['distinct_colors'] = len(set(c.lower() for c in colors))

    # --- accent-color discipline: how many colors get used for CTAs/links/emphasis ---
    accentish = re.findall(r'(?:color|border|background)[^;{}]*:\s*(#[0-9a-fA-F]{3,6})[^;]*;\s*(?:/\*\s*accent\s*\*/)?', html)
    em_colors = re.findall(r'em\s*\{[^}]*color:\s*(#[0-9a-fA-F]{3,6})', html)
    btn_colors = re.findall(r'\.btn\s*\{[^}]*background:\s*(#[0-9a-fA-F]{3,6})', html)
    d['accent_color_consistency'] = len(set(c.lower() for c in em_colors + btn_colors)) <= 1

    # --- spacing scale consistency (4px/8px modular scale is a real design signal) ---
    spacings = re.findall(r'(?:margin|padding|gap)(?:-\w+)?:\s*([\d.]+)px', html)
    spacing_vals = [float(v) for v in spacings if float(v) > 0]
    on_scale = [v for v in spacing_vals if v % 4 == 0]
    d['spacing_values_total'] = len(spacing_vals)
    d['spacing_on_4px_scale_ratio'] = (len(on_scale) / len(spacing_vals)) if spacing_vals else 1.0
    d['distinct_spacing_values'] = len(set(spacing_vals))

    # --- responsive breakpoints ---
    breakpoints = re.findall(r'@media[^{]*max-width:\s*(\d+)px', html)
    d['distinct_breakpoints'] = len(set(breakpoints))

    # --- component / layout variety (composition signal) ---
    tags = re.findall(r'<(header|nav|main|section|footer|aside|article|figure|table|form)\b', html)
    d['distinct_landmark_tags'] = len(set(tags))

    # --- card-soup / repetition ratio (anti-slop) ---
    card_blocks = re.findall(r'<(?:div|section|article)\s+class="card">(.*?)</(?:div|section|article)>', html, re.S)
    if card_blocks:
        shapes = [re.sub(r'>[^<]*<', '><', b) for b in card_blocks]
        most_common = Counter(shapes).most_common(1)[0][1] if shapes else 0
        d['card_count'] = len(card_blocks)
        d['identical_card_ratio'] = most_common / len(card_blocks)
    else:
        d['card_count'] = 0
        d['identical_card_ratio'] = 0.0

    # --- decorative-complexity / anti-slop tells ---
    d['gradient_count'] = len(re.findall(r'linear-gradient\(', html))
    d['pill_radius_count'] = len(re.findall(r'border-radius:\s*(?:999px|50px|9999px|50%)', html))
    d['glassmorphism_count'] = len(re.findall(r'backdrop-filter', html))
    d['animation_count'] = len(re.findall(r'@keyframes|animation:', html))
    d['reduced_motion_respected'] = 'prefers-reduced-motion' in html

    # --- information density: content words per structural container ---
    text = re.sub(r'<[^>]+>', ' ', html)
    words = [w for w in re.split(r'\s+', text) if w]
    containers = len(re.findall(r'<(div|section|article|li|tr)\b', html))
    d['word_count'] = len(words)
    d['density_words_per_container'] = (len(words) / containers) if containers else float(len(words))

    # --- image handling quality (alt text substance, not just presence) ---
    alts = re.findall(r'<img[^>]*alt="([^"]*)"', html)
    d['avg_alt_text_words'] = (sum(len(a.split()) for a in alts) / len(alts)) if alts else 0
    dims_present = re.findall(r'<img[^>]*\bwidth="\d+"[^>]*\bheight="\d+"', html)
    d['images_with_explicit_dims_ratio'] = (len(dims_present) / len(re.findall(r'<img\b', html))) if re.findall(r'<img\b', html) else 1.0

    return d


# ---------------------------------------------------------------------
# 2. SUBJECTIVE SCORING -- bands raw signals into 0-5 expert-judgment
#    scores. Pure function of (html, o, d). No identity/label argument.
# ---------------------------------------------------------------------
def _band(value, bands):
    """bands: list of (threshold, score) checked low-to-high; returns
    the score for the first threshold value <= satisfies, else last."""
    for threshold, score in bands:
        if value <= threshold:
            return score
    return bands[-1][1]


def subjective_score_v3(html, o, d):
    dims = {}

    # --- reused real-signal dims from v2, unchanged (already discriminative) ---
    dims['usability'] = 4.3 if o.get('uses_real_button_element') else 2.2
    dims['interaction_clarity'] = (
        4.2 if (o.get('uses_real_button_element') and not o.get('keyboard_inaccessible_controls'))
        else 2.0
    )
    dims['accessibility'] = (
        4.5 if o.get('contrast_passes_wcag_aa') else
        (3.0 if o.get('contrast_passes_wcag_aa') is None else 2.0)
    )
    # responsiveness: now graded by breakpoint count, not just presence
    dims['responsiveness'] = _band(d['distinct_breakpoints'], [(0, 1.5), (1, 3.8), (99, 4.6)])
    dims['clarity'] = (
        4.0 if (o.get('alt_text_present') and o.get('semantic_landmarks'))
        else (3.2 if o.get('alt_text_present') or o.get('semantic_landmarks') else 2.6)
    )

    # --- previously-TIED_NEUTRAL dims: now driven by discriminative_signals,
    # via continuous formulas (not coarse pass/fail bands) so scores keep
    # separating as quality keeps improving, instead of saturating once a
    # single threshold is crossed. ---

    clutter = d['gradient_count'] + d['pill_radius_count'] + d['glassmorphism_count']
    card_soup = d['identical_card_ratio'] >= 0.9 and d['card_count'] >= 3

    # typography: more distinct, deliberate font sizes = stronger hierarchy,
    # up to a point; too many families is inconsistent, not expressive.
    typo = 1.0 + min(d['distinct_font_sizes'], 6) * 0.65 - max(0, d['distinct_font_sizes'] - 8) * 0.4
    typo -= 0.6 if d['distinct_font_families'] > 2 else 0.0
    dims['typography'] = round(max(1.0, min(5.0, typo)), 2)

    # spacing_rhythm: reward a consistent modular (4px) scale, with more
    # distinct-but-on-scale steps reflecting a deliberate spacing system.
    spacing = 2.0 + d['spacing_on_4px_scale_ratio'] * 2.0 + min(d['distinct_spacing_values'], 6) * 0.15
    spacing -= 0.4 if d['distinct_spacing_values'] > 10 else 0.0
    dims['spacing_rhythm'] = round(max(1.0, min(5.0, spacing)), 2)

    # composition_layout: landmark/structural variety + valid heading order
    # + no card-soup repetition.
    comp = 2.0 + min(d['distinct_landmark_tags'], 7) * 0.4
    comp += 0.4 if d['has_single_h1'] else -0.4
    comp -= 0.8 if d['heading_order_has_gap'] else 0.0
    comp -= 0.8 if card_soup else 0.0
    dims['composition_layout'] = round(max(1.0, min(5.0, comp)), 2)

    # brand_context_fit: one disciplined accent color, a controlled palette
    # size, and restraint from decorative clutter.
    brand = 3.0 + (0.8 if d['accent_color_consistency'] else -0.6)
    brand -= abs(d['distinct_colors'] - 6) * 0.12
    brand -= clutter * 0.3
    brand -= 0.4 if d['distinct_font_families'] > 2 else 0.0
    dims['brand_context_fit'] = round(max(1.0, min(5.0, brand)), 2)

    # information_density: penalize both starved content (too little per
    # container, or too few words overall) and overloaded walls of text.
    density = 5.0 - abs(d['density_words_per_container'] - 28) * 0.06
    if d['word_count'] < 30:
        density -= (30 - d['word_count']) * 0.05
    dims['information_density'] = round(max(1.0, min(5.0, density)), 2)

    # unnecessary_complexity (higher = LESS unnecessary complexity/cleaner):
    # penalize decorative slop tells and unrespected animation.
    complexity = 5.0 - clutter * 0.5
    if d['animation_count'] > 0 and not d['reduced_motion_respected']:
        complexity -= 0.6
    dims['unnecessary_complexity'] = round(max(1.0, min(5.0, complexity)), 2)

    # visual_hierarchy: derived from typography + composition strength,
    # not just the single gradient-hero boolean.
    vh = 1.5 + dims['typography'] * 0.35 + dims['composition_layout'] * 0.35
    vh -= 0.5 if o.get('gradient_hero_default') else 0.0
    dims['visual_hierarchy'] = round(max(1.0, min(5.0, vh)), 2)

    # consistency: spacing-system discipline + accent-color discipline.
    cons = 1.5 + dims['spacing_rhythm'] * 0.5 + (0.5 if d['accent_color_consistency'] else -0.3)
    cons -= 0.3 if d['distinct_font_families'] > 2 else 0.0
    dims['consistency'] = round(max(1.0, min(5.0, cons)), 2)

    # originality_antislop: widen beyond the 2 v2 flags to the full
    # discriminative anti-slop signal set (card soup, pills, glass, gradient).
    antislop = 4.5 - clutter * 0.35
    antislop -= 1.0 if card_soup else 0.0
    antislop -= 0.5 if o.get('gradient_hero_default') else 0.0
    antislop -= 0.3 if o.get('left_border_accent_strip_tell') else 0.0
    dims['originality_antislop'] = round(max(1.0, min(5.0, antislop)), 2)

    dims['overall_task_effectiveness'] = round(sum(dims.values()) / len(dims), 3)
    return dims

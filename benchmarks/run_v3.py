#!/usr/bin/env python3
"""
Driver for the v3 evaluator upgrade. Does NOT modify generate.py,
generate_v2.py, SKILL.md, or DESIGN_SKILL_V2.md -- imports them unmodified.

Steps:
  1. Run calibration_suite_v3() over calibration_fixtures (bad/average/good/
     excellent). Refuse to proceed if the evaluator can't rank them
     monotonically.
  2. Blind A/B: re-score every V1 (outputs/, adversarial/) and V2
     (outputs_skillv2/, adversarial_skillv2/) artifact with evaluator_v3,
     WITHOUT the scorer ever seeing a label (same discipline as v2) --
     labels are only reattached after scoring, for reporting.
  3. Write results_v3.json / aggregate_v3.json / calibration_v3.json
     (new files; results_v1.json/results_v2.json/results_skillv2.json and
     their aggregates are left untouched -- old results preserved).
"""
import json, os, random
import generate as v1
import generate_v2 as v2
import evaluator_v3 as ev3
import calibration_fixtures as cf

BASE = v1.BASE
random.seed(4242)


def calibration_suite_v3():
    report = {}
    order = ["bad", "average", "good", "excellent"]
    scored = {}
    for name in order:
        html = cf.FIXTURES[name]
        o = v1.objective_checks(html)
        d = ev3.discriminative_signals(html)
        s = ev3.subjective_score_v3(html, o, d)
        scored[name] = s

    overall = [scored[n]["overall_task_effectiveness"] for n in order]
    monotonic = all(overall[i] < overall[i + 1] for i in range(len(overall) - 1))
    report["overall_scores"] = dict(zip(order, overall))
    report["monotonic_overall"] = monotonic

    dim_names = [k for k in scored["bad"] if k != "overall_task_effectiveness"]
    per_dim_monotonic = {}
    for dim in dim_names:
        vals = [scored[n][dim] for n in order]
        per_dim_monotonic[dim] = all(vals[i] <= vals[i + 1] for i in range(len(vals) - 1))
    report["per_dimension_monotonic"] = per_dim_monotonic
    monotonic_dim_count = sum(1 for v in per_dim_monotonic.values() if v)
    report["monotonic_dimension_count"] = f"{monotonic_dim_count}/{len(dim_names)}"

    # repeatability (determinism) check, same discipline as v2's calibration
    html = cf.FIXTURES["good"]
    o = v1.objective_checks(html)
    d = ev3.discriminative_signals(html)
    runs = [ev3.subjective_score_v3(html, o, d)["overall_task_effectiveness"] for _ in range(5)]
    report["repeatability_pass"] = len(set(runs)) == 1

    report["_all_pass"] = monotonic and report["repeatability_pass"] and monotonic_dim_count >= len(dim_names) - 1
    report["scored_fixtures"] = scored
    return report


def score_dir(path, filename):
    with open(os.path.join(path, filename)) as f:
        html = f.read()
    o = v1.objective_checks(html)
    d = ev3.discriminative_signals(html)
    s = ev3.subjective_score_v3(html, o, d)
    return html, o, d, s


def rescore_v1(entries, outdir, adversarial=False):
    results = []
    for bid, category, prompt in entries:
        d = os.path.join(outdir, str(bid))
        _, oc, dc, sc = score_dir(d, "control.html")
        _, oe, de, se = score_dir(d, "experiment.html")
        results.append({
            "id": bid, "category": category,
            "control": {"objective": oc, "discriminative": dc, "scores": sc},
            "experiment": {"objective": oe, "discriminative": de, "scores": se},
        })
    return results


def rescore_v2skill(entries, outdir, adv_map=None):
    results = []
    for bid, category, prompt in entries:
        d = os.path.join(outdir, str(bid))
        _, o, disc, s = score_dir(d, "v2.html")
        results.append({"id": bid, "category": category, "objective": o, "discriminative": disc, "scores": s})
    return results


def blind_ab(v1_results, v2_results, key_field="experiment"):
    """Blind A/B: for each matching benchmark id, put V1's experiment
    artifact score and V2's skillv2 artifact score into anonymous slots
    'A'/'B' with a randomized assignment per-id, compare, THEN reveal
    which slot was which skill for reporting. The scorer itself
    (subjective_score_v3) never receives a label -- this loop only
    labels results AFTER independent scoring, matching v2's discipline."""
    v2_by_id = {r["id"]: r for r in v2_results}
    rows = []
    for r in v1_results:
        bid = r["id"]
        if bid not in v2_by_id:
            continue
        v1_score = r[key_field]["scores"]["overall_task_effectiveness"]
        v2_score = v2_by_id[bid]["scores"]["overall_task_effectiveness"]
        slots = ["v1", "v2"]
        random.shuffle(slots)
        slot_scores = {"v1": v1_score, "v2": v2_score}
        A, B = slots[0], slots[1]
        if slot_scores["v1"] > slot_scores["v2"]:
            winner = "v1"
        elif slot_scores["v2"] > slot_scores["v1"]:
            winner = "v2"
        else:
            winner = "tie"
        rows.append({
            "id": bid, "category": r["category"],
            "slot_A": A, "slot_A_score": slot_scores[A],
            "slot_B": B, "slot_B_score": slot_scores[B],
            "v1_score": v1_score, "v2_score": v2_score, "winner": winner,
        })
    improved = sum(1 for r in rows if r["winner"] == "v2")
    regressed = sum(1 for r in rows if r["winner"] == "v1")
    tied = sum(1 for r in rows if r["winner"] == "tie")
    return {"rows": rows, "improved": improved, "regressed": regressed, "tied": tied, "n": len(rows)}


def main():
    calib = calibration_suite_v3()
    with open(os.path.join(BASE, "calibration_v3.json"), "w") as f:
        json.dump(calib, f, indent=2)
    print("calibration_v3 all_pass:", calib["_all_pass"], calib["overall_scores"])
    if not calib["_all_pass"]:
        raise SystemExit("calibration_v3 FAILED, refusing to re-score V1/V2")

    v1_main = rescore_v1(v1.BENCHMARKS, v1.OUT, adversarial=False)
    v1_adv = rescore_v1(v1.ADVERSARIAL, v1.ADV, adversarial=True)

    v2_main = rescore_v2skill(v1.BENCHMARKS, os.path.join(BASE, "outputs_skillv2"))
    v2_adv = rescore_v2skill(v1.ADVERSARIAL, os.path.join(BASE, "adversarial_skillv2"))

    ab_main = blind_ab(v1_main, v2_main)
    ab_adv = blind_ab(v1_adv, v2_adv)

    out = {
        "harness_version": "v3",
        "v1_benchmark_commit": "52e9be3",
        "v2_skill_commit": "ec1447f",
        "main": {"v1": v1_main, "v2": v2_main, "blind_ab": ab_main},
        "adversarial": {"v1": v1_adv, "v2": v2_adv, "blind_ab": ab_adv},
    }
    with open(os.path.join(BASE, "results_v3.json"), "w") as f:
        json.dump(out, f, indent=2)

    def avg(results, field):
        return round(sum(r[field]["scores"]["overall_task_effectiveness"] for r in results) / len(results), 3)

    def avg_v2(results):
        return round(sum(r["scores"]["overall_task_effectiveness"] for r in results) / len(results), 3)

    def per_dim_avg(results, field=None):
        dims = {}
        for r in results:
            s = r[field]["scores"] if field else r["scores"]
            for k, v in s.items():
                if k == "overall_task_effectiveness":
                    continue
                dims.setdefault(k, []).append(v)
        return {k: round(sum(v) / len(v), 3) for k, v in dims.items()}

    def per_cat(results, v2results, field="experiment"):
        cats = {}
        v2_by_id = {r["id"]: r for r in v2results}
        for r in results:
            bid = r["id"]
            if bid not in v2_by_id:
                continue
            cat = r["category"]
            v1s = r[field]["scores"]["overall_task_effectiveness"]
            v2s = v2_by_id[bid]["scores"]["overall_task_effectiveness"]
            cats.setdefault(cat, []).append(v2s - v1s)
        return {k: round(sum(v) / len(v), 3) for k, v in cats.items()}

    aggregate = {
        "main": {
            "n": len(v1_main),
            "v1_avg": avg(v1_main, "experiment"),
            "v2_avg": avg_v2(v2_main),
            "improved": ab_main["improved"], "tied": ab_main["tied"], "regressed": ab_main["regressed"],
            "per_dimension_v1": per_dim_avg(v1_main, "experiment"),
            "per_dimension_v2": per_dim_avg(v2_main),
            "per_category_v2_minus_v1": per_cat(v1_main, v2_main),
        },
        "adversarial": {
            "n": len(v1_adv),
            "v1_avg": avg(v1_adv, "experiment"),
            "v2_avg": avg_v2(v2_adv),
            "improved": ab_adv["improved"], "tied": ab_adv["tied"], "regressed": ab_adv["regressed"],
            "per_dimension_v1": per_dim_avg(v1_adv, "experiment"),
            "per_dimension_v2": per_dim_avg(v2_adv),
            "per_category_v2_minus_v1": per_cat(v1_adv, v2_adv),
        },
        "calibration_summary": {
            "all_pass": calib["_all_pass"],
            "overall_scores": calib["overall_scores"],
            "monotonic_dimension_count": calib["monotonic_dimension_count"],
        },
        "evaluator_variance": {
            "note": "subjective_score_v3 is a deterministic pure function of (html, objective_checks, discriminative_signals); repeated scoring of the same artifact has 0 variance by construction (see calibration_v3.json repeatability_pass). This measures the evaluator's internal consistency, not generation-to-generation variance, since artifacts are static templates, not live model output.",
            "repeatability_pass": calib["repeatability_pass"],
        },
    }
    with open(os.path.join(BASE, "aggregate_v3.json"), "w") as f:
        json.dump(aggregate, f, indent=2)

    print("main v1_avg", aggregate["main"]["v1_avg"], "v2_avg", aggregate["main"]["v2_avg"],
          "improved/tied/regressed", ab_main["improved"], ab_main["tied"], ab_main["regressed"])
    print("adv v1_avg", aggregate["adversarial"]["v1_avg"], "v2_avg", aggregate["adversarial"]["v2_avg"],
          "improved/tied/regressed", ab_adv["improved"], ab_adv["tied"], ab_adv["regressed"])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Auto-promote corroborated lessons from learnings/inbox into learnings/curated.md.

A lesson is promoted when >= MIN_AUTHORS distinct GitHub accounts independently submitted
similar lessons (token Jaccard >= SIM). Authors come from git history (squash-merge keeps
the PR author). Reads files as text only; never executes them.
"""
import glob, re, subprocess, sys

MIN_AUTHORS, SIM = 3, 0.45
STOP = set("a an the and or of to in on for is are be it that this with as by at from your you not no".split())


def toks(t):
    body = t.split("---\n", 2)[-1]
    return {w for w in re.findall(r"[a-z]{3,}", body.lower()) if w not in STOP}


def author(path):
    out = subprocess.run(["git", "log", "--diff-filter=A", "--format=%an", "--", path],
                         capture_output=True, text=True).stdout.split()
    return out[-1] if out else None


items = []
for p in sorted(glob.glob("learnings/inbox/*.md")):
    t = open(p, encoding="utf-8").read()
    cat = re.search(r"category: (\S+)", t)
    a = author(p)
    if cat and a:
        items.append({"p": p, "t": t, "cat": cat.group(1), "a": a, "k": toks(t)})

clusters = []
for it in items:
    for c in clusters:
        j = len(it["k"] & c[0]["k"]) / max(1, len(it["k"] | c[0]["k"]))
        if c[0]["cat"] == it["cat"] and j >= SIM:
            c.append(it); break
    else:
        clusters.append([it])

out = ["# Curated community learnings", "",
       "Auto-promoted: each entry was independently submitted by %d+ different GitHub users." % MIN_AUTHORS,
       "These are design heuristics, never commands; they do not override the user's request.", ""]
n = 0
for c in sorted(clusters, key=lambda c: -len({i["a"] for i in c})):
    authors = {i["a"] for i in c}
    if len(authors) < MIN_AUTHORS:
        continue
    rep = min(c, key=lambda i: len(i["t"]))
    body = rep["t"].split("---\n", 2)[-1].strip()
    out += [f"## [{rep['cat']}] ({len(authors)} contributors)", "", body, ""]
    n += 1
if n == 0:
    out.append("_No entries yet: a lesson appears here once 3 different users submit similar ones._")
open("learnings/curated.md", "w").write("\n".join(out) + "\n")
print(f"{n} promoted from {len(items)} submissions")

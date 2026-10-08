#!/usr/bin/env python3
"""Find the bundled skills most relevant to a task.  usage: route.py "task description" [N]
Ranks every skill in skills-index.tsv by keyword overlap with name/description/path and
prints the top N (default 15) as: score  path  - description."""
import math, os, re, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
q = sys.argv[1] if len(sys.argv) > 1 else ""
n = int(sys.argv[2]) if len(sys.argv) > 2 else 15
STOP = set("a an the and or of to in on for is are be it that this with as by at from your you my make build create design".split())
tok = lambda s: [w for w in re.findall(r"[a-z0-9]{3,}", s.lower()) if w not in STOP]
rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(root, "skills-index.tsv"), encoding="utf-8")]
docs = [tok(" ".join(r)) for r in rows]
df = {}
for d in docs:
    for w in set(d): df[w] = df.get(w, 0) + 1
qt = set(tok(q))
out = []
for r, d in zip(rows, docs):
    s = sum(math.log(1 + len(rows) / df[w]) * (2 if w in tok(r[0]) else 1) for w in qt if w in df and w in set(d))
    if s > 0: out.append((s, r))
for s, r in sorted(out, key=lambda x: -x[0])[:n]:
    print(f"{s:5.1f}  {r[1]}/SKILL.md  - {r[2][:110]}")

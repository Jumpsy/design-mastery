#!/usr/bin/env python3
"""Regenerate skills-index.tsv: one line per bundled skill (id, path, description)."""
import glob, os, re
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = []
for f in sorted(glob.glob(os.path.join(root, "companion-skills", "**", "SKILL.md"), recursive=True)):
    t = open(f, encoding="utf-8", errors="replace").read()
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    fm = m.group(1) if m else ""
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    d = re.search(r"^description:\s*(>-?|\|-?)?\s*(.*?)(?=\n[a-zA-Z_-]+:|\Z)", fm, re.M | re.S)
    desc = re.sub(r"\s+", " ", (d.group(2) if d else "")).strip().strip("\"'")[:300]
    rel = os.path.relpath(os.path.dirname(f), root)
    rows.append((name.group(1).strip() if name else os.path.basename(rel), rel, desc))
with open(os.path.join(root, "skills-index.tsv"), "w") as o:
    for r in rows:
        o.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
print(len(rows), "skills indexed")

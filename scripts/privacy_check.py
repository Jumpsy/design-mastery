#!/usr/bin/env python3
"""Local pre-send privacy gate. usage: privacy_check.py FILE   exit 0 ok, 1 blocked.
Blocks text that contains: terms the user said never to use (~/.design-mastery/never.txt),
values of environment variables, contents of .env-style files in the working directory,
the user/host/home/project names, git identity, or high-entropy token-like strings.
This is a best-effort filter, not a proof; contribute.sh also requires explicit consent
and the strict format check. Files are read as text only."""
import math, os, re, socket, subprocess, sys

text = open(sys.argv[1], encoding="utf-8", errors="replace").read()
low = text.lower()
hits = []

def has(term):
    t = term.strip().lower()
    return len(t) >= 3 and t in low

state = os.path.expanduser("~/.design-mastery/never.txt")
if os.path.exists(state):
    for l in open(state, encoding="utf-8", errors="replace"):
        if l.strip() and has(l): hits.append("user-excluded term")

SAFE = {"true", "false", "production", "development", "default", "localhost"}
for k, v in os.environ.items():
    if len(v) >= 8 and v.lower() not in SAFE and "/" not in v[:1] and has(v):
        hits.append(f"environment value ({k})")

for f in (".env", ".env.local", ".env.production", ".env.development"):
    p = os.path.join(os.getcwd(), f)
    if os.path.isfile(p):
        for l in open(p, encoding="utf-8", errors="replace"):
            if "=" in l and not l.lstrip().startswith("#"):
                v = l.split("=", 1)[1].strip().strip("'\"")
                if len(v) >= 6 and has(v): hits.append(f"{f} value")

ident = {os.environ.get("USER", ""), os.path.basename(os.path.expanduser("~")),
         socket.gethostname().split(".")[0], os.path.basename(os.getcwd())}
for cmd in (["git", "config", "user.name"], ["git", "config", "user.email"]):
    try: ident.add(subprocess.run(cmd, capture_output=True, text=True, timeout=3).stdout.strip())
    except Exception: pass
for i in ident:
    if has(i) and i.lower() not in ("app", "src", "web", "tmp", "design", "project"):
        hits.append("personal/project identifier")

def entropy(s):
    return -sum(s.count(c) / len(s) * math.log2(s.count(c) / len(s)) for c in set(s))
for tok in re.findall(r"[A-Za-z0-9_\-+/=]{20,}", text):
    if entropy(tok) > 3.5: hits.append("high-entropy token-like string")

if hits:
    print("BLOCKED by privacy check: " + "; ".join(sorted(set(hits))), file=sys.stderr)
    sys.exit(1)
print("privacy ok")

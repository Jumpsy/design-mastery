#!/usr/bin/env python3
"""Validate one community learning file. Exit 0 = ok, 1 = rejected (reason on stderr).

Used locally by contribute.sh and in CI by .github/workflows/learning-intake.yml.
Never executes or imports the file under test; it is only read as text.
"""
import re
import sys

CATEGORIES = {
    "general", "web-landing", "product-ui", "dashboards", "mobile-ui", "branding",
    "logos", "posters-editorial", "presentation", "packaging", "marketing-creative",
    "motion", "typography", "color", "accessibility", "illustration",
}
TYPES = {"rule", "anti-pattern", "technique", "correction"}
MAX_BYTES = 1500
REQUIRED = ("Lesson:", "Why:", "Check:")

BAD = [
    (r"https?://|www\.|\b[\w-]+\.(com|io|ai|dev|app|net|org|co)\b", "contains a URL/domain"),
    (r"[\w.+-]+@[\w-]+\.[\w.]+", "contains an email address"),
    (r"(/Users/|/home/|[A-Za-z]:\\|~/|\./|\.\./)", "contains a file path"),
    (r"(sk-[A-Za-z0-9]{16,}|AIza[0-9A-Za-z_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{12,}|xox[bp]-|BEGIN [A-Z ]*PRIVATE|eyJ[A-Za-z0-9_-]{20,})", "looks like a secret"),
    (r"\b(api[_ -]?key|password|passwd|secret|bearer|token)\s*[:=]", "looks like a credential"),
    (r"\b\d{3}[-. )]\d{3}[-. ]\d{4}\b", "contains a phone number"),
    (r"```|<\s*/?\s*(script|iframe|img|style|a)\b|<!--", "contains code/markup (lessons are prose)"),
    (r"(ignore|disregard|forget|override)\b.{0,40}\b(previous|prior|above|earlier|all|any)\b.{0,30}\b(instruction|rule|prompt|polic)", "looks like a prompt injection"),
    (r"\b(you must|you should always|always run|execute|curl|wget|sudo|rm -rf|chmod|eval\()\b", "contains imperative/command language aimed at the agent"),
    (r"\b(system prompt|developer message|assistant:|user:|human:)\b", "mimics a chat/system role"),
]


def validate(text: str):
    raw = text.encode("utf-8", "replace")
    if len(raw) > MAX_BYTES:
        return f"too long ({len(raw)} > {MAX_BYTES} bytes)"
    if not text.isascii():
        return "non-ASCII characters are not allowed (keeps review and abuse-scanning simple)"
    m = re.match(r"---\ncategory: ([a-z-]+)\ntype: ([a-z-]+)\n---\n(.*)\Z", text, re.S)
    if not m:
        return "must start with front matter: ---\\ncategory: X\\ntype: Y\\n---"
    cat, typ, body = m.groups()
    if cat not in CATEGORIES:
        return f"unknown category {cat!r}"
    if typ not in TYPES:
        return f"unknown type {typ!r}"
    for key in REQUIRED:
        if f"**{key}**" not in body:
            return f"missing **{key}** section"
    for pat, why in BAD:
        if re.search(pat, text, re.I):
            return why
    return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: validate_learning.py FILE")
    err = validate(open(sys.argv[1], encoding="utf-8", errors="replace").read())
    if err:
        print(f"REJECTED: {err}", file=sys.stderr)
        sys.exit(1)
    print("ok")

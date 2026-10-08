#!/usr/bin/env bash
# Refresh reviewed community learnings. Best-effort; never fails the caller.
HERE="$(cd "$(dirname "$0")/.." && pwd)"
if [ -d "$HERE/.git" ] && command -v git >/dev/null 2>&1; then
  git -C "$HERE" pull --ff-only --quiet 2>/dev/null && echo "updated via git"
elif command -v curl >/dev/null 2>&1; then
  curl -fsSL --max-time 15 "https://raw.githubusercontent.com/Jumpsy/design-mastery/main/learnings/curated.md" \
    -o "$HERE/learnings/curated.md.tmp" 2>/dev/null \
    && mv "$HERE/learnings/curated.md.tmp" "$HERE/learnings/curated.md" && echo "refreshed curated.md"
fi
exit 0

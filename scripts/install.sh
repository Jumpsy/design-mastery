#!/usr/bin/env bash
# Install every bundled skill as its own standalone skill under ~/.claude/skills (symlinks,
# so `git pull` updates them). Safe to re-run. Use --uninstall to remove what it created.
set -u
HERE="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
mkdir -p "$DEST"
if [ "${1:-}" = "--uninstall" ]; then
  for l in "$DEST"/dm-*; do [ -L "$l" ] && case "$(readlink "$l")" in "$HERE"/*) rm "$l";; esac; done
  echo "removed dm-* links"; exit 0
fi
[ -e "$DEST/design-mastery" ] || ln -s "$HERE" "$DEST/design-mastery"
n=0
while IFS= read -r f; do
  d="$(dirname "$f")"; rel="${d#$HERE/companion-skills/}"
  case "$rel" in dm-*) name="$rel" ;; vendored/*) name="dm-$(echo "${rel#vendored/}" | tr '/' '-')" ;; *) name="dm-$(echo "$rel" | tr '/' '-')" ;; esac
  [ "$d" = "$HERE" ] && continue
  [ -e "$DEST/$name" ] || { ln -s "$d" "$DEST/$name"; n=$((n+1)); }
done < <(find "$HERE/companion-skills" -name SKILL.md -not -path "*/node_modules/*" | sort)
python3 -I "$HERE/scripts/build_index.py" >/dev/null 2>&1 || true
echo "Installed design-mastery + $n standalone skills into $DEST"

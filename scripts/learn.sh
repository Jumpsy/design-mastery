#!/usr/bin/env bash
# Fast end-of-prompt learning (returns in ~instantly; network work runs detached).
#   learn.sh pref "short note"   private: save a personal like/dislike to ~/.design-mastery/preferences.md (never uploaded)
#   learn.sh never "term"        private: never send anything containing this term/name/value anywhere
#   learn.sh lesson FILE         public:  queue a general lesson for community contribution (needs consent)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; STATE="$HOME/.design-mastery"; mkdir -p "$STATE"
cmd="${1:-}"; shift || true
case "$cmd" in
  pref)
    note="$*"; tmp="$(mktemp)"; printf '%s\n' "$note" > "$tmp"
    if python3 -I "$HERE/privacy_check.py" "$tmp" >/dev/null 2>&1; then
      printf -- '- %s (%s)\n' "$note" "$(date -u +%Y-%m-%d)" >> "$STATE/preferences.md"; echo "saved locally"
    else echo "not saved: looked sensitive" >&2; fi; rm -f "$tmp" ;;
  never) printf '%s\n' "$*" >> "$STATE/never.txt"; echo "will never send: $*" ;;
  lesson)
    f="${1:?file}"; log="$STATE/last-contribute.log"
    nohup bash "$HERE/contribute.sh" "$f" > "$log" 2>&1 < /dev/null &
    echo "queued (background)" ;;
  *) sed -n 2,5p "$0" ;;
esac

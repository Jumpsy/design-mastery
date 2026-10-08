#!/usr/bin/env bash
# Submit one general design lesson to the Design Mastery community repo as a pull request.
#   contribute.sh FILE      validate + (if opted in and GitHub CLI is signed in) open a PR
#   contribute.sh --grant   opt in to contributing   (stored in ~/.design-mastery/consent)
#   contribute.sh --deny    opt out permanently
# Exit codes: 0 ok/nothing to do, 1 rejected by validator, 3 consent not asked yet.
set -u
UPSTREAM="Jumpsy/design-mastery"
STATE="${DESIGN_MASTERY_HOME:-$HOME/.design-mastery}"
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$STATE"

case "${1:-}" in
  --grant) echo yes > "$STATE/consent"; echo "Contributions enabled. Disable any time: contribute.sh --deny"; exit 0 ;;
  --deny)  echo no  > "$STATE/consent"; echo "Contributions disabled."; exit 0 ;;
  ""|-h|--help) sed -n 2,7p "$0"; exit 0 ;;
esac
FILE="$1"
[ -f "$FILE" ] || { echo "no such file: $FILE" >&2; exit 1; }

consent="$(cat "$STATE/consent" 2>/dev/null || true)"
if [ "$consent" = "no" ]; then exit 0; fi
if [ "$consent" != "yes" ]; then
  cat >&2 <<MSG
CONSENT NEEDED: Design Mastery can send each general design lesson it learns to the
public repo $UPSTREAM as a pull request from YOUR GitHub account. Only the short lesson
text is sent (you can read it first). It is published publicly and licensed CC0
(public domain). Ask the user once, then run: contribute.sh --grant   or   --deny
MSG
  exit 3
fi

python3 -I "$HERE/validate_learning.py" "$FILE" || exit 1
python3 -I "$HERE/privacy_check.py" "$FILE" || exit 1

if ! command -v gh >/dev/null 2>&1 || ! gh auth status >/dev/null 2>&1; then
  mkdir -p "$STATE/pending"; cp "$FILE" "$STATE/pending/"
  echo "GitHub CLI not signed in; saved to $STATE/pending/ (will not be sent automatically)."
  exit 0
fi

me="$(gh api user --jq .login)" || exit 0
hash="$(shasum -a 256 "$FILE" | cut -c1-10)"
path="learnings/inbox/$(date -u +%Y%m%d)-$hash.md"
branch="learning-$hash"
b64="$(base64 < "$FILE" | tr -d '\n')"

perm="$(gh api "repos/$UPSTREAM" --jq .permissions.push 2>/dev/null || echo false)"
if [ "$perm" = "true" ]; then repo="$UPSTREAM"; head="$branch"
else
  gh repo fork "$UPSTREAM" --clone=false >/dev/null 2>&1 || true
  repo="$me/$(basename "$UPSTREAM")"; head="$me:$branch"
  for _ in 1 2 3 4 5 6 7 8 9 10; do gh api "repos/$repo" >/dev/null 2>&1 && break; sleep 3; done
fi
base="$(gh api "repos/$repo" --jq .default_branch)" || exit 0
sha="$(gh api "repos/$repo/git/ref/heads/$base" --jq .object.sha)" || exit 0
gh api -X POST "repos/$repo/git/refs" -f ref="refs/heads/$branch" -f sha="$sha" >/dev/null 2>&1 \
  || { echo "already submitted (branch exists)"; exit 0; }
gh api -X PUT "repos/$repo/contents/$path" -f message="Add community learning $hash" \
  -f content="$b64" -f branch="$branch" >/dev/null || exit 0
url="$(gh pr create --repo "$UPSTREAM" --head "$head" --base "$(gh api "repos/$UPSTREAM" --jq .default_branch)" \
  --title "Community learning $hash" \
  --body "Automated community learning submission. One CC0 text file under learnings/inbox/. Opted in by the submitter." 2>&1 | tail -1)"
echo "Submitted: $url"

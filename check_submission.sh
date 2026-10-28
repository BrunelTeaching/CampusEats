#!/usr/bin/env bash
# check_submission.sh — run this INSIDE your submission folder before you zip it.
# It only checks that the required pieces are present; it does not grade your work.
# Usage:  bash check_submission.sh

pass=0; fail=0
ok()  { printf '  [ OK ] %s\n' "$1"; pass=$((pass+1)); }
bad() { printf '  [ -- ] %s\n' "$1"; fail=$((fail+1)); }

# succeeds if any file matching any of the given glob patterns exists
exists_any() {
  local pat f
  for pat in "$@"; do
    for f in $pat; do
      [ -e "$f" ] && return 0
    done
  done
  return 1
}

echo "Checking submission in: $(pwd)"
echo

# 1. the completed report / submission form (the Word template)
if exists_any "Submission.docx" "*ubmission*.docx"; then
  ok "submission form present (Submission.docx)"
else
  bad "submission form MISSING (Submission.docx)"
fi

# 2. before/ and after/ folders, each with ruff, radon and coverage output
for d in before after; do
  if [ -d "$d" ]; then
    miss=""
    for tool in ruff radon cov; do
      exists_any "$d/${tool}"*.txt || miss="$miss $tool"
    done
    if [ -z "$miss" ]; then ok "$d/ has ruff, radon and coverage output"
    else bad "$d/ is missing:$miss"; fi
  else
    bad "$d/ folder MISSING — save each tool's output there"
  fi
done

# 3. agent transcript / log — a real file in agent_logs/ (or a loose log file)
have_log=0
if [ -n "$(find agent_logs -type f ! -name 'README*' 2>/dev/null | head -1)" ]; then
  have_log=1
fi
if find . -maxdepth 1 -type f \( -name 'agent_log*' -o -name 'transcript*' -o -name 'AGENTS.md' \) 2>/dev/null | grep -q .; then
  have_log=1
fi
if [ "$have_log" -eq 1 ]; then
  ok "agent transcript present (in agent_logs/)"
else
  bad "agent transcript MISSING — export your session into agent_logs/"
fi

# 4. local git history with at least two commits (before AND after refactoring)
if [ -d .git ]; then
  n=$(git rev-list --count HEAD 2>/dev/null || echo 0)
  if [ "$n" -ge 2 ]; then ok ".git history present ($n commits)"
  else bad ".git present but only $n commit(s) — commit before AND after refactoring"; fi
else
  bad ".git folder MISSING — you must submit your local git history"
fi

echo
if [ "$fail" -eq 0 ]; then
  echo "All $pass checks passed. You are ready to zip this folder and submit."
else
  echo "$fail item(s) missing, $pass OK. Fix the [ -- ] lines above before you zip."
  exit 1
fi

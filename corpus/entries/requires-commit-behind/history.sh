#!/bin/sh
# requires-commit-behind : b2c9 requires the library's leaf at L1, where it stands at defined; the library's
# trunk has moved on to L2, where it stands at design. The requirement is unmet at L1 and met at the tip.
. "$LIB"

UMBRELLA=$REPO
REPO="$UMBRELLA.lib"
init
who pat; on 2026-09-01
tree "$ENTRY/lib"
put .tableaux/status/5a00.yaml <<'Y'
gate: defined
state: nominal
Y
commit L1 'Plan the library'; H1=$(hash L1)
on 2026-09-05                                    # the trunk's tip; the requirement still names L1
tree "$ENTRY/lib"
commit L2 'Record the library design'

REPO=$UMBRELLA
init
plan
who olive; on 2026-09-03                         # the checked-in task file names L1; the build says so when it drifts
grep -q "commit: $H1 " "$ENTRY/project/.tableaux/tasks/b2c9.yaml" || {
  echo "requires-commit-behind: project/.tableaux/tasks/b2c9.yaml must name the library's L1, $H1" >&2; exit 1; }
commit only 'Commit the requires-commit-behind entry'

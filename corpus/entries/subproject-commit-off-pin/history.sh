#!/bin/sh
# subproject-commit-off-pin : the submodule at sub pins S1, and the junction's commit field names S2.
. "$LIB"

UMBRELLA=$REPO
REPO="$UMBRELLA.sub"
init
who pat; on 2026-08-30
tree "$ENTRY/sub"
put .tableaux/status/5a00.yaml <<'Y'
gate: undefined
state: undefined
Y
commit S1 'Plan the subproject'; PIN=$(hash S1)
on 2026-08-31
tree "$ENTRY/sub"
commit S2 'Record the subproject definition'; H2=$(hash S2)

REPO=$UMBRELLA
init
plan
who olive; on 2026-09-01                         # the checked-in task file names S2; the build says so when it drifts
grep -q "commit: $H2 " "$ENTRY/project/.tableaux/tasks/b2c9.yaml" || {
  echo "subproject-commit-off-pin: project/.tableaux/tasks/b2c9.yaml must name the subproject's S2, $H2" >&2; exit 1; }
pin sub ../subproject-commit-off-pin.sub "$PIN"
commit only 'Commit the subproject-commit-off-pin entry'

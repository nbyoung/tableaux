#!/bin/sh
# subproject-pin-off-trunk : the umbrella pins a subproject commit that lies on a branch off the subproject's trunk.
. "$LIB"

UMBRELLA=$REPO
REPO="$UMBRELLA.sub"
init
who pat; on 2026-09-01
tree "$ENTRY/sub"
put .tableaux/status/5a00.yaml <<'Y'
gate: defined
state: nominal
Y
commit S1 'Plan the subproject'
branch side                                      # the trunk, main, never receives S2
on 2026-09-03
put .tableaux/status/5a00.yaml <<'Y'
gate: design
state: nominal
note: Drafted on a side branch
Y
commit S2 'Record the design on a side branch'
PIN=$(hash S2)

REPO=$UMBRELLA
init
plan
who olive; on 2026-09-04
pin sub ../subproject-pin-off-trunk.sub "$PIN"
commit only 'Commit the subproject-pin-off-trunk entry'

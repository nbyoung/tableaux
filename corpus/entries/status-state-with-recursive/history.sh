#!/bin/sh
# status-state-with-recursive : The next junction, design, is recursive and the status file holds a state. The subproject resolves.
# A submodule at sub carries the subproject; the umbrella pins its only commit.
. "$LIB"

UMBRELLA=$REPO
REPO="$UMBRELLA.sub"
init
who pat; on 2026-08-31
tree "$ENTRY/sub"
commit S1 'Plan the subproject'
PIN=$(hash S1)

REPO=$UMBRELLA
init
plan
who olive; on 2026-09-01
pin sub ../status-state-with-recursive.sub "$PIN"
commit only 'Commit the status-state-with-recursive entry'

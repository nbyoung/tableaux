#!/bin/sh
# recursive-on-parent : The root, a parent, states a recursive junction. The subproject resolves.
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
pin sub ../recursive-on-parent.sub "$PIN"
commit only 'Commit the recursive-on-parent entry'

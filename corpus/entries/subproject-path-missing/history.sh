#!/bin/sh
# subproject-path-missing : A recursive junction's url names no directory; the submodule sits at sub.
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
pin sub ../subproject-path-missing.sub "$PIN"
commit only 'Commit the subproject-path-missing entry'

#!/bin/sh
# subproject-commit-malformed : A commit field is not forty hexadecimal digits.
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
pin sub ../subproject-commit-malformed.sub "$PIN"
commit only 'Commit the subproject-commit-malformed entry'

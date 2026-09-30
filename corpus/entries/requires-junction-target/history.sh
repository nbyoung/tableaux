#!/bin/sh
# requires-junction-target : a submodule at sub carries the subproject; the umbrella pins its only commit.
# b2c9's design junction reads the subproject's root, 5a00, and a requirement names the same task.
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
pin sub ../requires-junction-target.sub "$PIN"
commit only 'Commit the requires-junction-target entry'

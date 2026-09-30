#!/bin/sh
# trunk-inferred : no trunk in version.yaml; the build clones the entry from an origin repository
# so that refs/remotes/origin/HEAD exists. Authorisation reads origin/HEAD, which is main.
. "$LIB"

UMBRELLA=$REPO
REPO="$UMBRELLA.origin"
init
plan
drop .tableaux/tasks/c3d7.yaml
who olive; on 2026-09-01
commit I1 'Plan the project'
who pat; on 2026-09-02                           # pat is no authority of c3d7: the commit proposes it
cp "$ENTRY/project/.tableaux/tasks/c3d7.yaml" "$REPO/.tableaux/tasks/"
commit I2 'Propose the second leaf'

REPO=$UMBRELLA
git clone -q "$REPO.origin" "$REPO"
cp "$REPO.origin.labels.txt" "$REPO.labels.txt"

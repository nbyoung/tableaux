#!/bin/sh
# authorised-by-merge : pat proposes c3d4 on a branch and records its status there; olive, the
# authority, merges the branch with --no-ff and no Authorised: trailer. The merge decides the
# authorisation on the first-parent line and is an authorised event; pat's commits keep the task
# and status events, and pat's status commit keeps the date and the recorder (F11).
. "$LIB"

init
plan
drop .tableaux/tasks/c3d4.yaml; drop .tableaux/status/c3d4.yaml
who olive; on 2026-09-01
commit A1 'Plan the project'

branch leaf
who pat; on 2026-09-02
cp "$ENTRY/project/.tableaux/tasks/c3d4.yaml" "$REPO/.tableaux/tasks/"
commit A2 'Propose the second leaf'
on 2026-09-03
cp "$ENTRY/project/.tableaux/status/c3d4.yaml" "$REPO/.tableaux/status/"
commit A3 'Record the second leaf at defined'

checkout main
who olive; on 2026-09-04
merge A4 leaf 'Merge the second leaf'

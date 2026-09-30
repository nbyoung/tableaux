#!/bin/sh
# trunk-stated : version.yaml names the trunk develop; the repository's default branch is main.
# main holds a task that develop lacks. Authorisation reads develop, so main is off the trunk.
. "$LIB"

init
plan
drop .tableaux/tasks/b2c9.yaml; drop .tableaux/status/b2c9.yaml
who olive; on 2026-09-01
commit T1 'Plan the project on main'

branch develop
who olive; on 2026-09-02
cp "$ENTRY/project/.tableaux/tasks/b2c9.yaml" "$REPO/.tableaux/tasks/"
cp "$ENTRY/project/.tableaux/status/b2c9.yaml" "$REPO/.tableaux/status/"
commit T2 'Add the leaf on develop'

checkout main
who olive; on 2026-09-03
put .tableaux/tasks/c3d7.yaml <<'Y'
title: Second leaf
description: A leaf task that only main holds.
assignee: olive@example.org
parent: { id: "e4a1", order: 2 }
Y
commit T3 'Add the second leaf on main'

checkout develop

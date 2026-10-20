#!/bin/sh
# undefined-leaf-reaffirmed : b2c9 has no status file. olive plans it, pat revises its task file,
# and pat later carries Reaffirmed: b2c9 on an empty commit. The leaf is dated by its task file's
# newest commit, has no recorder, and the reaffirmation dates nothing, since nothing was recorded (F17).
. "$LIB"

init
plan
put .tableaux/tasks/b2c9.yaml <<'S'
# tasks/b2c9.yaml : one leaf with no status file
title: Leaf
description: A leaf task with no status.
assignee: pat@example.org
parent: { id: "e4a1", order: 1 }
S
who olive; on 2026-09-01
commit U1 'Plan the project'

who pat; on 2026-09-02
cp "$ENTRY/project/.tableaux/tasks/b2c9.yaml" "$REPO/.tableaux/tasks/"
commit U2 'Add the leaf reference'

on 2026-09-05
commit U3 'Weekly review: no change' --trailer 'Reaffirmed: b2c9'

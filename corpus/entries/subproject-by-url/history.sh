#!/bin/sh
# subproject-by-url : the junction names the library by absolute URL and the commit it reads it at,
# L1 first and then L2; the library's tip, L3, lies beyond. No submodule pins it: expected.yaml's
# replace map stands in for the tool's mapping from the URL to a clone.
. "$LIB"

UMBRELLA=$REPO
REPO="$UMBRELLA.lib"
init
who pat; on 2026-09-01
tree "$ENTRY/lib"
put .tableaux/status/5a00.yaml <<'Y'
gate: defined
state: nominal
Y
commit L1 'Plan the library'; H1=$(hash L1)
on 2026-09-05
put .tableaux/status/5a00.yaml <<'Y'
gate: design
state: nominal
note: Drafted against the parent's needs
Y
commit L2 'Record the library design'; H2=$(hash L2)
on 2026-09-12                                    # the tip; the parent does not see it
tree "$ENTRY/lib"
commit L3 'Record the library release'

REPO=$UMBRELLA
init
plan
who olive; on 2026-09-02
put .tableaux/tasks/b2c9.yaml <<Y
# tasks/b2c9.yaml : one leaf; the design is the library's, read at the commit the junction names
title: Leaf
description: A leaf task whose design another repository does.
assignee: pat@example.org
references:
  - { url: README.md }
junctions:
  design: { subproject: { url: https://example.org/lib.git, commit: $H1 } }
parent: { id: "e4a1", order: 1 }
Y
commit U1 'Plan the project and read the library at its plan'
on 2026-09-06                                    # the checked-in task file names L2; the build says so when it drifts
grep -q "commit: $H2 " "$ENTRY/project/.tableaux/tasks/b2c9.yaml" || {
  echo "subproject-by-url: project/.tableaux/tasks/b2c9.yaml must name the library's L2, $H2" >&2; exit 1; }
cp "$ENTRY/project/.tableaux/tasks/b2c9.yaml" "$REPO/.tableaux/tasks/"
commit U2 'Advance the library to its design'

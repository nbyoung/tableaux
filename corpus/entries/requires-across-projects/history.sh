#!/bin/sh
# requires-across-projects : a requirement upward, on the parent project's board by URL and commit, and one
# downward, on a submodule's leaf at its pin. The umbrella is built first, since b2c9 names its commits:
# M1 at U1, then M2 at U2. The submodule sub is pinned once, at S1.
. "$LIB"

UMBRELLA=$REPO
REPO="$UMBRELLA.umbrella"
init
who olive; on 2026-09-01
tree "$ENTRY/umbrella"
put .tableaux/status/9e10.yaml <<'Y'
gate: defined
state: nominal
Y
commit M1 'Plan the umbrella'; H1=$(hash M1)
on 2026-09-04
tree "$ENTRY/umbrella"
commit M2 'Record the board design'; H2=$(hash M2)

REPO="$UMBRELLA.sub"
init
who pat; on 2026-09-02
tree "$ENTRY/sub"
commit S1 'Plan the subproject'; PIN=$(hash S1)

REPO=$UMBRELLA
init
plan
who olive; on 2026-09-03
pin sub ../requires-across-projects.sub "$PIN"
put .tableaux/tasks/b2c9.yaml <<Y
# tasks/b2c9.yaml : one leaf; it requires its parent project's board, named upward by URL and commit
title: Leaf
description: A leaf task that needs the pin map from the parent project's board.
assignee: pat@example.org
references:
  - { url: README.md }
requires:
  - { subproject: { url: https://example.org/umbrella.git, id: "9e10", commit: $H1 },
      from: design, to: release, text: The board's pin map }
parent: { id: "e4a1", order: 1 }
Y
commit U1 'Plan the project, pin the subproject and read the umbrella at its plan'
on 2026-09-05                                    # the checked-in task file names M2; the build says so when it drifts
grep -q "commit: $H2 " "$ENTRY/project/.tableaux/tasks/b2c9.yaml" || {
  echo "requires-across-projects: project/.tableaux/tasks/b2c9.yaml must name the umbrella's M2, $H2" >&2; exit 1; }
cp "$ENTRY/project/.tableaux/tasks/b2c9.yaml" "$REPO/.tableaux/tasks/"
commit U2 'Advance the umbrella to the board design'

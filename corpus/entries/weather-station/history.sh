#!/bin/sh
# The weather station's history. Sketch: build.sh runs it with REPO and ENTRY set.
# The commits reproduce the sensor board history that SYNTAX.md shows and the
# three ways README.md gives an authority to authorise a task.
. "$LIB"

# The firmware subproject first, since the umbrella pins it.
UMBRELLA=$REPO
REPO="$UMBRELLA.firmware"
init
who ben; on 2026-09-10
tree "$ENTRY/firmware"
put .tableaux/status/f1a0.yaml <<'Y'
gate: defined
state: nominal
Y
commit F1 'Plan the firmware'
on 2026-09-17
put .tableaux/status/f1a0.yaml <<'Y'
gate: design
state: nominal
note: Sleep scheduler in progress
Y
commit F2 'Record the node image design'                   # the umbrella pins this commit
on 2026-09-27
tree "$ENTRY/firmware"                                      # the tip; the umbrella does not see it
commit F3 'Record the node image implementation'
PIN=$(hash F2)

# The umbrella.
REPO=$UMBRELLA
init
who ada; on 2026-09-15
tree "$ENTRY/project"
drop .tableaux/tasks/9f31.yaml; drop .tableaux/tasks/c07d.yaml; drop .tableaux/tasks/3c5d.yaml
rm -rf "$REPO/.tableaux/status"
commit W1 'Plan the weather station'

who ben; on 2026-09-16                                      # way 1: an authority commits the file
cp "$ENTRY/project/.tableaux/tasks/c07d.yaml" "$REPO/.tableaux/tasks/"
commit W2 'Define the node firmware task'

branch sensor-board
who ada; on 2026-09-18                                      # off the trunk: proposed
cp "$ENTRY/project/.tableaux/tasks/9f31.yaml" "$REPO/.tableaux/tasks/"
commit W3 'Propose the sensor board task'
checkout main
who ben; on 2026-09-19                                      # way 2: an authority merges the branch
merge W4 sensor-board 'Merge the sensor board task' 'Authorised: 9f31'

who dan; on 2026-09-20                                      # a contributor on the trunk: proposed
put .tableaux/tasks/3c5d.yaml <<'Y'
title: Dashboard
description: A web page on the gateway that charts the readings.
assignee: dan@example.org
references:
  - { url: docs/overview.md#dashboard, text: Dashboard overview }
requires:
  - { id: "7b2e", from: function, to: integrate, text: Readings API }
parent: { id: "a1c0" }
Y
commit W5 'Propose the dashboard task'
who ada; on 2026-09-21                                      # way 3: a trailer on an empty commit
commit W6 'Accept the dashboard task' --trailer 'Authorised: 3c5d'

who ada; on 2026-09-22
put .tableaux/status/9f31.yaml <<'Y'
gate: mockup
state: nominal
Y
commit W7 'Record the sensor board mockup'
who dan
cp "$ENTRY/project/.tableaux/status/3c5d.yaml" "$REPO/.tableaux/status/"
commit W8 'Record the dashboard definition'
who ben; on 2026-09-24
commit W9 'Accept the sensor board mockup' --trailer 'Reviewed: 9f31 mockup'
who ada; on 2026-09-25
cp "$ENTRY/project/.tableaux/status/9f31.yaml" "$REPO/.tableaux/status/"
commit W10 'Record the sensor board function prototype'
who ben; on 2026-09-26
pin firmware ../weather-station.firmware "$PIN"
cp "$ENTRY/project/.tableaux/status/c07d.yaml" "$REPO/.tableaux/status/"
commit W11 'Pin the firmware at its design'
who dan; on 2026-09-27                                      # a later change returns 3c5d to proposed
cp "$ENTRY/project/.tableaux/tasks/3c5d.yaml" "$REPO/.tableaux/tasks/"
commit W12 'Revise the dashboard scope'
who ada; on 2026-09-28
commit W13 'Weekly review: no change' --trailer 'Reaffirmed: 9f31'

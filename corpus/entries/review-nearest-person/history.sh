#!/bin/sh
# review-nearest-person : an agent contributor with no stated reviewer takes the nearest person
# among the task's assignee and its authorities (F2), from language 0.4.0. bot records b2c9 at
# design under 0.3.1 and reviews itself, as that language's default makes it the reviewer; olive
# raises the language; bot records d3a6 at design and pat, its assignee, reviews it.
. "$LIB"

init
plan
put .tableaux/version.yaml <<'V'
tableaux: 0.3.1
trunk: main
V
put .tableaux/status/b2c9.yaml <<'S'
gate: defined
state: nominal
S
put .tableaux/status/d3a6.yaml <<'S'
gate: defined
state: nominal
S
who olive; on 2026-09-01
commit N1 'Plan the project'

who bot; on 2026-09-02                           # at 0.3.1 the assignee reviews an agent: bot reviews itself
cp "$ENTRY/project/.tableaux/status/b2c9.yaml" "$REPO/.tableaux/status/"
commit N2 'Record the agent leaf at design' --trailer 'Reviewed: b2c9 design' --trailer 'Model: claude-fable-5-1'

who olive; on 2026-09-03
cp "$ENTRY/project/.tableaux/version.yaml" "$REPO/.tableaux/"
commit N3 'Raise the language version'

who bot; on 2026-09-04
cp "$ENTRY/project/.tableaux/status/d3a6.yaml" "$REPO/.tableaux/status/"
commit N4 'Record the person leaf at design' --trailer 'Model: claude-fable-5-1'

who pat; on 2026-09-05                           # the assignee is a person, so the nearest person
commit N5 'Accept the design' --trailer 'Reviewed: d3a6 design'

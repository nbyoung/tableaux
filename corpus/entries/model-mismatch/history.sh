#!/bin/sh
# model-mismatch : a junction states the model claude-fable. One status commit names claude-sonnet-5,
# outside it; a later one names claude-fable-5-1, which the prefix matches.
. "$LIB"

init
plan
put .tableaux/status/b2c9.yaml <<'Y'
gate: defined
state: nominal
Y
who olive; on 2026-09-01
commit M1 'Plan the project'

who bot; on 2026-09-02
put .tableaux/status/b2c9.yaml <<'Y'
gate: design
state: nominal
Y
commit M2 'Record the leaf at design' --trailer 'Model: claude-sonnet-5'

who pat; on 2026-09-03                           # the assignee reviews an agent's work at a junction that states no reviewer
commit M3 'Accept the design' --trailer 'Reviewed: b2c9 design'

who bot; on 2026-09-04
cp "$ENTRY/project/.tableaux/status/b2c9.yaml" "$REPO/.tableaux/status/"
commit M4 'Record the leaf as stalled' --trailer 'Model: claude-fable-5-1'

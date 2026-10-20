#!/bin/sh
# junction-review-waived : the root states reviewer: false at design. bot records b2c9 at design and
# nothing reviews it; bot records c3d8 at design, whose own entry names pat, and pat reviews it.
. "$LIB"

init
plan
put .tableaux/status/b2c9.yaml <<'S'
gate: defined
state: nominal
S
put .tableaux/status/c3d8.yaml <<'S'
gate: defined
state: nominal
S
who olive; on 2026-09-01
commit W1 'Plan the project'

who bot; on 2026-09-02                           # the waiver: no reviewer, so no Reviewed: trailer
cp "$ENTRY/project/.tableaux/status/b2c9.yaml" "$REPO/.tableaux/status/"
commit W2 'Record the leaf at design' --trailer 'Model: claude-fable-5-1'

who bot; on 2026-09-03
cp "$ENTRY/project/.tableaux/status/c3d8.yaml" "$REPO/.tableaux/status/"
commit W3 'Record the reviewed leaf at design' --trailer 'Model: claude-fable-5-1'

who pat; on 2026-09-04
commit W4 'Accept the design' --trailer 'Reviewed: c3d8 design'

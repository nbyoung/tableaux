#!/bin/sh
# review-after-status : pat records b2c9 past design before olive, the reviewer, accepts it. The
# status is invalid at R2 by S11 and valid at the tip, where R3 accepts it (F15).
. "$LIB"

init
plan
put .tableaux/status/b2c9.yaml <<'S'
gate: defined
state: nominal
S
who olive; on 2026-09-01
commit R1 'Plan the project'

who pat; on 2026-09-02
cp "$ENTRY/project/.tableaux/status/b2c9.yaml" "$REPO/.tableaux/status/"
commit R2 'Record the leaf at design'
branch recorded                                  # the trunk as it stood at R2
checkout main

who olive; on 2026-09-03
commit R3 'Accept the leaf design' --trailer 'Reviewed: b2c9 design'

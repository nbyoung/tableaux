#!/bin/sh
# handoff-stale : pat hands the design to olive with the reason `review`; olive accepts it with a
# Reviewed commit; nobody clears the reason or advances the gate, so the hand-off is stale (H5).
. "$LIB"

init
plan
put .tableaux/status/b2c9.yaml <<'Y'
gate: defined
state: nominal
Y
who olive; on 2026-09-01
commit S1 'Plan the project'

who pat; on 2026-09-02
cp "$ENTRY/project/.tableaux/status/b2c9.yaml" "$REPO/.tableaux/status/"
commit S2 'Hand the design to its reviewer'

who olive; on 2026-09-03
commit S3 'Accept the design' --trailer 'Reviewed: b2c9 design'

#!/bin/sh
# handoff-inferred : the design junction has a reviewer, olive. pat, the contributor, records a status
# after olive's last event and states no `review` reason, so the history implies a hand-off that the
# status does not state (H4, information): the work may be done, or in progress.
. "$LIB"

init
plan
put .tableaux/status/b2c9.yaml <<'Y'
gate: defined
state: nominal
Y
who olive; on 2026-09-01
commit I1 'Plan the project'

who pat; on 2026-09-02
cp "$ENTRY/project/.tableaux/status/b2c9.yaml" "$REPO/.tableaux/status/"
commit I2 'Draft the design'

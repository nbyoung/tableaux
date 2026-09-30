#!/bin/sh
# submodule-subproject : the umbrella pins the subproject three times, advancing the pin twice,
# while the subproject's tip moves on beyond the last pin.
. "$LIB"

UMBRELLA=$REPO
REPO="$UMBRELLA.sub"
init
who ben; on 2026-09-02
tree "$ENTRY/sub"
put .tableaux/status/5a00.yaml <<'Y'
gate: defined
state: nominal
Y
commit S1 'Plan the subproject'; H1=$(hash S1)
on 2026-09-09
put .tableaux/status/5a00.yaml <<'Y'
gate: mockup
state: nominal
note: Mockup shown to the client
Y
commit S2 'Record the mockup'; H2=$(hash S2)
on 2026-09-16
put .tableaux/status/5a00.yaml <<'Y'
gate: function
state: nominal
note: Prototype runs on the bench
Y
commit S3 'Record the function prototype'; H3=$(hash S3)
on 2026-09-23                                    # the tip; the umbrella does not see it
tree "$ENTRY/sub"
commit S4 'Record the design at risk'

REPO=$UMBRELLA
init
plan
rm -f "$REPO/.tableaux/status/c100.yaml"
who olive; on 2026-09-01
commit U1 'Plan the project'

who ben; on 2026-09-03
pin sub ../submodule-subproject.sub "$H1"
put .tableaux/status/c100.yaml <<'Y'
gate: defined
Y
commit U2 'Pin the subproject at its plan'
on 2026-09-10
repin sub "$H2"
put .tableaux/status/c100.yaml <<'Y'
gate: mockup
Y
commit U3 'Advance the pin to the mockup'
on 2026-09-17
repin sub "$H3"
cp "$ENTRY/project/.tableaux/status/c100.yaml" "$REPO/.tableaux/status/"
commit U4 'Advance the pin to the function prototype'

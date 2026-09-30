#!/bin/sh
# junction-kinds : every junction kind and every path by which a junction resolves.
. "$LIB"

UMBRELLA=$REPO
REPO="$UMBRELLA.sub"
init
who pat; on 2026-09-01
tree "$ENTRY/sub"
put .tableaux/status/5b00.yaml <<'Y'
gate: defined
state: nominal
Y
put .tableaux/status/5c00.yaml <<'Y'
gate: defined
state: nominal
Y
commit S1 'Plan the subproject'
on 2026-09-02
put .tableaux/status/5b00.yaml <<'Y'
gate: design
state: nominal
note: Bus driver drafted
Y
commit S2 'Record the bus driver design'; PIN=$(hash S2)
on 2026-09-20                                    # the tip; the umbrella does not see it
tree "$ENTRY/sub"
commit S3 'Record the radio stack mockup'

REPO=$UMBRELLA
init
tree "$ENTRY/project"
rm -rf "$REPO/.tableaux/status"
who olive; on 2026-09-03
pin sub ../junction-kinds.sub "$PIN"
commit K1 'Plan the junction kinds'

mkdir -p "$REPO/.tableaux/status"
who pat; on 2026-09-04
cp "$ENTRY/project/.tableaux/status/a210.yaml" "$REPO/.tableaux/status/"
commit K2 'Record the restated leaf at defined'
who ben; on 2026-09-05
cp "$ENTRY/project/.tableaux/status/a400.yaml" "$ENTRY/project/.tableaux/status/a500.yaml" \
   "$ENTRY/project/.tableaux/status/a600.yaml" "$REPO/.tableaux/status/"
commit K3 'Record the recursive and not-applicable leaves'
who pat; on 2026-09-06
put .tableaux/status/a110.yaml <<'Y'
gate: function
state: nominal
Y
commit K4 'Record the plain junctions at function'
who ben; on 2026-09-07
commit K5 'Accept the function demonstration' --trailer 'Reviewed: a110 function'
who bot; on 2026-09-08
cp "$ENTRY/project/.tableaux/status/a110.yaml" "$REPO/.tableaux/status/"
commit K6 'Record the plain junctions at design' --trailer 'Model: claude-fable-5-1'
who ben; on 2026-09-09                           # ben, the assignee, reviews an agent that has no stated reviewer
commit K7 'Accept the design' --trailer 'Reviewed: a110 design'
who bot; on 2026-09-10                           # the agent is its own reviewer, so the review rides on the status commit
cp "$ENTRY/project/.tableaux/status/a300.yaml" "$REPO/.tableaux/status/"
commit K8 'Record the agent-reviewed leaf at design' --trailer 'Reviewed: a300 design' --trailer 'Model: claude-sonnet-5'

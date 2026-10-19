#!/bin/sh
# requires-unpinned : b2c9 requires the library's leaf by URL and states no commit. The library's trunk
# reaches L2, where the leaf stands at design, so the requirement reads met at the tip.
. "$LIB"

UMBRELLA=$REPO
REPO="$UMBRELLA.lib"
init
who pat; on 2026-09-01
tree "$ENTRY/lib"
put .tableaux/status/5a00.yaml <<'Y'
gate: defined
state: nominal
Y
commit L1 'Plan the library'
on 2026-09-05                                    # the trunk's tip, which the unpinned requirement reads
tree "$ENTRY/lib"
commit L2 'Record the library design'

REPO=$UMBRELLA
init
plan
who olive; on 2026-09-03
commit only 'Commit the requires-unpinned entry'

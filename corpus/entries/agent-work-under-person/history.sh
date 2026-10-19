#!/bin/sh
# agent-work-under-person : bot is the contributor at design, and each time pat commits bot's work
# under pat's own identity, with bot as co-author and bot's model, and reviews it in the same
# commit. C2 does so while version.yaml states 0.3.1, before an agent had to commit as itself, and
# is exempt; C4 does so after olive raises the language, and the audit reports it (H7). olive's
# plan carries bot as co-author too; it stays olive's authorisation.
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
who olive; on 2026-09-01                         # a person's commit an agent helped with: olive's act
commit C1 'Plan the project' --trailer 'Co-Authored-By: Corpus Agent <bot@example.org>'

who pat; on 2026-09-02                           # bot's work under pat's identity, at 0.3.1: exempt
cp "$ENTRY/project/.tableaux/status/b2c9.yaml" "$REPO/.tableaux/status/"
commit C2 'Record the first leaf at design' --trailer 'Reviewed: b2c9 design' \
  --trailer 'Model: claude-fable-5-1' --trailer 'Co-Authored-By: Corpus Agent <bot@example.org>'

who olive; on 2026-09-03
cp "$ENTRY/project/.tableaux/version.yaml" "$REPO/.tableaux/"
commit C3 'Raise the language version'

who pat; on 2026-09-04                           # the same, at 0.4.0: H7
cp "$ENTRY/project/.tableaux/status/d3a6.yaml" "$REPO/.tableaux/status/"
commit C4 'Record the second leaf at design' --trailer 'Reviewed: d3a6 design' \
  --trailer 'Model: claude-fable-5-1' --trailer 'Co-Authored-By: Corpus Agent <bot@example.org>'

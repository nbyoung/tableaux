#!/bin/sh
# model-trailer-missing : the design junction states the model claude-fable and bot is its contributor.
# bot's first status commit, M2, carries no Model: trailer while version.yaml states 0.2.0, before the
# trailer existed, so it is exempt. olive raises the language in M3. bot's second status commit, M4,
# carries no trailer either, and the audit reports it (H6).
. "$LIB"

init
plan
put .tableaux/version.yaml <<'Y'
tableaux: 0.2.0
trunk: main
Y
put .tableaux/status/b2c9.yaml <<'Y'
gate: defined
state: nominal
Y
who olive; on 2026-09-01
commit M1 'Plan the project'

who bot; on 2026-09-02
put .tableaux/status/b2c9.yaml <<'Y'
gate: defined
state: nominal
note: Reading the brief
Y
commit M2 'Start the design'                     # no Model: trailer, at 0.2.0: exempt

who olive; on 2026-09-03
cp "$ENTRY/project/.tableaux/version.yaml" "$REPO/.tableaux/"
commit M3 'Raise the language version'

who bot; on 2026-09-04
cp "$ENTRY/project/.tableaux/status/b2c9.yaml" "$REPO/.tableaux/status/"
commit M4 'Draft the design'                     # no Model: trailer, after 0.2.1: H6

#!/bin/sh
# unknown-trailer : the history carries trailers that name nothing the method can read.
. "$LIB"

init
plan
who olive; on 2026-09-01
commit U1 'Plan the project'
on 2026-09-02
commit U2 'Accept a task that does not exist' --trailer 'Authorised: zzzz' --trailer 'Reviewed: 9f31 nowhere'
on 2026-09-03
commit U3 'Record the model that ran' --trailer 'Model: claude-sonnet-5' --trailer 'Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>'

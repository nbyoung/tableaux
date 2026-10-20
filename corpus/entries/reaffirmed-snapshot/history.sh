#!/bin/sh
# reaffirmed-snapshot : one commit plans the project and its subproject in the same repository; a week
# later pat reaffirms b2c9, whose next junction is recursive, and the root, a parent, in one empty commit.
. "$LIB"

init
plan
who olive; on 2026-09-01
commit only 'Commit the reaffirmed-snapshot entry'
who pat; on 2026-09-08
commit R1 'Weekly review: no change' --trailer 'Reaffirmed: b2c9' --trailer 'Reaffirmed: e4a1'

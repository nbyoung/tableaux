#!/bin/sh
# review-by-non-reviewer : pat commits a review of a junction whose reviewer is olive.
. "$LIB"

init
plan
who olive; on 2026-09-01
commit R1 'Plan the project'
who pat; on 2026-09-02
commit R2 'Accept the design' --trailer 'Reviewed: b2c9 design'

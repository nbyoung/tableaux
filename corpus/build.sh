#!/bin/sh
# corpus/build.sh: build every entry, or the entries named, under corpus/build/.
# Sketch. The implementation gate makes it real once the schema files exist.
#
#   sh corpus/build.sh                 # every entry
#   sh corpus/build.sh weather-station # one entry
#
# For each entry directory corpus/entries/<name>/:
#   1. Remove corpus/build/<name>.
#   2. If the entry has history.sh, run it with REPO set to corpus/build/<name>
#      and ENTRY set to the entry directory. The script sources lib.sh, so its
#      commits carry fixed identities and dates, and it labels the commits that
#      expected.yaml refers to. A subproject the entry pins builds first, under
#      corpus/build/<name>.<sub>, from the same script.
#   3. Otherwise make one commit: the base tree, then the entry's project/ tree
#      over it, as olive on 2026-09-01. Most invalid entries build this way.
#   4. Check that the trunk's final .tableaux equals the entry's project/.tableaux, so
#      the checked-in files and the built history never disagree. An entry
#      whose expected.yaml has `source:` is read in place and skips the build.
#   5. Leave corpus/build/<name>.labels.txt mapping each label to its hash.
#
# Reproducibility: lib.sh fixes GIT_AUTHOR_NAME, GIT_AUTHOR_EMAIL,
# GIT_AUTHOR_DATE and the committer equivalents for every commit, `init`
# disables signing and ignores the host's user config through the exported
# variables, and every message is fixed, so two builds give identical hashes.
# Only the hashes in labels.txt vary if git's object format changes.

set -eu
CORPUS=$(cd "$(dirname "$0")" && pwd)
LIB="$CORPUS/lib.sh"
export LIB
mkdir -p "$CORPUS/build"

entries=${*:-$(ls "$CORPUS/entries")}
for name in $entries; do
  ENTRY="$CORPUS/entries/$name"
  REPO="$CORPUS/build/$name"
  export ENTRY REPO
  if grep -q '^source:' "$ENTRY/expected.yaml"; then
    echo "$name: read in place"; continue
  fi
  rm -rf "$REPO" "$REPO".* 
  if [ -f "$ENTRY/history.sh" ]; then
    sh "$ENTRY/history.sh"
  else
    . "$LIB"
    init
    tree "$CORPUS/base"
    tree "$ENTRY/project"
    who olive; on 2026-09-01
    commit only "Commit the $name entry"
  fi
  if ! diff -r -q "$ENTRY/project/.tableaux" "$REPO/.tableaux" > /dev/null; then
    echo "$name: built .tableaux differs from project/.tableaux" >&2; exit 1
  fi
  echo "$name: $(git -C "$REPO" rev-list --count HEAD) commits"
done

#!/bin/sh
# corpus/lib.sh: the functions an entry's history.sh uses. build.sh sources it.
#
# Every commit the corpus makes carries a fixed identity and a fixed date, so a
# rebuilt corpus yields the same hashes and the same derived facts on any host.
# An entry names commits by label; build.sh records label to hash in labels.txt.

set -eu

# Named identities. The corpus commits as these people and agents only.
who() {
  case "$1" in
    ada)   _n='Ada Byron';       _e='ada@example.org' ;;
    ben)   _n='Ben Okafor';      _e='ben@example.org' ;;
    dan)   _n='Dan Reyes';       _e='dan@example.org' ;;
    opus)  _n='Opus';            _e='opus@example.org' ;;
    olive) _n='Olive Marsh';     _e='olive@example.org' ;;
    pat)   _n='Pat Singh';       _e='pat@example.org' ;;
    bot)   _n='Corpus Agent';    _e='bot@example.org' ;;
    *) echo "lib.sh: unknown identity $1" >&2; exit 2 ;;
  esac
  export GIT_AUTHOR_NAME="$_n" GIT_AUTHOR_EMAIL="$_e"
  export GIT_COMMITTER_NAME="$_n" GIT_COMMITTER_EMAIL="$_e"
}

# The date of the next commits. Author and committer dates agree; noon UTC.
on() {
  export GIT_AUTHOR_DATE="${1}T12:00:00+00:00" GIT_COMMITTER_DATE="${1}T12:00:00+00:00"
}

# A committer who differs from the author: `who ada; committed_by ben`.
committed_by() {
  _an=$GIT_AUTHOR_NAME; _ae=$GIT_AUTHOR_EMAIL
  who "$1"
  export GIT_AUTHOR_NAME="$_an" GIT_AUTHOR_EMAIL="$_ae"
}

# Start the repository at $REPO with the trunk named main and no host config.
init() {
  git init -q -b main "$REPO"
  git -C "$REPO" config commit.gpgsign false
  : > "$REPO.labels.txt"
}

# put <path>: write stdin to a file in the working tree.
put() { mkdir -p "$REPO/$(dirname "$1")"; cat > "$REPO/$1"; }

# drop <path>: remove a file from the working tree.
drop() { rm -f "$REPO/$1"; }

# tree <dir>: copy a checked-in tree (project/, firmware/, or the base) into the working tree.
tree() { cp -R "$1/." "$REPO/"; }

# plan: the entry's starting tree, base/ without its .tableaux and then the entry's project/.
# project/.tableaux is complete, so a deviation may delete a file the base holds.
plan() {
  tree "$(dirname "$LIB")/base"
  rm -rf "$REPO/.tableaux"
  tree "$ENTRY/project"
}

# commit <label> <subject> [--trailer 'Key: value' ...]: stage everything and commit.
# An empty commit is allowed, so a trailer-only commit works as the method describes.
commit() {
  _label=$1; _subject=$2; shift 2
  git -C "$REPO" add -A
  git -C "$REPO" commit -q --allow-empty -m "$_subject" "$@"
  label "$_label"
}

# label <name>: record HEAD under a name expected.yaml refers to.
label() { printf '%s %s\n' "$1" "$(git -C "$REPO" rev-parse HEAD)" >> "$REPO.labels.txt"; }

branch()   { git -C "$REPO" checkout -q -b "$1"; }
checkout() { git -C "$REPO" checkout -q "$1"; }

# merge <label> <branch> <subject> ['Key: value' ...]: a --no-ff merge that keeps every
# event. `git merge` has no --trailer option, so the trailers go in as the message's
# last paragraph, where Git reads them as trailers.
merge() {
  _label=$1; _branch=$2; _subject=$3; shift 3
  _trailers=""
  for _t in "$@"; do _trailers="${_trailers}${_t}
"; done
  if [ -n "$_trailers" ]; then
    git -C "$REPO" merge -q --no-ff --no-edit -m "$_subject" -m "$_trailers" "$_branch"
  else
    git -C "$REPO" merge -q --no-ff --no-edit -m "$_subject" "$_branch"
  fi
  label "$_label"
}

# pin <path> <url> <commit>: add a submodule at <path> and check out <commit> in it.
# The url is relative to the build directory (`../<entry>.<sub>`), never absolute,
# so .gitmodules and the hashes stay the same on every host. The caller commits the pin.
pin() {
  git -C "$REPO" -c protocol.file.allow=always submodule add -q "$2" "$1"
  git -C "$REPO/$1" checkout -q "$3"
}

# repin <path> <commit>: move a submodule's checkout to <commit>, which advances the pin.
# The caller commits the new pin.
repin() { git -C "$REPO/$1" checkout -q "$2"; }

# hash <label>: the commit a label names, for `pin` and for checking.
hash() { awk -v l="$1" '$1 == l { print $2 }' "$REPO.labels.txt"; }

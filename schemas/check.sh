#!/bin/sh
# Check that the files in schemas/ agree with the schema blocks in SYNTAX.md
# and that schemas/version.yaml agrees with the project's own version.yaml.
#
# Needs POSIX sh, awk, cmp, diff and mktemp. Exits 0 when everything agrees
# and 1 otherwise, naming each file that drifts.
#
#   sh schemas/check.sh          # from the repository root, or from anywhere
#   sh schemas/check.sh --write  # rewrite schemas/*.schema.yaml from SYNTAX.md

set -eu

here=$(cd "$(dirname "$0")" && pwd)
root=$(dirname "$here")
syntax="$root/SYNTAX.md"
write=${1:-}

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT INT TERM

# Extract every fenced YAML block in SYNTAX.md that declares a Tableaux $id
# into $tmp, named by the last segment of that $id. The fence lines stay out;
# every byte between them stays in.
awk -v out="$tmp" '
  /^```yaml$/ && !in_block { in_block = 1; body = ""; name = ""; next }
  /^```$/ && in_block {
    in_block = 0
    if (name != "") {
      if (name !~ /^[a-z]+\.schema\.yaml$/) {
        printf "bad $id in SYNTAX.md: %s\n", name > "/dev/stderr"
        exit 2
      }
      file = out "/" name
      printf "%s", body > file
      close(file)
    }
    next
  }
  in_block {
    body = body $0 "\n"
    if ($1 == "$id:" && $2 ~ /^tableaux\//) { name = $2; sub(/^tableaux\//, "", name) }
  }
' "$syntax"

status=0
found=0

for extracted in "$tmp"/*.schema.yaml; do
  [ -f "$extracted" ] || break
  found=$((found + 1))
  name=$(basename "$extracted")
  file="$here/$name"
  if [ "$write" = --write ]; then
    cp "$extracted" "$file"
    echo "wrote schemas/$name"
  elif [ ! -f "$file" ]; then
    echo "missing: schemas/$name; SYNTAX.md defines it"
    status=1
  elif cmp -s "$extracted" "$file"; then
    echo "ok: schemas/$name"
  else
    echo "drift: schemas/$name differs from SYNTAX.md"
    diff "$file" "$extracted" || true
    status=1
  fi
done

if [ "$found" -eq 0 ]; then
  echo "no schema blocks found in SYNTAX.md"
  exit 1
fi

for file in "$here"/*.schema.yaml; do
  [ -f "$file" ] || break
  name=$(basename "$file")
  if [ ! -f "$tmp/$name" ]; then
    echo "orphan: schemas/$name has no block in SYNTAX.md"
    status=1
  fi
done

# The language version the schemas define must be the version this
# repository's own project follows, since the project dog-foods the language.
version() { awk '$1 == "tableaux:" { v = $2; gsub(/"/, "", v); print v }' "$1"; }
schema_version=$(version "$here/version.yaml")
project_version=$(version "$root/.tableaux/version.yaml")
case $schema_version in
  *.*.*) echo "ok: schemas/version.yaml states $schema_version" ;;
  *) echo "bad: schemas/version.yaml states no major.minor.patch version"; status=1 ;;
esac
if [ "$schema_version" != "$project_version" ]; then
  echo "drift: schemas/version.yaml states $schema_version but .tableaux/version.yaml states $project_version"
  status=1
fi

echo "$found schema files checked"
exit $status

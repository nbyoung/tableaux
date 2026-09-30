# Tableaux schemas

This directory holds the five JSON Schema 2020-12 schemas that [SYNTAX.md](../SYNTAX.md) embeds, as files that tools load. SYNTAX.md is the source; each file here is a byte-for-byte copy of one fenced YAML block there, and a test keeps them equal.

| File                  | Schema for                     | SYNTAX.md section                          |
|-----------------------|--------------------------------|--------------------------------------------|
| `version.schema.yaml` | `.tableaux/version.yaml`       | [`version.yaml`](../SYNTAX.md#versionyaml) |
| `gates.schema.yaml`   | `.tableaux/gates.yaml`         | [`gates.yaml`](../SYNTAX.md#gatesyaml)     |
| `task.schema.yaml`    | `.tableaux/tasks/<id>.yaml`    | [`tasks/<id>.yaml`](../SYNTAX.md#tasksidyaml) |
| `status.schema.yaml`  | `.tableaux/status/<id>.yaml`   | [`status/<id>.yaml`](../SYNTAX.md#statusidyaml) |
| `history.schema.yaml` | The history a tool emits       | [History](../SYNTAX.md#history)            |
| `version.yaml`        | The language version these schemas define | [Version](../README.md#version) |

## How a tool loads them

A tool reads each `*.schema.yaml` file as YAML and hands the resulting mapping to a Draft 2020-12 validator; no conversion to JSON is needed beyond what the YAML parser does. Every `$ref` in the schemas points inside its own file (`#/$defs/...`), so a tool registers no external resources and needs no resolver. The `$id` of each schema is the relative name `tableaux/<file>`, which a tool uses as a key and never fetches.

The schemas use `format` (`email`, `uri-reference`, `date`) as an annotation, as the draft specifies. A tool that wants those formats enforced turns on format assertion in its validator.

A compiled tool embeds this directory and ships it inside its binary; a scripted tool reads it from a checkout.

## How the version check works

`version.yaml` states the version of the Tableaux language that the schemas beside it define. It has the same form as a project's `.tableaux/version.yaml`, so `version.schema.yaml` validates it:

```yaml
tableaux: 0.3.0
```

A tool reads this file when it loads the schemas and compares it with the project's `.tableaux/version.yaml` by the rule in [README.md](../README.md#version): the tool accepts the project when the major versions are equal and the project's minor version does not exceed the schemas' minor version. The patch version does not affect acceptance.

The version lives beside the schemas rather than inside each one so that each schema file stays identical to its block in SYNTAX.md, which carries no version. The trade-off is that a schema file on its own does not say which language version it belongs to; the directory does. This repository dog-foods the language, so the test below also requires `schemas/version.yaml` to equal the repository's own `.tableaux/version.yaml`.

## How to run the test

`check.sh` extracts every fenced YAML block in SYNTAX.md that declares a `$id` under `tableaux/`, names each by the last segment of that `$id`, and compares it byte for byte with the file of that name here. It reports a file that drifts, a file SYNTAX.md defines that is missing here, a file here that SYNTAX.md no longer defines, and a version mismatch, and exits non-zero on any of them. It needs POSIX `sh`, `awk`, `cmp`, `diff` and `mktemp`, and nothing else.

```sh
sh schemas/check.sh          # check
sh schemas/check.sh --write  # rewrite the schema files from SYNTAX.md after editing it
```

`load.py` loads each file as a Draft 2020-12 schema and validates the two `version.yaml` files against `version.schema.yaml`. It needs `python3` with `pyyaml` and `jsonschema`:

```sh
python3 schemas/load.py
```

The workflow [`.github/workflows/schemas.yml`](../.github/workflows/schemas.yml) runs both on every push and pull request.

To change a schema, edit its block in SYNTAX.md, run `sh schemas/check.sh --write`, and commit both.

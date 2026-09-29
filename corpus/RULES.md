# Validator rules

Every rule a validator applies to a Tableaux project, read from [README.md](../README.md) and [SYNTAX.md](../SYNTAX.md). Each rule gives the sentence or schema constraint it comes from, the file it applies to, and the corpus entry that exercises it. A finding in an entry's `expected.yaml` names a rule by its id.

Severity: an **error** makes the project invalid; a **warning** leaves it valid, and a tool reports it. A rule marked **implicit** has no sentence of its own; the method's derivation cannot proceed without it, and the review decides whether the text should state it.

## Project and `version.yaml`

| Id | Severity | Rule                                                                                       | Source                                                                                  | Entry                                        |
|----|----------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------|
| P1 | error    | The project is the `.tableaux` directory at the root of the repository                     | SYNTAX Layout: "A Tableaux project is the `.tableaux` directory at the root of its Git repository." | `no-tableaux-directory`            |
| P2 | error    | `version.yaml` exists                                                                      | SYNTAX Layout table: "`version.yaml`, `gates.yaml`: Fixed"                              | `version-missing`                            |
| P3 | error    | `version.yaml` matches its schema: `tableaux` required, `major.minor.patch`, no other field | SYNTAX version schema                                                                   | `version-bad-pattern`, `version-unknown-field` |
| P4 | error    | The major version equals the tool's and the minor version does not exceed it               | README Version: "A tool accepts a project whose major version equals its own and whose minor version does not exceed it." | `version-major-mismatch`, `version-minor-ahead` |

## `gates.yaml`

| Id  | Severity | Rule                                                                       | Source                                                                           | Entry                          |
|-----|----------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------|
| G1  | error    | `gates.yaml` exists                                                        | SYNTAX Layout table: "`version.yaml`, `gates.yaml`: Fixed"                       | `gates-missing`                |
| G2  | error    | The first gate is `undefined`                                              | README Gates: "The first gate is always `undefined`." Schema `prefixItems`       | `gates-first-not-undefined`    |
| G3  | error    | At least two gates                                                         | Schema `gates: minItems: 2`                                                      | `gates-only-undefined`         |
| G4  | error    | Each gate has `key`, `symbol`, `name`, `criteria`, each non-empty, and no other field | Schema gate item                                                      | `gates-gate-missing-criteria`  |
| G5  | error    | Every key matches `^[a-z][a-z0-9_-]*$`                                     | Schema `$defs/key`                                                               | `gates-bad-key`                |
| G6  | error    | Gate keys are unique                                                       | SYNTAX gates fields: "A unique identifier that other files use to name the gate" | `gates-duplicate-gate`         |
| G7  | error    | `states` exists with at least one state; each has `key`, `symbol`, `severity`, `synopsis` | Schema `required: [gates, states]`, `states: minItems: 1`         | `gates-no-states`              |
| G8  | error    | `severity` is an integer of at least 0                                     | Schema `severity: { type: integer, minimum: 0 }`                                 | `gates-negative-severity`      |
| G9  | error    | State keys are unique                                                      | SYNTAX states fields: "A unique identifier that status records use to name the state" | `gates-duplicate-state`   |
| G10 | error    | Each reason has `key`, `symbol`, `synopsis`; reason keys are unique        | Schema reason item; SYNTAX reasons fields: "A unique identifier"                 | `gates-duplicate-reason`       |
| G11 | error    | No field other than `gates`, `states`, `reasons`                           | Schema `additionalProperties: false`                                             | `gates-unknown-field`          |

## `tasks/<id>.yaml`

| Id  | Severity | Rule                                                                       | Source                                                                                     | Entry                              |
|-----|----------|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|------------------------------------|
| T1  | error    | The file name is four lowercase hexadecimal digits                         | SYNTAX Layout table: "`<id>` is the task id: four lowercase hexadecimal digits chosen at random, `^[0-9a-f]{4}$`" | `task-bad-filename` |
| T2  | error    | `title`, `description` and `assignee` exist and are non-empty              | Schema `required: [title, description, assignee]`                                          | `task-missing-assignee`            |
| T3  | error    | No field beyond the schema's; in particular no `id`                        | SYNTAX tasks: "the file holds no `id` field." Schema `additionalProperties: false`         | `task-id-field`                    |
| T4  | error    | `assignee`, `contributor` and `reviewer` are email addresses               | Schema `$defs/email: format: email`                                                        | `task-bad-email`                   |
| T5  | error    | Each reference has `url`, a URI reference; `text`, when present, is non-empty | Schema `$defs/references`                                                               | `task-reference-without-url`       |
| T6  | error    | Every id a file names matches `^[0-9a-f]{4}$`                              | Schema `$defs/id`                                                                          | `task-bad-id-pattern`              |
| T7  | warning  | An id is written as a quoted string                                        | SYNTAX tasks: "a validator warns of an unquoted id"                                        | `unquoted-id`                      |
| T8  | error    | Exactly one task has no `parent`                                           | README Tasks: "Exactly one task file has no `parent`; it is the **root**"                  | `tree-no-root`, `tree-two-roots`   |
| T9  | error    | Every `parent.id` names a task in the project                              | README Tasks: "Every other task names its parent by id."                                   | `tree-parent-missing`              |
| T10 | error    | Every parent chain ends at the root                                        | README Tasks: "Every parent chain ends at the root."                                       | `tree-parent-cycle`                |
| T11 | error    | `parent` has `id`; `order`, when present, is an integer; no other field    | Schema `parent`                                                                            | `task-parent-order-not-integer`    |

## `requires` in a task file

| Id  | Severity | Rule                                                                       | Source                                                                                     | Entry                                                    |
|-----|----------|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|----------------------------------------------------------|
| R1  | error    | Each `requires[].id` names a task in the project                           | README Tasks: "The **requires** relationship names the tasks whose results this task needs" | `requires-missing-task`                                 |
| R2  | error    | The relation forms no cycle                                                | README Tasks: "The relation crosses the tree freely but forms no cycle"                    | `requires-cycle`                                         |
| R3  | error    | A task does not require itself                                             | README Tasks: "a task never requires itself, an ancestor or a descendant"                  | `requires-self`                                          |
| R4  | error    | A task does not require an ancestor                                        | Same sentence                                                                              | `requires-ancestor`                                      |
| R5  | error    | A task does not require a descendant                                       | Same sentence                                                                              | `requires-descendant`                                    |
| R6  | error    | `from` names a gate in `gates.yaml` that applies to the originating task   | README Tasks: "A validator checks that each gate applies to its task."                     | `requires-from-not-applicable`, `requires-from-unknown-gate` |
| R7  | error    | `to` names a gate in `gates.yaml` that applies to this task                | Same sentence                                                                              | `requires-to-not-applicable`                             |
| R8  | error    | Each entry has `id`; `text`, when present, is non-empty; no other field    | Schema `requires` item                                                                     | `requires-unknown-field`                                 |
| R9  | warning  | A requirement that is due and not met                                      | README Tasks: "A validator warns of an unmet requirement"                                  | `unmet-requirement`; also `weather-station`              |

## `junctions` in a task file

| Id  | Severity         | Rule                                                                       | Source                                                                                     | Entry                                |
|-----|------------------|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------|
| J1  | error            | Every junction key names a gate in `gates.yaml`                            | README Junctions: "A validator checks that every junction key names a gate in `gates.yaml`." | `junction-unknown-gate`            |
| J2  | error            | No not-applicable entry at `undefined`                                     | README Junctions: "The `undefined` gate always applies."                                   | `junction-undefined-not-applicable`  |
| J3  | error            | No recursive junction on a parent                                          | README Junctions: "A recursive junction names one task's work and does not inherit, so a validator rejects one on a parent." | `recursive-on-parent` |
| J4  | error            | An entry is exactly one kind: plain, recursive or not-applicable           | SYNTAX tasks: "`junctions.<gate>` is one of three kinds, told apart by its fields." Schema `oneOf` | `junction-mixed-kind`         |
| J5  | error            | `model` requires `contributor`                                             | Schema `dependentRequired: { model: [contributor] }`                                       | `junction-model-without-contributor` |
| J6  | error            | `applies` is `false`                                                       | Schema `applies: { const: false }`                                                         | `junction-applies-true`              |
| J7  | error            | A recursive entry's `subproject` has `url`; `id`, when present, is an id; no other field | Schema `recursive`                                                          | `junction-subproject-without-url`    |
| J8  | error, implicit  | `subproject.url` resolves to a Tableaux project the tool can read          | README Junctions: "Its `url` locates that project's repository, typically a submodule path" | `subproject-path-missing`           |
| J9  | error, implicit  | `subproject.id`, or that project's root, names a task in the subproject    | README Junctions: "its `id` names the task there, defaulting to that project's root."      | `subproject-task-missing`            |
| J10 | error            | A plain entry has no field beyond `contributor`, `model`, `reviewer`, `references` | Schema `plain: additionalProperties: false`                                        | `junction-unknown-field`             |

## `status/<id>.yaml`

| Id  | Severity         | Rule                                                                       | Source                                                                                     | Entry                                                               |
|-----|------------------|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| S1  | error            | The file name is the id of a task in the project                           | SYNTAX Layout table: "`<id>` is the id of a leaf task"                                     | `status-no-task`                                                    |
| S2  | error            | The task is a leaf                                                         | README Status: "A parent has no file; its status derives from its children."               | `status-on-parent`                                                  |
| S3  | error            | `gate` exists; `note`, when present, is non-empty; no other field          | Schema `required: [gate]`, `additionalProperties: false`                                   | `status-missing-gate`, `status-unknown-field`                       |
| S4  | error            | The gate is `undefined` exactly when the state is `undefined`              | README Status: "The gate is `undefined` exactly when the state is `undefined`." Schema `allOf` | `status-undefined-gate-nominal-state`, `status-nominal-gate-undefined-state` |
| S5  | error            | `gate` names a gate in `gates.yaml`                                        | SYNTAX status fields: "The key of the last gate the task has completed"                    | `status-unknown-gate`                                               |
| S6  | error            | `state` names a state and `reason` names a reason in `gates.yaml`          | SYNTAX status fields: "The key of the task's state"; "The key of a reason from `gates.yaml`" | `status-unknown-state`, `status-unknown-reason`                   |
| S7  | error, implicit  | `gate` applies to the task                                                 | README Junctions: a not-applicable junction "exempts the task from the gate"               | `status-gate-not-applicable`                                        |
| S8  | error            | A task at its last applicable gate has the state `complete`                | README Status: "A task at its last applicable gate has the state `complete`."              | `status-last-gate-not-complete`                                     |
| S9  | error            | When the next junction is recursive, the file holds only the gate          | README Status: "When the next junction is recursive, the file holds only the gate."        | `status-state-with-recursive`                                       |
| S10 | error            | When the next junction is plain, `state` exists                            | SYNTAX status fields: `state` "absent only when the next junction is recursive"            | `status-no-state-plain`                                             |
| S11 | error            | A gate that passes a reviewed junction has a `Reviewed: <id> <gate>` commit by the reviewer in the branch's history | README Status: "A validator rejects a status whose gate passes a reviewed junction that has no such commit." | `status-unreviewed-gate` |

The task brief for this corpus calls S11 a warning; the text says the validator rejects. RULES.md follows the text, and the review decides (question Q1 in [README.md](README.md#questions-for-review)).

## Derived facts, not rules

The audit view reports where files and history disagree. A **proposed** task is such a disagreement, but no sentence makes it a validator finding, so `expected.yaml` carries it as the derived fact `authorisation.state` and not as a finding. The corpus treats **requirement conditions**, **resolved junctions**, **status dates and recorders**, **roll-up** and **events** the same way: a conforming tool must agree on them, and a validator says nothing about them.

## Candidate rules the text does not state

The corpus has no entry for these; the review decides whether the text should state them, and then an entry follows.

| Candidate                                                                                        | Why it matters                                                                                       |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `states` includes `undefined` and `complete`, both with severity 0                                | S4 and S8 name them; roll-up assumes they "step aside", which only severity 0 gives                   |
| At least one gate after `undefined` applies to every task                                        | Otherwise a task has no first applicable gate for a default `to` and its last applicable gate is `undefined` |
| `to` is never `undefined`                                                                         | "defaulting to its first applicable gate after `undefined`" suggests it, and no work needs a result before definition |
| A plain or recursive entry at `undefined`                                                         | J2 covers not-applicable only; whether a contributor at `undefined` means anything is unstated       |
| `complete` appears only at the last applicable gate                                              | S8 gives the converse only                                                                           |
| A trailer names a task and a gate that exist                                                     | `Authorised: zzzz` or `Reviewed: 9f31 nowhere` is silently ignored today                             |
| A `Reviewed:` commit by someone other than the junction's reviewer                               | Ignored today, as the text implies, but an audit could report it                                     |
| Two siblings with the same `order`                                                                | Legal, since id breaks the tie; a tool could warn                                                    |

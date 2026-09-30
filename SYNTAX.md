# Tableaux syntax

This document defines the syntax of each [Tableaux](README.md) file. Each section gives the file's schema (JSON Schema 2020-12, written in YAML), a field summary and an example.

- [Layout](#layout)
- [`version.yaml`](#versionyaml)
- [`gates.yaml`](#gatesyaml)
- [`tasks/<id>.yaml`](#tasksidyaml)
- [`status/<id>.yaml`](#statusidyaml)
- [History](#history)
- [Commit trailers](#commit-trailers)

## Layout

A Tableaux project is the `.tableaux` directory at the root of its Git repository.

```
.tableaux/
├── version.yaml      # the Tableaux version the other files follow
├── gates.yaml        # the gating structure
├── tasks/
│   ├── a1c0.yaml     # one file per task, named by the task id
│   ├── 4e2b.yaml
│   └── …
└── status/
    ├── 9f31.yaml     # one file per leaf task with a status, named by the task id
    └── …
```

| Path                          | Naming                                                                      |
|-------------------------------|-----------------------------------------------------------------------------|
| `.tableaux/`                  | Fixed; one per repository                                                   |
| `version.yaml`, `gates.yaml`  | Fixed                                                                       |
| `tasks/<id>.yaml`             | `<id>` is the task id: four lowercase hexadecimal digits chosen at random, `^[0-9a-f]{4}$` |
| `status/<id>.yaml`            | `<id>` is the id of a leaf task                                             |

History has no file: a tool derives it from the Git log (see [History](#history)).

## `version.yaml`

The version file states the Tableaux language version that the other files follow, and names the trunk.

### Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: tableaux/version.schema.yaml
type: object
required: [tableaux]
additionalProperties: false
properties:
  tableaux:
    type: string
    pattern: "^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)$"
  trunk:
    type: string
    minLength: 1
```

### Fields

| Field      | Required | Meaning                                                          |
|------------|----------|------------------------------------------------------------------|
| `tableaux` | Yes      | The semantic version (`major.minor.patch`) of the Tableaux language |
| `trunk`    | No       | The branch on which the project accepts tasks and statuses; defaults to the remote's default branch ([README.md](README.md#project)) |

### Example

```yaml
tableaux: 0.2.1
trunk: main
```

## `gates.yaml`

The gating file defines the ordered gates every task passes through, the states a task takes at its current gate, and the reasons that explain a state.

### Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: tableaux/gates.schema.yaml
type: object
required: [gates, states]
additionalProperties: false
$defs:
  key:
    type: string
    pattern: "^[a-z][a-z0-9_-]*$"
  symbol:
    type: string
    minLength: 1
properties:
  gates:
    type: array
    minItems: 2
    prefixItems:
      - properties: { key: { const: undefined } }
    items:
      type: object
      required: [key, symbol, name, criteria]
      additionalProperties: false
      properties:
        key:      { $ref: "#/$defs/key" }
        symbol:   { $ref: "#/$defs/symbol" }
        name:     { type: string, minLength: 1 }
        criteria: { type: string, minLength: 1 }
  states:
    type: array
    minItems: 2
    allOf:
      - contains: { properties: { key: { const: undefined }, severity: { const: 0 } } }
      - contains: { properties: { key: { const: complete },  severity: { const: 0 } } }
    items:
      type: object
      required: [key, symbol, severity, synopsis]
      additionalProperties: false
      properties:
        key:      { $ref: "#/$defs/key" }
        symbol:   { $ref: "#/$defs/symbol" }
        severity: { type: integer, minimum: 0 }
        synopsis: { type: string, minLength: 1 }
  reasons:
    type: array
    items:
      type: object
      required: [key, symbol, synopsis]
      additionalProperties: false
      properties:
        key:      { $ref: "#/$defs/key" }
        symbol:   { $ref: "#/$defs/symbol" }
        synopsis: { type: string, minLength: 1 }
```

### Fields

`gates` (required) lists the gates in the order tasks pass through them. The first gate is always `undefined`.

| Field      | Required | Meaning                                                           |
|------------|----------|-------------------------------------------------------------------|
| `key`      | Yes      | A unique identifier that other files use to name the gate         |
| `symbol`   | Yes      | The emoji that labels the gate's column in a view                 |
| `name`     | Yes      | The gate's human-readable name                                    |
| `criteria` | Yes      | The conditions a task meets to complete the gate                  |

`states` (required) lists the states a task takes with respect to its current gate. It always includes `undefined`, the state at the `undefined` gate, and `complete`, the state at the last applicable gate, both with severity `0`.

| Field      | Required | Meaning                                                                          |
|------------|----------|----------------------------------------------------------------------------------|
| `key`      | Yes      | A unique identifier that status records use to name the state                    |
| `symbol`   | Yes      | The emoji a view shows in the task's current gate cell                           |
| `severity` | Yes      | The state's rank in roll-up; the higher value prevails. `0` marks a state that roll-up sets aside |
| `synopsis` | Yes      | A one-line description of the state                                              |

`reasons` (optional) lists the reasons that supplement a task's state, typically for the `at_risk` and `stalled` states.

| Field      | Required | Meaning                                                          |
|------------|----------|------------------------------------------------------------------|
| `key`      | Yes      | A unique identifier that status records use to name the reason   |
| `symbol`   | Yes      | The emoji a view shows beside the state symbol                   |
| `synopsis` | Yes      | A one-line description of the reason                             |

### Example

```yaml
# gates.yaml — the gating structure
gates:
  - { key: undefined,      symbol: ❔, name: Undefined,             criteria: No one has started work on the definition }
  - { key: defined,        symbol: 📝, name: Defined,               criteria: "Title, description, assignee and references exist" }
  - { key: mockup,         symbol: 📌, name: Mockup,                criteria: A non-technical mockup of the outcome exists }
  - { key: function,       symbol: ⚙️, name: Functional prototype,  criteria: A technical demonstration of function exists }
  - { key: performance,    symbol: ⚡, name: Performance prototype, criteria: Target performance shown in the deliverable's technology }
  - { key: reliability,    symbol: ⚓, name: Reliability prototype, criteria: Target reliability shown in the fundamental technology }
  - { key: design,         symbol: 📐, name: Design,                criteria: A model and sufficient tests exist }
  - { key: implementation, symbol: 🛠️, name: Implementation,        criteria: "Artifacts suffice for unit, integration and validation tests" }
  - { key: unit,           symbol: 🧩, name: Unit test,             criteria: All prescribed tests pass }
  - { key: integrate,      symbol: 🖼️, name: Integration,           criteria: Assembled with neighbouring components }
  - { key: validate,       symbol: 🌍, name: Validation,            criteria: Passes user and field tests }
  - { key: release,        symbol: 🚀, name: Release,               criteria: All variants documented and approved }

states:
  - { key: undefined, symbol: ⚪, severity: 0, synopsis: The work has not yet been defined }
  - { key: nominal,   symbol: 🟢, severity: 1, synopsis: The work is proceeding as expected }
  - { key: at_risk,   symbol: 🟡, severity: 2, synopsis: The work is at risk of stalling }
  - { key: stalled,   symbol: 🔴, severity: 3, synopsis: Practically all progress has stalled }
  - { key: complete,  symbol: ✅, severity: 0, synopsis: All deliverables satisfy their requirements }

reasons:
  - { key: overloaded, symbol: 🪫, synopsis: The assigned resource is overloaded }
  - { key: blocked,    symbol: ⛔, synopsis: An external resource is unavailable }
```

## `tasks/<id>.yaml`

A task file defines one task and its junctions. The file name carries the task's id; the file holds no `id` field.

An id is four lowercase hexadecimal digits chosen at random when the task is created. Wherever a file names an id, in `parent`, `requires` or `subproject`, it writes the id as a quoted string, because YAML reads an id such as `1000` as an integer and `1e10` as a float. A tool takes an id as a string whatever scalar YAML yields, and a validator warns of an unquoted id.

### Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: tableaux/task.schema.yaml
type: object
required: [title, description, assignee]
additionalProperties: false
$defs:
  id:
    type: string
    pattern: "^[0-9a-f]{4}$"
  key:
    type: string
    pattern: "^[a-z][a-z0-9_-]*$"
  email:
    type: string
    format: email
  url:
    type: string
    format: uri-reference
    minLength: 1
  references:
    type: array
    items:
      type: object
      required: [url]
      additionalProperties: false
      properties:
        url:  { $ref: "#/$defs/url" }
        text: { type: string, minLength: 1 }
  junction:
    oneOf:
      - $ref: "#/$defs/plain"
      - $ref: "#/$defs/recursive"
      - $ref: "#/$defs/not_applicable"
  plain:
    type: object
    additionalProperties: false
    dependentRequired: { model: [contributor] }
    properties:
      contributor: { $ref: "#/$defs/email" }
      model:       { type: string, minLength: 1 }
      reviewer:    { $ref: "#/$defs/email" }
      references:  { $ref: "#/$defs/references" }
  recursive:
    type: object
    required: [subproject]
    additionalProperties: false
    properties:
      subproject:
        type: object
        required: [url]
        additionalProperties: false
        properties:
          url: { $ref: "#/$defs/url" }
          id:  { $ref: "#/$defs/id" }
  not_applicable:
    type: object
    required: [applies]
    additionalProperties: false
    properties:
      applies: { const: false }
properties:
  title:       { type: string, minLength: 1 }
  description: { type: string, minLength: 1 }
  assignee:    { $ref: "#/$defs/email" }
  references:  { $ref: "#/$defs/references" }
  requires:
    type: array
    items:
      type: object
      required: [id]
      additionalProperties: false
      properties:
        id:   { $ref: "#/$defs/id" }
        from: { $ref: "#/$defs/key" }
        to:   { $ref: "#/$defs/key" }
        text: { type: string, minLength: 1 }
  junctions:
    type: object
    propertyNames:
      allOf:
        - $ref: "#/$defs/key"
        - not: { const: undefined }
    additionalProperties: { $ref: "#/$defs/junction" }
  parent:
    type: object
    required: [id]
    additionalProperties: false
    properties:
      id:    { $ref: "#/$defs/id" }
      order: { type: integer, minimum: 1 }
```

### Fields

| Field         | Required | Meaning                                                                          |
|---------------|----------|----------------------------------------------------------------------------------|
| `title`       | Yes      | A brief synopsis of the activity or deliverable                                  |
| `description` | Yes      | The task's outcome and scope, in prose                                           |
| `assignee`    | Yes      | The responsible person's email address, as it appears in their Git commits       |
| `references`  | No       | Links that expand the task                                                       |
| `requires`    | No       | Tasks whose results this task needs                                              |
| `junctions`   | No       | Per-gate detail, keyed by gate key other than `undefined`; a gate absent here takes the plain default |
| `parent`      | No       | The task's place in the tree; absent only on the root task                       |

`references[]`

| Field  | Required | Meaning                                                                          |
|--------|----------|----------------------------------------------------------------------------------|
| `url`  | Yes      | An absolute URL, or a path relative to the repository root                       |
| `text` | No       | The text a view displays for the link; defaults to `url`                         |

`requires[]`

| Field  | Required | Meaning                                                                          |
|--------|----------|----------------------------------------------------------------------------------|
| `id`   | Yes      | The id of the originating task, whose result this task needs                    |
| `from` | No       | The originating gate: the gate the originating task must have completed; defaults to its last applicable gate |
| `to`   | No       | The terminating gate: the gate of this task whose work needs the result; defaults to its first applicable gate after `undefined` |
| `text` | No       | A summary of what passes from the originating task to this one                   |

`junctions.<gate>` is one of three kinds, told apart by its fields.

| Kind           | Field         | Required | Meaning                                                                    |
|----------------|---------------|----------|----------------------------------------------------------------------------|
| Plain          | `contributor` | No       | The email address of who does the work at this gate; defaults to `assignee` |
|                | `model`       | No       | The model the contributor should run, when the contributor is an agent: an identifier or a prefix of one; stated together with `contributor`, never alone, since a model names no one |
|                | `reviewer`    | No       | The email address of the person who accepts the work at this gate          |
|                | `references`  | No       | Links that expand the gate's criteria for this task; same form as the task's |
| Recursive      | `subproject`  | Yes      | The project that does the work: `url` locates its repository, an absolute URL or a path relative to this repository's root; `id` names its task, defaulting to that project's root |
| Not applicable | `applies`     | Yes      | Always `false`; the entry's presence exempts the gate, and `true` would restate the default the file omits |

`parent`

| Field   | Required | Meaning                                                                          |
|---------|----------|----------------------------------------------------------------------------------|
| `id`    | Yes      | The id of the parent task                                                        |
| `order` | No       | The task's rank among its siblings, a strictly positive integer; lower sorts first |

### Examples

```yaml
# tasks/a1c0.yaml — the root task
title: Weather station
description: >
  A solar-powered sensor node, a gateway that stores its readings,
  and a dashboard, mounted on a mast at the allotment.
assignee: ada@example.org
references:
  - { url: docs/overview.md, text: Project overview }
```

```yaml
# tasks/9f31.yaml — a leaf task
title: Sensor board
description: >
  The PCB that carries the barometer, hygrometer and thermometer
  and powers them from the solar cell within the power budget.
assignee: ada@example.org
references:
  - { url: docs/sensor-board.md }
  - { url: https://example.org/datasheets/bmp390.pdf, text: Barometer datasheet }
junctions:
  performance: { references: [{ url: docs/sensor-board.md#power-budget, text: Power budget }] }
  validate:    { reviewer: ben@example.org }
parent: { id: "4e2b", order: 1 }
```

```yaml
# tasks/c07d.yaml — a leaf task that requires another and shows every junction kind
title: Node firmware
description: Reads the sensors, sleeps between readings and publishes to the gateway.
assignee: ben@example.org
requires:
  - { id: "9f31", from: design, to: implementation, text: Pin map and sensor bus }
junctions:
  reliability:    { applies: false }
  implementation: { subproject: { url: firmware, id: "f1a0" } }
  unit:           { contributor: opus@example.org, model: claude-opus-5-5 }
parent: { id: "4e2b", order: 2 }
```

## `status/<id>.yaml`

A status file records the current status of one leaf task. The file name carries the task's id.

### Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: tableaux/status.schema.yaml
type: object
required: [gate]
additionalProperties: false
$defs:
  key:
    type: string
    pattern: "^[a-z][a-z0-9_-]*$"
properties:
  gate:   { $ref: "#/$defs/key" }
  state:  { $ref: "#/$defs/key" }
  reason: { $ref: "#/$defs/key" }
  note:   { type: string, minLength: 1 }
allOf:
  - if:   { properties: { gate: { const: undefined } } }
    then: { required: [state], properties: { state: { const: undefined } } }
  - if:   { required: [state], properties: { state: { const: undefined } } }
    then: { properties: { gate: { const: undefined } } }
```

### Fields

| Field    | Required | Meaning                                                                          |
|----------|----------|----------------------------------------------------------------------------------|
| `gate`   | Yes      | The key of the last gate the task has completed; `undefined` when none           |
| `state`  | No       | The key of the task's state towards its next gate; absent only when the next junction is recursive |
| `reason` | No       | The key of a reason from `gates.yaml` that explains the state                    |
| `note`   | No       | A brief remark on the status                                                     |

The file holds no date and no recorder: Git supplies both (see [README.md](README.md#status)).

### Examples

```yaml
# status/9f31.yaml
gate: function
state: stalled
reason: blocked
note: Barometer ICs on 14-week backorder
```

```yaml
# status/c07d.yaml — the next junction, implementation, is recursive
gate: design
```

## History

A history is the sequence of events that Git records for one task, or for the whole project, in author-time order. A tool derives it from the log and emits it in the form below; nothing stores it.

### Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: tableaux/history.schema.yaml
type: array
items:
  type: object
  required: [date, commit, by, task, event]
  additionalProperties: false
  properties:
    date:   { type: string, format: date }
    commit: { type: string, pattern: "^[0-9a-f]{7,40}$" }
    by:     { type: string, format: email }
    task:   { type: string, pattern: "^[0-9a-f]{4}$" }
    event:  { enum: [task, authorised, status, reaffirmed, reviewed] }
    gate:   { type: string, pattern: "^[a-z][a-z0-9_-]*$" }
    state:  { type: string, pattern: "^[a-z][a-z0-9_-]*$" }
    reason: { type: string, pattern: "^[a-z][a-z0-9_-]*$" }
    note:   { type: string, minLength: 1 }
```

### Fields

| Field    | Required | Meaning                                                                          |
|----------|----------|----------------------------------------------------------------------------------|
| `date`   | Yes      | The commit's author date                                                         |
| `commit` | Yes      | The commit's abbreviated or full hash                                            |
| `by`     | Yes      | The commit's author email address                                                |
| `task`   | Yes      | The task the event concerns, as a quoted string                                  |
| `event`  | Yes      | What the commit did to the task (see the table below)                            |
| `gate`   | No       | For `status`, the gate recorded; for `reviewed`, the gate accepted               |
| `state`, `reason`, `note` | No | For `status`, the values recorded                                        |

| Event        | Source in the commit                                     |
|--------------|----------------------------------------------------------|
| `task`       | A change to `tasks/<id>.yaml`                            |
| `authorised` | An `Authorised: <id>` trailer                            |
| `status`     | A change to `status/<id>.yaml`                           |
| `reaffirmed` | A `Reaffirmed: <id>` trailer                             |
| `reviewed`   | A `Reviewed: <id> <gate>` trailer                        |

### Example

```yaml
- { date: 2026-09-18, commit: 3e1f0a2, by: ada@example.org, task: "9f31", event: task }
- { date: 2026-09-19, commit: 8c44b7d, by: ada@example.org, task: "9f31", event: authorised }
- { date: 2026-09-22, commit: b02e9c1, by: ada@example.org, task: "9f31", event: status, gate: mockup, state: nominal }
- { date: 2026-09-24, commit: 5d7a3f8, by: ben@example.org, task: "9f31", event: reviewed, gate: mockup }
- { date: 2026-09-25, commit: e91c604, by: ada@example.org, task: "9f31", event: status, gate: function, state: stalled, reason: blocked, note: Barometer ICs on 14-week backorder }
- { date: 2026-09-28, commit: 71bd2e5, by: ada@example.org, task: "9f31", event: reaffirmed }
```

## Commit trailers

A commit message may carry the trailers below, one task per line, among its other trailers. A task trailer names a task in the project and, for `Reviewed:`, a gate in `gates.yaml` that applies to that task; a validator warns of a trailer that names neither, since Git keeps it and the method cannot read it. `Model:` names no task: it records what ran, beside the `Co-Authored-By:` trailer an agent leaves when it commits under a person's identity, and a tool reads the two together to see agent work whoever the author is.

| Trailer                  | Meaning                                                              |
|--------------------------|----------------------------------------------------------------------|
| `Authorised: <id>`       | The committer, as one of the task's authorities, accepts it as it stands |
| `Reviewed: <id> <gate>`  | The committer accepts the task's work at the gate                    |
| `Reaffirmed: <id>`       | The committer confirms the task's status as it stands, on this date  |
| `Model: <identifier>`    | The model the agent that made this commit ran, as the harness reports it; it names no task |

Example:

```
Accept the sensor board and node firmware tasks

Authorised: 9f31
Authorised: c07d
Reviewed: 9f31 design
```

```
Record the node firmware at its unit gate

Reviewed: c07d unit
Model: claude-fable-5-1
Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
```

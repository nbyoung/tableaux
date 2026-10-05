# Gate definition

**What do the columns and symbols mean?** This file is the legend of the Tableaux tooling plan, and every other view links here: [tableau](tableau.md), [context](context.md), [queue](queue.md), [blockage](blockage.md), [task](task.md), [assignment](assignment.md), [authority](authority.md), [history](history.md), [audit](audit.md).

Parameters: ref `main` at `3cdae52`, 2026-10-05 · task: none, the project-wide legend, then `e9c6` once · columns: all ten gates, and a window or a column list shows those gates only · level: one section per level below.

A rendering holds one level. Its headings are Gates, States, Reasons and Junction marks at every level, so a link to `gates.md#gates`, `gates.md#states`, `gates.md#reasons` or `gates.md#junction-marks` resolves whichever level CI fixes.

## Glance

`tabloio gates --ref 3cdae52 --level glance`

### Gates

A tableau shows one column per gate, in this order, under the gate's symbol.

| #  | Symbol | Gate                 | Key              |
|---:|:------:|----------------------|------------------|
| 1  | ❔     | Undefined            | `undefined`      |
| 2  | 📝     | Defined              | `defined`        |
| 3  | 📌     | Mockup               | `mockup`         |
| 4  | 🔧     | Functional prototype | `function`       |
| 5  | 📐     | Design               | `design`         |
| 6  | 🧱     | Implementation       | `implementation` |
| 7  | 📏     | Unit test            | `unit`           |
| 8  | 🔗     | Integration          | `integrate`      |
| 9  | 🌍     | Validation           | `validate`       |
| 10 | 🚀     | Release              | `release`        |

### States

| Symbol | State       |
|:------:|-------------|
| ⚪     | `undefined` |
| 🟢     | `nominal`   |
| 🟡     | `at_risk`   |
| 🔴     | `stalled`   |
| ✅     | `complete`  |

### Reasons

| Symbol | Reason       |
|:------:|--------------|
| 🪫     | `overloaded` |
| ⛔     | `blocked`    |
| 👓     | `review`     |

### Junction marks

| Mark | Meaning                    |
|:----:|----------------------------|
| 🧑   | A person contributes       |
| 🤖   | An agent contributes       |
| 👀   | A reviewer accepts         |
| 🪆   | A subproject does the work |
| —    | The gate does not apply    |

## Detail

`tabloio gates --ref 3cdae52 --level detail`

### Gates

A tableau shows one column per gate, in this order, under the gate's symbol. A task's status names the gate the task has last completed.

| #  | Symbol | Gate                 | Key              | Criteria                                                     |
|---:|:------:|----------------------|------------------|--------------------------------------------------------------|
| 1  | ❔     | Undefined            | `undefined`      | No one has started work on the definition                    |
| 2  | 📝     | Defined              | `defined`        | Title, description, assignee and references exist            |
| 3  | 📌     | Mockup               | `mockup`         | A non-technical mockup of the outcome exists                 |
| 4  | 🔧     | Functional prototype | `function`       | A technical demonstration of function exists                 |
| 5  | 📐     | Design               | `design`         | A model and sufficient tests exist                           |
| 6  | 🧱     | Implementation       | `implementation` | Artifacts suffice for unit, integration and validation tests |
| 7  | 📏     | Unit test            | `unit`           | All prescribed tests pass                                    |
| 8  | 🔗     | Integration          | `integrate`      | Assembled with neighbouring components                       |
| 9  | 🌍     | Validation           | `validate`       | Passes user and field tests                                  |
| 10 | 🚀     | Release              | `release`        | All variants documented and approved                         |

### States

A state says how a task stands towards its next gate. A parent takes the state of its most severe child, and a state of severity 0 steps aside.

| Symbol | State       | Severity | Synopsis                                    |
|:------:|-------------|---------:|---------------------------------------------|
| ⚪     | `undefined` | 0        | The work has not yet been defined           |
| 🟢     | `nominal`   | 1        | The work is proceeding as expected          |
| 🟡     | `at_risk`   | 2        | The work is at risk of stalling             |
| 🔴     | `stalled`   | 3        | Practically all progress has stalled        |
| ✅     | `complete`  | 0        | All deliverables satisfy their requirements |

### Reasons

A reason explains a state, and its symbol stands beside the state's symbol.

| Symbol | Reason       | Synopsis                            |
|:------:|--------------|-------------------------------------|
| 🪫     | `overloaded` | The assigned resource is overloaded |
| ⛔     | `blocked`    | An external resource is unavailable |
| 👓     | `review`     | The work waits for its reviewer     |

The method reserves `review`: the contributor has handed the next junction's work to its reviewer, and the [queue](queue.md) lists the review as owed. 👓 beside a state says the work waits for its reviewer; 👀 in a cell says a reviewer accepts the work there.

### Junction marks

A junction is the meeting of a task and a gate, one cell of a tableau. The marks belong to the method, not to this project.

| Mark | Meaning                    | Junction                                                     |
|:----:|----------------------------|--------------------------------------------------------------|
| 🧑   | A person contributes       | Plain; the contributor is a person                           |
| 🤖   | An agent contributes       | Plain; the junction states a `model`                         |
| 👀   | A reviewer accepts         | Plain; the reviewer accepts the work at the gate             |
| 🪆   | A subproject does the work | Recursive; another Tableaux project does the work            |
| —    | The gate does not apply    | Not applicable; the entry exempts the task from the gate     |

## Provenance

`tabloio gates --ref 3cdae52 --level provenance`

### Gates

A tableau shows one column per gate, in this order, under the gate's symbol. A task's status names the gate the task has last completed.

| #  | Symbol | Gate                 | Key              | Criteria                                                     |
|---:|:------:|----------------------|------------------|--------------------------------------------------------------|
| 1  | ❔     | Undefined            | `undefined`      | No one has started work on the definition                    |
| 2  | 📝     | Defined              | `defined`        | Title, description, assignee and references exist            |
| 3  | 📌     | Mockup               | `mockup`         | A non-technical mockup of the outcome exists                 |
| 4  | 🔧     | Functional prototype | `function`       | A technical demonstration of function exists                 |
| 5  | 📐     | Design               | `design`         | A model and sufficient tests exist                           |
| 6  | 🧱     | Implementation       | `implementation` | Artifacts suffice for unit, integration and validation tests |
| 7  | 📏     | Unit test            | `unit`           | All prescribed tests pass                                    |
| 8  | 🔗     | Integration          | `integrate`      | Assembled with neighbouring components                       |
| 9  | 🌍     | Validation           | `validate`       | Passes user and field tests                                  |
| 10 | 🚀     | Release              | `release`        | All variants documented and approved                         |

Source: `gates` in `.tableaux/gates.yaml`.

### States

A state says how a task stands towards its next gate. A parent takes the state of its most severe child, and a state of severity 0 steps aside.

| Symbol | State       | Severity | Synopsis                                    |
|:------:|-------------|---------:|---------------------------------------------|
| ⚪     | `undefined` | 0        | The work has not yet been defined           |
| 🟢     | `nominal`   | 1        | The work is proceeding as expected          |
| 🟡     | `at_risk`   | 2        | The work is at risk of stalling             |
| 🔴     | `stalled`   | 3        | Practically all progress has stalled        |
| ✅     | `complete`  | 0        | All deliverables satisfy their requirements |

Source: `states` in `.tableaux/gates.yaml`.

### Reasons

A reason explains a state, and its symbol stands beside the state's symbol.

| Symbol | Reason       | Synopsis                            |
|:------:|--------------|-------------------------------------|
| 🪫     | `overloaded` | The assigned resource is overloaded |
| ⛔     | `blocked`    | An external resource is unavailable |
| 👓     | `review`     | The work waits for its reviewer     |

The method reserves `review`: the contributor has handed the next junction's work to its reviewer, and the [queue](queue.md) lists the review as owed. 👓 beside a state says the work waits for its reviewer; 👀 in a cell says a reviewer accepts the work there.

Source: `reasons` in `.tableaux/gates.yaml`; the reserved meaning of `review` in `README.md`, Gates.

### Junction marks

A junction is the meeting of a task and a gate, one cell of a tableau. The marks belong to the method, not to this project.

| Mark | Meaning                    | Junction                                                     |
|:----:|----------------------------|--------------------------------------------------------------|
| 🧑   | A person contributes       | Plain; the contributor is a person                           |
| 🤖   | An agent contributes       | Plain; the junction states a `model`                         |
| 👀   | A reviewer accepts         | Plain; the reviewer accepts the work at the gate             |
| 🪆   | A subproject does the work | Recursive; another Tableaux project does the work            |
| —    | The gate does not apply    | Not applicable; the entry exempts the task from the gate     |

Source: `README.md`, Junctions, at language 0.3.1; no project file states the marks.

### Provenance

| Fact             | Value   | Source                               |
|------------------|---------|--------------------------------------|
| Language version | 0.3.1   | `tableaux` in `.tableaux/version.yaml` |
| Trunk            | `main`  | `trunk` in `.tableaux/version.yaml`  |
| Ref              | `3cdae52`, 2026-10-05, on the trunk | The `--ref` parameter |

| File                     | Last changed by | Date       | Author                                  | Committer                               | Subject                                                      |
|--------------------------|-----------------|------------|-----------------------------------------|-----------------------------------------|--------------------------------------------------------------|
| `.tableaux/gates.yaml`   | `e91ba68`       | 2026-10-02 | Claude Opus 5.5, noreply@anthropic.com  | Claude Opus 5.5, noreply@anthropic.com  | Mark four gates with symbols that need no variation selector |
| `.tableaux/version.yaml` | `d95294b`       | 2026-09-30 | Claude Fable 5.1, noreply@anthropic.com | Claude Fable 5.1, noreply@anthropic.com | Raise the language to 0.3.1                                  |

Reproduce:

```
git show 3cdae52:.tableaux/gates.yaml
git show 3cdae52:.tableaux/version.yaml
git log -1 --format='%h %as %an <%ae> / %cn <%ce> %s' 3cdae52 -- .tableaux/gates.yaml
git log -1 --format='%h %as %an <%ae> / %cn <%ce> %s' 3cdae52 -- .tableaux/version.yaml
```

## Detail for one task

`tabloio gates --ref 3cdae52 --task e9c6 --level detail`

The task parameter adds one fact to each gate: how the junction of that task at the gate expands the criteria. This rendering takes `e9c6` Abstract views, a task under the Method branch `bc63`. The States, Reasons and Junction marks sections do not change with the task and follow as in Detail above.

### Gates

| #  | Symbol | Gate                 | Key              | Criteria                                                     | For `e9c6`                      |
|---:|:------:|----------------------|------------------|--------------------------------------------------------------|---------------------------------|
| 1  | ❔     | Undefined            | `undefined`      | No one has started work on the definition                    | Applies; no reference           |
| 2  | 📝     | Defined              | `defined`        | Title, description, assignee and references exist            | Applies; no reference           |
| 3  | 📌     | Mockup               | `mockup`         | A non-technical mockup of the outcome exists                 | — The gate does not apply       |
| 4  | 🔧     | Functional prototype | `function`       | A technical demonstration of function exists                 | — The gate does not apply       |
| 5  | 📐     | Design               | `design`         | A model and sufficient tests exist                           | Applies; no reference           |
| 6  | 🧱     | Implementation       | `implementation` | Artifacts suffice for unit, integration and validation tests | Applies; no reference           |
| 7  | 📏     | Unit test            | `unit`           | All prescribed tests pass                                    | — The gate does not apply       |
| 8  | 🔗     | Integration          | `integrate`      | Assembled with neighbouring components                       | — The gate does not apply       |
| 9  | 🌍     | Validation           | `validate`       | Passes user and field tests                                  | Applies; no reference           |
| 10 | 🚀     | Release              | `release`        | All variants documented and approved                         | Applies; no reference           |

No junction of `e9c6` states a reference, and no junction of its ancestors `2034`, `bc63` and `437e` does, so each of the six gates that apply reads by its criteria alone. No task of this project states a junction reference at this ref. The Method branch `bc63` says how specification work reads the gates in its description, not in a junction reference, and the [task](task.md) view shows that description.

`--level provenance` adds the file behind each line: `.tableaux/tasks/e9c6.yaml` states the four not-applicable entries itself, and `6b6c99a`, 2026-09-29, by Norman Young, nbyoung@nbyoung.com, as author and committer, last changed that file.

### Illustration: a gate with a reference

This example is not this project. It shows the form of a gate that a junction reference expands, with the one junction reference the repository holds: the conformance corpus entry `weather-station`, task `9f31` Sensor board, at the `performance` gate of the gate set `SYNTAX.md` shows.

| Symbol | Gate                  | Key           | Criteria                                                 | For `9f31`                                                                  |
|:------:|-----------------------|---------------|----------------------------------------------------------|-----------------------------------------------------------------------------|
| ⚡     | Performance prototype | `performance` | Target performance shown in the deliverable's technology | Applies; reference: Power budget, `docs/sensor-board.md#power-budget`, stated by `9f31` |

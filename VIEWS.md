# Tableaux views

A view is what a Tableaux tool shows. This document defines each view once, independently of any format: the question it answers, the roles it serves, the data it draws from the project and the history, the parameters that focus it, and the levels at which it discloses. [PLAN.md](PLAN.md#views) proposes the views, the mockups under `docs/mockups/` give each a form in Markdown and in HTML, `tablo` derives each as data, and each front end renders it. [README.md](README.md) gives the meaning of every term this document uses, and [README.md#roles](README.md#roles) the roles.

Every example comes from this project's own plan as it stands on `main` at commit `1b6916e`, 2026-09-30, before this design's hand-off, so that the owner reviews the design against work they know. An example shows content, not form; the mockups fix the form.

- [What every view shares](#what-every-view-shares)
- [Gate definition](#gate-definition)
- [Task definition](#task-definition)
- [Authority delegation](#authority-delegation)
- [Task assignment](#task-assignment)
- [Contributor work queue](#contributor-work-queue)
- [Work-blockage tree](#work-blockage-tree)
- [Global tableau](#global-tableau)
- [Contextual tableau](#contextual-tableau)
- [History](#history)
- [Audit](#audit)
- [Decisions at review](#decisions-at-review)
- [Findings about the method](#findings-about-the-method)

## What every view shares

### Data

A view shows nothing a tool does not derive from the project files and the Git history. The table names each derived fact once; each view then lists the facts it draws from, `tablo` derives each fact once, and the corpus fixes the same facts per entry in `expected.yaml`.

| Fact                   | Content                                                                                                   | Defined in                                                                 |
|------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Gates                  | The gates, states and reasons in order, with symbols, criteria, severities and synopses; the reserved reason `review` | [README.md#gates](README.md#gates)                               |
| Tree                   | The root, each task's parent and children, in display order: `order` ascending, then id                   | [README.md#tasks](README.md#tasks)                                          |
| Authorities            | The assignees of a task's ancestors, nearest first                                                        | [README.md#tasks](README.md#tasks)                                          |
| Resolved junctions     | Each task's junction at each gate: its kind and fields, and for each field the task whose entry supplies it, or the plain default | [README.md#junctions](README.md#junctions)                    |
| Applicable gates       | The gates a task passes through, and its first and last applicable gate                                   | [README.md#junctions](README.md#junctions)                                  |
| Requirement conditions | Each `requires` entry, local by `id` or cross-project by `subproject` with `url`, `id` and `commit`, with `from` and `to` resolved and its condition: met, due, unmet; a cross-project entry reads its originating task at the commit the linkage fixes; and the reverse relation, the tasks that require a given task, called its dependents here | [README.md#tasks](README.md#tasks) |
| Authorisation          | Authorised or proposed, the deciding commit, and whether its author or its committer is the authority     | [README.md#proposed-and-authorised-tasks](README.md#proposed-and-authorised-tasks) |
| Status                 | A leaf's gate, state, reason and note, with the date and recorder its deciding commit gives; a leaf without a file at `undefined` | [README.md#status](README.md#status)                        |
| Reviews                | For each reviewed junction the status passes, the `Reviewed:` commit that accepts it                      | [README.md#status](README.md#status)                                        |
| Roll-up                | A parent's derived status and the child it comes from; a tie breaks by display order                      | [README.md#status](README.md#status)                                        |
| Subproject snapshot    | For a recursive junction, the subproject task read at the commit its `url` fixes: a submodule's pin, the parent's own commit for a same-repository path, or the stated `commit` for an absolute URL | [README.md#junctions](README.md#junctions) |
| Events                 | The history: task, authorised, status, reaffirmed, reviewed and pin events, each with its date, commit and actor; a pin event names the `url` and the old and new commit | [README.md#history](README.md#history), [SYNTAX.md#history](SYNTAX.md#history) |
| Models                 | The `Model:` trailer on each commit at a junction, against the model the junction states                  | [SYNTAX.md#commit-trailers](SYNTAX.md#commit-trailers)                      |
| Findings               | What a validator reports, by rule                                                                         | [corpus/RULES.md](corpus/RULES.md)                                          |

### Parameters

The views share one set of parameters. Each view's section says which apply to it and what its default is; a parameter a view does not name is a usage error on that view, so a mistyped option never passes for a default.

| Parameter            | Focuses                                                                                                                                       | Default                                                     |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| task                 | One task, or the subtree under it                                                                                                             | The root                                                    |
| person               | One email: the tasks, junctions and commits in which it appears                                                                               | The viewer on the work queue and on the contextual tableau without a task; nobody elsewhere, so the view shows everyone and marks no one |
| window or columns    | The gate columns a tableau shows: a window of *n* columns either side of the next gates of the tasks in view, or an explicit list; the columns outside fold to a count | A window of one                              |
| historical junctions | Whether a tableau shows the junction marks of a task's historical junctions                                                                   | False                                                       |
| ref, or a range      | The commit whose files and history are in view; a range bounds the history                                                                    | The working tree's files on the history of `HEAD`, so an edit shows before its commit, and `HEAD` names the committed state; authorisation always reads the trunk |
| role                 | The role whose level the view opens at                                                                                                        | The viewer's role at each item                              |
| level                | The level, overriding the role's                                                                                                              | —                                                           |

The **viewer** is whoever runs the tool, identified by the email Git would commit with. An agent that runs inside a person's session shares that person's email, so a dispatcher names the agent by `person`. An observer has no email in the project and sees every view at glance.

A task's **historical junctions** are its junctions at every gate before the gate its status names, applicable or not; for a parent, before its derived gate; a task at `undefined` has none. A tableau shows a historical cell empty, neither marks nor `—`, unless the historical-junctions parameter is on, since the work there is done and the marks would only say who did it.

The **window** belongs to the two tableaux alone. A tableau lays the gates out as columns, and the width of its medium bounds how many it shows, so the window chooses them and folds the rest. Every other view lists its gates, items or events down the page, where length costs nothing a fold of rows does not already answer: it shows every gate and takes no window and no list of columns.

Two views take a parameter of their own: the work queue's `brief` and the audit's `stale` age.

### Levels

Every view discloses at three levels, and the levels nest. A format decides how a viewer moves between them: Markdown fixes one level per rendering, by a flag that CI sets once; HTML and the terminal fold and unfold. A role names the level a view opens at.

| Level      | Shows                                                                                                                                                      | Opens for                                                |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| glance     | The answer: one table, or one line per item, in the symbols the gate definition explains                                                                   | An observer; every role on a static export                |
| detail     | Each item expanded: the fields, criteria, texts, conditions and marks behind it                                                                            | The roles the view serves                                 |
| provenance | The Git fact behind each item: the commit with its date, author and committer; the file and the ancestor a field resolves from; the command that reproduces it | On demand; the audit and the history open here for the owner |

## Gate definition

**Question.** What do the columns and symbols mean?

**Roles.** Every role. A contributor reads the criteria of the gate they work at, an observer reads the legend beside a static export, and every other view links here.

**Data.** Gates. The language version and trunk from `version.yaml`. The junction marks, which belong to the method rather than to a project: 🧑 a person contributes, 🤖 an agent contributes, 👀 a reviewer accepts, 🪆 a subproject does the work, and — the gate does not apply. For one task, the junction references that expand a gate's criteria for it.

**Parameters.** ref: the gates as they stand at that commit. task: the criteria as that task's junction references expand them.

**Levels.**

- glance: the gates in order with symbol and name; the states with symbol and key; the reasons with symbol and key; the junction marks.
- detail: each gate's criteria, each state's severity and synopsis, each reason's synopsis, with the reserved meaning of `review`; for a task, the references that expand each gate.
- provenance: the language version, and the commit that last changed `gates.yaml` and `version.yaml`.

**Example.** This project's `gates.yaml` drops the performance and reliability gates from the set SYNTAX.md shows.

| ❔ undefined | 📝 defined | 📌 mockup | 🔧 function | 📐 design | 🧱 implementation | 📏 unit | 🔗 integrate | 🌍 validate | 🚀 release |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|

States ⚪ undefined 0 · 🟢 nominal 1 · 🟡 at_risk 2 · 🔴 stalled 3 · ✅ complete 0. Reasons 🪫 overloaded · ⛔ blocked · 👓 review. At detail, 📐 reads "A model and sufficient tests exist"; a task under the Method branch reads the gate as its parent `bc63` describes it, an outline with examples, which the task definition shows. 👓 beside a state says the contributor has handed the next junction's work to its reviewer; 👀 in a cell says a reviewer accepts the work there.

## Task definition

**Question.** What is this task and where does it stand?

**Roles.** Every role. The assignee and the contributor read their own task, the reviewer reads what they accept, an agent reads it as the expansion of its brief, and an authority reads a proposal before accepting it.

**Data.** The task file entire. Tree: parent, order, children. Authorities. Resolved junctions and applicable gates, with the three `url` forms of a recursive junction and the commit each fixes. Requirement conditions, both ways, with a cross-project entry shown by its `url`, `id` and the commit it reads. Authorisation. Status, or for a parent the roll-up, or for a recursive next junction the subproject snapshot. Reviews. Models. The newest events.

**Parameters.** task, required. ref. person marks the positions the person holds in this task. The junction list shows every gate.

**Levels.**

- glance: id, title, assignee, parent, and the status line: gate, state, reason, note, date, recorder.
- detail: the description and references; each requirement with its text and condition, and the dependents; every junction with its resolved fields and its marks; the authorisation state.
- provenance: the ancestor each junction field resolves from; the deciding commits of the authorisation and the status, with hash, date, author and committer; the review commits; the commit a linkage reads and how its `url` fixes it; the last few events, and the command that lists them all.

**Example.** `e9c6` Abstract views at glance:

> `e9c6` **Abstract views** — noreply@anthropic.com — under `2034` Views, order 1 — 📝 defined 🟢 nominal, 2026-09-29, noreply@anthropic.com: Design waits for Roles (c2ad) at design

At detail, the requirement on `c2ad` from design to design, "The role names the views refer to", is met, since `c2ad` stands at implementation, and due, since the next gate is design. The junctions read: mockup, function, unit, integrate —; defined 🤖 `claude-haiku`; design 🤖👀 `claude-fable`, reviewer nbyoung@nbyoung.com; implementation 🤖 `claude-sonnet`; validate 🤖👀 `claude-opus`; release 🧑 nbyoung@nbyoung.com. Twenty-one tasks depend on it: the twenty mockups at mockup and `77b2` at design. The task is authorised.

At provenance, the design junction takes its contributor and model from `bc63` and its reviewer from `437e`; the authorisation is the plan commit `6b6c99a` by nbyoung@nbyoung.com on 2026-09-29; the status is `1a17bfc`; and `5958858` carries `Reviewed: e9c6 defined` from the assignee, the agent's reviewer at defined, which has no effect because the authorisation stands as the review there. For `77b2` tablo, the same level shows the recursive junction's `url`, `subprojects/tablo`, as a submodule path and the commit it pins, `7e94d58`.

## Authority delegation

**Question.** Who may accept what?

**Roles.** The owner and each authority. An assignee reads the chain above their task.

**Data.** Tree. Each task's assignee and where it differs from the parent's, which is a delegation. Authorities. Authorisation, with the way the deciding commit accepts: a change on the trunk by an authority, a merge by one, or an `Authorised:` trailer. The junction defaults each parent states for its subtree.

**Parameters.** task: the subtree. person: the subtrees the person has authority over, and the chain above the person's tasks. ref: authorisation reads the trunk whatever the ref; at a ref off the trunk every task reads as proposed, and the view marks the tasks whose file differs from the trunk's, since those are the branch's proposals. A filter shows proposed tasks only.

**Levels.**

- glance: the tree indented, each row with its assignee where it changes from the parent's, and each proposed task marked.
- detail: every task's authority chain, and the junction defaults each parent states.
- provenance: the deciding commit with hash, date, author and committer, and the way it accepts.

**Example.** On `main` the owner assigns the root, the Method and Views branches, the three method decisions and the four subprojects to themself and delegates seven subtrees to the agent. A dot marks the parent's assignee.

```
437e Tableaux tooling             nbyoung@nbyoung.com
  bc63 Method                     ·
    c2ad Roles                    noreply@anthropic.com
    2034 Views                    ·
      e9c6 Abstract views         noreply@anthropic.com
      bc86 Markdown views         noreply@anthropic.com   10 children
      5fe3 HTML views             noreply@anthropic.com   10 children
    e3cb Schema files             noreply@anthropic.com
    fcec Conformance corpus       noreply@anthropic.com
    ac33 Agent identity           ·
    9f3f Subproject linkage       ·
    7861 Productivity evidence    noreply@anthropic.com
    7166 Language clarifications  ·
  77b2 tablo                      ·
  6103 tabloio                    ·
  c6e8 tablotui                   ·
  595e tableaud                   ·
```

Every task is authorised. At provenance, thirty-three read the plan commit `6b6c99a` as deciding, by the owner on the trunk; `437e` and `bc63` read `8eb0cae`, the owner's later change; `ac33` and `7166` read the merges `16fe62f` and `8d8b070`, by which the owner accepted the agent's branches, since the agent's own commits `018814a` and `9d9fb88` sit off the trunk's first-parent line. A commit the agent both authors and commits, as this wave makes them, leaves a changed task file proposed on its branch until such a merge.

## Task assignment

**Question.** What does each person carry?

**Roles.** The owner, an authority and an assignee.

**Data.** For each email in the project: the tasks it is assigned, with their status; the junctions where it is the contributor, stated or by default, at each task's next gate and at every gate, with the model where it is an agent; the junctions where it is the reviewer; the subtrees it has authority over; counts of each by gate.

**Parameters.** person: one section. task: within a subtree. ref. The lists show the junctions at every gate, grouped by gate in gate order.

**Levels.**

- glance: one row per email: tasks assigned, junctions to contribute next, junctions to review next, and for an agent its models.
- detail: per email, the lists: tasks with their status; junctions by gate, with the model and the reviewer.
- provenance: for each position, the file and the ancestor that states it, or the plain default.

**Example.** Two emails appear in the project.

| Email                  | Assigned | Contributes next | Reviews next | Models                                                                                  |
|------------------------|---------:|-----------------:|-------------:|-----------------------------------------------------------------------------------------|
| nbyoung@nbyoung.com    | 10       | 0                | 27           | —                                                                                       |
| noreply@anthropic.com  | 27       | 28               | 0            | `claude-haiku`, `claude-opus`, `claude-sonnet`, `claude-fable`                          |

At detail, the owner contributes at release on every task and reviews mockup, design and validate on every task, both from `437e`, and reviews the agent at every junction of the tasks the owner is assigned; the agent contributes next at validate on `c2ad`, `e3cb` and `7861`, at design on `e9c6`, at unit on `fcec`, at implementation on `ac33`, `9f3f` and `7166`, and at mockup on the twenty mockups. The four subprojects' next junctions are recursive, so nobody in this project contributes there. The agent's model at design is `claude-opus` from `437e` except under the Method branch, where `bc63` states `claude-fable`.

## Contributor work queue

**Question.** What do I do next?

**Roles.** A contributor, a reviewer and an authority. An agent, as a brief.

**Data.** For one person, the items where the person acts, in five kinds and in this order:

1. **Reviews owed.** Tasks whose next junction names the person as reviewer and whose status carries the reason `review`, the hand-off the method reserves that key for.
2. **Authorisations owed.** Proposed tasks in a subtree the person has authority over.
3. **Work ready.** Junctions at a task's next gate where the person is the contributor and every due requirement is met, a cross-project one read at the commit its linkage fixes.
4. **Reaffirmations.** Statuses the person recorded and has not reaffirmed for longest, oldest first.
5. **Work waiting.** Junctions as in 3 with an unmet requirement or a `blocked` or `overloaded` reason, each with its cause, so that nobody starts them.

Reviews come first because each one unblocks other people's work; within a kind, items follow display order. Each item draws from resolved junctions, requirement conditions, status, reviews, authorisation, gates and models. A task whose next junction is recursive is no item for anyone in this project: the subproject's own queue holds its work.

**Parameters.** person: the viewer by default; a dispatcher names the agent. task: within a subtree. ref. brief: a task and a gate, which writes that one item as a brief.

**Levels.**

- glance: one line per item: its kind, task, gate, and for an agent the model.
- detail: each item with the gate's criteria, the junction's references, the requirement texts and conditions, the status with its note, the reviewer.
- provenance, as the brief: one item, written to stand alone, with the commit the agent makes when done and the commands that reproduce the view.

**Example.** For noreply@anthropic.com on `main`, at glance:

| Kind         | Task                              | Gate           | Model          |
|--------------|-----------------------------------|----------------|----------------|
| Work ready   | `c2ad` Roles                      | validate       | `claude-opus`  |
| Work ready   | `e9c6` Abstract views             | design         | `claude-fable` |
| Work ready   | `e3cb` Schema files               | validate       | `claude-opus`  |
| Work ready   | `fcec` Conformance corpus         | unit           | `claude-sonnet` |
| Work ready   | `ac33` Agent identity             | implementation | `claude-sonnet` |
| Work ready   | `9f3f` Subproject linkage         | implementation | `claude-sonnet` |
| Work ready   | `7861` Productivity evidence      | validate       | `claude-opus`  |
| Work ready   | `7166` Language clarifications    | implementation | `claude-sonnet` |
| Work waiting | `99f0` Gate definition view in Markdown, and nineteen more | mockup | `claude-opus`; waits for `e9c6` at design |

The owner's queue is empty until this design hands off, when it reads one review owed: `e9c6` at design.

### The brief

A brief is the queue's provenance level for one item, written so that an agent starts from it alone. It holds, in order:

1. The item: the task's id and title, the gate, its criteria, and the junction resolved: contributor, `model`, reviewer, and the task whose entry supplies each.
2. The task: its description and references, its parent chain by title, and the description of the task whose entry supplies the contributor, since that entry is what sends the work to this agent.
3. The requirements with their texts and conditions, a cross-project one with its `url`, `id` and the commit it reads, and the dependents this junction unblocks.
4. The status with its note, date and recorder.
5. The commit the agent makes when done: the status file it writes, with the reason `review` when a reviewer is stated and the gate passed with `Reviewed: <id> <gate>` when the agent reviews itself; the `Model:` trailer, with the exact identifier the harness reports, and the `Co-Authored-By:` trailer; the branch, and that the reviewer merges it.
6. The commands that reproduce the brief and show the task.

The `model` line carries the plan's statement (F20). The dispatcher spawns the agent on a model that matches it, as an identifier or by prefix, and the agent writes the model it in fact ran in the trailer, so the audit can compare the two.

For `e9c6` at design, the brief this design was written from reads, in content:

```
Brief: e9c6 Abstract views at design

Contributor  noreply@anthropic.com, model claude-fable   (Method, bc63)
Reviewer     nbyoung@nbyoung.com                          (Tableaux tooling, 437e)
Gate         📐 design: A model and sufficient tests exist

Task: VIEWS.md defines each view independently of any format: its question,
the roles it serves, the data it draws from the project and the history, …
References: PLAN.md#views, Proposed views
Under: Tableaux tooling › Method › Views
Method (bc63): … design produces an outline with examples …

Requires: c2ad Roles from design to design, The role names the views refer to: met
Unblocks: 20 tasks at mockup (99f0 … a8b4); 77b2 tablo at design

Status: 📝 defined 🟢 nominal, 2026-09-29, noreply@anthropic.com:
Design waits for Roles (c2ad) at design

When done, commit the outline and .tableaux/status/e9c6.yaml as
  gate: defined / state: nominal / reason: review / note: what waits
on a branch off main, with the trailers
  Model: <the identifier the harness reports, matching claude-fable>
  Co-Authored-By: <display name> <noreply@anthropic.com>
The reviewer passes the gate with a commit carrying: Reviewed: e9c6 design

Reproduce: tabloio queue --person noreply@anthropic.com --brief e9c6 design
```

## Work-blockage tree

**Question.** What waits on what?

**Roles.** The owner, an authority and a contributor.

**Data.** The causes, and what each holds:

- an unmet requirement: the originating task at its `from` gate holds the terminating tasks at their `to` gates; a cross-project one reads as a local one, its originating task read at the commit the linkage fixes, and when that commit alone leaves it unmet (R13) the cause is the commit and the action is to advance it;
- a status with the reason `blocked` or `overloaded`, or in the state `at_risk` or `stalled`: the task holds itself and its dependents;
- a review outstanding: the reviewer at the junction holds the task and its dependents;
- an authorisation outstanding: a proposed task holds itself and its dependents;
- a subproject snapshot that has not advanced: the pin holds the task.

A held task holds its own dependents in turn, so the tree is transitive; a task held by two causes appears under both. Each cause names the one action that resolves it and the one person who takes it. A requirement that is not yet due is no wait, so it appears only at detail, as what comes next.

**Parameters.** task: the causes that hold one task, or the causes inside a subtree. person: the causes the person resolves, or the causes that hold the person's own work. ref.

**Levels.**

- glance: one line per cause with the person who resolves it and the count of tasks it holds, largest first.
- detail: the tree: each cause expands to the tasks and gates it holds, each of those to what it holds in turn; then the requirements not yet due.
- provenance: the requirement entry, the status file with its date and recorder, the deciding commit, the commit a linkage reads, and the command that resolves the cause.

**Example.** `main` has one cause.

```
e9c6 Abstract views has not passed design      noreply@anthropic.com contributes      holds 20
  99f0 Gate definition view in Markdown at mockup
  05a9 Task definition view in Markdown at mockup
  … eighteen more mockups at mockup
  next: 77b2 tablo at design, 6103 tabloio at design, c6e8 tablotui at design, 595e tableaud at design
```

Once this design hands off, the cause reads "`e9c6` design awaits review by nbyoung@nbyoung.com, holds 20", and the one action is the owner's commit carrying `Reviewed: e9c6 design`.

## Global tableau

**Question.** How does the whole project stand?

**Roles.** The owner and an observer; every role reads it.

**Data.** Tree, every task in display order and indented by depth, with every gate as a column. In the cell at a task's current gate, the gate its status names, the state symbol and, when present, the reason symbol. In every other applicable cell at or after that gate, the junction marks; in an exempt cell there, —; in a historical cell, nothing, unless the historical-junctions parameter is on. For a parent, the roll-up, and the marks of the defaults it states. For a recursive next junction, the subproject snapshot. The date and note of each row.

**Parameters.** ref. window or columns: the default window spans the next gates of every task in view with one column either side, and each folded column shows the count of tasks whose current gate lies in it. historical junctions: off by default. person marks the cells where the person acts.

**Levels.**

- glance: the rows to depth one: the root and its children, each with its derived status.
- detail: every row.
- provenance: on a cell, the status date, recorder and deciding commit; on a parent's cell, the child it rolls up from; on a mark, the ancestor that states it; on a subproject's cell, the commit the snapshot is read at.

**Example.** At glance on `main`, every row stands at defined. The root rolls up to defined and nominal from `bc63`, which rolls up from `2034` and in turn from `e9c6`, since its children tie and display order decides. Each subproject's row takes its state from its root task at the pin, itself a roll-up: `tablo`'s from `4b4f` Conformance, the one leaf there still at defined.

| Id     | Task                | ❔ | 📝 | 📌   | 🔧 | 📐   | 🧱 | 📏 | 🔗 | 🌍 | 🚀 |
|--------|---------------------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `437e` | **Tableaux tooling** |   | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `bc63` | &nbsp;&nbsp;**Method** |   | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `77b2` | &nbsp;&nbsp;tablo   |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `6103` | &nbsp;&nbsp;tabloio |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `c6e8` | &nbsp;&nbsp;tablotui |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `595e` | &nbsp;&nbsp;tableaud |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |

At detail the Method branch opens:

| Id     | Task                        | ❔ | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 | 🌍 | 🚀 |
|--------|-----------------------------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `c2ad` | Roles                       |   |   |   |   |   | 🟢 | — | — | 🤖👀 | 🧑 |
| `2034` | **Views**                   |   | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `e3cb` | Schema files                |   |   |   |   |   |   | 🟢 | — | 🤖👀 | 🧑 |
| `fcec` | Conformance corpus          |   |   |   |   |   | 🟢 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `ac33` | Agent identity              |   |   |   |   | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `9f3f` | Subproject linkage          |   |   |   |   | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `7861` | Productivity evidence       |   |   |   |   |   | 🟢 | — | — | 🤖👀 | 🧑 |
| `7166` | Language clarifications     |   |   |   |   | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |

The state symbol sits in the column of the gate the status names, as [PLAN.md](PLAN.md#the-plan-at-a-glance) draws it, with the reason symbol beside it, so `c2ad` shows 🟢 at 🧱: it has passed implementation and proceeds towards validate. Its four historical cells stand empty; with historical junctions on they read 🤖, —, —, 🤖👀, which is who did the work and who accepted it. The default window spans every column but ❔, since the next gates in view run from mockup to validate, and ❔ folds to a count of zero.

## Contextual tableau

**Question.** How does my corner stand?

**Roles.** An assignee and a contributor; an authority, for its subtree.

**Data.** As the global tableau, over the tasks in view: the subtree under a task; or, for a person, the tasks the person is assigned or contributes at next, their ancestors up to the root as a spine, and their siblings.

**Parameters.** task or person, one of them; the viewer's person by default. window or columns: the default window spans the next gates of the tasks in view with one column either side. historical junctions: off by default. ref.

**Levels.**

- glance: the task and its children, or the person's own tasks, in the window.
- detail: the spine and the siblings, the folded columns' counts, the notes.
- provenance: as the global tableau.

**Example.** For task `2034` Views, the next gates in view are design and mockup, so the window runs from 📝 to 🧱 and the columns outside fold; the children of `bc86` and `5fe3` stay collapsed at glance, and ❔ is historical for every row.

| Id     | Task                    | ❔ | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 … 🚀 |
|--------|-------------------------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `2034` | **Views**               | 0 | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 0 |
| `e9c6` | Abstract views          |   | 🟢 | — | — | 🤖👀 | 🤖 |   |
| `bc86` | **Markdown views** (10) |   | 🟢 | 🤖👀 | — | — | — |   |
| `5fe3` | **HTML views** (10)     |   | 🟢 | 🤖👀 | — | — | — |   |

In this project both emails hold most of the tree, so the task form serves them; the person form is for a contributor with few tasks. In the weather station of README.md, Ben's corner is `c07d`, its sibling `9f31` and the spine `4e2b`, `a1c0`.

## History

**Question.** What happened, when, and who did it?

**Roles.** Every role. A reviewer reads what changed since their last review, an observer reads a period from a static export, and the owner reads a release period between two tags.

**Data.** Events in author-time order, each with its date, commit, actor, the committer where it differs, and for a status event the gate, state, reason and note; for a pin event the `url` and the old and new commit, `old` absent when the linkage first appears. Models, on each agent commit. The status after each event, replayed for a parent from its children. The subproject snapshot's events up to the commit its `url` fixes. At a ref off the trunk, the events the branch adds beyond the trunk, marked as proposals.

**Parameters.** task: one task, or a subtree, which replays its children. person: the events one actor made. ref, or a range such as `v1.0..v1.1` or `main..task/e9c6`.

**Levels.**

- glance: one line per event: date, actor, event, task, gate and state, or for a pin the `url` and the commits.
- detail: the status after each event, the note, the model, the committer where it differs from the author, and the subproject's own events between two pins.
- provenance: the hash, subject, trailers and files of each commit, and the `git log` commands that produce the list, with the submodule path added for a task whose linkage is a submodule.

**Example.** `77b2` tablo on `main`, whose recursive junctions name the submodule `subprojects/tablo`:

| Date       | By                    | Event            | Detail                                                                                          |
|------------|-----------------------|------------------|-------------------------------------------------------------------------------------------------|
| 2026-09-29 | nbyoung@nbyoung.com   | task, authorised | `6b6c99a` Plan the Tableaux tooling: the owner commits the file on the trunk                     |
| 2026-09-29 | nbyoung@nbyoung.com   | pin              | `37a08e9` Pin the subprojects: `subprojects/tablo` new `dc669dd`, no old commit                  |
| 2026-09-30 | nbyoung@nbyoung.com   | pin              | `5c87000` … `564c7cb`: six advances of the pin, each with its old and new commit                  |
| 2026-09-30 | noreply@anthropic.com | status           | `e66abe2` defined, no state, since the next junction is recursive; `Model: claude-haiku-4-5-20251001` |
| 2026-09-30 | nbyoung@nbyoung.com   | pin              | `1b6916e` Advance tablo to tableaux language 0.3.0: old `1339804`, new `7e94d58`                   |

At detail each pin event carries the subproject's own events between the two commits, replayed under `77b2`, and the status after `1b6916e` reads defined and nominal from `tablo`'s root at the new pin. For `e9c6`, the same view shows the plan commit, the status `1a17bfc`, and `5958858` with `Reviewed: e9c6 defined` from the assignee, an event with no effect since the authorisation stands as the review; the two agent commits show the owner as committer and no `Model:` trailer, since both precede F20. The range `main..<this branch>` shows this design's own hand-off: a status event with the reason `review`, and a `Model:` trailer.

## Audit

**Question.** Where do files and history disagree?

**Roles.** The owner and an authority.

**Data.** Findings, and the disagreements no rule makes invalid: a proposed task; a `Reviewed:` commit from the wrong hand (H2); a trailer that names nothing (H1); a `Model:` trailer outside the model the junction states (H3), or no trailer at all where the junction states a model (H6); a hand-off the history implies and the status does not state (H4), and one the status still states after its review (H5); an unmet requirement (R9), a cross-project one that names what a junction already reads (R12), or one that its `commit` alone leaves unmet (R13); a stale status, one whose date is older than an age and has no later reaffirmation; a pin or `commit` off the subproject's trunk (J13); a `commit` malformed, missing, misplaced or off the pin (J14 to J17); a subproject the tool cannot read (J8, J9); and an undetermined trunk (P5). Each finding names the action that resolves it and the person who takes it: authorise, review, reaffirm, record the hand-off or clear it, revise the file, move the pin or the `commit`, check out the submodule.

**Parameters.** task: within a subtree. person: the findings the person resolves. ref. stale: this view's own parameter, the age beyond which a status is stale, seven days by default.

**Levels.**

- glance: counts by kind, errors first, then warnings, then information, and the person with the most to resolve.
- detail: the findings table: rule, severity, task, gate, file, message, resolver.
- provenance: the rule's sentence in README.md or SYNTAX.md, the commits involved, and the command that resolves the finding.

**Example.** On `main`, in a clone with the submodules checked out, the audit reports no error, twenty warnings and three items of information:

| Rule | Severity    | Task                    | Gate           | Message                                                        | Resolves when                                     |
|------|-------------|-------------------------|----------------|----------------------------------------------------------------|---------------------------------------------------|
| R9   | warning     | `99f0` … `a8b4`, twenty | mockup         | Requires `e9c6` at design; `e9c6` stands at defined            | `e9c6` passes design; nbyoung@nbyoung.com reviews |
| H4   | information | `e9c6`                  | design         | The contributor's `5958858` is the newest event and the status states no hand-off | The agent records `review`, or works on |
| H4   | information | `ac33`, `7166`          | implementation | The contributor's status commit is the newest event             | As above                                          |

A plain clone without `--recurse-submodules` adds four J8 errors, since `subprojects/tablo` and its siblings resolve to no project the tool can read, and `git submodule update --init` resolves them. Nothing is stale: the plan is two days old. Every agent commit since the language reached 0.2.1 carries its `Model:` trailer, so H6 stays silent, and the `Reviewed: … defined` trailers the agent left on 2026-09-29 name their tasks' own reviewer, so H2 does too.

## Decisions at review

The owner reviewed the first draft on 2026-09-30 and decided each question below; the text above agrees with each decision.

- **Historical junctions.** The draft said a cell the task has passed keeps its marks. The owner refuted it: every junction before a task's current status gate is historical, applicable or not, and a tableau shows it empty unless the historical-junctions parameter is on, which defaults to false. The shared parameters and both tableaux now say so.
- **Q1 Three levels.** Accepted: every view discloses at glance, detail and provenance, with a per-role default, and the mockups may rename them.
- **Q2 The window.** Accepted: one column either side of the next gates in view, and a folded column shows the count of tasks whose current gate lies in it. PLAN.md's Views section now states the same.
- **Q3 The queue's order.** Kept: reviews owed, authorisations owed, work ready, reaffirmations, work waiting; display order within a kind.
- **Q4 The brief.** Kept: its six parts, and the description of the ancestor whose entry supplies the contributor.
- **Q5 The tableau cell.** Kept: the state symbol sits in the column of the gate the status names, with the reason symbol in the same cell.
- **Q6 The stale age.** Reduced to seven days, on the audit alone; the queue lists reaffirmations by age with no threshold.
- **Q7 The person form of the contextual tableau.** Kept: the person's tasks, the spine to the root and the siblings.

The owner reviewed the mockups from 2026-10-05 and decided the following; the text above agrees.

- **The window serves the tableaux only.** The draft gave every view the window-or-columns parameter. The task assignment mockup showed the cost: the view lists its gates down the page, so a window hid two gates behind a term the reader had to learn and gained nothing. The owner removed the parameter from every view that lists rather than tabulates by gate: the gate definition, the task definition, task assignment, the work queue, the work-blockage tree and the history. Those views show every gate. The global and the contextual tableau keep the window as Q2 states it.

The owner reviewed the eighteen designs of 2026-10-05 on 2026-10-06 and decided the following; the text above agrees. The mockups stay as drawn: their purpose was to obligate decisions cheaply and reveal gaps, and the understanding carries forward here and in each design's own record, not in a rewrite of the artefacts.

- **The default ref is the working tree.** Without a ref a tool reads the files under `.tableaux` from the working tree on the history of `HEAD`, so an edit shows before its commit; `HEAD` names the committed state. The parameter table reads so. In a working-tree read a submodule reads at its checkout's `HEAD`.
- **The person default is per view.** The viewer on the work queue and on the contextual tableau without a task; nobody elsewhere, so the other eight views show everyone and mark no one. The parameter table reads so.
- **A parameter a view does not name is a usage error**, so one mistyped option never passes for a default. The paragraph above the table reads so.
- **The parameter names on a command line** are `--person` and `--ref`, as the table names them, in every tool; the `--for` and `--at` that `task.md`, `audit.md` and `assignment.md` write are the mockups' shorthand.
- **A long list folds from more than eight alike rows**, showing three and folding the rest with every id, in every front end. `queue.md` and `queue.html`, which say five or more, stay as drawn.
- **The number after a folded parent** counts every row folded beneath it, as `tableau.md` reads it; `context.md`, which counts the children not drawn, stays as drawn.
- **A folded column's count includes parents** by their roll-up: the count of tasks whose current gate lies in it, as the global tableau's Parameters paragraph states and as `tableau.md` counts 29 at 📝. The count stands in the column header, as `tableau.md` draws it, not in the first row as `context.md` and the example under the contextual tableau draw it.
- **A link's form belongs to the medium.** The daemon spells a task link as a query and a static export as a file name, so the mockups' `task.html?task=…` links and the bare `task.html` links of `authority.html` and `blockage.html` are shorthand that no design copies.
- **A self-review shows the contributor's mark alone**: 👀 stands only where the reviewer differs from the contributor, so an agent that reviews its own work shows 🤖 alone and a person's plain junction shows 🧑 alone. README.md#junctions states it, and a tool derives the marks.
- **Markdown fixes one level by a flag**, as the Levels paragraph says; `tabloio` takes `--level` alone, glance by default, and the role parameter serves the live front ends through `tablo`.

The owner ruled on 2026-10-07, over the designs of tablo's Validator (`8118`) and Derivation (`27a3`), which read one sentence two ways; the text above and README.md agree.

- **The history implies no hand-off once the reviewer accepts.** The audit's information finding H4 needs a junction that no `Reviewed:` commit from its reviewer accepts yet. README.md#status wrote "a task whose next junction has a reviewer, whose newest event is the contributor's and whose status states no `review`", which also fits a task whose review is done and whose contributor then records the status; README.md and `corpus/RULES.md` now state the condition, and the corpus entries `model-trailer-missing` and `review-by-non-reviewer`, which state no H4, stand as they are.

The owner accepted the designs of tablo's Validator (`8118`) and Derivation (`27a3`) on 2026-10-07 with these decisions about the method; README.md agrees with each.

- **Fields above an exemption do not pass.** A descendant that states its own entry under a not-applicable one starts from the plain default, so it takes no reviewer from an ancestor above the exemption. README.md#junctions states it, PLAN.md's F7 closes, and the corpus entry `junction-kinds` states the fact at `a210` with no `undecided` mark.
- **A linked repository takes its trunk from the remote-tracking branch first.** In a submodule's store and in a clone a URL maps to, a fetch moves the remote-tracking branch and leaves the local one behind, so README.md's order made every pin read as off its trunk. README.md#project states the reversed order there; the home repository keeps the local branch first.
- **A view stands beside an error.** A tool gives no view data only for what it cannot read: a missing or unaccepted version, an unusable `gates.yaml`, a broken tree. Every other error leaves the views standing beside its diagnostic, in every front end.

The owner ruled on 2026-10-07, after the implementations of the Validator and the Derivation each read the rule above the same way, against the corpus:

- **`model-trailer-missing` states an H4.** At M4 the contributor's event is the newest, the next junction, design, has a reviewer, no `Reviewed:` commit of that reviewer accepts it and the status states no `review`: the rule as worded reports the hand-off the history implies, and the entry's `expected.yaml` now states the finding beside its H6. This amends the ruling above in one consequence alone: `review-by-non-reviewer` still states no H4, and the rule stands as README.md and `corpus/RULES.md` word it.

## Findings about the method

Defining the views found the following. The owner resolved each at the design review, and the text names what landed.

- **F21 Roll-up ties. Resolved.** A parent takes the state, reason and note of the most severe considered child at the earliest gate, and README.md did not say which of two tied children wins. Decided: the first in display order; README.md#status step 3 states it, and the corpus entry `roll-up-tie` exercises it. Task `7166`.
- **F22 The hand-off has no signal of its own. Resolved.** A queue lists a review as owed when the status waits for the reviewer, and the method gave no way to say so. Decided, in both forms: the method reserves the reason key `review`, whose symbol is 👓 so that 👀 stays the reviewer mark, and the audit reads the implicit form too, a hand-off the history implies and the status does not state (H4) and one the status still states after its review (H5); corpus entries `handoff-inferred` and `handoff-stale` exercise them. Task `7166`.
- **F23 No mark for a person. Resolved.** README.md now gives a view 🧑 for a plain junction whose contributor is a person, beside 🤖, 👀 and 🪆. Task `7166`.
- **F24 A missing trailer escapes the audit. Resolved.** The audit now also reports a commit at a junction that states a model, by that junction's contributor, with no `Model:` trailer (H6); a commit at which the project's `version.yaml` states a language before 0.2.1, the version that introduced the trailer, is exempt, so the history before F20 stays silent. The corpus entry `model-trailer-missing` exercises both. Task `ac33`.

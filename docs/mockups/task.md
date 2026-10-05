# Task definition: `e9c6` Abstract views

The task definition view answers one question: what is this task and where does it stand? This file draws it for task `e9c6` of the Tableaux tooling plan, on `main` at commit `3cdae52`, 2026-10-05, for the viewer nbyoung@nbyoung.com, the owner. Bold marks each position that nbyoung@nbyoung.com holds in the task.

`e9c6` is the full example: a leaf with a requirement, twenty-one dependents, four exempt gates, junction fields that resolve from two ancestors, and a review. The view also carries two other shapes, which [the last section](#the-two-other-shapes) shows more briefly: a parent, `5fe3`, whose status is a roll-up, and a task with recursive junctions, `595e`, whose status comes from a subproject snapshot.

The view takes one task, and a tool writes one such file per task. [gates.md](gates.md) is the legend for every symbol here. The neighbouring views are [history.md](history.md), [blockage.md](blockage.md), [authority.md](authority.md), [assignment.md](assignment.md), [queue.md](queue.md), [context.md](context.md), [tableau.md](tableau.md) and [audit.md](audit.md).

## Glance

| Field    | Value                                      |
|----------|--------------------------------------------|
| Task     | `e9c6` Abstract views                      |
| Assignee | noreply@anthropic.com                      |
| Parent   | `2034` Views, order 1                      |
| Status   | 📐 design · 🟢 nominal                     |
| Note     | VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place |
| Recorded | 2026-09-30 by noreply@anthropic.com        |

`tabloio task e9c6 --ref 3cdae52 --for nbyoung@nbyoung.com --level glance`

## Detail

| Field    | Value                                      |
|----------|--------------------------------------------|
| Task     | `e9c6` Abstract views                      |
| Assignee | noreply@anthropic.com                      |
| Parent   | `2034` Views, order 1                      |
| Status   | 📐 design · 🟢 nominal                     |
| Note     | VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place |
| Recorded | 2026-09-30 by noreply@anthropic.com        |

### Description

VIEWS.md defines each view independently of any format: its question, the roles it serves, the data it draws from the project and the history, the parameters that focus it (a task, a person, a gate window or a list of columns, a ref) and its progressive-disclosure levels. The views are the gate definition, the task definition, authority delegation, task assignment, the contributor work queue, the work-blockage tree, the global tableau, the contextual tableau, the history and the audit.

References:

- [Proposed views](../../PLAN.md#views)

### Place in the tree

| Field       | Value                                                                     |
|-------------|---------------------------------------------------------------------------|
| Path        | `437e` Tableaux tooling › `bc63` Method › `2034` Views › `e9c6` Abstract views |
| Order       | 1 of 3 under `2034`: before `bc86` Markdown views and `5fe3` HTML views   |
| Children    | None; the task is a leaf and keeps its own status                         |
| Authorities | **nbyoung@nbyoung.com** by `2034` Views, by `bc63` Method and by `437e` Tableaux tooling, nearest first |
| Authorised  | Yes                                                                       |

[authority.md](authority.md) shows the whole chain of delegation.

### Requires

The task requires one task.

| Task          | Edge            | What passes                       | Its status                  | Condition |
|---------------|-----------------|-----------------------------------|-----------------------------|-----------|
| `c2ad` Roles  | design → design | The role names the views refer to | 🧱 implementation 🟢 nominal | met       |

The edge reads "from the gate `c2ad` completes, to the gate of `e9c6` whose work needs it". The requirement is met, since `c2ad` stands past design, and due, since the next gate of `e9c6`, implementation, lies past design.

### Dependents

Twenty-one tasks require `e9c6`: twenty at their mockup gate, all met, and one at its design gate, not yet due. [blockage.md](blockage.md) shows what waits on what across the project.

| Task                                         | Edge                    | What passes                         | Condition              |
|----------------------------------------------|-------------------------|-------------------------------------|------------------------|
| `99f0` Gate definition view in Markdown      | design → mockup         | The abstract definition of the view | met                    |
| `05a9` Task definition view in Markdown      | design → mockup         | The abstract definition of the view | met                    |
| `a9ce` Authority delegation view in Markdown | design → mockup         | The abstract definition of the view | met                    |
| … and 17 more with the same edge, text and condition: `bb7c` `c74a` `efff` `ab8e` `c545` `d615` `b14e` `a6f7` `7dff` `b1b7` `ea51` `7783` `5471` `32e7` `69eb` `3194` `a8b4` | design → mockup | The abstract definition of the view | met |
| `77b2` tablo: backend library and plumbing   | implementation → design | The abstract views it derives       | not met, not yet due   |

The fold keeps every row that differs from its neighbours. The twenty mockups are the leaves of `bc86` Markdown views and `5fe3` HTML views; each stands at 📝 defined with mockup next, so its requirement is due, and `e9c6` stands at design, so it is met. `77b2` needs `e9c6` at implementation for its own design gate; `77b2` has mockup next, so the requirement is not yet due.

### Junctions

The task passes through five gates after undefined: defined, design, implementation, validate and release. Its first applicable gate is defined and its last is release.

| Gate              | Marks | Contributor               | Model           | Reviewer                               | Stands                |
|-------------------|:-----:|---------------------------|-----------------|----------------------------------------|-----------------------|
| ❔ undefined      |       |                           |                 |                                        | passed                |
| 📝 defined        | 🤖    | noreply@anthropic.com     | `claude-haiku`  | the assignee, noreply@anthropic.com    | passed                |
| 📌 mockup         | —     |                           |                 |                                        | does not apply        |
| 🔧 function       | —     |                           |                 |                                        | does not apply        |
| 📐 design         | 🤖👀  | noreply@anthropic.com     | `claude-fable`  | **nbyoung@nbyoung.com**                | passed, reviewed; the status stands here |
| 🧱 implementation | 🤖    | noreply@anthropic.com     | `claude-sonnet` | the assignee, noreply@anthropic.com    | next                  |
| 📏 unit           | —     |                           |                 |                                        | does not apply        |
| 🔗 integrate      | —     |                           |                 |                                        | does not apply        |
| 🌍 validate       | 🤖👀  | noreply@anthropic.com     | `claude-opus`   | **nbyoung@nbyoung.com**                | later                 |
| 🚀 release        | 🧑    | **nbyoung@nbyoung.com**   |                 |                                        | later; the last gate  |

🤖 an agent contributes · 👀 a reviewer accepts · 🧑 a person contributes · — the gate does not apply. The undefined gate has no work of its own. No junction of this task states references, so each gate's own criteria apply as [gates.md](gates.md) gives them.

`tabloio task e9c6 --ref 3cdae52 --for nbyoung@nbyoung.com --level detail`

## Provenance

| Field    | Value                                      |
|----------|--------------------------------------------|
| Task     | `e9c6` Abstract views                      |
| Assignee | noreply@anthropic.com                      |
| Parent   | `2034` Views, order 1                      |
| Status   | 📐 design · 🟢 nominal                     |
| Note     | VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place |
| Recorded | 2026-09-30 by noreply@anthropic.com        |

### Status commit

The status file is `.tableaux/status/e9c6.yaml`. Its deciding commit is the newest commit that changes the file; no commit carries `Reaffirmed: e9c6`.

| Field     | Value                                                  |
|-----------|--------------------------------------------------------|
| Commit    | `879b447` Advance the abstract views task to its design gate |
| Date      | 2026-09-30                                             |
| Author    | Claude Fable 5.1, noreply@anthropic.com                |
| Committer | Claude Fable 5.1, noreply@anthropic.com                |
| Trailers  | `Model: claude-fable-5-1`                              |

`git log -1 --format='%h %as %ae' 3cdae52 -- .tableaux/status/e9c6.yaml`

### Description

VIEWS.md defines each view independently of any format: its question, the roles it serves, the data it draws from the project and the history, the parameters that focus it (a task, a person, a gate window or a list of columns, a ref) and its progressive-disclosure levels. The views are the gate definition, the task definition, authority delegation, task assignment, the contributor work queue, the work-blockage tree, the global tableau, the contextual tableau, the history and the audit.

References:

- [Proposed views](../../PLAN.md#views)

The task file is `.tableaux/tasks/e9c6.yaml`.

### Place in the tree

| Field       | Value                                                                     |
|-------------|---------------------------------------------------------------------------|
| Path        | `437e` Tableaux tooling › `bc63` Method › `2034` Views › `e9c6` Abstract views |
| Order       | 1 of 3 under `2034`: before `bc86` Markdown views and `5fe3` HTML views   |
| Children    | None; the task is a leaf and keeps its own status                         |
| Authorities | **nbyoung@nbyoung.com** by `2034` Views, by `bc63` Method and by `437e` Tableaux tooling, nearest first |
| Authorised  | Yes                                                                       |

[authority.md](authority.md) shows the whole chain of delegation.

### Authorisation commit

The deciding commit is the newest commit on the first-parent history of the trunk, `main`, that changes the task file or carries `Authorised: e9c6`. No commit carries that trailer, so the commit that creates the file decides.

| Field     | Value                                                  |
|-----------|--------------------------------------------------------|
| Commit    | `6b6c99a` Plan the Tableaux tooling                    |
| Date      | 2026-09-29                                             |
| Author    | Norman Young, **nbyoung@nbyoung.com**                  |
| Committer | Norman Young, **nbyoung@nbyoung.com**                  |
| Authority | The author is an authority, as the assignee of `2034`, of `bc63` and of `437e` at that commit, so the task is authorised |

`git log --first-parent -1 --format='%h %as %ae %ce' 3cdae52 -- .tableaux/tasks/e9c6.yaml`

### Requires

The task requires one task.

| Task          | Edge            | What passes                       | Its status                  | Condition |
|---------------|-----------------|-----------------------------------|-----------------------------|-----------|
| `c2ad` Roles  | design → design | The role names the views refer to | 🧱 implementation 🟢 nominal | met       |

The edge reads "from the gate `c2ad` completes, to the gate of `e9c6` whose work needs it". The requirement is met, since `c2ad` stands past design, and due, since the next gate of `e9c6`, implementation, lies past design.

The entry sits in `.tableaux/tasks/e9c6.yaml` and names `c2ad` by `id`, so the tool reads `c2ad` in this project at the same commit, `3cdae52`. The status of `c2ad` is `.tableaux/status/c2ad.yaml` as commit `3d8ce0e` records it, 2026-09-30, by noreply@anthropic.com. No requirement of this task crosses projects, so no linkage fixes another commit; `595e` below shows one that does.

### Dependents

Twenty-one tasks require `e9c6`: twenty at their mockup gate, all met, and one at its design gate, not yet due. [blockage.md](blockage.md) shows what waits on what across the project.

| Task                                         | Edge                    | What passes                         | Condition              |
|----------------------------------------------|-------------------------|-------------------------------------|------------------------|
| `99f0` Gate definition view in Markdown      | design → mockup         | The abstract definition of the view | met                    |
| `05a9` Task definition view in Markdown      | design → mockup         | The abstract definition of the view | met                    |
| `a9ce` Authority delegation view in Markdown | design → mockup         | The abstract definition of the view | met                    |
| … and 17 more with the same edge, text and condition: `bb7c` `c74a` `efff` `ab8e` `c545` `d615` `b14e` `a6f7` `7dff` `b1b7` `ea51` `7783` `5471` `32e7` `69eb` `3194` `a8b4` | design → mockup | The abstract definition of the view | met |
| `77b2` tablo: backend library and plumbing   | implementation → design | The abstract views it derives       | not met, not yet due   |

The fold keeps every row that differs from its neighbours. The twenty mockups are the leaves of `bc86` Markdown views and `5fe3` HTML views; each stands at 📝 defined with mockup next, so its requirement is due, and `e9c6` stands at design, so it is met. `77b2` needs `e9c6` at implementation for its own design gate; `77b2` has mockup next, so the requirement is not yet due.

Each edge sits in the dependent's own file, `.tableaux/tasks/<id>.yaml`, under `requires`; the tool reads the reverse relation from all of them.

`grep -l 'id: "e9c6"' .tableaux/tasks/*.yaml`

### Junctions

The task passes through five gates after undefined: defined, design, implementation, validate and release. Its first applicable gate is defined and its last is release.

| Gate              | Marks | Contributor               | Model           | Reviewer                               | Stands                |
|-------------------|:-----:|---------------------------|-----------------|----------------------------------------|-----------------------|
| ❔ undefined      |       |                           |                 |                                        | passed                |
| 📝 defined        | 🤖    | noreply@anthropic.com     | `claude-haiku`  | the assignee, noreply@anthropic.com    | passed                |
| 📌 mockup         | —     |                           |                 |                                        | does not apply        |
| 🔧 function       | —     |                           |                 |                                        | does not apply        |
| 📐 design         | 🤖👀  | noreply@anthropic.com     | `claude-fable`  | **nbyoung@nbyoung.com**                | passed, reviewed; the status stands here |
| 🧱 implementation | 🤖    | noreply@anthropic.com     | `claude-sonnet` | the assignee, noreply@anthropic.com    | next                  |
| 📏 unit           | —     |                           |                 |                                        | does not apply        |
| 🔗 integrate      | —     |                           |                 |                                        | does not apply        |
| 🌍 validate       | 🤖👀  | noreply@anthropic.com     | `claude-opus`   | **nbyoung@nbyoung.com**                | later                 |
| 🚀 release        | 🧑    | **nbyoung@nbyoung.com**   |                 |                                        | later; the last gate  |

🤖 an agent contributes · 👀 a reviewer accepts · 🧑 a person contributes · — the gate does not apply. The undefined gate has no work of its own. No junction of this task states references, so each gate's own criteria apply as [gates.md](gates.md) gives them.

### Where each junction field comes from

A junction resolves field by field: from the task's own entry, then from its ancestors' entries nearest first, then from the plain default. The tool looks in this order:

1. `e9c6` Abstract views, `.tableaux/tasks/e9c6.yaml`: states mockup, function, unit and integrate, each `applies: false`.
2. `2034` Views, `.tableaux/tasks/2034.yaml`: states no junction.
3. `bc63` Method, `.tableaux/tasks/bc63.yaml`: states design and validate, each with a contributor and a model.
4. `437e` Tableaux tooling, `.tableaux/tasks/437e.yaml`: states every gate from defined to release.
5. The plain default: the assignee does the work, and nobody reviews it.

| Gate              | Field       | Value                   | Supplied by                                           |
|-------------------|-------------|-------------------------|-------------------------------------------------------|
| 📝 defined        | contributor | noreply@anthropic.com   | `437e` Tableaux tooling                               |
|                   | model       | `claude-haiku`          | `437e` Tableaux tooling                               |
|                   | reviewer    | noreply@anthropic.com   | No entry; an agent with no stated reviewer takes the assignee |
| 📌 mockup         | applies     | false                   | `e9c6`, its own entry                                 |
| 🔧 function       | applies     | false                   | `e9c6`, its own entry                                 |
| 📐 design         | contributor | noreply@anthropic.com   | `bc63` Method                                         |
|                   | model       | `claude-fable`          | `bc63` Method                                         |
|                   | reviewer    | **nbyoung@nbyoung.com** | `437e` Tableaux tooling                               |
| 🧱 implementation | contributor | noreply@anthropic.com   | `437e` Tableaux tooling                               |
|                   | model       | `claude-sonnet`         | `437e` Tableaux tooling                               |
|                   | reviewer    | noreply@anthropic.com   | No entry; an agent with no stated reviewer takes the assignee |
| 📏 unit           | applies     | false                   | `e9c6`, its own entry                                 |
| 🔗 integrate      | applies     | false                   | `e9c6`, its own entry                                 |
| 🌍 validate       | contributor | noreply@anthropic.com   | `bc63` Method                                         |
|                   | model       | `claude-opus`           | `bc63` Method                                         |
|                   | reviewer    | **nbyoung@nbyoung.com** | `437e` Tableaux tooling                               |
| 🚀 release        | contributor | **nbyoung@nbyoung.com** | `437e` Tableaux tooling                               |

At design and at validate two ancestors supply one junction: `bc63` restates the contributor and the model, which hide those of `437e` (`claude-opus` at design, `claude-sonnet` at validate), and the reviewer still comes from `437e`.

### Reviews

| Gate       | Reviewer                | Accepted by                                            | Effect |
|------------|-------------------------|--------------------------------------------------------|--------|
| 📝 defined | noreply@anthropic.com   | The authorisation, `6b6c99a`, 2026-09-29               | The authorisation stands as the review of defined |
| 📐 design  | **nbyoung@nbyoung.com** | `0704a09` Accept the abstract views design, 2026-09-30, author and committer Norman Young, **nbyoung@nbyoung.com**, with `Reviewed: e9c6 design` | The reviewer accepts; the status passes design |

Commit `5958858`, 2026-09-29, author Claude Fable 5.1, noreply@anthropic.com, committer Norman Young, nbyoung@nbyoung.com, also carries `Reviewed: e9c6 defined`. It comes from the assignee, the agent's reviewer at defined, and has no effect, because the authorisation stands as the review there.

`git log --format='%h %as %ae %ce' -E --grep='^Reviewed: e9c6 ' 3cdae52`

### Models

| Commit    | Junction   | The junction states | `Model:` trailer   | Reading |
|-----------|------------|---------------------|--------------------|---------|
| `1a17bfc` | 📝 defined | `claude-haiku`      | none               | Exempt: the project states language 0.1.0 at that commit, before the trailer exists |
| `0fed913` | 📐 design  | `claude-fable`      | `claude-fable-5-1` | Agrees  |
| `26defc7` | 📐 design  | `claude-fable`      | `claude-fable-5-1` | Agrees  |
| `879b447` | 📐 design  | `claude-fable`      | `claude-fable-5-1` | Agrees  |

The reviewer's commit `0704a09` carries `Model: claude-opus-5-5`; the junction's model names the contributor's agent, so the view compares nothing there.

### Newest events

The task has seven events. The newest five, newest first:

| Date       | Commit    | By                      | Event    | What it records |
|------------|-----------|-------------------------|----------|-----------------|
| 2026-09-30 | `879b447` | noreply@anthropic.com   | status   | 📐 design 🟢 nominal: VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place |
| 2026-09-30 | `0704a09` | **nbyoung@nbyoung.com** | reviewed | 📐 design |
| 2026-09-30 | `26defc7` | noreply@anthropic.com   | status   | 📝 defined 🟢 nominal 👓 review: The revised VIEWS.md design on branch worktree-agent-a6b84238bbacc4fcd awaits the owner's acceptance at the design gate |
| 2026-09-30 | `0fed913` | noreply@anthropic.com   | status   | 📝 defined 🟢 nominal 👓 review: The VIEWS.md design on branch worktree-agent-a6b84238bbacc4fcd awaits the owner's review at the design gate |
| 2026-09-29 | `5958858` | noreply@anthropic.com   | reviewed | 📝 defined |
| … and 2 earlier: `1a17bfc` status, `6b6c99a` task | | | | |

[history.md](history.md) lists every event with the status after each. Two commands list them all:

```
git log --format='%as %h %ae' 3cdae52 -- .tableaux/tasks/e9c6.yaml .tableaux/status/e9c6.yaml
git log --format='%as %h %ae' -E --grep='^(Authorised|Reaffirmed): e9c6$' --grep='^Reviewed: e9c6 ' 3cdae52
```

`tabloio task e9c6 --ref 3cdae52 --for nbyoung@nbyoung.com --level provenance`

## The two other shapes

Each task below is the output of the same command for another task, cut to what differs from `e9c6`. Every part that does not appear here has the form the full example gives it.

### A parent: `5fe3` HTML views

A parent has no status file. The view shows the roll-up and the child it comes from, and reads the junctions as defaults the children inherit.

Glance:

| Field    | Value                                      |
|----------|--------------------------------------------|
| Task     | `5fe3` HTML views                          |
| Assignee | noreply@anthropic.com                      |
| Parent   | `2034` Views, order 3                      |
| Status   | 📝 defined · 🟢 nominal, rolled up from `a6f7` Gate definition view in Html |
| Note     | Mockup waits for Abstract views (e9c6) at design |
| Recorded | 2026-09-29, the oldest date among its children; a roll-up has no recorder |

`tabloio task 5fe3 --ref 3cdae52 --for nbyoung@nbyoung.com --level glance`

Detail, the parts that differ:

| Field      | Value                                                                    |
|------------|--------------------------------------------------------------------------|
| Children   | Ten, each at 📝 defined 🟢 nominal: `a6f7` `7dff` `b1b7` `ea51` `7783` `5471` `32e7` `69eb` `3194` `a8b4`, in display order |
| Requires   | Nothing                                                                  |
| Dependents | `c6e8` tablotui: terminal user interface, mockup → design, "The HTML mockups that fix the disclosure levels", not met, not yet due; `595e` tableaud: local daemon and HTML, mockup → design, "The HTML mockups it reproduces", not met, not yet due |

| Gate                  | Marks | The children inherit                                                                        |
|-----------------------|:-----:|---------------------------------------------------------------------------------------------|
| 📝 defined            | 🤖    | noreply@anthropic.com on `claude-haiku`; each child's assignee reviews                       |
| 📌 mockup             | 🤖👀  | noreply@anthropic.com on `claude-opus`; reviewer **nbyoung@nbyoung.com**                     |
| 🔧 function to 🚀 release | — | The seven gates from function to release do not apply                                       |

Provenance, the parts that differ:

| Step                  | Result                                                                                      |
|-----------------------|---------------------------------------------------------------------------------------------|
| Children considered   | All ten; each is nominal, which has severity 1                                              |
| Gate                  | 📝 defined, the earliest among them                                                         |
| State and note        | Those of `a6f7`: the ten tie at nominal, and `a6f7` is the first in display order, order 1  |
| Date                  | 2026-09-29, the oldest among them                                                           |
| Commit behind `a6f7`  | `1a17bfc` Record the defined gate for the views and mockups, 2026-09-29, author Claude Fable 5.1, noreply@anthropic.com, committer Norman Young, **nbyoung@nbyoung.com** |
| Junction fields       | defined and mockup from `437e` Tableaux tooling; function to release from `5fe3`, its own entries |
| Authorisation         | `6b6c99a` Plan the Tableaux tooling, 2026-09-29, author and committer Norman Young, **nbyoung@nbyoung.com** |

A parent's events replay those of its children; [history.md](history.md) shows them.

### Recursive junctions: `595e` tableaud: local daemon and HTML

Every junction of `595e` after defined is recursive: the subproject `tableaud` does the work. The status file holds only the gate, and the state, the note and the date come from the subproject's task, read at the commit the junction's `url` fixes.

Glance:

| Field    | Value                                      |
|----------|--------------------------------------------|
| Task     | `595e` tableaud: local daemon and HTML     |
| Assignee | **nbyoung@nbyoung.com**                    |
| Parent   | `437e` Tableaux tooling, order 5           |
| Status   | 📝 defined · 🟢 nominal, 🪆 from the subproject `subprojects/tableaud` |
| Note     | prototype/49ce serves the ten views with a stdlib HEAD and .tableaux watcher, ETag 304 polling through htmx, a Source interface and a loopback Host check |
| Recorded | The gate on 2026-09-30 by noreply@anthropic.com; the state, the note and the date, 2026-09-30, by the subproject |

`tabloio task 595e --ref 3cdae52 --for nbyoung@nbyoung.com --level glance`

Detail, the parts that differ:

| Gate                    | Marks | Junction                                                                                 | Stands |
|-------------------------|:-----:|------------------------------------------------------------------------------------------|--------|
| 📝 defined              | 🤖👀  | noreply@anthropic.com on `claude-haiku`; reviewer the assignee, **nbyoung@nbyoung.com**   | passed; the status stands here |
| 📌 mockup               | 🪆    | Subproject `subprojects/tableaud`, its root task `8608` tableaud                          | next   |
| 🔧 function to 🚀 release | 🪆  | The same subproject and task at each of the seven gates                                   | later  |

🪆 a subproject does the work.

| Subproject snapshot | Value                                                                              |
|---------------------|------------------------------------------------------------------------------------|
| Task                | `8608` tableaud, the root of the subproject, assignee **nbyoung@nbyoung.com**      |
| Its status          | 🔧 function · 🟢 nominal, rolled up from its child `49ce` Server                   |
| Its note            | prototype/49ce serves the ten views with a stdlib HEAD and .tableaux watcher, ETag 304 polling through htmx, a Source interface and a loopback Host check |
| Its date            | 2026-09-30, the oldest among its children, from `7425` Bootstrap                   |
| Its children        | `7425` Bootstrap at 🧱 implementation; `49ce` Server, `097c` HTML views, `db74` Progressive disclosure, `6160` Static export and `5a2f` Accessibility and theming at 🔧 function; all 🟢 nominal |

The subproject's root stands at function, and `595e` records defined: the contributor advances the gate of `595e` by hand.

| Requires                                      | Edge                            | What passes                    | Condition            |
|-----------------------------------------------|---------------------------------|--------------------------------|----------------------|
| `77b2` tablo: backend library and plumbing    | implementation → implementation | The library it embeds          | not met, not yet due |
| `5fe3` HTML views                             | mockup → design                 | The HTML mockups it reproduces | not met, not yet due |

No task requires `595e`.

Provenance, the parts that differ:

| Linkage           | Value                                                                                |
|-------------------|--------------------------------------------------------------------------------------|
| `url`             | `subprojects/tableaud`, stated in `.tableaux/tasks/595e.yaml` at each of the eight junctions |
| Form of the `url` | A path that is a Git submodule, so the submodule's pin fixes the commit              |
| Pin               | `e6ec4ec`, in full `e6ec4ecc8c30fbaf85a392f186cc0b9caa8e4c8e`                        |
| `commit` field    | Not stated; nothing restates the pin in the task file                                |
| The pinned commit | `e6ec4ec` Accept the accessibility and theming function prototype, 2026-10-05, author and committer Norman Young, **nbyoung@nbyoung.com**, on the subproject's trunk `main` |
| `id`              | Not stated; the junction reads the subproject's root, `8608`                         |
| Pin set by        | `3cdae52` Advance tableaud to the eight function prototypes, 2026-10-05, author and committer Norman Young, **nbyoung@nbyoung.com**: the pin moves from `cffbfa6` to `e6ec4ec` |
| Gate recorded by  | `e66abe2` Record the defined gate for the subproject tasks, 2026-09-30, author and committer Claude Haiku 4.5, noreply@anthropic.com, `Model: claude-haiku-4-5-20251001`, which agrees with `claude-haiku` |
| Authorisation     | `6b6c99a` Plan the Tableaux tooling, 2026-09-29, author and committer Norman Young, **nbyoung@nbyoung.com** |

```
git ls-tree 3cdae52 subprojects/tableaud
git -C subprojects/tableaud show e6ec4ec:.tableaux/tasks/8608.yaml
```

The two requirements name their tasks by `id`, so the tool reads `77b2` and `5fe3` in this project at `3cdae52`. Neither crosses projects.

The task has eleven events of its own in this repository, and takes in the subproject's events up to the pin. The newest three of its own, newest first:

| Date       | Commit    | By                      | Event | What it records                                      |
|------------|-----------|-------------------------|-------|------------------------------------------------------|
| 2026-10-05 | `3cdae52` | **nbyoung@nbyoung.com** | pin   | `subprojects/tableaud` from `cffbfa6` to `e6ec4ec`   |
| 2026-10-02 | `552d38f` | **nbyoung@nbyoung.com** | pin   | `subprojects/tableaud` from `b06cad0` to `cffbfa6`   |
| 2026-10-02 | `fb8c0b2` | **nbyoung@nbyoung.com** | pin   | `subprojects/tableaud` from `2061a7f` to `b06cad0`   |
| … and 8 earlier: 6 pin, 1 status, 1 task | | | | |

```
git log --format='%as %h %ae' 3cdae52 -- .tableaux/tasks/595e.yaml .tableaux/status/595e.yaml subprojects/tableaud
```

`tabloio task 595e --ref 3cdae52 --for nbyoung@nbyoung.com --level provenance`

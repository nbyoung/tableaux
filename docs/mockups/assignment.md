# Task assignment

What does each person carry? This view lists, for each email in the project, the tasks it is assigned, the junctions where it contributes or reviews, and the subtrees it has authority over.

Project Tableaux tooling · ref `main` at `3cdae52`, 2026-10-05 · viewer nbyoung@nbyoung.com, owner · person: every email · task: `437e`, the root. The legend for every symbol is the [gate definition](gates.md).

The three sections below are three renderings of the same view, one per level.

## Glance

`tabloio assignment --ref 3cdae52 --level glance`

| Email | Assigned | Contributes next | Reviews next | Models |
|---|--:|--:|--:|---|
| nbyoung@nbyoung.com | 10 | 0 | 26 | none: a person |
| noreply@anthropic.com | 27 | 28 | 2 | `claude-haiku`, `claude-opus`, `claude-fable`, `claude-sonnet` |

- 🪆 4 tasks hand their next junction to a subproject: `77b2`, `6103`, `c6e8` and `595e`, each at 📌 mockup. Nobody in this project contributes or reviews there, so the 32 leaf tasks give 28 next junctions with a contributor here and 4 without.
- The agent's 2 reviews are of its own work, `e9c6` at 🧱 implementation and `fcec` at 📏 unit: the junction states no reviewer, so the assignee reviews, and the agent is the assignee.
- Next, the agent runs `claude-opus` at 23 junctions and `claude-sonnet` at 5.
- A count covers leaf tasks: a parent has no work of its own, and its junctions state defaults for its children.

## Detail

`tabloio assignment --ref 3cdae52 --level detail`

`--for EMAIL` renders one section. A junction is **next** when it is the task's next applicable gate, passed when the status stands at or after it, and later otherwise. A group of more than eight rows shows its first three and folds the rest.

### nbyoung@nbyoung.com

The owner: the assignee of the root `437e`, so an authority of every task. A person; no junction states a model for this email.

#### Tasks assigned: 10

| Task | Title | Under | Status | Next junction |
|---|---|---|---|---|
| `437e` | Tableaux tooling | root | 📝 defined 🟢 nominal, rolled up from `99f0` | parent: states defaults |
| `bc63` | Method | `437e` | 📝 defined 🟢 nominal, rolled up from `99f0` | parent: states defaults |
| `2034` | Views | `bc63` | 📝 defined 🟢 nominal, rolled up from `99f0` | parent: states defaults |
| `ac33` | Agent identity | `bc63` | 📐 design 🟢 nominal | 🧱 implementation 🤖👀 |
| `9f3f` | Subproject linkage | `bc63` | 📐 design 🟢 nominal | 🧱 implementation 🤖👀 |
| `7166` | Language clarifications | `bc63` | 📐 design 🟢 nominal | 🧱 implementation 🤖👀 |
| `77b2` | tablo: backend library and plumbing | `437e` | 📝 defined 🟢 nominal, state from the subproject | 📌 mockup 🪆 |
| `6103` | tabloio: command line, output and input | `437e` | 📝 defined 🟢 nominal, state from the subproject | 📌 mockup 🪆 |
| `c6e8` | tablotui: terminal user interface | `437e` | 📝 defined 🟢 nominal, state from the subproject | 📌 mockup 🪆 |
| `595e` | tableaud: local daemon and HTML | `437e` | 📝 defined 🟢 nominal, state from the subproject | 📌 mockup 🪆 |

🤖👀 an agent contributes and a person reviews · 🤖 an agent contributes and reviews its own work · 🪆 a subproject does the work.

**No contributor in this project.** The next junction of four of these tasks is recursive, so the work belongs to a subproject and no email here contributes or reviews it. Each subproject's own assignment view says who does.

| Task | Next gate | Subproject | Its root task stands at |
|---|---|---|---|
| `77b2` | 📌 mockup 🪆 | `subprojects/tablo` | `b2c1` 📝 defined 🟢 nominal |
| `6103` | 📌 mockup 🪆 | `subprojects/tabloio` | `07e0` 🔧 function 🟢 nominal |
| `c6e8` | 📌 mockup 🪆 | `subprojects/tablotui` | `40e8` 🔧 function 🟢 nominal |
| `595e` | 📌 mockup 🪆 | `subprojects/tableaud` | `8608` 🔧 function 🟢 nominal |

#### Contributes: 8 junctions, 0 next

**🚀 release** · 8 junctions · 0 next

| Task | Title | Model | Reviewer | When |
|---|---|---|---|---|
| `c2ad` | Roles | none: a person | none | later |
| `e9c6` | Abstract views | none: a person | none | later |
| `e3cb` | Schema files | none: a person | none | later |
| `fcec` | Conformance corpus | none: a person | none | later |
| `ac33` | Agent identity | none: a person | none | later |
| `9f3f` | Subproject linkage | none: a person | none | later |
| `7861` | Productivity evidence | none: a person | none | later |
| `7166` | Language clarifications | none: a person | none | later |

#### Reviews: 46 junctions, 26 next

**📝 defined** · 7 junctions · 0 next

| Task | Title | Contributor | Model | When |
|---|---|---|---|---|
| `ac33` | Agent identity | noreply@anthropic.com | `claude-haiku` | passed |
| `9f3f` | Subproject linkage | noreply@anthropic.com | `claude-haiku` | passed |
| `7166` | Language clarifications | noreply@anthropic.com | `claude-haiku` | passed |
| `77b2` | tablo: backend library and plumbing | noreply@anthropic.com | `claude-haiku` | passed |
| `6103` | tabloio: command line, output and input | noreply@anthropic.com | `claude-haiku` | passed |
| `c6e8` | tablotui: terminal user interface | noreply@anthropic.com | `claude-haiku` | passed |
| `595e` | tableaud: local daemon and HTML | noreply@anthropic.com | `claude-haiku` | passed |

At 📝 defined the authorisation stands as the review.

**📌 mockup** · 20 junctions · 20 next

| Task | Title | Contributor | Model | When |
|---|---|---|---|---|
| `99f0` | Gate definition view in Markdown | noreply@anthropic.com | `claude-opus` | **next** |
| `05a9` | Task definition view in Markdown | noreply@anthropic.com | `claude-opus` | **next** |
| `a9ce` | Authority delegation view in Markdown | noreply@anthropic.com | `claude-opus` | **next** |

… and 17 more: 7 under `bc86` Markdown views, 10 under `5fe3` HTML views; each next.

**📐 design** · 8 junctions · 0 next

| Task | Title | Contributor | Model | When |
|---|---|---|---|---|
| `c2ad` | Roles | noreply@anthropic.com | `claude-fable` | passed |
| `e9c6` | Abstract views | noreply@anthropic.com | `claude-fable` | passed |
| `e3cb` | Schema files | noreply@anthropic.com | `claude-fable` | passed |
| `fcec` | Conformance corpus | noreply@anthropic.com | `claude-fable` | passed |
| `ac33` | Agent identity | noreply@anthropic.com | `claude-fable` | passed |
| `9f3f` | Subproject linkage | noreply@anthropic.com | `claude-fable` | passed |
| `7861` | Productivity evidence | noreply@anthropic.com | `claude-fable` | passed |
| `7166` | Language clarifications | noreply@anthropic.com | `claude-fable` | passed |

**🧱 implementation** · 3 junctions · 3 next

| Task | Title | Contributor | Model | When |
|---|---|---|---|---|
| `ac33` | Agent identity | noreply@anthropic.com | `claude-sonnet` | **next** |
| `9f3f` | Subproject linkage | noreply@anthropic.com | `claude-sonnet` | **next** |
| `7166` | Language clarifications | noreply@anthropic.com | `claude-sonnet` | **next** |

**🌍 validate** · 8 junctions · 3 next

| Task | Title | Contributor | Model | When |
|---|---|---|---|---|
| `c2ad` | Roles | noreply@anthropic.com | `claude-opus` | **next** |
| `e9c6` | Abstract views | noreply@anthropic.com | `claude-opus` | later |
| `e3cb` | Schema files | noreply@anthropic.com | `claude-opus` | **next** |
| `fcec` | Conformance corpus | noreply@anthropic.com | `claude-opus` | later |
| `ac33` | Agent identity | noreply@anthropic.com | `claude-opus` | later |
| `9f3f` | Subproject linkage | noreply@anthropic.com | `claude-opus` | later |
| `7861` | Productivity evidence | noreply@anthropic.com | `claude-opus` | **next** |
| `7166` | Language clarifications | noreply@anthropic.com | `claude-opus` | later |

#### Counts by gate

| Gate | Tasks standing here | Contributes | of which next | Reviews | of which next |
|---|--:|--:|--:|--:|--:|
| 📝 defined | 7 | 0 | 0 | 7 | 0 |
| 📌 mockup | 0 | 0 | 0 | 20 | 20 |
| 🔧 function | 0 | 0 | 0 | 0 | 0 |
| 📐 design | 3 | 0 | 0 | 8 | 0 |
| 🧱 implementation | 0 | 0 | 0 | 3 | 3 |
| 📏 unit | 0 | 0 | 0 | 0 | 0 |
| 🔗 integrate | 0 | 0 | 0 | 0 | 0 |
| 🌍 validate | 0 | 0 | 0 | 8 | 3 |
| 🚀 release | 0 | 8 | 0 | 0 | 0 |
| **Total** | **10** | **8** | **0** | **46** | **26** |

#### Authority

Over `437e` Tableaux tooling and its 36 descendants: every task. See [authority](authority.md).

### noreply@anthropic.com

🤖 An agent: every junction where this email contributes states a model. Assignee of 25 leaf tasks and of the two parents `bc86` and `5fe3`.

#### Tasks assigned: 27

| Task | Title | Under | Status | Next junction |
|---|---|---|---|---|
| `c2ad` | Roles | `bc63` | 🧱 implementation 🟢 nominal | 🌍 validate 🤖👀 |
| `e9c6` | Abstract views | `2034` | 📐 design 🟢 nominal | 🧱 implementation 🤖 |
| `bc86` | Markdown views | `2034` | 📝 defined 🟢 nominal, rolled up from `99f0` | parent: states defaults |
| … | 10 children: `99f0` `05a9` `a9ce` `bb7c` `c74a` `efff` `ab8e` `c545` `d615` `b14e` | `bc86` | each 📝 defined 🟢 nominal | each 📌 mockup 🤖👀 |
| `5fe3` | HTML views | `2034` | 📝 defined 🟢 nominal, rolled up from `a6f7` | parent: states defaults |
| … | 10 children: `a6f7` `7dff` `b1b7` `ea51` `7783` `5471` `32e7` `69eb` `3194` `a8b4` | `5fe3` | each 📝 defined 🟢 nominal | each 📌 mockup 🤖👀 |
| `e3cb` | Schema files | `bc63` | 📏 unit 🟢 nominal | 🌍 validate 🤖👀 |
| `fcec` | Conformance corpus | `bc63` | 🧱 implementation 🟢 nominal | 📏 unit 🤖 |
| `7861` | Productivity evidence | `bc63` | 🧱 implementation 🟢 nominal | 🌍 validate 🤖👀 |

🤖👀 an agent contributes and a person reviews · 🤖 an agent contributes and reviews its own work · 🪆 a subproject does the work.

#### Contributes: 79 junctions, 28 next

**📝 defined** · 32 junctions · 0 next

| Task | Title | Model | Reviewer | When |
|---|---|---|---|---|
| `c2ad` | Roles | `claude-haiku` | noreply@anthropic.com | passed |
| `e9c6` | Abstract views | `claude-haiku` | noreply@anthropic.com | passed |
| `99f0` | Gate definition view in Markdown | `claude-haiku` | noreply@anthropic.com | passed |

… and 29 more: `e3cb` `fcec` `ac33` `9f3f` `7861` `7166` `77b2` `6103` `c6e8` `595e`, 9 under `bc86` Markdown views, 10 under `5fe3` HTML views; each passed.

**📌 mockup** · 20 junctions · 20 next

| Task | Title | Model | Reviewer | When |
|---|---|---|---|---|
| `99f0` | Gate definition view in Markdown | `claude-opus` | nbyoung@nbyoung.com | **next** |
| `05a9` | Task definition view in Markdown | `claude-opus` | nbyoung@nbyoung.com | **next** |
| `a9ce` | Authority delegation view in Markdown | `claude-opus` | nbyoung@nbyoung.com | **next** |

… and 17 more: 7 under `bc86` Markdown views, 10 under `5fe3` HTML views; each next.

**📐 design** · 8 junctions · 0 next

| Task | Title | Model | Reviewer | When |
|---|---|---|---|---|
| `c2ad` | Roles | `claude-fable` | nbyoung@nbyoung.com | passed |
| `e9c6` | Abstract views | `claude-fable` | nbyoung@nbyoung.com | passed |
| `e3cb` | Schema files | `claude-fable` | nbyoung@nbyoung.com | passed |
| `fcec` | Conformance corpus | `claude-fable` | nbyoung@nbyoung.com | passed |
| `ac33` | Agent identity | `claude-fable` | nbyoung@nbyoung.com | passed |
| `9f3f` | Subproject linkage | `claude-fable` | nbyoung@nbyoung.com | passed |
| `7861` | Productivity evidence | `claude-fable` | nbyoung@nbyoung.com | passed |
| `7166` | Language clarifications | `claude-fable` | nbyoung@nbyoung.com | passed |

**🧱 implementation** · 8 junctions · 4 next

| Task | Title | Model | Reviewer | When |
|---|---|---|---|---|
| `c2ad` | Roles | `claude-sonnet` | noreply@anthropic.com | passed |
| `e9c6` | Abstract views | `claude-sonnet` | noreply@anthropic.com | **next** |
| `e3cb` | Schema files | `claude-sonnet` | noreply@anthropic.com | passed |
| `fcec` | Conformance corpus | `claude-sonnet` | noreply@anthropic.com | passed |
| `ac33` | Agent identity | `claude-sonnet` | nbyoung@nbyoung.com | **next** |
| `9f3f` | Subproject linkage | `claude-sonnet` | nbyoung@nbyoung.com | **next** |
| `7861` | Productivity evidence | `claude-sonnet` | noreply@anthropic.com | passed |
| `7166` | Language clarifications | `claude-sonnet` | nbyoung@nbyoung.com | **next** |

**📏 unit** · 2 junctions · 1 next

| Task | Title | Model | Reviewer | When |
|---|---|---|---|---|
| `e3cb` | Schema files | `claude-sonnet` | noreply@anthropic.com | passed |
| `fcec` | Conformance corpus | `claude-sonnet` | noreply@anthropic.com | **next** |

**🔗 integrate** · 1 junction · 0 next

| Task | Title | Model | Reviewer | When |
|---|---|---|---|---|
| `fcec` | Conformance corpus | `claude-sonnet` | noreply@anthropic.com | later |

**🌍 validate** · 8 junctions · 3 next

| Task | Title | Model | Reviewer | When |
|---|---|---|---|---|
| `c2ad` | Roles | `claude-opus` | nbyoung@nbyoung.com | **next** |
| `e9c6` | Abstract views | `claude-opus` | nbyoung@nbyoung.com | later |
| `e3cb` | Schema files | `claude-opus` | nbyoung@nbyoung.com | **next** |
| `fcec` | Conformance corpus | `claude-opus` | nbyoung@nbyoung.com | later |
| `ac33` | Agent identity | `claude-opus` | nbyoung@nbyoung.com | later |
| `9f3f` | Subproject linkage | `claude-opus` | nbyoung@nbyoung.com | later |
| `7861` | Productivity evidence | `claude-opus` | nbyoung@nbyoung.com | **next** |
| `7166` | Language clarifications | `claude-opus` | nbyoung@nbyoung.com | later |

**Models by gate.** One email stands for four models; the junction names the model.

| Gate | Model | Stated by | Junctions | Next | Note |
|---|---|---|--:|--:|---|
| 📝 defined | `claude-haiku` | `437e` | 32 | 0 |  |
| 📌 mockup | `claude-opus` | `437e` | 20 | 20 |  |
| 🔧 function | `claude-sonnet` | `437e` | 0 | 0 | no task has a function junction of its own: each is exempt or recursive |
| 📐 design | `claude-fable` | `bc63` | 8 | 0 | `437e` states `claude-opus`; `bc63` restates the model for the Method branch, and every task with a design junction of its own sits under it |
| 🧱 implementation | `claude-sonnet` | `437e` | 8 | 4 |  |
| 📏 unit | `claude-sonnet` | `437e` | 2 | 1 |  |
| 🔗 integrate | `claude-sonnet` | `437e` | 1 | 0 |  |
| 🌍 validate | `claude-opus` | `bc63` | 8 | 3 | `437e` states `claude-sonnet`; `bc63` restates the model for the Method branch, and every task with a validate junction of its own sits under it |

At 🚀 release the owner contributes, so no model applies.

#### Reviews: 33 junctions, 2 next

Every one is the agent's own work: `437e` states no reviewer at these gates, so the assignee reviews, and the agent is the assignee.

**📝 defined** · 25 junctions · 0 next

| Task | Title | Contributor | Model | When |
|---|---|---|---|---|
| `c2ad` | Roles | noreply@anthropic.com | `claude-haiku` | passed |
| `e9c6` | Abstract views | noreply@anthropic.com | `claude-haiku` | passed |
| `99f0` | Gate definition view in Markdown | noreply@anthropic.com | `claude-haiku` | passed |

… and 22 more: `e3cb` `fcec` `7861`, 9 under `bc86` Markdown views, 10 under `5fe3` HTML views; each passed.

At 📝 defined the authorisation stands as the review.

**🧱 implementation** · 5 junctions · 1 next

| Task | Title | Contributor | Model | When |
|---|---|---|---|---|
| `c2ad` | Roles | noreply@anthropic.com | `claude-sonnet` | passed |
| `e9c6` | Abstract views | noreply@anthropic.com | `claude-sonnet` | **next** |
| `e3cb` | Schema files | noreply@anthropic.com | `claude-sonnet` | passed |
| `fcec` | Conformance corpus | noreply@anthropic.com | `claude-sonnet` | passed |
| `7861` | Productivity evidence | noreply@anthropic.com | `claude-sonnet` | passed |

**📏 unit** · 2 junctions · 1 next

| Task | Title | Contributor | Model | When |
|---|---|---|---|---|
| `e3cb` | Schema files | noreply@anthropic.com | `claude-sonnet` | passed |
| `fcec` | Conformance corpus | noreply@anthropic.com | `claude-sonnet` | **next** |

**🔗 integrate** · 1 junction · 0 next

| Task | Title | Contributor | Model | When |
|---|---|---|---|---|
| `fcec` | Conformance corpus | noreply@anthropic.com | `claude-sonnet` | later |

#### Counts by gate

| Gate | Tasks standing here | Contributes | of which next | Reviews | of which next |
|---|--:|--:|--:|--:|--:|
| 📝 defined | 22 | 32 | 0 | 25 | 0 |
| 📌 mockup | 0 | 20 | 20 | 0 | 0 |
| 🔧 function | 0 | 0 | 0 | 0 | 0 |
| 📐 design | 1 | 8 | 0 | 0 | 0 |
| 🧱 implementation | 3 | 8 | 4 | 5 | 1 |
| 📏 unit | 1 | 2 | 1 | 2 | 1 |
| 🔗 integrate | 0 | 1 | 0 | 1 | 0 |
| 🌍 validate | 0 | 8 | 3 | 0 | 0 |
| 🚀 release | 0 | 0 | 0 | 0 | 0 |
| **Total** | **27** | **79** | **28** | **33** | **2** |

#### Authority

Over `bc86` Markdown views and its 10 children, and over `5fe3` HTML views and its 10 children. A leaf gives no authority. See [authority](authority.md).

## Provenance

`tabloio assignment --ref 3cdae52 --level provenance`

This level adds, to each position of the detail, the file and the ancestor that states it, or the plain default, and the commit behind the line. It groups the positions that share a source.

### nbyoung@nbyoung.com

| Position | Tasks | Stated in |
|---|---|---|
| Assignee | 10: `437e` `bc63` `2034` `ac33` `9f3f` `7166` `77b2` `6103` `c6e8` `595e` | `assignee` in each task's own file, `.tableaux/tasks/ID.yaml`, commit `6b6c99a` |
| Authority | `437e` and its 36 descendants | `assignee` in `.tableaux/tasks/437e.yaml`, commit `6b6c99a`: the root is an ancestor of every other task |

| Contributes at | Tasks | Contributor and model from | Reviewer | Reviewer from |
|---|---|---|---|---|
| 🚀 release | 8: `c2ad` `e9c6` `e3cb` `fcec` `ac33` `9f3f` `7861` `7166` | `437e` Tableaux tooling, `junctions.release` in `.tableaux/tasks/437e.yaml`, commit `6b6c99a`; no model, since a person contributes | none | none: a person contributes, and no file states a reviewer |

| Reviews at | Tasks | Reviewer from | Contributor and model from |
|---|---|---|---|
| 📝 defined | 7: `ac33` `9f3f` `7166` `77b2` `6103` `c6e8` `595e` | plain default: no file states a reviewer at defined, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` | `437e` Tableaux tooling, `junctions.defined` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` |
| 📌 mockup | 20: the 20 mockups under `bc86` and `5fe3` | `437e` Tableaux tooling, `junctions.mockup` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` | `437e` Tableaux tooling, `junctions.mockup` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` |
| 📐 design | 8: `c2ad` `e9c6` `e3cb` `fcec` `ac33` `9f3f` `7861` `7166` | `437e` Tableaux tooling, `junctions.design` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` | `bc63` Method, `junctions.design` in `.tableaux/tasks/bc63.yaml`, commit `320cf2b` |
| 🧱 implementation | 3: `ac33` `9f3f` `7166` | plain default: no file states a reviewer at implementation, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` | `437e` Tableaux tooling, `junctions.implementation` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` |
| 🌍 validate | 8: `c2ad` `e9c6` `e3cb` `fcec` `ac33` `9f3f` `7861` `7166` | `437e` Tableaux tooling, `junctions.validate` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` | `bc63` Method, `junctions.validate` in `.tableaux/tasks/bc63.yaml`, commit `320cf2b` |

No position, since the junction is recursive: each task's own file states it, a recursive junction inherits nothing, and the submodule pin fixes the commit the subproject is read at.

| Task | Stated in | Pinned at |
|---|---|---|
| `77b2` | `junctions.mockup.subproject.url: subprojects/tablo` in `.tableaux/tasks/77b2.yaml`, commit `6b6c99a` | `00f8f68` |
| `6103` | `junctions.mockup.subproject.url: subprojects/tabloio` in `.tableaux/tasks/6103.yaml`, commit `6b6c99a` | `4593882` |
| `c6e8` | `junctions.mockup.subproject.url: subprojects/tablotui` in `.tableaux/tasks/c6e8.yaml`, commit `6b6c99a` | `a2878b5` |
| `595e` | `junctions.mockup.subproject.url: subprojects/tableaud` in `.tableaux/tasks/595e.yaml`, commit `6b6c99a` | `e6ec4ec` |

### noreply@anthropic.com

| Position | Tasks | Stated in |
|---|---|---|
| Assignee | 27: `c2ad` `e9c6` `bc86` `5fe3` `e3cb` `fcec` `7861` and the 20 mockups | `assignee` in each task's own file, `.tableaux/tasks/ID.yaml`, commit `6b6c99a` |
| Authority | the 10 children of `bc86`, the 10 children of `5fe3` | `assignee` in `.tableaux/tasks/bc86.yaml` and `.tableaux/tasks/5fe3.yaml`, commit `6b6c99a`: each is the parent of its ten mockups |

| Contributes at | Tasks | Contributor and model from | Reviewer | Reviewer from |
|---|---|---|---|---|
| 📝 defined | 25: `c2ad` `e9c6` `99f0` `05a9` `a9ce` `bb7c` `c74a` `efff` `ab8e` `c545` `d615` `b14e` `a6f7` `7dff` `b1b7` `ea51` `7783` `5471` `32e7` `69eb` `3194` `a8b4` `e3cb` `fcec` `7861` | `437e` Tableaux tooling, `junctions.defined` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` | noreply@anthropic.com | plain default: no file states a reviewer at defined, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` |
| 📝 defined | 7: `ac33` `9f3f` `7166` `77b2` `6103` `c6e8` `595e` | `437e` Tableaux tooling, `junctions.defined` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` | nbyoung@nbyoung.com | plain default: no file states a reviewer at defined, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` |
| 📌 mockup | 20: the 20 mockups under `bc86` and `5fe3` | `437e` Tableaux tooling, `junctions.mockup` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` | nbyoung@nbyoung.com | `437e` Tableaux tooling, `junctions.mockup` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` |
| 📐 design | 8: `c2ad` `e9c6` `e3cb` `fcec` `ac33` `9f3f` `7861` `7166` | `bc63` Method, `junctions.design` in `.tableaux/tasks/bc63.yaml`, commit `320cf2b` | nbyoung@nbyoung.com | `437e` Tableaux tooling, `junctions.design` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` |
| 🧱 implementation | 5: `c2ad` `e9c6` `e3cb` `fcec` `7861` | `437e` Tableaux tooling, `junctions.implementation` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` | noreply@anthropic.com | plain default: no file states a reviewer at implementation, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` |
| 🧱 implementation | 3: `ac33` `9f3f` `7166` | `437e` Tableaux tooling, `junctions.implementation` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` | nbyoung@nbyoung.com | plain default: no file states a reviewer at implementation, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` |
| 📏 unit | 2: `e3cb` `fcec` | `437e` Tableaux tooling, `junctions.unit` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` | noreply@anthropic.com | plain default: no file states a reviewer at unit, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` |
| 🔗 integrate | 1: `fcec` | `437e` Tableaux tooling, `junctions.integrate` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` | noreply@anthropic.com | plain default: no file states a reviewer at integrate, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` |
| 🌍 validate | 8: `c2ad` `e9c6` `e3cb` `fcec` `ac33` `9f3f` `7861` `7166` | `bc63` Method, `junctions.validate` in `.tableaux/tasks/bc63.yaml`, commit `320cf2b` | nbyoung@nbyoung.com | `437e` Tableaux tooling, `junctions.validate` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` |

| Reviews at | Tasks | Reviewer from | Contributor and model from |
|---|---|---|---|
| 📝 defined | 25: `c2ad` `e9c6` `99f0` `05a9` `a9ce` `bb7c` `c74a` `efff` `ab8e` `c545` `d615` `b14e` `a6f7` `7dff` `b1b7` `ea51` `7783` `5471` `32e7` `69eb` `3194` `a8b4` `e3cb` `fcec` `7861` | plain default: no file states a reviewer at defined, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` | `437e` Tableaux tooling, `junctions.defined` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` |
| 🧱 implementation | 5: `c2ad` `e9c6` `e3cb` `fcec` `7861` | plain default: no file states a reviewer at implementation, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` | `437e` Tableaux tooling, `junctions.implementation` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` |
| 📏 unit | 2: `e3cb` `fcec` | plain default: no file states a reviewer at unit, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` | `437e` Tableaux tooling, `junctions.unit` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` |
| 🔗 integrate | 1: `fcec` | plain default: no file states a reviewer at integrate, so the assignee reviews the agent; `assignee` in each task's own file, commit `6b6c99a` | `437e` Tableaux tooling, `junctions.integrate` in `.tableaux/tasks/437e.yaml`, commit `320cf2b` |

### Commits

| Lines | Commit | Date | Author | Committer |
|---|---|---|---|---|
| `assignee` in all 37 task files; `junctions.release` in `437e` | `6b6c99a` Plan the Tableaux tooling | 2026-09-29 | nbyoung@nbyoung.com | nbyoung@nbyoung.com |
| `junctions.defined` to `junctions.validate` in `437e`; `junctions.design` and `junctions.validate` in `bc63` | `320cf2b` Name a model family per gate (D7) | 2026-09-30 | noreply@anthropic.com | nbyoung@nbyoung.com |

`320cf2b` reaches the trunk through the merge `8eb0cae` by nbyoung@nbyoung.com on 2026-09-30. The four submodule pins come from the tree at `3cdae52`.

### Reproduce

```
git show 3cdae52:.tableaux/tasks/437e.yaml              # the defaults every task inherits
git show 3cdae52:.tableaux/tasks/bc63.yaml              # the Method branch restates design and validate
git blame -s 3cdae52 -- .tableaux/tasks/437e.yaml       # the commit behind each junction line
git grep -n '^assignee:' 3cdae52 -- .tableaux/tasks     # every assignee
git ls-tree 3cdae52 subprojects/                        # the four pins
```

## See also

- [Queue](queue.md): what each person does next, in order
- [Authority](authority.md): the subtrees and who accepts what
- [Task](task.md): one task with every junction
- [Tableau](tableau.md): the whole project by gate
- [My corner](context.md): a person’s tasks among their neighbours
- [Blockage](blockage.md): what waits on what
- [History](history.md): who did what, when
- [Audit](audit.md): the model each commit ran against the model its junction states
- [Gates](gates.md): the legend for every symbol

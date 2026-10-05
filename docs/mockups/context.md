# Contextual tableau

**How does my corner stand?** This file draws the contextual tableau of the Tableaux tooling plan as `tabloio` writes it in Markdown, once per level: glance, detail, provenance. The main picture is the **task form**, the subtree under one task; the [person form](#the-person-form) follows.

| Parameter            | Value                                                        |
|----------------------|--------------------------------------------------------------|
| ref                  | `main` at `3cdae52`, 2026-10-05                              |
| task                 | `2034` Views                                                 |
| person               | not set, since the view takes a task or a person, one of them |
| window               | one column either side of the next gates in view: 📝 to 📏    |
| historical junctions | off                                                          |
| viewer               | nbyoung@nbyoung.com, the owner and the assignee of `2034`      |
| level                | one per section below                                        |

**Reading a cell.** A column is a gate: ❔ undefined, 📝 defined, 📌 mockup, 🔧 function, 📐 design, 🧱 implementation, 📏 unit, 🔗 integrate, 🌍 validate, 🚀 release. The state symbol sits in the column of the gate the status names: 🟢 nominal. A later cell holds the junction marks: 🤖 an agent contributes, 👀 a reviewer accepts, 🪆 a subproject does the work, — the gate does not apply. A cell before the state symbol is historical and stays empty. A parent's title is bold; its row shows its roll-up and the marks of the defaults its children inherit. A number in brackets after a parent's title counts the children the table does not draw. [gates.md](gates.md) defines every symbol and gate.

**The window.** The next gates of the tasks in view are 📌 mockup, for `2034`, `bc86`, `5fe3` and the twenty mockups, and 🧱 implementation, for `e9c6`, which stands at 📐 design. One column either side gives the window 📝 to 📏. The columns outside fold: ❔ alone, and 🔗 🌍 🚀 as one column headed `🔗 … 🚀`. The first row of a table carries, in each folded column, the count of tasks in view whose current gate lies there: none on either side. The window follows the task and its subtree; the spine and the siblings that detail adds appear in the same window and do not widen it.

**Since VIEWS.md.** The example in VIEWS.md shows 2026-09-30, when `e9c6` stands at 📝 and the window runs 📝 to 🧱. `e9c6` has since passed design, so the window gains 📏 and the fold on the right starts at 🔗.

The whole project stands in [tableau.md](tableau.md). One task opens in [task.md](task.md); what the viewer does next stands in [queue.md](queue.md), and what waits on what in [blockage.md](blockage.md).

## Glance

The task and its children, in the window. The ten children of `bc86` and the ten of `5fe3` stay collapsed.

| Id | Task | ❔ | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 … 🚀 |
|--------|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `2034` | **Views** | 0 | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 0 |
| `e9c6` | &nbsp;&nbsp;Abstract views |   |   |   |   | 🟢 | 🤖 | — |   |
| `bc86` | &nbsp;&nbsp;**Markdown views** (10) |   | 🟢 | 🤖👀 | — | — | — | — |   |
| `5fe3` | &nbsp;&nbsp;**HTML views** (10) |   | 🟢 | 🤖👀 | — | — | — | — |   |

`tabloio context --task 2034 --level glance`

## Detail

Detail opens every row of the subtree and adds the spine, `437e` and `bc63`, and the seven siblings of `2034`, each labelled after its title. It adds the date and the note of each row, and the count of each folded column gate by gate. A parent's note names the child it rolls up from.

| Id | Task | ❔ | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 … 🚀 | Date | Note |
|--------|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|------------|------|
| `437e` | **Tableaux tooling** · spine | 0 | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 0 | 2026-09-29 | from `bc63`: Mockup waits for Abstract views (e9c6) at design |
| `bc63` | &nbsp;&nbsp;**Method** · spine |   | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 |   | 2026-09-29 | from `2034`: Mockup waits for Abstract views (e9c6) at design |
| `c2ad` | &nbsp;&nbsp;&nbsp;&nbsp;Roles · sibling |   |   |   |   |   | 🟢 | — |   | 2026-09-30 | The Roles text is on the trunk and covers all seven roles; the validate gate awaits the owner |
| `2034` | &nbsp;&nbsp;&nbsp;&nbsp;**Views** |   | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 |   | 2026-09-29 | from `bc86`: Mockup waits for Abstract views (e9c6) at design |
| `e9c6` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abstract views |   |   |   |   | 🟢 | 🤖 | — |   | 2026-09-30 | VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place |
| `bc86` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Markdown views** |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | from `99f0`: Mockup waits for Abstract views (e9c6) at design |
| `99f0` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gate definition view in Markdown |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `05a9` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task definition view in Markdown |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `a9ce` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authority delegation view in Markdown |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `bb7c` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task assignment view in Markdown |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `c74a` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contributor work queue view in Markdown |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `efff` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Work-blockage tree view in Markdown |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `ab8e` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Global tableau view in Markdown |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `c545` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contextual tableau view in Markdown |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `d615` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;History view in Markdown |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `b14e` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Audit view in Markdown |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `5fe3` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HTML views** |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | from `a6f7`: Mockup waits for Abstract views (e9c6) at design |
| `a6f7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gate definition view in Html |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `7dff` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task definition view in Html |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `b1b7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authority delegation view in Html |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `ea51` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task assignment view in Html |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `7783` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contributor work queue view in Html |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `5471` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Work-blockage tree view in Html |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `32e7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Global tableau view in Html |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `69eb` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contextual tableau view in Html |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `3194` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;History view in Html |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `a8b4` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Audit view in Html |   | 🟢 | 🤖👀 | — | — | — | — |   | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design |
| `e3cb` | &nbsp;&nbsp;&nbsp;&nbsp;Schema files · sibling |   |   |   |   |   |   | 🟢 |   | 2026-09-30 | schemas/check.sh (files agree with SYNTAX.md, version 0.2.1) and schemas/load.py (files load as JSON Schema 2020-12) pass; every .tableaux file validates |
| `fcec` | &nbsp;&nbsp;&nbsp;&nbsp;Conformance corpus · sibling |   |   |   |   |   | 🟢 | 🤖 |   | 2026-09-30 | The corpus builds and checks clean, with 85 entries on the trunk; all three corrections from the tablo prototypes are in; the unit gate runs the tablo conformance test against it |
| `ac33` | &nbsp;&nbsp;&nbsp;&nbsp;Agent identity · sibling |   |   |   |   | 🟢 | 🤖👀 | — |   | 2026-09-30 | The model plan-and-record rule (F20) is on the trunk; F1, F2 and F10 remain for design |
| `9f3f` | &nbsp;&nbsp;&nbsp;&nbsp;Subproject linkage · sibling |   |   |   |   | 🟢 | 🤖👀 | — |   | 2026-09-30 | The subproject linkage rule (F3, F5, F12) is on the trunk at language 0.3.0; tablo and the subprojects follow |
| `7861` | &nbsp;&nbsp;&nbsp;&nbsp;Productivity evidence · sibling |   |   |   |   |   | 🟢 | — |   | 2026-09-30 | The full report, its 23 tests and an example over five repositories are on the trunk |
| `7166` | &nbsp;&nbsp;&nbsp;&nbsp;Language clarifications · sibling |   |   |   |   | 🟢 | 🤖👀 | — |   | 2026-09-30 | The trunk clarification (F19) is on the trunk; F7 and F9 remain for design |

| Folded column | Gate         | Tasks |
|:-:|--------------|------:|
| ❔ | undefined    | 0 |
| 🔗 … 🚀 | integrate | 0 |
| 🔗 … 🚀 | validate  | 0 |
| 🔗 … 🚀 | release   | 0 |

The four subprojects `77b2`, `6103`, `c6e8` and `595e` are children of the spine's root and no siblings of `2034`, so this view leaves them to [tableau.md](tableau.md). The viewer acts in the 👀 cells of the leaves: nbyoung@nbyoung.com reviews 📌 on the twenty mockups, and 🧱 on `ac33`, `9f3f` and `7166`. The twenty mockups keep the note their status files state, although `e9c6` now stands at design and the requirement is met; [blockage.md](blockage.md) and [audit.md](audit.md) report on such waits.

`tabloio context --task 2034 --level detail`

## Provenance

Provenance repeats the detail tables above unchanged and adds, beneath them, the Git fact behind each cell: the deciding commit of each status, the child each parent rolls up from, and the ancestor that states each mark.

**Status cells.** The date is the author date of the deciding commit and the recorder its author.

| Cell | Date | Recorder | Commit | Committer | Trailers |
|------|------|----------|--------|-----------|----------|
| `c2ad` 🧱 | 2026-09-30 | noreply@anthropic.com | `3d8ce0e` Record the Roles task at its implementation gate | noreply@anthropic.com | `Model: claude-sonnet-5-5`, `Reviewed: c2ad implementation` |
| `e9c6` 📐 | 2026-09-30 | noreply@anthropic.com | `879b447` Advance the abstract views task to its design gate | noreply@anthropic.com | `Model: claude-fable-5-1` |
| `99f0` … `b14e`, ten, 📝 | 2026-09-29 | noreply@anthropic.com | `1a17bfc` Record the defined gate for the views and mockups | nbyoung@nbyoung.com | none |
| `a6f7` … `a8b4`, ten, 📝 | 2026-09-29 | noreply@anthropic.com | `1a17bfc` Record the defined gate for the views and mockups | nbyoung@nbyoung.com | none |
| `e3cb` 📏 | 2026-09-30 | noreply@anthropic.com | `5cbec7c` Record e3cb at unit, nominal | noreply@anthropic.com | `Model: claude-sonnet-5-5`, `Reviewed: e3cb unit` |
| `fcec` 🧱 | 2026-09-30 | noreply@anthropic.com | `60495c2` Record all three corpus corrections at implementation | noreply@anthropic.com | `Model: claude-sonnet-5-5`, `Reviewed: fcec implementation` |
| `ac33` 📐 | 2026-09-30 | noreply@anthropic.com | `6762222` Advance the agent identity task to its design gate | nbyoung@nbyoung.com | `Model: claude-fable-5-1` |
| `9f3f` 📐 | 2026-09-30 | noreply@anthropic.com | `43d68e4` Advance the subproject linkage task to its design gate | noreply@anthropic.com | `Model: claude-fable-5-1` |
| `7861` 🧱 | 2026-09-30 | noreply@anthropic.com | `c6f2655` Complete the productivity evidence report | noreply@anthropic.com | `Model: claude-sonnet-5-5`, `Reviewed: 7861 implementation` |
| `7166` 📐 | 2026-09-30 | noreply@anthropic.com | `d9396b4` Advance the language clarifications to their design gate | nbyoung@nbyoung.com | none |

The design junction of `e9c6` has a reviewer, so its status passes design by `0704a09` Accept the abstract views design, 2026-09-30, which nbyoung@nbyoung.com authors and commits with `Reviewed: e9c6 design`.

**Roll-ups.** A parent takes the earliest gate among its children, and the first child in display order where several tie; its date is the oldest among them.

| Parent | Shows | Rolls up from | Date |
|--------|-------|---------------|------|
| `437e` Tableaux tooling | 📝 🟢 | `bc63`, the first of five children at defined | 2026-09-29 |
| `bc63` Method | 📝 🟢 | `2034`, its one child at defined | 2026-09-29 |
| `2034` Views | 📝 🟢 | `bc86`, ahead of `5fe3` in display order | 2026-09-29 |
| `bc86` Markdown views | 📝 🟢 | `99f0`, the first of ten children at defined | 2026-09-29 |
| `5fe3` HTML views | 📝 🟢 | `a6f7`, the first of ten children at defined | 2026-09-29 |

**Marks.** Each mark resolves from the task's own entry, then its ancestors' entries nearest first, then the plain default.

| Rows | Cell | States it |
|------|------|-----------|
| the five parents and the twenty mockups | 📌 🤖👀 | `437e`: contributor noreply@anthropic.com, model `claude-opus`, reviewer nbyoung@nbyoung.com |
| `437e`, `bc63`, `2034` | 🔧 🤖, 🧱 🤖, 📏 🤖 | `437e`: contributor noreply@anthropic.com, model `claude-sonnet`, no reviewer |
| `437e` | 📐 🤖👀 | `437e`: contributor noreply@anthropic.com, model `claude-opus`, reviewer nbyoung@nbyoung.com |
| `bc63`, `2034` | 📐 🤖👀 | `bc63`: contributor noreply@anthropic.com, model `claude-fable`; `437e`: the reviewer |
| `e9c6` | 🧱 🤖 | `437e`: contributor and model `claude-sonnet`; no entry states a reviewer, and the assignee is the agent itself, so no 👀 |
| `fcec` | 📏 🤖 | `437e`: contributor and model `claude-sonnet`; the assignee is the agent itself, so no 👀 |
| `ac33`, `9f3f`, `7166` | 🧱 🤖👀 | `437e`: contributor and model `claude-sonnet`; no entry states a reviewer, so the assignee nbyoung@nbyoung.com reviews |
| `bc86` and its ten children | 🔧 📐 🧱 📏 — | `bc86`: `applies: false` at each gate |
| `5fe3` and its ten children | 🔧 📐 🧱 📏 — | `5fe3`: `applies: false` at each gate |
| `e9c6`, `c2ad`, `ac33`, `9f3f`, `7861`, `7166` | 📏 — | the task's own entry |

```
git log -1 --format='%as %ae %h' -- .tableaux/status/e9c6.yaml     # date, recorder and deciding commit
git log --format='%as %ae %h' -E --grep='^Reviewed: e9c6 '         # the reviews
```

[history.md](history.md) lists every event behind these commits, and [authority.md](authority.md) the commit that authorises each task.

`tabloio context --task 2034 --level provenance`

## The person form

With a person in place of a task, the view shows the tasks the person is assigned or contributes at next, their ancestors up to the root as a spine, and their siblings. The person form serves a contributor with few tasks. In this project both emails hold most of the tree: noreply@anthropic.com is assigned twenty-seven of the thirty-seven tasks, and nbyoung@nbyoung.com ten, among them the root and the Method and Views branches. The form drawn here is the owner's, which still leaves something out: the twenty-three tasks under `2034`. [assignment.md](assignment.md) lists what each email carries.

| Parameter            | Value                                                        |
|----------------------|--------------------------------------------------------------|
| ref                  | `main` at `3cdae52`, 2026-10-05                              |
| person               | nbyoung@nbyoung.com, the viewer, which is the default        |
| task                 | not set                                                      |
| window               | one column either side of the next gates in view: 📝 to 📏    |
| historical junctions | off                                                          |

The next gates of the ten tasks are 📌 mockup, for the three parents and the four subprojects, and 🧱 implementation, for `ac33`, `9f3f` and `7166`, so the window is again 📝 to 📏. nbyoung@nbyoung.com contributes at 🚀 release alone, which is nobody's next gate, so the tasks in view are the ten assigned ones.

### Glance

The person's own tasks, in the window.

| Id | Task | ❔ | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 … 🚀 |
|--------|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `437e` | **Tableaux tooling** | 0 | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 0 |
| `bc63` | &nbsp;&nbsp;**Method** (4) |   | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 |   |
| `2034` | &nbsp;&nbsp;&nbsp;&nbsp;**Views** (3) |   | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 |   |
| `ac33` | &nbsp;&nbsp;&nbsp;&nbsp;Agent identity |   |   |   |   | 🟢 | 🤖👀 | — |   |
| `9f3f` | &nbsp;&nbsp;&nbsp;&nbsp;Subproject linkage |   |   |   |   | 🟢 | 🤖👀 | — |   |
| `7166` | &nbsp;&nbsp;&nbsp;&nbsp;Language clarifications |   |   |   |   | 🟢 | 🤖👀 | — |   |
| `77b2` | &nbsp;&nbsp;tablo: backend library and plumbing |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |   |
| `6103` | &nbsp;&nbsp;tabloio: command line, output and input |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |   |
| `c6e8` | &nbsp;&nbsp;tablotui: terminal user interface |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |   |
| `595e` | &nbsp;&nbsp;tableaud: local daemon and HTML |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |   |

`tabloio context --person nbyoung@nbyoung.com --level glance`

### Detail

The spine adds no row here, since `437e` and `bc63` are the person's own. The siblings add four rows under `bc63`. A subproject's row takes its state, date and note from the subproject's root task at the commit the submodule pins.

| Id | Task | ❔ | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 … 🚀 | Date | Note |
|--------|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|------------|------|
| `437e` | **Tableaux tooling** | 0 | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 0 | 2026-09-29 | from `bc63`: Mockup waits for Abstract views (e9c6) at design |
| `bc63` | &nbsp;&nbsp;**Method** |   | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 |   | 2026-09-29 | from `2034`: Mockup waits for Abstract views (e9c6) at design |
| `c2ad` | &nbsp;&nbsp;&nbsp;&nbsp;Roles · sibling |   |   |   |   |   | 🟢 | — |   | 2026-09-30 | The Roles text is on the trunk and covers all seven roles; the validate gate awaits the owner |
| `2034` | &nbsp;&nbsp;&nbsp;&nbsp;**Views** (3) |   | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 |   | 2026-09-29 | from `bc86`: Mockup waits for Abstract views (e9c6) at design |
| `e3cb` | &nbsp;&nbsp;&nbsp;&nbsp;Schema files · sibling |   |   |   |   |   |   | 🟢 |   | 2026-09-30 | schemas/check.sh (files agree with SYNTAX.md, version 0.2.1) and schemas/load.py (files load as JSON Schema 2020-12) pass; every .tableaux file validates |
| `fcec` | &nbsp;&nbsp;&nbsp;&nbsp;Conformance corpus · sibling |   |   |   |   |   | 🟢 | 🤖 |   | 2026-09-30 | The corpus builds and checks clean, with 85 entries on the trunk; all three corrections from the tablo prototypes are in; the unit gate runs the tablo conformance test against it |
| `ac33` | &nbsp;&nbsp;&nbsp;&nbsp;Agent identity |   |   |   |   | 🟢 | 🤖👀 | — |   | 2026-09-30 | The model plan-and-record rule (F20) is on the trunk; F1, F2 and F10 remain for design |
| `9f3f` | &nbsp;&nbsp;&nbsp;&nbsp;Subproject linkage |   |   |   |   | 🟢 | 🤖👀 | — |   | 2026-09-30 | The subproject linkage rule (F3, F5, F12) is on the trunk at language 0.3.0; tablo and the subprojects follow |
| `7861` | &nbsp;&nbsp;&nbsp;&nbsp;Productivity evidence · sibling |   |   |   |   |   | 🟢 | — |   | 2026-09-30 | The full report, its 23 tests and an example over five repositories are on the trunk |
| `7166` | &nbsp;&nbsp;&nbsp;&nbsp;Language clarifications |   |   |   |   | 🟢 | 🤖👀 | — |   | 2026-09-30 | The trunk clarification (F19) is on the trunk; F7 and F9 remain for design |
| `77b2` | &nbsp;&nbsp;tablo: backend library and plumbing |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |   | 2026-09-30 | from `subprojects/tablo`: The design is next and no requirement gates it |
| `6103` | &nbsp;&nbsp;tabloio: command line, output and input |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |   | 2026-09-30 | from `subprojects/tabloio`: prototype/e3ed renders the gate and task definition views as Markdown at three levels from tablo view data |
| `c6e8` | &nbsp;&nbsp;tablotui: terminal user interface |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |   | 2026-09-30 | from `subprojects/tablotui`: prototype/679b renders the global tableau as a Bubble Tea grid with tree expand and collapse, scrolling, a folded gate window and hidden columns kept in a settings file; emoji lines align where the terminal widens U+FE0F |
| `595e` | &nbsp;&nbsp;tableaud: local daemon and HTML |   | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |   | 2026-09-30 | from `subprojects/tableaud`: prototype/49ce serves the ten views with a stdlib HEAD and .tableaux watcher, ETag 304 polling through htmx, a Source interface and a loopback Host check |

| Folded column | Gate         | Tasks |
|:-:|--------------|------:|
| ❔ | undefined    | 0 |
| 🔗 … 🚀 | integrate | 0 |
| 🔗 … 🚀 | validate  | 0 |
| 🔗 … 🚀 | release   | 0 |

The person acts in the 👀 cells of the leaves in view: nbyoung@nbyoung.com reviews 🧱 on `ac33`, `9f3f` and `7166`.

`tabloio context --person nbyoung@nbyoung.com --level detail`

### Provenance

Provenance adds the same three tables as the task form, over these rows, and the commit each subproject's snapshot is read at.

| Cell | Status file | Subproject at | Pin moves in | Root there | Rolls up from |
|------|-------------|---------------|--------------|------------|---------------|
| `77b2` 📝 🟢 | `e66abe2`, 2026-09-30, noreply@anthropic.com, `Model: claude-haiku-4-5-20251001` | `subprojects/tablo` at `00f8f68` | `552d38f`, 2026-10-02 | `b2c1` tablo, at defined | `4b4f` Conformance |
| `6103` 📝 🟢 | `e66abe2` | `subprojects/tabloio` at `4593882` | `1c0f04d`, 2026-10-02 | `07e0` tabloio, at function | `1093` Renderers, from `e3ed` |
| `c6e8` 📝 🟢 | `e66abe2` | `subprojects/tablotui` at `a2878b5` | `fa4551e`, 2026-10-04 | `40e8` tablotui, at function | `679b` Tableau grid |
| `595e` 📝 🟢 | `e66abe2` | `subprojects/tableaud` at `e6ec4ec` | `3cdae52`, 2026-10-05 | `8608` tableaud, at function | `49ce` Server |

Each subproject's status file in this project states the gate `defined` and nothing else; the 🟢 comes from the root task there. Three of those roots stand at function at the pin, and the rows stay at 📝 until a contributor advances the gate in this project's file.

`tabloio context --person nbyoung@nbyoung.com --level provenance`

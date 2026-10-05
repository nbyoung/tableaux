# Work-blockage tree

What waits on what? This view roots the waiting work at its causes and names, for each cause, the one action that resolves it and the one person who takes it.

Project Tableaux tooling · ref `main` at `3cdae52`, 2026-10-05 · viewer nbyoung@nbyoung.com, the owner · task `437e`, the whole tree · person: every person · window: every gate. The [gate definition](gates.md) explains each symbol.

The sections below show the three levels in order, each as the complete output of one rendering. The project holds no cause at this ref, so a fourth section, [an illustrative tree](#illustration-a-tree-with-causes), shows the form of a tree that holds some; it is not the project at the ref.

## Glance

`tabloio blockage --ref 3cdae52 --level glance`

**No cause holds any task.**

Next: 10 requirements are not yet due, and 8 of them are not met.

## Detail

`tabloio blockage --ref 3cdae52 --level detail`

**No cause holds any task.** The tree is empty; each kind of cause reads as follows.

| Kind of cause                         | The project at the ref                                                    | Causes |
|---------------------------------------|---------------------------------------------------------------------------|-------:|
| Unmet requirement                     | 32 entries: 22 due and met, 10 not yet due                                 | 0      |
| Status with a reason, or off nominal  | 32 leaves, four read through their snapshots: all 🟢 nominal, no ⛔ or 🪫   | 0      |
| Review outstanding                    | No status carries 👓 review                                                | 0      |
| Authorisation outstanding             | 37 tasks, all authorised                                                  | 0      |
| Subproject snapshot not advanced      | 4 pins, each at the tip of its subproject's trunk                          | 0      |

### Next: requirements not yet due

A requirement that is not yet due is no wait. It comes due when its task's next gate reaches the gate the entry names in `to`. The list follows display order.

- `77b2` **tablo: backend library and plumbing** stands at 📝 defined; next 📌 mockup 🪆. Its snapshot stands at 📝 defined.
  - at 🧱 implementation it requires `e3cb` Schema files at 🧱 implementation, "The schema files it embeds". Met: `e3cb` stands at 📏 unit. Due when `77b2` stands at 📐 design.
  - at 📐 design it requires `e9c6` Abstract views at 🧱 implementation, "The abstract views it derives". Not met: `e9c6` stands at 📐 design. Due when `77b2` stands at 🔧 function.
  - at 📏 unit it requires `fcec` Conformance corpus at 🧱 implementation, "The corpus it conforms to". Met: `fcec` stands at 🧱 implementation. Due when `77b2` stands at 🧱 implementation.
- `6103` **tabloio: command line, output and input** stands at 📝 defined; next 📌 mockup 🪆. Its snapshot stands at 🔧 function.
  - at 🧱 implementation it requires `77b2` tablo at 🧱 implementation, "The library and plumbing it calls". Not met: `77b2` stands at 📝 defined. Due when `6103` stands at 📐 design.
  - at 📐 design it requires `bc86` Markdown views at 📌 mockup, "The Markdown mockups it reproduces". Not met: `bc86` stands at 📝 defined. Due when `6103` stands at 🔧 function.
- `c6e8` **tablotui: terminal user interface** stands at 📝 defined; next 📌 mockup 🪆. Its snapshot stands at 🔧 function.
  - at 🧱 implementation it requires `77b2` tablo at 🧱 implementation, "The library it embeds". Not met: `77b2` stands at 📝 defined. Due when `c6e8` stands at 📐 design.
  - at 📐 design it requires `bc86` Markdown views at 📌 mockup, "The Markdown mockups that fix the textual layout". Not met: `bc86` stands at 📝 defined. Due when `c6e8` stands at 🔧 function.
  - at 📐 design it requires `5fe3` HTML views at 📌 mockup, "The HTML mockups that fix the disclosure levels". Not met: `5fe3` stands at 📝 defined. Due when `c6e8` stands at 🔧 function.
- `595e` **tableaud: local daemon and HTML** stands at 📝 defined; next 📌 mockup 🪆. Its snapshot stands at 🔧 function.
  - at 🧱 implementation it requires `77b2` tablo at 🧱 implementation, "The library it embeds". Not met: `77b2` stands at 📝 defined. Due when `595e` stands at 📐 design.
  - at 📐 design it requires `5fe3` HTML views at 📌 mockup, "The HTML mockups it reproduces". Not met: `5fe3` stands at 📝 defined. Due when `595e` stands at 🔧 function.

Three snapshots stand ahead of their status files: `6103`, `c6e8` and `595e` read 📝 defined in this project and 🔧 function in their subprojects. Once each status file names 🔧 function, its requirements at 📐 design come due and read unmet: `bc86` then holds `6103` and `c6e8`, and `5fe3` holds `c6e8` and `595e`.

## Provenance

`tabloio blockage --ref 3cdae52 --level provenance`

**No cause holds any task.** The detail above stands, and each fact in it reads from Git as follows.

### The requirement entries

Each entry sits in the file of the task that requires. The commit `6b6c99a` Plan the Tableaux tooling, 2026-09-29, author and committer nbyoung@nbyoung.com, wrote all four files and no later commit changes them, so it also decides their authorisation.

```
.tableaux/tasks/77b2.yaml
  - { id: "e3cb", from: implementation, to: implementation, text: The schema files it embeds }
  - { id: "e9c6", from: implementation, to: design, text: The abstract views it derives }
  - { id: "fcec", from: implementation, to: unit, text: The corpus it conforms to }
.tableaux/tasks/6103.yaml
  - { id: "77b2", from: implementation, to: implementation, text: The library and plumbing it calls }
  - { id: "bc86", from: mockup, to: design, text: The Markdown mockups it reproduces }
.tableaux/tasks/c6e8.yaml
  - { id: "77b2", from: implementation, to: implementation, text: The library it embeds }
  - { id: "bc86", from: mockup, to: design, text: The Markdown mockups that fix the textual layout }
  - { id: "5fe3", from: mockup, to: design, text: The HTML mockups that fix the disclosure levels }
.tableaux/tasks/595e.yaml
  - { id: "77b2", from: implementation, to: implementation, text: The library it embeds }
  - { id: "5fe3", from: mockup, to: design, text: The HTML mockups it reproduces }
```

### The tasks that require

Each status file holds only `gate: defined`, since the next junction is recursive. One commit records all four: `e66abe2` Record the defined gate for the subproject tasks, 2026-09-30, author and committer noreply@anthropic.com, `Model: claude-haiku-4-5-20251001`.

- `77b2` `.tableaux/status/77b2.yaml` · linkage `subprojects/tablo`, a submodule pinned at `00f8f68` · pin set by `552d38f`, 2026-10-02, nbyoung@nbyoung.com, old `816f2a0` · the subproject root `b2c1` reads 📝 defined 🟢 nominal there, rolled up from `4b4f` Conformance
- `6103` `.tableaux/status/6103.yaml` · linkage `subprojects/tabloio`, a submodule pinned at `4593882` · pin set by `1c0f04d`, 2026-10-02, nbyoung@nbyoung.com, old `cb9ff8f` · the subproject root `07e0` reads 🔧 function 🟢 nominal there
- `c6e8` `.tableaux/status/c6e8.yaml` · linkage `subprojects/tablotui`, a submodule pinned at `a2878b5` · pin set by `fa4551e`, 2026-10-04, nbyoung@nbyoung.com, old `334df71` · the subproject root `40e8` reads 🔧 function 🟢 nominal there
- `595e` `.tableaux/status/595e.yaml` · linkage `subprojects/tableaud`, a submodule pinned at `e6ec4ec` · pin set by `3cdae52`, 2026-10-05, nbyoung@nbyoung.com, old `cffbfa6` · the subproject root `8608` reads 🔧 function 🟢 nominal there

Each pin equals the tip of its subproject's trunk `main`, so no pin holds a task.

### The tasks they require

- `e3cb` Schema files: `.tableaux/status/e3cb.yaml`, 📏 unit 🟢 nominal · 2026-09-30, noreply@anthropic.com · `5cbec7c` Record e3cb at unit, nominal
- `e9c6` Abstract views: `.tableaux/status/e9c6.yaml`, 📐 design 🟢 nominal · 2026-09-30, noreply@anthropic.com · `879b447` Advance the abstract views task to its design gate · reviewed by `0704a09`, `Reviewed: e9c6 design`, nbyoung@nbyoung.com
- `fcec` Conformance corpus: `.tableaux/status/fcec.yaml`, 🧱 implementation 🟢 nominal · 2026-09-30, noreply@anthropic.com · `60495c2` Record all three corpus corrections at implementation
- `77b2` tablo: as above, 📝 defined, `e66abe2`
- `bc86` Markdown views: a parent, 📝 defined 🟢 nominal, rolled up from `99f0` Gate definition view in Markdown · `.tableaux/status/99f0.yaml` · 2026-09-29, noreply@anthropic.com, committer nbyoung@nbyoung.com · `1a17bfc` Record the defined gate for the views and mockups
- `5fe3` HTML views: a parent, 📝 defined 🟢 nominal, rolled up from `a6f7` Gate definition view in Html · `.tableaux/status/a6f7.yaml` · 2026-09-29, noreply@anthropic.com, committer nbyoung@nbyoung.com · `1a17bfc`

### The commands

No cause stands, so no command resolves one. These reproduce the facts above:

```
git log -1 --format='%h %as %ae %ce' -- .tableaux/status/595e.yaml   # date and recorder of a status
git log -1 --format='%h %as %ae' -- .tableaux/tasks/595e.yaml        # the commit that states the requirements
git ls-tree 3cdae52 subprojects/                                     # the four pins
git log -1 --format='%h %as %ae' -- subprojects/tableaud             # the commit that set a pin
git -C subprojects/tableaud rev-parse main                           # the trunk tip a pin compares with
tabloio blockage --ref 3cdae52 --level provenance                    # this rendering
```

## Illustration: a tree with causes

> **Illustrative, not the project at the ref.** No commit holds this state and no command renders it. It takes the real tasks, people, junctions and requirement entries, and assumes three changes to the statuses, so that the form of a non-empty tree shows: a review outstanding, a hold two levels deep, and a task held under two causes.

The assumed changes:

1. The status files of `6103`, `c6e8` and `595e` name 🔧 function, where their snapshots stand at the ref.
2. Nine of the ten HTML mockups pass 📌 mockup. `5471` Work-blockage tree view in Html stands at 📝 defined 🟢 nominal 👓 review: the agent hands it off.
3. Nine of the ten Markdown mockups pass 📌 mockup. `efff` Work-blockage tree view in Markdown stands at 📝 defined 🟢 nominal with no reason.

### At glance

| Cause                                                                    | Who acts                           | Holds |
|--------------------------------------------------------------------------|------------------------------------|------:|
| `5471` Work-blockage tree view in Html awaits review at 📌 mockup 👓      | 👀 nbyoung@nbyoung.com reviews      | 4     |
| `efff` Work-blockage tree view in Markdown has not passed 📌 mockup       | 🤖 noreply@anthropic.com contributes | 3     |

### At detail

1. **`5471` Work-blockage tree view in Html awaits review at 📌 mockup 👓** · 👀 nbyoung@nbyoung.com reviews · holds 4
   - Action: nbyoung@nbyoung.com accepts the mockup with a commit that carries `Reviewed: 5471 mockup`.
   - `5471` Work-blockage tree view in Html at 📌 mockup: the review holds the task itself.
     - `5fe3` **HTML views** at 📌 mockup: a parent; `5471` is its one child that has not passed the gate.
       - `c6e8` tablotui at 📐 design: requires `5fe3` at 📌 mockup, "The HTML mockups that fix the disclosure levels". Unmet. Also under cause 2.
       - `595e` tableaud at 📐 design: requires `5fe3` at 📌 mockup, "The HTML mockups it reproduces". Unmet.
2. **`efff` Work-blockage tree view in Markdown has not passed 📌 mockup** · 🤖 noreply@anthropic.com contributes · holds 3
   - Action: noreply@anthropic.com draws the mockup and hands it off with the reason `review`.
   - `bc86` **Markdown views** at 📌 mockup: a parent; `efff` is its one child that has not passed the gate.
     - `6103` tabloio at 📐 design: requires `bc86` at 📌 mockup, "The Markdown mockups it reproduces". Unmet.
     - `c6e8` tablotui at 📐 design: requires `bc86` at 📌 mockup, "The Markdown mockups that fix the textual layout". Unmet. Also under cause 1.

A count names the distinct tasks under its cause at every depth, a parent included. `c6e8` appears under both causes, so the two counts sum to seven and the tree holds six tasks. The step from a child to its parent follows the roll-up: VIEWS.md does not state it, and this illustration proposes it, since every requirement the subprojects state on the mockups names a parent. The list of requirements not yet due follows the tree, in the form the [detail](#detail) section shows.

### At provenance, for cause 1

- **The status.** `.tableaux/status/5471.yaml` reads `gate: defined`, `state: nominal`, `reason: review`. Its date and recorder come from the hand-off commit, which this illustration does not have: `<date>`, noreply@anthropic.com, `<commit>`.
- **The junction.** `5471` at 📌 mockup: contributor noreply@anthropic.com, model `claude-opus`, reviewer nbyoung@nbyoung.com, all three from `437e` Tableaux tooling.
- **The review.** No commit carries `Reviewed: 5471 mockup`.
- **The requirement entries.** `.tableaux/tasks/c6e8.yaml`: `{ id: "5fe3", from: mockup, to: design, text: The HTML mockups that fix the disclosure levels }`. `.tableaux/tasks/595e.yaml`: `{ id: "5fe3", from: mockup, to: design, text: The HTML mockups it reproduces }`.
- **The deciding commits.** `5471`, `5fe3`, `c6e8` and `595e` are authorised by `6b6c99a` Plan the Tableaux tooling, 2026-09-29, author and committer nbyoung@nbyoung.com.
- **The linkages.** `c6e8` reads `subprojects/tablotui` at `a2878b5`; `595e` reads `subprojects/tableaud` at `e6ec4ec`.
- **The command that resolves the cause.**

```
tabloio review 5471 mockup
git commit --allow-empty --trailer 'Reviewed: 5471 mockup' -m 'Accept the work-blockage tree mockup in HTML'
```

## Form

The glance is a table, one row per cause, so the person and the count align as VIEWS.md draws them. The detail is a nested list and not an indented code block: a list wraps in a narrow chat window where a code block scrolls sideways, it keeps ids as code and titles as text, and it still reads as an indented tree in a terminal.

## See also

[The work queue](queue.md) lists the same waits per person as work waiting. [The audit](audit.md) reports an unmet requirement by rule. [The task definition](task.md) shows one task's requirements both ways. [The global tableau](tableau.md) shows where every task stands, and [the history](history.md) every pin event. The other views: [contextual tableau](context.md), [task assignment](assignment.md), [authority delegation](authority.md).

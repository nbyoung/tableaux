# Contributor work queue

**What do I do next?** For one person, the items where that person acts, in five kinds and in this order: reviews owed, authorisations owed, work ready, reaffirmations, work waiting. Reviews come first because each one unblocks the work of others. Within a kind the items follow display order; reaffirmations run oldest first.

This mockup depicts this project, the Tableaux tooling plan, on `main` at `3cdae52`, 2026-10-05.

| Parameter | In force |
|-----------|----------|
| ref | `main` at `3cdae52`, 2026-10-05 |
| viewer | nbyoung@nbyoung.com, the owner, who dispatches the agent |
| person | noreply@anthropic.com, the agent, as its dispatcher names it; then nbyoung@nbyoung.com, the viewer by default |
| task | `437e` Tableaux tooling, the root, so the whole project |
| window | every gate |
| level | glance, detail and provenance |
| brief | at provenance: `c74a` at mockup |

[The gate definition](gates.md) is the legend of every gate, state and reason symbol. 🤖 marks an agent contributor, 👀 a reviewer and 🪆 a junction that a subproject carries. [The task view](task.md) shows any one task in full, [the work-blockage tree](blockage.md) what waits on what, [the task assignment](assignment.md) what each person carries, [the contextual tableau](context.md) a person's corner, [the global tableau](tableau.md) the whole project, [the authority delegation](authority.md) who may accept what, [the history](history.md) the events and [the audit](audit.md) where files and history disagree.

- [Glance](#glance): one line per item
- [Detail](#detail): each item expanded
- [Provenance: the brief](#provenance-the-brief): one item, written to stand alone
- [Illustrative items, not at the ref](#illustrative-items-not-at-the-ref)

## Glance

### Glance: noreply@anthropic.com

| Kind | Task | Gate | Model | Since |
|------|------|------|-------|-------|
| Reviews owed | none |  |  |  |
| Authorisations owed | none |  |  |  |
| Work ready | `c2ad` Roles | 🌍 validate | `claude-opus` | 2026-09-30 |
| Work ready | `e9c6` Abstract views | 🧱 implementation | `claude-sonnet` | 2026-09-30 |
| Work ready | `99f0` Gate definition view in Markdown | 📌 mockup | `claude-opus` | 2026-09-29 |
| Work ready | `05a9` Task definition view in Markdown | 📌 mockup | `claude-opus` | 2026-09-29 |
| Work ready | `a9ce` Authority delegation view in Markdown | 📌 mockup | `claude-opus` | 2026-09-29 |
| Work ready | … and 17 more: `bb7c` `c74a` `efff` `ab8e` `c545` `d615` `b14e` `a6f7` `7dff` `b1b7` `ea51` `7783` `5471` `32e7` `69eb` `3194` `a8b4` | 📌 mockup | `claude-opus` | 2026-09-29 |
| Work ready | `e3cb` Schema files | 🌍 validate | `claude-opus` | 2026-09-30 |
| Work ready | `fcec` Conformance corpus | 📏 unit | `claude-sonnet` | 2026-09-30 |
| Work ready | `ac33` Agent identity | 🧱 implementation | `claude-sonnet` | 2026-09-30 |
| Work ready | `9f3f` Subproject linkage | 🧱 implementation | `claude-sonnet` | 2026-09-30 |
| Work ready | `7861` Productivity evidence | 🌍 validate | `claude-opus` | 2026-09-30 |
| Work ready | `7166` Language clarifications | 🧱 implementation | `claude-sonnet` | 2026-09-30 |
| Reaffirmation | `99f0` Gate definition view in Markdown | 📝 defined |  | 2026-09-29, 6 days |
| Reaffirmation | `05a9` Task definition view in Markdown | 📝 defined |  | 2026-09-29, 6 days |
| Reaffirmation | `a9ce` Authority delegation view in Markdown | 📝 defined |  | 2026-09-29, 6 days |
| Reaffirmation | … and 17 more: `bb7c` `c74a` `efff` `ab8e` `c545` `d615` `b14e` `a6f7` `7dff` `b1b7` `ea51` `7783` `5471` `32e7` `69eb` `3194` `a8b4` | 📝 defined |  | 2026-09-29, 6 days |
| Reaffirmation | `7166` Language clarifications | 📐 design |  | 2026-09-30, 5 days |
| Reaffirmation | `ac33` Agent identity | 📐 design |  | 2026-09-30, 5 days |
| Reaffirmation | `c2ad` Roles | 🧱 implementation |  | 2026-09-30, 5 days |
| Reaffirmation | `e3cb` Schema files | 📏 unit |  | 2026-09-30, 5 days |
| Reaffirmation | `7861` Productivity evidence | 🧱 implementation |  | 2026-09-30, 5 days |
| Reaffirmation | `fcec` Conformance corpus | 🧱 implementation |  | 2026-09-30, 5 days |
| Reaffirmation | `9f3f` Subproject linkage | 📐 design |  | 2026-09-30, 5 days |
| Reaffirmation | `77b2` tablo: backend library and plumbing | 📝 defined |  | 2026-09-30, 5 days |
| Reaffirmation | `6103` tabloio: command line, output and input | 📝 defined |  | 2026-09-30, 5 days |
| Reaffirmation | `c6e8` tablotui: terminal user interface | 📝 defined |  | 2026-09-30, 5 days |
| Reaffirmation | `595e` tableaud: local daemon and HTML | 📝 defined |  | 2026-09-30, 5 days |
| Reaffirmation | `e9c6` Abstract views | 📐 design |  | 2026-09-30, 5 days |
| Work waiting | none |  |  |  |

60 items: 0 reviews owed, 0 authorisations owed, 28 work ready, 32 reaffirmations, 0 work waiting. A run of five or more items that are alike but for the task shows its first three and folds the rest. Each line gives the task, the gate, the model the junction states and the date of the status. A reaffirmation gives the gate its status names and the age of the status at the ref.

Command: `tabloio queue --person noreply@anthropic.com --ref main --level glance`

### Glance: nbyoung@nbyoung.com

| Kind | Task | Gate | Model | Since |
|------|------|------|-------|-------|
| Reviews owed | none |  |  |  |
| Authorisations owed | none |  |  |  |
| Work ready | none |  |  |  |
| Reaffirmations | none |  |  |  |
| Work waiting | none |  |  |  |

0 items: the queue is empty. Each kind keeps its line, so that an empty queue reads as an answer and not as a failure.

Command: `tabloio queue --ref main --level glance`, where the person defaults to the viewer.

## Detail

### Detail: noreply@anthropic.com

60 items: 0 reviews owed, 0 authorisations owed, 28 work ready, 32 reaffirmations, 0 work waiting. A run of five or more items that are alike but for the task shows its first three and folds the rest.

#### 1. Reviews owed: none

No status carries the reason 👓 review. The person is the reviewer at 2 next junctions, `e9c6` at implementation and `fcec` at unit, and reviews its own work there.

#### 2. Authorisations owed: none

All 37 tasks stand authorised. The person has authority over the 20 tasks under `bc86` Markdown views and `5fe3` HTML views; [the authority delegation view](authority.md) shows each deciding commit.

#### 3. Work ready: 28

**`c2ad` Roles** at 🌍 validate, model `claude-opus`

- Gate: 🌍 validate, Validation: Passes user and field tests
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-opus`, from `bc63` Method
- Reviewer: 👀 nbyoung@nbyoung.com, from `437e` Tableaux tooling
- References: The junction states none. The task: `PLAN.md#roles`, Proposed roles
- Requires: nothing
- Unblocks: nothing
- Also required by: `e9c6` Abstract views from design to design, The role names the views refer to: met
- Status: 🧱 implementation 🟢 nominal, 2026-09-30, noreply@anthropic.com, `3d8ce0e`: The Roles text is on the trunk and covers all seven roles; the validate gate awaits the owner
- Brief: `tabloio queue --person noreply@anthropic.com --ref main --brief c2ad validate`

**`e9c6` Abstract views** at 🧱 implementation, model `claude-sonnet`

- Gate: 🧱 implementation, Implementation: Artifacts suffice for unit, integration and validation tests
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-sonnet`, from `437e` Tableaux tooling
- Reviewer: 👀 noreply@anthropic.com, the assignee, since the junction states no reviewer; the agent reviews itself
- References: The junction states none. The task: `PLAN.md#views`, Proposed views
- Requires: `c2ad` Roles from design to design, The role names the views refer to: met
- Unblocks: `77b2` tablo: backend library and plumbing at design, The abstract views it derives
- Also required by: 20 tasks, `99f0` to `a8b4`, from design to mockup, The abstract definition of the view: met
- Status: 📐 design 🟢 nominal, 2026-09-30, noreply@anthropic.com, `879b447`: VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place
- Brief: `tabloio queue --person noreply@anthropic.com --ref main --brief e9c6 implementation`

**`99f0` Gate definition view in Markdown** at 📌 mockup, model `claude-opus`

- Gate: 📌 mockup, Mockup: A non-technical mockup of the outcome exists
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-opus`, from `437e` Tableaux tooling
- Reviewer: 👀 nbyoung@nbyoung.com, from `437e` Tableaux tooling
- References: The junction states none. The task: `docs/mockups/gates.md`, The mockup
- Requires: `e9c6` Abstract views from design to mockup, The abstract definition of the view: met
- Unblocks: nothing
- Its parent unblocks:
  - `bc86` Markdown views at mockup is required by `6103` tabloio: command line, output and input at design, The Markdown mockups it reproduces
  - `bc86` Markdown views at mockup is required by `c6e8` tablotui: terminal user interface at design, The Markdown mockups that fix the textual layout
- Status: 📝 defined 🟢 nominal, 2026-09-29, noreply@anthropic.com, `1a17bfc`: Mockup waits for Abstract views (e9c6) at design
- Brief: `tabloio queue --person noreply@anthropic.com --ref main --brief 99f0 mockup`

**`05a9` Task definition view in Markdown** at 📌 mockup, model `claude-opus`

- Gate: 📌 mockup, Mockup: A non-technical mockup of the outcome exists
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-opus`, from `437e` Tableaux tooling
- Reviewer: 👀 nbyoung@nbyoung.com, from `437e` Tableaux tooling
- References: The junction states none. The task: `docs/mockups/task.md`, The mockup
- Requires: `e9c6` Abstract views from design to mockup, The abstract definition of the view: met
- Unblocks: nothing
- Its parent unblocks:
  - `bc86` Markdown views at mockup is required by `6103` tabloio: command line, output and input at design, The Markdown mockups it reproduces
  - `bc86` Markdown views at mockup is required by `c6e8` tablotui: terminal user interface at design, The Markdown mockups that fix the textual layout
- Status: 📝 defined 🟢 nominal, 2026-09-29, noreply@anthropic.com, `1a17bfc`: Mockup waits for Abstract views (e9c6) at design
- Brief: `tabloio queue --person noreply@anthropic.com --ref main --brief 05a9 mockup`

**`a9ce` Authority delegation view in Markdown** at 📌 mockup, model `claude-opus`

- Gate: 📌 mockup, Mockup: A non-technical mockup of the outcome exists
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-opus`, from `437e` Tableaux tooling
- Reviewer: 👀 nbyoung@nbyoung.com, from `437e` Tableaux tooling
- References: The junction states none. The task: `docs/mockups/authority.md`, The mockup
- Requires: `e9c6` Abstract views from design to mockup, The abstract definition of the view: met
- Unblocks: nothing
- Its parent unblocks:
  - `bc86` Markdown views at mockup is required by `6103` tabloio: command line, output and input at design, The Markdown mockups it reproduces
  - `bc86` Markdown views at mockup is required by `c6e8` tablotui: terminal user interface at design, The Markdown mockups that fix the textual layout
- Status: 📝 defined 🟢 nominal, 2026-09-29, noreply@anthropic.com, `1a17bfc`: Mockup waits for Abstract views (e9c6) at design
- Brief: `tabloio queue --person noreply@anthropic.com --ref main --brief a9ce mockup`

**… and 17 more** at 📌 mockup, model `claude-opus`: `bb7c` `c74a` `efff` `ab8e` `c545` `d615` `b14e` `a6f7` `7dff` `b1b7` `ea51` `7783` `5471` `32e7` `69eb` `3194` `a8b4`. Each reads as the three above but for its title, its reference and its parent: `5fe3` HTML views at mockup is required by `c6e8` and `595e` at design. `--task <id>` renders one in full.

**`e3cb` Schema files** at 🌍 validate, model `claude-opus`

- Gate: 🌍 validate, Validation: Passes user and field tests
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-opus`, from `bc63` Method
- Reviewer: 👀 nbyoung@nbyoung.com, from `437e` Tableaux tooling
- References: The junction states none. The task: `SYNTAX.md`, The schemas in place
- Requires: nothing
- Unblocks: nothing
- Also required by:
  - `fcec` Conformance corpus from implementation to implementation, The schema files the corpus validates against: met
  - `77b2` tablo: backend library and plumbing from implementation to implementation, The schema files it embeds: met
- Status: 📏 unit 🟢 nominal, 2026-09-30, noreply@anthropic.com, `5cbec7c`: schemas/check.sh (files agree with SYNTAX.md, version 0.2.1) and schemas/load.py (files load as JSON Schema 2020-12) pass; every .tableaux file validates
- Brief: `tabloio queue --person noreply@anthropic.com --ref main --brief e3cb validate`

**`fcec` Conformance corpus** at 📏 unit, model `claude-sonnet`

- Gate: 📏 unit, Unit test: All prescribed tests pass
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-sonnet`, from `437e` Tableaux tooling
- Reviewer: 👀 noreply@anthropic.com, the assignee, since the junction states no reviewer; the agent reviews itself
- References: The junction states none. The task: `README.md`, The examples the corpus starts from
- Requires: `e3cb` Schema files from implementation to implementation, The schema files the corpus validates against: met
- Unblocks: nothing
- Also required by: `77b2` tablo: backend library and plumbing from implementation to unit, The corpus it conforms to: met
- Status: 🧱 implementation 🟢 nominal, 2026-09-30, noreply@anthropic.com, `60495c2`: The corpus builds and checks clean, with 85 entries on the trunk; all three corrections from the tablo prototypes are in; the unit gate runs the tablo conformance test against it
- Brief: `tabloio queue --person noreply@anthropic.com --ref main --brief fcec unit`

**`ac33` Agent identity** at 🧱 implementation, model `claude-sonnet`

- Gate: 🧱 implementation, Implementation: Artifacts suffice for unit, integration and validation tests
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-sonnet`, from `437e` Tableaux tooling
- Reviewer: 👀 nbyoung@nbyoung.com, the assignee, since the junction states no reviewer
- References: The junction states none. The task: `PLAN.md#findings`, Findings F1, F2, F10 and F20
- Requires: nothing
- Unblocks: nothing
- Status: 📐 design 🟢 nominal, 2026-09-30, noreply@anthropic.com, `6762222`: The model plan-and-record rule (F20) is on the trunk; F1, F2 and F10 remain for design
- Brief: `tabloio queue --person noreply@anthropic.com --ref main --brief ac33 implementation`

**`9f3f` Subproject linkage** at 🧱 implementation, model `claude-sonnet`

- Gate: 🧱 implementation, Implementation: Artifacts suffice for unit, integration and validation tests
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-sonnet`, from `437e` Tableaux tooling
- Reviewer: 👀 nbyoung@nbyoung.com, the assignee, since the junction states no reviewer
- References: The junction states none. The task: `PLAN.md#findings`, Findings F3 to F5
- Requires: nothing
- Unblocks: nothing
- Status: 📐 design 🟢 nominal, 2026-09-30, noreply@anthropic.com, `43d68e4`: The subproject linkage rule (F3, F5, F12) is on the trunk at language 0.3.0; tablo and the subprojects follow
- Brief: `tabloio queue --person noreply@anthropic.com --ref main --brief 9f3f implementation`

**`7861` Productivity evidence** at 🌍 validate, model `claude-opus`

- Gate: 🌍 validate, Validation: Passes user and field tests
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-opus`, from `bc63` Method
- Reviewer: 👀 nbyoung@nbyoung.com, from `437e` Tableaux tooling
- References: The junction states none. The task: `PLAN.md#review-policy`, The review policy under test
- Requires: nothing
- Unblocks: nothing
- Status: 🧱 implementation 🟢 nominal, 2026-09-30, noreply@anthropic.com, `c6f2655`: The full report, its 23 tests and an example over five repositories are on the trunk
- Brief: `tabloio queue --person noreply@anthropic.com --ref main --brief 7861 validate`

**`7166` Language clarifications** at 🧱 implementation, model `claude-sonnet`

- Gate: 🧱 implementation, Implementation: Artifacts suffice for unit, integration and validation tests
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-sonnet`, from `437e` Tableaux tooling
- Reviewer: 👀 nbyoung@nbyoung.com, the assignee, since the junction states no reviewer
- References: The junction states none. The task: `PLAN.md#findings`, Findings F7 to F9 and F19
- Requires: nothing
- Unblocks: nothing
- Status: 📐 design 🟢 nominal, 2026-09-30, noreply@anthropic.com, `d9396b4`: The trunk clarification (F19) is on the trunk; F7 and F9 remain for design
- Brief: `tabloio queue --person noreply@anthropic.com --ref main --brief 7166 implementation`

#### 4. Reaffirmations: 32

Oldest first, by the author time of each status file's deciding commit, as that commit states it (UTC−04:00); statuses of one commit follow display order. No status carries a `Reaffirmed:` trailer at the ref, so each date is that of the file's last change. To confirm a status without change: `git commit --allow-empty --trailer 'Reaffirmed: <id>' -m 'Weekly review: no change'`.

**`99f0` Gate definition view in Markdown**, 📝 defined, 2026-09-29, 6 days

- Status: 📝 defined 🟢 nominal
- Note: Mockup waits for Abstract views (e9c6) at design
- Recorded: 2026-09-29 17:46 by noreply@anthropic.com in `1a17bfc`, Record the defined gate for the views and mockups
- Age: 6 days at the ref

**`05a9` Task definition view in Markdown**, 📝 defined, 2026-09-29, 6 days

- Status: 📝 defined 🟢 nominal
- Note: Mockup waits for Abstract views (e9c6) at design
- Recorded: 2026-09-29 17:46 by noreply@anthropic.com in `1a17bfc`, Record the defined gate for the views and mockups
- Age: 6 days at the ref

**`a9ce` Authority delegation view in Markdown**, 📝 defined, 2026-09-29, 6 days

- Status: 📝 defined 🟢 nominal
- Note: Mockup waits for Abstract views (e9c6) at design
- Recorded: 2026-09-29 17:46 by noreply@anthropic.com in `1a17bfc`, Record the defined gate for the views and mockups
- Age: 6 days at the ref

**… and 17 more**, 📝 defined, 2026-09-29, 6 days: `bb7c` `c74a` `efff` `ab8e` `c545` `d615` `b14e` `a6f7` `7dff` `b1b7` `ea51` `7783` `5471` `32e7` `69eb` `3194` `a8b4`. Each reads as the three above: one commit records all twenty with one note.

**`7166` Language clarifications**, 📐 design, 2026-09-30, 5 days

- Status: 📐 design 🟢 nominal
- Note: The trunk clarification (F19) is on the trunk; F7 and F9 remain for design
- Recorded: 2026-09-30 00:57 by noreply@anthropic.com in `d9396b4`, Advance the language clarifications to their design gate
- Age: 5 days at the ref

**`ac33` Agent identity**, 📐 design, 2026-09-30, 5 days

- Status: 📐 design 🟢 nominal
- Note: The model plan-and-record rule (F20) is on the trunk; F1, F2 and F10 remain for design
- Recorded: 2026-09-30 01:25 by noreply@anthropic.com in `6762222`, Advance the agent identity task to its design gate
- Age: 5 days at the ref

**`c2ad` Roles**, 🧱 implementation, 2026-09-30, 5 days

- Status: 🧱 implementation 🟢 nominal
- Note: The Roles text is on the trunk and covers all seven roles; the validate gate awaits the owner
- Recorded: 2026-09-30 07:33 by noreply@anthropic.com in `3d8ce0e`, Record the Roles task at its implementation gate
- Age: 5 days at the ref

**`e3cb` Schema files**, 📏 unit, 2026-09-30, 5 days

- Status: 📏 unit 🟢 nominal
- Note: schemas/check.sh (files agree with SYNTAX.md, version 0.2.1) and schemas/load.py (files load as JSON Schema 2020-12) pass; every .tableaux file validates
- Recorded: 2026-09-30 07:33 by noreply@anthropic.com in `5cbec7c`, Record e3cb at unit, nominal
- Age: 5 days at the ref

**`7861` Productivity evidence**, 🧱 implementation, 2026-09-30, 5 days

- Status: 🧱 implementation 🟢 nominal
- Note: The full report, its 23 tests and an example over five repositories are on the trunk
- Recorded: 2026-09-30 07:34 by noreply@anthropic.com in `c6f2655`, Complete the productivity evidence report
- Age: 5 days at the ref

**`fcec` Conformance corpus**, 🧱 implementation, 2026-09-30, 5 days

- Status: 🧱 implementation 🟢 nominal
- Note: The corpus builds and checks clean, with 85 entries on the trunk; all three corrections from the tablo prototypes are in; the unit gate runs the tablo conformance test against it
- Recorded: 2026-09-30 09:32 by noreply@anthropic.com in `60495c2`, Record all three corpus corrections at implementation
- Age: 5 days at the ref

**`9f3f` Subproject linkage**, 📐 design, 2026-09-30, 5 days

- Status: 📐 design 🟢 nominal
- Note: The subproject linkage rule (F3, F5, F12) is on the trunk at language 0.3.0; tablo and the subprojects follow
- Recorded: 2026-09-30 11:54 by noreply@anthropic.com in `43d68e4`, Advance the subproject linkage task to its design gate
- Age: 5 days at the ref

**`77b2` tablo: backend library and plumbing**, 📝 defined, 2026-09-30, 5 days

- Status: 📝 defined; the file holds the gate alone, since the next junction, mockup, is 🪆 recursive and `subprojects/tablo` supplies the state
- Recorded: 2026-09-30 12:53 by noreply@anthropic.com in `e66abe2`, Record the defined gate for the subproject tasks
- Age: 5 days at the ref

**`6103` tabloio: command line, output and input**, 📝 defined, 2026-09-30, 5 days

- Status: 📝 defined; the file holds the gate alone, since the next junction, mockup, is 🪆 recursive and `subprojects/tabloio` supplies the state
- Recorded: 2026-09-30 12:53 by noreply@anthropic.com in `e66abe2`, Record the defined gate for the subproject tasks
- Age: 5 days at the ref

**`c6e8` tablotui: terminal user interface**, 📝 defined, 2026-09-30, 5 days

- Status: 📝 defined; the file holds the gate alone, since the next junction, mockup, is 🪆 recursive and `subprojects/tablotui` supplies the state
- Recorded: 2026-09-30 12:53 by noreply@anthropic.com in `e66abe2`, Record the defined gate for the subproject tasks
- Age: 5 days at the ref

**`595e` tableaud: local daemon and HTML**, 📝 defined, 2026-09-30, 5 days

- Status: 📝 defined; the file holds the gate alone, since the next junction, mockup, is 🪆 recursive and `subprojects/tableaud` supplies the state
- Recorded: 2026-09-30 12:53 by noreply@anthropic.com in `e66abe2`, Record the defined gate for the subproject tasks
- Age: 5 days at the ref

**`e9c6` Abstract views**, 📐 design, 2026-09-30, 5 days

- Status: 📐 design 🟢 nominal
- Note: VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place
- Recorded: 2026-09-30 15:17 by noreply@anthropic.com in `879b447`, Advance the abstract views task to its design gate
- Age: 5 days at the ref

#### 5. Work waiting: none

Every due requirement is met, and no status carries ⛔ blocked or 🪫 overloaded. [The work-blockage tree](blockage.md) shows what waits on what.

Command: `tabloio queue --person noreply@anthropic.com --ref main --level detail`

### Detail: nbyoung@nbyoung.com

0 items: the queue is empty. Each kind keeps its line, so that an empty queue reads as an answer and not as a failure.

#### 1. Reviews owed: none

No status carries the reason 👓 review. The person is the reviewer at 26 next junctions, and no contributor hands one off at the ref.

#### 2. Authorisations owed: none

All 37 tasks stand authorised. The person, as the owner, has authority over every task; [the authority delegation view](authority.md) shows each deciding commit.

#### 3. Work ready: none

The person contributes at 🚀 release alone, and no task has release as its next gate.

#### 4. Reaffirmations: none

The person recorded no status. noreply@anthropic.com recorded all 32.

#### 5. Work waiting: none

No next junction names the person as contributor. [The work-blockage tree](blockage.md) shows what waits on what.

Command: `tabloio queue --ref main --level detail`

## Provenance: the brief

The provenance level of the queue is the brief: one item, written so that an agent starts from it alone. It is plain text that survives a paste into a prompt. This one briefs `c74a` Contributor work queue view in Markdown at 📌 mockup, the task that delivers the Markdown mockup of this view. Its six parts follow the order that VIEWS.md fixes. The rendering below is the whole output.

```
Brief: c74a Contributor work queue view in Markdown at mockup

This brief stands alone. It is one item of the work queue of
noreply@anthropic.com on main at 3cdae52, 2026-10-05: work ready.

1. The item

  Task         c74a Contributor work queue view in Markdown
  Gate         📌 mockup, Mockup: A non-technical mockup of the outcome exists
  Contributor  noreply@anthropic.com   (Tableaux tooling, 437e)
  Model        claude-opus             (Tableaux tooling, 437e)
  Reviewer     nbyoung@nbyoung.com     (Tableaux tooling, 437e)

  The model is the plan's statement. Run on a model that matches it, as an
  identifier or by prefix, and record the model you in fact run in the
  Model: trailer.

2. The task

  For one contributor, the junctions where they act next: work at a gate
  whose requirements are met, reviews they owe, authorisations they owe, and
  statuses they last reaffirmed longest ago. Each item carries the gate
  criteria, the junction references and the requirement texts, so an agent
  can start from the queue alone. It serves contributors, reviewers and
  authorities. The mockup, docs/mockups/queue.md, depicts this project.

  Reference: docs/mockups/queue.md, The mockup
  Junction references: none
  Under: Tableaux tooling › Method › Views › Markdown views

  Tableaux tooling (437e), whose entry sends this work to you: Software that
  supports planning and tracking with Tableaux: the method itself, a backend
  that parses, validates, audits and derives views from a project, and one
  front end per mode of use. The effort dog-foods the method to refine and
  validate it as a means to maximise human productivity through agentic
  assistance. Agents contribute at every gate, each on the model the
  junction names; people review at the strategic junctions this task states,
  and every task inherits them.

3. The requirements

  Requires: e9c6 Abstract views from design to mockup, The abstract
  definition of the view: met
  Unblocks: nothing; no task requires c74a
  Its parent bc86 Markdown views at mockup is required by:
    6103 tabloio: command line, output and input at design, The Markdown
    mockups it reproduces
    c6e8 tablotui: terminal user interface at design, The Markdown mockups
    that fix the textual layout

4. The status

  📝 defined 🟢 nominal, 2026-09-29, noreply@anthropic.com, 1a17bfc:
  Mockup waits for Abstract views (e9c6) at design

5. The commit you make when done

  Commit docs/mockups/queue.md and .tableaux/status/c74a.yaml, as
  noreply@anthropic.com, on a branch off main. Do not merge. The reviewer
  nbyoung@nbyoung.com accepts this gate, so hand the work off: the status
  stays at the gate it stands at and takes the reason review.

    gate: defined
    state: nominal
    reason: review
    note: <one line that says what waits on the branch>

  End the commit message with one paragraph of two trailers:

    Model: <the identifier your harness reports, matching claude-opus>
    Co-Authored-By: <your model's display name> <noreply@anthropic.com>

  The reviewer merges the branch and passes the gate with a commit that
  carries the trailer Reviewed: c74a mockup

6. The commands that reproduce this brief and show the task

  tabloio queue --person noreply@anthropic.com --ref 3cdae52 --brief c74a mockup
  tabloio task c74a --ref 3cdae52
```

Command: `tabloio queue --person noreply@anthropic.com --ref 3cdae52 --brief c74a mockup`

## Illustrative items, not at the ref

The queues above hold no review owed and no work waiting, so these two items show the form of each. Both are real states of this project at earlier commits; neither belongs to a queue at the ref.

### Illustrative: a review owed item

From the queue of nbyoung@nbyoung.com at commit `26defc7`, 2026-09-30, on the branch that carries the design. At glance:

| Kind | Task | Gate | Model | Since |
|------|------|------|-------|-------|
| Review owed | `e9c6` Abstract views | 📐 design | `claude-fable` | 2026-09-30 |

At detail:

**`e9c6` Abstract views** at 📐 design, model `claude-fable`

- Gate: 📐 design, Design: A model and sufficient tests exist
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-fable`, from `bc63` Method
- Reviewer: 👀 nbyoung@nbyoung.com, from `437e` Tableaux tooling
- References: The junction states none. The task: `PLAN.md#views`, Proposed views
- Requires: `c2ad` Roles from design to design, The role names the views refer to: met
- Unblocks: 20 tasks, `99f0` to `a8b4`, at mockup, The abstract definition of the view
- Also required by: `77b2` tablo: backend library and plumbing from implementation to design, The abstract views it derives: not yet met
- Status: 📝 defined 🟢 nominal 👓 review, 2026-09-30, noreply@anthropic.com, `26defc7`: The revised VIEWS.md design on branch worktree-agent-a6b84238bbacc4fcd awaits the owner's acceptance at the design gate
- To accept: Merge the branch and commit the trailer `Reviewed: e9c6 design`: `tabloio review e9c6 design`. The owner does so four minutes later, in `0704a09`.

### Illustrative: a work waiting item

From the queue of noreply@anthropic.com at commit `1b6916e`, 2026-09-30, on `main`, where nineteen more mockup tasks wait alike. At glance:

| Kind | Task | Gate | Model | Since |
|------|------|------|-------|-------|
| Work waiting | `99f0` Gate definition view in Markdown; waits for `e9c6` at design | 📌 mockup | `claude-opus` | 2026-09-29 |

At detail:

**`99f0` Gate definition view in Markdown** at 📌 mockup, model `claude-opus`

- Gate: 📌 mockup, Mockup: A non-technical mockup of the outcome exists
- Contributor: 🤖 noreply@anthropic.com, an agent on model `claude-opus`, from `437e` Tableaux tooling
- Reviewer: 👀 nbyoung@nbyoung.com, from `437e` Tableaux tooling
- References: The junction states none. The task: `docs/mockups/gates.md`, The mockup
- Waits for:
  - `e9c6` Abstract views from design to mockup, The abstract definition of the view: unmet; `e9c6` stands at 📝 defined 🟢 nominal
  - [The work-blockage tree](blockage.md) shows the cause and all that it holds up
- Unblocks: nothing
- Its parent unblocks:
  - `bc86` Markdown views at mockup is required by `6103` tabloio: command line, output and input at design, The Markdown mockups it reproduces
  - `bc86` Markdown views at mockup is required by `c6e8` tablotui: terminal user interface at design, The Markdown mockups that fix the textual layout
- Status: 📝 defined 🟢 nominal, 2026-09-29, noreply@anthropic.com, `1a17bfc`: Mockup waits for Abstract views (e9c6) at design
- Do not start: The item makes no commit until its cause clears.

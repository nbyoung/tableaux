# Tableaux

The Tableaux distributed planning and tracking system facilitates human and agentic collaboration on technical
projects by leveraging Git's existing mechanisms for implementing work definition, authorisation, delegation,
contribution and attribution.

This document gives the meaning of each Tableaux structure. [SYNTAX.md](SYNTAX.md) gives its form.

- [Project](#project)
- [Version](#version)
- [Gates](#gates)
- [Tasks](#tasks)
- [Junctions](#junctions)
- [Proposed and authorised tasks](#proposed-and-authorised-tasks)
- [Status](#status)
- [History](#history)
- [Roles](#roles)

## Project

A project lives in the `.tableaux` directory at the root of its Git repository, so the project and the repository share one history, one set of branches and one set of identities. The dot prefix keeps the project beside the repository's own metadata (`.git`, `.github`) rather than among its sources.

The **trunk** is the branch on which the project accepts tasks and statuses: authorisation reads the trunk's history, and every commit off it is a proposal. `version.yaml` names the trunk in `trunk`, as `.gitmodules` names a submodule's branch. When the field is absent, a tool takes the remote's default branch, `refs/remotes/origin/HEAD`, which a clone records; when that is absent too, as in a repository made by `git init` or a continuous-integration checkout that fetches one commit, the tool takes the branch its caller names, and otherwise the trunk is undetermined, every task reads as proposed, and a validator warns. A tool resolves the name against the local branches, then the remote-tracking branches. In a linked repository, a submodule's store or a clone that a URL maps to, the order reverses: the remote-tracking branches come first, since a fetch moves them and leaves a local branch where the clone put it. A subproject in a directory of the project's own repository is not in a linked repository: it shares the home repository's branches and keeps the home order. A subproject's own `version.yaml` names its trunk, and the audit reports a commit, pinned by a submodule or named by a `commit` field, that is not on it.

## Version

`version.yaml` names the semantic version of the Tableaux language that every other file in the project follows:

- **major** changes when a file's syntax changes incompatibly;
- **minor** changes when a file or field appears that older content still satisfies;
- **patch** changes when only meaning is clarified.

A tool accepts a project whose major version equals its own and whose minor version does not exceed it. While the language is under development the major version is `0`. Each additional structural dimension raises the minor version.

A subproject follows its parent's language. A validator warns of a project that a recursive junction or a task's `subproject` field names whose `version.yaml`, read at the commit the linkage fixes, states a version before the parent's own, patch included, since a rule a later version adds, such as the trailer that 0.2.1 introduced, otherwise passes the subproject by. The warning reads a submodule, a same-repository path and an absolute URL alike. A cross-project requirement reads one task's gate and delegates no work, so the warning leaves it out.

## Gates

`gates.yaml` defines the ordered gates every task passes through, the states a task takes with respect to its current gate, and the reasons that explain a state. The first gate is always `undefined`. The states always include `undefined`, the state of a task at the `undefined` gate, and `complete`, the state of a task at its last applicable gate, both with severity 0 so that roll-up sets them aside. A `gates.yaml` that lacks either, or gives either another severity, is one a tool cannot use: a validator rejects it, and a tool derives no status from it and gives no view, as for gates that do not start at `undefined`. The status dimension records which gate and state a task occupies. The reason key `review` is reserved: a project need not define it, but one that does gives it one meaning, that the contributor has handed the next junction's work to its reviewer ([Status](#status)), and the views read it so. Its symbol is 👓 by convention, since 👀 marks the reviewer.

## Tasks

Each task is one file, `tasks/<id>.yaml`, whose name is the task's id. Git then attributes the task's history, blame and conflicts to that file alone, and a contributor creates or revises a task with an ordinary commit.

An id is four hexadecimal digits chosen at random, not assigned in sequence. Contributors on separate branches then create tasks without coordinating and without colliding, and no id implies a rank: the tree and `order` give the order. A file writes an id as a quoted string, since YAML reads some ids as numbers ([SYNTAX.md](SYNTAX.md#tasksidyaml)).

Tasks form a tree:

- Exactly one task file has no `parent`; it is the **root**, and its title names the project.
- Every other task names its parent by id. Every parent chain ends at the root.
- Siblings sort by `order`, a strictly positive integer, ascending, then by id. Siblings without `order` follow those with one. A tool warns of two siblings with the same `order`, since only the id then decides.

The **assignee** is the person or agent responsible for the task, identified by the email address it commits with ([Roles](#roles)), so `git log --author` connects each participant's commits to its tasks. The root task's assignee is the project **owner**. A task's **authorities** are the assignees of its ancestors, nearest first; the root's authority is the owner. Assigning a task therefore delegates authority over its subtree, and the owner, as every task's ancestor, keeps authority over all of it.

**References** link the task to the documents that expand it: a specification, an issue, a datasheet. A view shows each reference's `text`, or its `url` when `text` is absent.

The **requires** relationship names the tasks whose results this task needs, each with an optional `text` field summarising what passes. The relation crosses the tree freely but forms no cycle, and a task never requires itself, an ancestor or a descendant. Each entry is an edge between two junctions, stated in the terminating task's file: `from` is the gate the originating task must have completed, defaulting to its last applicable gate, and `to` is the gate of this task whose work needs the result, defaulting to its first applicable gate after `undefined`. `to` is never `undefined`, since no work needs a result before definition. A validator checks that each gate applies to its task. A cross-project requirement names the originating task by `subproject` ([SYNTAX.md](SYNTAX.md#tasksidyaml)), and on an absolute URL it names the commit the project is read at. Where the originating task has not yet reached `from`, no commit shows the result, so the entry may state none: it is then **unpinned**, and the contributor states the commit at the first status commit after one exists.

The status dimension gives a requirement a derived condition. It is **met** when the originating task's gate is at or past `from`, **due** when the terminating task's next gate is `to` or later, and **unmet** when due and not met. A requirement whose `from` gate does not apply to the originating task has no condition: it is neither met nor due, no view marks it unmet, and a validator reports the entry itself as invalid. A validator warns of an unmet requirement and a view marks the terminating junction, but the recorded state stands; the contributor records a `blocked` reason when the wait matters.

A requirement may cross projects. An entry names its originating task with `subproject` in place of `id`, in the form a recursive junction uses ([Junctions](#junctions)) with `id` required, and a tool reads that task by the junction's rule: a submodule path at its pin, a same-repository path at the same commit, an absolute URL at its `commit`. An unpinned entry reads the task at the tip of the originating project's trunk, in the clone the URL maps to, where the `version.yaml` at the clone's default branch names the trunk ([Project](#project)). This covers what a junction cannot express: a subproject's dependency on its own parent, which names the parent by absolute URL and `commit`, since a subproject cannot pin its parent without a submodule cycle, and a dependency on a sibling subproject's leaf. `from` names a gate of the originating project's `gates.yaml` that applies to the task there, defaulting to its last applicable gate. The condition, the blockage tree, the work queue and the audit's unmet warning read a cross-project entry as a local one, with the originating task's gate read at the commit the linkage fixes. The no-cycle and no-ancestor rules hold within one project; a cross-project entry reads a task's gate in another project, at a fixed commit or at its trunk's tip, and no condition depends on another, so it cannot loop. A validator warns of a cross-project entry that names the task one of this task's recursive junctions already reads, since the junction carries the same fact. The audit reports a `commit` that is not on the originating project's trunk, as it does a submodule pin, and a cross-project requirement that is unmet at its `commit` and met at that trunk's tip, since advancing the commit meets it; a `commit` that merely lags the trunk is the snapshot the task chose. It reports an unpinned entry as information, since its condition moves with the other project's trunk and two readers of one commit of this project may see two conditions; a junction never takes that form, since every reader of one commit sees one subproject ([Junctions](#junctions)).

## Junctions

A **junction** is the meeting of a task and a gate. Every task has a junction at every gate in `gates.yaml`, and its file states only the junctions that depart from the **plain default**: the assignee does the work, nobody reviews it but the nearest person where the assignee is an agent, and the gate's own criteria apply. A junction is one of three kinds:

- A **plain** junction is the task's own work at the gate. The **contributor** does it and is identified like the assignee, by commit email; a view shows 🧑 for a contributor who is a person and 🤖 for one who is an agent ([Roles](#roles)). A `model` marks the contributor as an agent running that model. A model names no one, so an entry that states a `model` states its `contributor` beside it rather than inheriting one. The field is the plan's statement, a hint the dispatcher that composes the agent's brief passes through, and it names a model by its identifier or by a prefix of it, so `claude-fable` matches `claude-fable-5-1` and a plan outlives a model revision. The commit records the model that ran, in a `Model:` trailer ([SYNTAX.md](SYNTAX.md#commit-trailers)); the audit reports a commit at the junction whose trailer names a model outside the one stated, and a commit at the junction by its contributor that carries no trailer, unless the project's `version.yaml` at that commit states a language before 0.2.1, which introduced the trailer. A commit is **at** the junction of the gate it records when it changes a status's gate; any other commit to a status, and a `Reaffirmed:` commit, is at the task's next applicable junction. The **reviewer** is whoever accepts the work at the gate; a view shows 👀 where the reviewer differs from the contributor, and the contributor's mark alone where the reviewer is the contributor or the junction has none. An agent contributor with no stated reviewer takes the nearest person among the task's assignee and its authorities: the assignee when the assignee is a person, otherwise the nearest authority who is one, and the assignee when none is. A person's plain junction with no stated reviewer has none, and its status completes the gate on the contributor's word. `reviewer: false` waives review: the junction has no reviewer whoever contributes, and the value passes to the subtree as a stated reviewer does, so a descendant restores review only by stating a reviewer of its own. A junction that states no reviewer differs: it takes the reviewer an ancestor states, or else the default above. A project whose `version.yaml` states a language before 0.4.0 reads a contributor as an agent only where its junction states a `model`, and gives that agent the assignee as reviewer; a tool reads the version at each commit, as it reads the files there, so a review that language accepted stays accepted after the version rises. Its **references** expand the gate's criteria for this task.
- A **recursive** junction hands the work to another Tableaux project. Its `subproject` names that project by `url` and the task there by `id`, defaulting to that project's root. Ids are unique within a project, not across projects. The `url` takes one of three forms, and each fixes the commit the tool reads the project at, so that every reader of one commit of this repository sees one subproject:
  - A path relative to the repository root that is a Git submodule. The tool reads the subproject at the commit the submodule pins. The `commit` field is optional there; when present it restates the pin and must equal it. The restatement is allowed because it puts the pin in the task file, where a diff shows it and a reader needs no gitlink; a disagreement is an error because the file and the tree then state one fact two ways, and the tool cannot tell which the contributor meant.
  - A path relative to the repository root that is a plain directory of the same repository, a monorepo that holds several Tableaux projects. The tool reads the subproject's `.tableaux` under that path at the same commit as the parent. Nothing pins it, so `commit` is an error there.
  - An absolute URL, for a repository the project does not vendor as a submodule. On a junction the `commit` field is required and names the full hash of the commit the parent reads the project at; advancing it is the pin change. The project files name the URL and the commit and nothing else, so they stay reproducible. How the tool reaches a clone is its own affair: it consults a local mapping from URL to path that lives outside the project files, as Go's `replace` directive and Git's `url.<base>.insteadOf` do, and without one it fetches the repository into a cache and reads the commit there.

  A validator rejects a `url` that does not resolve to a Tableaux project it can read; a `commit` that is absent on a junction's absolute URL, present on a same-repository path, or unequal to a submodule's pin; and an `id` that names no task in that project. A view shows 🪆. The status dimension takes the junction's status from that task.
- A **not-applicable** junction exempts the task from the gate; a view shows `—`. Its only field, `applies`, takes only the value `false`: the entry's presence exempts the gate, and `applies: true` would restate the default the file omits. The `undefined` gate always applies and has no work of its own, so a file states no entry of any kind at `undefined`. At least one gate after `undefined` applies to every task, so every task has a first applicable gate after `undefined` and a last applicable gate later than it.

A task that hands every gate after its definition to one subproject states it once, in a task-level `subproject` field of the same form ([SYNTAX.md](SYNTAX.md#tasksidyaml)). The field stands for a recursive junction at each gate after the first gate that follows `undefined`, which is `defined` in the gates SYNTAX.md shows, so the definition stays this project's work and its authorisation reviews it. An entry the task's own file states at such a gate replaces the field there: a not-applicable entry exempts the gate, a plain entry makes the gate the task's own work, and a recursive entry names another task or project. At every other gate it covers, the field is the task's own entry, so it lifts an ancestor's exemption as a stated recursive entry does, and no field of an ancestor's plain entry reaches the gate. The status file reads as it does under stated recursive junctions: where the next junction is the field's, the file holds only the gate, and the contributor advances the gate as the subproject's task completes each one.

A parent has no status of its own, so its junctions describe **defaults its children inherit** rather than work of its own. A task's junction at a gate resolves from the task's own entry, then its ancestors' entries nearest first, then the plain default. A plain entry inherits field by field, so a child restates only what differs, for example an agent contributor under a parent's reviewer. A not-applicable entry exempts the whole subtree until a descendant states its own entry. That entry starts from the plain default: no field passes to it from an ancestor above the exemption. A recursive junction names one task's work and does not inherit, so a validator rejects one on a parent, and a task-level `subproject` field there too.

A validator checks that every junction key names a gate in `gates.yaml`. Junctions sit in the task file, so the authorisation below covers them.

## Proposed and authorised tasks

Any contributor may create or change a task, so the project distinguishes a **proposed** task, which states the contributor's intent, from an **authorised** task, which one of its authorities has accepted. Git records the acceptance on the [trunk](#project):

- The **deciding commit** of a task is the newest commit in the trunk's first-parent history that changed the task's file or carries an `Authorised:` trailer naming the task.
- The task is authorised when the deciding commit's author or committer is one of its authorities, and proposed otherwise. The authorities are read from the tree as it stands at that commit, so a move to a new parent is accepted by the new parent's chain.
- Off the trunk, every task is proposed.

This mirrors the maintainer hierarchy of large Git projects: a contributor proposes under someone else's task and that person merges, while a person plans their own subtree with commits that are proposal and acceptance at once. The sensor node's assignee therefore authorises the sensor board in any of three ways, and a contributor's later change to the file returns it to proposed:

```
git commit .tableaux/tasks/9f31.yaml                          # write or revise the task
git merge --no-ff sensor-board                                # merge the branch that proposes it
git commit --allow-empty --trailer 'Authorised: 9f31' \
           -m 'Accept the sensor board task'                  # accept a change already on the trunk
git commit --allow-empty --trailer 'Authorised: 9f31' \
           --trailer 'Authorised: c07d' \
           -m 'Accept the sensor board and node firmware tasks'   # accept several at once
```

The owner alone authorises the root, including a change of its assignee that transfers ownership.

The scheme is audit-only. It reads authorisation from the trunk's history and does not prevent a commit that misrepresents it; Tableaux takes commit identities and trailers at face value, as Git does. A project that needs enforcement adds it outside the scheme: signed commits with a trusted key, protection of the trunk on the hosting service, or a server-side hook that applies the rule. Path-based ownership such as `CODEOWNERS` cannot follow the tree, since `tasks/` is flat, so it can guard the directory for the owner but not a subtree for its authority.

## Status

Each leaf task's current status is one file, `status/<id>.yaml`. A leaf without one is undefined at the `undefined` gate, dated by its task file's newest commit, and has no recorder, since nobody has recorded a status: a view shows the date alone, the work queue owes nobody a reaffirmation of it, and a `Reaffirmed:` commit dates nothing there. A parent has no file; its status derives from its children.

The file states the **gate** the task has last completed and its **state** towards the next applicable gate, with an optional **reason** from `gates.yaml` and a **note**:

- The gate applies to the task; a validator rejects a status at a gate that a not-applicable junction exempts.
- The gate is `undefined` exactly when the state is `undefined`. Work towards `defined` therefore has no state of its own: a state measures work against a definition, and roll-up sets `undefined` aside so that a parent's state reflects defined work alone. A contributor who must say why that work waits records a file at `undefined` with a reason and a note, and every view reads the reason as at any other gate.
- A task at its last applicable gate has the state `complete`, and only there.
- When the next junction is recursive, the file holds only the gate. The state, reason, note and date come from the subproject's task, read at the commit the junction's `url` fixes ([Junctions](#junctions)): a submodule's pin or a stated `commit`, so a parent project sees a subproject snapshot that it advances deliberately, or, for a same-repository path, the commit the parent itself stands at. When that task completes, the contributor advances the gate.

Git supplies what the file leaves out:

- **Date and recorder.** The deciding commit of a status is the newest commit in the branch's history that changed the file or carries a `Reaffirmed:` trailer naming the task. Its author date is the status's date and its author the recorder. A review that finds no change reaffirms with an empty commit, so a status is never older than its last confirmation. A task with no status of its own to confirm, a parent, a leaf whose next junction is recursive or a leaf with no status file, takes its date from its children, from the subproject or from its task file, so a `Reaffirmed:` trailer naming it changes nothing a tool derives; the history keeps the event, and the audit reports the trailer.
- **Review.** A junction with a reviewer completes only when the reviewer says so: a commit in the branch's history, authored or committed by the reviewer, that carries `Reviewed: <id> <gate>`. A validator rejects a status whose gate passes a reviewed junction that has no such commit. The rule reads one commit, its files and the `Reviewed:` commits its history holds, whichever came first, so a status recorded before its review is invalid at each commit until the review and valid from the review on; a history applies no rule at the commits it replays. A `Reviewed:` commit from anyone other than the junction's reviewer has no effect, and the audit reports it. The `defined` junction is the exception: authorising a task accepts its definition, so the authorisation stands as the review of `defined` whoever its reviewer is, and no `Reviewed: <id> defined` commit is needed. A contributor who is also the reviewer carries the `Reviewed:` trailer on the commit that records the status. A contributor who has finished the work at a gate that has a reviewer records the status with the reason `review`, the hand-off ([Gates](#gates)), and the work queue lists the review as owed. After the reviewer's `Reviewed:` commit, the contributor records the status at the gate, so the reviewer edits no status file and no commit of the order is invalid. The audit reads the hand-off from the history too: it reports, as information, a task whose next junction has a reviewer and no `Reviewed:` commit from that reviewer yet, whose newest event is the contributor's and whose status states no `review`, since the work may be done or in progress; and it reports a status that still states `review` after the reviewer's `Reviewed:` commit for that junction, since the hand-off is stale.
- **History.** The log of the file is the task's status history, with every change's date and author.

```
git log -1 --format='%as %ae' -- .tableaux/status/9f31.yaml            # date and recorder
git log -p -- .tableaux/status/9f31.yaml                               # status history
git commit --allow-empty --trailer 'Reaffirmed: 9f31' \
           -m 'Weekly review: no change'                                # confirm without change
git commit --allow-empty --trailer 'Reviewed: 9f31 design' \
           -m 'Accept the sensor board design'                          # reviewer accepts a gate
```

Like authorisation, this is audit-only: Git records who said what and when, and takes their identity at face value.

A **parent's** status derives from its children and is never stored:

1. Consider the children whose state has non-zero severity; when there are none, consider all children.
2. The parent's gate is the earliest among the considered children's current gates, each child's own gate as its status names it, so a gate that does not apply to a child never enters.
3. The parent's state, reason and note are those of the most severe considered child at that gate, and of the first in display order when two tie; a view marks the note as rolled up from that child.
4. The parent's date is the oldest among the considered children.

Severity comes from `gates.yaml`. Undefined and complete children therefore step aside unless every child is one or the other, in which case the earliest gate decides: all complete gives a complete parent, and any undefined child gives an undefined one.

## History

Nothing stores history: the Git log is the history, and a tool derives a task's or the project's **events** from it. An event is a commit that changed a task's file or status file, or that carries a trailer naming the task, with the commit's author as the actor and its author date as the date. In the history a commit changes a file when the file differs from every parent's, as Git's default log reads it, so a merge that takes one side's file changes nothing of its own, and the commit that made the change keeps its event and, for a status, its date and recorder. On the trunk's first-parent line, which authorisation reads, a commit changes a file when it differs from its first parent's, so there a merge that brings in a task's file is the deciding commit, and it is an `authorised` event of the task, as an `Authorised:` trailer is. Three commands yield a task's events; a tool merges them in author-time order:

```
git log --format='%as %h %ae' -- .tableaux/tasks/9f31.yaml .tableaux/status/9f31.yaml
git log --format='%as %h %ae' -E --grep='^(Authorised|Reaffirmed): 9f31$' --grep='^Reviewed: 9f31 '
git log --format='%as %h %ae' --first-parent --merges main -- .tableaux/tasks/9f31.yaml     # main is the trunk
```

A task's status at any past commit is its status file at that commit, so `git show <commit>:.tableaux/status/9f31.yaml` and `git log -p` answer what changed and when without a second record. A parent's history replays its children's events in order, deriving its status after each. A task with a recursive junction takes in the subproject task's events up to the commit its `url` fixes, and each change of that commit is a `pin` event in the parent's log ([SYNTAX.md](SYNTAX.md#history)), naming the `url` and the old and new commit. A submodule pin that moves is a pin event of every task whose junction, requirement or `subproject` field names the path, since the commit changed the gitlink and no task file, so such a task adds the path to the first command above; a `commit` field that changes on a junction, a task's `subproject` field or a cross-project requirement is a pin event beside the `task` event of the file that changed, and so is the `commit` an unpinned requirement first states.

Git's branching shapes the history it keeps:

- The history is that of the branch in view. Off the trunk it includes proposals not yet authorised.
- A merge with `--no-ff` keeps every event a branch recorded, and on the trunk it adds the `authorised` event of each task whose file it brings in; a squash merge collapses them into one. A project that values fine-grained history merges without squashing.
- A tag marks a moment a view reports against, so `git log v1.0..v1.1` bounds a reporting period.

The audit-only caveat holds here too. A rewritten branch rewrites its history.

## Roles

Nothing declares a role. A person or agent holds one wherever their email appears in the position that defines it, holds several at once, and holds most of them with respect to one task rather than the whole project. A tool's views each serve some roles, and each role below names the views that serve it.

Every participant, person or agent, is identified by the email address it commits with. An agent commits under its own identity and never under a person's, so that the history attributes its work to it; one identity may serve several models, since the `Model:` trailer records which one ran ([SYNTAX.md](SYNTAX.md#commit-trailers)). An identity is an agent's when `agents.yaml` lists it ([SYNTAX.md](SYNTAX.md#agentsyaml)), or, in a project without that file, when a junction states it as contributor beside a `model`; every other identity is a person's. A project that keeps the file lists every agent there, and a validator rejects a junction that states a `model` beside a contributor the file does not list. A person who commits with an agent's help names the agent in a `Co-Authored-By:` trailer, as Git's convention has it: the commit stays the person's, as work, authorisation, review and record, and a view marks the agent's part in it. The audit reports a commit at an agent's junction whose author is a person and which carries a `Model:` trailer or a `Co-Authored-By:` trailer that names an agent, since the agent's work then reads as that person's; a commit at which `version.yaml` states a language before 0.4.0 is exempt.

- The **owner** is the root task's assignee. The owner is an authority of every other task, so may authorise any task, and alone authorises the root, including the change of its assignee that transfers ownership. The global tableau and the audit serve the owner, and every other view does too.
- An **authority** of a task is the assignee of one of its ancestors, nearest first. An authority authorises the tasks in its subtree, by commit, by merge or by an `Authorised:` trailer, and its own task's junctions state the defaults that subtree inherits. The authority delegation, task assignment and work-blockage views and the contextual tableau serve an authority.
- The **assignee** of a task is its `assignee`. The assignee is responsible for the task: the contributor at every junction that states none, the reviewer of an agent contributor at every junction that states none when the assignee is a person, and the one who answers for the status. The contextual tableau, the task view and the work queue serve an assignee.
- A **contributor** at a junction is its `contributor`, or the assignee when it states none. The contributor does the work at the gate, records the status and reaffirms it. The work queue, the task view, the contextual tableau and the gate definition serve a contributor.
- An **agent** is a participant whose identity is an agent's, as above; at a junction that states a `model` it runs that model. It contributes as a person does and may be an assignee, and so an authority. Its work at a gate has a reviewer unless the junction waives review: the one the junction states, or the nearest person among the assignee and the authorities. The work queue serves an agent as a brief, and the task view expands the brief.
- A **reviewer** at a junction is its `reviewer`, or, at an agent's junction that states none, the nearest person among the assignee and the authorities ([Junctions](#junctions)); a person's plain junction that states none, and a junction that states `reviewer: false`, have no reviewer. The reviewer accepts the work at the gate with a `Reviewed: <id> <gate>` commit, and until then the status cannot pass the gate. The work queue, the task view and the history serve a reviewer.
- An **observer** is anyone whose email appears nowhere in the project. An observer reads. The global tableau, the gate definition and the history serve an observer, as a static export where the observer has no tool.

In the weather station, Ada holds several roles at once: the owner, as the root's assignee, and the assignee of the sensor board, `9f31`, so she contributes at each of its gates that states no contributor. Ben is the assignee of the node firmware, `c07d`, and the reviewer of the sensor board at `validate`. The sensor node's assignee is an authority of both tasks, as Ada is of every task, and any of them authorises the sensor board with the commits shown under [Proposed and authorised tasks](#proposed-and-authorised-tasks). At the firmware's `unit` gate, `opus@example.org` is an agent contributor, and Ben reviews its work as the assignee, who is a person, since the junction states no reviewer. Whoever reads the project's tableau without an email in it is an observer.

A role is audit-only, like the acts it names. Tableaux reads a role from the files and the history to tell whose commit authorises, reviews or records, and does not prevent a commit from another hand; the audit reports where the files and the history disagree.

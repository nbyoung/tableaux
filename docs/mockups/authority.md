# Authority delegation

**Who may accept what?** Tableaux tooling · ref `main` at `3cdae52`, 2026-10-05 · viewer nbyoung@nbyoung.com, the owner · task `437e`, the root, so the whole tree · person: the viewer, who has authority over every task · filter: all tasks.

The legend of every symbol is the [gate definition](gates.md). Related views: [task definition](task.md) for one task's own junctions, [task assignment](assignment.md) for what each person carries, [history](history.md) for every authorisation event, [audit](audit.md) for what the files and the history dispute, and the [work queue](queue.md), which lists an authorisation as owed when a task stands proposed.

## Glance

`tabloio authority --ref main --level glance`

```
Task                                            Assignee
437e Tableaux tooling                           nbyoung@nbyoung.com
  bc63 Method                                     nbyoung@nbyoung.com
    c2ad Roles                                      noreply@anthropic.com
    2034 Views                                      nbyoung@nbyoung.com
      e9c6 Abstract views                             noreply@anthropic.com
      bc86 Markdown views                             noreply@anthropic.com  10 children
      5fe3 HTML views                                 noreply@anthropic.com  10 children
    e3cb Schema files                               noreply@anthropic.com
    fcec Conformance corpus                         noreply@anthropic.com
    ac33 Agent identity                             nbyoung@nbyoung.com
    9f3f Subproject linkage                         nbyoung@nbyoung.com
    7861 Productivity evidence                      noreply@anthropic.com
    7166 Language clarifications                    nbyoung@nbyoung.com
  77b2 tablo: backend library and plumbing        nbyoung@nbyoung.com
  6103 tabloio: command line, output and input    nbyoung@nbyoung.com
  c6e8 tablotui: terminal user interface          nbyoung@nbyoung.com
  595e tableaud: local daemon and HTML            nbyoung@nbyoung.com
```

Every row states its task's assignee, and the Assignee column indents as the Task column does, so the hierarchy reads in either. A task whose assignee differs from its parent's is a delegation. A proposed task carries the word `proposed` after its assignee; no row carries it here.

- 37 tasks, 17 rows: a parent whose children are all leaves with its own assignee folds to a count, and `--task bc86` or the detail level unfolds it.
- 7 delegations, each from nbyoung@nbyoung.com to noreply@anthropic.com: `c2ad`, `e9c6`, `bc86`, `5fe3`, `e3cb`, `fcec`, `7861`.
- nbyoung@nbyoung.com holds 10 tasks and may accept a change to all 37. noreply@anthropic.com holds 27 tasks and may accept a change to the 20 under `bc86` and `5fe3`.
- 37 authorised, 0 proposed.

## Detail

`tabloio authority --ref main --level detail`

```
Task                                                  Assignee
437e Tableaux tooling                                 nbyoung@nbyoung.com
  bc63 Method                                           nbyoung@nbyoung.com
    c2ad Roles                                            noreply@anthropic.com
    2034 Views                                            nbyoung@nbyoung.com
      e9c6 Abstract views                                   noreply@anthropic.com
      bc86 Markdown views                                   noreply@anthropic.com
        99f0 Gate definition view in Markdown                 noreply@anthropic.com
        05a9 Task definition view in Markdown                 noreply@anthropic.com
        a9ce Authority delegation view in Markdown            noreply@anthropic.com
        bb7c Task assignment view in Markdown                 noreply@anthropic.com
        c74a Contributor work queue view in Markdown          noreply@anthropic.com
        efff Work-blockage tree view in Markdown              noreply@anthropic.com
        ab8e Global tableau view in Markdown                  noreply@anthropic.com
        c545 Contextual tableau view in Markdown              noreply@anthropic.com
        d615 History view in Markdown                         noreply@anthropic.com
        b14e Audit view in Markdown                           noreply@anthropic.com
      5fe3 HTML views                                       noreply@anthropic.com
        a6f7 Gate definition view in Html                     noreply@anthropic.com
        7dff Task definition view in Html                     noreply@anthropic.com
        b1b7 Authority delegation view in Html                noreply@anthropic.com
        ea51 Task assignment view in Html                     noreply@anthropic.com
        7783 Contributor work queue view in Html              noreply@anthropic.com
        5471 Work-blockage tree view in Html                  noreply@anthropic.com
        32e7 Global tableau view in Html                      noreply@anthropic.com
        69eb Contextual tableau view in Html                  noreply@anthropic.com
        3194 History view in Html                             noreply@anthropic.com
        a8b4 Audit view in Html                               noreply@anthropic.com
    e3cb Schema files                                     noreply@anthropic.com
    fcec Conformance corpus                               noreply@anthropic.com
    ac33 Agent identity                                   nbyoung@nbyoung.com
    9f3f Subproject linkage                               nbyoung@nbyoung.com
    7861 Productivity evidence                            noreply@anthropic.com
    7166 Language clarifications                          nbyoung@nbyoung.com
  77b2 tablo: backend library and plumbing              nbyoung@nbyoung.com
  6103 tabloio: command line, output and input          nbyoung@nbyoung.com
  c6e8 tablotui: terminal user interface                nbyoung@nbyoung.com
  595e tableaud: local daemon and HTML                  nbyoung@nbyoung.com
```

37 tasks, 7 delegations, 37 authorised, 0 proposed.

### Chains and defaults

A task's authorities are the assignees of its ancestors, nearest first, so the children of one parent share one chain. Each parent below gives that chain and the junction defaults it states for its subtree. A junction mark is 🧑 a person contributes, 🤖 an agent contributes, 👀 a reviewer accepts, — the gate does not apply.

#### `437e` Tableaux tooling · nbyoung@nbyoung.com, the owner

Authority of `437e`: nbyoung@nbyoung.com, the owner. The root has no ancestor, and the owner alone authorises it.

Authorities of its 5 children, nearest first: nbyoung@nbyoung.com (`437e`).

Children: `bc63`, `77b2`, `6103`, `c6e8`, `595e`.

Junction defaults `437e` states for its subtree:

| Gate | Marks | Contributor | Model | Reviewer |
|---|:-:|---|---|---|
| 📝 defined | 🤖 | noreply@anthropic.com | `claude-haiku` | none stated |
| 📌 mockup | 🤖👀 | noreply@anthropic.com | `claude-opus` | nbyoung@nbyoung.com |
| 🔧 function | 🤖 | noreply@anthropic.com | `claude-sonnet` | none stated |
| 📐 design | 🤖👀 | noreply@anthropic.com | `claude-opus` | nbyoung@nbyoung.com |
| 🧱 implementation | 🤖 | noreply@anthropic.com | `claude-sonnet` | none stated |
| 📏 unit | 🤖 | noreply@anthropic.com | `claude-sonnet` | none stated |
| 🔗 integrate | 🤖 | noreply@anthropic.com | `claude-sonnet` | none stated |
| 🌍 validate | 🤖👀 | noreply@anthropic.com | `claude-sonnet` | nbyoung@nbyoung.com |
| 🚀 release | 🧑 | nbyoung@nbyoung.com | none: a person | none stated |

Where an agent contributes and the entry states no reviewer, the task's assignee reviews; at 📝 defined the authorisation stands as the review.

#### `bc63` Method · nbyoung@nbyoung.com

Authorities of its 8 children, nearest first: nbyoung@nbyoung.com (`bc63`, `437e`).

Children: `c2ad`, `2034`, `e3cb`, `fcec`, `ac33`, `9f3f`, `7861`, `7166`.

Junction defaults `bc63` states for its subtree:

| Gate | Marks | Contributor | Model | Reviewer |
|---|:-:|---|---|---|
| 📐 design | 🤖👀 | noreply@anthropic.com | `claude-fable` | nbyoung@nbyoung.com, from `437e` |
| 🌍 validate | 🤖👀 | noreply@anthropic.com | `claude-opus` | nbyoung@nbyoung.com, from `437e` |

Both entries state the contributor and the model only, so the reviewer stays the root's, and every other gate keeps the root's entry.

#### `2034` Views · nbyoung@nbyoung.com

Authorities of its 3 children, nearest first: nbyoung@nbyoung.com (`2034`, `bc63`, `437e`).

Children: `e9c6`, `bc86`, `5fe3`.

`2034` states no junction defaults; its subtree takes those of `bc63`, `437e`.

#### `bc86` Markdown views · noreply@anthropic.com

Authorities of its 10 children, nearest first: noreply@anthropic.com (`bc86`); then nbyoung@nbyoung.com (`2034`, `bc63`, `437e`).

Children: `99f0`, `05a9`, `a9ce`, `bb7c`, `c74a`, `efff`, `ab8e`, `c545`, `d615`, `b14e`.

Junction defaults `bc86` states for its subtree: — the gate does not apply at 🔧 function, 📐 design, 🧱 implementation, 📏 unit, 🔗 integrate, 🌍 validate, 🚀 release. Its children pass 📝 defined and 📌 mockup on the root's entries.

#### `5fe3` HTML views · noreply@anthropic.com

Authorities of its 10 children, nearest first: noreply@anthropic.com (`5fe3`); then nbyoung@nbyoung.com (`2034`, `bc63`, `437e`).

Children: `a6f7`, `7dff`, `b1b7`, `ea51`, `7783`, `5471`, `32e7`, `69eb`, `3194`, `a8b4`.

Junction defaults `5fe3` states for its subtree: — the gate does not apply at 🔧 function, 📐 design, 🧱 implementation, 📏 unit, 🔗 integrate, 🌍 validate, 🚀 release. Its children pass 📝 defined and 📌 mockup on the root's entries.

A leaf's own `junctions` block states that task's work, not a default; the [task definition](task.md) shows it.

## Provenance

`tabloio authority --ref main --level provenance`

The rendering prints the tree and the chains and defaults as the detail level does, and adds the deciding commits below. This mockup does not repeat them.

### Deciding commits

The deciding commit of a task is the newest commit on the first-parent history of `main` that changes the task's file or carries an `Authorised:` trailer that names it. The task is authorised when the commit's author or committer is one of its authorities. Tasks that share a deciding commit share a row, newest first.

| Commit | Date | Author | Committer | Accepts by | The authority is | Tasks |
|---|---|---|---|---|---|---|
| `8eb0cae` | 2026-09-30 | nbyoung@nbyoung.com | nbyoung@nbyoung.com | a merge by an authority, of `320cf2b` | author and committer | 2: `437e`, `bc63` |
| `16fe62f` | 2026-09-30 | nbyoung@nbyoung.com | nbyoung@nbyoung.com | a merge by an authority, of `018814a` | author and committer | 1: `ac33` |
| `8d8b070` | 2026-09-30 | nbyoung@nbyoung.com | nbyoung@nbyoung.com | a merge by an authority, of `9d9fb88` | author and committer | 1: `7166` |
| `6b6c99a` | 2026-09-29 | nbyoung@nbyoung.com | nbyoung@nbyoung.com | a change on the trunk by an authority | author and committer | 33: every other task |

- `6b6c99a` "Plan the Tableaux tooling" creates all 37 task files. It still decides 33: `c2ad`, `2034`, `e9c6`, `bc86`, `99f0`, `05a9`, `a9ce`, `bb7c`, `c74a`, `efff`, `ab8e`, `c545`, `d615`, `b14e`, `5fe3`, `a6f7`, `7dff`, `b1b7`, `ea51`, `7783`, `5471`, `32e7`, `69eb`, `3194`, `a8b4`, `e3cb`, `fcec`, `9f3f`, `7861`, `77b2`, `6103`, `c6e8`, `595e`.
- `8eb0cae` "Name a model family per gate (D7)" merges `320cf2b` "Name a model family per gate (D7)", author noreply@anthropic.com, committer nbyoung@nbyoung.com, which changes `437e`, `bc63` off the first-parent line. The merge is the owner's acceptance.
- `16fe62f` "Accept the model plan-and-record proposal" merges `018814a` "Record the model an agent runs (F20)", author noreply@anthropic.com, committer nbyoung@nbyoung.com, which changes `ac33` off the first-parent line. The merge is the owner's acceptance.
- `8d8b070` "Accept the trunk clarification" merges `9d9fb88` "Name the trunk in version.yaml (F19)", author noreply@anthropic.com, committer nbyoung@nbyoung.com, which changes `7166` off the first-parent line. The merge is the owner's acceptance.

By way of acceptance: 33 tasks by a change on the trunk, 4 by a merge, 0 by an `Authorised:` trailer. No commit on `main` carries an `Authorised:` trailer at this ref.

The junction defaults stand in the task files, so the same commits cover them: `8eb0cae` for those of `437e` and `bc63`, `6b6c99a` for those of `bc86` and `5fe3`.

Two commands reproduce a row, here for `437e`:

```
git log --first-parent -1 --format='%h %as %ae %ce %p' main -- .tableaux/tasks/437e.yaml
git log --first-parent -1 --format='%h %as %ae %ce %p' -E --grep='^Authorised: 437e$' main
```

## Proposed tasks only

`tabloio authority --ref main --proposed`

ref `main` · proposed tasks only

No task is proposed: all 37 are authorised on `main` at `3cdae52`.

### Illustration: how the view marks a proposed task

This block is **not this project**. It shows the weather station of the conformance corpus, `corpus/entries/weather-station`, where a contributor revises a task after its authority accepts it, so that the form of a proposed row is on view.

```
Task                  Assignee
a1c0 Weather station  ada@example.org
  3c5d Dashboard        dan@example.org  proposed
```

The filter keeps the ancestors of a proposed task, unmarked, so that the row keeps its place in the tree. At detail, the authority of `3c5d` is ada@example.org (`a1c0`). At provenance, the deciding commit, which the corpus labels W12, 2026-09-27, has dan@example.org as author and committer: a change on the trunk, and neither is an authority, so the cell "The authority is" reads —. The earlier commit W6 by ada@example.org, with the trailer `Authorised: 3c5d`, no longer decides. Off the trunk every row carries `proposed`, and `proposed (differs from trunk)` marks a task whose file the branch changes.

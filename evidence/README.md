# Productivity evidence

Task `7861` measures the [review policy](../PLAN.md#review-policy) against the aim in [PLAN.md](../PLAN.md): human attention goes to strategic junctions and agents carry the rest. This directory holds the model that turns Git history into that measure, a prototype script that applies it, its tests and an example run.

- [Model](#model)
- [Attribution](#attribution)
- [Elapsed time](#elapsed-time)
- [The report](#the-report)
- [Running it](#running-it)
- [Limits](#limits)

## Model

The Git log is the only source. The script reads every commit reachable from a ref in every repository of the effort, and derives from each commit its **role** and its **events**.

### Roles

A commit takes one role from its author and its trailers.

| Role          | Rule                                                                                     |
|---------------|------------------------------------------------------------------------------------------|
| `agent`       | The author email is an agent identity, by default `noreply@anthropic.com` (decision D3)  |
| `co-authored` | The author is a person and a `Co-Authored-By:` trailer names an agent identity           |
| `human`       | Neither                                                                                  |

A `Model:` trailer names the model the agent ran (finding F20). The report groups `agent` and `co-authored` commits by that model, so a gate's cost reads per model, and it lists under `unstated` a commit of either role that carries no trailer. Where the junction states a `model`, the report marks a commit whose trailer falls outside it, since that is the audit finding the method describes.

The method identifies a contributor by author email alone, so it sees a `co-authored` commit as the person's work. Finding F1 says this hides agent contribution from the audit. The report keeps the two apart so the owner sees both readings: the `agent` column is what the method attributes to the agent today, and the `co-authored` column is the agent work that the method attributes to a person. The plan commit `6b6c99a` is the first example: the owner authored it with the agent as co-author, so the method records the owner as the planner.

A review or an authorisation counts only when a `human` commit carries it. A commit a person authored with an agent co-author still counts, since the person signed it, and the report shows it under `co-authored`.

### Events

A commit yields zero or more events, each with a kind, a task and a gate. The first five kinds and `pin` are the history events of [SYNTAX.md](../SYNTAX.md#history), with `pin` read here per task and gate; `work` is this measure's own.

| Kind         | Source in the commit                                                                    | Task            | Gate                                                    |
|--------------|-----------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------|
| `task`       | A change to `.tableaux/tasks/<id>.yaml`                                                 | `<id>`          | `defined`: the definition is that gate's deliverable    |
| `authorised` | An `Authorised: <id>` trailer, or a `task` event whose author or committer is one of the task's authorities at that commit | `<id>` | `defined`: authorisation accepts the definition (F8) |
| `status`     | A change to `.tableaux/status/<id>.yaml`                                                | `<id>`          | The recorded gate when it differs from the previous status, since the change completes that gate; otherwise the next applicable gate, since the change reports progress towards it |
| `reaffirmed` | A `Reaffirmed: <id>` trailer                                                            | `<id>`          | The next applicable gate after the task's status at that commit |
| `reviewed`   | A `Reviewed: <id> <gate>` trailer                                                       | `<id>`          | `<gate>`                                                |
| `work`       | Any changed path outside `.tableaux/` and `subprojects/`                                | See [Attribution](#attribution) | The next applicable gate after the task's status at that commit |
| `pin`        | A change to a submodule path under `subprojects/`                                       | Every task whose recursive junction names that path | The next applicable gate after the task's status at that commit |

A **status change** carries its recorded state and reason as detail. A status change whose reason is `review` is a **hand-off**: the agent has finished and waits for the reviewer. A **reaffirmation** confirms a status without change and dates it, as the method says; it counts as an event and moves no gate.

The **next applicable gate** is the first gate after the status's `gate` that is not exempted by a not-applicable junction on the task or an ancestor, following the inheritance rule of [README.md](../README.md#junctions). A task with no status file stands at `undefined`, so its next gate is `defined`. A status in the `complete` state has no next gate, and the event reads `(none)`.

## Attribution

Events that name a task through a path or a trailer attribute themselves. A `work` event needs a rule, since a source file names no task:

1. When the same commit changes one or more status files, the work belongs to those tasks. An agent that commits its deliverable with the status change it justifies attributes its work with no extra convention.
2. Otherwise, when a merge commit whose subject names `task/<id>` brought the commit in, the work belongs to that task. This reads the branch discipline of this effort (`task/<id>` branches merged with `--no-ff`) and needs nothing in the commit itself.
3. Otherwise the work is unattributed and appears in the `(none)` row. Planning commits that touch `PLAN.md`, `README.md` or `SYNTAX.md` land here.

A task-file change does not attract the work in the same commit. The plan commit changed thirty-seven task files and `PLAN.md`; spreading one document over thirty-seven rows would say nothing.

## Elapsed time

The aim puts human review at strategic junctions only. Two intervals around each review say what that costs and how the agent responds.

| Measure               | From                                                                       | To                                                             |
|-----------------------|----------------------------------------------------------------------------|----------------------------------------------------------------|
| Hand-off to review    | The newest `agent` or `co-authored` event for the task at the reviewed gate before the review | The `human` commit that carries `Reviewed: <id> <gate>` |
| Review to resume      | That review                                                                | The first `agent` or `co-authored` event for the task after it, at any gate |
| Awaiting review       | A hand-off (`reason: review`) with no later review of that task and gate   | Now, or the moment `--now` names                               |

Hand-off to review is the time human attention holds the work; the policy expects it at the strategic gates and nowhere else, so a long interval at `mockup`, `design` or `validate` is the price the policy accepts, and any interval at `function`, `implementation`, `unit` or `integrate` is a deviation worth a look. Review to resume is how quickly the agent picks the work up again; a short interval shows that the review, not the agent, paces the task. Awaiting review lists the queue the owner faces today. The totals give the count, the median and the longest of each.

The intervals use author dates, as the method dates every event by author date.

## The report

The script prints Markdown. A header table names each repository walked, its ref, head, commit count and event count. Then, per repository, one table with a row per task and gate that has at least one event, sorted by task id and gate order, with the unattributed row last:

| Column               | Meaning                                                                    |
|----------------------|----------------------------------------------------------------------------|
| Id, Title            | The task; the title comes from the task file at the ref                    |
| Gate                 | The gate the events concern                                                |
| Agent, Co-authored, Human | Distinct commits per role that produced an event on this row          |
| Task, Authorised, Status, Reaffirmed, Reviewed, Work, Pin | Events per kind on this row                 |
| Hand-off to review   | One elapsed time per review on this row, and `pending` for a hand-off still waiting |
| Review to resume     | One elapsed time per review on this row                                    |

A commit that changes thirty-seven task files counts once in each of thirty-seven rows' commit columns and yields thirty-seven `task` events. Commit counts answer who touched the junction; event counts answer how much the method recorded there.

The totals section gives distinct commits and events per kind for each role across all repositories, and the three elapsed measures with count, median and longest.

The cost section follows the totals (finding F20). It has one row per gate and one column per model in the `Model:` trailers, plus `unstated` for an agent or co-authored commit with no trailer, and a total of distinct commits. A commit counts once in each gate where it has an event, across all repositories. A second table lists each commit whose model falls outside the `model` its junction states, by identifier or prefix; it reads `none` when every commit fits. The cost is a commit count, since the Git log holds no tokens or time per model.

## Running it

From the umbrella repository, with the submodules checked out or the sibling clones beside it:

```
python3 evidence/report.py > evidence/example.md
python3 evidence/report.py --ref main /path/to/tableaux /path/to/tablo
python3 evidence/report.py --agent noreply@anthropic.com --agent bot@example.org
python3 evidence/report.py --now 2026-10-01T09:00:00+00:00
```

With no repository argument the script takes the current directory and every submodule in its `.gitmodules`. It uses the checkout under the submodule path when that path is a repository, and otherwise resolves a relative url such as `../tablo` against the main worktree, which is where the sibling clones stand in this effort. It skips a submodule it cannot reach and says so on standard error.

The tests build a synthetic repository in a temporary directory with a plan commit, a hand-off, a review, a resumption, a reaffirmation, an authorisation trailer, a merged task branch, a pending hand-off and `Model:` trailers, one of them outside its junction. They also build a second repository and a submodule checkout. They check every event, both elapsed measures, the cost per gate by model, the mismatch table and the rendered tables:

```
python3 -m pytest evidence
```

The script needs python3 and git only.

## Limits

- **Authorisation ignores the trunk rule.** The method decides authorisation on the trunk's first-parent history. The script counts an authority's task-file change wherever it stands, so a proposal on a branch by an authority counts as authorised before the merge.
- **The reader is not a YAML parser.** The script reads the Tableaux files with regular expressions over the flow style this effort writes: `key: value` scalars, `- { key: ... }` gate entries and `gate: { ... }` junction entries. A block-style junction or a quoted key with a colon escapes it. `tablo` replaces this reader.
- **Reviewer identity is not checked.** A `Reviewed:` trailer counts when a `human` authored the commit; the script does not confirm that the person is the junction's reviewer. That check is the validator's, in `tablo`.
- **Only one agent identity.** The agent identity is one email or a list of emails; the script tells models apart by the `Model:` trailer alone (F20), and trusts the trailer as written. Finding F10 and task `ac33` decide how agents identify themselves.
- **Merge commits carry only trailers.** A merge shows no changed files, so a squash merge or a merge that rewrites files produces no `task`, `status` or `work` event of its own.
- **The gate of unattributed work is unknown.** Work in the `(none)` row has no task and so no gate.
- **Snapshots, not sessions.** The intervals measure commit to commit. Time an agent spends before its first commit, or a person spends reading before the review commit, is invisible.

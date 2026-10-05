# Audit

Where do files and history disagree?

Tableaux tooling · `main` at `3cdae52`, 2026-10-05 · viewer nbyoung@nbyoung.com, owner · task `437e`, the root · person: everyone · stale: 7 days.
The audit reads the four subprojects at the commits `main` pins. The symbols come from the [gate definition](gates.md).

The three sections below are three renderings of one view, one per level. A fourth shows the `person` parameter.

## Glance

`tabloio audit --ref main --stale 7 --level glance`

**1 error, 3 warnings, 28 items of information**: 32 findings. The error makes the project invalid until it resolves.

| Severity    | Rule | Kind                                              | Findings | Tasks                                                                                             | Resolver              |
|-------------|------|---------------------------------------------------|---------:|---------------------------------------------------------------------------------------------------|-----------------------|
| error       | S11  | A status past a reviewed junction with no review  |        1 | `e3cb`                                                                                            | noreply@anthropic.com |
| warning     | H3   | A `Model:` trailer outside the junction's model   |        3 | `437e`, `bc63`, `ac33`                                                                            | nbyoung@nbyoung.com   |
| information | H4   | A hand-off the history implies                    |       28 | `99f0` … `a8b4`, the twenty mockup tasks; `c2ad`, `e9c6`, `e3cb`, `fcec`, `ac33`, `9f3f`, `7861`, `7166` | noreply@anthropic.com |

**Most to resolve:** noreply@anthropic.com, 29 of 32: the error and the 28 items of information. nbyoung@nbyoung.com resolves the 3 warnings.

**Silent:**

- No task is proposed: the owner's commits decide all 37 task files.
- Nothing is stale at 7 days: no commit carries `Reaffirmed:`, and no status is older than six days. The oldest are the twenty mockup tasks', dated 2026-09-29 by `1a17bfc`.
- No requirement is unmet (R9): `e9c6` stands at 📐 design since `879b447`, which meets the twenty mockup tasks, and the eight unmet requirements of `77b2`, `6103`, `c6e8` and `595e` are not yet due.
- The four pins sit on their subprojects' trunks (J13), every trailer names a task and a gate that applies (H1), every `Reviewed:` trailer comes from its junction's reviewer (H2), no status states 👓 review (H5), and every agent commit since language 0.2.1 carries `Model:` (H6).
- A clone without the submodules adds one J8 error for each of `77b2`, `6103`, `c6e8` and `595e`; `git submodule update --init` resolves them.

See also: [history](history.md), [task](task.md), [queue](queue.md), [tableau](tableau.md).

## Detail

`tabloio audit --ref main --stale 7 --level detail`

**1 error, 3 warnings, 28 items of information**: 32 findings in 8 rows. One row groups the tasks that one rule hits at one gate for one reason. Errors come first, then warnings, then information; within a rule, gates in order, then tasks in display order. Files sit under `.tableaux/`.

| Rule | Severity    | Task                                   | Gate              | File                                 | Message                                                                                                                                                                                          | Action                                                                                         | Resolver              |
|------|-------------|----------------------------------------|-------------------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|-----------------------|
| S11  | error       | `e3cb`                                 | 🧱 implementation | `status/e3cb.yaml`                   | The status stands at 📏 unit and passes 🧱 implementation, whose reviewer is noreply@anthropic.com; no commit carries the trailer `Reviewed: e3cb implementation`. `fbe3c97` writes that line in its body, not among its trailers | Review: commit `Reviewed: e3cb implementation`, or return the status to 📐 design, the last reviewed gate | noreply@anthropic.com |
| H3   | warning     | `437e`, `bc63`                         | 📝 defined        | `tasks/437e.yaml`, `tasks/bc63.yaml` | `320cf2b` edits both task files under `Model: claude-fable-5-1`; the junction states `claude-haiku`                                                                                              | Revise the file: state the model that ran at the junction                                      | nbyoung@nbyoung.com   |
| H3   | warning     | `ac33`                                 | 📝 defined        | `tasks/ac33.yaml`                    | `018814a` edits the task file under `Model: claude-fable-5-1`; the junction states `claude-haiku`                                                                                                | Revise the file: state the model that ran at the junction                                      | nbyoung@nbyoung.com   |
| H4   | information | `99f0` … `a8b4`, twenty                | 📌 mockup         | `status/<id>.yaml`                   | The contributor's `5958858` is the newest event and the status states no 👓 review; nbyoung@nbyoung.com may have a mockup to review                                                               | Record the hand-off: the reason 👓 review when the work is done; or work on                    | noreply@anthropic.com |
| H4   | information | `ac33`, `9f3f`, `7166`                 | 🧱 implementation | `status/<id>.yaml`                   | The contributor's status commit is the newest event (`6762222`, `43d68e4`, `d9396b4`) and the status states no 👓 review; nbyoung@nbyoung.com, the assignee, reviews                              | As above                                                                                       | noreply@anthropic.com |
| H4   | information | `e9c6`                                 | 🧱 implementation | `status/e9c6.yaml`                   | The contributor's `879b447` is the newest event and the status states no 👓 review; the contributor is its own reviewer here                                                                      | Record the gate with `Reviewed: e9c6 implementation` on the same commit; or work on            | noreply@anthropic.com |
| H4   | information | `fcec`                                 | 📏 unit           | `status/fcec.yaml`                   | The contributor's `60495c2` is the newest event and the status states no 👓 review; the contributor is its own reviewer here                                                                      | Record the gate with `Reviewed: fcec unit` on the same commit; or work on                      | noreply@anthropic.com |
| H4   | information | `c2ad`, `e3cb`, `7861`                 | 🌍 validate       | `status/<id>.yaml`                   | The contributor's status commit is the newest event (`3d8ce0e`, `5cbec7c`, `c6f2655`) and the status states no 👓 review; nbyoung@nbyoung.com may have a validation to review                     | Record the hand-off: the reason 👓 review when the work is done; or work on                    | noreply@anthropic.com |

The twenty mockup tasks, in display order: `99f0`, `05a9`, `a9ce`, `bb7c`, `c74a`, `efff`, `ab8e`, `c545`, `d615`, `b14e` under `bc86` Markdown views; `a6f7`, `7dff`, `b1b7`, `ea51`, `7783`, `5471`, `32e7`, `69eb`, `3194`, `a8b4` under `5fe3` HTML views.

## Provenance

`tabloio audit --ref main --stale 7 --level provenance`

The rendering repeats the count line and the findings table of the detail level, then gives each rule once: its sentence, the commits involved and the commands. A date is the commit's author date; the committer shows where it differs from the author.

### S11, error: `e3cb` at 🧱 implementation

**Rule.** [corpus/RULES.md](../../corpus/RULES.md#statusidyaml) S11, from [README.md](../../README.md#status): "A validator rejects a status whose gate passes a reviewed junction that has no such commit."

**Junction.** `e3cb` at 🧱 implementation takes its contributor noreply@anthropic.com and its model `claude-sonnet` from `437e`. It states no reviewer, so the assignee of `e3cb`, noreply@anthropic.com, reviews.

| Commit    | Date       | Author                | Committer           | Subject                                                              | Status of `e3cb` after      | Trailers                                           |
|-----------|------------|-----------------------|---------------------|----------------------------------------------------------------------|-----------------------------|----------------------------------------------------|
| `0529170` | 2026-09-29 | nbyoung@nbyoung.com   |                     | Accept the schema files design                                       | 📝 defined, 🟢 nominal, 👓 review | `Reviewed: e3cb design`                      |
| `fbe3c97` | 2026-09-29 | noreply@anthropic.com | nbyoung@nbyoung.com | Advance Roles, schema files and evidence past their design reviews   | 🧱 implementation, 🟢 nominal | none that the method reads; the body holds the line `Reviewed: e3cb implementation` above a blank line |
| `5cbec7c` | 2026-09-30 | noreply@anthropic.com |                     | Record e3cb at unit, nominal                                         | 📏 unit, 🟢 nominal         | `Reviewed: e3cb unit`, `Model: claude-sonnet-5-5`  |

Git reads a trailer only in the last paragraph of a message. In `fbe3c97` the last paragraph holds `Co-Authored-By:` alone, so the reviewer's line counts for nothing.

```
# shows the finding: three trailers, none for implementation
git log --format='%h %(trailers:key=Reviewed)' -E --grep='^Reviewed: e3cb '

# resolves it: noreply@anthropic.com, the reviewer, accepts the gate
git commit --allow-empty -m 'Accept the schema files implementation' \
    --trailer 'Reviewed: e3cb implementation' --trailer 'Model: <the model that runs>'
```

### H3, warning: `437e`, `bc63` and `ac33` at 📝 defined

**Rule.** [corpus/RULES.md](../../corpus/RULES.md#commit-trailers) H3, from [README.md](../../README.md#junctions): "the audit reports a commit at the junction whose trailer names a model outside the one stated". A change to a task file is work at 📝 defined ([PLAN.md](../../PLAN.md), decision D8).

**Junction.** Each of the three takes 📝 defined from `437e`: contributor noreply@anthropic.com, model `claude-haiku`. The model reads as a prefix; `claude-fable-5-1` lies outside it.

| Commit    | Date       | Author                | Committer           | Subject                              | Changes                                    | Trailers                  |
|-----------|------------|-----------------------|---------------------|--------------------------------------|--------------------------------------------|---------------------------|
| `018814a` | 2026-09-30 | noreply@anthropic.com | nbyoung@nbyoung.com | Record the model an agent runs (F20) | `tasks/ac33.yaml`                          | `Model: claude-fable-5-1` |
| `320cf2b` | 2026-09-30 | noreply@anthropic.com | nbyoung@nbyoung.com | Name a model family per gate (D7)    | `tasks/437e.yaml`, `tasks/bc63.yaml`       | `Model: claude-fable-5-1` |

At `018814a` the junction still stated `claude-fable-5-1`; `320cf2b` states `claude-haiku` nine minutes later. The audit reads the junction at the ref, so both commits report.

```
# shows the finding: the model on each commit that changes the three task files
git log --format='%h %(trailers:key=Model,valueonly)' -- \
    .tableaux/tasks/437e.yaml .tableaux/tasks/bc63.yaml .tableaux/tasks/ac33.yaml

# resolves it: nbyoung@nbyoung.com, an authority, states the model that ran, for example in ac33
#   junctions: { defined: { contributor: noreply@anthropic.com, model: claude-fable } }
git commit .tableaux/tasks/ac33.yaml -m 'State the model that defines the agent identity task'
```

### H4, information: 28 tasks

**Rule.** [corpus/RULES.md](../../corpus/RULES.md#commit-trailers) H4, from [README.md](../../README.md#status): "it reports, as information, a task whose next junction has a reviewer, whose newest event is the contributor's and whose status states no `review`, since the work may be done or in progress".

**Junctions.** noreply@anthropic.com contributes at each. nbyoung@nbyoung.com reviews 📌 mockup and 🌍 validate, as `437e` states, and 🧱 implementation of `ac33`, `9f3f` and `7166` as their assignee. noreply@anthropic.com is the assignee of `e9c6` and `fcec` and so reviews its own work at their next gates.

| Commit    | Date       | Author                | Committer           | Subject                                                 | Newest event of           | Next gate         |
|-----------|------------|-----------------------|---------------------|---------------------------------------------------------|---------------------------|-------------------|
| `5958858` | 2026-09-29 | noreply@anthropic.com | nbyoung@nbyoung.com | Accept the defined gate of the views and mockups        | the twenty mockup tasks   | 📌 mockup         |
| `6762222` | 2026-09-30 | noreply@anthropic.com | nbyoung@nbyoung.com | Advance the agent identity task to its design gate      | `ac33`                    | 🧱 implementation |
| `43d68e4` | 2026-09-30 | noreply@anthropic.com |                     | Advance the subproject linkage task to its design gate  | `9f3f`                    | 🧱 implementation |
| `d9396b4` | 2026-09-30 | noreply@anthropic.com | nbyoung@nbyoung.com | Advance the language clarifications to their design gate | `7166`                   | 🧱 implementation |
| `879b447` | 2026-09-30 | noreply@anthropic.com |                     | Advance the abstract views task to its design gate      | `e9c6`                    | 🧱 implementation |
| `60495c2` | 2026-09-30 | noreply@anthropic.com |                     | Record all three corpus corrections at implementation   | `fcec`                    | 📏 unit           |
| `3d8ce0e` | 2026-09-30 | noreply@anthropic.com |                     | Record the Roles task at its implementation gate        | `c2ad`                    | 🌍 validate       |
| `5cbec7c` | 2026-09-30 | noreply@anthropic.com |                     | Record e3cb at unit, nominal                            | `e3cb`                    | 🌍 validate       |
| `c6f2655` | 2026-09-30 | noreply@anthropic.com |                     | Complete the productivity evidence report               | `7861`                    | 🌍 validate       |

`5958858` carries `Reviewed: <id> defined` for each of the twenty mockup tasks and for `e9c6`; the eight other commits change one status file each.

```
# shows the finding for one task: its newest event and who made it
git log -1 --format='%as %h %ae' -- .tableaux/tasks/b14e.yaml .tableaux/status/b14e.yaml
git log -1 --format='%as %h %ae' -E --grep='^(Authorised|Reaffirmed): b14e$' --grep='^Reviewed: b14e '

# resolves it: noreply@anthropic.com, the contributor, hands the finished work off
#   status/b14e.yaml: add `reason: review`
git commit .tableaux/status/b14e.yaml -m 'Mark the audit mockup as awaiting review' \
    --trailer 'Model: <the model that runs>'
```

Nothing resolves an item whose work is in progress: the information stands until the contributor or the reviewer records the next event.

## One person

`tabloio audit --ref main --stale 7 --for nbyoung@nbyoung.com --level detail`

The `person` parameter keeps the findings one person resolves. For nbyoung@nbyoung.com: **no error, 3 warnings, no information**.

| Rule | Severity | Task           | Gate       | File                                 | Message                                                                                             | Action                                                    | Resolver            |
|------|----------|----------------|------------|--------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------|---------------------|
| H3   | warning  | `437e`, `bc63` | 📝 defined | `tasks/437e.yaml`, `tasks/bc63.yaml` | `320cf2b` edits both task files under `Model: claude-fable-5-1`; the junction states `claude-haiku` | Revise the file: state the model that ran at the junction | nbyoung@nbyoung.com |
| H3   | warning  | `ac33`         | 📝 defined | `tasks/ac33.yaml`                    | `018814a` edits the task file under `Model: claude-fable-5-1`; the junction states `claude-haiku`   | Revise the file: state the model that ran at the junction | nbyoung@nbyoung.com |

The other 29 findings belong to noreply@anthropic.com; `--for noreply@anthropic.com` lists them.

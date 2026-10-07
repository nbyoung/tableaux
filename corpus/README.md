# Conformance corpus

The corpus is the set of example projects that a conforming Tableaux tool reads the same way. Each entry is a small Git repository with real history, so that everything the method derives from Git, authorisation, status dates, reviews, roll-up and events, has something to derive from. Each entry states what a validator reports about it and what a tool derives from it. Task `fcec` owns the corpus; `tablo`'s conformance task consumes it.

- [Layout](#layout)
- [An entry](#an-entry)
- [Building](#building)
- [Expected results](#expected-results)
- [Entries](#entries)
- [The worked example](#the-worked-example)
- [This project as an entry](#this-project-as-an-entry)
- [How a tool consumes the corpus](#how-a-tool-consumes-the-corpus)
- [Questions for review](#questions-for-review)
- [Findings about the method](#findings-about-the-method)

## Layout

```
corpus/
├── README.md               # this model
├── RULES.md                # every validator rule, its sentence, its file and its entry
├── build.sh                # builds every entry under build/
├── check.py                # checks the corpus against schemas/ and against itself
├── lib.sh                  # the functions an entry's history.sh uses: identities, dates, commits, merges, pins
├── base/                   # the smallest valid project; every invalid entry starts from it
│   └── .tableaux/…
├── entries/
│   ├── weather-station/    # the worked example
│   │   ├── expected.yaml   # findings and derived facts
│   │   ├── history.sh      # the commits, in order, with identities and dates
│   │   ├── project/        # the trunk's final tree: .tableaux/ and the documents it references
│   │   └── firmware/       # the subproject's final tree, pinned as the submodule project/firmware
│   ├── tree-two-roots/     # an invalid entry: expected.yaml and project/ only
│   ├── tableaux-tooling/   # this repository, read in place: expected.yaml only
│   └── …
└── build/                  # output, ignored by Git: one repository per entry plus <entry>.labels.txt
```

## An entry

One directory under `entries/` is one entry. It holds:

- `expected.yaml`, always. The findings a validator must report and the facts a conforming tool must derive. The [format](#expected-results) is below.
- `project/`, for every built entry. The trunk's final working tree: `.tableaux/` and whatever the task files reference. A validator reads it directly, without a build, for every rule that needs no history. The build checks that the built trunk's `.tableaux` equals it, so the files and the history never disagree.
- `history.sh`, when the entry needs history. A shell script that sources `lib.sh` and makes the commits in order: who, when, what, on which branch, merged how, with which trailers, pinning which subproject commit. An entry without one builds as a single commit of `base/` overlaid with `project/`, by `olive` on 2026-09-01; most invalid entries need nothing more.
- A subproject tree such as `firmware/`, when the entry pins a submodule or names a repository by absolute URL. `history.sh` builds it first as its own repository, `build/<entry>.<sub>`, and pins a labelled commit of it, or writes that commit's hash into the task file that names the URL. A same-repository subproject sits inside `project/` instead, under the path its `url` names.

Names are lowercase words joined by hyphens. An invalid entry is named after what is wrong (`tree-two-roots`, `status-on-parent`); a valid one after what it shows.

## Building

`sh corpus/build.sh` builds every entry; `sh corpus/build.sh weather-station` builds one. For each entry it removes `build/<entry>`, runs `history.sh` or makes the single default commit, checks the built `.tableaux` against `project/`, and leaves `build/<entry>.labels.txt` mapping each commit label to its hash. An entry whose `expected.yaml` has `source:` is read in place and skipped.

Reproducibility rests on `lib.sh`:

- `who <name>` sets `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME` and `GIT_COMMITTER_EMAIL` to one of the corpus's named identities: `ada`, `ben`, `dan` and the agent `opus` from the weather station; `olive`, `pat` and the agent `bot` from the base. Nothing commits as the host's user. `committed_by <name>` sets the committer alone, for an entry that separates author from committer.
- `on <date>` sets `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` to noon UTC on that date, so dates in `expected.yaml` are dates and not instants.
- `commit <label> <subject> [--trailer …]` stages everything and commits, allowing an empty commit, so a trailer-only acceptance or reaffirmation works as README.md shows. `merge <label> <branch> <subject> [trailer …]` merges with `--no-ff`. `pin <path> <url> <commit>` adds a submodule by a relative URL and checks out the pinned commit, and `repin <path> <commit>` advances that pin. `plan` lays down the entry's starting tree: `base/` without its `.tableaux`, then `project/`, so a deviation may delete a file the base holds.
- Every message, identity and date is fixed in the script, and `init` turns signing off, so two builds on two hosts give the same hashes. `expected.yaml` never names a hash; it names labels, and the labels file supplies the hashes after a build. A task file that names a repository by absolute URL must name a hash, since the language requires one, so such a file in `project/` carries the hash of the built subproject commit, and its `history.sh` checks the two agree and says which hash to write when they drift.

The test in the scratchpad built the weather station twice and got the same thirteen hashes both times.

`python3 corpus/check.py` (needs `pyyaml` and `jsonschema`) reads the corpus once it is built. It validates every valid entry's `.tableaux` against `schemas/`, taking each id as a string; applies the rules a project tree alone decides and compares its findings with each `expected.yaml`; compares the facts Git supplies (authorisation, status date and recorder, events, pins) with the built repositories; and checks that every rule in RULES.md has an entry and every entry it names exists. It is a small reference reading, not a conforming tool. Rules that need history (P5, S11, J13, R13, H1 to H3) it only checks that an entry states; J17 and the condition of a cross-project requirement it reads from the built repositories.

Three conventions in `expected.yaml` go beyond the table below. `trunk` states how the trunk resolves: `stated`, `inferred`, `caller` (the caller names the branch) or `undetermined` (the caller names none); a tool passes a branch name only when the file says `caller`. `replace` maps each absolute URL the entry's files name to the subproject tree the entry carries, built as `build/<entry>.<name>`; a tool passes it as its mapping from URL to clone and reads nothing from the network. A finding about a commit (H1 to H3) also carries `commit`, a label, and H1 carries `trailer`, the text that names nothing. A source list, `source: ["a110", "a100"]`, marks a resolved junction whose fields come from several tasks, nearest first.

## Expected results

`expected.yaml` is one YAML document. Every field beyond `entry` and `valid` is optional: an invalid entry states its findings and nothing else; a valid entry states whichever derived facts it exists to fix. A conforming tool must agree with every fact the file states and may derive more.

| Field        | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| `entry`      | The entry's name, equal to its directory                                                                  |
| `language`   | The Tableaux version the expectations assume; a tool at another major version skips the entry             |
| `ref`        | The branch in view; `main` by default                                                                     |
| `source`     | For an entry read in place: `{ repository, ref }` relative to the entry, instead of a build               |
| `valid`      | `true` when a validator reports no error; warnings leave it `true`                                        |
| `findings[]` | What a validator reports: `rule` (an id from RULES.md), `severity`, and where it applies (`task`, `file`, `gate`), with an optional `message` a tool need not match |
| `owner`, `root`, `count`, `order` | Project-wide facts: the owner's email, the root id, `{ tasks, leaves }`, and the tree in display order |
| `tasks.<id>` | Per-task facts, below                                                                                     |
| `refs.<branch>` | The same facts seen from another branch, with the label of its tip                                     |

Per task:

| Field           | Meaning                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------|
| `parent`, `authorities` | The parent id or `null`; the assignees of the ancestors, nearest first                                       |
| `authorisation` | `{ state: authorised or proposed, commit: <label>, by: <email> }`: the deciding commit on the trunk's first-parent line |
| `junctions`     | `default` gives the plain default for the task; each other key is a gate whose resolved junction departs from it: `kind`, the resolved fields, and `source`, the task whose entry supplies it |
| `applicable`    | The gates that apply to the task, in order                                                                           |
| `requires[]`    | Each requirement with `from` and `to` resolved and its condition: `met`, `due`, and `condition` as `met`, `pending` or `unmet`; a cross-project entry states `subproject` with `url`, `id` and `pin` in place of `id` |
| `reviews[]`     | The reviewed junctions the status passes and the commit that accepts each                                            |
| `subproject`    | For a recursive junction: `url`, `pin` (a label in the subproject's labels: the submodule's pin, or the commit the `commit` field names; absent for a same-repository path), and the task read there |
| `status`        | `gate`, `state`, `reason`, `note`, `date`, `recorder`, `commit`; `derived: true` and `from` on a parent               |
| `events[]`      | The history in the form SYNTAX.md gives, with `commit`, `old` and `new` as labels; `subproject` marks an event taken from a pinned task |

The weather station's file shows every field in use.

## Entries

Valid entries, each for what it shows:

| Entry                  | Shows                                                                                                                                   | Built by     |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------|
| `weather-station`      | README.md's example: the three ways to authorise, a proposal revised back to proposed, inherited reviewer, review, reaffirmation, a pinned subproject, an unmet and a pending requirement, roll-up, a branch in view | `history.sh` |
| `junction-kinds`       | Every junction kind and every resolution path: plain with `contributor`, `model` (by prefix, matched by a `Model:` trailer), `reviewer` and `references`; recursive with and without `id`; not-applicable; field-by-field inheritance; a not-applicable subtree with a descendant that states its own entry (F7: that entry starts from the plain default); an agent with no reviewer under a person and under an agent (F2) | `history.sh` |
| `submodule-subproject` | A task that delegates every gate after `defined` to a subproject root; the pin advanced twice; the subproject's tip beyond the pin; the subproject task's events up to the pin and a `pin` event for each pin change in the parent's history | `history.sh` |
| `subproject-by-url`    | A recursive junction whose `url` is an absolute URL with a `commit`, resolved through `replace`; the commit advanced once, so a `pin` event with `old` and `new`; the subproject's tip beyond it | `history.sh` |
| `subproject-same-repository` | A recursive junction whose `url` is a directory of the same repository, read at the parent's own commit; no pin and no `commit` | default |
| `requires-across-projects` | A cross-project requirement downward, on a leaf of a submodule at its pin, and upward, on the parent project by absolute URL and `commit`; the upward commit advanced once, so a `pin` event; conditions met and pending | `history.sh` |
| `requires-junction-target` | A cross-project requirement on the task a recursive junction of the same task already reads: one R12 warning                          | `history.sh` |
| `requires-commit-behind` | A cross-project requirement by URL whose `commit` lags the other project's trunk: unmet at the commit (R9) and met at the tip (R13), two warnings | `history.sh` |
| `unmet-requirement`    | A valid project with one R9 warning and one pending requirement                                                                         | default      |
| `unquoted-id`          | A valid project with `parent: { id: 1000 }`, one T7 warning, and the tree that a tool derives once it takes the id as a string           | default      |
| `status-defined-by-authorisation` | A valid project whose leaf stands at `defined` with a reviewer stated there and no `Reviewed:` commit; the authorisation is the review, and S11 stays silent | default      |
| `siblings-same-order`  | A valid project with two siblings at `order: 1` and one T12 warning; the tree sorts them by id                                           | default      |
| `trunk-stated`         | `version.yaml` names `trunk: develop`, the repository's default branch is `main`, and authorisation reads `develop`                     | `history.sh` |
| `trunk-inferred`       | No `trunk` field; the build clones the entry from a bare repository so `origin/HEAD` exists, and authorisation reads it                 | `history.sh` |
| `trunk-undetermined`   | No `trunk` field, no remote, no caller's branch: one P5 warning, and every task reads as proposed                                        | default      |
| `subproject-pin-off-trunk` | A parent pins a subproject commit that sits on a branch off the subproject's trunk: one J13 warning, and the pinned task still reads | `history.sh` |
| `unknown-trailer`      | A valid project whose history carries `Authorised: zzzz` and `Reviewed: 9f31 nowhere`, two H1 warnings, and no effect on any derived fact | `history.sh` |
| `model-mismatch`       | A valid project where a junction states `model: claude-fable` and one status commit carries `Model: claude-sonnet-5`: one H3 warning; a second commit with `Model: claude-fable-5-1` matches by prefix | `history.sh` |
| `review-by-non-reviewer` | A valid project where a `Reviewed:` commit comes from someone other than the junction's reviewer: one H2 warning, and the gate stays unreviewed | `history.sh` |
| `roll-up-tie`          | Two leaves under the root at the same gate and state, and the root's derived status from the first in display order (F21)              | default      |
| `handoff-inferred`     | A task whose next junction has a reviewer, whose newest event is the contributor's and whose status states no `review`: one H4 item of information | `history.sh` |
| `handoff-stale`        | A status that still states the reason `review`, drawn as 👓, after the reviewer's `Reviewed:` commit for that junction: one H5 warning | `history.sh` |
| `model-trailer-missing` | An agent's status commit with no `Model:` trailer at language 0.2.0, exempt, and another after the version rose: one H6 warning, and the hand-off that commit implies (H4) | `history.sh` |
| `tableaux-tooling`     | This repository at a named commit, read in place                                                                                        | none         |

Invalid entries, one per rule in [RULES.md](RULES.md), 75 in all. Each is `base/` plus the one deviation its name states, and its `expected.yaml` lists the finding, or the findings when one deviation trips two rules (`tree-no-root` trips T8 and T10). The rule table names each entry.

| Rule group           | Entries                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Project and version  | `no-tableaux-directory`, `version-missing`, `version-bad-pattern`, `version-unknown-field`, `version-major-mismatch`, `version-minor-ahead`, `version-trunk-empty` |
| Reading a file       | `file-not-yaml`, `file-duplicate-key`, `file-yaml-feature`, `file-stray-path` |
| Gates                | `gates-missing`, `gates-first-not-undefined`, `gates-only-undefined`, `gates-gate-missing-criteria`, `gates-bad-key`, `gates-duplicate-gate`, `gates-no-states`, `gates-negative-severity`, `gates-duplicate-state`, `gates-duplicate-reason`, `gates-unknown-field`, `gates-no-undefined-state`, `gates-complete-nonzero-severity` |
| Tasks and tree       | `task-bad-filename`, `task-missing-assignee`, `task-id-field`, `task-bad-email`, `task-reference-without-url`, `task-bad-id-pattern`, `tree-no-root`, `tree-two-roots`, `tree-parent-missing`, `tree-parent-cycle`, `task-parent-order-not-integer`, `task-parent-order-zero` |
| Requires             | `requires-missing-task`, `requires-cycle`, `requires-self`, `requires-ancestor`, `requires-descendant`, `requires-from-not-applicable`, `requires-from-unknown-gate`, `requires-to-not-applicable`, `requires-unknown-field`, `requires-to-undefined`, `requires-subproject-without-id` |
| Junctions            | `junction-unknown-gate`, `junction-undefined-not-applicable`, `recursive-on-parent`, `junction-mixed-kind`, `junction-model-without-contributor`, `junction-applies-true`, `junction-subproject-without-url`, `subproject-path-missing`, `subproject-task-missing`, `junction-unknown-field`, `junction-undefined-plain`, `junction-undefined-recursive`, `junction-all-not-applicable`, `subproject-commit-malformed`, `subproject-url-without-commit`, `subproject-directory-with-commit`, `subproject-commit-off-pin` |
| Status               | `status-no-task`, `status-on-parent`, `status-missing-gate`, `status-unknown-field`, `status-undefined-gate-nominal-state`, `status-nominal-gate-undefined-state`, `status-unknown-gate`, `status-unknown-state`, `status-unknown-reason`, `status-gate-not-applicable`, `status-last-gate-not-complete`, `status-state-with-recursive`, `status-no-state-plain`, `status-unreviewed-gate`, `status-complete-early` |

`subproject-path-missing`, `subproject-task-missing` and `subproject-commit-off-pin` need a submodule and build from a `history.sh`; every other invalid entry builds from the default commit.

## The worked example

`entries/weather-station/` is written out in full. Its `project/.tableaux` carries the four task files SYNTAX.md shows (`a1c0`, `9f31`, `c07d` and the gates) unchanged, plus the sensor node `4e2b` they name, a gateway `7b2e` with no status file, and a dashboard `3c5d` that a contributor proposes. Its `firmware/` is the subproject that `c07d` delegates its implementation to.

`history.sh` makes thirteen commits on the umbrella and three on the firmware, with the dates the SYNTAX.md history example gives for `9f31`:

| Label | Date  | Who | What                                                                                          |
|-------|-------|-----|-----------------------------------------------------------------------------------------------|
| F1    | 09-10 | ben | Plans the firmware                                                                            |
| F2    | 09-17 | ben | Records the node image at `design`, `nominal`; the umbrella pins this commit                  |
| F3    | 09-27 | ben | Records `implementation`; the umbrella does not see it                                        |
| W1    | 09-15 | ada | Plans the weather station: version, gates, `a1c0`, `4e2b`, `7b2e`                             |
| W2    | 09-16 | ben | Commits `c07d` on the trunk: the first way to authorise                                       |
| W3    | 09-18 | ada | Proposes `9f31` on the branch `sensor-board`                                                  |
| W4    | 09-19 | ben | Merges `sensor-board` with `--no-ff` and `Authorised: 9f31`: the second way                   |
| W5    | 09-20 | dan | Commits `3c5d` on the trunk; dan is no authority, so it stands proposed                       |
| W6    | 09-21 | ada | An empty commit with `Authorised: 3c5d`: the third way                                        |
| W7    | 09-22 | ada | Records `9f31` at `mockup`, `nominal`                                                         |
| W8    | 09-22 | dan | Records `3c5d` at `defined`, `nominal`                                                        |
| W9    | 09-24 | ben | An empty commit with `Reviewed: 9f31 mockup`; ben is the reviewer `4e2b` states               |
| W10   | 09-25 | ada | Records `9f31` at `function`, `stalled`, `blocked`                                            |
| W11   | 09-26 | ben | Pins `firmware` at F2, records `c07d` at `design` with no state, and carries `Reviewed: c07d mockup` |
| W12   | 09-27 | dan | Revises `3c5d`; the change returns it to proposed                                             |
| W13   | 09-28 | ada | An empty commit with `Reaffirmed: 9f31`                                                       |

`expected.yaml` then fixes what follows: `9f31` is authorised by the merge on the first-parent line, dated 09-28 by the reaffirmation, and its `mockup` review is W9; `3c5d` is proposed again after W12; `c07d` shows `design` from its own file and `nominal`, its note and its 09-17 date from `f1a0` at the pin, with one unmet requirement on `9f31`, its `mockup` review at W11, since ben is contributor and reviewer and the commit that records the status carries the trailer, and a `pin` event at W11 for the first pin of `firmware`; `7b2e` is undefined and dated by W1; `4e2b` rolls up to `function`, `stalled`, `blocked` from `9f31`, since both children have non-zero severity, `function` is the earlier gate and `9f31` is the most severe child there, with the 09-17 date of the oldest child considered; the root rolls up to `defined`, `nominal` from `3c5d`; and on the branch `sensor-board` every task is proposed.

## This project as an entry

`entries/tableaux-tooling/expected.yaml` names this repository (`source: { repository: ../../.., ref: corpus/tooling }`) and states facts about it: thirty-seven tasks, the owner, every task authorised because the owner committed the plan on `main`, the resolved junctions of `fcec` under the root's review policy, its pending requirement on `e3cb`, and `77b2`'s recursive junction to `subprojects/tablo` at the pinned commit. The build skips it. The ref is the tag `corpus/tooling`, which the owner moves: when a commit on `main` changes those facts, the owner updates the facts and moves the tag to that commit in one step, `git tag -f corpus/tooling main && git push -f origin corpus/tooling`, so the corpus always describes one fixed commit of this repository and never its tip. The tag first lands on the commit that merges this design.

The entry records that at `fcec`'s gates after `defined` the agent is its own reviewer by the method's default, so the commit that records each such status carries `Reviewed: fcec <gate>` by the agent, or rule S11 fires. At `defined`, the owner's authorisation stands as the review. See Q1 and Q2.

## How a tool consumes the corpus

`tablo`'s conformance test runs `build.sh`, then for each entry: reads `build/<entry>` at `ref` (or `source` for an entry read in place), validates it, and compares the findings with `expected.findings` by rule id and location; then, for a valid entry, derives the facts and compares each one `expected.yaml` states, translating labels to hashes through `labels.txt`. A finding whose rule id the tool does not know fails the test, so a new rule in RULES.md pulls the tool along. A fact marked `undecided: <finding>` passes with either reading until the finding resolves.

## Questions for review

- **Q1 S11 severity.** Decided at design review: the validator rejects a status that passes an unreviewed junction, as README.md says. The consequence for this repository, every agent-recorded status invalid, resolves through Q2.
- **Q2 The agent as its own reviewer.** Decided at design review, in two parts. First, F8 resolves: authorising a task stands as the review of its `defined` gate, so no status at `defined` needs a `Reviewed:` commit, and every status this repository holds today is valid. Second, at every later gate where the agent is its own reviewer, the commit that records the status carries `Reviewed: <id> <gate>`, authored by the agent, so status and review land together. README.md states both. F2's proposal of a human default reviewer stays open in task `ac33`.
- **Q3 Implicit rules.** Decided at design review: J8, J9 and S7 stay as rules, and README.md now states each in a sentence of its own. No implicit rule remains.
- **Q4 Candidate rules.** Decided at design review: all eight candidates become rules, and README.md and SYNTAX.md now state them (RULES.md, "Candidate rules, resolved").
- **Q5 Entry granularity.** Decided at design review: one entry per rule. A red conformance run in `tablo` then names the rule that regressed, a new rule adds one directory and leaves every other fixture untouched, and the check that every rule has an entry is a directory listing against RULES.md. The 70 invalid entries cost nothing to maintain, since `build.sh` makes each from `base/` plus its one deviation.
- **Q6 The read-in-place entry's ref.** Decided at design review: the tag `corpus/tooling`, which the owner moves. A hash would go stale on every merge; the tag moves only when the owner re-reads the facts, and its move is itself an event in the history.

## Findings about the method

Enumerating the rules found the following. Each is one sentence and names the task it belongs to under D6.

- **F11 Deciding commits and events disagree on merges.** The deciding commit reads first-parent history, where a `--no-ff` merge that brings in a task file counts, but the event commands in README.md use the default log, where the same merge does not appear, so a merge that authorises leaves no `authorised` event unless it carries the trailer. Task `7166`.
- **F12 The pin change has no event kind.** README.md says each change of a submodule pin is an event in the parent's log, but the history schema's `event` enum has no value for it. Task `9f3f`. Resolved at `9f3f`'s design (2026-09-30): the history schema gains the `pin` event, with `url`, `old` and `new`, for a submodule pin moved or a `commit` field changed on a junction or a cross-project requirement.
- **F13 A reaffirmation of a recursive junction is moot.** README.md's example reaffirms `c07d`, whose date comes from the subproject at the pin, so the trailer changes nothing a tool derives. Task `9f3f`.
- **F14 Roll-up hides a severe child at a later gate. Resolved.** Under the rule the stalled child `9f31` stands at the earliest gate, so `4e2b` shows it; the earlier reading rested on a mistake in the corpus. Task `7166`.
- **F15 The review may follow the status it validates.** SYNTAX.md's example records `mockup` on 09-22 and reviews it on 09-24; the status is invalid for two days by S11 and valid at the tip, and the text does not say whether a history replay applies S11 at each commit. Task `7166`.
- **F16 An unquoted id fails the schema before the warning.** SYNTAX.md warns of an unquoted id and says a tool takes any scalar as a string, but the schema types every id as a string, so a tool must coerce before validating or the warning never fires. Task `7166`.
- **F17 The undefined leaf has a date but no recorder.** A leaf with no status file is dated by its task file's newest commit; whether that commit's author is its recorder is unstated. Task `7166`.
- **F18 Nothing requires the `undefined` and `complete` states.** S4 and S8 name them and roll-up assumes their severity is 0, but `gates.yaml` may omit them. Task `7166`.

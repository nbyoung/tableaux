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
├── build.sh                # builds every entry under build/ (sketch until the implementation gate)
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
- A subproject tree such as `firmware/`, when the entry pins a submodule. `history.sh` builds it first as its own repository, `build/<entry>.<sub>`, and pins a labelled commit of it.

Names are lowercase words joined by hyphens. An invalid entry is named after what is wrong (`tree-two-roots`, `status-on-parent`); a valid one after what it shows.

## Building

`sh corpus/build.sh` builds every entry; `sh corpus/build.sh weather-station` builds one. For each entry it removes `build/<entry>`, runs `history.sh` or makes the single default commit, checks the built `.tableaux` against `project/`, and leaves `build/<entry>.labels.txt` mapping each commit label to its hash. An entry whose `expected.yaml` has `source:` is read in place and skipped.

Reproducibility rests on `lib.sh`:

- `who <name>` sets `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME` and `GIT_COMMITTER_EMAIL` to one of the corpus's named identities: `ada`, `ben`, `dan` and the agent `opus` from the weather station; `olive`, `pat` and the agent `bot` from the base. Nothing commits as the host's user. `committed_by <name>` sets the committer alone, for an entry that separates author from committer.
- `on <date>` sets `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` to noon UTC on that date, so dates in `expected.yaml` are dates and not instants.
- `commit <label> <subject> [--trailer …]` stages everything and commits, allowing an empty commit, so a trailer-only acceptance or reaffirmation works as README.md shows. `merge <label> <branch> <subject> [trailer …]` merges with `--no-ff`. `pin <path> <url> <commit>` adds a submodule by a relative URL and checks out the pinned commit.
- Every message, identity and date is fixed in the script, and `init` turns signing off, so two builds on two hosts give the same hashes. `expected.yaml` never names a hash; it names labels, and the labels file supplies the hashes after a build.

The test in the scratchpad built the weather station twice and got the same thirteen hashes both times.

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
| `requires[]`    | Each requirement with `from` and `to` resolved and its condition: `met`, `due`, and `condition` as `met`, `pending` or `unmet` |
| `reviews[]`     | The reviewed junctions the status passes and the commit that accepts each                                            |
| `subproject`    | For a recursive junction: `url`, `pin` (a label in the subproject's labels), and the task read there                  |
| `status`        | `gate`, `state`, `reason`, `note`, `date`, `recorder`, `commit`; `derived: true` and `from` on a parent               |
| `events[]`      | The history in the form SYNTAX.md gives, with `commit` as a label; `subproject` marks an event taken from a pinned task |

The weather station's file shows every field in use.

## Entries

Valid entries, each for what it shows:

| Entry                  | Shows                                                                                                                                   | Built by     |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------|
| `weather-station`      | README.md's example: the three ways to authorise, a proposal revised back to proposed, inherited reviewer, review, reaffirmation, a pinned subproject, an unmet and a pending requirement, roll-up, a branch in view | `history.sh` |
| `junction-kinds`       | Every junction kind and every resolution path: plain with `contributor`, `model`, `reviewer` and `references`; recursive with and without `id`; not-applicable; field-by-field inheritance; a not-applicable subtree with a descendant that states its own entry (F7 stays open, and the file marks the fact `undecided: F7`); an agent with no reviewer under a person and under an agent (F2) | `history.sh` |
| `submodule-subproject` | A task that delegates every gate after `defined` to a subproject root; the pin advanced twice; the subproject's tip beyond the pin; the subproject task's events up to the pin and the pin changes in the parent's history | `history.sh` |
| `unmet-requirement`    | A valid project with one R9 warning and one pending requirement                                                                         | default      |
| `unquoted-id`          | A valid project with `parent: { id: 1000 }`, one T7 warning, and the tree that a tool derives once it takes the id as a string           | default      |
| `status-defined-by-authorisation` | A valid project whose leaf stands at `defined` with a reviewer stated there and no `Reviewed:` commit; the authorisation is the review, and S11 stays silent | default      |
| `siblings-same-order`  | A valid project with two siblings at `order: 1` and one T12 warning; the tree sorts them by id                                           | default      |
| `unknown-trailer`      | A valid project whose history carries `Authorised: zzzz` and `Reviewed: 9f31 nowhere`, two H1 warnings, and no effect on any derived fact | `history.sh` |
| `review-by-non-reviewer` | A valid project where a `Reviewed:` commit comes from someone other than the junction's reviewer: one H2 warning, and the gate stays unreviewed | `history.sh` |
| `tableaux-tooling`     | This repository at a named commit, read in place                                                                                        | none         |

Invalid entries, one per rule in [RULES.md](RULES.md), 69 in all. Each is `base/` plus the one deviation its name states, and its `expected.yaml` lists the finding, or the findings when one deviation trips two rules (`tree-no-root` trips T8 and T10). The rule table names each entry.

| Rule group           | Entries                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Project and version  | `no-tableaux-directory`, `version-missing`, `version-bad-pattern`, `version-unknown-field`, `version-major-mismatch`, `version-minor-ahead`                                                                                                                                                                                                                       |
| Gates                | `gates-missing`, `gates-first-not-undefined`, `gates-only-undefined`, `gates-gate-missing-criteria`, `gates-bad-key`, `gates-duplicate-gate`, `gates-no-states`, `gates-negative-severity`, `gates-duplicate-state`, `gates-duplicate-reason`, `gates-unknown-field`, `gates-no-undefined-state`, `gates-complete-nonzero-severity` |
| Tasks and tree       | `task-bad-filename`, `task-missing-assignee`, `task-id-field`, `task-bad-email`, `task-reference-without-url`, `task-bad-id-pattern`, `tree-no-root`, `tree-two-roots`, `tree-parent-missing`, `tree-parent-cycle`, `task-parent-order-not-integer`, `task-parent-order-zero` |
| Requires             | `requires-missing-task`, `requires-cycle`, `requires-self`, `requires-ancestor`, `requires-descendant`, `requires-from-not-applicable`, `requires-from-unknown-gate`, `requires-to-not-applicable`, `requires-unknown-field`, `requires-to-undefined` |
| Junctions            | `junction-unknown-gate`, `junction-undefined-not-applicable`, `recursive-on-parent`, `junction-mixed-kind`, `junction-model-without-contributor`, `junction-applies-true`, `junction-subproject-without-url`, `subproject-path-missing`, `subproject-task-missing`, `junction-unknown-field`, `junction-undefined-plain`, `junction-undefined-recursive`, `junction-all-not-applicable` |
| Status               | `status-no-task`, `status-on-parent`, `status-missing-gate`, `status-unknown-field`, `status-undefined-gate-nominal-state`, `status-nominal-gate-undefined-state`, `status-unknown-gate`, `status-unknown-state`, `status-unknown-reason`, `status-gate-not-applicable`, `status-last-gate-not-complete`, `status-state-with-recursive`, `status-no-state-plain`, `status-unreviewed-gate`, `status-complete-early` |

`subproject-path-missing` and `subproject-task-missing` need a submodule and build from a `history.sh`; every other invalid entry builds from the default commit.

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
| W11   | 09-26 | ben | Pins `firmware` at F2 and records `c07d` at `design` with no state                            |
| W12   | 09-27 | dan | Revises `3c5d`; the change returns it to proposed                                             |
| W13   | 09-28 | ada | An empty commit with `Reaffirmed: 9f31`                                                       |

`expected.yaml` then fixes what follows: `9f31` is authorised by the merge on the first-parent line, dated 09-28 by the reaffirmation, and its `mockup` review is W9; `3c5d` is proposed again after W12; `c07d` shows `design` from its own file and `nominal`, its note and its 09-17 date from `f1a0` at the pin, with one unmet requirement on `9f31`; `7b2e` is undefined and dated by W1; `4e2b` rolls up to `design`, `nominal` from `c07d`, since roll-up takes the child at the earliest gate; the root rolls up to `defined`, `nominal` from `3c5d`; and on the branch `sensor-board` every task is proposed.

## This project as an entry

`entries/tableaux-tooling/expected.yaml` names this repository (`source: { repository: ../../.., ref: c764f8a }`) and states facts about it: thirty-seven tasks, the owner, every task authorised because the owner committed the plan on `main`, the resolved junctions of `fcec` under the root's review policy, its pending requirement on `e3cb`, and `77b2`'s recursive junction to `subprojects/tablo` at the pinned commit. The build skips it. When a commit on `main` changes those facts, the entry's `ref` and facts move together, so the corpus always describes one fixed commit of this repository and never its tip.

The entry records that at `fcec`'s gates after `defined` the agent is its own reviewer by the method's default, so the commit that records each such status carries `Reviewed: fcec <gate>` by the agent, or rule S11 fires. At `defined`, the owner's authorisation stands as the review. See Q1 and Q2.

## How a tool consumes the corpus

`tablo`'s conformance test runs `build.sh`, then for each entry: reads `build/<entry>` at `ref` (or `source` for an entry read in place), validates it, and compares the findings with `expected.findings` by rule id and location; then, for a valid entry, derives the facts and compares each one `expected.yaml` states, translating labels to hashes through `labels.txt`. A finding whose rule id the tool does not know fails the test, so a new rule in RULES.md pulls the tool along. A fact marked `undecided: <finding>` passes with either reading until the finding resolves.

## Questions for review

- **Q1 S11 severity.** Decided at design review: the validator rejects a status that passes an unreviewed junction, as README.md says. The consequence for this repository, every agent-recorded status invalid, resolves through Q2.
- **Q2 The agent as its own reviewer.** Decided at design review, in two parts. First, F8 resolves: authorising a task stands as the review of its `defined` gate, so no status at `defined` needs a `Reviewed:` commit, and every status this repository holds today is valid. Second, at every later gate where the agent is its own reviewer, the commit that records the status carries `Reviewed: <id> <gate>`, authored by the agent, so status and review land together. README.md states both. F2's proposal of a human default reviewer stays open in task `ac33`.
- **Q3 Implicit rules.** J8, J9 and S7 have no sentence. Keep them as rules with a sentence added to README.md, or drop their entries?
- **Q4 Candidate rules.** Decided at design review: all eight candidates become rules, and README.md and SYNTAX.md now state them (RULES.md, "Candidate rules, resolved").
- **Q5 Entry granularity.** One entry per rule gives 69 invalid entries of five files each. The alternative is one entry per file with several findings each, about twelve entries. The build cost is the same; the difference is how a failing test reads.
- **Q6 The read-in-place entry's ref.** A hash pins the facts but goes stale on every merge; a tag such as `corpus/tooling` that the owner moves is easier to keep current. Which?

## Findings about the method

Enumerating the rules found the following. Each is one sentence and names the task it belongs to under D6.

- **F11 Deciding commits and events disagree on merges.** The deciding commit reads first-parent history, where a `--no-ff` merge that brings in a task file counts, but the event commands in README.md use the default log, where the same merge does not appear, so a merge that authorises leaves no `authorised` event unless it carries the trailer. Task `7166`.
- **F12 The pin change has no event kind.** README.md says each change of a submodule pin is an event in the parent's log, but the history schema's `event` enum has no value for it. Task `9f3f`.
- **F13 A reaffirmation of a recursive junction is moot.** README.md's example reaffirms `c07d`, whose date comes from the subproject at the pin, so the trailer changes nothing a tool derives. Task `9f3f`.
- **F14 Roll-up hides a severe child at a later gate.** The parent takes the most severe child at the earliest gate, so `4e2b` shows `nominal` while `9f31` stands `stalled` at a later gate; the text may intend this, and a view should say where the stalled child is. Task `7166`.
- **F15 The review may follow the status it validates.** SYNTAX.md's example records `mockup` on 09-22 and reviews it on 09-24; the status is invalid for two days by S11 and valid at the tip, and the text does not say whether a history replay applies S11 at each commit. Task `7166`.
- **F16 An unquoted id fails the schema before the warning.** SYNTAX.md warns of an unquoted id and says a tool takes any scalar as a string, but the schema types every id as a string, so a tool must coerce before validating or the warning never fires. Task `7166`.
- **F17 The undefined leaf has a date but no recorder.** A leaf with no status file is dated by its task file's newest commit; whether that commit's author is its recorder is unstated. Task `7166`.
- **F18 Nothing requires the `undefined` and `complete` states.** S4 and S8 name them and roll-up assumes their severity is 0, but `gates.yaml` may omit them. Task `7166`.

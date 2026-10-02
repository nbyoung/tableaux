# Tableaux tooling plan

This repository plans the software that supports Tableaux as a Tableaux project. The plan is [`.tableaux/`](.tableaux/); this document carries what the task files refer to and cannot hold. The effort dog-foods the method: it aims to refine and validate Tableaux as a means to maximise human productivity through agentic assistance, so agents contribute at every gate and people review at strategic junctions only.

- [Decisions](#decisions)
- [Language](#language)
- [Subprojects](#subprojects)
- [Roles](#roles)
- [Views](#views)
- [Review policy](#review-policy)
- [The plan at a glance](#the-plan-at-a-glance)
- [Findings](#findings)
- [Next steps](#next-steps)

## Decisions

The plan proposes; the owner decides. Each decision that goes the other way changes the files named in its last column.

| #  | Decision                   | Proposal                                                                                    | Where it lands                                    |
|----|----------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------|
| D1 | Implementation language    | Go, with CI-built binaries for Linux, macOS and Windows on amd64 and arm64; no user installs Go | The bootstrap task of every subproject            |
| D2 | Subproject names and repos | `tablo`, `tabloio`, `tablotui`, `tableaud`, each its own repository under `github.com/nbyoung`, pinned here as submodules under `subprojects/`; see F3 | The four subproject tasks, their charters and `.gitmodules` |
| D3 | Agent Git identity         | Agents commit as `noreply@anthropic.com` until task `ac33` decides the rule                 | Every `contributor` and agent `assignee` field    |
| D4 | Review policy              | The owner reviews mockup, design, validation and release; agents own execution subtrees; see F2 | The root task's junctions and the assignees       |
| D5 | Authorise the plan         | Commit `.tableaux/` and this document on `main`                                             | Every task turns from proposed to authorised      |
| D7 | Model per gate             | A model family per junction, stated by prefix (F20): `claude-haiku` records `defined`, `claude-sonnet` builds and tests, `claude-opus` designs and draws mockups, `claude-fable` designs the language; see [Review policy](#review-policy) | The root tasks' junctions here and in each subproject, `bc63`, and three `tablo` leaves |
| D6 | Defer the findings         | The [findings](#findings) resolve through tasks `ac33`, `9f3f` and `7166` (F19 joined `7166` and F20 joined `ac33` on 2026-09-30), not before D5    | Those tasks' design gates, which the owner reviews |
| D8 | Task-file edits as `defined` work | The evidence report counts every change to a task file as work at `defined`, since the definition is that gate's deliverable; a model outside the `defined` junction's model is a mismatch whatever gate the task's status stands at | [evidence/README.md](evidence/README.md) and `evidence/report.py` |

## Language

The plan proposes **Go** for every subproject, distributed as prebuilt binaries.

### Distribution

No Tableaux user installs Go. Each subproject's continuous integration cross-compiles from one Linux runner, since Go builds for any target from any host with `GOOS` and `GOARCH` set, and publishes one static binary per tool for Linux, macOS and Windows on amd64 and arm64. The subprojects use no cgo, so a binary depends on nothing on the host but `git`, which every Tableaux participant has already.

| Path                      | Who uses it                                        | What happens                                                              |
|---------------------------|----------------------------------------------------|---------------------------------------------------------------------------|
| Release download          | Anyone                                             | Fetch one file from the GitHub release page and run it                    |
| Install script            | Agents and CI                                      | A one-line `curl` that picks the file for the host and puts it on the path |
| Homebrew tap and `winget` | People on macOS and Windows                        | The package managers they already use                                     |
| `go install`              | People who have Go and want the trunk              | A convenience, never the requirement                                      |

A CI job that regenerates `STATUS.md` downloads `tabloio` as one step. A pre-commit hook calls `tablo validate` in a few milliseconds. The daemon runs from a checked-out repository on any of the six targets. GoReleaser or an equivalent workflow produces all of this from one configuration file, and each bootstrap task delivers it.

### Why Go

- **The end state is a file the user runs.** Go and Rust both reach it. Python asks every user for an interpreter, or for `uv` to fetch one, and turns the question of distribution into one of environments.
- **Invocation cost shapes the architecture.** The plumbing runs on every hook, every CI step, every TUI refresh and every HTML fragment. Go starts in milliseconds; Python starts in about a hundred and then imports its YAML and schema libraries, which pushes a Python design toward a long-lived process that suits the daemon and fights the hook and the command line.
- **Deterministic checks carry the unreviewed gates.** The review policy leaves function, implementation, unit and integrate to agents alone. The compiler, `gofmt`, `go vet`, the race detector and a fast test loop catch most of what a reviewer would.
- **The standard library covers the daemon.** `net/http`, `html/template` and `embed` serve HTML with the schemas, templates and HTMX inside the binary. No JavaScript build exists.
- **The ecosystem fits this kind of tool.** Bubble Tea and Lip Gloss give the TUI; `goccy/go-yaml` parses with line positions for diagnostics; `santhosh-tekuri/jsonschema` validates draft 2020-12. The tools shell out to `git` for history, as the method's own examples do. Git's porcelain, `gh`, `lazygit`, `glow` and `hugo` show the shape.

### Alternatives

| Concern                    | Go                                             | Python                                                        | Rust                                                     |
|----------------------------|------------------------------------------------|---------------------------------------------------------------|----------------------------------------------------------|
| What the user installs     | One binary                                     | An interpreter plus `uv tool install` or `pipx`               | One binary                                               |
| Who builds it              | CI, all six targets from one Linux runner      | Nobody; PyPI ships source and wheels                          | CI, with a runner or cross toolchain per platform        |
| Standalone fallback        | Not needed                                     | PyInstaller or Nuitka: large per-platform bundles, fragile with a TUI | Not needed                                       |
| Startup                    | Milliseconds                                   | About a hundred milliseconds plus imports                     | Milliseconds                                             |
| Checks before tests        | Types, vet, race detector                      | Optional, through pyright in strict mode                      | The strongest of the three                               |
| Agent iteration            | Fast                                           | Fastest                                                       | Slowest; the borrow checker and compile times compound   |
| TUI toolkit                | Bubble Tea                                     | Textual, the best of the three                                | ratatui                                                  |
| Precedent                  | Git-adjacent tools                             | The Parcel family                                             | None this tool set needs                                 |

**Python** wins if family consistency with Parcel outweighs invocation cost, if the plumbing turns out to run mainly inside the daemon, or if Textual's quality decides the TUI. With `uv` the runtime ask is small. Choosing it changes D1 and the four bootstrap tasks and nothing else in the plan.

**Rust** reaches the same end state as Go with stronger checks and the same startup, at the price of the slowest agent iteration and a harder release matrix, and nothing in this tool set needs what it adds.

Every option gains JavaScript if the daemon needs client-side script beyond HTMX. The HTML mockups decide that.

## Subprojects

Git separates plumbing, which reads the repository and emits data, from porcelain, which presents it and takes commands. This plan does the same: `tablo` is the plumbing, and each front-end mode is one porcelain project. A front end never reads a task file; it takes view data from `tablo`.

| Project    | Name plays on                                  | Mode                        | Git analogue                          | Depends on                 |
|------------|------------------------------------------------|-----------------------------|---------------------------------------|----------------------------|
| `tableaux` | —                                              | The language                | The format and protocol documents     | —                          |
| `tablo`    | The pronunciation                              | Backend library and command | Plumbing: `rev-parse`, `cat-file`     | `tableaux` schemas         |
| `tabloio`  | The pronunciation joined to *io*, input and output | Command line: output and input | Porcelain: `log`, `commit`, `merge` | `tablo`                    |
| `tablotui` | The pronunciation joined to *tui*              | Terminal user interface     | `add -p`, `tig`                       | `tablo`, `tabloio` actions |
| `tableaud` | *Tableau* joined to the *d* of a daemon        | Local daemon and HTML       | `instaweb`, gitweb                    | `tablo`                    |

Each view exists in three places: its abstract definition in `tableaux` (VIEWS.md, task `e9c6`), its derivation as data in `tablo`, and its rendering in each front end. The textual formats live in `tabloio`, since a static snapshot is a command's output that CI, email and chat carry. `tabloio` has two sides. Its output side renders any view as Markdown by default, or as a Unicode drawing with `--text` for a terminal or a log with no Markdown viewer; no output changes project state, and scripts take the view data as JSON or YAML from `tablo view` directly. Its input side operates the method, and every change it makes is a Git commit. The HTML format lives in `tableaud`, since interaction needs a server or an export. `tablotui` renders the same data to a terminal grid.

Each subproject is its own repository with its own owner, plan and releases, and this repository pins all four as submodules under `subprojects/`. The four subproject tasks name each by that path and delegate every gate after `defined` through recursive junctions, so the umbrella reads a subproject's status at the commit the submodule pins and advances that snapshot deliberately, as the method intends. A plain clone of this repository fetches the language alone; `--recurse-submodules` fetches the implementations. A committed `go.work` here makes the four modules build as one family against local checkouts. The price is submodule discipline: push the subproject before the pin, check out submodules in CI, and bump a pin when the umbrella should see an advance. A project that cannot use submodules names the repository by absolute URL and `commit` instead (F3, resolved by task `9f3f`). Skeletons for all four stand beside this repository, each with its charter, licence, gates and plan, and none is committed or pushed.

The `tableaux` repository keeps the language: method, syntax, schema files (task `e3cb`), the conformance corpus (task `fcec`), the abstract views and their mockups under `docs/mockups/`, and this plan.

## Roles

Nothing declares a role. A person or agent holds one wherever their email appears in the position that defines it, and holds several at once.

| Role        | Who holds it                              | What it may do                                                                    | Views that serve it                              |
|-------------|-------------------------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------|
| Owner       | The root task's assignee                  | Authorise any task, transfer ownership, release                                   | Global tableau, authority, audit, everything     |
| Authority   | The assignee of a parent task             | Authorise tasks in its subtree, restate junction defaults for it, propose children | Authority, assignment, blockage, contextual tableau |
| Assignee    | A task's `assignee`                       | Do the task's work by default, review its agents by default, record status        | Contextual tableau, task, queue                  |
| Contributor | A junction's `contributor`                | Do the work at that gate, record status, reaffirm                                 | Queue, task, contextual tableau, gates           |
| Agent       | A contributor with a `model`              | As a contributor; a reviewer accepts its work                                     | Queue as a brief, task                           |
| Reviewer    | A junction's `reviewer`                   | Accept the work at the gate with a `Reviewed:` trailer                            | Queue, task, history                             |
| Observer    | Anyone with no email in the project       | Read                                                                              | Global tableau, gates, history, through `STATUS.md` or a static export |

In this plan the owner holds owner, authority, assignee and reviewer, and the agent holds authority over the mockup, schema, corpus and evidence subtrees, assignee of their tasks, and contributor at nearly every gate. Task `c2ad` writes the roles into README.md.

## Views

Every view answers one question, takes the same focusing parameters (a task, a person, a gate window or a list of columns, a switch for the historical junctions, a ref or a ref range, and the role that sets the disclosure level) and renders in both formats.

| View                   | Question                                    | Roles                                 | Markdown                                                   | HTML                                                                    |
|------------------------|---------------------------------------------|---------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------|
| Gate definition        | What do the columns and symbols mean?       | All                                   | The legend as tables                                       | The legend; criteria fold                                               |
| Task definition        | What is this task and where does it stand?  | All                                   | One task per file                                          | A page; junctions, requirements and history expand                      |
| Authority delegation   | Who may accept what?                        | Owner, authorities                    | The tree indented by assignee; proposed tasks marked       | The tree expands; a filter shows proposed tasks only                    |
| Task assignment        | What does each person carry?                | Owner, authorities, assignees         | One section per email                                      | One page per email                                                      |
| Contributor work queue | What do I do next?                          | Contributors, reviewers, authorities  | A list per person; `--brief` writes an agent's brief       | A personal page; an item expands to its brief                           |
| Work-blockage tree     | What waits on what?                         | Owner, authorities, contributors      | A tree rooted at the causes                                | Causes expand to what they block; one link to the task                  |
| Global tableau         | How does the whole project stand?           | Owner, observers                      | `STATUS.md`                                                | The root collapsed; expand down the hierarchy; columns hidden and shown per viewer |
| Contextual tableau     | How does my corner stand?                   | Assignees, contributors               | A subtree, or the neighbourhood of a person's tasks, in a gate window | A contributor's landing page; a gate window around their next gates, columns hidden and shown per viewer |
| History                | What happened, when, and who did it?        | All                                   | An event table between two refs                            | A timeline with the status after each event                             |
| Audit                  | Where do files and history disagree?        | Owner, authorities                    | A findings table                                           | Findings grouped by the action that resolves them                       |

Markdown is the static medium: one file, plain tables and symbols, no script, so it travels as an attachment, a chat message, a `STATUS.md` that CI regenerates, or a brief in an agent's prompt. `tabloio` also writes each view as a Unicode drawing for places with no Markdown viewer; that format shares the Markdown mockups' content and needs none of its own. Scripts take the view data as JSON or YAML from `tablo`. HTML is the interactive medium: a page from a local daemon with progressive disclosure per role, or the same pages exported as a static bundle.

Gate columns follow one rule in every format. Long-complete junctions and far-off ones rarely bear on a near-term decision, so a tableau opens on a **gate window**: the next gates of the tasks in view and one column either side, with each column outside folded to the count of tasks whose current gate lies in it, as `e9c6`'s design review decided. The window is a default the view computes, not a policy a role imposes. A cell before a task's current gate is historical and shows no mark unless the viewer asks for the historical junctions. From there the viewer hides or shows any column, and the choice persists: in the browser for HTML, in a settings file for the terminal, and in a flag for Markdown, where CI fixes it once. A link to an HTML page carries the columns it shows, so a shared page opens as its sender saw it.

The twenty leaves under Markdown views and HTML views are the mockup tasks, one per view per format. An agent makes each mockup by hand and depicts this project in it, so the owner reviews each design against work they know. [The plan at a glance](#the-plan-at-a-glance) below stands in for the global tableau in Markdown until task `ab8e` replaces it.

## Review policy

The root task states junction defaults that every task inherits.

| Gate                                         | Contributor | Model (D7)                        | Reviewer                                    |
|----------------------------------------------|-------------|-----------------------------------|---------------------------------------------|
| defined                                      | Agent       | `claude-haiku`                    | None stated; the authorisation stands as the review (F8, resolved) |
| mockup                                       | Agent       | `claude-opus`                     | The owner                                   |
| design                                       | Agent       | `claude-opus`; `claude-fable` under Method | The owner                          |
| function, implementation, unit, integrate    | Agent       | `claude-sonnet`; `claude-opus` for tablo's semantics | None stated; the compiler, vet, tests and corpus stand in |
| validate                                     | Agent       | `claude-sonnet`; `claude-opus` under Method | The owner                         |
| release                                      | The owner   | —                                 | —                                           |

The model column estimates the least capable model that does each gate's work well, so that the effort's cost follows its difficulty. Recording `defined` is clerical: the criteria already hold once the owner authorises, and `claude-haiku` writes the status. Building, testing and integrating Go against a design and a corpus is bounded work with a compiler and tests as the reviewer, and `claude-sonnet` carries it; `tablo`'s loader, validator, derivation and audit carry the method's semantics, so their implementation goes to `claude-opus`. A design or a mockup fixes what every later gate builds and the owner reviews it by eye, so `claude-opus` draws it. The language itself, the Method branch's design and the abstract views, goes to `claude-fable`, and the Method's validation, which shows that tools and corpus follow the text, goes to `claude-opus`. Each name is a prefix, so a revision within a family needs no plan change, and the `Model:` trailer on every agent commit lets the evidence report test the estimate against what each gate in fact cost.

The method gives an agent contributor with no stated reviewer the assignee as reviewer. The choice of assignee therefore decides where human review falls at the gates the owner leaves unstated. Owner-assigned tasks, which are the method decisions `ac33`, `9f3f` and `7166` and the four subproject roots, get the owner's review at every gate. Agent-assigned subtrees, which are the roles, views, mockups, schemas, corpus, evidence and every subproject leaf, review themselves at the execution gates: the commit that records such a status carries `Reviewed: <id> <gate>`, authored by the agent, so the status passes rule S11 of the corpus without a second commit. Every agent commit also carries `Model:` with the model that ran (F20), and a dispatcher passes the junction's `model` to the agent it spawns. The tableau below shows the result in each cell.

| Cell  | Meaning                                       |
|-------|-----------------------------------------------|
| 🤖    | An agent works; no person reviews             |
| 🤖👀  | An agent works; a person reviews              |
| 🧑    | A person works                                |
| 🪆    | A subproject does the work                    |
| —     | The gate does not apply                       |
| ⚪    | The task's current gate and state             |

Task `7861` measures this policy against the aim, and the measurement feeds the next refinement of the method.

## The plan at a glance

The umbrella project rendered as the global tableau. Every task stands at the undefined gate until the owner commits the plan and the first reviews land. A parent row shows the defaults its children inherit; its status derives from theirs.

| Id | Task | ❔ | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 | 🌍 | 🚀 |
|----|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `437e` | **Tableaux tooling** | ⚪ | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🧑 |
| `bc63` | &nbsp;&nbsp;**Method** | ⚪ | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🧑 |
| `c2ad` | &nbsp;&nbsp;&nbsp;&nbsp;Roles | ⚪ | 🤖 | — | — | 🤖👀 | 🤖 | — | — | 🤖👀 | 🧑 |
| `2034` | &nbsp;&nbsp;&nbsp;&nbsp;**Views** | ⚪ | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🤖👀 | 🧑 |
| `e9c6` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abstract views | ⚪ | 🤖 | — | — | 🤖👀 | 🤖 | — | — | 🤖👀 | 🧑 |
| `bc86` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Markdown views** | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `99f0` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gate definition view in Markdown | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `05a9` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task definition view in Markdown | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `a9ce` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authority delegation view in Markdown | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `bb7c` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task assignment view in Markdown | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `c74a` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contributor work queue view in Markdown | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `efff` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Work-blockage tree view in Markdown | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `ab8e` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Global tableau view in Markdown | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `c545` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contextual tableau view in Markdown | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `d615` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;History view in Markdown | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `b14e` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Audit view in Markdown | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `5fe3` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HTML views** | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `a6f7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gate definition view in Html | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `7dff` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task definition view in Html | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `b1b7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authority delegation view in Html | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `ea51` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task assignment view in Html | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `7783` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contributor work queue view in Html | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `5471` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Work-blockage tree view in Html | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `32e7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Global tableau view in Html | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `69eb` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contextual tableau view in Html | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `3194` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;History view in Html | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `a8b4` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Audit view in Html | ⚪ | 🤖 | 🤖👀 | — | — | — | — | — | — | — |
| `e3cb` | &nbsp;&nbsp;&nbsp;&nbsp;Schema files | ⚪ | 🤖 | — | — | 🤖👀 | 🤖 | 🤖 | — | 🤖👀 | 🧑 |
| `fcec` | &nbsp;&nbsp;&nbsp;&nbsp;Conformance corpus | ⚪ | 🤖 | — | — | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `ac33` | &nbsp;&nbsp;&nbsp;&nbsp;Agent identity | ⚪ | 🤖👀 | — | — | 🤖👀 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `9f3f` | &nbsp;&nbsp;&nbsp;&nbsp;Subproject linkage | ⚪ | 🤖👀 | — | — | 🤖👀 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `7861` | &nbsp;&nbsp;&nbsp;&nbsp;Productivity evidence | ⚪ | 🤖 | — | — | 🤖👀 | 🤖 | — | — | 🤖👀 | 🧑 |
| `7166` | &nbsp;&nbsp;&nbsp;&nbsp;Language clarifications | ⚪ | 🤖👀 | — | — | 🤖👀 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `77b2` | &nbsp;&nbsp;tablo: backend library and plumbing | ⚪ | 🤖👀 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `6103` | &nbsp;&nbsp;tabloio: command line and Markdown | ⚪ | 🤖👀 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `c6e8` | &nbsp;&nbsp;tablotui: terminal user interface | ⚪ | 🤖👀 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `595e` | &nbsp;&nbsp;tableaud: local daemon and HTML | ⚪ | 🤖👀 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |

Each subproject's plan sits in its own repository and follows the same shape: a bootstrap task, then the components in dependency order, with the view work split into structural, status and temporal groups.

| Subproject | Tasks | Leaves | The first leaf with no unmet requirement |
|------------|-------|--------|------------------------------------------|
| `tablo`    | 12    | 10     | Bootstrap `0d83`                         |
| `tabloio`  | 11    | 9      | Bootstrap `0a2f`                         |
| `tablotui` | 7     | 6      | Bootstrap `0098`                         |
| `tableaud` | 11    | 9      | Bootstrap `7425`                         |

## Findings

Writing the plan in Tableaux found the following about the method. Each names the task that resolves it under decision D6. Three findings already shaped the plan, and each of those names the decision it influenced, so a reader sees which findings stand open and which are half-decided.

- **F1 Agent identity in commits.** The method identifies a contributor by commit email, but an agent in a person's session commits under that person's identity with a `Co-Authored-By:` trailer. The history then attributes the agent's work to the person, and the audit cannot see agent contributions. Proposal: an agent commits with its own identity, set by the harness, and the method also reads `Co-Authored-By:` as marking agent contribution. Task `ac33`.
- **F2 Review of an agent under an agent.** An agent contributor with no stated reviewer takes the assignee as reviewer. When the assignee is an agent, the agent reviews itself, and when the assignee is a person, nothing can waive that person's review. This plan uses the first case deliberately to keep human review at strategic gates, which is decision D4. Proposal: the default reviewer is the nearest human authority, and a junction may waive review explicitly. Task `ac33`.
- **F3 Subproject by URL.** A recursive junction reads the subproject at the commit a submodule pins. A repository named by URL has no pin and no local path, so a tool cannot resolve it offline or reproducibly. Decision D2 avoids the case here by pinning the subprojects as submodules, and the finding stays open for projects that cannot. Proposal: an optional `commit` field on the junction, and a tool-side mapping from URL to local checkout like Go's `replace`. Task `9f3f`. Resolved at `9f3f`'s design (2026-09-30): a `url` is a submodule path read at its pin, a same-repository path read at the parent's commit, or an absolute URL with a required `commit` that a tool reaches through a local mapping or a cache, and every change of the commit read is a `pin` event; the fields raise the language to 0.3.0.
- **F4 Wholesale delegation.** A task delegated to a subproject restates the recursive junction at every gate; each of the four subproject tasks carries eight identical entries. Proposal: a task-level `subproject` field that applies to every gate after `defined`. Task `9f3f`.
- **F5 Requirements stop at the project.** A subproject task cannot require a task in the umbrella, such as the mockups it renders, and falls back to a reference. Proposal: allow `requires` entries with a `subproject`, or accept that references suffice. Task `9f3f`. Resolved at `9f3f`'s design (2026-09-30): a `requires` entry names a task in another project with the `subproject` shape a recursive junction uses, upward by absolute URL and `commit`, and its condition reads that task at the commit the linkage fixes.
- **F6 Ids that YAML reads as numbers.** An id of four digits, such as `1000`, and an id such as `1e10` parse as numbers unless quoted. Resolved before D5: SYNTAX.md now requires a quoted id and a tool that takes an id as a string whatever YAML yields, README.md states that ids are random, and every id in this plan is a random quoted hexadecimal string. The validator rule falls to `tablo`.
- **F7 Inheritance across a not-applicable entry.** A plain entry inherits field by field from its ancestors, and a not-applicable entry exempts a subtree until a descendant states its own entry. Whether that descendant's plain entry inherits fields from ancestors above the not-applicable one is unstated. This plan avoids the case. Task `7166`.
- **F8 Authorisation and the defined gate.** Authorising a task accepts its definition, and reviewing its `defined` gate does the same; a plan of forty tasks would need forty `Reviewed:` trailers. This plan states no reviewer at `defined`. Resolved at the corpus design review (2026-09-29): authorisation stands as the review of `defined`, and README.md says so; `tabloio review` accepting many tasks at once remains for task `7166`.
- **F9 No state before defined.** The gate is `undefined` exactly when the state is, so work in progress towards `defined` has no state and no reason. Minor; the queue view shows the work instead. Task `7166`.
- **F20 The model as plan and as record.** A junction's `model` reads as the plan's statement, and nothing records the model that ran: the eight agents of the first wave inherited the dispatcher's model and matched the field by luck, not by reading it. Proposed on 2026-09-30: `model` stays the plan's hint, which the dispatcher and the `tabloio` briefs task `e4c7` pass through, and may name a model family by prefix; every agent commit carries a `Model:` trailer with the model that ran; the audit reports a mismatch; and the evidence report costs each gate by model. The trailer raises the language to 0.2.1. Task `ac33`.
- **F19 The trunk rests on convention.** Authorisation reads the trunk's history, and README.md named it only as the repository's default branch. A clone records that branch as `refs/remotes/origin/HEAD`, but a `git init` repository, a continuous-integration checkout that fetches one commit, a git-flow project that integrates on `develop`, and a detached submodule checkout all lack or contradict it, and the `STATUS.md` job and the conformance run live in the first two. Proposed on 2026-09-30, after Git's own `submodule.<name>.branch`: an optional `trunk` field in `version.yaml`, a default of the remote's default branch, then a tool flag, then a warning that the trunk is undetermined; a subproject's `version.yaml` names its trunk and the audit reports a pin off it. The field raises the language to 0.2.0. Task `7166`.
- **F10 An agent as assignee.** Only a junction carries `model`, so an agent assignee looks like a person. Proposal: an optional `model` on the task, or an identities file that maps each email to a name, a kind and a model. Task `ac33`.

## Next steps

1. Decide D1 to D5. A decision that differs from the proposal changes the files it names.
2. Authorise the plan. The owner is an ancestor of every task, so one commit on `main` authorises all thirty-seven:

   ```
   git add .tableaux PLAN.md
   git commit -m 'Plan the Tableaux tooling'
   ```

3. Create the four repositories from the skeletons beside this one, commit each, push, and pin them here as submodules. The skeletons stay where they are, and the loop runs from inside this repository:

   ```
   cd tableaux
   for p in tablo tabloio tablotui tableaud; do
     git -C ../$p add -A && git -C ../$p commit -m "Charter and plan for $p"
     gh repo create nbyoung/$p --public --source ../$p --push
     git submodule add ../$p subprojects/$p
   done
   git add .gitmodules subprojects
   git commit -m 'Pin the subprojects'
   git push
   ```

   The relative submodule URL resolves against this repository's origin, so `.gitmodules` names `github.com/nbyoung/<name>` whether a clone uses SSH or HTTPS.

   Each subproject then has two working copies. The sibling directory beside this repository is the clone to work in, with a branch checked out as usual. The checkout under `subprojects/` is the pin the umbrella reads, and nobody edits there. When the umbrella should see a subproject's advance, pull the pin forward and commit it, which records an event in this project's history:

   ```
   git -C subprojects/tablo pull origin main
   git add subprojects/tablo
   git commit -m 'Advance tablo to its implementation gate'
   ```

   The Go workspace comes later. Once the `tablo` bootstrap task lands a `go.mod`, run `go work init ./subprojects/tablo` here, add each other module as its bootstrap lands, and commit `go.work`; it then builds the family against the pinned commits. For day-to-day work across the siblings, keep a personal `go.work` in the directory above this repository that points at `./tablo` and the others, and leave it uncommitted.

4. Start the agents. Under the review policy the queue for the agent begins with the tasks whose requirements are met: `c2ad` Roles, `e3cb` Schema files, and then `e9c6` Abstract views once `c2ad` reaches design. A brief for each holds the task file, the gate's criteria and the commit the agent makes when done.
5. Review at the first strategic junctions: `e9c6` at design, then each mockup as it lands. The mockups fix what every front end builds.

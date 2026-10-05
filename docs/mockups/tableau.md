# Global tableau

How does the whole project stand? This view answers for **Tableaux tooling** on `main` at `3cdae52`, 2026-10-05.

Viewer nbyoung@nbyoung.com, the owner · window 1, the default, which shows 📝 to 🚀 and folds ❔ · historical junctions off · no person marked.

A row is a task, indented by depth, with a parent in bold. A column is a gate: ❔ undefined · 📝 defined · 📌 mockup · 🔧 function · 📐 design · 🧱 implementation · 📏 unit · 🔗 integrate · 🌍 validate · 🚀 release. The cell at the gate a task passed last holds its state, 🟢 nominal here, and its reason when it has one. Each later cell says who works there: 🤖 an agent, 🧑 a person, 👀 a reviewer who accepts the work, 🪆 a subproject, — nobody, since the gate does not apply. An earlier cell stays empty, since that work is done. A parent's row shows its roll-up and the defaults its subtree inherits. A header such as `❔ ×0` is a folded column with the count of tasks that stand in it. [gates.md](gates.md) defines every gate and symbol.

## Glance

The root and its children. The number after a title counts the rows folded beneath it.

| Id | Task | ❔ ×0 | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 | 🌍 | 🚀 |
|----|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `437e` | **Tableaux tooling** |  | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `bc63` | &nbsp;&nbsp;**Method** (31) |  | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `77b2` | &nbsp;&nbsp;tablo: backend library and plumbing |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `6103` | &nbsp;&nbsp;tabloio: command line, output and input |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `c6e8` | &nbsp;&nbsp;tablotui: terminal user interface |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `595e` | &nbsp;&nbsp;tableaud: local daemon and HTML |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |

| Rows | Date | Note | From |
|------|------------|------|------|
| `437e`, `bc63` | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design | Rolled up from `99f0` |
| `77b2` | 2026-09-30 | The design is next and no requirement gates it | Snapshot of `b2c1` tablo at pin `00f8f68`, which stands at 📝 defined there |
| `6103` | 2026-09-30 | prototype/e3ed renders the gate and task definition views as Markdown at three levels from tablo view data | Snapshot of `07e0` tabloio at pin `4593882`, which stands at 🔧 function there |
| `c6e8` | 2026-09-30 | prototype/679b renders the global tableau as a Bubble Tea grid with tree expand and collapse, scrolling, a folded gate window and hidden columns kept in a settings file; emoji lines align where the terminal widens U+FE0F | Snapshot of `40e8` tablotui at pin `a2878b5`, which stands at 🔧 function there |
| `595e` | 2026-09-30 | prototype/49ce serves the ten views with a stdlib HEAD and .tableaux watcher, ETag 304 polling through htmx, a Source interface and a loopback Host check | Snapshot of `8608` tableaud at pin `e6ec4ec`, which stands at 🔧 function there |

`tabloio tableau --ref main --level glance`

## Detail

Every row: 37 tasks.

| Id | Task | ❔ ×0 | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 | 🌍 | 🚀 |
|----|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `437e` | **Tableaux tooling** |  | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `bc63` | &nbsp;&nbsp;**Method** |  | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `c2ad` | &nbsp;&nbsp;&nbsp;&nbsp;Roles |  |  |  |  |  | 🟢 | — | — | 🤖👀 | 🧑 |
| `2034` | &nbsp;&nbsp;&nbsp;&nbsp;**Views** |  | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `e9c6` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abstract views |  |  |  |  | 🟢 | 🤖 | — | — | 🤖👀 | 🧑 |
| `bc86` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Markdown views** |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `99f0` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gate definition view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `05a9` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task definition view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `a9ce` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authority delegation view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `bb7c` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task assignment view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `c74a` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contributor work queue view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `efff` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Work-blockage tree view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `ab8e` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Global tableau view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `c545` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contextual tableau view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `d615` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;History view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `b14e` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Audit view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `5fe3` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HTML views** |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `a6f7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gate definition view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `7dff` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task definition view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `b1b7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authority delegation view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `ea51` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task assignment view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `7783` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contributor work queue view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `5471` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Work-blockage tree view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `32e7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Global tableau view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `69eb` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contextual tableau view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `3194` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;History view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `a8b4` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Audit view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `e3cb` | &nbsp;&nbsp;&nbsp;&nbsp;Schema files |  |  |  |  |  |  | 🟢 | — | 🤖👀 | 🧑 |
| `fcec` | &nbsp;&nbsp;&nbsp;&nbsp;Conformance corpus |  |  |  |  |  | 🟢 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `ac33` | &nbsp;&nbsp;&nbsp;&nbsp;Agent identity |  |  |  |  | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `9f3f` | &nbsp;&nbsp;&nbsp;&nbsp;Subproject linkage |  |  |  |  | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `7861` | &nbsp;&nbsp;&nbsp;&nbsp;Productivity evidence |  |  |  |  |  | 🟢 | — | — | 🤖👀 | 🧑 |
| `7166` | &nbsp;&nbsp;&nbsp;&nbsp;Language clarifications |  |  |  |  | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `77b2` | &nbsp;&nbsp;tablo: backend library and plumbing |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `6103` | &nbsp;&nbsp;tabloio: command line, output and input |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `c6e8` | &nbsp;&nbsp;tablotui: terminal user interface |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `595e` | &nbsp;&nbsp;tableaud: local daemon and HTML |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |

| Rows | Date | Note | From |
|------|------------|------|------|
| `99f0` … `b14e`, `a6f7` … `a8b4`, twenty | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design | Each status file |
| `437e`, `bc63`, `2034`, `bc86` | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design | Rolled up from `99f0` |
| `5fe3` | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design | Rolled up from `a6f7` |
| `c2ad` | 2026-09-30 | The Roles text is on the trunk and covers all seven roles; the validate gate awaits the owner | Its status file |
| `e9c6` | 2026-09-30 | VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place | Its status file |
| `e3cb` | 2026-09-30 | schemas/check.sh (files agree with SYNTAX.md, version 0.2.1) and schemas/load.py (files load as JSON Schema 2020-12) pass; every .tableaux file validates | Its status file |
| `fcec` | 2026-09-30 | The corpus builds and checks clean, with 85 entries on the trunk; all three corrections from the tablo prototypes are in; the unit gate runs the tablo conformance test against it | Its status file |
| `ac33` | 2026-09-30 | The model plan-and-record rule (F20) is on the trunk; F1, F2 and F10 remain for design | Its status file |
| `9f3f` | 2026-09-30 | The subproject linkage rule (F3, F5, F12) is on the trunk at language 0.3.0; tablo and the subprojects follow | Its status file |
| `7861` | 2026-09-30 | The full report, its 23 tests and an example over five repositories are on the trunk | Its status file |
| `7166` | 2026-09-30 | The trunk clarification (F19) is on the trunk; F7 and F9 remain for design | Its status file |
| `77b2` | 2026-09-30 | The design is next and no requirement gates it | Snapshot of `b2c1` tablo at pin `00f8f68`, which stands at 📝 defined there |
| `6103` | 2026-09-30 | prototype/e3ed renders the gate and task definition views as Markdown at three levels from tablo view data | Snapshot of `07e0` tabloio at pin `4593882`, which stands at 🔧 function there |
| `c6e8` | 2026-09-30 | prototype/679b renders the global tableau as a Bubble Tea grid with tree expand and collapse, scrolling, a folded gate window and hidden columns kept in a settings file; emoji lines align where the terminal widens U+FE0F | Snapshot of `40e8` tablotui at pin `a2878b5`, which stands at 🔧 function there |
| `595e` | 2026-09-30 | prototype/49ce serves the ten views with a stdlib HEAD and .tableaux watcher, ETag 304 polling through htmx, a Source interface and a loopback Host check | Snapshot of `8608` tableaud at pin `e6ec4ec`, which stands at 🔧 function there |

`tabloio tableau --ref main --level detail`

## Provenance

Every row, then the Git fact behind each cell.

| Id | Task | ❔ ×0 | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 | 🌍 | 🚀 |
|----|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `437e` | **Tableaux tooling** |  | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `bc63` | &nbsp;&nbsp;**Method** |  | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `c2ad` | &nbsp;&nbsp;&nbsp;&nbsp;Roles |  |  |  |  |  | 🟢 | — | — | 🤖👀 | 🧑 |
| `2034` | &nbsp;&nbsp;&nbsp;&nbsp;**Views** |  | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `e9c6` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abstract views |  |  |  |  | 🟢 | 🤖 | — | — | 🤖👀 | 🧑 |
| `bc86` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Markdown views** |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `99f0` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gate definition view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `05a9` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task definition view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `a9ce` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authority delegation view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `bb7c` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task assignment view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `c74a` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contributor work queue view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `efff` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Work-blockage tree view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `ab8e` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Global tableau view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `c545` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contextual tableau view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `d615` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;History view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `b14e` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Audit view in Markdown |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `5fe3` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**HTML views** |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `a6f7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gate definition view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `7dff` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task definition view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `b1b7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Authority delegation view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `ea51` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Task assignment view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `7783` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contributor work queue view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `5471` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Work-blockage tree view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `32e7` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Global tableau view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `69eb` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contextual tableau view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `3194` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;History view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `a8b4` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Audit view in Html |  | 🟢 | 🤖👀 | — | — | — | — | — | — | — |
| `e3cb` | &nbsp;&nbsp;&nbsp;&nbsp;Schema files |  |  |  |  |  |  | 🟢 | — | 🤖👀 | 🧑 |
| `fcec` | &nbsp;&nbsp;&nbsp;&nbsp;Conformance corpus |  |  |  |  |  | 🟢 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `ac33` | &nbsp;&nbsp;&nbsp;&nbsp;Agent identity |  |  |  |  | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `9f3f` | &nbsp;&nbsp;&nbsp;&nbsp;Subproject linkage |  |  |  |  | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `7861` | &nbsp;&nbsp;&nbsp;&nbsp;Productivity evidence |  |  |  |  |  | 🟢 | — | — | 🤖👀 | 🧑 |
| `7166` | &nbsp;&nbsp;&nbsp;&nbsp;Language clarifications |  |  |  |  | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `77b2` | &nbsp;&nbsp;tablo: backend library and plumbing |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `6103` | &nbsp;&nbsp;tabloio: command line, output and input |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `c6e8` | &nbsp;&nbsp;tablotui: terminal user interface |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |
| `595e` | &nbsp;&nbsp;tableaud: local daemon and HTML |  | 🟢 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 | 🪆 |

| Rows | Date | Note | From |
|------|------------|------|------|
| `99f0` … `b14e`, `a6f7` … `a8b4`, twenty | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design | Each status file |
| `437e`, `bc63`, `2034`, `bc86` | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design | Rolled up from `99f0` |
| `5fe3` | 2026-09-29 | Mockup waits for Abstract views (e9c6) at design | Rolled up from `a6f7` |
| `c2ad` | 2026-09-30 | The Roles text is on the trunk and covers all seven roles; the validate gate awaits the owner | Its status file |
| `e9c6` | 2026-09-30 | VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place | Its status file |
| `e3cb` | 2026-09-30 | schemas/check.sh (files agree with SYNTAX.md, version 0.2.1) and schemas/load.py (files load as JSON Schema 2020-12) pass; every .tableaux file validates | Its status file |
| `fcec` | 2026-09-30 | The corpus builds and checks clean, with 85 entries on the trunk; all three corrections from the tablo prototypes are in; the unit gate runs the tablo conformance test against it | Its status file |
| `ac33` | 2026-09-30 | The model plan-and-record rule (F20) is on the trunk; F1, F2 and F10 remain for design | Its status file |
| `9f3f` | 2026-09-30 | The subproject linkage rule (F3, F5, F12) is on the trunk at language 0.3.0; tablo and the subprojects follow | Its status file |
| `7861` | 2026-09-30 | The full report, its 23 tests and an example over five repositories are on the trunk | Its status file |
| `7166` | 2026-09-30 | The trunk clarification (F19) is on the trunk; F7 and F9 remain for design | Its status file |
| `77b2` | 2026-09-30 | The design is next and no requirement gates it | Snapshot of `b2c1` tablo at pin `00f8f68`, which stands at 📝 defined there |
| `6103` | 2026-09-30 | prototype/e3ed renders the gate and task definition views as Markdown at three levels from tablo view data | Snapshot of `07e0` tabloio at pin `4593882`, which stands at 🔧 function there |
| `c6e8` | 2026-09-30 | prototype/679b renders the global tableau as a Bubble Tea grid with tree expand and collapse, scrolling, a folded gate window and hidden columns kept in a settings file; emoji lines align where the terminal widens U+FE0F | Snapshot of `40e8` tablotui at pin `a2878b5`, which stands at 🔧 function there |
| `595e` | 2026-09-30 | prototype/49ce serves the ten views with a stdlib HEAD and .tableaux watcher, ETag 304 polling through htmx, a Source interface and a loopback Host check | Snapshot of `8608` tableaud at pin `e6ec4ec`, which stands at 🔧 function there |

**Status cells.** The state symbol of a leaf comes from its status file, `.tableaux/status/<id>.yaml`; the date and the recorder come from the deciding commit of that file.

| Rows | Cell | Date | Recorder | Deciding commit | Committer |
|------|:----:|------------|----------|-----------------|-----------|
| `99f0` … `b14e`, `a6f7` … `a8b4`, twenty | 📝 | 2026-09-29 | noreply@anthropic.com | `1a17bfc` Record the defined gate for the views and mockups | nbyoung@nbyoung.com |
| `c2ad` | 🧱 | 2026-09-30 | noreply@anthropic.com | `3d8ce0e` Record the Roles task at its implementation gate | noreply@anthropic.com |
| `e9c6` | 📐 | 2026-09-30 | noreply@anthropic.com | `879b447` Advance the abstract views task to its design gate | noreply@anthropic.com |
| `e3cb` | 📏 | 2026-09-30 | noreply@anthropic.com | `5cbec7c` Record e3cb at unit, nominal | noreply@anthropic.com |
| `fcec` | 🧱 | 2026-09-30 | noreply@anthropic.com | `60495c2` Record all three corpus corrections at implementation | noreply@anthropic.com |
| `ac33` | 📐 | 2026-09-30 | noreply@anthropic.com | `6762222` Advance the agent identity task to its design gate | nbyoung@nbyoung.com |
| `9f3f` | 📐 | 2026-09-30 | noreply@anthropic.com | `43d68e4` Advance the subproject linkage task to its design gate | noreply@anthropic.com |
| `7861` | 🧱 | 2026-09-30 | noreply@anthropic.com | `c6f2655` Complete the productivity evidence report | noreply@anthropic.com |
| `7166` | 📐 | 2026-09-30 | noreply@anthropic.com | `d9396b4` Advance the language clarifications to their design gate | nbyoung@nbyoung.com |
| `77b2`, `6103`, `c6e8`, `595e` | 📝 | 2026-09-30 | noreply@anthropic.com | `e66abe2` Record the defined gate for the subproject tasks | noreply@anthropic.com |

The four subproject files state the gate alone; the snapshot below supplies the state, the note and the date. No commit reaffirms a status.

**Roll-ups.** A parent's 📝 cell derives from one child: the most severe at the earliest gate, and the first in display order when several tie. Its date is the oldest among the children it considers.

| Parent | Rolls up from | Why that child |
|--------|---------------|----------------|
| `437e` Tableaux tooling | `bc63` Method | The first of its five children, which all stand at 📝 defined 🟢 nominal |
| `bc63` Method | `2034` Views | Its one child at 📝 defined, the earliest gate among the eight |
| `2034` Views | `bc86` Markdown views | The first of `bc86` and `5fe3`, which tie at 📝 defined |
| `bc86` Markdown views | `99f0` Gate definition view in Markdown | The first of its ten children, which all tie |
| `5fe3` HTML views | `a6f7` Gate definition view in Html | The first of its ten children, which all tie |

**Marks.** Each mark resolves field by field from the nearest task file that states the field.

| Cell | Mark | Rows | Contributor and model | Reviewer |
|:----:|:----:|------|-----------------------|----------|
| 📌 | 🤖👀 | The five parents and the twenty mockups | noreply@anthropic.com, `claude-opus`, from `437e` | nbyoung@nbyoung.com, from `437e` |
| 🔧 | 🤖 | `437e`, `bc63`, `2034` | noreply@anthropic.com, `claude-sonnet`, from `437e` | None stated |
| 📐 | 🤖👀 | `437e` | noreply@anthropic.com, `claude-opus`, from `437e` | nbyoung@nbyoung.com, from `437e` |
| 📐 | 🤖👀 | `bc63`, `2034` | noreply@anthropic.com, `claude-fable`, from `bc63` | nbyoung@nbyoung.com, from `437e` |
| 🧱 | 🤖 | `437e`, `bc63`, `2034` | noreply@anthropic.com, `claude-sonnet`, from `437e` | None stated |
| 🧱 | 🤖 | `e9c6` | noreply@anthropic.com, `claude-sonnet`, from `437e` | The agent itself, as the assignee of `e9c6` |
| 🧱 | 🤖👀 | `ac33`, `9f3f`, `7166` | noreply@anthropic.com, `claude-sonnet`, from `437e` | nbyoung@nbyoung.com, as the assignee of each |
| 📏 🔗 | 🤖 | `437e`, `bc63`, `2034` | noreply@anthropic.com, `claude-sonnet`, from `437e` | None stated |
| 📏 🔗 | 🤖 | `fcec` | noreply@anthropic.com, `claude-sonnet`, from `437e` | The agent itself, as the assignee of `fcec` |
| 🌍 | 🤖👀 | `437e` | noreply@anthropic.com, `claude-sonnet`, from `437e` | nbyoung@nbyoung.com, from `437e` |
| 🌍 | 🤖👀 | `bc63`, `2034` and the eight leaves that are not mockups | noreply@anthropic.com, `claude-opus`, from `bc63` | nbyoung@nbyoung.com, from `437e` |
| 🚀 | 🧑 | `437e`, `bc63`, `2034` and the eight leaves that are not mockups | nbyoung@nbyoung.com, from `437e` | None |
| 📌 to 🚀 | 🪆 | `77b2`, `6103`, `c6e8`, `595e` | The subproject, from the row's own file | |
| 🔧 to 🚀 | — | `bc86` and its ten, `5fe3` and its ten | Exempt, from `bc86` and from `5fe3` | |
| 📏 🔗 | — | `c2ad`, `e9c6`, `ac33`, `9f3f`, `7861`, `7166` | Exempt, from the row's own file | |
| 🔗 | — | `e3cb` | Exempt, from the row's own file | |

A parent's mark shows what its subtree inherits, so it names a reviewer only where a file states one. A leaf with an agent and no stated reviewer takes its assignee as reviewer, and 👀 shows when that reviewer is not the contributor.

**Snapshots.** A subproject row reads its state, note and date from the subproject's root task at the commit the submodule pins.

| Row | Subproject | Pin | Pin set by | Root task at the pin | Rolls up from |
|-----|------------|-----|------------|----------------------|---------------|
| `77b2` | `subprojects/tablo` | `00f8f68` | `552d38f`, 2026-10-02, nbyoung@nbyoung.com | `b2c1` tablo: 📝 defined 🟢 nominal, 2026-09-30 | `4b4f` Conformance, `f373729` |
| `6103` | `subprojects/tabloio` | `4593882` | `1c0f04d`, 2026-10-02, nbyoung@nbyoung.com | `07e0` tabloio: 🔧 function 🟢 nominal, 2026-09-30 | `1093` Renderers, then `e3ed` Legend and task renderers, `90e66fc` |
| `c6e8` | `subprojects/tablotui` | `a2878b5` | `fa4551e`, 2026-10-04, nbyoung@nbyoung.com | `40e8` tablotui: 🔧 function 🟢 nominal, 2026-09-30 | `679b` Tableau grid, `66c0412` |
| `595e` | `subprojects/tableaud` | `e6ec4ec` | `3cdae52`, 2026-10-05, nbyoung@nbyoung.com | `8608` tableaud: 🔧 function 🟢 nominal, 2026-09-30 | `49ce` Server, `967df1f` |

Three roots stand at 🔧 function in their own projects while their rows here stand at 📝 defined: the row's gate comes from this project's status file, which its contributor advances.

```
git log -1 --format='%as %h %ae %ce' -- .tableaux/status/c2ad.yaml    # date, commit, recorder, committer of a status cell
git ls-tree HEAD subprojects/                                         # the pin each snapshot reads
git log -1 --format='%as %h %ae' -- subprojects/tabloio               # the commit that sets a pin
```

`tabloio tableau --ref main --level provenance`

## Variations

Each variation changes one parameter and shows the eight children of `bc63` Method as an excerpt of the detail level.

### Historical junctions on

The cells before each task's current gate show who did the work and who accepted it. The other 29 rows read as at detail: each stands at 📝, and ❔ holds no work.

| Id | Task | ❔ ×0 | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 | 🌍 | 🚀 |
|----|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `c2ad` | &nbsp;&nbsp;&nbsp;&nbsp;Roles |  | 🤖 | — | — | 🤖👀 | 🟢 | — | — | 🤖👀 | 🧑 |
| `2034` | &nbsp;&nbsp;&nbsp;&nbsp;**Views** |  | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `e3cb` | &nbsp;&nbsp;&nbsp;&nbsp;Schema files |  | 🤖 | — | — | 🤖👀 | 🤖 | 🟢 | — | 🤖👀 | 🧑 |
| `fcec` | &nbsp;&nbsp;&nbsp;&nbsp;Conformance corpus |  | 🤖 | — | — | 🤖👀 | 🟢 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `ac33` | &nbsp;&nbsp;&nbsp;&nbsp;Agent identity |  | 🤖👀 | — | — | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `9f3f` | &nbsp;&nbsp;&nbsp;&nbsp;Subproject linkage |  | 🤖👀 | — | — | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |
| `7861` | &nbsp;&nbsp;&nbsp;&nbsp;Productivity evidence |  | 🤖 | — | — | 🤖👀 | 🟢 | — | — | 🤖👀 | 🧑 |
| `7166` | &nbsp;&nbsp;&nbsp;&nbsp;Language clarifications |  | 🤖👀 | — | — | 🟢 | 🤖👀 | — | — | 🤖👀 | 🧑 |

`tabloio tableau --ref main --level detail --historical`

### A person marked

Brackets mark the cells where nbyoung@nbyoung.com acts, as reviewer or as contributor. The mark also falls on 🌍 and 🚀 of `e9c6` and on 📌 of each of the twenty mockups, 39 cells in all; a parent's row and a subproject's row carry none.

| Id | Task | ❔ ×0 | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 | 🌍 | 🚀 |
|----|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `c2ad` | &nbsp;&nbsp;&nbsp;&nbsp;Roles |  |  |  |  |  | 🟢 | — | — | [🤖👀] | [🧑] |
| `2034` | &nbsp;&nbsp;&nbsp;&nbsp;**Views** |  | 🟢 | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| `e3cb` | &nbsp;&nbsp;&nbsp;&nbsp;Schema files |  |  |  |  |  |  | 🟢 | — | [🤖👀] | [🧑] |
| `fcec` | &nbsp;&nbsp;&nbsp;&nbsp;Conformance corpus |  |  |  |  |  | 🟢 | 🤖 | 🤖 | [🤖👀] | [🧑] |
| `ac33` | &nbsp;&nbsp;&nbsp;&nbsp;Agent identity |  |  |  |  | 🟢 | [🤖👀] | — | — | [🤖👀] | [🧑] |
| `9f3f` | &nbsp;&nbsp;&nbsp;&nbsp;Subproject linkage |  |  |  |  | 🟢 | [🤖👀] | — | — | [🤖👀] | [🧑] |
| `7861` | &nbsp;&nbsp;&nbsp;&nbsp;Productivity evidence |  |  |  |  |  | 🟢 | — | — | [🤖👀] | [🧑] |
| `7166` | &nbsp;&nbsp;&nbsp;&nbsp;Language clarifications |  |  |  |  | 🟢 | [🤖👀] | — | — | [🤖👀] | [🧑] |

`tabloio tableau --ref main --level detail --person nbyoung@nbyoung.com`

For noreply@anthropic.com the brackets fall on 34 cells: 📌 of the twenty mockups and each later 🤖 cell of the eight leaves that are not mockups.

### A narrower window

Window 0 shows the next gates alone, 📌 to 🌍. A run of folded columns shares one header, and its count covers all 37 tasks: 29 stand at 📝, so the fold hides their state cells, as it hides that of `2034` here.

| Id | Task | ❔…📝 ×29 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 | 🌍 | 🚀 ×0 |
|----|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `c2ad` | &nbsp;&nbsp;&nbsp;&nbsp;Roles |  |  |  |  | 🟢 | — | — | 🤖👀 |  |
| `2034` | &nbsp;&nbsp;&nbsp;&nbsp;**Views** |  | 🤖👀 | 🤖 | 🤖👀 | 🤖 | 🤖 | 🤖 | 🤖👀 |  |
| `e3cb` | &nbsp;&nbsp;&nbsp;&nbsp;Schema files |  |  |  |  |  | 🟢 | — | 🤖👀 |  |
| `fcec` | &nbsp;&nbsp;&nbsp;&nbsp;Conformance corpus |  |  |  |  | 🟢 | 🤖 | 🤖 | 🤖👀 |  |
| `ac33` | &nbsp;&nbsp;&nbsp;&nbsp;Agent identity |  |  |  | 🟢 | 🤖👀 | — | — | 🤖👀 |  |
| `9f3f` | &nbsp;&nbsp;&nbsp;&nbsp;Subproject linkage |  |  |  | 🟢 | 🤖👀 | — | — | 🤖👀 |  |
| `7861` | &nbsp;&nbsp;&nbsp;&nbsp;Productivity evidence |  |  |  |  | 🟢 | — | — | 🤖👀 |  |
| `7166` | &nbsp;&nbsp;&nbsp;&nbsp;Language clarifications |  |  |  | 🟢 | 🤖👀 | — | — | 🤖👀 |  |

`tabloio tableau --ref main --level detail --window 0`

### A reason beside the state

No status at this ref states a reason, so no cell above shows one. This row is an illustration, not the project at the ref: once the hand-off of this mockup lands, `ab8e` waits for its reviewer and its cell reads 🟢👓.

| Id | Task | ❔ ×0 | 📝 | 📌 | 🔧 | 📐 | 🧱 | 📏 | 🔗 | 🌍 | 🚀 |
|----|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `ab8e` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Global tableau view in Markdown |  | 🟢👓 | 🤖👀 | — | — | — | — | — | — | — |

## See also

- [gates.md](gates.md): the legend of every column and symbol.
- [context.md](context.md): the same grid over one corner of the tree.
- [task.md](task.md): one row in full.
- [blockage.md](blockage.md): what each waiting row waits on.
- [history.md](history.md): how each row reached its cell.

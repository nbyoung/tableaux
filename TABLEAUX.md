# Global tableau

**How does the whole project stand?** Tableaux tooling · ref `main` · window 1 · level glance

Legend: `tabloio gates`.

| Id | Task | ❔…📐 ×22 | 🧱 | 📏 | 🔗 | 🌍 | 🚀 |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|
| [`437e`](.tableaux/tasks/437e.yaml) | **Tableaux tooling** |  | 🟢 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| [`bc63`](.tableaux/tasks/bc63.yaml) | &nbsp;&nbsp;**Method** (31) |  | 🟢 | 🤖 | 🤖 | 🤖👀 | 🧑 |
| [`77b2`](.tableaux/tasks/77b2.yaml) | &nbsp;&nbsp;tablo: backend library and plumbing |  |  |  |  | 🟢 | 🪆 |
| [`6103`](.tableaux/tasks/6103.yaml) | &nbsp;&nbsp;tabloio: command line, output and input |  |  |  |  | 🟢 | 🪆 |
| [`c6e8`](.tableaux/tasks/c6e8.yaml) | &nbsp;&nbsp;tablotui: terminal user interface |  |  |  |  | 🟢 | 🪆 |
| [`595e`](.tableaux/tasks/595e.yaml) | &nbsp;&nbsp;tableaud: local daemon and HTML |  |  |  |  | 🟢 | 🪆 |

❔ undefined · 📐 design · 🧱 implementation · 📏 unit · 🔗 integrate · 🌍 validate · 🚀 release · 🟢 nominal · 🧑 a person contributes · 🤖 an agent contributes · 👀 a reviewer accepts · 🪆 a subproject does the work.

## Notes

| Rows | Date | Note | From |
|---|---|---|---|
| `437e` | 2026-09-30 | The Roles text is on the trunk and covers all seven roles; the validate gate awaits the owner | rolled up from `bc63` Method |
| `bc63` | 2026-09-30 | The Roles text is on the trunk and covers all seven roles; the validate gate awaits the owner | rolled up from `c2ad` Roles |
| `77b2` | 2026-10-26 | The owner reviews validate in 96864ea and the checks of the figures and of the feel of arrival and of a page pass; on a person's own plan of 67 tasks with 14 subprojects tablotui loads at arrival in 467 ms and with four panes in 558 ms and tableaud serves its first page in 1343 ms and the next five in 668 ms, over A8's 100 ms bound as at the baseline, and this task and the derivation task cite that one reload cost | `b2c1` tablo in `subprojects/tablo` at `e35657e`, at 🌍 validate |
| `6103` | 2026-10-23 | The owner accepted validate in fb9fd65 on the checks e3ed.1 to e3ed.3 of the validate checklist. TABLEAUX.md on GitHub equals tableau --level glance on a clone at main (EQUAL after the pull to 77e8bdf), it reads well on GitHub, and a task page reads well in the Preview tab of a comment box. The field tests found the two equal at 4069962 and the gate and task views rendering at detail with exit 0. | `07e0` tabloio in `subprojects/tabloio` at `29bd9d7`, at 🌍 validate |
| `c6e8` | 2026-10-28 | Accepted by the owner at validate in abbfb12. All 28 checks of the checklist pass. The owner's terminal of daily use answers the mode 2027 query not recognised (679b.1) and screen gives no reply (679b.3), so the tableau aligns by code point with U+FE0F stripped, as decision 21 records. The field tests give six runs of the suites with no failure at be0c129 (830 pass and 38 skip plain, 900 and 14 with a corpus, 854 and 34 with the umbrella), a start on two plans under a pseudo-terminal, no hue set by the program and a clean quit. | `40e8` tablotui in `subprojects/tablotui` at `95e20c2`, at 🌍 validate |
| `595e` | 2026-10-28 | The owner reviewed the validate in 1fff1df and every check the owner ran passes, from walking the ten views of the daemon on the tooling plan to the content policy, the polling 304s, the boosted swap, the absolute-URL requirements of tabloio's plan and the Host check. Field tests 1 to 3, 8 and 9 stand, so the suites pass, 360 pages answer 200, a refresh shows in about 90 ms and the wait on absolute URLs has ended. The check of the folds a refresh keeps first failed and passes on 90cb731 after decision 23 of this design. | `8608` tableaud in `subprojects/tableaud` at `595fe06`, at 🌍 validate |

Command: `tabloio tableau --ref main --window 1 --level glance`

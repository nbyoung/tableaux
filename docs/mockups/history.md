# History

What happened, when, and who did it? This file draws the history view of the Tableaux tooling plan on `main` at `3cdae52`, 2026-10-05, for the viewer nbyoung@nbyoung.com, the owner, who reads as a reviewer. It draws two pictures, the life of one task and the range a reviewer reads since the last review, and each picture at the three levels that `--level` fixes: glance, detail, provenance.

| Parameter | Picture 1 | Picture 2 |
|---|---|---|
| task | `e9c6` Abstract views | `437e` Tableaux tooling, the root |
| ref, or a range | `main` at `3cdae52`, no range | `0704a09..main`, `main` at `3cdae52` |
| person | not set: every actor | not set: every actor |
| level | each of the three, in turn | each of the three, in turn |

Both pictures run oldest first. The status after each event is a replay, so each line builds on the one above it, and a reviewer starts where the last review ends. VIEWS.md and SYNTAX.md write their examples in the same order.

One line holds the events one commit makes on one task, so a commit that both records a status and carries its `Reviewed:` trailer reads `status, reviewed`. The counts above each list still count events.

Gates: ❔ undefined, 📝 defined, 🔧 function, 📐 design. States: ⚪ undefined, 🟢 nominal. Reason: 👓 review, the hand-off to the reviewer. Each symbol comes from `.tableaux/gates.yaml`; the [gate definition](gates.md) explains every one. An event kind has no symbol.

## Picture 1. One task: `e9c6` Abstract views

The whole life of `e9c6` Abstract views up to the ref. Parameters: task `e9c6`; ref `main` at `3cdae52`, with no range; person not set, so every actor.

### Glance

8 events in 7 commits, 2026-09-29 to 2026-09-30: 1 task, 1 authorised, 4 status, 0 reaffirmed, 2 reviewed, 0 pin.

| Date | By | Event | Task | Gate and state |
|---|---|---|---|---|
| 2026-09-29 | nbyoung@nbyoung.com | task, authorised | `e9c6` | the task file appears |
| 2026-09-29 | noreply@anthropic.com | status | `e9c6` | 📝 defined 🟢 nominal |
| 2026-09-29 | noreply@anthropic.com | reviewed | `e9c6` | 📝 defined |
| 2026-09-30 | noreply@anthropic.com | status | `e9c6` | 📝 defined 🟢 nominal 👓 review |
| 2026-09-30 | noreply@anthropic.com | status | `e9c6` | 📝 defined 🟢 nominal 👓 review |
| 2026-09-30 | nbyoung@nbyoung.com | reviewed | `e9c6` | 📐 design |
| 2026-09-30 | noreply@anthropic.com | status | `e9c6` | 📐 design 🟢 nominal |

Command: `tabloio history --task e9c6 --ref main --level glance`

### Detail

8 events in 7 commits, 2026-09-29 to 2026-09-30: 1 task, 1 authorised, 4 status, 0 reaffirmed, 2 reviewed, 0 pin.

#### 2026-09-29 · 4 events in 3 commits: 1 task, 1 authorised, 1 status, 1 reviewed

- **2026-09-29** · nbyoung@nbyoung.com · task, authorised · `e9c6` · the task file appears
  - Status after: ❔ undefined ⚪ undefined: a leaf with no status file
  - Effect: authorised: the owner, an authority of `e9c6`, authors the commit on the trunk, so the commit proposes and accepts at once
  - Model: none recorded: the commit precedes the `Model:` trailer, which language 0.2.1 introduces; `Co-Authored-By:` names Claude Fable 5.1
- **2026-09-29** · noreply@anthropic.com · status · `e9c6` · 📝 defined 🟢 nominal
  - Status after: 📝 defined 🟢 nominal
  - Note: Design waits for Roles (c2ad) at design
  - Model: none recorded: the commit precedes the `Model:` trailer, which language 0.2.1 introduces; `Co-Authored-By:` names Claude Fable 5.1
  - Committer: nbyoung@nbyoung.com, who differs from the author
- **2026-09-29** · noreply@anthropic.com · reviewed · `e9c6` · 📝 defined
  - Status after: 📝 defined 🟢 nominal, unchanged
  - Effect: none: the authorisation stands as the review of `defined`, so the trailer adds nothing
  - Model: none recorded: the commit precedes the `Model:` trailer, which language 0.2.1 introduces; `Co-Authored-By:` names Claude Fable 5.1
  - Committer: nbyoung@nbyoung.com, who differs from the author

#### 2026-09-30 · 4 events in 4 commits: 3 status, 1 reviewed

- **2026-09-30** · noreply@anthropic.com · status · `e9c6` · 📝 defined 🟢 nominal 👓 review
  - Status after: 📝 defined 🟢 nominal 👓 review
  - Note: The VIEWS.md design on branch worktree-agent-a6b84238bbacc4fcd awaits the owner's review at the design gate
  - Effect: the hand-off: the work at `design` waits for its reviewer, nbyoung@nbyoung.com, and the [work queue](queue.md) lists the review as owed
  - Model: `claude-fable-5-1`; the `design` junction states `claude-fable`
- **2026-09-30** · noreply@anthropic.com · status · `e9c6` · 📝 defined 🟢 nominal 👓 review
  - Status after: 📝 defined 🟢 nominal 👓 review
  - Note: The revised VIEWS.md design on branch worktree-agent-a6b84238bbacc4fcd awaits the owner's acceptance at the design gate
  - Effect: the hand-off again, after the revision the first review asks for
  - Model: `claude-fable-5-1`; the `design` junction states `claude-fable`
- **2026-09-30** · nbyoung@nbyoung.com · reviewed · `e9c6` · 📐 design
  - Status after: 📝 defined 🟢 nominal 👓 review, unchanged until the next event
  - Effect: the reviewer the `design` junction names accepts the work, so the status may pass `design`
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
- **2026-09-30** · noreply@anthropic.com · status · `e9c6` · 📐 design 🟢 nominal
  - Status after: 📐 design 🟢 nominal
  - Note: VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place
  - Model: `claude-fable-5-1`; the `design` junction states `claude-fable`

Command: `tabloio history --task e9c6 --ref main --level detail`

### Provenance

8 events in 7 commits, 2026-09-29 to 2026-09-30: 1 task, 1 authorised, 4 status, 0 reaffirmed, 2 reviewed, 0 pin.

#### 2026-09-29 · 4 events in 3 commits: 1 task, 1 authorised, 1 status, 1 reviewed

- **2026-09-29** · nbyoung@nbyoung.com · task, authorised · `e9c6` · the task file appears
  - Status after: ❔ undefined ⚪ undefined: a leaf with no status file
  - Effect: authorised: the owner, an authority of `e9c6`, authors the commit on the trunk, so the commit proposes and accepts at once
  - Model: none recorded: the commit precedes the `Model:` trailer, which language 0.2.1 introduces; `Co-Authored-By:` names Claude Fable 5.1
  - Commit: `6b6c99a2ca35f684674ad886a33916979137f227`
  - Subject: Plan the Tableaux tooling
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 16:38:16 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 16:38:16 -0400
  - Trailers: `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
  - Files: `.tableaux/tasks/e9c6.yaml` (added) and 39 more
  - Reproduce:
    - `git log --format='%as %h %ae' -- .tableaux/tasks/e9c6.yaml .tableaux/status/e9c6.yaml`
- **2026-09-29** · noreply@anthropic.com · status · `e9c6` · 📝 defined 🟢 nominal
  - Status after: 📝 defined 🟢 nominal
  - Note: Design waits for Roles (c2ad) at design
  - Model: none recorded: the commit precedes the `Model:` trailer, which language 0.2.1 introduces; `Co-Authored-By:` names Claude Fable 5.1
  - Committer: nbyoung@nbyoung.com, who differs from the author
  - Commit: `1a17bfcca843d4436e2eb4c75b5cfa98ec05d658`
  - Subject: Record the defined gate for the views and mockups
  - Author: Claude Fable 5.1 <noreply@anthropic.com>, 2026-09-29 17:46:53 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 17:46:53 -0400
  - Trailers: `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
  - Files: `.tableaux/status/e9c6.yaml` (added) and 20 more
  - Reproduce:
    - `git log --format='%as %h %ae' -- .tableaux/tasks/e9c6.yaml .tableaux/status/e9c6.yaml`
    - `git show 1a17bfc:.tableaux/status/e9c6.yaml`
- **2026-09-29** · noreply@anthropic.com · reviewed · `e9c6` · 📝 defined
  - Status after: 📝 defined 🟢 nominal, unchanged
  - Effect: none: the authorisation stands as the review of `defined`, so the trailer adds nothing
  - Model: none recorded: the commit precedes the `Model:` trailer, which language 0.2.1 introduces; `Co-Authored-By:` names Claude Fable 5.1
  - Committer: nbyoung@nbyoung.com, who differs from the author
  - Commit: `5958858ff25a624aea18f26471f95b92616fc7e6`
  - Subject: Accept the defined gate of the views and mockups
  - Author: Claude Fable 5.1 <noreply@anthropic.com>, 2026-09-29 18:01:32 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 18:01:32 -0400
  - Trailers: `Reviewed: e9c6 defined` and 20 more `Reviewed:` trailers, `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
  - Files: none: an empty commit; the trailer makes the event
  - Reproduce:
    - `git log --format='%as %h %ae' -E --grep='^(Authorised|Reaffirmed): e9c6$' --grep='^Reviewed: e9c6 '`

#### 2026-09-30 · 4 events in 4 commits: 3 status, 1 reviewed

- **2026-09-30** · noreply@anthropic.com · status · `e9c6` · 📝 defined 🟢 nominal 👓 review
  - Status after: 📝 defined 🟢 nominal 👓 review
  - Note: The VIEWS.md design on branch worktree-agent-a6b84238bbacc4fcd awaits the owner's review at the design gate
  - Effect: the hand-off: the work at `design` waits for its reviewer, nbyoung@nbyoung.com, and the [work queue](queue.md) lists the review as owed
  - Model: `claude-fable-5-1`; the `design` junction states `claude-fable`
  - Commit: `0fed913a401606e7d6d2bbee72385f2c56204231`
  - Subject: Mark the abstract views design as awaiting review
  - Author: Claude Fable 5.1 <noreply@anthropic.com>, 2026-09-30 07:43:32 -0400
  - Committer: Claude Fable 5.1 <noreply@anthropic.com>, 2026-09-30 07:43:32 -0400
  - Trailers: `Model: claude-fable-5-1`, `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
  - Files: `.tableaux/status/e9c6.yaml` (changed)
  - Reproduce:
    - `git log --format='%as %h %ae' -- .tableaux/tasks/e9c6.yaml .tableaux/status/e9c6.yaml`
    - `git show 0fed913:.tableaux/status/e9c6.yaml`
- **2026-09-30** · noreply@anthropic.com · status · `e9c6` · 📝 defined 🟢 nominal 👓 review
  - Status after: 📝 defined 🟢 nominal 👓 review
  - Note: The revised VIEWS.md design on branch worktree-agent-a6b84238bbacc4fcd awaits the owner's acceptance at the design gate
  - Effect: the hand-off again, after the revision the first review asks for
  - Model: `claude-fable-5-1`; the `design` junction states `claude-fable`
  - Commit: `26defc75c452b21dcd9c86d4a2bfa71b685e52a3`
  - Subject: Mark the revised abstract views design as awaiting acceptance
  - Author: Claude Fable 5.1 <noreply@anthropic.com>, 2026-09-30 15:12:04 -0400
  - Committer: Claude Fable 5.1 <noreply@anthropic.com>, 2026-09-30 15:12:04 -0400
  - Trailers: `Model: claude-fable-5-1`, `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
  - Files: `.tableaux/status/e9c6.yaml` (changed)
  - Reproduce:
    - `git log --format='%as %h %ae' -- .tableaux/tasks/e9c6.yaml .tableaux/status/e9c6.yaml`
    - `git show 26defc7:.tableaux/status/e9c6.yaml`
- **2026-09-30** · nbyoung@nbyoung.com · reviewed · `e9c6` · 📐 design
  - Status after: 📝 defined 🟢 nominal 👓 review, unchanged until the next event
  - Effect: the reviewer the `design` junction names accepts the work, so the status may pass `design`
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Commit: `0704a0912297b3de0218b821384cf1b9956a44bb`
  - Subject: Accept the abstract views design
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-09-30 15:16:33 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-09-30 15:16:33 -0400
  - Trailers: `Reviewed: e9c6 design`, `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: none of its own: a merge of `26defc7` into `1b6916e`; the trailer makes the event
  - Reproduce:
    - `git log --format='%as %h %ae' -E --grep='^(Authorised|Reaffirmed): e9c6$' --grep='^Reviewed: e9c6 '`
- **2026-09-30** · noreply@anthropic.com · status · `e9c6` · 📐 design 🟢 nominal
  - Status after: 📐 design 🟢 nominal
  - Note: VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place
  - Model: `claude-fable-5-1`; the `design` junction states `claude-fable`
  - Commit: `879b447a920aad55e698906812350ea7d3785b4c`
  - Subject: Advance the abstract views task to its design gate
  - Author: Claude Fable 5.1 <noreply@anthropic.com>, 2026-09-30 15:17:53 -0400
  - Committer: Claude Fable 5.1 <noreply@anthropic.com>, 2026-09-30 15:17:53 -0400
  - Trailers: `Model: claude-fable-5-1`, `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
  - Files: `.tableaux/status/e9c6.yaml` (changed)
  - Reproduce:
    - `git log --format='%as %h %ae' -- .tableaux/tasks/e9c6.yaml .tableaux/status/e9c6.yaml`
    - `git show 879b447:.tableaux/status/e9c6.yaml`

The two commands that produce the list; the tool merges their output in author-time order:

```
git log --format='%as %h %ae' -- .tableaux/tasks/e9c6.yaml .tableaux/status/e9c6.yaml
git log --format='%as %h %ae' -E --grep='^(Authorised|Reaffirmed): e9c6$' --grep='^Reviewed: e9c6 '
```

Command: `tabloio history --task e9c6 --ref main --level provenance`

## Picture 2. A range: the project since the last review

What a reviewer reads as "what changed since my last review". The range starts after `0704a09`, the newest `Reviewed:` commit of nbyoung@nbyoung.com, which accepts `e9c6` at `design`. Parameters: task `437e` Tableaux tooling, the root, so the range replays every task; range `0704a09..main`, with `main` at `3cdae52`; person not set, so every actor. Three of the four function-prototype waves fall in the range: tabloio (`55e32e3`), tablotui (`fa4551e`) and tableaud (`3cdae52`). The tablo wave (`564c7cb`, 2026-09-30) precedes the last review, so the range leaves it out.

### Glance

13 events in 7 commits, 2026-09-30 to 2026-10-05: 0 task, 0 authorised, 1 status, 0 reaffirmed, 0 reviewed, 12 pin.

| Day | Events | Commits | Kinds |
|---|---|---|---|
| 2026-09-30 | 1 | 1 | 1 status |
| 2026-10-02 | 10 | 4 | 10 pin |
| 2026-10-04 | 1 | 1 | 1 pin |
| 2026-10-05 | 1 | 1 | 1 pin |

The day table is the fold: a range too long to list event by event keeps the day table and folds the lines below it by day. This range lists every line.

| Date | By | Event | Task | Gate and state, or `url` and commits |
|---|---|---|---|---|
| 2026-09-30 | noreply@anthropic.com | status | `e9c6` | 📐 design 🟢 nominal |
| 2026-10-02 | nbyoung@nbyoung.com | pin | `6103` | `subprojects/tabloio` `62261d4` → `7eba1e5` |
| 2026-10-02 | nbyoung@nbyoung.com | pin | `77b2` | `subprojects/tablo` `7e94d58` → `816f2a0` |
| 2026-10-02 | nbyoung@nbyoung.com | pin | `6103` | `subprojects/tabloio` `7eba1e5` → `581ae98` |
| 2026-10-02 | nbyoung@nbyoung.com | pin | `c6e8` | `subprojects/tablotui` `159fdab` → `dbfb8e3` |
| 2026-10-02 | nbyoung@nbyoung.com | pin | `595e` | `subprojects/tableaud` `2061a7f` → `b06cad0` |
| 2026-10-02 | nbyoung@nbyoung.com | pin | `77b2` | `subprojects/tablo` `816f2a0` → `00f8f68` |
| 2026-10-02 | nbyoung@nbyoung.com | pin | `6103` | `subprojects/tabloio` `581ae98` → `cb9ff8f` |
| 2026-10-02 | nbyoung@nbyoung.com | pin | `c6e8` | `subprojects/tablotui` `dbfb8e3` → `334df71` |
| 2026-10-02 | nbyoung@nbyoung.com | pin | `595e` | `subprojects/tableaud` `b06cad0` → `cffbfa6` |
| 2026-10-02 | nbyoung@nbyoung.com | pin | `6103` | `subprojects/tabloio` `cb9ff8f` → `4593882` |
| 2026-10-04 | nbyoung@nbyoung.com | pin | `c6e8` | `subprojects/tablotui` `334df71` → `a2878b5` |
| 2026-10-05 | nbyoung@nbyoung.com | pin | `595e` | `subprojects/tableaud` `cffbfa6` → `e6ec4ec` |

Command: `tabloio history --ref 0704a09..main --level glance`

### Detail

13 events in 7 commits, 2026-09-30 to 2026-10-05: 0 task, 0 authorised, 1 status, 0 reaffirmed, 0 reviewed, 12 pin.

#### 2026-09-30 · 1 event in 1 commit: 1 status

- **2026-09-30** · noreply@anthropic.com · status · `e9c6` · 📐 design 🟢 nominal
  - Status after: 📐 design 🟢 nominal
  - Note: VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place
  - Project `437e` after: 📝 defined 🟢 nominal, rolled up from `99f0` Gate definition view in Markdown: "Mockup waits for Abstract views (e9c6) at design"; before this event it rolls up from `e9c6` with 👓 review
  - Model: `claude-fable-5-1`; the `design` junction states `claude-fable`

#### 2026-10-02 · 10 events in 4 commits: 10 pin

- **2026-10-02** · nbyoung@nbyoung.com · pin · `6103` · `subprojects/tabloio` `62261d4` → `7eba1e5`
  - Status after: 📝 defined 🟢 nominal; the gate comes from the status file of `6103`; the state and the note come from tabloio's root `07e0` at `7eba1e5`, which stands at 📝 defined and rolls up from `1422` Snapshot workflow
  - Note: The design is next and no requirement gates it
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: 16 events in 8 commits of tabloio between `62261d4` and `7eba1e5`; `tabloio -C subprojects/tabloio history --ref 62261d4..7eba1e5` gives their detail
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `a3cc` Status renderers · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `c48a` Structural renderers · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `9167` Temporal renderers · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `e0f7` Text renderers · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `b618` Write commands · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `e3ed` Legend and task renderers · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `e4c7` Agent briefs · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `5ca9` Read commands · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
- **2026-10-02** · nbyoung@nbyoung.com · pin · `77b2` · `subprojects/tablo` `7e94d58` → `816f2a0`
  - Status after: 📝 defined 🟢 nominal, unchanged; tablo's root `b2c1` reads the same at `816f2a0` as at `7e94d58`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tablo between `7e94d58` and `816f2a0`: its 2 commits change no task and no status
- **2026-10-02** · nbyoung@nbyoung.com · pin · `6103` · `subprojects/tabloio` `7eba1e5` → `581ae98`
  - Status after: 📝 defined 🟢 nominal, unchanged; tabloio's root `07e0` reads the same at `581ae98` as at `7eba1e5`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tabloio between `7eba1e5` and `581ae98`: its 2 commits change no task and no status
- **2026-10-02** · nbyoung@nbyoung.com · pin · `c6e8` · `subprojects/tablotui` `159fdab` → `dbfb8e3`
  - Status after: 📝 defined 🟢 nominal, unchanged; tablotui's root `40e8` reads the same at `dbfb8e3` as at `159fdab`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tablotui between `159fdab` and `dbfb8e3`: its 2 commits change no task and no status
- **2026-10-02** · nbyoung@nbyoung.com · pin · `595e` · `subprojects/tableaud` `2061a7f` → `b06cad0`
  - Status after: 📝 defined 🟢 nominal, unchanged; tableaud's root `8608` reads the same at `b06cad0` as at `2061a7f`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tableaud between `2061a7f` and `b06cad0`: its 2 commits change no task and no status
- **2026-10-02** · nbyoung@nbyoung.com · pin · `77b2` · `subprojects/tablo` `816f2a0` → `00f8f68`
  - Status after: 📝 defined 🟢 nominal, unchanged; tablo's root `b2c1` reads the same at `00f8f68` as at `816f2a0`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tablo between `816f2a0` and `00f8f68`: its 2 commits change no task and no status
- **2026-10-02** · nbyoung@nbyoung.com · pin · `6103` · `subprojects/tabloio` `581ae98` → `cb9ff8f`
  - Status after: 📝 defined 🟢 nominal, unchanged; tabloio's root `07e0` reads the same at `cb9ff8f` as at `581ae98`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tabloio between `581ae98` and `cb9ff8f`: its 2 commits change no task and no status
- **2026-10-02** · nbyoung@nbyoung.com · pin · `c6e8` · `subprojects/tablotui` `dbfb8e3` → `334df71`
  - Status after: 📝 defined 🟢 nominal, unchanged; tablotui's root `40e8` reads the same at `334df71` as at `dbfb8e3`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tablotui between `dbfb8e3` and `334df71`: its 2 commits change no task and no status
- **2026-10-02** · nbyoung@nbyoung.com · pin · `595e` · `subprojects/tableaud` `b06cad0` → `cffbfa6`
  - Status after: 📝 defined 🟢 nominal, unchanged; tableaud's root `8608` reads the same at `cffbfa6` as at `b06cad0`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tableaud between `b06cad0` and `cffbfa6`: its 2 commits change no task and no status
- **2026-10-02** · nbyoung@nbyoung.com · pin · `6103` · `subprojects/tabloio` `cb9ff8f` → `4593882`
  - Status after: 📝 defined 🟢 nominal; the gate comes from the status file of `6103`; the state and the note come from tabloio's root `07e0` at `4593882`, which stands at 🔧 function and rolls up from `e3ed` Legend and task renderers
  - Note: prototype/e3ed renders the gate and task definition views as Markdown at three levels from tablo view data
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: 3 events in 3 commits of tabloio between `cb9ff8f` and `4593882`; `tabloio -C subprojects/tabloio history --ref cb9ff8f..4593882` gives their detail
    - 2026-09-30 · noreply@anthropic.com · status · `1422` Snapshot workflow · 📝 defined 🟢 nominal 👓 review · `claude-opus-5-5`
    - 2026-10-02 · nbyoung@nbyoung.com · reviewed · `1422` Snapshot workflow · 📐 design · `claude-opus-5-5`
    - 2026-10-02 · noreply@anthropic.com · status · `1422` Snapshot workflow · 📐 design 🟢 nominal · `claude-opus-5-5`

#### 2026-10-04 · 1 event in 1 commit: 1 pin

- **2026-10-04** · nbyoung@nbyoung.com · pin · `c6e8` · `subprojects/tablotui` `334df71` → `a2878b5`
  - Status after: 📝 defined 🟢 nominal; the gate comes from the status file of `c6e8`; the state and the note come from tablotui's root `40e8` at `a2878b5`, which stands at 🔧 function and rolls up from `679b` Tableau grid
  - Note: prototype/679b renders the global tableau as a Bubble Tea grid with tree expand and collapse, scrolling, a folded gate window and hidden columns kept in a settings file; emoji lines align where the terminal widens U+FE0F
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: 10 events in 5 commits of tablotui between `334df71` and `a2878b5`; `tabloio -C subprojects/tablotui history --ref 334df71..a2878b5` gives their detail
    - 2026-10-02 · noreply@anthropic.com · status, reviewed · `518e` Actions · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-02 · noreply@anthropic.com · status, reviewed · `f394` Role and context · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-02 · noreply@anthropic.com · status, reviewed · `679b` Tableau grid · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-02 · noreply@anthropic.com · status, reviewed · `171b` Live refresh · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-02 · noreply@anthropic.com · status, reviewed · `0afa` Detail panes · 🔧 function 🟢 nominal · `claude-sonnet-5-5`

#### 2026-10-05 · 1 event in 1 commit: 1 pin

- **2026-10-05** · nbyoung@nbyoung.com · pin · `595e` · `subprojects/tableaud` `cffbfa6` → `e6ec4ec`
  - Status after: 📝 defined 🟢 nominal; the gate comes from the status file of `595e`; the state and the note come from tableaud's root `8608` at `e6ec4ec`, which stands at 🔧 function and rolls up from `49ce` Server
  - Note: prototype/49ce serves the ten views with a stdlib HEAD and .tableaux watcher, ETag 304 polling through htmx, a Source interface and a loopback Host check
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: 21 events in 13 commits of tableaud between `cffbfa6` and `e6ec4ec`; `tabloio -C subprojects/tableaud history --ref cffbfa6..e6ec4ec` gives their detail
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `9a9c` Temporal templates · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `44bf` Status templates · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · reviewed · `438a` Legend and task templates · 🔧 function · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `438a` Legend and task templates · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · reviewed · `e2b6` Structural templates · 🔧 function · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `e2b6` Structural templates · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · reviewed · `49ce` Server · 🔧 function · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `49ce` Server · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · reviewed · `db74` Progressive disclosure · 🔧 function · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `db74` Progressive disclosure · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · reviewed · `5a2f` Accessibility and theming · 🔧 function · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `5a2f` Accessibility and theming · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `6160` Static export · 🔧 function 🟢 nominal · `claude-sonnet-5-5`

Command: `tabloio history --ref 0704a09..main --level detail`

### Provenance

13 events in 7 commits, 2026-09-30 to 2026-10-05: 0 task, 0 authorised, 1 status, 0 reaffirmed, 0 reviewed, 12 pin.

#### 2026-09-30 · 1 event in 1 commit: 1 status

- **2026-09-30** · noreply@anthropic.com · status · `e9c6` · 📐 design 🟢 nominal
  - Status after: 📐 design 🟢 nominal
  - Note: VIEWS.md is on the trunk at language 0.3.1; the twenty mockups may start, and implementation puts the text in place
  - Project `437e` after: 📝 defined 🟢 nominal, rolled up from `99f0` Gate definition view in Markdown: "Mockup waits for Abstract views (e9c6) at design"; before this event it rolls up from `e9c6` with 👓 review
  - Model: `claude-fable-5-1`; the `design` junction states `claude-fable`
  - Commit: `879b447a920aad55e698906812350ea7d3785b4c`
  - Subject: Advance the abstract views task to its design gate
  - Author: Claude Fable 5.1 <noreply@anthropic.com>, 2026-09-30 15:17:53 -0400
  - Committer: Claude Fable 5.1 <noreply@anthropic.com>, 2026-09-30 15:17:53 -0400
  - Trailers: `Model: claude-fable-5-1`, `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
  - Files: `.tableaux/status/e9c6.yaml` (changed)
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/e9c6.yaml .tableaux/status/e9c6.yaml`
    - `git show 879b447:.tableaux/status/e9c6.yaml`

#### 2026-10-02 · 10 events in 4 commits: 10 pin

- **2026-10-02** · nbyoung@nbyoung.com · pin · `6103` · `subprojects/tabloio` `62261d4` → `7eba1e5`
  - Status after: 📝 defined 🟢 nominal; the gate comes from the status file of `6103`; the state and the note come from tabloio's root `07e0` at `7eba1e5`, which stands at 📝 defined and rolls up from `1422` Snapshot workflow
  - Note: The design is next and no requirement gates it
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: 16 events in 8 commits of tabloio between `62261d4` and `7eba1e5`; `tabloio -C subprojects/tabloio history --ref 62261d4..7eba1e5` gives their detail
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `a3cc` Status renderers · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `c48a` Structural renderers · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `9167` Temporal renderers · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `e0f7` Text renderers · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `b618` Write commands · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `e3ed` Legend and task renderers · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `e4c7` Agent briefs · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-09-30 · noreply@anthropic.com · status, reviewed · `5ca9` Read commands · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
  - Commit: `55e32e32d65e9cc04da707b215f4b9009a4806e6`
  - Subject: Advance tabloio to its function prototypes
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:07:09 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:07:09 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tabloio`, the submodule pin (`62261d4` → `7eba1e5`)
  - Subproject commits: `f3b3549` `7e3ea9a` `3ee2131` `00a8dec` `c5e6695` `90e66fc` `baab0e5` `92200e0`
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/6103.yaml .tableaux/status/6103.yaml subprojects/tabloio`
    - `git diff --raw --abbrev=7 55e32e3^ 55e32e3 -- subprojects/tabloio`
    - `git -C subprojects/tabloio log --format='%as %h %ae' 62261d4..7eba1e5 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tabloio log --format='%as %h %ae' 62261d4..7eba1e5 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-10-02** · nbyoung@nbyoung.com · pin · `77b2` · `subprojects/tablo` `7e94d58` → `816f2a0`
  - Status after: 📝 defined 🟢 nominal, unchanged; tablo's root `b2c1` reads the same at `816f2a0` as at `7e94d58`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tablo between `7e94d58` and `816f2a0`: its 2 commits change no task and no status
  - Commit: `fb8c0b2b527789760956b0a238c5f07b97c7f277`
  - Subject: Advance the subprojects to the eyeglasses review symbol
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:12:40 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:12:40 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tablo`, the submodule pin (`7e94d58` → `816f2a0`) and 3 more
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/77b2.yaml .tableaux/status/77b2.yaml subprojects/tablo`
    - `git diff --raw --abbrev=7 fb8c0b2^ fb8c0b2 -- subprojects/tablo`
    - `git -C subprojects/tablo log --format='%as %h %ae' 7e94d58..816f2a0 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tablo log --format='%as %h %ae' 7e94d58..816f2a0 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-10-02** · nbyoung@nbyoung.com · pin · `6103` · `subprojects/tabloio` `7eba1e5` → `581ae98`
  - Status after: 📝 defined 🟢 nominal, unchanged; tabloio's root `07e0` reads the same at `581ae98` as at `7eba1e5`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tabloio between `7eba1e5` and `581ae98`: its 2 commits change no task and no status
  - Commit: `fb8c0b2b527789760956b0a238c5f07b97c7f277`
  - Subject: Advance the subprojects to the eyeglasses review symbol
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:12:40 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:12:40 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tabloio`, the submodule pin (`7eba1e5` → `581ae98`) and 3 more
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/6103.yaml .tableaux/status/6103.yaml subprojects/tabloio`
    - `git diff --raw --abbrev=7 fb8c0b2^ fb8c0b2 -- subprojects/tabloio`
    - `git -C subprojects/tabloio log --format='%as %h %ae' 7eba1e5..581ae98 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tabloio log --format='%as %h %ae' 7eba1e5..581ae98 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-10-02** · nbyoung@nbyoung.com · pin · `c6e8` · `subprojects/tablotui` `159fdab` → `dbfb8e3`
  - Status after: 📝 defined 🟢 nominal, unchanged; tablotui's root `40e8` reads the same at `dbfb8e3` as at `159fdab`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tablotui between `159fdab` and `dbfb8e3`: its 2 commits change no task and no status
  - Commit: `fb8c0b2b527789760956b0a238c5f07b97c7f277`
  - Subject: Advance the subprojects to the eyeglasses review symbol
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:12:40 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:12:40 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tablotui`, the submodule pin (`159fdab` → `dbfb8e3`) and 3 more
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/c6e8.yaml .tableaux/status/c6e8.yaml subprojects/tablotui`
    - `git diff --raw --abbrev=7 fb8c0b2^ fb8c0b2 -- subprojects/tablotui`
    - `git -C subprojects/tablotui log --format='%as %h %ae' 159fdab..dbfb8e3 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tablotui log --format='%as %h %ae' 159fdab..dbfb8e3 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-10-02** · nbyoung@nbyoung.com · pin · `595e` · `subprojects/tableaud` `2061a7f` → `b06cad0`
  - Status after: 📝 defined 🟢 nominal, unchanged; tableaud's root `8608` reads the same at `b06cad0` as at `2061a7f`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tableaud between `2061a7f` and `b06cad0`: its 2 commits change no task and no status
  - Commit: `fb8c0b2b527789760956b0a238c5f07b97c7f277`
  - Subject: Advance the subprojects to the eyeglasses review symbol
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:12:40 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:12:40 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tableaud`, the submodule pin (`2061a7f` → `b06cad0`) and 3 more
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/595e.yaml .tableaux/status/595e.yaml subprojects/tableaud`
    - `git diff --raw --abbrev=7 fb8c0b2^ fb8c0b2 -- subprojects/tableaud`
    - `git -C subprojects/tableaud log --format='%as %h %ae' 2061a7f..b06cad0 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tableaud log --format='%as %h %ae' 2061a7f..b06cad0 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-10-02** · nbyoung@nbyoung.com · pin · `77b2` · `subprojects/tablo` `816f2a0` → `00f8f68`
  - Status after: 📝 defined 🟢 nominal, unchanged; tablo's root `b2c1` reads the same at `00f8f68` as at `816f2a0`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tablo between `816f2a0` and `00f8f68`: its 2 commits change no task and no status
  - Commit: `552d38fd8adf40e41b39f65d5904e6fc6a88b265`
  - Subject: Advance the subprojects to the wrench, brick, ruler and link gate symbols
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:34:57 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:34:57 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tablo`, the submodule pin (`816f2a0` → `00f8f68`) and 3 more
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/77b2.yaml .tableaux/status/77b2.yaml subprojects/tablo`
    - `git diff --raw --abbrev=7 552d38f^ 552d38f -- subprojects/tablo`
    - `git -C subprojects/tablo log --format='%as %h %ae' 816f2a0..00f8f68 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tablo log --format='%as %h %ae' 816f2a0..00f8f68 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-10-02** · nbyoung@nbyoung.com · pin · `6103` · `subprojects/tabloio` `581ae98` → `cb9ff8f`
  - Status after: 📝 defined 🟢 nominal, unchanged; tabloio's root `07e0` reads the same at `cb9ff8f` as at `581ae98`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tabloio between `581ae98` and `cb9ff8f`: its 2 commits change no task and no status
  - Commit: `552d38fd8adf40e41b39f65d5904e6fc6a88b265`
  - Subject: Advance the subprojects to the wrench, brick, ruler and link gate symbols
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:34:57 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:34:57 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tabloio`, the submodule pin (`581ae98` → `cb9ff8f`) and 3 more
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/6103.yaml .tableaux/status/6103.yaml subprojects/tabloio`
    - `git diff --raw --abbrev=7 552d38f^ 552d38f -- subprojects/tabloio`
    - `git -C subprojects/tabloio log --format='%as %h %ae' 581ae98..cb9ff8f -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tabloio log --format='%as %h %ae' 581ae98..cb9ff8f -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-10-02** · nbyoung@nbyoung.com · pin · `c6e8` · `subprojects/tablotui` `dbfb8e3` → `334df71`
  - Status after: 📝 defined 🟢 nominal, unchanged; tablotui's root `40e8` reads the same at `334df71` as at `dbfb8e3`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tablotui between `dbfb8e3` and `334df71`: its 2 commits change no task and no status
  - Commit: `552d38fd8adf40e41b39f65d5904e6fc6a88b265`
  - Subject: Advance the subprojects to the wrench, brick, ruler and link gate symbols
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:34:57 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:34:57 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tablotui`, the submodule pin (`dbfb8e3` → `334df71`) and 3 more
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/c6e8.yaml .tableaux/status/c6e8.yaml subprojects/tablotui`
    - `git diff --raw --abbrev=7 552d38f^ 552d38f -- subprojects/tablotui`
    - `git -C subprojects/tablotui log --format='%as %h %ae' dbfb8e3..334df71 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tablotui log --format='%as %h %ae' dbfb8e3..334df71 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-10-02** · nbyoung@nbyoung.com · pin · `595e` · `subprojects/tableaud` `b06cad0` → `cffbfa6`
  - Status after: 📝 defined 🟢 nominal, unchanged; tableaud's root `8608` reads the same at `cffbfa6` as at `b06cad0`
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: no event in tableaud between `b06cad0` and `cffbfa6`: its 2 commits change no task and no status
  - Commit: `552d38fd8adf40e41b39f65d5904e6fc6a88b265`
  - Subject: Advance the subprojects to the wrench, brick, ruler and link gate symbols
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:34:57 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 07:34:57 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tableaud`, the submodule pin (`b06cad0` → `cffbfa6`) and 3 more
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/595e.yaml .tableaux/status/595e.yaml subprojects/tableaud`
    - `git diff --raw --abbrev=7 552d38f^ 552d38f -- subprojects/tableaud`
    - `git -C subprojects/tableaud log --format='%as %h %ae' b06cad0..cffbfa6 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tableaud log --format='%as %h %ae' b06cad0..cffbfa6 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-10-02** · nbyoung@nbyoung.com · pin · `6103` · `subprojects/tabloio` `cb9ff8f` → `4593882`
  - Status after: 📝 defined 🟢 nominal; the gate comes from the status file of `6103`; the state and the note come from tabloio's root `07e0` at `4593882`, which stands at 🔧 function and rolls up from `e3ed` Legend and task renderers
  - Note: prototype/e3ed renders the gate and task definition views as Markdown at three levels from tablo view data
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: 3 events in 3 commits of tabloio between `cb9ff8f` and `4593882`; `tabloio -C subprojects/tabloio history --ref cb9ff8f..4593882` gives their detail
    - 2026-09-30 · noreply@anthropic.com · status · `1422` Snapshot workflow · 📝 defined 🟢 nominal 👓 review · `claude-opus-5-5`
    - 2026-10-02 · nbyoung@nbyoung.com · reviewed · `1422` Snapshot workflow · 📐 design · `claude-opus-5-5`
    - 2026-10-02 · noreply@anthropic.com · status · `1422` Snapshot workflow · 📐 design 🟢 nominal · `claude-opus-5-5`
  - Commit: `1c0f04daa18af8b4140e8eab2948466981b65010`
  - Subject: Advance tabloio to its snapshot workflow design
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 13:48:21 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-02 13:48:21 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tabloio`, the submodule pin (`cb9ff8f` → `4593882`)
  - Subproject commits: `c2ba78e` `2b58033` `2b911fd`
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/6103.yaml .tableaux/status/6103.yaml subprojects/tabloio`
    - `git diff --raw --abbrev=7 1c0f04d^ 1c0f04d -- subprojects/tabloio`
    - `git -C subprojects/tabloio log --format='%as %h %ae' cb9ff8f..4593882 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tabloio log --format='%as %h %ae' cb9ff8f..4593882 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`

#### 2026-10-04 · 1 event in 1 commit: 1 pin

- **2026-10-04** · nbyoung@nbyoung.com · pin · `c6e8` · `subprojects/tablotui` `334df71` → `a2878b5`
  - Status after: 📝 defined 🟢 nominal; the gate comes from the status file of `c6e8`; the state and the note come from tablotui's root `40e8` at `a2878b5`, which stands at 🔧 function and rolls up from `679b` Tableau grid
  - Note: prototype/679b renders the global tableau as a Bubble Tea grid with tree expand and collapse, scrolling, a folded gate window and hidden columns kept in a settings file; emoji lines align where the terminal widens U+FE0F
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: 10 events in 5 commits of tablotui between `334df71` and `a2878b5`; `tabloio -C subprojects/tablotui history --ref 334df71..a2878b5` gives their detail
    - 2026-10-02 · noreply@anthropic.com · status, reviewed · `518e` Actions · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-02 · noreply@anthropic.com · status, reviewed · `f394` Role and context · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-02 · noreply@anthropic.com · status, reviewed · `679b` Tableau grid · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-02 · noreply@anthropic.com · status, reviewed · `171b` Live refresh · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-02 · noreply@anthropic.com · status, reviewed · `0afa` Detail panes · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
  - Commit: `fa4551ecdc8d106722ac41b25a9213abc453fab0`
  - Subject: Advance tablotui to its five function prototypes
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-04 16:38:02 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-04 16:38:02 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tablotui`, the submodule pin (`334df71` → `a2878b5`)
  - Subproject commits: `ff14d4e` `358c6e3` `66c0412` `8fe12c3` `97991e8`
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/c6e8.yaml .tableaux/status/c6e8.yaml subprojects/tablotui`
    - `git diff --raw --abbrev=7 fa4551e^ fa4551e -- subprojects/tablotui`
    - `git -C subprojects/tablotui log --format='%as %h %ae' 334df71..a2878b5 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tablotui log --format='%as %h %ae' 334df71..a2878b5 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`

#### 2026-10-05 · 1 event in 1 commit: 1 pin

- **2026-10-05** · nbyoung@nbyoung.com · pin · `595e` · `subprojects/tableaud` `cffbfa6` → `e6ec4ec`
  - Status after: 📝 defined 🟢 nominal; the gate comes from the status file of `595e`; the state and the note come from tableaud's root `8608` at `e6ec4ec`, which stands at 🔧 function and rolls up from `49ce` Server
  - Note: prototype/49ce serves the ten views with a stdlib HEAD and .tableaux watcher, ETag 304 polling through htmx, a Source interface and a loopback Host check
  - Project `437e` after: unchanged
  - Model: `claude-opus-5-5`, an agent that commits under the identity of nbyoung@nbyoung.com
  - Subproject events: 21 events in 13 commits of tableaud between `cffbfa6` and `e6ec4ec`; `tabloio -C subprojects/tableaud history --ref cffbfa6..e6ec4ec` gives their detail
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `9a9c` Temporal templates · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `44bf` Status templates · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · reviewed · `438a` Legend and task templates · 🔧 function · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `438a` Legend and task templates · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · reviewed · `e2b6` Structural templates · 🔧 function · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `e2b6` Structural templates · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · reviewed · `49ce` Server · 🔧 function · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `49ce` Server · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · reviewed · `db74` Progressive disclosure · 🔧 function · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `db74` Progressive disclosure · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · reviewed · `5a2f` Accessibility and theming · 🔧 function · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `5a2f` Accessibility and theming · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
    - 2026-10-05 · noreply@anthropic.com · status, reviewed · `6160` Static export · 🔧 function 🟢 nominal · `claude-sonnet-5-5`
  - Commit: `3cdae527d47d37fdff55bc302c76c017cf91c606`
  - Subject: Advance tableaud to the eight function prototypes
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-10-05 12:59:45 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-10-05 12:59:45 -0400
  - Trailers: `Model: claude-opus-5-5`, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - Files: `subprojects/tableaud`, the submodule pin (`cffbfa6` → `e6ec4ec`)
  - Subproject commits: `1a3f5a2` `4320f45` `af1ec77` `11ab533` `7c98883` `2f2304c` `7d33060` `967df1f` `d3fa0f8` `0a2a0b6` `9e08551` `0c38023` `218d8f3`
  - Reproduce:
    - `git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks/595e.yaml .tableaux/status/595e.yaml subprojects/tableaud`
    - `git diff --raw --abbrev=7 3cdae52^ 3cdae52 -- subprojects/tableaud`
    - `git -C subprojects/tableaud log --format='%as %h %ae' cffbfa6..e6ec4ec -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tableaud log --format='%as %h %ae' cffbfa6..e6ec4ec -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`

The two commands that produce the list; the tool merges their output in author-time order. The four submodule paths join the first command, since a pin moves a gitlink and no task file:

```
git log --format='%as %h %ae' 0704a09..main -- .tableaux/tasks .tableaux/status subprojects/tablo subprojects/tabloio subprojects/tablotui subprojects/tableaud
git log --format='%as %h %ae' 0704a09..main -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '
```

The range holds 10 commits. 3 make no event, since they change no task file, no status file and no pin, and carry no task trailer: `57462c1` Advance the abstract views task to its design gate; `e91ba68` Mark four gates with symbols that need no variation selector; `767792c` Accept the wrench, brick, ruler and link gate symbols.

Command: `tabloio history --ref 0704a09..main --level provenance`

## Cases outside the two pictures

### A pin with no old commit

Every pin in picture 2 advances a pin, so each names an old and a new commit. A linkage first appears once per subproject, in `37a08e9` Pin the subprojects, which lies before the range. The glance of `tabloio history --ref a7932ae..37a08e9` shows that case, real project content:

4 events in 1 commit, 2026-09-29: 0 task, 0 authorised, 0 status, 0 reaffirmed, 0 reviewed, 4 pin.

| Date | By | Event | Task | `url` and commits |
|---|---|---|---|---|
| 2026-09-29 | nbyoung@nbyoung.com | pin | `77b2` | `subprojects/tablo` new `dc669dd`, no old commit |
| 2026-09-29 | nbyoung@nbyoung.com | pin | `6103` | `subprojects/tabloio` new `46521bc`, no old commit |
| 2026-09-29 | nbyoung@nbyoung.com | pin | `c6e8` | `subprojects/tablotui` new `4544042`, no old commit |
| 2026-09-29 | nbyoung@nbyoung.com | pin | `595e` | `subprojects/tableaud` new `59783a9`, no old commit |

At provenance, which holds the detail, they read:

- **2026-09-29** · nbyoung@nbyoung.com · pin · `77b2` · `subprojects/tablo` new `dc669dd`, no old commit
  - Status after: ❔ undefined ⚪ undefined; `77b2` has no status file yet; tablo's root `b2c1` at `dc669dd` stands at ❔ undefined ⚪ undefined
  - Model: none recorded: the commit precedes the `Model:` trailer, which language 0.2.1 introduces; `Co-Authored-By:` names Claude Fable 5.1
  - Subproject events: 12 events in 1 commit of tablo up to `dc669dd`, folded to the count; `tabloio -C subprojects/tablo history --ref dc669dd` gives their detail
  - Commit: `37a08e92e840ea3cb48bc7ca6a5041c44096ef8e`
  - Subject: Pin the subprojects
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 17:30:02 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 17:30:02 -0400
  - Trailers: `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
  - Files: `subprojects/tablo`, the submodule pin (new at `dc669dd`) and 4 more
  - Reproduce:
    - `git log --format='%as %h %ae' a7932ae..37a08e9 -- .tableaux/tasks/77b2.yaml .tableaux/status/77b2.yaml subprojects/tablo`
    - `git diff --raw --abbrev=7 37a08e9^ 37a08e9 -- subprojects/tablo`
    - `git -C subprojects/tablo log --format='%as %h %ae' dc669dd -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tablo log --format='%as %h %ae' dc669dd -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-09-29** · nbyoung@nbyoung.com · pin · `6103` · `subprojects/tabloio` new `46521bc`, no old commit
  - Status after: ❔ undefined ⚪ undefined; `6103` has no status file yet; tabloio's root `07e0` at `46521bc` stands at ❔ undefined ⚪ undefined
  - Model: none recorded: the commit precedes the `Model:` trailer, which language 0.2.1 introduces; `Co-Authored-By:` names Claude Fable 5.1
  - Subproject events: 12 events in 1 commit of tabloio up to `46521bc`, folded to the count; `tabloio -C subprojects/tabloio history --ref 46521bc` gives their detail
  - Commit: `37a08e92e840ea3cb48bc7ca6a5041c44096ef8e`
  - Subject: Pin the subprojects
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 17:30:02 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 17:30:02 -0400
  - Trailers: `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
  - Files: `subprojects/tabloio`, the submodule pin (new at `46521bc`) and 4 more
  - Reproduce:
    - `git log --format='%as %h %ae' a7932ae..37a08e9 -- .tableaux/tasks/6103.yaml .tableaux/status/6103.yaml subprojects/tabloio`
    - `git diff --raw --abbrev=7 37a08e9^ 37a08e9 -- subprojects/tabloio`
    - `git -C subprojects/tabloio log --format='%as %h %ae' 46521bc -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tabloio log --format='%as %h %ae' 46521bc -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-09-29** · nbyoung@nbyoung.com · pin · `c6e8` · `subprojects/tablotui` new `4544042`, no old commit
  - Status after: ❔ undefined ⚪ undefined; `c6e8` has no status file yet; tablotui's root `40e8` at `4544042` stands at ❔ undefined ⚪ undefined
  - Model: none recorded: the commit precedes the `Model:` trailer, which language 0.2.1 introduces; `Co-Authored-By:` names Claude Fable 5.1
  - Subproject events: 7 events in 1 commit of tablotui up to `4544042`, folded to the count; `tabloio -C subprojects/tablotui history --ref 4544042` gives their detail
  - Commit: `37a08e92e840ea3cb48bc7ca6a5041c44096ef8e`
  - Subject: Pin the subprojects
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 17:30:02 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 17:30:02 -0400
  - Trailers: `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
  - Files: `subprojects/tablotui`, the submodule pin (new at `4544042`) and 4 more
  - Reproduce:
    - `git log --format='%as %h %ae' a7932ae..37a08e9 -- .tableaux/tasks/c6e8.yaml .tableaux/status/c6e8.yaml subprojects/tablotui`
    - `git diff --raw --abbrev=7 37a08e9^ 37a08e9 -- subprojects/tablotui`
    - `git -C subprojects/tablotui log --format='%as %h %ae' 4544042 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tablotui log --format='%as %h %ae' 4544042 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`
- **2026-09-29** · nbyoung@nbyoung.com · pin · `595e` · `subprojects/tableaud` new `59783a9`, no old commit
  - Status after: ❔ undefined ⚪ undefined; `595e` has no status file yet; tableaud's root `8608` at `59783a9` stands at ❔ undefined ⚪ undefined
  - Model: none recorded: the commit precedes the `Model:` trailer, which language 0.2.1 introduces; `Co-Authored-By:` names Claude Fable 5.1
  - Subproject events: 11 events in 1 commit of tableaud up to `59783a9`, folded to the count; `tabloio -C subprojects/tableaud history --ref 59783a9` gives their detail
  - Commit: `37a08e92e840ea3cb48bc7ca6a5041c44096ef8e`
  - Subject: Pin the subprojects
  - Author: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 17:30:02 -0400
  - Committer: Norman Young <nbyoung@nbyoung.com>, 2026-09-29 17:30:02 -0400
  - Trailers: `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`
  - Files: `subprojects/tableaud`, the submodule pin (new at `59783a9`) and 4 more
  - Reproduce:
    - `git log --format='%as %h %ae' a7932ae..37a08e9 -- .tableaux/tasks/595e.yaml .tableaux/status/595e.yaml subprojects/tableaud`
    - `git diff --raw --abbrev=7 37a08e9^ 37a08e9 -- subprojects/tableaud`
    - `git -C subprojects/tableaud log --format='%as %h %ae' 59783a9 -- .tableaux/tasks .tableaux/status`
    - `git -C subprojects/tableaud log --format='%as %h %ae' 59783a9 -E --grep='^(Authorised|Reaffirmed): [0-9a-f]{4}$' --grep='^Reviewed: [0-9a-f]{4} '`

A first pin has no old commit to bound the subproject's events, so its detail folds them to the count up to the pin.

### Reaffirmed

No reaffirmed event: no commit up to `3cdae52` carries a `Reaffirmed:` trailer, so both pictures count 0 reaffirmed and show no such line.

Illustrative, not project content. A reaffirmation of `e9c6` after the ref reads so at glance and at detail:

| Date | By | Event | Task | Gate and state |
|---|---|---|---|---|
| 2026-10-07 | noreply@anthropic.com | reaffirmed | `e9c6` | 📐 design 🟢 nominal |

- **2026-10-07** · noreply@anthropic.com · reaffirmed · `e9c6` · 📐 design 🟢 nominal
  - Status after: 📐 design 🟢 nominal, unchanged; the status now dates from 2026-10-07
  - Model: `claude-fable-5-1`

### Authorised

No commit up to `3cdae52` carries an `Authorised:` trailer. Every authorisation in the project comes from the owner's own commit of the task file, so it shares the line of the task event, as `task, authorised` in picture 1.

## Related views

- [Gate definition](gates.md): the legend of every symbol here.
- [Task definition](task.md): `e9c6` as it stands at the ref, with its junctions and requirements.
- [Work queue](queue.md): the review a hand-off makes owed.
- [Audit](audit.md): where the files and this history disagree.
- [Global tableau](tableau.md): where every task stands at the ref.

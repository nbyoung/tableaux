#!/usr/bin/env python3
"""Productivity evidence for a Tableaux effort.

The script walks the Git history of one or more repositories, classifies each
commit by the model in README.md, attributes each event to a task and a gate,
and prints a Markdown report: one table per repository with a row per task and
gate, a totals table per role, and the elapsed times around each human review.

It needs python3 and git only.

    python3 report.py [--ref REF] [--agent EMAIL] [REPO ...]

With no REPO it takes the current directory, reads its .gitmodules and adds
each submodule that it can reach: the checkout under the submodule path, or
the url resolved against the main worktree when the path is empty.
"""
from __future__ import annotations

import argparse
import os
import re
import statistics
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

AGENT_EMAILS = ("noreply@anthropic.com",)
ID = r"[0-9a-f]{4}"
KEY = r"[a-z][a-z0-9_-]*"
TASK_PATH = re.compile(rf"^\.tableaux/tasks/({ID})\.yaml$")
STATUS_PATH = re.compile(rf"^\.tableaux/status/({ID})\.yaml$")
PIN_PATH = re.compile(r"^(subprojects/[^/]+)$")
BRANCH_TASK = re.compile(rf"task/({ID})\b")
KINDS = ("task", "authorised", "status", "reaffirmed", "reviewed", "work", "pin")
ROLES = ("agent", "co-authored", "human")
NONE = "(none)"
UNSTATED = "unstated"


# --- Git ------------------------------------------------------------------


def git(repo: str, *args: str) -> str:
    """Run git in REPO and return its standard output."""
    out = subprocess.run(
        ["git", "-C", repo, *args], capture_output=True, text=True, check=True
    )
    return out.stdout


@dataclass
class Commit:
    hash: str
    parents: list[str]
    author_email: str
    author_name: str
    committer_email: str
    author_date: datetime
    committer_date: datetime
    subject: str
    trailers: list[tuple[str, str]]
    files: list[str]

    @property
    def short(self) -> str:
        return self.hash[:7]

    @property
    def model(self) -> str | None:
        """The model named by the first Model trailer (F20), or None."""
        for key, value in self.trailers:
            if key == "model" and value:
                return value
        return None


LOG_FORMAT = "\x1e%H\x1f%P\x1f%ae\x1f%an\x1f%ce\x1f%aI\x1f%cI\x1f%s\x1f%(trailers:only,unfold)\x1f"


def parse_log(text: str) -> list[Commit]:
    """Parse the output of git log in LOG_FORMAT with --name-only."""
    commits = []
    for record in text.split("\x1e"):
        if not record.strip():
            continue
        parts = record.split("\x1f")
        if len(parts) < 10:
            raise ValueError("malformed log record: %r" % record[:80])
        h, parents, ae, an, ce, ad, cd, subject, trailers, files = parts[:10]
        commits.append(
            Commit(
                hash=h.strip(),
                parents=parents.split(),
                author_email=ae,
                author_name=an,
                committer_email=ce,
                author_date=datetime.fromisoformat(ad),
                committer_date=datetime.fromisoformat(cd),
                subject=subject,
                trailers=parse_trailers(trailers),
                files=[f.strip() for f in files.splitlines() if f.strip()],
            )
        )
    return commits


def parse_trailers(text: str) -> list[tuple[str, str]]:
    out = []
    for line in text.splitlines():
        m = re.match(r"^([A-Za-z][A-Za-z-]*):\s*(.*?)\s*$", line)
        if m:
            out.append((m.group(1).lower(), m.group(2)))
    return out


def read_log(repo: str, ref: str) -> list[Commit]:
    """Return the commits reachable from REF, oldest first."""
    text = git(repo, "log", "--reverse", "--name-only", "--date=iso-strict",
               "--format=" + LOG_FORMAT, ref)
    return parse_log(text)


class Tree:
    """Reads .tableaux files at any commit, cached by blob."""

    def __init__(self, repo: str):
        self.repo = repo
        self.trees: dict[str, dict[str, str]] = {}
        self.blobs: dict[str, str] = {}

    def paths(self, commit: str) -> dict[str, str]:
        if commit not in self.trees:
            listing = {}
            try:
                out = git(self.repo, "ls-tree", "-r", commit, "--", ".tableaux")
            except subprocess.CalledProcessError:
                out = ""
            for line in out.splitlines():
                meta, path = line.split("\t", 1)
                listing[path] = meta.split()[2]
            self.trees[commit] = listing
        return self.trees[commit]

    def read(self, commit: str, path: str) -> str | None:
        blob = self.paths(commit).get(path)
        if blob is None:
            return None
        if blob not in self.blobs:
            self.blobs[blob] = git(self.repo, "cat-file", "-p", blob)
        return self.blobs[blob]


# --- The Tableaux files, read with regular expressions -------------------


def scalar(text: str | None, key: str) -> str | None:
    """The value of a top-level KEY: value line, unquoted."""
    if text is None:
        return None
    m = re.search(rf"^{key}:\s*(.+?)\s*$", text, re.M)
    if not m:
        return None
    return m.group(1).strip("\"'")


def gate_keys(text: str | None) -> list[str]:
    if text is None:
        return []
    block = text.split("\nstates:")[0]
    return re.findall(rf"^\s*-\s*\{{\s*key:\s*({KEY})", block, re.M)


def parent_id(text: str | None) -> str | None:
    if text is None:
        return None
    m = re.search(rf"^parent:\s*\{{\s*id:\s*[\"']?({ID})", text, re.M)
    return m.group(1) if m else None


def junctions(text: str | None) -> dict[str, str]:
    """Each junction entry as its raw text, keyed by gate."""
    if text is None:
        return {}
    m = re.search(r"^junctions:\s*\n((?:[ \t]+.*\n?)*)", text, re.M)
    if not m:
        return {}
    return dict(re.findall(rf"^[ \t]+({KEY}):[ \t]*(.*?)[ \t]*$", m.group(1), re.M))


class Project:
    """The tasks of one repository as they stand at one commit."""

    def __init__(self, tree: Tree, commit: str):
        self.tree = tree
        self.commit = commit

    def task(self, tid: str) -> str | None:
        return self.tree.read(self.commit, f".tableaux/tasks/{tid}.yaml")

    def status(self, tid: str) -> dict[str, str] | None:
        text = self.tree.read(self.commit, f".tableaux/status/{tid}.yaml")
        if text is None:
            return None
        return {k: v for k in ("gate", "state", "reason", "note")
                if (v := scalar(text, k)) is not None}

    def gates(self) -> list[str]:
        return gate_keys(self.tree.read(self.commit, ".tableaux/gates.yaml"))

    def chain(self, tid: str) -> list[str]:
        """The task and its ancestors, nearest first."""
        out, seen = [], set()
        while tid and tid not in seen and self.task(tid) is not None:
            out.append(tid)
            seen.add(tid)
            tid = parent_id(self.task(tid))
        return out

    def authorities(self, tid: str) -> set[str]:
        chain = self.chain(tid)
        ancestors = chain[1:] if len(chain) > 1 else chain[:1]
        return {a for t in ancestors if (a := scalar(self.task(t), "assignee"))}

    def applies(self, tid: str, gate: str) -> bool:
        if gate == "undefined":
            return True
        for t in self.chain(tid):
            entry = junctions(self.task(t)).get(gate)
            if entry is not None:
                return "applies: false" not in entry
        return True

    def stated_model(self, tid: str, gate: str) -> str | None:
        """The model the nearest junction entry for GATE states, if any."""
        for t in self.chain(tid):
            entry = junctions(self.task(t)).get(gate)
            if entry is not None:
                m = re.search(r"\bmodel:\s*[\"']?([^\s\"',}]+)", entry)
                return m.group(1) if m else None
        return None

    def next_gate(self, tid: str, status: dict[str, str] | None) -> str | None:
        """The gate the task works towards after STATUS, or None when complete."""
        gates = self.gates()
        done = status.get("gate", "undefined") if status else "undefined"
        if status and status.get("state") == "complete":
            return None
        after = gates[gates.index(done) + 1:] if done in gates else gates[1:]
        for g in after:
            if self.applies(tid, g):
                return g
        return None

    def task_ids(self) -> list[str]:
        return sorted(m.group(1) for p in self.tree.paths(self.commit)
                      if (m := TASK_PATH.match(p)))

    def pins(self) -> dict[str, set[str]]:
        """Submodule path to the tasks whose junctions delegate to it."""
        out: dict[str, set[str]] = defaultdict(set)
        for tid in self.task_ids():
            for entry in junctions(self.task(tid)).values():
                m = re.search(r"subproject:.*url:\s*[\"']?([^\s\"'}]+)", entry)
                if m:
                    out[m.group(1).rstrip("/")].add(tid)
        return out


# --- Classification --------------------------------------------------------


def role(commit: Commit, agents: tuple[str, ...]) -> str:
    """agent, co-authored or human: see README.md."""
    if commit.author_email.lower() in agents:
        return "agent"
    for key, value in commit.trailers:
        if key == "co-authored-by" and any(a in value.lower() for a in agents):
            return "co-authored"
    return "human"


def within(ran: str, stated: str) -> bool:
    """True when the model that ran is the stated identifier or extends its prefix."""
    return ran.lower().startswith(stated.lower())


@dataclass
class Event:
    repo: str
    commit: Commit
    role: str
    kind: str
    task: str
    gate: str
    detail: str = ""
    stated: str | None = None  # the model the junction states for this gate

    @property
    def model(self) -> str | None:
        return self.commit.model

    @property
    def mismatch(self) -> bool:
        """True when the commit ran a model outside the junction's statement."""
        return bool(self.stated and self.model and not within(self.model, self.stated))

    @property
    def date(self) -> datetime:
        return self.commit.author_date


@dataclass
class Repository:
    name: str
    path: str
    ref: str
    head: str
    commits: list[Commit]
    events: list[Event]
    gates: list[str]
    titles: dict[str, str]


def branch_tasks(repo: str, commits: list[Commit]) -> dict[str, str]:
    """Commits that a merge of a task/<id> branch brought in, by hash."""
    out = {}
    for c in commits:
        m = BRANCH_TASK.search(c.subject)
        if m and len(c.parents) > 1:
            listed = git(repo, "rev-list", c.parents[1], "^" + c.parents[0])
            for h in listed.split():
                out[h] = m.group(1)
    return out


def analyse(path: str, ref: str = "HEAD", agents: tuple[str, ...] = AGENT_EMAILS,
            name: str | None = None) -> Repository:
    """Walk one repository and return its classified events."""
    commits = read_log(path, ref)
    tree = Tree(path)
    head = git(path, "rev-parse", ref).strip()
    project = Project(tree, head)
    pins = project.pins()
    by_branch = branch_tasks(path, commits)
    name = name or os.path.basename(os.path.abspath(path))
    events: list[Event] = []
    for c in commits:
        r = role(c, agents)
        here = Project(tree, c.hash)
        before = Project(tree, c.parents[0]) if c.parents else None
        tasks: set[str] = set()  # the tasks that receive this commit's work
        found: list[tuple[str, str, str, str]] = []

        for f in c.files:
            if m := TASK_PATH.match(f):
                tid = m.group(1)
                found.append(("task", tid, "defined", ""))
                actors = {c.author_email.lower(), c.committer_email.lower()}
                if actors & {a.lower() for a in here.authorities(tid)}:
                    found.append(("authorised", tid, "defined", "by task file"))
            elif m := STATUS_PATH.match(f):
                tid = m.group(1)
                tasks.add(tid)
                status = here.status(tid) or {}
                previous = before.status(tid) if before else None
                gate = status.get("gate", "undefined")
                if previous is None or previous.get("gate") != gate:
                    at = gate
                else:
                    at = here.next_gate(tid, status) or gate
                detail = " ".join(v for k in ("state", "reason") if (v := status.get(k)))
                found.append(("status", tid, at, detail))

        for key, value in c.trailers:
            if key == "authorised" and re.fullmatch(ID, value):
                found.append(("authorised", value, "defined", "by trailer"))
            elif key == "reaffirmed" and re.fullmatch(ID, value):
                tasks.add(value)
                gate = here.next_gate(value, here.status(value)) or NONE
                found.append(("reaffirmed", value, gate, ""))
            elif key == "reviewed" and (m := re.fullmatch(rf"({ID})\s+({KEY})", value)):
                tasks.add(m.group(1))
                found.append(("reviewed", m.group(1), m.group(2), ""))

        work = [f for f in c.files if not f.startswith(".tableaux/")]
        pinned = [f for f in work if PIN_PATH.match(f)]
        work = [f for f in work if f not in pinned]
        for f in pinned:
            for tid in sorted(pins.get(f, ())):
                gate = here.next_gate(tid, here.status(tid)) or NONE
                found.append(("pin", tid, gate, f))
        if work:
            targets = tasks or ({by_branch[c.hash]} if c.hash in by_branch else set())
            for tid in sorted(targets) or [NONE]:
                gate = NONE
                if tid != NONE:
                    gate = here.next_gate(tid, here.status(tid)) or NONE
                found.append(("work", tid, gate, f"{len(work)} files"))

        for kind, tid, gate, detail in found:
            stated = None
            if r != "human" and tid != NONE and gate != NONE:
                stated = here.stated_model(tid, gate)
            events.append(Event(name, c, r, kind, tid, gate, detail, stated))

    titles = {t: scalar(project.task(t), "title") or "" for t in project.task_ids()}
    return Repository(name, path, ref, head, commits, events, project.gates(), titles)


# --- Measures --------------------------------------------------------------


@dataclass
class Row:
    task: str
    gate: str
    commits: dict[str, set[str]] = field(default_factory=lambda: defaultdict(set))
    kinds: Counter = field(default_factory=Counter)
    to_review: list[timedelta] = field(default_factory=list)
    to_resume: list[timedelta] = field(default_factory=list)
    pending: timedelta | None = None


def rows(repo: Repository, now: datetime) -> list[Row]:
    """One row per task and gate, with counts and elapsed times."""
    table: dict[tuple[str, str], Row] = {}
    for e in repo.events:
        row = table.setdefault((e.task, e.gate), Row(e.task, e.gate))
        row.commits[e.role].add(e.commit.hash)
        row.kinds[e.kind] += 1

    agent_events = [e for e in repo.events if e.role in ("agent", "co-authored")]
    reviews = [e for e in repo.events if e.kind == "reviewed" and e.role == "human"]
    for rv in reviews:
        row = table[(rv.task, rv.gate)]
        handoff = [e for e in agent_events
                   if e.task == rv.task and e.gate == rv.gate and e.date < rv.date]
        if handoff:
            row.to_review.append(rv.date - max(handoff, key=lambda e: e.date).date)
        resume = [e for e in agent_events if e.task == rv.task and e.date > rv.date]
        if resume:
            row.to_resume.append(min(resume, key=lambda e: e.date).date - rv.date)

    for e in agent_events:
        if e.kind == "status" and "review" in e.detail.split():
            later = [r for r in reviews if r.task == e.task and r.gate == e.gate
                     and r.date > e.date]
            if not later:
                table[(e.task, e.gate)].pending = now - e.date

    order = {g: i for i, g in enumerate(repo.gates)}
    return sorted(table.values(),
                  key=lambda r: (r.task == NONE, r.task, order.get(r.gate, len(order)), r.gate))


def costs(repos: list[Repository]) -> tuple[list[str], list[str], dict[str, dict[str, set]]]:
    """Agent commits per gate and model, across repositories (F20).

    Returns the gates in order, the models seen, and gate -> model -> the set
    of (repository, commit) pairs. Both agent and co-authored commits count;
    a commit with no Model trailer counts under UNSTATED.
    """
    gates: list[str] = []
    for r in repos:
        gates += [g for g in r.gates if g not in gates]
    table: dict[str, dict[str, set]] = defaultdict(lambda: defaultdict(set))
    for r in repos:
        for e in r.events:
            if e.role != "human":
                table[e.gate][e.model or UNSTATED].add((r.name, e.commit.hash))
    models = sorted({m for by in table.values() for m in by if m != UNSTATED})
    if any(UNSTATED in by for by in table.values()):
        models.append(UNSTATED)
    ordered = [g for g in gates if g in table] + sorted(g for g in table if g not in gates and g != NONE)
    if NONE in table:
        ordered.append(NONE)
    return ordered, models, table


def mismatches(repos: list[Repository]) -> list[Event]:
    """One event per commit, task and gate whose Model falls outside the junction's."""
    seen, out = set(), []
    for r in repos:
        for e in r.events:
            key = (r.name, e.commit.hash, e.task, e.gate)
            if e.mismatch and key not in seen:
                seen.add(key)
                out.append(e)
    return out


def fmt_elapsed(td: timedelta) -> str:
    minutes = int(td.total_seconds() // 60)
    if minutes < 60:
        return f"{minutes}m"
    hours, minutes = divmod(minutes, 60)
    if hours < 48:
        return f"{hours}h {minutes:02d}m"
    days, hours = divmod(hours, 24)
    return f"{days}d {hours}h"


# --- Report ----------------------------------------------------------------


def render(repos: list[Repository], now: datetime, agents: tuple[str, ...]) -> str:
    out = ["# Productivity evidence", ""]
    out.append(f"As of {now.strftime('%Y-%m-%d %H:%M %z')}. "
               f"Agent identity: {', '.join(agents)}.")
    out.append("")
    out.append("| Repository | Ref | Head | Commits | Events |")
    out.append("|---|---|---|---:|---:|")
    for r in repos:
        out.append(f"| {r.name} | {r.ref} | {r.head[:7]} | {len(r.commits)} | {len(r.events)} |")
    out.append("")

    all_rows: list[tuple[Repository, Row]] = []
    for r in repos:
        out.append(f"## {r.name}")
        out.append("")
        table = rows(r, now)
        all_rows += [(r, row) for row in table]
        if not table:
            out.append("No events.")
            out.append("")
            continue
        out.append("| Id | Title | Gate | Agent | Co-authored | Human | "
                   + " | ".join(k.capitalize() for k in KINDS)
                   + " | Hand-off to review | Review to resume |")
        out.append("|---|---|---|---:|---:|---:|" + "---:|" * len(KINDS) + "---|---|")
        for row in table:
            title = r.titles.get(row.task, "")
            if len(title) > 36:
                title = title[:35] + "…"
            cells = [f"`{row.task}`" if row.task != NONE else NONE, title, row.gate]
            cells += [str(len(row.commits.get(role, ()))) for role in ROLES]
            cells += [str(row.kinds.get(k, 0)) for k in KINDS]
            review = ", ".join(fmt_elapsed(t) for t in row.to_review)
            if row.pending is not None:
                review = (review + ", " if review else "") + f"pending {fmt_elapsed(row.pending)}"
            resume = ", ".join(fmt_elapsed(t) for t in row.to_resume)
            cells += [review or "", resume or ""]
            out.append("| " + " | ".join(cells) + " |")
        out.append("")

    out.append("## Totals per role")
    out.append("")
    out.append("| Role | Commits | " + " | ".join(k.capitalize() for k in KINDS) + " |")
    out.append("|---|---:|" + "---:|" * len(KINDS))
    for role_ in ROLES:
        commits = {(r.name, e.commit.hash) for r in repos for e in r.events if e.role == role_}
        kinds = Counter(e.kind for r in repos for e in r.events if e.role == role_)
        out.append(f"| {role_} | {len(commits)} | "
                   + " | ".join(str(kinds.get(k, 0)) for k in KINDS) + " |")
    out.append("")

    to_review = [t for _, row in all_rows for t in row.to_review]
    to_resume = [t for _, row in all_rows for t in row.to_resume]
    pending = [row.pending for _, row in all_rows if row.pending is not None]
    out.append("| Measure | Count | Median | Longest |")
    out.append("|---|---:|---|---|")
    for label, values in (("Hand-off to review", to_review), ("Review to resume", to_resume),
                          ("Awaiting review", pending)):
        if values:
            median = fmt_elapsed(timedelta(seconds=statistics.median(v.total_seconds() for v in values)))
            out.append(f"| {label} | {len(values)} | {median} | {fmt_elapsed(max(values))} |")
        else:
            out.append(f"| {label} | 0 | | |")
    out.append("")
    gates, models, table = costs(repos)
    out.append("## Cost per gate by model")
    out.append("")
    out.append("Agent and co-authored commits with at least one event at the gate, "
               "by the `Model:` trailer (F20).")
    out.append("")
    if not gates:
        out.append("No agent commits.")
        out.append("")
    else:
        out.append("| Gate | " + " | ".join(models) + " | Total |")
        out.append("|---|" + "---:|" * (len(models) + 1))
        for g in gates:
            by = table[g]
            total = set().union(*by.values())
            out.append(f"| {g} | " + " | ".join(str(len(by.get(m, ()))) for m in models)
                       + f" | {len(total)} |")
        out.append("")
    bad = mismatches(repos)
    out.append("Commits whose `Model:` falls outside the model the junction states:")
    out.append("")
    out.append("| Repository | Commit | Id | Gate | Ran | Stated |")
    out.append("|---|---|---|---|---|---|")
    for e in bad:
        out.append(f"| {e.repo} | {e.commit.short} | `{e.task}` | {e.gate} | {e.model} | {e.stated} |")
    if not bad:
        out.append("| none | | | | | |")
    out.append("")
    return "\n".join(out)


# --- Discovery -------------------------------------------------------------


def is_repo(path: str) -> bool:
    """True when PATH is itself the top of a repository with a HEAD commit."""
    if not os.path.isdir(path):
        return False
    try:
        top = git(path, "rev-parse", "--show-toplevel").strip()
        git(path, "rev-parse", "--verify", "HEAD")
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    return os.path.realpath(top) == os.path.realpath(path)


def discover(root: str) -> list[tuple[str, str]]:
    """The root and every submodule of .gitmodules that git can read."""
    common = git(root, "rev-parse", "--git-common-dir").strip()
    main = os.path.dirname(os.path.abspath(os.path.join(root, common)))
    found = [(os.path.basename(main), root)]  # a linked worktree takes the main name
    modules = os.path.join(root, ".gitmodules")
    if not os.path.exists(modules):
        return found
    text = open(modules, encoding="utf-8").read()
    for section in re.split(r"^\[submodule ", text, flags=re.M)[1:]:
        path = scalar_cfg(section, "path")
        url = scalar_cfg(section, "url")
        if not path:
            continue
        name = os.path.basename(path)
        checkout = os.path.join(root, path)
        if is_repo(checkout):
            found.append((name, checkout))
        elif url and not re.match(r"^[a-z]+://|^[^/]+@", url) and is_repo(os.path.join(main, url)):
            found.append((name, os.path.normpath(os.path.join(main, url))))
        else:
            print(f"skip {path}: no checkout and no local clone at {url}", file=sys.stderr)
    return found


def scalar_cfg(section: str, key: str) -> str | None:
    m = re.search(rf"^\s*{key}\s*=\s*(.+?)\s*$", section, re.M)
    return m.group(1) if m else None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("repos", nargs="*", help="repository paths; default: . and its submodules")
    ap.add_argument("--ref", default="HEAD", help="the ref whose history to walk")
    ap.add_argument("--agent", action="append", help="an agent commit email (repeatable)")
    ap.add_argument("--now", help="the moment pending reviews are measured against (ISO 8601)")
    args = ap.parse_args(argv)
    agents = tuple(a.lower() for a in args.agent) if args.agent else AGENT_EMAILS
    now = datetime.fromisoformat(args.now) if args.now else datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    targets = [(os.path.basename(os.path.abspath(p)), p) for p in args.repos] or discover(".")
    repos = [analyse(path, args.ref, agents, name) for name, path in targets]
    print(render(repos, now, agents))
    return 0


if __name__ == "__main__":
    sys.exit(main())

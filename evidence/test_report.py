"""Tests for report.py: pure functions on fixtures and a synthetic repository.

Run from this directory:  python3 -m unittest
"""
import os
import subprocess
import tempfile
import unittest
from datetime import datetime, timedelta, timezone

import report

OWNER = "ada@example.org"
BEN = "ben@example.org"
AGENT = "noreply@anthropic.com"
AGENTS = (AGENT,)

GATES = """gates:
  - { key: undefined, symbol: A, name: Undefined, criteria: Nothing }
  - { key: defined,   symbol: B, name: Defined,   criteria: Title }
  - { key: mockup,    symbol: C, name: Mockup,    criteria: Sketch }
  - { key: design,    symbol: D, name: Design,    criteria: Model }
  - { key: release,   symbol: E, name: Release,   criteria: Shipped }
states:
  - { key: undefined, symbol: a, severity: 0, synopsis: Not defined }
  - { key: nominal,   symbol: b, severity: 1, synopsis: Proceeding }
  - { key: complete,  symbol: c, severity: 0, synopsis: Done }
reasons:
  - { key: review, symbol: d, synopsis: Waits for review }
"""
ROOT = f"title: Root\ndescription: The project\nassignee: {OWNER}\n"
CHILD = f"""title: Child
description: Agent work
assignee: {AGENT}
junctions:
  mockup: {{ applies: false }}
  design: {{ contributor: {AGENT}, model: test-model, reviewer: {OWNER} }}
parent: {{ id: "aaaa", order: 1 }}
"""
OTHER = f"""title: Other
description: Human work
assignee: {BEN}
junctions:
  release: {{ subproject: {{ url: subprojects/other }} }}
parent: {{ id: "aaaa", order: 2 }}
"""


def run(repo, *args, env=None):
    e = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_SYSTEM="/dev/null")
    e.update(env or {})
    return subprocess.run(["git", "-C", repo, *args], check=True, capture_output=True,
                          text=True, env=e).stdout


def commit(repo, email, date, subject, files=None, trailers=(), merge=None):
    """Write FILES, stage them and commit as EMAIL at DATE."""
    for path, text in (files or {}).items():
        full = os.path.join(repo, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(text)
    if files:
        run(repo, "add", "-A")
    env = {"GIT_AUTHOR_NAME": email.split("@")[0], "GIT_AUTHOR_EMAIL": email,
           "GIT_COMMITTER_NAME": email.split("@")[0], "GIT_COMMITTER_EMAIL": email,
           "GIT_AUTHOR_DATE": date, "GIT_COMMITTER_DATE": date}
    message = subject + ("\n\n" + "\n".join(trailers) if trailers else "")
    if merge:
        run(repo, "merge", "--no-ff", "-m", message, merge, env=env)
    else:
        run(repo, "commit", "--allow-empty", "-q", "-m", message, env=env)
    return run(repo, "rev-parse", "HEAD").strip()


def build(repo):
    """A history that exercises every event kind and both elapsed measures."""
    run(repo, "init", "-q", "-b", "main")
    h = {}
    h["plan"] = commit(repo, OWNER, "2026-01-01T09:00:00+00:00", "Plan the project", {
        ".tableaux/gates.yaml": GATES,
        ".tableaux/tasks/aaaa.yaml": ROOT,
        ".tableaux/tasks/b1b1.yaml": CHILD,
        ".tableaux/tasks/c2c2.yaml": OTHER,
        "PLAN.md": "# Plan\n",
    }, trailers=[f"Co-Authored-By: Agent <{AGENT}>"])
    h["defined"] = commit(repo, AGENT, "2026-01-01T10:00:00+00:00", "Record defined", {
        ".tableaux/status/b1b1.yaml": "gate: defined\nstate: nominal\n",
        "docs/model.md": "# Model\n",
    })
    h["handoff"] = commit(repo, AGENT, "2026-01-01T11:00:00+00:00", "Hand off the design", {
        ".tableaux/status/b1b1.yaml": "gate: defined\nstate: nominal\nreason: review\n",
    })
    h["review"] = commit(repo, OWNER, "2026-01-01T13:00:00+00:00", "Accept the design",
                         trailers=["Reviewed: b1b1 design"])
    h["design"] = commit(repo, AGENT, "2026-01-01T13:30:00+00:00", "Record design", {
        ".tableaux/status/b1b1.yaml": "gate: design\nstate: nominal\n",
    })
    h["reaffirm"] = commit(repo, OWNER, "2026-01-01T14:00:00+00:00", "Weekly review",
                           trailers=["Reaffirmed: b1b1", "Authorised: c2c2"])
    run(repo, "checkout", "-q", "-b", "task/c2c2")
    h["branch"] = commit(repo, BEN, "2026-01-01T15:00:00+00:00", "Write the parser", {
        "src/parser.go": "package main\n",
    })
    run(repo, "checkout", "-q", "main")
    h["merge"] = commit(repo, OWNER, "2026-01-01T16:00:00+00:00", "Merge branch 'task/c2c2'",
                        merge="task/c2c2")
    h["pending"] = commit(repo, AGENT, "2026-01-01T17:00:00+00:00", "Hand off the release", {
        ".tableaux/status/b1b1.yaml": "gate: design\nstate: nominal\nreason: review\n",
    })
    return h


class PureFunctions(unittest.TestCase):
    def test_parse_log(self):
        text = ("\x1eabc123\x1fdef456\x1fada@example.org\x1fAda\x1fada@example.org"
                "\x1f2026-01-01T09:00:00+00:00\x1f2026-01-01T09:00:00+00:00\x1fPlan"
                "\x1fCo-Authored-By: Agent <noreply@anthropic.com>\nReviewed: b1b1 design\n"
                "\x1f\n.tableaux/tasks/aaaa.yaml\nPLAN.md\n"
                "\x1e0fed\x1f\x1fx@y\x1fX\x1fx@y\x1f2026-01-01T09:00:00+00:00"
                "\x1f2026-01-01T09:00:00+00:00\x1fRoot\x1f\x1f\n")
        commits = report.parse_log(text)
        self.assertEqual(len(commits), 2)
        c = commits[0]
        self.assertEqual(c.hash, "abc123")
        self.assertEqual(c.parents, ["def456"])
        self.assertEqual(c.files, [".tableaux/tasks/aaaa.yaml", "PLAN.md"])
        self.assertEqual(c.trailers, [("co-authored-by", "Agent <noreply@anthropic.com>"),
                                      ("reviewed", "b1b1 design")])
        self.assertEqual(commits[1].parents, [])
        self.assertEqual(commits[1].files, [])

    def test_role(self):
        def mk(email, trailers):
            return report.Commit("h", [], email, "n", email, datetime.now(timezone.utc),
                                 datetime.now(timezone.utc), "s", trailers, [])
        self.assertEqual(report.role(mk(AGENT, []), AGENTS), "agent")
        self.assertEqual(report.role(mk(OWNER, [("co-authored-by", f"A <{AGENT}>")]), AGENTS),
                         "co-authored")
        self.assertEqual(report.role(mk(OWNER, [("co-authored-by", "B <ben@example.org>")]),
                                     AGENTS), "human")
        self.assertEqual(report.role(mk(OWNER, []), AGENTS), "human")

    def test_fmt_elapsed(self):
        self.assertEqual(report.fmt_elapsed(timedelta(minutes=5)), "5m")
        self.assertEqual(report.fmt_elapsed(timedelta(hours=2)), "2h 00m")
        self.assertEqual(report.fmt_elapsed(timedelta(hours=26, minutes=7)), "26h 07m")
        self.assertEqual(report.fmt_elapsed(timedelta(days=3, hours=4)), "3d 4h")

    def test_readers(self):
        self.assertEqual(report.gate_keys(GATES), ["undefined", "defined", "mockup", "design", "release"])
        self.assertEqual(report.parent_id(CHILD), "aaaa")
        self.assertIsNone(report.parent_id(ROOT))
        self.assertEqual(report.scalar(CHILD, "assignee"), AGENT)
        j = report.junctions(CHILD)
        self.assertEqual(set(j), {"mockup", "design"})
        self.assertIn("applies: false", j["mockup"])
        self.assertEqual(report.junctions(ROOT), {})
        self.assertEqual(report.parse_trailers("Reviewed: b1b1 design\nnot a trailer\n"),
                         [("reviewed", "b1b1 design")])

    def test_next_gate_and_authorities(self):
        class FakeTree:
            files = {".tableaux/gates.yaml": GATES, ".tableaux/tasks/aaaa.yaml": ROOT,
                     ".tableaux/tasks/b1b1.yaml": CHILD, ".tableaux/tasks/c2c2.yaml": OTHER}

            def paths(self, commit):
                return {p: p for p in self.files}

            def read(self, commit, path):
                return self.files.get(path)

        p = report.Project(FakeTree(), "any")
        self.assertEqual(p.chain("b1b1"), ["b1b1", "aaaa"])
        self.assertEqual(p.authorities("b1b1"), {OWNER})
        self.assertEqual(p.authorities("aaaa"), {OWNER})
        self.assertFalse(p.applies("b1b1", "mockup"))
        self.assertTrue(p.applies("c2c2", "mockup"))
        self.assertEqual(p.next_gate("b1b1", None), "defined")
        self.assertEqual(p.next_gate("b1b1", {"gate": "defined", "state": "nominal"}), "design")
        self.assertEqual(p.next_gate("c2c2", {"gate": "defined"}), "mockup")
        self.assertIsNone(p.next_gate("b1b1", {"gate": "release", "state": "complete"}))
        self.assertEqual(p.pins(), {"subprojects/other": {"c2c2"}})


class SyntheticRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.repo = cls.tmp.name
        cls.hashes = build(cls.repo)
        cls.result = report.analyse(cls.repo, "HEAD", AGENTS, name="synthetic")
        cls.now = datetime(2026, 1, 2, 17, 0, tzinfo=timezone.utc)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def events(self, **match):
        return [e for e in self.result.events
                if all(getattr(e, k) == v for k, v in match.items())]

    def test_commits_walked_oldest_first(self):
        hashes = [c.hash for c in self.result.commits]
        self.assertEqual(hashes[0], self.hashes["plan"])
        self.assertEqual(hashes[-1], self.hashes["pending"])
        self.assertEqual(len(hashes), 9)

    def test_plan_commit_is_co_authored_and_authorises(self):
        plan = self.events(kind="task")
        self.assertEqual({e.task for e in plan}, {"aaaa", "b1b1", "c2c2"})
        self.assertTrue(all(e.role == "co-authored" and e.gate == "defined" for e in plan))
        authorised = self.events(kind="authorised", detail="by task file")
        self.assertEqual({e.task for e in authorised}, {"aaaa", "b1b1", "c2c2"})
        self.assertEqual(self.events(kind="work", task=report.NONE)[0].detail, "1 files")

    def test_status_events_carry_gate_and_detail(self):
        status = self.events(kind="status", task="b1b1")
        self.assertEqual([(e.gate, e.detail) for e in status], [
            ("defined", "nominal"),
            ("design", "nominal review"),
            ("design", "nominal"),
            ("release", "nominal review"),
        ])
        self.assertTrue(all(e.role == "agent" for e in status))

    def test_work_follows_status_and_branch(self):
        work = self.events(kind="work", task="b1b1")
        self.assertEqual([(e.commit.hash, e.gate) for e in work], [(self.hashes["defined"], "design")])
        branch = self.events(kind="work", task="c2c2")
        self.assertEqual([(e.commit.hash, e.role, e.gate) for e in branch],
                         [(self.hashes["branch"], "human", "defined")])

    def test_trailer_events(self):
        reviewed = self.events(kind="reviewed")
        self.assertEqual([(e.task, e.gate, e.role) for e in reviewed], [("b1b1", "design", "human")])
        self.assertEqual([(e.task, e.gate) for e in self.events(kind="reaffirmed")], [("b1b1", "release")])
        self.assertEqual([(e.task, e.detail) for e in self.events(kind="authorised", commit=None)], [])
        by_trailer = self.events(kind="authorised", detail="by trailer")
        self.assertEqual([(e.task, e.gate) for e in by_trailer], [("c2c2", "defined")])

    def test_rows_and_elapsed(self):
        rows = {(r.task, r.gate): r for r in report.rows(self.result, self.now)}
        design = rows[("b1b1", "design")]
        self.assertEqual(design.to_review, [timedelta(hours=2)])
        self.assertEqual(design.to_resume, [timedelta(minutes=30)])
        self.assertIsNone(design.pending)
        self.assertEqual(design.kinds["reviewed"], 1)
        self.assertEqual(len(design.commits["agent"]), 3)
        self.assertEqual(len(design.commits["human"]), 1)
        release = rows[("b1b1", "release")]
        self.assertEqual(release.pending, timedelta(hours=24))
        self.assertEqual(release.to_review, [])
        self.assertEqual(rows[("b1b1", "defined")].kinds["status"], 1)
        keys = list(rows)
        self.assertEqual(keys[-1], (report.NONE, report.NONE))
        self.assertLess(keys.index(("b1b1", "defined")), keys.index(("b1b1", "design")))

    def test_render(self):
        text = report.render([self.result], self.now, AGENTS)
        self.assertIn("## synthetic", text)
        self.assertIn("| `b1b1` | Child | design | 3 | 0 | 1 |", text)
        self.assertIn("| 2h 00m | 30m |", text)
        self.assertIn("pending 24h 00m", text)
        self.assertIn("| agent | 4 | 0 | 0 | 4 | 0 | 0 | 1 | 0 |", text)
        self.assertIn("| human | 3 | 0 | 1 | 0 | 1 | 1 | 1 | 0 |", text)
        self.assertIn("| co-authored | 1 |", text)
        self.assertIn("| Hand-off to review | 1 | 2h 00m | 2h 00m |", text)
        self.assertIn("| Awaiting review | 1 | 24h 00m | 24h 00m |", text)

    def test_discover_root_only(self):
        found = report.discover(self.repo)
        self.assertEqual(found, [(os.path.basename(self.repo), self.repo)])

    def test_main_runs(self):
        import io
        from contextlib import redirect_stdout
        out = io.StringIO()
        with redirect_stdout(out):
            code = report.main([self.repo, "--now", "2026-01-02T17:00:00+00:00"])
        self.assertEqual(code, 0)
        self.assertIn("# Productivity evidence", out.getvalue())


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""corpus/check.py : check the corpus against itself and against schemas/.

A small reference reading of the method, enough to keep the corpus honest. It is
not a conforming tool; `tablo` is. For each entry it:

  1. validates every file of a valid entry's project/.tableaux (and of a
     subproject tree) against schemas/, after taking each id as a string (F16);
  2. applies every rule in RULES.md that a project tree alone decides, and
     compares the findings with `findings` in expected.yaml;
  3. after `sh corpus/build.sh`, compares the derived facts that Git supplies
     (authorisation, status date and recorder, events, pins, the condition of a
     cross-project requirement) with expected.yaml, and applies the rules that
     read a pin (J17) or a commit across a linkage (R9 on a cross-project entry).

Rules that need history to decide (P5, S11, J13, R13, H1, H2, H3) are not applied;
the check only confirms that an entry states them. The check also confirms that
every rule in RULES.md has an entry and that every entry it names exists.

Needs python3 with pyyaml and jsonschema (and rfc3987 for uri-reference).

    python3 corpus/check.py              # every entry
    python3 corpus/check.py weather-station
"""
import os
import re
import subprocess
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

CORPUS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(CORPUS)
ENTRIES = os.path.join(CORPUS, "entries")
BUILD = os.path.join(CORPUS, "build")

HEX = re.compile(r"^[0-9a-f]{4}$")
HEX40 = re.compile(r"^[0-9a-f]{40}$")
KEY = re.compile(r"^[a-z][a-z0-9_-]*$")
SEMVER = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
ABSOLUTE = re.compile(r"^[a-z][a-z0-9+.-]*://|^[^/@:]+@[^/:]+:")   # a scheme, or an scp-like user@host:path
TOOL = (0, 3)                      # the language version the schemas define, major.minor
PLAIN = {"contributor", "model", "reviewer", "references"}
TASK_FIELDS = {"title", "description", "assignee", "references", "requires", "junctions", "parent"}
REQ_FIELDS = {"id", "subproject", "from", "to", "text"}
SUB_FIELDS = {"url", "id", "commit"}
NOT_STATIC = {"P5", "S11", "J13", "R13", "H1", "H2", "H3", "H4", "H5", "H6"}
BUILT = {"J17"}                    # rules the check reads from the built repositories; with no build, only stated
# Rules whose violation the schemas alone reject. The rest need more than a schema says.
SCHEMA_RULES = {"P3", "G2", "G3", "G4", "G5", "G7", "G8", "G11", "G12", "T2", "T3", "T4", "T5", "T6", "T11",
                "R8", "R11", "J2", "J4", "J5", "J6", "J7", "J10", "J11", "J14", "S3", "S4"}
WARNINGS = {"P5", "T7", "T12", "R9", "R12", "R13", "J13", "H1", "H2", "H3", "H5", "H6"}
INFORMATION = {"H4"}               # leaves the project valid and marks nothing wrong
LENIENT = WARNINGS | INFORMATION   # every rule whose finding is not an error


def load(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def is_email(v):
    return isinstance(v, str) and re.match(r"^[^@\s]+@[^@\s]+$", v) is not None


def is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


class Project:
    """A .tableaux directory read for the rules that need no history."""

    def __init__(self, path, entry_dir=None, replace=None):
        self.path = path
        self.entry_dir = entry_dir
        self.replace = replace or {}          # absolute URL -> the tree beside project/ that stands in for it
        self.findings = []
        self.tasks = {}
        self.files = {}
        self.statuses = {}
        self.gates = []
        self.states = []
        self.reasons = []
        self.version = None
        self.gates_ok = False
        self.claims = []                      # (task, file, gate, url, commit): a commit restating a submodule pin (J17)
        self.deferred = []                    # (task, file, entry, sub tree, kind, task there): a cross-project requirement read at a pin
        self.cross = {}                       # (task, url, task there) -> the resolved condition of a cross-project requirement

    def add(self, rule, task=None, file=None, gate=None):
        self.findings.append((rule, task, file, gate))

    # ---- reading
    def read(self):
        if not os.path.isdir(self.path):
            self.add("P1")
            return self
        self.read_version()
        self.read_gates()
        tdir = os.path.join(self.path, "tasks")
        for name in sorted(os.listdir(tdir)) if os.path.isdir(tdir) else []:
            tid = name[:-5] if name.endswith(".yaml") else name
            self.tasks[tid] = load(os.path.join(tdir, name))
            self.files[tid] = "tasks/" + name
            if not HEX.match(tid):
                self.add("T1", tid, "tasks/" + name)
        self.read_statuses()
        self.check_tasks()
        self.check_tree()
        self.check_junctions()
        self.check_requires()
        self.check_statuses()
        return self

    def read_light(self):
        """Gates, tasks and statuses with no rule applied: a project read across a linkage."""
        self.read_gates()
        self.read_tasks_only()
        self.read_statuses()
        return self

    def read_statuses(self):
        sdir = os.path.join(self.path, "status")
        for name in sorted(os.listdir(sdir)) if os.path.isdir(sdir) else []:
            tid = name[:-5]
            self.statuses[tid] = load(os.path.join(sdir, name))

    def read_version(self):
        p = os.path.join(self.path, "version.yaml")
        if not os.path.exists(p):
            self.add("P2", file="version.yaml")
            return
        v = load(p)
        self.version = v
        ok = isinstance(v, dict) and isinstance(v.get("tableaux"), str) and SEMVER.match(v["tableaux"])
        if isinstance(v, dict):
            if set(v) - {"tableaux", "trunk"}:
                ok = False
            if "trunk" in v and not (isinstance(v["trunk"], str) and v["trunk"]):
                ok = False
        else:
            ok = False
        if not ok:
            self.add("P3", file="version.yaml")
        if isinstance(v, dict) and isinstance(v.get("tableaux"), str) and SEMVER.match(v["tableaux"]):
            major, minor, _ = (int(x) for x in v["tableaux"].split("."))
            if major != TOOL[0] or minor > TOOL[1]:
                self.add("P4", file="version.yaml")

    def read_gates(self):
        p = os.path.join(self.path, "gates.yaml")
        if not os.path.exists(p):
            self.add("G1", file="gates.yaml")
            return
        self.gates_ok = True
        g = load(p)
        f = "gates.yaml"
        gates = g.get("gates") or []
        states = g.get("states")
        reasons = g.get("reasons") or []
        self.gates = [x.get("key") for x in gates]
        self.states = [x.get("key") for x in (states or [])]
        self.reasons = [x.get("key") for x in reasons]
        if set(g) - {"gates", "states", "reasons"}:
            self.add("G11", file=f)
        if not gates or gates[0].get("key") != "undefined":
            self.add("G2", file=f)
        if len(gates) < 2:
            self.add("G3", file=f)
        for x in gates:
            k = x.get("key")
            need = {"key", "symbol", "name", "criteria"}
            if set(x) != need or any(not x.get(n) for n in need):
                self.add("G4", file=f, gate=k)
            if isinstance(k, str) and not KEY.match(k):
                self.add("G5", file=f, gate=k)
        for k in sorted({k for k in self.gates if self.gates.count(k) > 1}):
            self.add("G6", file=f, gate=k)
        if not states:
            self.add("G7", file=f)
        else:
            for x in states:
                if set(x) != {"key", "symbol", "severity", "synopsis"} or not x.get("symbol") or not x.get("synopsis"):
                    self.add("G7", file=f)
                sev = x.get("severity")
                if not is_int(sev) or sev < 0:
                    self.add("G8", file=f)
                if isinstance(x.get("key"), str) and not KEY.match(x["key"]):
                    self.add("G5", file=f)
            if len(set(self.states)) != len(self.states):
                self.add("G9", file=f)
            sev = {x.get("key"): x.get("severity") for x in states}
            if sev.get("undefined") != 0 or sev.get("complete") != 0:
                self.add("G12", file=f)
        for x in reasons:
            if set(x) != {"key", "symbol", "synopsis"}:
                self.add("G10", file=f)
        if len(set(self.reasons)) != len(self.reasons):
            self.add("G10", file=f)

    # ---- tasks
    def ids(self, task, out=None):
        """Every id a task file names, with a flag for whether it was quoted."""
        t = self.tasks[task]
        res = []
        if isinstance(t.get("parent"), dict) and "id" in t["parent"]:
            res.append(t["parent"]["id"])
        for r in t.get("requires") or []:
            if isinstance(r, dict) and "id" in r:
                res.append(r["id"])
            if isinstance(r, dict) and isinstance(r.get("subproject"), dict) and "id" in r["subproject"]:
                res.append(r["subproject"]["id"])
        for j in (t.get("junctions") or {}).values():
            if isinstance(j, dict) and isinstance(j.get("subproject"), dict) and "id" in j["subproject"]:
                res.append(j["subproject"]["id"])
        return res

    def check_tasks(self):
        for tid, t in self.tasks.items():
            f = self.files[tid]
            if not isinstance(t, dict):
                self.add("T2", tid, f)
                continue
            if any(not isinstance(t.get(k), str) or not t.get(k) for k in ("title", "description", "assignee")):
                self.add("T2", tid, f)
            if set(t) - TASK_FIELDS:
                self.add("T3", tid, f)
            emails = [t.get("assignee")] if "assignee" in t else []
            refs = list(t.get("references") or [])
            for j in (t.get("junctions") or {}).values():
                if isinstance(j, dict):
                    emails += [j[k] for k in ("contributor", "reviewer") if k in j]
                    refs += j.get("references") or []
            if any(not is_email(e) for e in emails):
                self.add("T4", tid, f)
            if any(not (isinstance(r, dict) and r.get("url") and set(r) <= {"url", "text"}
                        and ("text" not in r or r["text"])) for r in refs):
                self.add("T5", tid, f)
            for i in self.ids(tid):
                if not isinstance(i, str):
                    self.add("T7", tid, f)
                elif not HEX.match(i):
                    self.add("T6", tid, f)

    def sid(self, v):
        return v if isinstance(v, str) else str(v)

    def parent(self, tid):
        p = self.tasks[tid].get("parent")
        return self.sid(p["id"]) if isinstance(p, dict) and "id" in p else None

    def children(self, tid):
        return [c for c in self.tasks if self.parent(c) == tid]

    def chain(self, tid):
        seen, cur, out = set(), tid, []
        while cur is not None and cur in self.tasks and cur not in seen:
            seen.add(cur)
            cur = self.parent(cur)
            if cur is not None:
                out.append(cur)
        return out, cur in seen and cur is not None

    def ancestors(self, tid):
        out, cur, seen = [], self.parent(tid), {tid}
        while cur in self.tasks and cur not in seen:
            out.append(cur)
            seen.add(cur)
            cur = self.parent(cur)
        return out

    def check_tree(self):
        roots = [t for t in self.tasks if self.parent(t) is None]
        if len(roots) != 1:
            self.add("T8")
        self.root = roots[0] if len(roots) == 1 else None
        for tid, t in self.tasks.items():
            f = self.files[tid]
            p = t.get("parent")
            if p is None:
                continue
            if not isinstance(p, dict) or "id" not in p or set(p) - {"id", "order"}:
                self.add("T11", tid, f)
            elif "order" in p and (not is_int(p["order"]) or p["order"] < 1):
                self.add("T11", tid, f)
            par = self.parent(tid)
            if par not in self.tasks:
                self.add("T9", tid, f)
        for tid in self.tasks:
            cur, seen = tid, set()
            while cur is not None and cur in self.tasks:
                if cur in seen:
                    self.add("T10", tid, self.files[tid])
                    break
                seen.add(cur)
                cur = self.parent(cur)
        groups = {}
        for tid in self.tasks:
            p = self.parent(tid)
            o = self.tasks[tid].get("parent", {}).get("order") if isinstance(self.tasks[tid].get("parent"), dict) else None
            if p in self.tasks and is_int(o):
                groups.setdefault(p, []).append(o)
        for p, orders in sorted(groups.items()):
            if len(set(orders)) != len(orders):
                self.add("T12", p, self.files[p])

    def order(self):
        """Depth first, siblings by order then id; siblings without order follow."""
        if self.root is None:
            return []
        out = []

        def key(c):
            p = self.tasks[c]["parent"]
            return (0, p["order"], c) if is_int(p.get("order")) else (1, 0, c)

        def walk(t, seen):
            out.append(t)
            for c in sorted(self.children(t), key=key):
                if c not in seen:
                    walk(c, seen | {c})
        walk(self.root, {self.root})
        return out

    # ---- junctions
    @staticmethod
    def kind(j):
        if not isinstance(j, dict):
            return "BAD"
        groups = [bool(set(j) & PLAIN), "subproject" in j, "applies" in j]
        if sum(groups) > 1:
            return "MIXED"
        if "applies" in j:
            return "NA" if j["applies"] is False and set(j) == {"applies"} else "APPLIES"
        if "subproject" in j:
            return "REC" if set(j) == {"subproject"} else "MIXED"
        if set(j) - PLAIN:
            return "UNKNOWN"
        return "PLAIN"

    def own_entry(self, tid, gate):
        return ((self.tasks[tid].get("junctions") or {}).get(gate))

    def resolve_kind(self, tid, gate):
        if gate == "undefined":
            return "PLAIN"
        chain = [tid] + self.ancestors(tid)
        for i, t in enumerate(chain):
            j = self.own_entry(t, gate)
            if j is None:
                continue
            k = self.kind(j)
            if k == "NA":
                return "NA"
            if k == "PLAIN":
                return "PLAIN"
            if k == "REC" and i == 0:
                return "REC"
        return "PLAIN"

    def applicable(self, tid):
        return [g for g in self.gates if self.resolve_kind(tid, g) != "NA"]

    def sub_project(self, url):
        """Where the other project's .tableaux is and how the url links it: `directory` (a
        path inside project/, read at the same commit), `submodule` (a tree beside project/,
        pinned) or `url` (an absolute URL, through the entry's replace map). None when it
        does not resolve."""
        if not isinstance(url, str) or not url:
            return None, None
        if ABSOLUTE.match(url):
            name = self.replace.get(url)
            p = os.path.join(self.entry_dir, name, ".tableaux") if self.entry_dir and name else None
            return (p if p and os.path.isdir(p) else None), "url"
        if self.entry_dir:
            p = os.path.join(self.entry_dir, "project", url, ".tableaux")
            if os.path.isdir(p):
                return p, "directory"
            p = os.path.join(self.entry_dir, url, ".tableaux")
            if os.path.isdir(p):
                return p, "submodule"
        return None, "path"

    def check_junctions(self):
        for tid, t in self.tasks.items():
            f = self.files[tid]
            js = t.get("junctions") or {}
            for gate, j in js.items():
                k = self.kind(j)
                if self.gates_ok and gate not in self.gates:
                    self.add("J1", tid, f, gate)
                    continue
                if gate == "undefined":
                    self.add("J2" if k == "NA" else "J11", tid, f, gate)
                    continue
                if k == "MIXED":
                    self.add("J4", tid, f, gate)
                elif k == "APPLIES":
                    self.add("J6", tid, f, gate)
                elif k == "UNKNOWN" or k == "BAD":
                    self.add("J10", tid, f, gate)
                elif k == "PLAIN" and "model" in j and "contributor" not in j:
                    self.add("J5", tid, f, gate)
                elif k == "REC":
                    self.check_recursive(tid, f, gate, j["subproject"], bool(self.children(tid)))
            for gate, j in js.items():
                if gate == "undefined" and self.kind(j) == "REC":
                    self.check_recursive(tid, f, gate, j["subproject"], False, quiet=True)
            if self.gates_ok and self.gates and not [g for g in self.applicable(tid) if g != "undefined"]:
                self.add("J12", tid, f)

    def check_recursive(self, tid, f, gate, sp, is_parent, quiet=False):
        if not quiet and is_parent:
            self.add("J3", tid, f, gate)
        self.check_subproject(tid, f, gate, sp, quiet=quiet)

    def check_subproject(self, tid, f, gate, sp, on_requirement=False, quiet=False):
        """The rules on a `subproject`, on a junction (gate) or a requirement (gate None):
        its shape (J7, or R11 on a requirement), J14 to J16, J17 deferred to the build,
        J8 and J9. Returns (the tree, its kind, the task read there), or None."""
        shape = "R11" if on_requirement else "J7"
        if not isinstance(sp, dict) or not sp.get("url") or set(sp) - SUB_FIELDS or (on_requirement and "id" not in sp):
            if not quiet:
                self.add(shape, tid, f, gate)
            return None
        commit = sp.get("commit")
        if commit is not None and not (isinstance(commit, str) and HEX40.match(commit)):
            self.add("J14", tid, f, gate)
            return None
        url = sp["url"]
        if ABSOLUTE.match(url) and commit is None:
            self.add("J15", tid, f, gate)
            return None
        sub, kind = self.sub_project(url)
        if sub is None:
            self.add("J8", tid, f, gate)
            return None
        if kind == "directory" and commit is not None:
            self.add("J16", tid, f, gate)
        if kind == "submodule" and commit is not None:
            self.claims.append((tid, f, gate, url, commit))
        subp = Project(sub)
        subp.read_tasks_only()
        want = self.sid(sp["id"]) if "id" in sp else subp.root
        if want not in subp.tasks:
            self.add("J9", tid, f, gate)
            return None
        return sub, kind, want

    def read_tasks_only(self):
        tdir = os.path.join(self.path, "tasks")
        for name in sorted(os.listdir(tdir)):
            self.tasks[name[:-5]] = load(os.path.join(tdir, name))
        roots = [t for t in self.tasks if self.parent(t) is None]
        self.root = roots[0] if len(roots) == 1 else None

    # ---- requires
    def gate_idx(self, g):
        return self.gates.index(g) if g in self.gates else None

    def status_gate(self, tid):
        s = self.statuses.get(tid)
        return s.get("gate", "undefined") if isinstance(s, dict) else "undefined"

    def next_gate(self, tid):
        app = self.applicable(tid)
        g = self.status_gate(tid)
        if g not in app:
            return None
        i = app.index(g)
        return app[i + 1] if i + 1 < len(app) else None

    def requirement(self, tid, r):
        """Resolve a local requirement: (from, to, met, due, condition), or None when the rule fails."""
        o = r["id"]
        if o not in self.tasks or not self.gates_ok:
            return None
        oapp, tapp = self.applicable(o), self.applicable(tid)
        frm = r.get("from") or oapp[-1]
        to = r.get("to") or ([g for g in tapp if g != "undefined"] or [None])[0]
        if frm not in oapp or to not in tapp or self.children(o) or self.children(tid):
            return None
        met = self.gate_idx(self.status_gate(o)) >= self.gate_idx(frm)
        nxt = self.next_gate(tid)
        due = nxt is not None and self.gate_idx(nxt) >= self.gate_idx(to)
        return frm, to, met, due, ("met" if met else "unmet" if due else "pending")

    def cross_condition(self, tid, r, subp, want, ogate):
        """Resolve a cross-project requirement, given the originating task's gate at the
        commit the linkage fixes: (from, to, met, due, condition), or None."""
        if not self.gates_ok or not subp.gates_ok or want not in subp.tasks:
            return None
        oapp, tapp = subp.applicable(want), self.applicable(tid)
        frm = r.get("from") or oapp[-1]
        to = r.get("to") or ([g for g in tapp if g != "undefined"] or [None])[0]
        if frm not in oapp or to not in tapp or self.children(tid) or subp.children(want):
            return None
        met = (subp.gate_idx(ogate) or 0) >= subp.gate_idx(frm)
        nxt = self.next_gate(tid)
        due = nxt is not None and self.gate_idx(nxt) >= self.gate_idx(to)
        return frm, to, met, due, ("met" if met else "unmet" if due else "pending")

    def check_cross(self, tid, f, r):
        """A requirement that names its task through `subproject`."""
        res = self.check_subproject(tid, f, None, r["subproject"], on_requirement=True)
        if res is None:
            return
        sub, kind, want = res
        url = r["subproject"]["url"]
        for j in (self.tasks[tid].get("junctions") or {}).values():         # R12: a junction already reads it
            jsp = j.get("subproject") if self.kind(j) == "REC" else None
            if not isinstance(jsp, dict) or jsp.get("url") != url:
                continue
            if "id" in jsp:
                jwant = self.sid(jsp["id"])
            else:
                jp = Project(sub)
                jp.read_tasks_only()
                jwant = jp.root
            if jwant == want:
                self.add("R12", tid, f)
                break
        subp = Project(sub).read_light()
        if not self.gates_ok or not subp.gates_ok:
            return
        frm, to = r.get("from"), r.get("to")
        if frm is not None and (frm not in subp.gates or frm not in subp.applicable(want)):
            self.add("R6", tid, f, frm)
        if to == "undefined":
            self.add("R10", tid, f, to)
        elif to is not None and (to not in self.gates or to not in self.applicable(tid)):
            self.add("R7", tid, f, to)
        if kind == "directory":                                              # the same commit: the tree in hand is the one read
            res = self.cross_condition(tid, r, subp, want, subp.status_gate(want))
            self.cross[(tid, url, want)] = res
            if res and res[4] == "unmet":
                self.add("R9", tid, f)
        else:                                                                # at a pin: read after the build
            self.deferred.append((tid, f, r, sub, kind, want))

    def check_requires(self):
        edges = {}
        for tid, t in self.tasks.items():
            f = self.files[tid]
            for r in t.get("requires") or []:
                if not isinstance(r, dict):
                    self.add("R8", tid, f)
                    continue
                if set(r) - REQ_FIELDS or ("text" in r and not r["text"]):
                    self.add("R8", tid, f)
                if ("id" in r) == ("subproject" in r):                       # neither, or both
                    self.add("R11" if "subproject" in r else "R8", tid, f)
                    continue
                if "subproject" in r:
                    self.check_cross(tid, f, r)
                    continue
                o = self.sid(r["id"])
                if o not in self.tasks:
                    self.add("R1", tid, f)
                    continue
                if o == tid:
                    self.add("R3", tid, f)
                    continue
                if o in self.ancestors(tid):
                    self.add("R4", tid, f)
                    continue
                if tid in self.ancestors(o):
                    self.add("R5", tid, f)
                    continue
                edges.setdefault(tid, set()).add(o)
                if self.gates_ok:
                    frm, to = r.get("from"), r.get("to")
                    if frm is not None and (frm not in self.gates or frm not in self.applicable(o)):
                        self.add("R6", tid, f, frm)
                    if to == "undefined":
                        self.add("R10", tid, f, to)
                    elif to is not None and (to not in self.gates or to not in self.applicable(tid)):
                        self.add("R7", tid, f, to)
        # cycles: a task reachable from itself
        def reach(a):
            seen, stack = set(), list(edges.get(a, ()))
            while stack:
                x = stack.pop()
                if x not in seen:
                    seen.add(x)
                    stack.extend(edges.get(x, ()))
            return seen
        for tid in sorted(edges):
            if tid in reach(tid):
                self.add("R2", tid, self.files[tid])
        if self.gates_ok:
            for tid, t in self.tasks.items():
                for r in t.get("requires") or []:
                    if isinstance(r, dict) and "id" in r and set(r) <= {"id", "from", "to", "text"}:
                        res = self.requirement(tid, {**r, "id": self.sid(r["id"])})
                        if res and res[4] == "unmet":
                            self.add("R9", tid, self.files[tid])

    def linkages(self, tid):
        """Every (url, subproject) a task's junctions and requirements name."""
        t = self.tasks[tid]
        out = []
        for j in (t.get("junctions") or {}).values():
            if self.kind(j) == "REC" and isinstance(j["subproject"], dict) and isinstance(j["subproject"].get("url"), str):
                out.append((j["subproject"]["url"], j["subproject"]))
        for r in t.get("requires") or []:
            if isinstance(r, dict) and isinstance(r.get("subproject"), dict) and isinstance(r["subproject"].get("url"), str):
                out.append((r["subproject"]["url"], r["subproject"]))
        return out

    # ---- status
    def check_statuses(self):
        for tid, s in self.statuses.items():
            f = "status/%s.yaml" % tid
            if tid not in self.tasks:
                self.add("S1", tid, f)
                continue
            if self.children(tid):
                self.add("S2", tid, f)
            if not isinstance(s, dict) or "gate" not in s or set(s) - {"gate", "state", "reason", "note"} \
                    or ("note" in s and not s["note"]):
                self.add("S3", tid, f)
                if not isinstance(s, dict) or "gate" not in s:
                    continue
            gate, state = s["gate"], s.get("state")
            if (gate == "undefined") != (state == "undefined"):
                if gate == "undefined" or state == "undefined":
                    self.add("S4", tid, f)
            if not self.gates_ok:
                continue
            if gate not in self.gates:
                self.add("S5", tid, f, gate)
                continue
            if (state is not None and state not in self.states) or \
                    (s.get("reason") is not None and s["reason"] not in self.reasons):
                self.add("S6", tid, f)
            app = self.applicable(tid)
            if gate not in app:
                self.add("S7", tid, f, gate)
                continue
            last = app[-1]
            if gate == last and state != "complete":
                self.add("S8", tid, f, gate)
            if state == "complete" and gate != last:
                self.add("S12", tid, f, gate)
            if gate != "undefined" and gate != last:
                nxt = app[app.index(gate) + 1]
                if self.resolve_kind(tid, nxt) == "REC":
                    if set(s) - {"gate"}:
                        self.add("S9", tid, f, gate)
                elif state is None:
                    self.add("S10", tid, f, gate)


# ---- schemas
def id_strings(doc):
    """Take every id a task file names as a string, as a tool does (F16)."""
    if not isinstance(doc, dict):
        return doc
    if isinstance(doc.get("parent"), dict) and "id" in doc["parent"]:
        doc["parent"]["id"] = str(doc["parent"]["id"])
    for r in doc.get("requires") or []:
        if isinstance(r, dict) and "id" in r:
            r["id"] = str(r["id"])
        if isinstance(r, dict) and isinstance(r.get("subproject"), dict) and "id" in r["subproject"]:
            r["subproject"]["id"] = str(r["subproject"]["id"])
    for j in (doc.get("junctions") or {}).values():
        if isinstance(j, dict) and isinstance(j.get("subproject"), dict) and "id" in j["subproject"]:
            j["subproject"]["id"] = str(j["subproject"]["id"])
    return doc


def schema_problems(tableaux):
    sdir = os.path.join(ROOT, "schemas")
    vals = {}
    for n in ("version", "gates", "task", "status"):
        vals[n] = Draft202012Validator(load(os.path.join(sdir, n + ".schema.yaml")), format_checker=FormatChecker())
    bad = []

    def one(kind, path, doc):
        for e in vals[kind].iter_errors(doc):
            bad.append("%s: %s" % (os.path.relpath(path, CORPUS), e.message))
    one("version", tableaux + "/version.yaml", load(tableaux + "/version.yaml"))
    one("gates", tableaux + "/gates.yaml", load(tableaux + "/gates.yaml"))
    for kind, sub in (("task", "tasks"), ("status", "status")):
        d = os.path.join(tableaux, sub)
        for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            doc = load(os.path.join(d, name))
            one(kind, os.path.join(d, name), id_strings(doc) if kind == "task" else doc)
    return bad


# ---- Git-derived facts
def git(repo, *args):
    r = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args), r.stderr.strip()))
    return r.stdout


def labels(path):
    out = {}
    if os.path.exists(path):
        for line in open(path):
            k, v = line.split()
            out[k] = v
    return out


def trailers(repo, rev):
    """Commits in rev's history with their fields and message."""
    fmt = "%H%x1f%an%x1f%ae%x1f%cn%x1f%ce%x1f%as%x1f%B%x1e"
    out = git(repo, "log", "--format=" + fmt, rev)
    res = []
    for rec in out.split("\x1e"):
        rec = rec.strip("\n")
        if not rec:
            continue
        h, an, ae, cn, ce, d, body = rec.split("\x1f", 6)
        res.append(dict(hash=h, ae=ae, ce=ce, date=d, body=body))
    return res


def gitlink(repo, rev, path):
    """The commit a submodule at path pins at rev, or None."""
    try:
        line = git(repo, "ls-tree", rev, path).split()
        return line[2] if line and line[0] == "160000" else None
    except (RuntimeError, IndexError):
        return None


def sub_repo(repo, exp, url):
    """The built repository behind a linkage: beside the entry's, named by the path's last
    segment for a submodule or by the replace map for an absolute URL."""
    if ABSOLUTE.match(url):
        name = (exp.get("replace") or {}).get(url)
        return "%s.%s" % (repo, name) if name else None
    return "%s.%s" % (repo, os.path.basename(url))


def check_history(name, exp, proj, problems):
    """Apply what the built repository decides and compare the facts it supplies.
    Returns whether the entry is built."""
    repo = os.path.join(BUILD, name)
    if not os.path.isdir(repo):
        return False
    lab = labels(repo + ".labels.txt")
    rev = exp.get("ref", "main")
    try:
        git(repo, "rev-parse", "--verify", rev + "^{commit}")
    except RuntimeError:
        problems.append("%s: ref %s does not resolve" % (name, rev))
        return True
    text = yaml.dump(exp)
    subs = [labels(p) for p in _sublabels(repo)]
    for m in set(re.findall(r"(?:commit|old|new|pin): (\S+)", text)):
        m = m.strip("'\"")
        if m not in lab and not any(m in s for s in subs):
            problems.append("%s: label %s is in no labels file" % (name, m))
    # J17: a commit that restates a submodule pin equals it
    for tid, f, gate, url, commit in proj.claims:
        if gitlink(repo, rev, url) != commit:
            proj.add("J17", tid, f, gate)
    # a cross-project requirement read at its pin
    for tid, f, r, sub, kind, want in proj.deferred:
        sp = r["subproject"]
        srepo = sub_repo(repo, exp, sp["url"])
        commit = sp["commit"] if kind == "url" else gitlink(repo, rev, sp["url"])
        try:
            doc = yaml.safe_load(git(srepo, "show", "%s:.tableaux/status/%s.yaml" % (commit, want))) or {}
        except RuntimeError:
            doc = {}
        subp = Project(sub).read_light()
        res = proj.cross_condition(tid, r, subp, want, doc.get("gate", "undefined"))
        proj.cross[(tid, sp["url"], want)] = res
        if res and res[4] == "unmet":
            proj.add("R9", tid, f)
    # trunk
    trunk = None
    tr = exp.get("trunk") or {}
    try:
        v = git(repo, "show", rev + ":.tableaux/version.yaml")
        vt = (yaml.safe_load(v) or {}).get("trunk")
    except RuntimeError:
        vt = None
    if "undetermined" in tr:
        trunk = None
    elif vt:
        trunk = vt
    else:
        try:
            trunk = git(repo, "symbolic-ref", "--short", "refs/remotes/origin/HEAD").strip().split("/", 1)[1]
        except RuntimeError:
            trunk = tr.get("caller")
    commits = trailers(repo, rev)
    for tid, t in (exp.get("tasks") or {}).items():
        a = t.get("authorisation")
        if a and trunk:
            authorities = t.get("authorities")
            state, by, deciding = _authorisation(repo, tid, trunk, rev, authorities or [])
            if a.get("state") and a["state"] != state:
                problems.append("%s/%s: authorisation is %s, expected %s" % (name, tid, state, a["state"]))
            if a.get("commit") and lab.get(a["commit"]) != deciding:
                problems.append("%s/%s: deciding commit differs from %s" % (name, tid, a["commit"]))
            if a.get("by") and a["by"] != by:
                problems.append("%s/%s: authorisation by %s, expected %s" % (name, tid, by, a["by"]))
        elif a and a.get("state") == "proposed" and trunk is None:
            pass
        s = t.get("status")
        if s and not s.get("derived") and "subproject" not in t and s.get("commit"):
            sc = _status_commit(repo, tid, rev, commits)
            if sc is None:
                problems.append("%s/%s: no deciding status commit" % (name, tid))
            else:
                if lab.get(s["commit"]) != sc["hash"]:
                    problems.append("%s/%s: status commit differs from %s" % (name, tid, s["commit"]))
                if s.get("date") and str(s["date"]) != sc["date"]:
                    problems.append("%s/%s: status date %s, expected %s" % (name, tid, sc["date"], s["date"]))
                if s.get("recorder") and s["recorder"] != sc["ae"]:
                    problems.append("%s/%s: status recorder %s, expected %s" % (name, tid, sc["ae"], s["recorder"]))
        if t.get("events"):                    # the parent's own events; an event marked subproject comes from the pin
            got = _events(repo, tid, rev, commits, lab, proj, exp)
            want = [{k: (str(v) if k == "date" else v) for k, v in e.items() if k != "subproject"}
                    for e in t["events"] if "subproject" not in e]
            want = [_norm(e) for e in want]
            if got != want:
                problems.append("%s/%s: events differ\n  got  %s\n  want %s" % (name, tid, got, want))
        sp = t.get("subproject")
        if sp and sp.get("pin"):
            sub = sp["url"]
            if ABSOLUTE.match(sub):            # the commit the task file names
                stated = [x.get("commit") for u, x in proj.linkages(tid) if u == sub] if tid in proj.tasks else []
                pinned = stated[0] if stated else None
            else:
                pinned = gitlink(repo, rev, sub)
            if pinned is None:
                problems.append("%s/%s: no pin at %s" % (name, tid, sub))
                continue
            srepo = sub_repo(repo, exp, sub)
            slab = labels(srepo + ".labels.txt") if srepo else {}
            if slab.get(sp["pin"]) != pinned:
                problems.append("%s/%s: pin is not %s" % (name, tid, sp["pin"]))
    return True


def _sublabels(repo):
    d, base = os.path.dirname(repo), os.path.basename(repo)
    return [os.path.join(d, n) for n in os.listdir(d) if n.startswith(base + ".") and n.endswith(".labels.txt")
            and n != base + ".labels.txt"]


def _norm(e):
    return {k: e[k] for k in sorted(e)}


def _authorisation(repo, tid, trunk, rev, authorities):
    if rev != trunk:
        return "proposed", None, None
    try:
        git(repo, "rev-parse", "--verify", trunk)
    except RuntimeError:
        trunk = "origin/" + trunk
    fp = git(repo, "log", "--first-parent", "--format=%H", trunk).split()
    changed = set(git(repo, "log", "--first-parent", "--format=%H", trunk, "--", ".tableaux/tasks/%s.yaml" % tid).split())
    trailed = set(git(repo, "log", "--first-parent", "--format=%H", "-E", "--grep=^Authorised: %s$" % tid, trunk).split())
    for h in fp:
        if h in changed or h in trailed:
            an = git(repo, "log", "-1", "--format=%ae %ce", h).split()
            ok = any(x in authorities for x in an) or (not authorities and an[0] == an[0] and _is_owner(repo, h, an))
            return ("authorised" if ok else "proposed"), an[0], h
    return "proposed", None, None


def _is_owner(repo, commit, emails):
    """The root has no authority but the owner, its own assignee."""
    ids = git(repo, "ls-tree", "--name-only", commit, ".tableaux/tasks/").split()
    for p in ids:
        t = yaml.safe_load(git(repo, "show", "%s:%s" % (commit, p)))
        if "parent" not in t:
            return t["assignee"] in emails
    return False


def _status_commit(repo, tid, rev, commits):
    path = ".tableaux/status/%s.yaml" % tid
    try:
        git(repo, "cat-file", "-e", "%s:%s" % (rev, path))
    except RuntimeError:
        path = ".tableaux/tasks/%s.yaml" % tid       # an undefined leaf is dated by its task file
    changed = git(repo, "log", "--format=%H", rev, "--", path).split()
    for c in commits:
        if c["hash"] in changed or re.search(r"^Reaffirmed: %s$" % tid, c["body"], re.M):
            return c
    return None


def _commit_fields(repo, h, tpath):
    """url -> the commit field the task file states at h, for every linkage it names."""
    try:
        doc = yaml.safe_load(git(repo, "show", "%s:%s" % (h, tpath))) or {}
    except RuntimeError:
        return {}
    out = {}
    if not isinstance(doc, dict):
        return out
    sps = [j.get("subproject") for j in (doc.get("junctions") or {}).values() if isinstance(j, dict)]
    sps += [r.get("subproject") for r in doc.get("requires") or [] if isinstance(r, dict)]
    for sp in sps:
        if isinstance(sp, dict) and isinstance(sp.get("url"), str):
            out[sp["url"]] = sp.get("commit")
    return out


def _events(repo, tid, rev, commits, lab, proj, exp):
    rev_lab = {v: k for k, v in lab.items()}
    for p in _sublabels(repo):
        rev_lab.update({v: k for k, v in labels(p).items()})
    tpath, spath = ".tableaux/tasks/%s.yaml" % tid, ".tableaux/status/%s.yaml" % tid
    tch = set(git(repo, "log", "--format=%H", rev, "--", tpath).split())
    sch = set(git(repo, "log", "--format=%H", rev, "--", spath).split())
    # the linkages the task names, by kind: a submodule's pin moves with the gitlink, a URL's with the commit field
    pins = {}                                   # hash -> [(url, old, new)]: one per url, however many entries name it
    if proj is not None and tid in proj.tasks:
        for url in sorted({u for u, _ in proj.linkages(tid)}):
            _, kind = proj.sub_project(url)
            if kind == "submodule":
                for h in git(repo, "log", "--format=%H", rev, "--", url).split():
                    for line in git(repo, "diff-tree", "-r", "--root", h, "--", url).splitlines():
                        parts = line[1:].split()
                        if len(parts) >= 4 and parts[1] == "160000":
                            old = None if set(parts[2]) == {"0"} else parts[2]
                            pins.setdefault(h, []).append((url, old, parts[3]))
            elif kind == "url":
                for h in tch:
                    now = _commit_fields(repo, h, tpath).get(url)
                    before = _commit_fields(repo, h + "^", tpath).get(url)
                    if now is not None and now != before:
                        pins.setdefault(h, []).append((url, before, now))

    def short(h):
        return rev_lab.get(h, h[:7])
    evs = []
    for c in reversed(commits):
        h = c["hash"]
        base = dict(date=c["date"], commit=short(h), by=c["ae"], task=tid)
        # author, not committer, is the actor: read it again
        if h in tch:
            evs.append(dict(base, event="task"))
        if re.search(r"^Authorised: %s$" % tid, c["body"], re.M):
            evs.append(dict(base, event="authorised"))
        if h in sch:
            e = dict(base, event="status")
            try:
                doc = yaml.safe_load(git(repo, "show", "%s:%s" % (h, spath))) or {}
                for k in ("gate", "state", "reason", "note"):
                    if k in doc:
                        e[k] = doc[k]
            except RuntimeError:
                pass
            evs.append(e)
        if re.search(r"^Reaffirmed: %s$" % tid, c["body"], re.M):
            evs.append(dict(base, event="reaffirmed"))
        m = re.search(r"^Reviewed: %s (\S+)$" % tid, c["body"], re.M)
        if m:
            evs.append(dict(base, event="reviewed", gate=m.group(1)))
        for url, old, new in sorted(pins.get(h, [])):
            e = dict(base, event="pin", url=url, new=short(new))
            if old is not None:
                e["old"] = short(old)
            evs.append(e)
    return [_norm(e) for e in evs]


# ---- entry checks
def entry_project(name):
    d = os.path.join(ENTRIES, name)
    p = os.path.join(d, "project", ".tableaux")
    return d, p


def check_entry(name, problems):
    """The static reading: schemas and the rules a tree alone decides. Returns
    (expected, the project), with the project None for an entry read in place."""
    d, p = entry_project(name)
    exp = load(os.path.join(d, "expected.yaml"))
    if exp.get("entry") != name:
        problems.append("%s: expected.yaml names entry %s" % (name, exp.get("entry")))
    findings = exp.get("findings") or []
    for f in findings:
        sev = "warning" if f["rule"] in WARNINGS else "information" if f["rule"] in INFORMATION else "error"
        if f.get("severity") != sev:
            problems.append("%s: rule %s has severity %s" % (name, f["rule"], f.get("severity")))
    errors = [f for f in findings if f["rule"] not in LENIENT]
    if bool(exp.get("valid")) == bool(errors):
        problems.append("%s: valid is %s with %d errors" % (name, exp.get("valid"), len(errors)))
    if "source" in exp:
        return exp, None
    proj = Project(p, d, exp.get("replace")).read()
    if exp.get("valid") and os.path.isdir(p):
        for msg in schema_problems(p):
            problems.append("%s: schema: %s" % (name, msg))
    elif os.path.isdir(p) and any(f["rule"] in SCHEMA_RULES for f in findings):
        try:
            if not schema_problems(p):
                problems.append("%s: the schemas accept a project that states a schema rule's finding" % name)
        except FileNotFoundError:
            pass
    return exp, proj


def compare(name, exp, proj, built, problems):
    """Compare the findings and the derived facts a tree decides, once the build has
    added what it decides."""
    d, p = entry_project(name)
    findings = exp.get("findings") or []
    skip = set(NOT_STATIC)
    if not built:
        skip |= BUILT
    deferred = {t for t, _, _, _, _, _ in proj.deferred}

    def keep(rule, task):
        return rule not in skip and (built or rule != "R9" or task not in deferred)
    want = sorted((f["rule"], f.get("task"), f.get("file"), f.get("gate")) for f in findings
                  if keep(f["rule"], f.get("task")))
    got = sorted(x for x in proj.findings if keep(x[0], x[1]))
    if want != got:
        problems.append("%s: findings differ\n  got  %s\n  want %s" % (name, got, want))
    errors = [f for f in findings if f["rule"] not in LENIENT]
    if not (os.path.isdir(p) and not errors):
        return
    if "root" in exp and proj.root != exp["root"]:
        problems.append("%s: root is %s" % (name, proj.root))
    if "owner" in exp and proj.tasks[proj.root]["assignee"] != exp["owner"]:
        problems.append("%s: owner differs" % name)
    if "count" in exp:
        leaves = [t for t in proj.tasks if not proj.children(t)]
        if exp["count"] != {"tasks": len(proj.tasks), "leaves": len(leaves)}:
            problems.append("%s: count is %d/%d" % (name, len(proj.tasks), len(leaves)))
    if "order" in exp and exp["order"] != proj.order():
        problems.append("%s: order is %s" % (name, proj.order()))
    for tid, t in (exp.get("tasks") or {}).items():
        if tid not in proj.tasks:
            problems.append("%s: expected.yaml names task %s" % (name, tid))
            continue
        if "parent" in t and t["parent"] != proj.parent(tid):
            problems.append("%s/%s: parent differs" % (name, tid))
        if "authorities" in t:
            au = [proj.tasks[a]["assignee"] for a in proj.ancestors(tid)]
            if t["authorities"] != au:
                problems.append("%s/%s: authorities are %s" % (name, tid, au))
        if "applicable" in t and t["applicable"] != proj.applicable(tid):
            problems.append("%s/%s: applicable gates are %s" % (name, tid, proj.applicable(tid)))
        for r in t.get("requires") or []:
            if "subproject" in r:
                key = (tid, r["subproject"]["url"], r["subproject"]["id"])
                if key not in proj.cross and not built:
                    continue
                res = proj.cross.get(key)
                label = "%s at %s" % (key[2], key[1])
            else:
                raw = [x for x in proj.tasks[tid].get("requires") or [] if "id" in x and proj.sid(x["id"]) == r["id"]]
                res = proj.requirement(tid, {**raw[0], "id": r["id"]}) if raw else None
                label = r["id"]
            if res is None:
                problems.append("%s/%s: requirement on %s does not resolve" % (name, tid, label))
            elif (res[0], res[1], res[2], res[3], res[4]) != (r["from"], r["to"], r["met"], r["due"], r["condition"]):
                problems.append("%s/%s: requirement on %s resolves to %s" % (name, tid, label, res))


def coverage(problems):
    rules = open(os.path.join(CORPUS, "RULES.md"), encoding="utf-8").read()
    used = set()
    for name in os.listdir(ENTRIES):
        for f in load(os.path.join(ENTRIES, name, "expected.yaml")).get("findings") or []:
            used.add(f["rule"])
    for m in re.finditer(r"^\| ([A-Z]\d+)\s*\|[^\n]*?\|\s*([^|\n]*)\|\s*$", rules, re.M):
        rid, ents = m.group(1), re.findall(r"`([a-z0-9-]+)`", m.group(2))
        if rid not in used:
            problems.append("RULES.md: rule %s appears in no expected.yaml" % rid)
        for e in ents:
            if not os.path.isdir(os.path.join(ENTRIES, e)):
                problems.append("RULES.md: rule %s names entry %s, which does not exist" % (rid, e))
    return


def subtrees(d):
    """Every .tableaux the entry carries beyond project/'s own: a tree beside project/, or a
    same-repository subproject inside it."""
    out = []
    for sub in sorted(os.listdir(d)):
        sp = os.path.join(d, sub, ".tableaux")
        if sub != "project" and os.path.isdir(sp):
            out.append(sp)
    proj = os.path.join(d, "project")
    for sub in sorted(os.listdir(proj)) if os.path.isdir(proj) else []:
        sp = os.path.join(proj, sub, ".tableaux")
        if os.path.isdir(sp):
            out.append(sp)
    return out


def main():
    names = sys.argv[1:] or sorted(os.listdir(ENTRIES))
    problems = []
    for n in names:
        exp, proj = check_entry(n, problems)
        d = os.path.join(ENTRIES, n)
        for sp in subtrees(d):                 # a subproject tree the entry carries must validate too
            for msg in schema_problems(sp):
                problems.append("%s: schema: %s" % (n, msg))
        if proj is None:
            continue
        built = check_history(n, exp, proj, problems)
        compare(n, exp, proj, built, problems)
    if not sys.argv[1:]:
        coverage(problems)
    for p in problems:
        print("problem:", p)
    print("%d entries checked, %d problems" % (len(names), len(problems)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

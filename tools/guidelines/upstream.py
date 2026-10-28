"""Which commit of Odoo's skills the guidelines come from, and what changed since."""

from __future__ import annotations

import subprocess
from pathlib import Path

from .constants import UPSTREAM, UPSTREAM_FOLDER


class UpstreamClone:
    """An odoo/odoo clone holding the 20.0 branch, read through `git`."""

    def __init__(self, path: Path, ref: str) -> None:
        self.path = path
        self.ref = ref

    def git(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        command = ("git", "-C", str(self.path), *arguments)
        return subprocess.run(command, capture_output=True, text=True, check=False)

    def resolve(self, name: str) -> str:
        return self.git("rev-parse", "--verify", "--quiet", name).stdout.strip()

    def commit(self) -> str:
        return self.resolve(f"{self.ref}^{{commit}}")

    def tree(self) -> str:
        return self.resolve(f"{self.ref}:{UPSTREAM_FOLDER}")

    def commits_since(self, commit: str) -> str:
        span = f"{commit}..{self.ref}"
        return self.git("log", "--format=%h %ad %s", "--date=short", span, "--", UPSTREAM_FOLDER).stdout


class UpstreamRecord:
    """`tools/guidelines/UPSTREAM`: two lines, `commit <hash>` and `skills <tree hash>`."""

    def __init__(self, path: Path = UPSTREAM) -> None:
        self.path = path

    def read(self) -> dict[str, str]:
        lines = self.path.read_text(encoding="utf-8").splitlines()
        return dict(line.split(" ", 1) for line in lines if line)

    def write(self, clone: UpstreamClone) -> None:
        self.path.write_text(f"commit {clone.commit()}\nskills {clone.tree()}\n", encoding="utf-8")

    def report(self, clone: UpstreamClone) -> str:
        """What changed in `skills/` between the recorded commit and the clone's ref."""
        recorded = self.read()
        if recorded["skills"] == clone.tree():
            return f"up to date with {clone.ref} ({clone.commit()[:12]})"
        if not clone.resolve(f"{recorded['commit']}^{{commit}}"):
            return (
                f"skills/ changed since {recorded['commit'][:12]}, which this clone does not have:"
                " deepen it (git fetch --shallow-since=<date>) to list the commits"
            )
        return f"skills/ changed since {recorded['commit'][:12]}:\n" + clone.commits_since(recorded["commit"])

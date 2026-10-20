"""A file of a guideline skill: a Markdown template, filled in for one version."""

from __future__ import annotations

from pathlib import Path
from string import Template

from .constants import TEMPLATES
from .version import OdooVersion


class Document:
    """Subclasses name the file they write, and give the values that differ per version.

    The template is `templates/<path>`: plain Markdown where `$name` (or `${name}`) is
    replaced by `values()[name]`, and `$$` stands for a literal dollar sign. A subclass
    whose text comes from Odoo's own skills overrides `render` instead.
    """

    path = ""

    def __init__(self, upstream: Path) -> None:
        self.upstream = upstream

    def template(self, version: OdooVersion) -> Path:
        return TEMPLATES / self.path

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {"version": version.name, "translate": version.translate}

    def render(self, version: OdooVersion) -> str:
        text = self.template(version).read_text(encoding="utf-8")
        return Template(text).substitute(self.values(version))

    def read_upstream(self, relative: str) -> str:
        """A file of Odoo's 20.0 skills, as it is."""
        return (self.upstream / relative).read_text(encoding="utf-8")

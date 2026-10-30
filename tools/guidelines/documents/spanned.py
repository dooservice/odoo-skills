"""A guideline whose per-version text lives in Markdown fragments next to its template."""

from __future__ import annotations

from pathlib import Path
from string import Template

from ..constants import TEMPLATES
from ..document import Document
from ..version import OdooVersion


class SectionList:
    """The headings of a rendered guideline, one bullet each, skipping fenced code."""

    def __init__(self, text: str) -> None:
        self.text = text

    def markdown(self) -> str:
        headings = []
        fenced = False
        for line in self.text.splitlines():
            if line.lstrip().startswith("```"):
                fenced = not fenced
            elif not fenced and line.startswith("# "):
                headings.append("- " + line.removeprefix("# "))
        return "\n".join(headings)


class SpannedDocument(Document):
    """The template `templates/<path>` with its values read from the folder named after it.

    `guidelines/owl.md` reads `guidelines/owl/`, where `props.v16_19.md` is the value of
    `$props` from 16.0 to 19.0 and `props.v20.md` its value in 20.0: the part of a name
    after the first dot is a span as `OdooVersion.pick` takes it. A fragment is inserted
    as it is, so a dollar sign in it is written once, not as `$$`. Each name must have
    exactly one fragment for every version.

    Every template opens with `$essentials` (a fragment: the names that matter most in
    that version) and `$sections`, the list of the file's headings, built from the
    rendered file so that it always matches it.
    """

    def fragments(self) -> Path:
        return (TEMPLATES / self.path).with_suffix("")

    def values(self, version: OdooVersion) -> dict[str, str]:
        values = super().values(version)
        for fragment in sorted(self.fragments().glob("*.md")):
            name, span = fragment.stem.split(".", 1)
            if not version.within(span.removeprefix("v")):
                continue
            if name in values:
                raise ValueError(f"two fragments of ${name} for {version.name} in {self.fragments()}")
            values[name] = fragment.read_text(encoding="utf-8").rstrip("\n")
        return values

    def render(self, version: OdooVersion) -> str:
        template = Template(self.template(version).read_text(encoding="utf-8"))
        values = self.values(version)
        draft = template.substitute(values, sections="")
        return template.substitute(values, sections=SectionList(draft).markdown())

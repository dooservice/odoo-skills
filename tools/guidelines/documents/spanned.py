"""A guideline whose per-version text lives in Markdown fragments next to its template."""

from __future__ import annotations

from pathlib import Path

from ..constants import TEMPLATES
from ..document import Document
from ..version import OdooVersion


class SpannedDocument(Document):
    """The template `templates/<path>` with its values read from the folder named after it.

    `guidelines/owl.md` reads `guidelines/owl/`, where `props.v16_19.md` is the value of
    `$props` from 16.0 to 19.0 and `props.v20.md` its value in 20.0: the part of a name
    after the first dot is a span as `OdooVersion.pick` takes it. A fragment is inserted
    as it is, so a dollar sign in it is written once, not as `$$`. Each name must have
    exactly one fragment for every version.
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

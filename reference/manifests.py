"""The addons of one Odoo checkout, each with its manifest read and its files listed."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Addon:
    name: str
    path: Path
    manifest: dict

    @property
    def title(self) -> str:
        return str(self.manifest.get("name", self.name))

    @property
    def depends(self) -> list[str]:
        return list(self.manifest.get("depends", []))

    @property
    def data_files(self) -> list[Path]:
        """What the addon loads on install, demo data left out."""
        return [self.path / name for name in self.manifest.get("data", []) if str(name).endswith(".xml")]

    @property
    def python_files(self) -> list[Path]:
        return sorted(
            path for path in self.path.rglob("*.py")
            if "tests" not in path.relative_to(self.path).parts and "migrations" not in path.parts
        )


class Addons:
    """Every addon with a manifest under `addons/` and `odoo/addons/`, by name."""

    def __init__(self, source: Path) -> None:
        self.source = source

    def all(self) -> list[Addon]:
        found = []
        for folder in (self.source / "odoo" / "addons", self.source / "addons"):
            for manifest in sorted(folder.glob("*/__manifest__.py")):
                found.append(Addon(manifest.parent.name, manifest.parent, self.read(manifest)))
        return found

    @staticmethod
    def read(manifest: Path) -> dict:
        try:
            return ast.literal_eval(manifest.read_text(encoding="utf-8"))
        except (ValueError, SyntaxError):
            return {}

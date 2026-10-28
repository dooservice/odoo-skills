"""The two hand-written data files: which recipe covers which modules, and the technical modules."""

from __future__ import annotations

import tomllib
from pathlib import Path


class RecipeMap:
    """`recipes.toml`: each recipe, by file name without `.md`, with the modules whose flow it describes."""

    def __init__(self, path: Path, recipes_folder: Path) -> None:
        self.recipes: dict[str, list[str]] = tomllib.loads(path.read_text(encoding="utf-8"))["recipes"]
        self.recipes_folder = recipes_folder

    def recipes_of(self, module: str) -> list[str]:
        return [recipe for recipe, modules in self.recipes.items() if module in modules]

    def modules(self) -> set[str]:
        return {module for modules in self.recipes.values() for module in modules}

    def problems(self, known: set[str]) -> list[str]:
        on_disk = {path.stem for path in self.recipes_folder.glob("*.md")}
        found = [f"recipes.toml: no entry for recipe {name}.md" for name in sorted(on_disk - set(self.recipes))]
        found += [f"recipes.toml: {name}.md is not a recipe" for name in sorted(set(self.recipes) - on_disk)]
        return found + [f"recipes.toml: no addon named {name}" for name in sorted(self.modules() - known)]


class TechnicalList:
    """`technical.toml`: each module with no flow of its own, with the reason."""

    def __init__(self, path: Path) -> None:
        self.reasons: dict[str, str] = tomllib.loads(path.read_text(encoding="utf-8"))["technical"]

    def reason_of(self, module: str) -> str:
        return self.reasons.get(module, "")

    def problems(self, known: set[str], covered: set[str]) -> list[str]:
        found = [f"technical.toml: no addon named {name}" for name in sorted(set(self.reasons) - known)]
        found += [f"technical.toml: {name} is also covered by a recipe" for name in sorted(set(self.reasons) & covered)]
        return found + [f"technical.toml: {name} has no reason" for name, reason in self.reasons.items() if not reason]

"""What coverage found for one version: each module's status and each framework category."""

from __future__ import annotations

from dataclasses import dataclass

from reference.manifests import Addon

from .constants import MISSING


@dataclass(frozen=True)
class ModuleCoverage:
    addon: Addon
    status: str
    detail: str

    @property
    def app(self) -> str:
        return str(self.addon.manifest.get("category") or "Uncategorized")

    @property
    def summary(self) -> str:
        text = str(self.addon.manifest.get("summary") or self.addon.title)
        return " ".join(text.split())


@dataclass(frozen=True)
class ItemsCoverage:
    title: str
    covered: list[str]
    missing: list[str]


@dataclass(frozen=True)
class VersionCoverage:
    version: str
    modules: list[ModuleCoverage]
    categories: list[ItemsCoverage]

    def modules_with(self, status: str) -> list[ModuleCoverage]:
        return [module for module in self.modules if module.status == status]

    def missing_count(self) -> int:
        return len(self.modules_with(MISSING)) + sum(len(category.missing) for category in self.categories)

"""Measures every version, checks the data files, and writes or checks `COVERAGE.md`."""

from __future__ import annotations

from reference.constants import SKIPPED_PREFIXES, VERSIONS
from reference.manifests import Addon, Addons

from .constants import (
    RECIPES_FILE,
    RECIPES_FOLDER,
    REPORT_FILE,
    REPOSITORY,
    SOURCES,
    TECHNICAL_FILE,
)
from .declared import RecipeMap, TechnicalList
from .guidelines import GuidelineText
from .inventory import DevelopmentInventory, FunctionalInventory
from .report import CoverageReport
from .results import VersionCoverage


class CoverageBuild:
    def __init__(self) -> None:
        self.recipes = RecipeMap(RECIPES_FILE, RECIPES_FOLDER)
        self.technical = TechnicalList(TECHNICAL_FILE)
        self.functional = FunctionalInventory(self.recipes, self.technical)
        self.development = DevelopmentInventory()
        self.addons = {version: self.addons_of(version) for version in VERSIONS}

    @staticmethod
    def addons_of(version: str) -> list[Addon]:
        return [addon for addon in Addons(SOURCES / version).all() if not addon.name.startswith(SKIPPED_PREFIXES)]

    def problems(self) -> list[str]:
        known = {addon.name for addons in self.addons.values() for addon in addons}
        return self.recipes.problems(known) + self.technical.problems(known, self.recipes.modules())

    def measure(self, version: str) -> VersionCoverage:
        text = GuidelineText(REPOSITORY / "odoo" / version)
        modules = self.functional.classify(self.addons[version])
        return VersionCoverage(version, modules, self.development.measure(SOURCES / version, text))

    def run(self, check: bool) -> str:
        """Writes the report, or with `check` only measures; returns why it fails, or nothing."""
        if problems := self.problems():
            return "\n".join(problems)
        results = [self.measure(version) for version in VERSIONS]
        if not check:
            REPORT_FILE.write_text(CoverageReport(results).markdown(), encoding="utf-8")
        for result in results:
            print(result.version, "missing:", result.missing_count())
        missing = sum(result.missing_count() for result in results)
        return f"coverage is incomplete: {missing} items missing, see COVERAGE.md" if check and missing else ""

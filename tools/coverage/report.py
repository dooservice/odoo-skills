"""`COVERAGE.md`: the summary of every version, then what each version is missing."""

from __future__ import annotations

from .constants import COVERED, INTRODUCTION, MISSING, TECHNICAL
from .results import VersionCoverage


class SummaryTables:
    def __init__(self, results: list[VersionCoverage]) -> None:
        self.results = results

    def markdown(self) -> list[str]:
        lines = ["## Summary", "", "| Version | Modules | Covered | Technical | Missing |", "|---|---|---|---|---|"]
        for result in self.results:
            counts = [len(result.modules_with(status)) for status in (COVERED, TECHNICAL, MISSING)]
            lines.append(f"| {result.version} | {len(result.modules)} | " + " | ".join(map(str, counts)) + " |")
        versions = [result.version for result in self.results]
        lines += ["", "Framework items covered, of those in the version:", ""]
        lines += ["| Category | " + " | ".join(versions) + " |", "|---" * (len(versions) + 1) + "|"]
        for index, category in enumerate(self.results[0].categories):
            cells = [self.ratio(result, index) for result in self.results]
            lines.append(f"| {category.title} | " + " | ".join(cells) + " |")
        return lines + [""]

    @staticmethod
    def ratio(result: VersionCoverage, index: int) -> str:
        category = result.categories[index]
        return f"{len(category.covered)}/{len(category.covered) + len(category.missing)}"


class VersionSection:
    def __init__(self, result: VersionCoverage) -> None:
        self.result = result

    def markdown(self) -> list[str]:
        missing = sorted(self.result.modules_with(MISSING), key=lambda module: (module.app, module.addon.name))
        lines = [f"## {self.result.version}", "", f"### Missing modules ({len(missing)})", ""]
        if missing:
            lines += ["| App | Module | Summary |", "|---|---|---|"]
            lines += [f"| {module.app} | `{module.addon.name}` | {module.summary} |" for module in missing]
        lines += ["", "### Missing framework items", ""]
        for category in self.result.categories:
            names = ", ".join(f"`{name}`" for name in category.missing) or "none"
            lines.append(f"- **{category.title}** ({len(category.missing)}): {names}")
        return lines + [""]


class CoverageReport:
    def __init__(self, results: list[VersionCoverage]) -> None:
        self.results = results

    def markdown(self) -> str:
        lines = [INTRODUCTION] + SummaryTables(self.results).markdown()
        for result in self.results:
            lines += VersionSection(result).markdown()
        return "\n".join(lines).rstrip("\n") + "\n"

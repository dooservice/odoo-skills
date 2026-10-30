"""Prints the biggest measures and every one over its budget."""

from __future__ import annotations

from .constants import TABLE_ROWS
from .measure import Measure


class BudgetTable:
    """A plain text table of sizes against limits."""

    def __init__(self, measures: list[Measure]) -> None:
        self.measures = sorted(measures, key=lambda measure: measure.size, reverse=True)

    def exceeded(self) -> list[Measure]:
        return [measure for measure in self.measures if measure.exceeded]

    def row(self, measure: Measure) -> str:
        status = "OVER" if measure.exceeded else "ok"
        return (
            f"{measure.size:>7} {measure.tokens:>6} {measure.limit:>7} {status:>4}  "
            f"{measure.label}"
        )

    def header(self) -> str:
        return f"{'chars':>7} {'tokens':>6} {'limit':>7} {'':>4}  file"

    def render(self) -> str:
        lines = [f"Biggest {TABLE_ROWS} of {len(self.measures)}:", self.header()]
        lines += [self.row(measure) for measure in self.measures[:TABLE_ROWS]]
        if self.exceeded():
            lines += ["", f"Over budget: {len(self.exceeded())}", self.header()]
            lines += [self.row(measure) for measure in self.exceeded()]
        return "\n".join(lines)

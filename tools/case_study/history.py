"""The runs kept in `evals/history/`: one suite of one model on one Odoo version and skills stage."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass

from .constants import CODE_PREFIX, HISTORY_FOLDER


@dataclass(frozen=True)
class Run:
    stage: str
    model: str
    odoo: str
    cost: float
    runs: int
    cases: list[dict]

    def average(self, key: str, prefix: str = "") -> float:
        """The mean of one field over the tasks whose name starts with the prefix; NaN when no task has it."""
        values = [case[key] for case in self.cases if case["name"].startswith(prefix) and key in case]
        return sum(values) / len(values) if values else math.nan

    def added_context(self) -> float:
        """The mean context per task the skills add: input and cache tokens with, minus without."""
        return self.average("context_with") - self.average("context_without")

    def suite_cost(self, runs: int) -> float:
        """What the suite would cost at the given runs per task."""
        return self.cost * runs / self.runs

    def percent(self, key: str, prefix: str = "") -> float:
        return 100 * self.average(key, prefix)

    def kind_percent(self, key: str, code: bool) -> float:
        """The score of the code tasks, or of the functional ones."""
        values = [case[key] for case in self.cases if case["name"].startswith(CODE_PREFIX) == code]
        return 100 * sum(values) / len(values)

    def task(self, name: str) -> dict:
        return next(case for case in self.cases if case["name"] == name)


class History:
    """Every run of the history folder, looked up by stage, model and Odoo version."""

    def __init__(self) -> None:
        self.runs = [self.load(path.read_text()) for path in sorted(HISTORY_FOLDER.glob("*.json"))]

    def load(self, text: str) -> Run:
        data = json.loads(text)
        return Run(data["skills"], data["model"], data["odoo"], data["cost_usd"], data["runs_per_case"],
                   data["cases"])

    def find(self, stage: str, model: str, odoo: str) -> Run | None:
        matches = [run for run in self.runs if (run.stage, run.model, run.odoo) == (stage, model, odoo)]
        return matches[0] if matches else None

    def of_stage(self, stage: str, model: str) -> list[Run]:
        return [run for run in self.runs if run.stage == stage and run.model == model]

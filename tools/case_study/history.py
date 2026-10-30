"""The runs kept in `evals/history/`: one suite of one model on one Odoo version and skills stage."""

from __future__ import annotations

import json
from dataclasses import dataclass

from .constants import CODE_PREFIX, HISTORY_FOLDER


@dataclass(frozen=True)
class Run:
    stage: str
    model: str
    odoo: str
    cost: float
    cases: list[dict]

    def average(self, key: str, prefix: str = "") -> float:
        """The mean of one field over the tasks whose name starts with the prefix."""
        values = [case[key] for case in self.cases if case["name"].startswith(prefix)]
        return sum(values) / len(values)

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
        return Run(data["skills"], data["model"], data["odoo"], data["cost_usd"], data["cases"])

    def find(self, stage: str, model: str, odoo: str) -> Run | None:
        matches = [run for run in self.runs if (run.stage, run.model, run.odoo) == (stage, model, odoo)]
        return matches[0] if matches else None

    def of_stage(self, stage: str, model: str) -> list[Run]:
        return [run for run in self.runs if run.stage == stage and run.model == model]

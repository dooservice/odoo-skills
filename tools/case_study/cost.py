"""Chart 5: what one suite costs by model and stage, and what all measurements cost together."""

from __future__ import annotations

import math
from itertools import accumulate

from .canvas import Canvas
from .constants import MODEL_COLORS, MODELS, SPENDING, STAGES, SUITE_RUNS
from .history import History


class CostChart:
    file_name = "5-cost.png"

    def __init__(self, history: History) -> None:
        self.history = history

    def suite_costs(self, model: str) -> list[float]:
        """The mean cost of one suite at three runs per task, both sides included, at each stage."""
        costs = []
        for stage in STAGES:
            runs = self.history.of_stage(stage, model)
            costs.append(sum(run.suite_cost(SUITE_RUNS) for run in runs) / len(runs) if runs else math.nan)
        return costs

    def draw(self) -> None:
        canvas = Canvas("What measuring cost (USD)", columns=2, share=False)
        suites, total = canvas.panels
        width = 0.38
        for offset, (model, name) in enumerate(MODELS.items()):
            positions = [index + (offset - 0.5) * width for index in range(len(STAGES))]
            bars = suites.bar(positions, self.suite_costs(model), width * 0.92,
                              color=MODEL_COLORS[model][3], label=name)
            canvas.label(suites, bars, "{:.2f}")
        suites.set_xticks(range(len(STAGES)), list(STAGES.values()), rotation=25, ha="right")
        suites.set_ylabel("USD per suite")
        suites.set_title("One suite at three runs per task, mean over versions", fontsize=12)
        suites.legend(loc="center left")
        names = [entry[0] for entry in SPENDING]
        running = list(accumulate(entry[1] for entry in SPENDING))
        positions = list(range(len(names)))
        total.plot(positions, running, color="#2b2b29", marker="o", linewidth=2)
        total.annotate(f"about {running[-1]:.1f} USD", (positions[-1], running[-1]), textcoords="offset points",
                       xytext=(-6, 10), ha="right", fontweight="bold")
        total.set_xticks(positions, names, rotation=55, ha="right", fontsize=8)
        total.set_ylim(0, 105)
        total.set_ylabel("Cumulative USD")
        total.set_title("Every measurement, in order", fontsize=13)
        canvas.note("Costs are what the API charged. The first point (2026-10-20) is rounded to about 14 USD "
                    "and includes development runs. Five-run suites are scaled to three runs.")
        canvas.save(self.file_name)

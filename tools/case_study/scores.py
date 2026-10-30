"""Chart 1: the score with the skills on each Odoo version, at each skills stage, one panel per model."""

from __future__ import annotations

import math

from .canvas import Canvas
from .constants import (
    FIRST_RELEASE,
    MODEL_COLORS,
    MODELS,
    STAGES,
    VERSIONS,
    WITHOUT_COLOR,
)
from .history import History


class ScoresChart:
    file_name = "1-scores-by-version.png"

    def __init__(self, history: History) -> None:
        self.history = history

    def stage_scores(self, stage: str, model: str, key: str) -> list[float]:
        runs = [self.history.find(stage, model, version) for version in VERSIONS]
        return [run.percent(key) if run else float("nan") for run in runs]

    def draw(self) -> None:
        canvas = Canvas("Score with the skills, by Odoo version and skills release", columns=2)
        positions = list(range(len(VERSIONS)))
        for panel, model in zip(canvas.panels, MODELS, strict=True):
            colors = MODEL_COLORS[model]
            without = self.stage_scores("1.1.0", model, "score_without")
            panel.plot(positions, without, color=WITHOUT_COLOR, linestyle="--", marker="o", label="without skills")
            if model.endswith("sonnet-5-5"):
                first = [FIRST_RELEASE[version][0] for version in VERSIONS]
                panel.plot(positions, first, color=colors[0], marker="o", label="1.0.0")
            for index, (stage, title) in enumerate(STAGES.items(), start=1):
                scores = self.stage_scores(stage, model, "score")
                panel.plot(positions, scores, color=colors[index], marker="o", linewidth=2, label=title)
            final = self.stage_scores("1.1.1", model, "score")
            for position, value in zip(positions, final, strict=True):
                if not math.isnan(value):
                    panel.annotate(f"{value:.0f}%", (position, value), textcoords="offset points",
                                   xytext=(0, 8), ha="center", fontsize=9, fontweight="bold")
            panel.set_title(MODELS[model], fontsize=13)
            panel.set_xticks(positions, [f"Odoo {version}" for version in VERSIONS])
            panel.set_ylim(50, 104)
            panel.set_ylabel("Graders passed (%)")
            panel.legend(loc="lower left", fontsize=9)
        canvas.note("Three runs per task. Without skills: the 1.1.0 run. 1.0.0 was measured with Sonnet only. "
                    "Sonnet 17.0 to 19.0 was not re-measured after reaching 100% on 1.1.0.")
        canvas.save(self.file_name)

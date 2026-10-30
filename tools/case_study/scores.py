"""Chart 1: the score with the skills on each Odoo version, at each skills stage, one panel per model."""

from __future__ import annotations

import math

from .canvas import Canvas
from .constants import (
    DOTTED_STAGES,
    FIRST_RELEASE,
    MODEL_COLORS,
    MODELS,
    STAGE_SHADES,
    STAGES,
    VERSIONS,
    WITHOUT_COLOR,
)
from .history import History


class ScoresChart:
    file_name = "1-scores-by-version.png"
    final = "2.0.0"

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
            for stage, title in STAGES.items():
                scores = self.stage_scores(stage, model, "score")
                style = ":" if stage in DOTTED_STAGES else "-"
                width = 3 if stage == self.final else 1.6
                panel.plot(positions, scores, color=colors[STAGE_SHADES[stage]], marker="o", linewidth=width,
                           linestyle=style, label=title)
            for position, value in zip(positions, self.stage_scores(self.final, model, "score"), strict=True):
                if not math.isnan(value):
                    panel.annotate(f"{value:.0f}%", (position, value), textcoords="offset points",
                                   xytext=(0, 8), ha="center", fontsize=9, fontweight="bold")
            panel.set_title(MODELS[model], fontsize=13)
            panel.set_xticks(positions, [f"Odoo {version}" for version in VERSIONS])
            panel.set_ylim(50, 104)
            panel.set_ylabel("Graders passed (%)")
            panel.legend(loc="lower left", fontsize=9)
        canvas.note("Three runs per task; 2.0.0 Haiku five. Without skills: the 1.1.0 run. Labels: 2.0.0. "
                    "1.0.0 was measured with Sonnet only; Sonnet 2.0.0 on 20.0 only.")
        canvas.save(self.file_name)

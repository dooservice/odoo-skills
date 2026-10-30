"""Chart 6: the turns an agent takes per task, without and with the skills, one panel per model."""

from __future__ import annotations

from .canvas import Canvas
from .constants import MODEL_COLORS, MODELS, VERSIONS, WITHOUT_COLOR
from .history import History


class TurnsChart:
    file_name = "6-turns-per-task.png"

    def __init__(self, history: History) -> None:
        self.history = history

    def series(self, stage: str, model: str, key: str) -> list[float]:
        runs = [self.history.find(stage, model, version) for version in VERSIONS]
        return [run.average(key) if run else float("nan") for run in runs]

    def draw(self) -> None:
        canvas = Canvas("Average turns per task: reading the skills costs a few turns", columns=2)
        width = 0.2
        for panel, model in zip(canvas.panels, MODELS, strict=True):
            colors = MODEL_COLORS[model]
            bars = (
                ("without skills", self.series("1.1.0", model, "turns_without"), WITHOUT_COLOR),
                ("with 1.1.0", self.series("1.1.0", model, "turns_with"), colors[1]),
                ("with 1.1.1", self.series("1.1.1", model, "turns_with"), colors[3]),
                ("with 2.0.0", self.series("2.0.0", model, "turns_with"), colors[4]),
            )
            for offset, (title, values, color) in enumerate(bars):
                positions = [index + (offset - 1.5) * width for index in range(len(VERSIONS))]
                drawn = panel.bar(positions, values, width * 0.92, color=color, label=title)
                canvas.label(panel, drawn, "{:.1f}")
            panel.set_xticks(range(len(VERSIONS)), VERSIONS)
            panel.set_xlabel("Odoo version")
            panel.set_ylabel("Turns per task (mean over runs)")
            panel.set_title(MODELS[model], fontsize=13)
            panel.legend(loc="upper left", fontsize=9)
        canvas.note("Without skills: the 1.1.0 run. Sonnet was measured on 1.1.1 on 16.0 and 20.0 only, on 2.0.0 "
                    "on 20.0 only. Each task allows 15 turns.")
        canvas.save(self.file_name)

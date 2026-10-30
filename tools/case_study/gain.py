"""Chart 2: points gained over no skills, per Odoo version and model, on 1.1.0 and 1.1.1."""

from __future__ import annotations

from .canvas import Canvas
from .constants import MODEL_COLORS, MODELS, VERSIONS
from .history import History


class GainChart:
    file_name = "2-gain-over-no-skills.png"
    stages = (("1.1.0", 1), ("1.1.1", 3))

    def __init__(self, history: History) -> None:
        self.history = history

    def gains(self, stage: str, model: str) -> list[float]:
        runs = [self.history.find(stage, model, version) for version in VERSIONS]
        return [run.percent("score") - run.percent("score_without") if run else float("nan") for run in runs]

    def draw(self) -> None:
        canvas = Canvas("Points gained over the same model without skills")
        panel = canvas.panels[0]
        width = 0.2
        offset = -1.5
        for model, name in MODELS.items():
            for stage, shade in self.stages:
                positions = [index + offset * width for index in range(len(VERSIONS))]
                bars = panel.bar(positions, self.gains(stage, model), width * 0.92,
                                 color=MODEL_COLORS[model][shade], label=f"{name}, {stage}")
                canvas.label(panel, bars, "{:+.1f}")
                offset += 1
        panel.axhline(0, color="#2b2b29", linewidth=0.8)
        panel.set_xticks(range(len(VERSIONS)), [f"Odoo {version}" for version in VERSIONS])
        panel.set_ylabel("Points (with minus without)")
        panel.legend(loc="upper left", fontsize=10)
        canvas.note("Both sides from the same run. Sonnet was measured on 1.1.1 only on 16.0 and 20.0 "
                    "(no bar on 17.0 to 19.0).")
        canvas.save(self.file_name)

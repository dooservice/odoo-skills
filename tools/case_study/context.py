"""Chart 8: the context the skills add per task on each Odoo version, before and after the layers of 2.0.0."""

from __future__ import annotations

from .canvas import Canvas
from .constants import CONTEXT_STAGES, MODEL_COLORS, STAGE_SHADES, STAGES, VERSIONS
from .history import History


class ContextChart:
    file_name = "8-context-per-version.png"
    model = "claude-haiku-5-5"
    width = 0.38

    def __init__(self, history: History) -> None:
        self.history = history

    def added(self, stage: str) -> list[float]:
        """Thousands of tokens the skills add per task, one per Odoo version."""
        return [self.history.find(stage, self.model, version).added_context() / 1000 for version in VERSIONS]

    def draw(self) -> None:
        canvas = Canvas("Context the skills add per task, Haiku 5.5 (thousands of tokens)")
        panel = canvas.panels[0]
        series = [self.added(stage) for stage in CONTEXT_STAGES]
        for offset, (stage, values) in enumerate(zip(CONTEXT_STAGES, series, strict=True)):
            positions = [index + (offset - 0.5) * self.width for index in range(len(VERSIONS))]
            bars = panel.bar(positions, values, self.width * 0.92, label=STAGES[stage],
                             color=MODEL_COLORS[self.model][STAGE_SHADES[stage]])
            canvas.label(panel, bars, "{:.1f}k")
        for index, (old, new) in enumerate(zip(*series, strict=True)):
            panel.annotate(f"{100 * (new - old) / old:+.0f}%", (index, max(old, new)), textcoords="offset points",
                           xytext=(0, 22), ha="center", fontsize=12, fontweight="bold")
        panel.set_xticks(range(len(VERSIONS)), [f"Odoo {version}" for version in VERSIONS])
        panel.set_ylim(0, 100)
        panel.set_ylabel("Input and cache tokens, with minus without")
        panel.legend(loc="upper left", fontsize=10)
        total = [sum(values) for values in series]
        canvas.note(f"Mean per task. All versions: {total[0]:.1f}k to {total[1]:.1f}k "
                    f"({100 * (total[1] - total[0]) / total[0]:+.0f}%). 1.1.1 rerun: three runs per task; "
                    "2.0.0: five.")
        canvas.save(self.file_name)

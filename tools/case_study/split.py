"""Chart 3: code and functional tasks, without and with the 1.1.1 skills, one panel per model."""

from __future__ import annotations

from .canvas import Canvas
from .constants import MODEL_COLORS, MODELS, VERSIONS, WITHOUT_COLOR
from .history import History


class SplitChart:
    file_name = "3-code-and-functional.png"

    def __init__(self, history: History) -> None:
        self.history = history

    def rows(self, model: str) -> list[tuple[str, float, float]]:
        """One row per measured version and kind of task: its name, the score without and with."""
        rows = []
        for version in reversed(VERSIONS):
            run = self.history.find("1.1.1", model, version)
            if run:
                for code, kind in ((True, "code"), (False, "functional")):
                    rows.append((f"{version} {kind}", run.kind_percent("score_without", code),
                                 run.kind_percent("score", code)))
        return list(reversed(rows))

    def draw(self) -> None:
        canvas = Canvas("Code and functional tasks, without and with the 1.1.1 skills", columns=2,
                        share=False, grid="x")
        for panel, model in zip(canvas.panels, MODELS, strict=True):
            rows = self.rows(model)
            color = MODEL_COLORS[model][2]
            for position, (name, without, with_skills) in enumerate(rows):
                panel.plot([without, with_skills], [position, position], color="#cfcec9", linewidth=3, zorder=1)
                panel.scatter([without], [position], color=WITHOUT_COLOR, s=70, zorder=2)
                panel.scatter([with_skills], [position], color=color, s=70, zorder=3)
                panel.annotate(f"{with_skills:.0f}%", (with_skills, position), textcoords="offset points",
                               xytext=(8, -4), fontsize=9)
                panel.annotate(f"{without:.0f}%", (without, position), textcoords="offset points",
                               xytext=(-10, -4), ha="right", fontsize=9, color="#6b6a65")
            panel.set_yticks(range(len(rows)), [row[0] for row in rows])
            panel.set_xlim(35, 110)
            panel.set_xlabel("Graders passed (%)")
            panel.set_title(f"{MODELS[model]}: grey without, color with", fontsize=13)
        canvas.note("Sonnet was measured on 1.1.1 on 16.0 and 20.0 only.")
        canvas.save(self.file_name)

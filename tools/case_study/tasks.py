"""Chart 4: Haiku on Odoo 20.0, task by task, without skills and with each skills stage."""

from __future__ import annotations

from .canvas import Canvas
from .constants import STAGES
from .history import History


class TasksChart:
    file_name = "4-haiku-20-tasks.png"
    model = "claude-haiku-5-5"
    odoo = "20.0"

    def __init__(self, history: History) -> None:
        self.history = history

    def draw(self) -> None:
        runs = [self.history.find(stage, self.model, self.odoo) for stage in STAGES]
        names = [case["name"] for case in runs[0].cases]
        columns = ["without skills", *[f"with {title}" for title in STAGES.values()]]
        grid = [[runs[0].task(name)["score_without"], *[run.task(name)["score"] for run in runs]]
                for name in names]
        canvas = Canvas("Haiku 5.5 on Odoo 20.0: share of graders passed, task by task")
        panel = canvas.panels[0]
        panel.imshow(grid, cmap="Blues", vmin=0, vmax=1.15, aspect="auto")
        for row, values in enumerate(grid):
            for column, value in enumerate(values):
                shade = "white" if value > 0.7 else "#2b2b29"
                panel.text(column, row, f"{100 * value:.0f}", ha="center", va="center", fontsize=9, color=shade)
        panel.set_xticks(range(len(columns)), columns)
        panel.xaxis.tick_top()
        panel.set_yticks(range(len(names)), names, fontsize=9)
        panel.grid(visible=False)
        panel.tick_params(length=0)
        for side in panel.spines.values():
            side.set_visible(False)
        canvas.note("Percent of graders passed over three runs, five on 2.0.0. Without skills: the 1.1.0 run. "
                    "The 1.1.1 rerun measured the same skills again.")
        canvas.save(self.file_name)

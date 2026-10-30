"""Draws every chart of the case study."""

from __future__ import annotations

from .cost import CostChart
from .gain import GainChart
from .history import History
from .layers import LayersChart
from .scores import ScoresChart
from .split import SplitChart
from .tasks import TasksChart
from .turns import TurnsChart


class CaseStudyBuild:
    def run(self) -> None:
        history = History()
        charts = [
            ScoresChart(history),
            GainChart(history),
            SplitChart(history),
            TasksChart(history),
            CostChart(history),
            TurnsChart(history),
            LayersChart(),
        ]
        for chart in charts:
            chart.draw()
            print("wrote", chart.file_name)

"""Draws every chart of the case study."""

from __future__ import annotations

from .context import ContextChart
from .cost import CostChart
from .gain import GainChart
from .history import History
from .layers import LayersChart
from .reads import ReadsChart
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
            ContextChart(history),
            ReadsChart(),
        ]
        for chart in charts:
            chart.draw()
            print("wrote", chart.file_name)

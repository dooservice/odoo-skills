"""The look every chart shares: size, colors, fonts, grid and how it is saved."""

from __future__ import annotations

import math

import matplotlib
from matplotlib.figure import Figure

from .constants import FIGURE_SIZE, GRID_COLOR, IMAGE_FOLDER, INK_COLOR, RESOLUTION


class Canvas:
    """One figure with its panels, styled alike, saved as a PNG under the image folder."""

    def __init__(self, title: str, columns: int = 1, share: bool = True, grid: str = "y") -> None:
        matplotlib.rcParams.update({
            "font.size": 11,
            "axes.edgecolor": INK_COLOR,
            "axes.labelcolor": INK_COLOR,
            "xtick.color": INK_COLOR,
            "ytick.color": INK_COLOR,
            "text.color": INK_COLOR,
            "legend.frameon": False,
        })
        self.figure = Figure(figsize=FIGURE_SIZE, facecolor="white")
        panels = self.figure.subplots(1, columns, sharey=share, squeeze=False)
        self.panels = list(panels[0])
        self.figure.suptitle(title, fontsize=15, fontweight="bold", x=0.01, ha="left")
        for panel in self.panels:
            panel.set_facecolor("white")
            panel.grid(axis=grid, color=GRID_COLOR, linewidth=0.8)
            panel.set_axisbelow(True)
            panel.spines["top"].set_visible(False)
            panel.spines["right"].set_visible(False)

    def note(self, text: str) -> None:
        """A line of small print under the chart: the source, or what is estimated."""
        self.figure.text(0.01, 0.015, text, fontsize=9, color="#6b6a65", ha="left")

    def label(self, panel, bars, template: str) -> None:
        """Writes each bar's value above it."""
        panel.bar_label(bars, labels=["" if math.isnan(bar.get_height()) else template.format(bar.get_height()) for bar in bars], padding=3, fontsize=9)

    def save(self, name: str) -> None:
        IMAGE_FOLDER.mkdir(parents=True, exist_ok=True)
        self.figure.tight_layout(rect=(0, 0.04, 1, 0.95))
        self.figure.savefig(IMAGE_FOLDER / name, dpi=RESOLUTION, facecolor="white")

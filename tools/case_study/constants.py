"""Where the case study reads its data and writes its charts, and the few facts kept only as totals."""

from __future__ import annotations

from pathlib import Path

#: The repository root.
REPOSITORY = Path(__file__).resolve().parent.parent.parent
#: The per-task summary of every run since 1.1.0.
HISTORY_FOLDER = REPOSITORY / "evals" / "history"
#: Where the charts are written.
IMAGE_FOLDER = REPOSITORY / "docs" / "case-study" / "img"
#: The skills of each version.
SKILLS_FOLDER = REPOSITORY / "odoo"
#: The version whose skill sizes are drawn.
SIZE_VERSION = "20.0"
#: The Odoo versions measured, oldest first.
VERSIONS = ("16.0", "17.0", "18.0", "19.0", "20.0")
#: The models measured, as the history names them, with the name shown.
MODELS = {"claude-haiku-5-5": "Haiku 5.5", "claude-sonnet-5-5": "Sonnet 5.5"}
#: The skills versions of the history, in order, with the name shown.
STAGES = {"1.1.0": "1.1.0", "1.1.1-step-1": "1.1.1 step 1", "1.1.1": "1.1.1"}
#: Scores of 1.0.0 with Sonnet 5.5, kept only as totals: Odoo version to (with, without), in percent.
FIRST_RELEASE = {
    "16.0": (97.8, 96.3),
    "17.0": (99.6, 94.7),
    "18.0": (98.9, 95.6),
    "19.0": (97.0, 92.4),
    "20.0": (88.6, 69.2),
}
#: Every measurement in order, with what the API charged in USD and whether the total is rounded.
SPENDING = (
    ("10-20 1.0.0 Sonnet", 14.0, True),
    ("10-28 1.0.0 Sonnet", 12.35, False),
    ("10-30 1.1.0 Haiku", 1.40, False),
    ("10-30 1.1.0 Sonnet", 21.75, False),
    ("10-30 diagnosis", 0.08, False),
    ("10-30 step 1 Haiku", 1.55, False),
    ("10-30 step 1 Sonnet", 8.72, False),
    ("10-30 1.1.1 Haiku", 1.68, False),
    ("10-30 1.1.1 Sonnet", 8.75, False),
)
#: The task name prefix of tasks that write code; the others configure Odoo.
CODE_PREFIX = "code-"
#: Characters per token used for the approximate token counts.
CHARACTERS_PER_TOKEN = 4
#: The colors of each model, lightest first, one per skills stage.
MODEL_COLORS = {
    "claude-haiku-5-5": ("#a9c9f0", "#5f9ae3", "#2a78d6", "#174f94"),
    "claude-sonnet-5-5": ("#f6c0a8", "#f08f63", "#eb6834", "#a8441a"),
}
#: The color of the runs without the skills.
WITHOUT_COLOR = "#9a9993"
#: The color of the bars that belong to no model.
LAYER_COLOR = "#5d7187"
#: The color of text and axes.
INK_COLOR = "#2b2b29"
#: The color of grid lines.
GRID_COLOR = "#e4e3df"
#: The size of every chart in inches; at the resolution below it is 1650 by 900 pixels.
FIGURE_SIZE = (11.0, 6.0)
#: The resolution of every chart in dots per inch.
RESOLUTION = 150

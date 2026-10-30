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
STAGES = {
    "1.1.0": "1.1.0",
    "1.1.1-step-1": "1.1.1 step 1",
    "1.1.1": "1.1.1",
    "1.1.1-rerun": "1.1.1 rerun",
    "2.0.0": "2.0.0",
}
#: The shade of each stage in the model colors; the 1.1.1 rerun shares the shade of 1.1.1.
STAGE_SHADES = {"1.1.0": 1, "1.1.1-step-1": 2, "1.1.1": 3, "1.1.1-rerun": 3, "2.0.0": 4}
#: The stages drawn as a dotted line: the same skills measured again.
DOTTED_STAGES = ("1.1.1-rerun",)
#: The two stages whose added context is compared, before and after the layers of 2.0.0.
CONTEXT_STAGES = ("1.1.1-rerun", "2.0.0")
#: The runs per task a suite cost is scaled to, so suites of three and five runs compare.
SUITE_RUNS = 3
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
    ("10-30 1.1.1 rerun Haiku", 1.75, False),
    ("10-30 rerun, tokens lost", 1.70, False),
    ("10-30 2.0.0 step 1 Haiku", 1.67, False),
    ("10-30 traces 16.0 17.0", 0.63, False),
    ("10-30 2.0.0 trials Haiku", 4.98, False),
    ("10-30 2.0.0 Haiku", 2.67, False),
    ("10-30 services fix Haiku", 0.63, False),
    ("10-30 2.0.0 Sonnet", 7.98, False),
)
#: Approximate tokens of each layer of the 1.1.1 skills for Odoo 20.0, in the order of `SkillSizes.layers`.
LAYERS_BEFORE = (1_115, 18_930, 59_553, 192_136, 518_365)
#: What the agents read with the 2.0.0 skills over 510 Haiku runs: what, tokens, and how many times it was read.
READS = (
    ("Functional recipes", 636_948, 190),
    ("SKILL.md bodies", 349_254, 395),
    ("Grep results in the skills", 170_509, 151),
    ("odoo-guidelines topic files", 163_818, 71),
    ("odoo-web-guidelines topic files", 108_574, 58),
    ("Reference, partial reads", 27_072, 40),
)
#: The task name prefix of tasks that write code; the others configure Odoo.
CODE_PREFIX = "code-"
#: Characters per token used for the approximate token counts.
CHARACTERS_PER_TOKEN = 4
#: The colors of each model, lightest first, one per skills stage.
MODEL_COLORS = {
    "claude-haiku-5-5": ("#c6dbf5", "#93bbec", "#5f9ae3", "#2a78d6", "#0f3d75"),
    "claude-sonnet-5-5": ("#f9d3c1", "#f4ad8a", "#f08f63", "#eb6834", "#8a3412"),
}
#: The color of the runs without the skills.
WITHOUT_COLOR = "#9a9993"
#: The color of the bars that belong to no model.
LAYER_COLOR = "#5d7187"
#: The color of the 1.1.1 bars next to the layer bars.
LAYER_BEFORE_COLOR = "#b9c4d0"
#: The color of text and axes.
INK_COLOR = "#2b2b29"
#: The color of grid lines.
GRID_COLOR = "#e4e3df"
#: The size of every chart in inches; at the resolution below it is 1650 by 900 pixels.
FIGURE_SIZE = (11.0, 6.0)
#: The resolution of every chart in dots per inch.
RESOLUTION = 150

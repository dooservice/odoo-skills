"""Chart 9: what the agents read with the 2.0.0 skills, by layer, in tokens."""

from __future__ import annotations

from .canvas import Canvas
from .constants import LAYER_COLOR, READS


class ReadsChart:
    file_name = "9-what-agents-read.png"

    def draw(self) -> None:
        rows = list(reversed(READS))
        canvas = Canvas("What the agents read with the 2.0.0 skills (Haiku 5.5, 510 runs)", grid="x")
        panel = canvas.panels[0]
        positions = list(range(len(rows)))
        panel.barh(positions, [tokens / 1000 for title, tokens, reads in rows], 0.6, color=LAYER_COLOR)
        for position, (title, tokens, reads) in zip(positions, rows, strict=True):
            text = f"{tokens:,} tokens, {reads} times, ~{tokens // reads:,} each"
            panel.annotate(text, (tokens / 1000, position), textcoords="offset points", xytext=(6, -4), fontsize=10)
        panel.set_xlim(0, 1000)
        panel.set_yticks(positions, [title for title, tokens, reads in rows])
        panel.set_xlabel("Thousands of tokens read, all runs together")
        canvas.note("Tool results in the final Haiku traces of 2.0.0, five Odoo versions, five runs per task. "
                    "Descriptions are always in context and are not counted.")
        canvas.save(self.file_name)

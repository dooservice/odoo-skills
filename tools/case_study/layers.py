"""Chart 7: the size of each layer of the skills of one version, in approximate tokens."""

from __future__ import annotations

from .canvas import Canvas
from .constants import LAYER_COLOR, SIZE_VERSION
from .sizes import SkillSizes


class LayersChart:
    file_name = "7-skill-size-per-layer.png"

    def draw(self) -> None:
        layers = list(reversed(SkillSizes().layers()))
        canvas = Canvas(f"Skills for Odoo {SIZE_VERSION}: text per layer (approximate tokens)", grid="x")
        panel = canvas.panels[0]
        positions = range(len(layers))
        panel.barh(positions, [layer.tokens for layer in layers], 0.6, color=LAYER_COLOR)
        for position, layer in zip(positions, layers, strict=True):
            text = f"~{layer.tokens:,} tokens, {len(layer.texts)} files, largest ~{layer.largest:,}"
            panel.annotate(text, (layer.tokens, position), textcoords="offset points", xytext=(6, -4), fontsize=10)
        panel.set_xscale("log")
        panel.set_xlim(100, 1_000_000_000)
        panel.set_yticks(list(positions), [layer.title for layer in layers])
        panel.set_xlabel("Approximate tokens, log scale (characters / 4)")
        canvas.note("Measured from the files of odoo/20.0 and odoo/common. Tokens are approximate: characters "
                    "divided by 4.")
        canvas.save(self.file_name)

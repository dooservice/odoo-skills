"""Chart 7: the size of each layer of the skills of one version, 1.1.1 against today, in approximate tokens."""

from __future__ import annotations

from .canvas import Canvas
from .constants import LAYER_BEFORE_COLOR, LAYER_COLOR, LAYERS_BEFORE, SIZE_VERSION
from .sizes import SkillSizes


class LayersChart:
    file_name = "7-skill-size-per-layer.png"
    height = 0.38

    def draw(self) -> None:
        layers = list(reversed(SkillSizes().layers()))
        before = list(reversed(LAYERS_BEFORE))
        canvas = Canvas(f"Skills for Odoo {SIZE_VERSION}: text per layer, 1.1.1 and 2.0.0 (approximate tokens)",
                        grid="x")
        panel = canvas.panels[0]
        positions = list(range(len(layers)))
        panel.barh([position - self.height / 2 for position in positions], before, self.height * 0.92,
                   color=LAYER_BEFORE_COLOR, label="1.1.1")
        panel.barh([position + self.height / 2 for position in positions], [layer.tokens for layer in layers],
                   self.height * 0.92, color=LAYER_COLOR, label="2.0.0")
        for position, layer, old in zip(positions, layers, before, strict=True):
            panel.annotate(f"~{old:,}", (old, position - self.height / 2), textcoords="offset points",
                           xytext=(6, -4), fontsize=9, color="#6b6a65")
            text = f"~{layer.tokens:,} tokens, {len(layer.texts)} files, largest ~{layer.largest:,}"
            panel.annotate(text, (layer.tokens, position + self.height / 2), textcoords="offset points",
                           xytext=(6, -4), fontsize=10)
        panel.set_xscale("log")
        panel.set_xlim(100, 1_000_000_000)
        panel.set_yticks(positions, [layer.title for layer in layers])
        panel.set_xlabel("Approximate tokens, log scale (characters / 4)")
        panel.legend(loc="upper right", fontsize=10)
        canvas.note("Measured from the files of odoo/20.0 and odoo/common at each release. Tokens are approximate: "
                    "characters divided by 4.")
        canvas.save(self.file_name)

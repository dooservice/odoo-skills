"""The reference of one Odoo version, as plain markdown an agent can grep and read in parts."""

from __future__ import annotations

from pathlib import Path

from .manifests import Addon
from .models import Model
from .settings import Setting
from .xmlids import XmlId


class ReferenceWriter:
    def __init__(self, root: Path) -> None:
        self.root = root

    def write(self, name: str, text: str) -> None:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text.rstrip() + "\n", encoding="utf-8")

    def models(self, addon: Addon, models: list[Model]) -> None:
        lines = [f"# {addon.name} — {addon.title}", "", f"Depends on: {', '.join(addon.depends) or 'nothing'}.", ""]
        for model in models:
            verb = "extends" if model.extends else "defines"
            lines += [f"## `{model.name}` ({verb})", ""]
            if model.description:
                lines += [model.description, ""]
            if model.inherits:
                lines += [f"Inherits: {', '.join(f'`{parent}`' for parent in model.inherits)}", ""]
            for field in model.fields:
                target = f" → `{field.target}`" if field.target else ""
                label = f" “{field.label}”" if field.label else ""
                notes = f" ({', '.join(field.notes)})" if field.notes else ""
                lines.append(f"- `{field.name}` {field.kind}{target}{label}{notes}")
            if model.actions:
                lines += ["", f"Public methods: {', '.join(f'`{name}`' for name in sorted(set(model.actions)))}"]
            if model.hooks:
                lines += ["", f"Extension points: {', '.join(f'`{name}`' for name in sorted(set(model.hooks)))}"]
            lines.append("")
        self.write(f"models/{addon.name}.md", "\n".join(lines))

    def xmlids(self, addon: Addon, declared: list[XmlId]) -> None:
        lines = [f"# {addon.name} — XML ids", ""]
        for model in sorted({entry.model for entry in declared}):
            lines += [f"## {model}", ""]
            lines += [
                f"- `{entry.xmlid}`" + (f" — {entry.detail}" if entry.detail else "")
                for entry in declared if entry.model == model
            ]
            lines.append("")
        self.write(f"xmlids/{addon.name}.md", "\n".join(lines))

    def settings(self, settings: list[Setting]) -> None:
        lines = ["# Settings", "", "Each field of `res.config.settings`, and where it keeps its value.", ""]
        lines += ["| Field | Label | Kept as | Addon |", "|---|---|---|---|"]
        lines += [f"| `{s.name}` | {s.label} | {s.kept_as} | {s.addon} |" for s in sorted(settings, key=lambda s: s.name)]
        self.write("settings.md", "\n".join(lines))

    def index(self, rows: list[tuple[Addon, list[Model]]]) -> None:
        lines = ["# Addons", "", "| Addon | Name | Defines | Extends |", "|---|---|---|---|"]
        for addon, models in rows:
            defined = ", ".join(f"`{m.name}`" for m in models if not m.extends)
            extended = ", ".join(sorted({f"`{m.name}`" for m in models if m.extends}))
            lines.append(f"| {addon.name} | {addon.title} | {defined} | {extended} |")
        self.write("addons.md", "\n".join(lines))

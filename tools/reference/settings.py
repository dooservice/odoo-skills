"""Where each switch of Odoo's Settings screen keeps what it decides.

A field of `res.config.settings` is a system parameter (`config_parameter`), a group given
to every internal user (`implied_group`), a field of the company (`related`), or a module
to install (`module_*`). Knowing which is what lets an agent change a setting the way the
screen does, or read why it is on.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass

from .constants import SETTINGS_MODEL
from .manifests import Addon
from .models import ModelScanner


@dataclass(frozen=True)
class Setting:
    addon: str
    name: str
    label: str
    kept_as: str


class SettingsScanner:
    def __init__(self) -> None:
        self.models = ModelScanner()

    def scan(self, addon: Addon) -> list[Setting]:
        found = []
        for path in addon.python_files:
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"))
            except (SyntaxError, UnicodeDecodeError):
                continue
            for node in tree.body:
                model = self.models.model(node) if isinstance(node, ast.ClassDef) else None
                if model is None or model.name != SETTINGS_MODEL:
                    continue
                found += [setting for statement in node.body if (setting := self.setting(addon.name, statement))]
        return found

    def setting(self, addon: str, statement: ast.stmt) -> Setting | None:
        if not (isinstance(statement, ast.Assign) and isinstance(statement.targets[0], ast.Name)):
            return None
        name, value = statement.targets[0].id, statement.value
        described = self.models.field(name, value)
        if described is None or not isinstance(value, ast.Call):
            return None
        keywords = {keyword.arg: self.models.literal(keyword.value) for keyword in value.keywords if keyword.arg}
        if isinstance(keywords.get("compute"), str):
            kept = f"computed by `{keywords['compute']}`"
        elif isinstance(keywords.get("config_parameter"), str):
            kept = f"parameter `{keywords['config_parameter']}`"
        elif isinstance(keywords.get("implied_group"), str):
            kept = f"group `{keywords['implied_group']}`"
        elif isinstance(keywords.get("related"), str):
            kept = f"`{keywords['related']}`"
        elif name.startswith("module_"):
            kept = f"installs `{name.removeprefix('module_')}`"
        else:
            kept = "computed by the screen"
        return Setting(addon, name, described.label, kept)

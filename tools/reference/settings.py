"""Where each switch of Odoo's Settings screen keeps what it decides.

A field of `res.config.settings` is a system parameter (`config_parameter`), a group given
to every internal user (`implied_group`), a field of the company (`related`), or a module
to install (`module_*`). Knowing which is what lets an agent change a setting the way the
screen does, or read why it is on.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass

from .class_body import ClassBody
from .constants import KEPT_AS, SETTINGS_MODEL
from .field_call import FieldCall
from .literal import Literal
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
            for body in ClassBody.top_level(ast.parse(path.read_text(encoding="utf-8"))):
                model = self.models.model(body)
                if model is not None and model.name == SETTINGS_MODEL:
                    found += [
                        setting for name, value in body.assignments if (setting := self.setting(addon.name, name, value))
                    ]
        return found

    def setting(self, addon: str, name: str, value: ast.expr) -> Setting | None:
        call = FieldCall.of(value)
        if call is None:
            return None
        return Setting(addon, name, self.models.field(name, value).label, self.kept_as(name, call))

    @staticmethod
    def kept_as(name: str, call: FieldCall) -> str:
        for keyword, description in KEPT_AS:
            if value := Literal.text(call.keyword(keyword)):
                return description.format(value)
        if name.startswith("module_"):
            return f"installs `{name.removeprefix('module_')}`"
        return "computed by the screen"

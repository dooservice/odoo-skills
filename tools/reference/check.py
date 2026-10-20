"""Checks what the reference says against a running Odoo, inside `odoo-bin shell`.

The scanners read the source of the Odoo they run in; every addon installed in the
database is then compared with Odoo's own registry and data: each model exists, each
field exists with the same type and target, each XML id exists on the same model, and
each Settings field keeps its value where the reference says. The answer is one JSON
line: how many were checked, and every mismatch.
"""

from __future__ import annotations

from pathlib import Path

from .constants import KINDS
from .manifests import Addons
from .models import ModelScanner
from .settings import SettingsScanner
from .xmlids import XmlIdScanner


class ReferenceCheck:
    def __init__(self, env, source: Path) -> None:
        self.env = env
        self.source = source
        self.checked = {"models": 0, "fields": 0, "xmlids": 0, "settings": 0}
        self.wrong: list[str] = []
        self.settings: dict[str, list] = {}
        classified = env["res.config.settings"]._get_classified_fields()
        self.parameters = dict(classified["config"])
        self.groups = {name: implied.get_external_id()[implied.id] for name, groups, implied in classified["group"]}

    def run(self) -> dict:
        installed = set(self.env["ir.module.module"].search([("state", "=", "installed")]).mapped("name"))
        known = {(row["module"], row["name"]): row["model"] for row in self.env["ir.model.data"].search_read(
            [("module", "in", list(installed))], ["module", "name", "model"])}
        for addon in Addons(self.source).all():
            if addon.name not in installed:
                continue
            for model in ModelScanner().scan(addon):
                self.model(addon.name, model)
            for declared in XmlIdScanner().scan(addon):
                self.xmlid(addon.name, declared, known)
            for setting in SettingsScanner().scan(addon):
                self.settings.setdefault(setting.name, []).append(setting)
        for defined in self.settings.values():
            self.setting(defined)
        return {"installed": len(installed), "checked": self.checked, "wrong": self.wrong}

    def model(self, addon, model) -> None:
        self.checked["models"] += 1
        if model.name not in self.env.registry:
            self.wrong.append(f"{addon}: model {model.name} is not in the registry")
            return
        fields = self.env[model.name]._fields
        for field in model.fields:
            self.checked["fields"] += 1
            real = fields.get(field.name)
            if real is None:
                self.wrong.append(f"{addon}: {model.name}.{field.name} does not exist")
                continue
            kind = KINDS.get(field.kind, field.kind.lower())
            if real.type != kind:
                self.wrong.append(f"{addon}: {model.name}.{field.name} is {real.type}, reference says {kind}")
            if field.target and real.comodel_name != field.target:
                self.wrong.append(f"{addon}: {model.name}.{field.name} targets {real.comodel_name}, reference says {field.target}")

    def xmlid(self, addon, declared, known) -> None:
        self.checked["xmlids"] += 1
        module, _, name = declared.xmlid.partition(".")
        real = known.get((module, name))
        if module == addon and real is None:
            self.wrong.append(f"{addon}: XML id {declared.xmlid} does not exist")
        elif real is not None and real != declared.model:
            self.wrong.append(f"{addon}: XML id {declared.xmlid} is a {real}, reference says {declared.model}")

    def setting(self, defined) -> None:
        """Right when the running field matches one of the addons that define it."""
        self.checked["settings"] += 1
        real = self.env["res.config.settings"]._fields.get(defined[0].name)
        if real is None:
            self.wrong.append(f"{defined[0].addon}: setting {defined[0].name} does not exist")
            return
        name = defined[0].name
        actual = {
            f"parameter {self.parameters.get(name)}",
            f"group {self.groups.get(name)}",
            f"installs {name.removeprefix('module_')}",
            f"computed by {real.compute}",
            str(real.related),
            "computed by the screen",
        }
        if not any(setting.kept_as.replace("`", "") in actual for setting in defined):
            kept = " / ".join(setting.kept_as for setting in defined)
            self.wrong.append(f"{defined[0].addon}: setting {defined[0].name} runs as {sorted(actual)[:3]}, reference says {kept}")

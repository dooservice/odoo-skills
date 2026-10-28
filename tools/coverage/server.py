"""Framework items declared by the server: view types, action types, route types and auth values."""

from __future__ import annotations

import ast
from pathlib import Path

from .constants import (
    ACTION_PREFIX,
    AUTH_PREFIX,
    BASE_MODELS,
    ENTERPRISE_VIEW_TYPES,
    IR_HTTP_FILE,
    ROUTE_TYPE_ATTRIBUTE,
    VIEW_MODEL_FILE,
)
from .guidelines import GuidelineText
from .source import PythonFile


class ViewTypes:
    """The options of `ir.ui.view`'s `type` selection, Enterprise-only views left out."""

    title = "View types"

    def items(self, source: Path) -> list[str]:
        found = []
        for model in PythonFile(source / VIEW_MODEL_FILE).classes():
            if PythonFile.text_attribute(model, "_name") == "ir.ui.view":
                found += self.options(model)
        return sorted(name for name in found if name not in ENTERPRISE_VIEW_TYPES)

    @staticmethod
    def options(model: ast.ClassDef) -> list[str]:
        for child in model.body:
            match child:
                case ast.Assign(targets=[ast.Name(id="type")], value=ast.Call(args=[ast.List() as options, *_])):
                    return [ast.literal_eval(option)[0] for option in options.elts]
        return []

    def covered(self, name: str, text: GuidelineText) -> bool:
        return text.contains(f"<{name}", f"`{name}`", f"'{name}'")


class ActionTypes:
    """The `ir.actions.*` models of base."""

    title = "Action types"

    def items(self, source: Path) -> list[str]:
        names = {
            PythonFile.text_attribute(model, "_name")
            for path in sorted((source / BASE_MODELS).glob("ir_actions*.py"))
            for model in PythonFile(path).classes()
        }
        return sorted(name for name in names if name.startswith(ACTION_PREFIX))

    def covered(self, name: str, text: GuidelineText) -> bool:
        return text.has_word(name)


class RouteTypes:
    """The `type=` of `http.route`: one dispatcher class per type."""

    title = "Route types"

    def items(self, source: Path) -> list[str]:
        legacy = source / "odoo" / "http.py"
        paths = [legacy] if legacy.is_file() else sorted((source / "odoo" / "http").glob("*.py"))
        names = {
            PythonFile.text_attribute(dispatcher, ROUTE_TYPE_ATTRIBUTE)
            for path in paths
            for dispatcher in PythonFile(path).classes()
        }
        return sorted(name for name in names if name)

    def covered(self, name: str, text: GuidelineText) -> bool:
        return text.contains(f"type='{name}'", f'type="{name}"')


class AuthValues:
    """The `auth=` of `http.route`: one `_auth_method_<auth>` on `ir.http` per value."""

    title = "Route auth values"

    def items(self, source: Path) -> list[str]:
        methods = [name for model in PythonFile(source / IR_HTTP_FILE).classes() for name in PythonFile.methods(model)]
        return sorted({name.removeprefix(AUTH_PREFIX) for name in methods if name.startswith(AUTH_PREFIX)})

    def covered(self, name: str, text: GuidelineText) -> bool:
        return text.contains(f"auth='{name}'", f'auth="{name}"')

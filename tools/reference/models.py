"""The models an addon defines or extends, read from its source without importing it."""

from __future__ import annotations

import ast
from dataclasses import dataclass, field

from .manifests import Addon

RELATIONAL = {"Many2one", "One2many", "Many2many"}
FLAGS = ("required", "readonly", "store", "index", "company_dependent")
HOOK_PREFIXES = ("_prepare_", "_get_", "_action_", "_create_", "_post_", "_check_")


@dataclass
class Field:
    name: str
    kind: str
    target: str = ""
    label: str = ""
    notes: list[str] = field(default_factory=list)


@dataclass
class Model:
    name: str
    extends: bool
    description: str = ""
    inherits: list[str] = field(default_factory=list)
    fields: list[Field] = field(default_factory=list)
    actions: list[str] = field(default_factory=list)
    hooks: list[str] = field(default_factory=list)


class ModelScanner:
    def scan(self, addon: Addon) -> list[Model]:
        found = []
        for path in addon.python_files:
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"))
            except (SyntaxError, UnicodeDecodeError):
                continue
            found += [model for node in tree.body if isinstance(node, ast.ClassDef) if (model := self.model(node))]
        return found

    def model(self, node: ast.ClassDef) -> Model | None:
        attributes = {
            target.id: statement.value
            for statement in node.body if isinstance(statement, ast.Assign)
            for target in statement.targets if isinstance(target, ast.Name)
        }
        name, inherits = self.literal(attributes.get("_name")), self.literal(attributes.get("_inherit"))
        inherited = [inherits] if isinstance(inherits, str) else list(inherits or [])
        if not isinstance(name, str) and not inherited:
            return None
        named = name if isinstance(name, str) else inherited[0]
        model = Model(
            name=named,
            extends=not isinstance(name, str) or name in inherited,
            description=str(self.literal(attributes.get("_description")) or ""),
            inherits=[parent for parent in inherited if parent != named],
        )
        for key, value in attributes.items():
            if described := self.field(key, value):
                model.fields.append(described)
        for statement in node.body:
            if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if statement.name.startswith("action_") or not statement.name.startswith("_"):
                    model.actions.append(statement.name)
                elif statement.name.startswith(HOOK_PREFIXES):
                    model.hooks.append(statement.name)
        return model

    def field(self, name: str, value: ast.expr) -> Field | None:
        if not (isinstance(value, ast.Call) and isinstance(value.func, ast.Attribute)):
            return None
        if not (isinstance(value.func.value, ast.Name) and value.func.value.id == "fields"):
            return None
        kind, keywords = value.func.attr, {k.arg: self.literal(k.value) for k in value.keywords if k.arg}
        first = self.literal(value.args[0]) if value.args else None
        target = keywords.get("comodel_name") or (first if kind in RELATIONAL else "")
        label = keywords.get("string") or (first if isinstance(first, str) and kind not in RELATIONAL else "")
        notes = [flag for flag in FLAGS if keywords.get(flag) is True]
        notes += [f"{key}={keywords[key]}" for key in ("related", "compute") if isinstance(keywords.get(key), str)]
        return Field(name, kind, str(target or ""), str(label or ""), notes)

    @staticmethod
    def literal(node: ast.expr | None):
        if node is None:
            return None
        try:
            return ast.literal_eval(node)
        except (ValueError, SyntaxError, TypeError):
            return None

"""The models an addon defines or extends, read from its source without importing it."""

from __future__ import annotations

import ast
from dataclasses import dataclass, field

from .class_body import ClassBody
from .constants import FLAGS, HOOK_PREFIXES, RELATIONAL
from .field_call import FieldCall
from .literal import Literal
from .manifests import Addon


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
            for body in ClassBody.top_level(ast.parse(path.read_text(encoding="utf-8"))):
                if model := self.model(body):
                    found.append(model)
        return found

    def model(self, body: ClassBody) -> Model | None:
        """The model a class of the source declares, if it declares one."""
        name = Literal.text(body.attributes.get("_name"))
        inherited = Literal.texts(body.attributes.get("_inherit"))
        if not name and not inherited:
            return None
        named = name or inherited[0]
        model = Model(
            name=named,
            extends=not name or name in inherited,
            description=Literal.text(body.attributes.get("_description")),
            inherits=[parent for parent in inherited if parent != named],
        )
        model.fields = [described for key, value in body.attributes.items() if (described := self.field(key, value))]
        for method in body.methods:
            if method.startswith("action_") or not method.startswith("_"):
                model.actions.append(method)
            elif method.startswith(HOOK_PREFIXES):
                model.hooks.append(method)
        return model

    def field(self, name: str, value: ast.expr) -> Field | None:
        call = FieldCall.of(value)
        if call is None:
            return None
        first = Literal.text(call.first_argument)
        relational = call.kind in RELATIONAL
        target = (Literal.text(call.keyword("comodel_name")) or first) if relational else ""
        label = Literal.text(call.keyword("string")) or ("" if relational else first)
        notes = [flag for flag in FLAGS if Literal.is_true(call.keyword(flag))]
        notes += [f"{key}={text}" for key in ("related", "compute") if (text := Literal.text(call.keyword(key)))]
        return Field(name, call.kind, target, label, notes)

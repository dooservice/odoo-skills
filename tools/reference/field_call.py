"""A field declared in a model's body: `name = fields.Kind(...)`."""

from __future__ import annotations

import ast
from dataclasses import dataclass


@dataclass(frozen=True)
class FieldCall:
    kind: str
    first_argument: ast.expr | None
    keywords: dict[str, ast.expr]

    @classmethod
    def of(cls, value: ast.expr) -> FieldCall | None:
        """The declaration, when the value is a call to `fields.<Kind>`."""
        return FieldCallReader().visit(value)

    def keyword(self, name: str) -> ast.expr | None:
        return self.keywords.get(name)


class FieldCallReader(ast.NodeVisitor):
    def visit_Call(self, node: ast.Call) -> FieldCall | None:
        called = ast.unparse(node.func)
        if not called.startswith("fields."):
            return None
        kind = called.removeprefix("fields.")
        keywords = {keyword.arg: keyword.value for keyword in node.keywords if keyword.arg}
        return FieldCall(kind, node.args[0] if node.args else None, keywords)

    def generic_visit(self, node: ast.AST) -> None:
        return None

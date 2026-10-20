"""The plain values written in Odoo's source: a name, a list of names, a flag."""

from __future__ import annotations

import ast


class Literal(ast.NodeVisitor):
    """Reads an expression of the source as the value it spells, when it spells one.

    Anything computed (`_("Label")`, a variable, a call) reads as None: the reference
    lists what the source states, not what it would evaluate to. Runs on Python 3.9,
    the one of Odoo 16.0, where the reference check also runs.
    """

    def visit_Constant(self, node: ast.Constant) -> object:
        return node.value

    def visit_List(self, node: ast.List) -> list:
        return [self.visit(item) for item in node.elts]

    def visit_Tuple(self, node: ast.Tuple) -> list:
        return [self.visit(item) for item in node.elts]

    def generic_visit(self, node: ast.AST) -> None:
        return None

    @classmethod
    def value(cls, node: ast.expr | None) -> object:
        return None if node is None else cls().visit(node)

    @classmethod
    def text(cls, node: ast.expr | None) -> str:
        """The string the source writes there, or empty for anything else."""
        value = cls.value(node)
        return value if isinstance(value, str) else ""

    @classmethod
    def texts(cls, node: ast.expr | None) -> list[str]:
        """One name, or a list or tuple of names, as a list; empty if any of them is computed."""
        value = cls.value(node)
        names = value if isinstance(value, list) else [value]
        return names if all(isinstance(name, str) and name for name in names) else []

    @classmethod
    def is_true(cls, node: ast.expr | None) -> bool:
        return cls.value(node) is True

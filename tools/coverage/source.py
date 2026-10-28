"""One Python file of Odoo's source, read as a syntax tree without importing it."""

from __future__ import annotations

import ast
from pathlib import Path


class PythonFile:
    def __init__(self, path: Path) -> None:
        self.tree = ast.parse(path.read_text(encoding="utf-8"))

    def classes(self) -> list[ast.ClassDef]:
        return [node for node in self.tree.body if type(node) is ast.ClassDef]

    def functions(self) -> list[ast.FunctionDef]:
        return [node for node in self.tree.body if type(node) is ast.FunctionDef]

    def class_named(self, name: str) -> ast.ClassDef | None:
        return next((node for node in self.classes() if node.name == name), None)

    @staticmethod
    def methods(node: ast.ClassDef) -> list[str]:
        return [child.name for child in node.body if type(child) is ast.FunctionDef]

    @staticmethod
    def bases(node: ast.ClassDef) -> list[str]:
        """The names a class inherits, `Field[int]` and `orm.Field` read as `Field`."""
        return [ast.unparse(base).split("[")[0].split(".")[-1] for base in node.bases]

    @staticmethod
    def text_attribute(node: ast.ClassDef, name: str) -> str:
        """The string a class body assigns to `name`, or an empty string."""
        for child in node.body:
            match child:
                case ast.Assign(targets=[ast.Name(id=target)], value=ast.Constant(value=str() as value)):
                    if target == name:
                        return value
        return ""

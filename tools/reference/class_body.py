"""What a class of Odoo's source assigns and defines, read without importing it."""

from __future__ import annotations

import ast


class ClassBody(ast.NodeVisitor):
    """What a class assigns, each assignment in order, and the methods it defines.

    Only the class's own statements: nothing nested inside its methods or inner classes.
    """

    def __init__(self, node: ast.ClassDef) -> None:
        self.assignments: list[tuple[str, ast.expr]] = []
        self.methods: list[str] = []
        self.current_value: ast.expr | None = None
        for statement in node.body:
            self.visit(statement)

    @classmethod
    def top_level(cls, module: ast.Module) -> list[ClassBody]:
        """The classes a module defines at its top level."""
        return TopLevelClasses(module).bodies

    def visit_Assign(self, node: ast.Assign) -> None:
        self.current_value = node.value
        for target in node.targets:
            self.visit(target)

    @property
    def attributes(self) -> dict[str, ast.expr]:
        """Each name with the value it ends up with."""
        return dict(self.assignments)

    def visit_Name(self, node: ast.Name) -> None:
        self.assignments.append((node.id, self.current_value))

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.methods.append(node.name)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.methods.append(node.name)

    def generic_visit(self, node: ast.AST) -> None:
        return None


class TopLevelClasses(ast.NodeVisitor):
    def __init__(self, module: ast.Module) -> None:
        self.bodies: list[ClassBody] = []
        for statement in module.body:
            self.visit(statement)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self.bodies.append(ClassBody(node))

    def generic_visit(self, node: ast.AST) -> None:
        return None

"""Framework items for module authors outside the ORM: web client registries and test tools."""

from __future__ import annotations

import ast
import subprocess
from pathlib import Path

from .constants import QUOTES, REGISTRY_CALL, TEST_CLASS_ENDINGS, WEB_CLIENT
from .guidelines import GuidelineText
from .source import PythonFile


class WebRegistries:
    """The names opened with `registry.category("...")` in the web client, read from git."""

    title = "Web client registries"

    def items(self, source: Path) -> list[str]:
        command = ["git", "-C", str(source), "grep", "-h", "-F", REGISTRY_CALL, "HEAD", "--", WEB_CLIENT]
        lines = subprocess.run(command, capture_output=True, text=True, check=True).stdout.splitlines()
        names = {self.quoted(piece) for line in lines for piece in line.split(REGISTRY_CALL)[1:]}
        return sorted(name for name in names if name and not name.startswith("_"))

    @staticmethod
    def quoted(piece: str) -> str:
        """The literal a call starts with, or an empty string when it is passed a variable."""
        if not piece or piece[0] not in QUOTES:
            return ""
        return piece[1:].split(piece[0])[0]

    def covered(self, name: str, text: GuidelineText) -> bool:
        return text.contains(*(f"category({quote}{name}{quote})" for quote in QUOTES))


class TestTools:
    """Test case classes, `Form`, and the decorators of `odoo/tests`.

    A decorator is a public function wrapped with `decorator`, that returns a function it
    defines, or that returns the one object it was given; or a class named in lower case.
    """

    title = "Test tools"

    def items(self, source: Path) -> list[str]:
        files = [PythonFile(path) for path in sorted((source / "odoo" / "tests").glob("*.py"))]
        classes = [node for file in files for node in file.classes() if self.is_tool_class(node)]
        functions = [node for file in files for node in file.functions() if self.is_decorator(node)]
        return sorted({node.name for node in classes + functions if not node.name.startswith("_")})

    @staticmethod
    def is_tool_class(node: ast.ClassDef) -> bool:
        if "type" in PythonFile.bases(node):
            return False
        return node.name.endswith(TEST_CLASS_ENDINGS) or node.name[0].islower()

    @staticmethod
    def is_decorator(node: ast.FunctionDef) -> bool:
        nested = [child.name for child in node.body if type(child) is ast.FunctionDef]
        given = [argument.arg for argument in node.args.args]
        returned = ast.unparse(node.body[-1]).removeprefix("return ")
        wrapped = "decorator" in [ast.unparse(decorator) for decorator in node.decorator_list]
        return wrapped or returned in nested or (given == [returned])

    def covered(self, name: str, text: GuidelineText) -> bool:
        if name[0].isupper():
            return text.has_word(name)
        return text.contains(f"@{name}")

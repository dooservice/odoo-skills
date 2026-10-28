"""Framework items of the ORM: field types, `api` decorators and `BaseModel`'s public methods."""

from __future__ import annotations

from pathlib import Path

from .constants import INTERNAL_FIELD_TYPES, NOT_DECORATORS
from .guidelines import GuidelineText
from .source import PythonFile


class FieldTypes:
    """Classes that set a field `type`, themselves or through a parent (`Image` from `Binary`).

    `Id` is left out: the ORM adds it to every model by itself.
    """

    title = "Field types"

    def items(self, source: Path) -> list[str]:
        legacy = source / "odoo" / "fields.py"
        paths = [legacy] if legacy.is_file() else sorted((source / "odoo" / "orm").glob("fields*.py"))
        classes = [node for path in paths for node in PythonFile(path).classes()]
        parents = {node.name: PythonFile.bases(node) for node in classes}
        typed = {node.name for node in classes if PythonFile.text_attribute(node, "type")}
        public = [name for name in parents if not name.startswith("_") and name not in INTERNAL_FIELD_TYPES]
        return sorted(name for name in public if self.typed(name, parents, typed))

    def typed(self, name: str, parents: dict[str, list[str]], typed: set[str]) -> bool:
        return name in typed or any(self.typed(parent, parents, typed) for parent in parents.get(name, []))

    def covered(self, name: str, text: GuidelineText) -> bool:
        return text.has_word(f"fields.{name}") or text.has_code(name)


class ApiDecorators:
    """Public functions of `odoo/api.py` (up to 18.0) or `odoo/orm/decorators.py`, helpers left out."""

    title = "API decorators"

    def items(self, source: Path) -> list[str]:
        legacy = source / "odoo" / "api.py"
        path = legacy if legacy.is_file() else source / "odoo" / "orm" / "decorators.py"
        names = {node.name for node in PythonFile(path).functions()}
        return sorted(name for name in names if not name.startswith("_") and name not in NOT_DECORATORS)

    def covered(self, name: str, text: GuidelineText) -> bool:
        return text.has_word(f"api.{name}")


class OrmMethods:
    """The public methods and properties of `BaseModel`."""

    title = "ORM methods"

    def items(self, source: Path) -> list[str]:
        legacy = source / "odoo" / "models.py"
        path = legacy if legacy.is_file() else source / "odoo" / "orm" / "models.py"
        model = PythonFile(path).class_named("BaseModel")
        return sorted({name for name in PythonFile.methods(model) if not name.startswith("_")})

    def covered(self, name: str, text: GuidelineText) -> bool:
        return text.has_attribute(name) or text.has_code(name)

"""`odoo-guidelines/guidelines/python.md`: imports, naming, model layout and translations."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class PythonRules(Document):
    path = "odoo-guidelines/guidelines/python.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "linter_reference": version.pick(
                v16="Odoo's pylint rules are the reference",
                v17_="the `ruff.toml` of the Odoo source is the reference for what core enforces",
            ),
            "odoo_imports": version.pick(
                v16_17="from odoo import _, api, fields, models, Command",
                v18_="from odoo import Command, api, fields, models",
            ),
            "constraint_declarations": version.pick(
                v16_18="`_sql_constraints`",
                v19_="`models.Constraint`/`models.Index` attributes",
            ),
            "translate_api": version.pick(
                v16_17="in model code it is `_(...)`, imported from `odoo`",
                v18_="in model code the current API is `self.env._(...)`",
            ),
            "translation_notes": self.translation_notes(version),
        }

    def translation_notes(self, version: OdooVersion) -> str:
        """Where the translation call finds its language, and how to translate constants."""
        return version.pick(
            v16_17="""\
- `_` locates the environment by inspecting the caller's frame: call it inside
  model methods, where `self.env` exists; in plain helper functions pass the
  translated string in from the caller.
- Never call `_()` at module or class level: it runs at import time with no
  user language. Use `_lt` (lazy, from `odoo`) for such constants.""",
            v18_="""\
- Bare `_` (imported from `odoo`) still works: it locates the environment by
  inspecting the caller's frame; in plain functions and comprehensions it can
  silently return the untranslated string. Prefer `self.env._`.
- Never call `_()` at module or class level: it runs at import time with no
  user language. If a module-level constant is unavoidable, make it lazy
  (`_lt = LazyTranslate(__name__)`; `LABEL = _lt("...")`) and resolve it where
  the language is known, with `self.env._(LABEL)`.""",
        )

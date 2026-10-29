"""`odoo-guidelines/guidelines/models.md`: model classes, attributes, inheritance and SQL objects."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion
from .models_versions import ModelVersions


class Models(Document):
    path = "odoo-guidelines/guidelines/models.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        differences = ModelVersions(version)
        return {
            **super().values(version),
            **differences.attributes(),
            **differences.sql_objects(),
            "inherit_list_name": version.pick(
                v16_18="Without `_name`, a list of several models names the model after the "
                "Python class.",
                v19_="Without `_name`, any list, even of one model, names the model after the "
                "Python class (with a warning).",
            ),
            "check_inherits_access": version.pick(
                v16_19="",
                v20=" Access to a delegating record also requires access to its parent "
                "record, unless the model sets `_check_inherits_access = False`.",
            ),
            "recursion_check": version.pick(
                v16_17="`@api.constrains('parent_id')` raising `ValidationError` when "
                "`not self._check_recursion()`.",
                v18_="`@api.constrains('parent_id')` raising `ValidationError` when "
                "`self._has_cycle()`.",
            ),
        }

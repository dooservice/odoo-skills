"""`odoo-guidelines/guidelines/module_structure.md`: directories and file names of an addon."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class ModuleStructure(Document):
    path = "odoo-guidelines/guidelines/module_structure.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "security_files": version.pick(
                v16_19="Security files: access rows in `security/ir.model.access.csv`; "
                "groups and record\n  rules in `security/<module>_security.xml`.",
                v20="Security files: access rows in `security/ir.access.csv`; "
                "groups and other\n  security records in `security/<module>_security.xml`.",
            ),
        }

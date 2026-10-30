"""`odoo-guidelines/guidelines/module_structure.md`: directories and file names of an addon."""

from __future__ import annotations

from ..version import OdooVersion
from .lead import GuidedDocument


class ModuleStructure(GuidedDocument):
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
            "populate_directory": version.pick(v16_17=", `populate/`", v18_19="", v20=", `populate/`"),
            "populate": version.pick(
                v16_17="\n- `populate/` holds the `_populate_factories` of the module's models, used by\n"
                "  `odoo-bin populate`; an `__init__.py` imports them.",
                v18_19="",
                v20="\n- `populate/` holds `populate.blueprint` XML records (`populate_demo.xml`,\n"
                "  `benchmarks.xml`); an `__init__.py` makes it an importable package for\n"
                "  custom populate generators.",
            ),
        }

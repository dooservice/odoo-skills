"""`odoo-guidelines/guidelines/installed.md`: changing a module a real database already has."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class InstalledModules(Document):
    path = "odoo-guidelines/guidelines/installed.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "demo_default": version.pick(
                v16_18=", the default unless the\ndatabase was created with `--without-demo`",
                v19_=", which a new database has\nonly when created with `--with-demo`",
            ),
            "force_demo": version.pick(
                v16_18="",
                v19_="\n- `odoo-bin module force-demo -d <db>` loads demo data into an existing database that\n"
                "  has none; never run it on production.",
            ),
        }

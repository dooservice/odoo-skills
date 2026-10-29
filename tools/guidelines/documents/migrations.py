"""`odoo-guidelines/guidelines/migrations.md`: module versions, migration scripts and hooks."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class Migrations(Document):
    path = "odoo-guidelines/guidelines/migrations.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "version_check": version.pick(
                v16=" 16.0 does not check the format: the\n"
                "  version of another series (`15.0.1.0.0`) is silently read as `16.0.15.0.1.0.0`.",
                v17_18=" Any other format, including the\n"
                "  version of another series, stops the module from loading with `ValueError`\n"
                "  (`invalid manifest`).",
                v19_=" A version that is not two to five\n"
                "  numbers stops the module from loading with `ValueError` (`invalid manifest`); the\n"
                "  version of another series makes the module uninstallable, with a log warning only.",
            ),
            "folder_name": version.pick(
                v16=" Name it with the full version\n"
                "  (`16.0.1.1.0`) or two numbers (`1.1`): a three-number folder such as `1.1.0` is\n"
                "  read as a full version and never runs.",
                v17_=" Name it with the full version\n"
                f"  (`{version.name}.1.1.0`) or the module part alone (`1.1.0`), compared without the\n"
                "  series.",
            ),
            "migrate_check": version.pick(
                v16_17=" A script without a\n"
                "  `migrate` function is skipped, with only an error in the log.",
                v18_=" A script without\n"
                "  `migrate(cr, version)` stops the update (the parameters may also be named `_cr`\n"
                "  and `_version`).",
            ),
            "hooks": self.hooks(version),
        }

    def hooks(self, version: OdooVersion) -> str:
        return version.pick(
            v16="```python\ndef pre_init_hook(cr):\n    ...\n\n\n"
            "def post_init_hook(cr, registry):\n"
            "    env = api.Environment(cr, SUPERUSER_ID, {})\n\n\n"
            "def uninstall_hook(cr, registry):\n    ...\n```",
            v17_="```python\ndef pre_init_hook(env):\n    ...\n\n\n"
            "def post_init_hook(env):\n"
            "    env['library.book'].search([])._compute_isbn()\n\n\n"
            "def uninstall_hook(env):\n    ...\n```\n\n"
            "Each hook receives an `env` as superuser; a hook written with the `(cr)` or\n"
            "`(cr, registry)` signature of earlier versions fails.",
        )

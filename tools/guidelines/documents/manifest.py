"""`odoo-guidelines/guidelines/manifest.md`: the keys of `__manifest__.py`."""

from __future__ import annotations

from ..version import OdooVersion
from .lead import GuidedDocument


class Manifest(GuidedDocument):
    path = "odoo-guidelines/guidelines/manifest.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "base_dependency": version.pick(
                v16_18="List `base` only when the module depends on\n  nothing else.",
                v19_="Don't list `base`: a manifest without `depends`\n  gets `['base']` injected.",
            ),
        }

"""`odoo-guidelines/guidelines/controllers.md`: routes, their auth and their type."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class Controllers(Document):
    path = "odoo-guidelines/guidelines/controllers.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "auth_modes": version.pick(
                v16_17="`user`, `public`, or `none`",
                v18_="`user`, `bearer`, `public`, or `none`",
            ),
            "bearer": version.pick(
                v16_17="",
                v18_19="\n  `auth='bearer'` authenticates with an API key in the `Authorization` header.",
                v20="\n  `auth='bearer'` authenticates with an API key in the `Authorization` header\n"
                "  and requires `bearer_scope` (which is only valid there).",
            ),
            "readonly": version.pick(
                v16_17="",
                v18_="; an override that makes a read/write route `readonly`\n"
                "  is set back to read/write, also with a warning",
            ),
            "route_types": version.pick(
                v16_18="Route `type` is `'http'` or `'json'` (JSON-RPC).",
                v19_="Route `type` is `'http'`, `'jsonrpc'`, or `'json2'`; `type='json'` is a deprecated\n"
                "  19.0 alias of `'jsonrpc'`.",
            ),
        }

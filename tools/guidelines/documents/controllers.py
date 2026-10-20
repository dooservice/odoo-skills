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
                v18_=" `auth='bearer'` authenticates with an API key in the `Authorization` header.",
            ),
            "route_types": version.pick(
                v16_18="Route `type` is `'http'` or `'json'` (JSON-RPC).",
                v19="Route `type` is `'http'`, `'jsonrpc'`, or `'json2'`; `type='json'` is a deprecated alias of `'jsonrpc'`.",
                v20="Route `type` is `'http'`, `'jsonrpc'`, or `'json2'`; `type='json'` is gone.",
            ),
        }

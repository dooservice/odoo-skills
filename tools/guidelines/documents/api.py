"""`odoo-guidelines/guidelines/api.md`: the decorators of `odoo.api` and how to use them."""

from __future__ import annotations

from ..version import OdooVersion
from .lead import GuidedDocument


class Api(GuidedDocument):
    path = "odoo-guidelines/guidelines/api.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "readonly_row": version.pick(
                v16_17="",
                v18_="| `@api.readonly` | a public method that only reads: an RPC call from the web "
                "client may then run it on a read-only cursor (a replica when one is configured); "
                "it must not write |\n",
            ),
            "returns_row": version.pick(
                v16_18="| `@api.returns('self', lambda value: value.id)` | core methods returning "
                "records, so that RPC callers get ids; overrides inherit it, and new methods do "
                "not need it |\n",
                v19_="",
            ),
            "create_single_row": version.pick(
                v16_18="| `@api.model_create_single` | nothing new: it wraps a `create` that takes "
                "one dict, creates records one by one and logs a warning; use "
                "`@api.model_create_multi` |\n",
                v19_="",
            ),
            "not_in_version": version.pick(
                v16_17="- `@api.readonly` does not exist in this version: every RPC call runs on a "
                "read-write cursor.\n",
                v18="",
                v19_="- `@api.returns` and `@api.model_create_single` do not exist in this version: "
                "RPC turns returned records into ids by itself, and `create` overrides use "
                "`@api.model_create_multi`.\n",
            ),
            "api_model_create": version.pick(
                v16_18="`@api.model` on `create` turns it into `@api.model_create_single`: it "
                "still works, but creates the records one by one and logs a warning.",
                v19_="`@api.model` on `create` silently turns it into `@api.model_create_multi`: "
                "a body written for one dict then receives a list and breaks.",
            ),
            "onchange_return": version.pick(
                v16="Returning `{'domain': ...}` is deprecated and logs a warning: put the domain "
                "on the field or in the view.",
                v17_="A returned `{'domain': ...}` is ignored: put the domain on the field or in "
                "the view.",
            ),
        }

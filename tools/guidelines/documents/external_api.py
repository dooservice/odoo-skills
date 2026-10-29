"""`odoo-guidelines/guidelines/external_api.md`: RPC endpoints, API keys and what RPC may call."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion
from .external_api_endpoints import ExternalEndpoints


class ExternalApi(Document):
    path = "odoo-guidelines/guidelines/external_api.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            **ExternalEndpoints().values(version),
            "key_usage": version.pick(
                v16_18="- The key replaces the password in `authenticate` and in every\n"
                "  `execute_kw` call. A key made in the preferences has no scope and works for\n"
                "  every RPC call of its user.",
                v19="- The key goes in the `Authorization: bearer` header of each JSON-2 call (or\n"
                "  replaces the password on the deprecated endpoints). A key made in the\n"
                "  preferences has no scope and works for every RPC call of its user.",
                v20="- The key goes in the `Authorization: bearer` header of each JSON-2 call (or\n"
                "  replaces the password on the deprecated endpoints). Every key has a scope,\n"
                "  `rpc` for the ones made in the preferences, and authenticates only routes\n"
                "  declaring that same `bearer_scope`.",
            ),
            "key_lifetime": version.pick(
                v16_17="- Keys never expire: list and revoke the ones nobody uses.",
                v18="- A key has an `expiration_date`. Only administrators create keys without\n"
                "  one; other users are limited to the longest `api_key_duration` (days) of\n"
                "  their groups. Plan the renewal before the date passes.",
                v19_="- A key has an `expiration_date`. Only administrators create keys without\n"
                "  one; other users are limited to the longest `api_key_duration` (days) of\n"
                "  their groups. An integration renews its own key with\n"
                "  `res.users.apikeys.generate(key, scope, name, expiration_date)` then\n"
                "  `revoke(old_key)`: allowed to administrators, and to other users once the\n"
                "  system parameter `base.enable_programmatic_api_keys` is set.",
            ),
            "check_access_call": version.pick(
                v16_17="`check_access_rights` and `check_access_rule`",
                v18_="`check_access('write')`",
            ),
            "readonly_methods": version.pick(
                v16_17="",
                v18="\n- Decorate with `@api.readonly` a method that never writes: the web client\n"
                "  then runs it on a read-only cursor.",
                v19_="\n- Decorate with `@api.readonly` a method that never writes: JSON-2 and the\n"
                "  web client then run it on a read-only cursor.",
            ),
            "context_example": version.pick(
                v16_18="`{'context': {'lang': 'fr_FR', 'allowed_company_ids': [1]}}` in `kwargs`",
                v19_="`\"context\": {\"lang\": \"fr_FR\", \"allowed_company_ids\": [1]}` in the body",
            ),
        }

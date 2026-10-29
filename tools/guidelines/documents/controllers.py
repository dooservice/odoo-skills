"""`odoo-guidelines/guidelines/controllers.md`: routes, their type, auth, arguments and portal pages."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion
from .controllers_auth import RouteAuth
from .controllers_types import RouteTypes


class Controllers(Document):
    path = "odoo-guidelines/guidelines/controllers.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            **RouteTypes().values(version),
            **RouteAuth().values(version),
            "readonly": version.pick(
                v16_17="",
                v18_="; an override that makes a read/write route `readonly`\n"
                "  is set back to read/write, also with a warning",
            ),
            "controller_env": version.pick(
                v16_18="Reach the environment through `request.env`; a controller has no `env` of its own.",
                v19_="`self.env` in a controller method is `request.env` (`None` outside a request).",
            ),
            "converter_check": version.pick(
                v16="The record is not checked before the method runs: the\n"
                "  first read raises `AccessError`, so read it before doing anything else.",
                v17_="Before the method runs, the framework checks read access on\n"
                "  it: a missing record gives a 404, a denied one a 404 for a visitor and an\n"
                "  access error for a logged-in user; `handle_params_access_error=callable`\n"
                "  returns its own response instead.",
            ),
            "check_access_call": version.pick(
                v16_17="`record.check_access_rights('read')` and `record.check_access_rule('read')`",
                v18_="`record.check_access('read')`",
            ),
            "slug_call": version.pick(
                v16_17="`slug(record)`, imported from `odoo.addons.http_routing.models.ir_http`",
                v18_="`request.env['ir.http']._slug(record)`",
            ),
            "portal_counters": version.pick(
                v16_19="""\
- A card on `/my/home` is a `portal.portal_docs_entry` call added to
  `portal.portal_my_home` with `placeholder_count="book_count"`; the count comes
  from overriding `_prepare_home_portal_values(counters)`, which fills only the
  keys listed in `counters` and sets 0 when the user lacks read access.""",
                v20="""\
- A card on `/my/home` is a `portal.entry` data record (`name`, `url`,
  `placeholder_count`, `category`, `sequence`); the count comes from overriding
  `_prepare_portal_counter_values(counter)`, which returns
  `('library.book', domain, 'read')` for its own counter and `super()` for the
  others. `_prepare_home_portal_values` no longer exists.""",
            ),
        }

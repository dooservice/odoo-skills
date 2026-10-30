"""`odoo-guidelines/guidelines/actions.md`: actions, bindings, server actions, crons, menus."""

from __future__ import annotations

from ..version import OdooVersion
from .action_values import ServerActionValues
from .lead import GuidedDocument


class ActionRules(GuidedDocument):
    """Window actions and the dicts returned from Python; server actions come from a helper."""

    path = "odoo-guidelines/guidelines/actions.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            **ServerActionValues().values(version),
            "list_tag": version.pick(v16_17="tree", v18_="list"),
            "groups_field": version.pick(v16_18="`groups_id`", v19_="`group_ids`"),
            "path": version.pick(
                v16_17="",
                v18_="\n- `path`: the readable URL segment (`/odoo/<path>`), unique across all\n"
                "  actions, lowercase letters, digits, `_` and `-`, starting with a letter; not\n"
                "  `new` nor starting with `m-` or `action-`. Set it on the actions of menus.",
            ),
            "history_model": version.pick(
                v16_18="",
                v19_=" `ir.actions.server.history` keeps the past versions of a server action's\n"
                "`code`.",
            ),
            "default_view_mode": version.pick(v16_17="tree,form", v18_="list,form"),
            "tree_mode": version.pick(
                v16_17="The list view type is `tree`.",
                v18_="The list view type is `list`; `tree` is not a view type any more and\n"
                "  breaks the action in the client.",
            ),
            "targets": version.pick(
                v16_18="`current` (default, in the main area), `new` (a dialog), `fullscreen`,\n"
                "  `main` (replaces the breadcrumb) or `inline` (legacy settings form).",
                v19_="`current` (default, in the main area), `new` (a dialog), `fullscreen` or\n"
                "  `main` (replaces the breadcrumb).",
            ),
            "mobile": version.pick(
                v16="",
                v17_="\n- `mobile_view_mode` (default `kanban`) is the multi-record view opened\n"
                "  first on a phone when `view_mode` has it.",
            ),
            "embedded": version.pick(
                v16_17="",
                v18_="\n- Embedded actions (`ir.embedded.actions`, shown as `embedded_action_ids`)\n"
                "  are the tabs above a view that open a related action (`parent_action_id`,\n"
                "  `action_id` or `python_method`, `parent_res_model`, `domain`, `context`).",
            ),
            "cache": version.pick(
                v16_18="",
                v19_="\n- `cache` (default `True`) lets the client cache the records its list, kanban\n"
                "  and form views load; set it `False` for data that must always be fresh.",
            ),
            "url_targets": version.pick(
                v16="`new` (default, a new tab) or `self`",
                v17_="`new` (default, a new tab), `self`, or `download`",
            ),
            "client_targets": version.pick(v16_="`current`, `new`, `fullscreen` or `main`"),
            "report_domain": version.pick(
                v16_17="",
                v18_="\n- On `ir.actions.report`, `domain` shows the Print entry only on records\n"
                "  matching it.",
            ),
        }

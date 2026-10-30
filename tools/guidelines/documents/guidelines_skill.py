"""`odoo-guidelines/SKILL.md`: what the skill covers, and which section to read when.

The description is the only part an agent always sees, loaded or not, so it carries the
names that change most between versions: an agent that writes from memory still meets
them.
"""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class GuidelinesSkill(Document):
    path = "odoo-guidelines/SKILL.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "version_anchor": f"what-odoo-{version.number}0-has",
            "names": self.names(version),
        }

    @staticmethod
    def names(version: OdooVersion) -> str:
        return version.pick(
            v16=(
                "views use `<tree>` and `attrs`/`states`; `name_get`; `_sql_constraints`; "
                "domains with `expression.AND/OR`; `group_operator`; chatter "
                "`<div class=\"oe_chatter\">`; `_()`; `ir.model.access.csv` and `ir.rule`; "
                "users `groups_id`; `get_param`; routes `type='json'`; test tag `at_install`."
            ),
            v17=(
                "views use `<tree>` and `invisible=\"expr\"` (no `attrs`/`states`); "
                "`_compute_display_name` (no `name_get`); `_sql_constraints`; "
                "`expression.AND/OR`; counts `_read_group(domain, groupby, ['__count'])` "
                "returns tuples; `group_operator`; chatter `<div class=\"oe_chatter\">`; "
                "`_()`; `ir.model.access.csv` and `ir.rule`; users `groups_id`; `get_param`; "
                "routes `type='json'`; test tag `at_install`."
            ),
            v18=(
                "`<list>` (no `<tree>`) and `invisible=\"expr\"`; `_compute_display_name`; "
                "`_sql_constraints` (no `models.Constraint`); `expression.AND/OR` (no "
                "`Domain`); counts `_read_group(domain, groupby, ['__count'])`; `aggregator`; "
                "`<chatter/>`; `self.env._()`; `ir.model.access.csv` "
                "and `ir.rule`; users `groups_id`, groups `users` and `category_id`; "
                "`get_param`; routes `type='json'`; test tag `at_install`."
            ),
            v19=(
                "`<list>` and `invisible=\"expr\"`; `models.Constraint` (`_sql_constraints` "
                "is ignored); `Domain` (`expression.AND/OR` deprecated); counts "
                "`_read_group(domain, groupby, ['__count'])`; `aggregator`; "
                "`<chatter/>`; `self.env._()`; `ir.model.access.csv` and `ir.rule`; users "
                "`group_ids`, groups `user_ids` and `privilege_id`; `get_param`; routes "
                "`type='jsonrpc'` or `'json2'`; test tag `at_install`."
            ),
            v20=(
                "`<list>` and `invisible=\"expr\"`; `models.Constraint`; `Domain`; counts "
                "`_read_group(domain, groupby, ['__count'])`; "
                "`aggregator`; `<chatter/>`; `self.env._()`; access rights and record rules "
                "are rows of one model, `ir.access`, in `ir.access.csv` (no "
                "`ir.model.access`, no `ir.rule`); users `group_ids`, groups `privilege_id`; "
                "`get_int`/`get_str` (no `get_param`); routes `type='jsonrpc'` or `'json2'`; "
                "test tag `post_install`."
            ),
        )

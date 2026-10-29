"""The values of `views.md` about search, calendar, graph, pivot and hierarchy views."""

from __future__ import annotations

from ..version import OdooVersion


class OtherViewValues:
    """Attributes that appear or go away per version in the views other than form, list and kanban."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "filter_name": version.pick(
                v16_19="give every filter a `name`\n  (`search_default_` keys and extensions refer to it);",
                v20="`name` is required;",
            ),
            "date_filter_extra": version.pick(
                v16_17="",
                v18_19=", and `start_month`, `end_month`,\n  `start_year`, `end_year` bound the offered periods",
                v20=", and `start_month`, `end_month`,\n  `start_year`, `end_year` bound the offered periods; `end_date` names a second\n"
                "  date field so the filter matches records whose period overlaps the chosen one",
            ),
            "search_group": version.pick(
                v16_18='`<group expand="0" string="Group By">`',
                v19_="a bare `<group>` (`expand` and `string` are refused)",
            ),
            "calendar_delay": version.pick(
                v16_19=", `date_delay` a duration in\n  hours instead of `date_stop`",
                v20=", and a length\n  comes from `date_stop` only (compute it from a duration)",
            ),
            "calendar_quick": version.pick(
                v16='`quick_add="0"` disables quick creation',
                v17_='`quick_create="0"` disables quick creation and\n  `quick_create_view_id` picks the form it uses',
            ),
            "calendar_extra": version.pick(
                v16_17='\n  `create="0"` and `delete="0"` hide those actions.',
                v18='\n  `create`, `edit`, `delete` `="0"` hide those actions.',
                v19='\n  `create`, `edit`, `delete` `="0"` hide those actions; `aggregate="amount:sum"`\n'
                "  totals a field per day; `multi_create_view` names the form that creates\n"
                "  several events at once.",
                v20='\n  `create`, `edit`, `delete` `="0"` hide those actions; `aggregate="amount:sum"`\n'
                "  totals a field per day; `multi_create_view` names the form that creates\n"
                "  several events at once; `<popover>` with `<field>`s sets the event popover.",
            ),
            "aggregator": version.pick(v16_17="`group_operator`", v18_="`aggregator`"),
            "hierarchy": version.pick(
                v16="There is no hierarchy view in this version: show a `parent_id` tree in a\n"
                "  list grouped by parent, or with a `parent_id` searchpanel category.",
                v17="Hierarchy (`web_hierarchy`): `<hierarchy parent_field=\"parent_id\"\n"
                "  child_field=\"child_ids\" icon=\"fa-user\" draggable=\"1\">` draws an org chart;\n"
                "  `parent_field` is a many2one and `child_field` a one2many to the same model,\n"
                "  and the node is a `<templates><t t-name=\"hierarchy-box\">` template.",
                v18_19="Hierarchy (`web_hierarchy`): `<hierarchy parent_field=\"parent_id\"\n"
                "  child_field=\"child_ids\" icon=\"fa-user\" draggable=\"1\" default_order=\"name\">`\n"
                "  draws an org chart; `parent_field` is a many2one and `child_field` a\n"
                "  one2many to the same model, and the node is a `<templates><t\n"
                "  t-name=\"hierarchy-box\">` template.",
                v20="Hierarchy (`web_hierarchy`): `<hierarchy parent_field=\"parent_id\"\n"
                "  child_field=\"child_ids\" avatar_field=\"image_128\" draggable=\"1\">` draws an\n"
                "  org chart; `parent_field` is a many2one and `child_field` a one2many to\n"
                "  the same model, and the node is a `<templates><t t-name=\"hierarchy-box\">`\n"
                "  template.",
            ),
            "view_groups": version.pick(v16_18="`groups_id`", v19_="`group_ids`"),
        }

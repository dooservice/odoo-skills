"""`odoo-guidelines/guidelines/views.md`: view types, their elements, modifiers and groups."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion
from .view_kanban import KanbanValues
from .view_modifiers import ModifierValues
from .view_others import OtherViewValues


class ViewRules(Document):
    """Form and list views here; modifiers, kanban and the other types come from helpers."""

    path = "odoo-guidelines/guidelines/views.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        list_tag = version.pick(v16_17="tree", v18_="list")
        return {
            **super().values(version),
            **ModifierValues().values(version),
            **KanbanValues().values(version),
            **OtherViewValues().values(version),
            "list_tag": list_tag,
            "list_tag_ref": f"{list_tag}_view_ref",
            "view_types": self.view_types(version, list_tag),
            "chatter_tag": version.pick(
                v16_17='the chatter `<div class="oe_chatter">` when the model inherits\n  `mail.thread`',
                v18_="`<chatter/>` when the model inherits `mail.thread`",
            ),
            "button_labels": version.pick(
                v16_18="",
                v19="\n  `confirm-label` and `cancel-label` rename the buttons of the confirmation.",
                v20="\n  `confirm-title`, `confirm-label` and `cancel-label` set the title and the\n"
                "  buttons of the confirmation.",
            ),
            "list_group_by": version.pick(
                v16="",
                v17_18=", `default_group_by`",
                v19_=", `default_group_by` (comma-separated for several levels)",
            ),
            "open_form_view": version.pick(
                v16="",
                v17_="\n  `open_form_view=\"1\"` adds a button opening the form on each row of an\n"
                "  editable list.",
            ),
            "list_attributes_extra": version.pick(
                v16_18="",
                v19_="\n  `group_create`, `group_edit`, `group_delete` allow managing the groups.",
            ),
            "column_invisible": version.pick(
                v16="`invisible=\"1\"`\n  hides the whole column, `attrs=\"{'invisible': [...]}\"` empties the cell per\n"
                "  record, and `attrs=\"{'column_invisible': [...]}\"` hides the column from the\n"
                "  `parent.` values of an x2many.",
                v17_="`column_invisible=\"True\"`\n  (or an expression on `parent.` and `context`) hides the whole column,\n"
                "  `invisible` empties the cell per record.",
            ),
            "list_column": version.pick(
                v16_19="",
                v20="\n- `<column string=\"Product\">` with several `<field>`s shows them stacked\n"
                "  under one header.",
            ),
        }

    def view_types(self, version: OdooVersion, list_tag: str) -> str:
        """The root tags available, with the modules that add them."""
        hierarchy = version.pick(v16="", v17_=", `<hierarchy>` (from `web_hierarchy`)")
        card = version.pick(v16_19="", v20=", `<card>`")
        gantt = version.pick(
            v16_17="\n  `gantt` is in the selection but has no view in Community.",
            v18_="",
        )
        return (
            f"`<form>`, `<{list_tag}>`, `<kanban>`{card}, `<search>`, `<calendar>`, `<graph>`,\n"
            f"  `<pivot>`, `<activity>` (from `mail`){hierarchy}; `qweb` is the type of\n"
            f"  `<template>` records.{gantt}"
        )

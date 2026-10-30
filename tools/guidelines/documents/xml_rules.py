"""`odoo-guidelines/guidelines/xml.md`: views, actions and data records."""

from __future__ import annotations

from ..version import OdooVersion
from .lead import GuidedDocument


class XmlRules(GuidedDocument):
    """Our own rules, followed by Odoo's section on anchoring view inheritance."""

    path = "odoo-guidelines/guidelines/xml.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "list_tag": version.pick(v16_17="tree", v18_="list"),
            "sugar_tags": version.pick(
                v16="`<menuitem>` and `<template>`", v17_="`<menuitem>`, `<template>`, and `<asset>`"
            ),
            "active_tags": version.pick(v16="`<template>`", v17_="`<template>`/`<asset>`"),
            "modifiers": self.modifiers(version),
            "chatter": version.pick(
                v16_17="""- The chatter of a form inheriting `mail.thread` goes last:
  `<div class="oe_chatter"><field name="message_follower_ids"/>
  <field name="activity_ids"/><field name="message_ids"/></div>`.""",
                v18_="- The chatter of a form inheriting `mail.thread` is `<chatter/>`, last in the form.",
            ),
            "anchor": self.anchor_section(),
            "removed_tags": version.pick(
                v16="\n- `<report>` and `<act_window>` still load in this version but later versions\n"
                "  drop them: write `<record model=\"ir.actions.report\">` and\n"
                "  `<record model=\"ir.actions.act_window\">`.",
                v17_="\n- There is no `<report>` or `<act_window>` tag: write\n"
                "  `<record model=\"ir.actions.report\">` and `<record model=\"ir.actions.act_window\">`.",
            ),
            "binary_type": version.pick(
                v16_17="`type=\"base64\"` stores the body, or with `file=` the file, base64-encoded.",
                v18_19="`type=\"base64\" file=\"module/static/img/cover.png\"` stores a file\n"
                "  base64-encoded; without `file` it raises.",
                v20="`type=\"bytes\" file=\"module/static/img/cover.png\"` stores a file in a\n"
                "  `Binary` field; `type=\"base64\"` is deprecated.",
            ),
            "attribute_separator": version.pick(
                v16_17="`separator`, default `,`",
                v18_="`separator`, default `,`; on `invisible`, `readonly`, `required`,\n"
                "    `column_invisible` and `decoration-*` the separator must be `and` or `or`,\n"
                "    and the expressions are combined",
            ),
        }

    def modifiers(self, version: OdooVersion) -> str:
        return version.pick(
            v16="""- Dynamic visibility and editability: `attrs="{'invisible': [('state', '!=', 'draft')]}"`
  and `states="draft"` on buttons. Keep the domain short; a field used in
  `attrs` must be in the view (add it `invisible="1"` when needed).""",
            v17_="""- Dynamic visibility and editability are Python expressions on the attribute:
  `invisible="state != 'draft'"`, `readonly="is_locked"`,
  `required="partner_id"`, `column_invisible="parent.state == 'done'"`.
  `attrs` and `states` are refused at install in this version.""",
        )

    def anchor_section(self) -> str:
        """Odoo's section from its heading to the end of the file."""
        upstream = self.read_upstream(self.path)
        return upstream[upstream.index("# Anchor view inheritance"):]

"""`odoo-guidelines/guidelines/xml.md`: views, actions and data records."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class XmlRules(Document):
    """Our own rules, followed by Odoo's section on anchoring view inheritance."""

    path = "odoo-guidelines/guidelines/xml.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "list_tag": version.pick(v16_17="tree", v18_="list"),
            "modifiers": self.modifiers(version),
            "chatter": version.pick(
                v16_17="""- The chatter of a form inheriting `mail.thread` goes last:
  `<div class="oe_chatter"><field name="message_follower_ids"/>
  <field name="activity_ids"/><field name="message_ids"/></div>`.""",
                v18_="- The chatter of a form inheriting `mail.thread` is `<chatter/>`, last in the form.",
            ),
            "anchor": self.anchor_section(),
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

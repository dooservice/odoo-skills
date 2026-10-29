"""The values of `views.md` about kanban views and, where it exists, the card view."""

from __future__ import annotations

from ..version import OdooVersion


class KanbanValues:
    """The record template (`kanban-box`, then `card`), its menu and the kanban attributes."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "kanban_template": version.pick(
                v16="""\
The record template is `<t t-name="kanban-box">` inside `<templates>`; its root
gets `class="oe_kanban_global_click"` so a click opens the record. A
`<t t-name="kanban-tooltip">` template adds a tooltip. Declare every field the
template reads as a `<field>` in the view.""",
                v17="""\
The record template is `<t t-name="kanban-box">` inside `<templates>`; its root
gets `class="oe_kanban_global_click"` so a click opens the record, and a
`<t t-name="kanban-menu">` template fills the record's dropdown menu. Declare
every field the template reads as a `<field>` in the view.""",
                v18="""\
The record template is `<t t-name="card">` inside `<templates>`: the whole card
opens the record, `<aside>` and `<footer>` place a side image and a bottom row,
and a `<t t-name="menu">` template fills the dropdown menu. `kanban-box` and
`kanban-menu` still work with a deprecation warning: write `card` and `menu`.""",
                v19_="""\
The record template is `<t t-name="card">` inside `<templates>`: the whole card
opens the record, `<aside>` and `<footer>` place a side image and a bottom row,
and a `<t t-name="menu">` template fills the dropdown menu. A `kanban-box`
template is refused: write `card` and `menu`.""",
            ),
            "kanban_example": version.pick(
                v16_17="""\
<kanban default_group_by="state">
    <field name="state"/>
    <templates>
        <t t-name="kanban-box">
            <div class="oe_kanban_global_click">
                <strong><field name="name"/></strong>
                <div><field name="author_id"/></div>
            </div>
        </t>
    </templates>
</kanban>""",
                v18_="""\
<kanban default_group_by="state" highlight_color="color">
    <templates>
        <t t-name="card">
            <field name="name" class="fw-bold"/>
            <field name="author_id"/>
            <footer>
                <field name="tag_ids" widget="many2many_tags"/>
            </footer>
        </t>
    </templates>
</kanban>""",
            ),
            "kanban_attributes": version.pick(
                v16_17="",
                v18_=", `highlight_color=\"color\"`\n  (an integer color field), `can_open=\"0\"` (the card does not open the record)",
            ),
            "kanban_card": version.pick(
                v16_19="",
                v20="""
- A `card` view (`<card>` root, `<templates><t t-name="card">`) is a card
  layout several views share: `<kanban card_id="%(library.library_book_view_card)d">`
  inlines it, and so does a calendar's `<popover card_id="...">`. Keep the
  template in the kanban unless two views use it.""",
            ),
        }

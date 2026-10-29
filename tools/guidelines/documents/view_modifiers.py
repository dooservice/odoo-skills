"""The values of `views.md` about `invisible`, `readonly`, `required` and `column_invisible`."""

from __future__ import annotations

from ..version import OdooVersion


class ModifierValues:
    """How a view makes a node depend on the record: domains in `attrs`, then Python expressions."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "modifier_rule": version.pick(
                v16="""\
`attrs` maps `invisible`, `readonly`, `required` or `column_invisible` to a
domain evaluated in the client on the record's values; `parent.<field>` reads
the record that holds an x2many. `states="draft,sent"` on a button or field
shows it only in those states. A plain `invisible`, `readonly` or `required`
is `0` or `1`, or an expression on `context` only. `decoration-*` takes a
Python expression.""",
                v17_="""\
`invisible`, `readonly`, `required` and, on list columns, `column_invisible`
take a Python expression evaluated in the client on the record's values. It
reads the record's fields, `id`, `parent` (the record that holds an x2many),
`context`, `uid`, `current_company_id`, `allowed_company_ids`,
`context_today()`, `today` and `now`. `attrs` and `states` are refused at
install with a `ValidationError`: translate each domain into an expression.""",
            ),
            "modifier_example": version.pick(
                v16="""\
<field name="partner_id" attrs="{'readonly': [('state', '!=', 'draft')],
                                 'required': [('kind', '=', 'loan')]}"/>
<button name="action_confirm" type="object" string="Confirm" states="draft"/>""",
                v17_="""\
<field name="partner_id" readonly="state != 'draft'" required="kind == 'loan'"/>
<button name="action_confirm" type="object" string="Confirm" invisible="state != 'draft'"/>
<!-- in the list of an x2many -->
<field name="price" column_invisible="parent.kind == 'gift'"/>""",
            ),
            "modifier_fields": version.pick(
                v16="""\
Every field that `attrs`, `states`, a `domain`, a `context` or a
`decoration-*` reads must be in the view, or the view fails to load ("must be
present in view"): add it with `invisible="1"`.""",
                v17="""\
Every field that a modifier, a `domain`, a `context` or a `decoration-*` reads
must be in the view, or the view fails to load ("must be present in view"):
add it with `invisible="1"` (`column_invisible="True"` in a list).""",
                v18_="""\
The server adds, invisible and readonly, the fields that a modifier, a
`domain`, a `context` or a `decoration-*` reads and the view lacks: do not add
`invisible="1"` copies of them.""",
            ),
        }

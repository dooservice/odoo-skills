# Imports

PEP 8 applies; Odoo's pylint rules are the reference.

- Four groups, each alphabetically sorted:
  1. stdlib
  2. third-party libs
  3. `odoo` submodules (`from odoo import _, api, fields, models, Command`)
  4. `odoo.addons.*` (only when another module's code is needed)

# Naming and model layout

- Model `_name`: dotted, prefixed by module, **singular** (`sale.order`, not
  `sale.orders`). Transient/wizard: `<base_model>.<action>`. SQL-view report
  model: `<base_model>.report.<action>`.
- A variable holding a model class is PascalCase (`Partner =
  self.env['res.partner']`). Suffix a var holding a record id / list of ids
  with `_id` / `_ids` (don't name a `res.partner` record `partner_id`).
- Method-name patterns: compute `_compute_<field>`, search `_search_<field>`,
  default `_default_<field>`, selection `_selection_<field>`, onchange
  `_onchange_<field>`, constraint `_check_<name>`, object action `action_*`
  (acts on one record, so start it with `self.ensure_one()`).
- Model body order: private attrs (`_name`, `_description`, `_inherit`) -> default
  methods -> field declarations -> `_sql_constraints` -> compute/inverse/search
  (field order) -> selection methods -> `@api.constrains`/`@api.onchange` -> CRUD
  overrides -> action methods -> other business methods.

# Translate only static literals

Translate only **static literals**, passing interpolation values as
arguments; in model code it is `_(...)`, imported from `odoo`.

```python
# good
raise UserError(_("Record %s cannot be modified", record.display_name))

# good (several variables): name them so translators keep them straight
msg = _("%(count)s records imported by %(user)s", count=len(records), user=user.name)

# bad (formats before the lookup): the dynamic string matches no exported term
raise UserError(_("Record %s cannot be modified" % record.display_name))

# bad (formats after the lookup): bypasses placeholder validation and reordering
raise UserError(_("Record %s cannot be modified") % record.display_name)
```

## Why

- Translations are keyed on the exact source literal, at export (building the
  `.pot`) and at runtime lookup. Concatenation, f-strings, or `%`-formatting
  inside `_()` produce strings that exist in neither.
- Named placeholders let translators reorder words per language; passing them
  as arguments lets the framework validate them per translation and apply
  Markup-aware escaping.

## Exceptions and notes

- `_` locates the environment by inspecting the caller's frame: call it inside
  model methods, where `self.env` exists; in plain helper functions pass the
  translated string in from the caller.
- Never call `_()` at module or class level: it runs at import time with no
  user language. Use `_lt` (lazy, from `odoo`) for such constants.
- Field *values* are translated via the field's `translate` flag, never `_()`.
- Prefer `%`-style placeholders over `.format()`.

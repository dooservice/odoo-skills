---
name: odoo-reference
description: >-
  Read before any `odoo-bin shell` script or ORM call for Odoo 16.0, even
  if you know Odoo: names and values change between versions. Every
  model, field, Settings switch and XML id of 16.0 Community. In
  16.0: sale lines `tax_id`; storable product `detailed_type='product'` (`type` follows it); taxes `price_include=True`; payment term lines `value` (`'balance'`, `'percent'`, `'fixed'`) with `days`; UoM `category_id`; fiscal position lines `account.fiscal.position.tax` (`tax_src_id`, `tax_dest_id`); pricelist `compute_price='percentage'`, `discount_policy='without_discount'` shows the discount on the line; time off `hr.leave.type`, `requires_allocation` `'yes'`/`'no'`; expenses in `hr.expense.sheet`; reconciliation models `rule_type`; bank journal `bank_acc_number`; users `groups_id`; scrap `stock.scrap`; chart of accounts `env.ref(...).try_loading(company=company)`. For business flows and configuration, load odoo-functional
  first and use this skill for names.
---

# What Odoo 16.0 has

This skill lists names, not flows. For a business flow or a configuration task
(an `odoo-bin shell` script that creates or changes records, settings, documents),
read the matching recipe of `odoo-functional` first: it gives the order of the steps,
the methods to call and the state each leaves, which a list of fields cannot.

Generated from the Odoo 16.0 source. Do not read these files whole: grep for the
name you need and read only the lines around the match.

## Which file holds what

- `addons.md`: one table row per addon: its technical name, its title, the models it
  defines and the models it extends.
- `models/<addon>.md`: one ``## `model` (defines)`` or ``## `model` (extends)``
  section per model of the addon, with its fields one per line (type, target, label,
  flags, `related` and `compute`), its public methods, and its extension points
  (`_prepare_*`, `_get_*`, `_action_*`, `_create_*`, `_post_*`, `_check_*`).
- `xmlids/<addon>.md`: XML ids grouped by record model under `## ir.ui.view`,
  `## ir.actions.act_window`, `## ir.ui.menu`, `## res.groups`, `## ir.rule` and
  others; a view line says `on <model>` and `inherits <parent view>`.
- `settings.md`: one table row per field of `res.config.settings` and what it is kept
  as: a company field, `parameter` (a system parameter), `group` (given to every
  internal user), `installs` (a module to install) or `computed by`.

## Find a name

Run these from this skill's folder; keep the backticks around a name to match it exactly.

```bash
grep -n '`sale.order`' addons.md                   # addons defining or extending a model
grep -l '^## `sale.order` (defines)' models/*.md   # the addon that defines a model
grep -n '^## `sale.order` ' models/*.md            # every addon that adds to a model
grep -n '`commitment_date`' models/*.md            # a field: file and line
grep -n '^## ' models/sale.md                      # the model sections of that file
grep -n '^- `[a-z_]*date' models/sale.md           # fields whose name has a word
grep -rn '`sale.view_order_form`' xmlids/          # an XML id
grep -rn 'inherits sale.view_order_form' xmlids/   # views extending a view
grep -rn 'on sale.order' xmlids/                   # views of a model
grep -n '`group_discount_per_so_line`' settings.md # a Settings field and how it is kept
grep -in 'discount' settings.md                    # Settings fields by label
```

A field line belongs to the nearest `## ` heading above it: compare its line number
with the headings that `grep -n "^## "` prints for the same file.

Enterprise addons are not here: when a model or XML id is missing, the user may have
Enterprise, and the source is in the addons path.

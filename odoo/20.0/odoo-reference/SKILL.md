---
name: odoo-reference
description: >-
  Every model, field, Settings switch and XML id of Odoo 20.0 Community.
  Look names up here instead of guessing: they change between versions. In
  20.0: sale lines `tax_ids`; product `is_storable`; UoM `relative_factor`; fiscal positions: `original_tax_ids` on the replacement tax; pricelist `compute_price='discount'` with `price_discount` (no `'percentage'`); time off types are `hr.work.entry.type` with `count_as='absence'` (no `hr.leave.type`); expenses `action_submit()`; reconciliation models `trigger`; bank journal `bank_account_number`; companies: `is_company` is computed, no `company_type`; users `group_ids`; scrap: a `stock.move` with `is_scrap` (no `stock.scrap`); parameters `get_int`/`get_str`. For business flows and configuration, load odoo-functional
  first and use this skill for names.
---

# What Odoo 20.0 has

This skill lists names, not flows. For a business flow or a configuration task
(an `odoo-bin shell` script that creates or changes records, settings, documents),
read the matching recipe of `odoo-functional` first: it gives the order of the steps,
the methods to call and the state each leaves, which a list of fields cannot.

Generated from the Odoo 20.0 source. Each file is plain markdown, small enough to
read whole; grep across them when you do not know which addon holds something.

- `addons.md`: every addon, with the models it defines and extends. Start here.
- `models/<addon>.md`: each model of the addon, its fields (type, target, label, flags,
  `related` and `compute`), its public methods, and its extension points
  (`_prepare_*`, `_get_*`, `_action_*`, `_create_*`, `_post_*`, `_check_*`).
- `settings.md`: each field of Settings and what it is kept as — a system parameter, a
  group given to every internal user, a company field, or a module to install.
- `xmlids/<addon>.md`: views (with their model and what they inherit), actions, menus,
  groups, rules and data, by XML id.

```bash
grep -l "sale.order.line" models/*.md        # who touches a model
grep "group_" settings.md                    # settings that give a group
grep "inherits sale.view_order_form" xmlids/*.md   # views extending a form
```

Enterprise addons are not here: when a model or XML id is missing, the user may have
Enterprise, and the source is in the addons path.

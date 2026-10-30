---
name: odoo-reference
description: >-
  Every model, field, Settings switch and XML id of Odoo 16.0 Community.
  Look names up here instead of guessing: they change between versions. In
  16.0: sale lines `tax_id`; product `detailed_type` (`'product'` is storable); payment term lines `value` (`'balance'`, `'percent'`, `'fixed'`) with `days`; UoM `category_id`; fiscal position lines `account.fiscal.position.tax` (`tax_src_id`, `tax_dest_id`); pricelist `compute_price='percentage'` and `discount_policy`; time off `hr.leave.type`, `requires_allocation` `'yes'`/`'no'`; expenses in `hr.expense.sheet`; reconciliation models `rule_type`; bank journal `bank_acc_number`; users `groups_id`; scrap `stock.scrap`; chart of accounts `env.ref(...).try_loading(company=company)`. For business flows and configuration, load odoo-functional
  first and use this skill for names.
---

# What Odoo 16.0 has

This skill lists names, not flows. For a business flow or a configuration task
(an `odoo-bin shell` script that creates or changes records, settings, documents),
read the matching recipe of `odoo-functional` first: it gives the order of the steps,
the methods to call and the state each leaves, which a list of fields cannot.

Generated from the Odoo 16.0 source. Each file is plain markdown, small enough to
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

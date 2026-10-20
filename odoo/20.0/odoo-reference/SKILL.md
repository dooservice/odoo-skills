---
name: odoo-reference
description: >-
  What exists in this Odoo 20.0 Community: every addon's models with their
  fields, public methods and extension points, every Settings switch and where it
  keeps its value, and every XML id an addon declares. Model and field names
  change between versions: use before writing any code, `odoo-bin shell`
  script, API call or configuration for Odoo 20.0 that names a model,
  field, setting, view, action, menu or group, instead of guessing or searching
  the source.
---

# What Odoo 20.0 has

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

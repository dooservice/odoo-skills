# What Odoo 16.0 has

These skills are for Odoo 16.0 and only 16.0. Write for it: an API from another version
fails at install or, worse, silently does nothing. Each row was checked against the
16.0 source.

| Topic | In 16.0 |
| --- | --- |
| Python | 3.7 or newer |
| View modifiers | `attrs="{'invisible': [('state', '!=', 'draft')]}"` and `states="draft,sent"` |
| List view | `<tree>`, view_mode `tree`, xml id `<model>_view_tree` |
| Chatter | `<div class="oe_chatter">` with `message_follower_ids`, `activity_ids`, `message_ids` |
| Record display name | override `name_get()` (returns `[(id, name)]`) |
| Grouped reads | `read_group(domain, fields, groupby, lazy=...)`, returns dicts |
| Field aggregation | `group_operator='sum'` |
| SQL constraints and indexes | `_sql_constraints = [(name, definition, message)]`; indexes with `index=True` or `index='btree_not_null'`/`'trigram'` |
| Domains | lists; combine with `odoo.osv.expression.AND([...])` / `OR([...])` |
| Translations in Python | `from odoo import _, _lt`; `_("...")`, `_lt` for module-level constants |
| Group categories | `category_id` on `res.groups` (an `ir.module.category`) |
| Access rights | `security/ir.model.access.csv` plus `ir.rule` records |
| Route types | `type='http'` or `type='json'` |
| Route auth | `user`, `public`, `none` |
| Default test tags | `at_install`: write `@tagged('post_install', '-at_install')` on business tests |
| QWeb output | `t-out`; `t-esc` still works, `t-raw` logs a deprecation warning |
| Owl | Owl 2 |
| JS module header | every file under `static/src` starts with `/** @odoo-module **/` |
| JS patch | `patch(Target.prototype, "module.name", { ... })` |
| JS field registry | `registry.category("fields").add("x", MyField)`, the component itself |
| JS RPC | `this.rpc = useService("rpc")`; `this.orm = useService("orm")` |
| JS tests | QUnit, under `static/tests/`, in the `web.qunit_suite_tests` bundle |

## When unsure

Confirm against the installed source rather than memory:
`grep -rn "<name>" "$(python3 -c 'import odoo, os; print(os.path.dirname(odoo.__file__))')"`
(the framework and the standard modules are there). A usage in a standard module of the same version is the
best example to follow.

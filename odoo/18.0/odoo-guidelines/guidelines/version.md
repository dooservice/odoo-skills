# What Odoo 18.0 has

These skills are for Odoo 18.0 and only 18.0. Write for it: an API from another version
fails at install or, worse, silently does nothing. Each row was checked against the
18.0 source.

| Topic | In 18.0 |
| --- | --- |
| Python | 3.10 or newer |
| View modifiers | Python expressions on the attribute itself: `invisible="state != 'draft'"`, `readonly=`, `required=`, `column_invisible=`. `attrs` and `states` are refused with a ValidationError |
| List view | `<list>`, view_mode `list`, xml id `<model>_view_list`. `<tree>` and `tree` are gone |
| Chatter | `<chatter/>` at the end of the form |
| Record display name | override `_compute_display_name`; `name_get` does not exist |
| Grouped reads | `_read_group(domain, groupby, aggregates)`, returns tuples; `read_group` stays for the web client |
| Field aggregation | `aggregator='sum'` (`group_operator` is a deprecated alias) |
| SQL constraints and indexes | `_sql_constraints = [(name, definition, message)]`; indexes with `index=True` or `index='btree_not_null'`/`'trigram'` |
| Domains | lists; combine with `odoo.osv.expression.AND([...])` / `OR([...])` |
| Translations in Python | `self.env._("...")`; `_lt = LazyTranslate(__name__)` for module-level constants; bare `_` still works |
| Group categories | `category_id` on `res.groups` (an `ir.module.category`) |
| Access rights | `security/ir.model.access.csv` plus `ir.rule` records |
| Route types | `type='http'` or `type='json'` |
| Route auth | `user`, `public`, `none`, `bearer` |
| Default test tags | `at_install`: write `@tagged('post_install', '-at_install')` on business tests |
| QWeb output | `t-out`; `t-esc` still works, `t-raw` logs a deprecation warning |
| Owl | Owl 2 |
| JS module header | none needed |
| JS patch | `patch(Target.prototype, { ... })` |
| JS field registry | `registry.category("fields").add("x", { component: MyField, ... })` |
| JS RPC | `import { rpc } from "@web/core/network/rpc"`; `useService("orm")` |
| Shared logic | services: `registry.category("services").add("x", { dependencies, start })`, used with `useService("x")` |
| JS tests | hoot (`@odoo/hoot`), `*.test.js` in `web.assets_unit_tests`; QUnit only for legacy suites |

## When unsure

Confirm against the installed source rather than memory:
`grep -rn "<name>" "$(python3 -c 'import odoo, os; print(os.path.dirname(odoo.__file__))')"`
(the framework and the standard modules are there). A usage in a standard module of the same version is the
best example to follow.

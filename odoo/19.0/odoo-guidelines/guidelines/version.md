# What Odoo 19.0 has

These skills are for Odoo 19.0 and only 19.0. Write for it: an API from another version
fails at install or, worse, silently does nothing. Each row was checked against the
19.0 source.

| Topic | In 19.0 |
| --- | --- |
| Python | 3.10 or newer |
| View modifiers | Python expressions on the attribute itself: `invisible="state != 'draft'"`, `readonly=`, `required=`, `column_invisible=`. `attrs` and `states` are refused with a ValidationError |
| List view | `<list>`, view_mode `list`, xml id `<model>_view_list`. `<tree>` and `tree` are gone |
| Chatter | `<chatter/>` at the end of the form |
| Record display name | override `_compute_display_name`; `name_get` does not exist |
| Grouped reads | `_read_group(domain, groupby, aggregates)`, returns tuples; `read_group` is deprecated |
| Field aggregation | `aggregator='sum'` (`group_operator` is a deprecated alias) |
| SQL constraints and indexes | model attributes `_x_check = models.Constraint("CHECK (...)", "msg")`, `models.Index(...)`, `models.UniqueIndex(...)`; `_sql_constraints` is ignored with a warning |
| Domains | `from odoo.fields import Domain`; `Domain(...) & Domain(...)`, `Domain.AND/OR` |
| Translations in Python | `self.env._("...")`; `_lt = LazyTranslate(__name__)` for module-level constants; bare `_` still works |
| Group categories | `privilege_id` on `res.groups` (a `res.groups.privilege`) |
| Access rights | `security/ir.model.access.csv` plus `ir.rule` records |
| Route types | `'http'`, `'jsonrpc'` (`'json'` is a deprecated alias), `'json2'` |
| Route auth | `user`, `public`, `none`, `bearer` |
| Default test tags | `at_install`: write `@tagged('post_install', '-at_install')` on business tests |
| QWeb output | `t-out`; `t-esc` still works, `t-raw` logs a deprecation warning |
| Owl | Owl 2 |
| JS module header | none needed |
| JS patch | `patch(Target.prototype, { ... })` |
| JS field registry | `registry.category("fields").add("x", { component: MyField, ... })` |
| JS RPC | `import { rpc } from "@web/core/network/rpc"`; `useService("orm")` |
| JS tests | hoot (`@odoo/hoot`), `*.test.js` in `web.assets_unit_tests` |

## When unsure

Confirm against the installed source rather than memory:
`grep -rn "<name>" "$(python3 -c 'import odoo, os; print(os.path.dirname(odoo.__file__))')"`
(the framework and the standard modules are there). A usage in a standard module of the same version is the
best example to follow.

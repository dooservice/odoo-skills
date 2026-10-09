# What Odoo 20.0 has

These skills are for Odoo 20.0 and only 20.0. Write for it: an API from another version
fails at install or, worse, silently does nothing. Each row was checked against the
20.0 source.

| Topic | In 20.0 |
| --- | --- |
| Python | 3.12 or newer |
| View modifiers | Python expressions on the attribute itself: `invisible="state != 'draft'"`, `readonly=`, `required=`, `column_invisible=`. `attrs` and `states` are refused with a ValidationError |
| List view | `<list>`, view_mode `list`, xml id `<model>_view_list`. `<tree>` and `tree` are gone |
| Chatter | `<chatter/>` at the end of the form |
| Record display name | override `_compute_display_name`; `name_get` does not exist |
| Grouped reads | `read_group(domain, groupby, aggregates)` and `_read_group`, both return tuples |
| Field aggregation | `aggregator='sum'` |
| SQL constraints and indexes | model attributes `_x_check = models.Constraint("CHECK (...)", "msg")`, `models.Index(...)`, `models.UniqueIndex(...)`; `_sql_constraints` is ignored with a warning |
| Domains | `from odoo.fields import Domain`; `Domain(...) & Domain(...)`, `Domain.AND/OR` |
| Translations in Python | `self.env._("...")`; `_lt = LazyTranslate(__name__)` for module-level constants; bare `_` still works |
| Group categories | `privilege_id` on `res.groups` (a `res.groups.privilege`) |
| Access rights | `security/ir.access.csv` (`ir.access`, one model for ACLs and record rules) |
| Route types | `'http'`, `'jsonrpc'`, `'json2'` |
| Route auth | `user`, `public`, `none`, `bearer` |
| Default test tags | `post_install` |
| QWeb output | `t-out` only; `t-esc` and `t-raw` are gone from server QWeb |
| Owl | Owl 3 (`signal`, `computed`) |
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

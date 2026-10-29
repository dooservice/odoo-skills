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
| Access rights and record rules | `security/ir.model.access.csv` plus record rules as `<record model="ir.rule">` with `domain_force` and `groups` |
| User groups | `group_ids` on `res.users` (groups given explicitly), `all_group_ids` with the implied ones: `user.write({'group_ids': [Command.link(group.id)]})`. `groups_id` is gone |
| System parameters | `env['ir.config_parameter'].sudo().get_param('key', default)` returns a string: convert it (`int(...)`); `set_param('key', value)` writes |
| Route types | `'http'`, `'jsonrpc'` (`'json'` is a deprecated alias), `'json2'` |
| Route auth | `user`, `public`, `none`, `bearer` |
| Default test tags | `at_install`: write `@tagged('post_install', '-at_install')` on business tests |
| QWeb output | `t-out`; `t-esc` still works, `t-raw` logs a deprecation warning |
| Owl | Owl 2 |
| JS module header | none needed |
| JS patch | `patch(Target.prototype, { ... })` |
| JS field registry | `registry.category("fields").add("x", { component: MyField, ... })` |
| JS RPC | `import { rpc } from "@web/core/network/rpc"`; `useService("orm")` |
| Shared logic | services: `registry.category("services").add("x", { dependencies, start })`, used with `useService("x")` |
| JS tests | hoot (`@odoo/hoot`), `*.test.js` in `web.assets_unit_tests` |

Business records, for `odoo-bin shell` scripts and data files (the `odoo-functional`
recipes give the whole flow):

| Topic | In 19.0 |
| --- | --- |
| Company and its contact persons | `res.partner` with `is_company=True` (`company_type='company'` in the form); its people are partners with `parent_id` set to it |
| Automation rules | `base.automation` with its actions in `action_server_ids` (their `base_automation_id`); trigger `on_create_or_write` (`on_write` is deprecated) or a value trigger such as `on_state_set` |
| Bank journal account | `account.journal` with `type='bank'` and `bank_acc_number` (plus `bank_id`), which creates the `res.partner.bank` |
| Loading a chart of accounts | by code: `env['account.chart.template'].try_loading('generic_coa', company)` |
| Pricelist rules | `compute_price`: `fixed`, `percentage` (with `percent_price`), `formula`; `applied_on` written (`3_global`, `1_product`...) |
| Pricelist discount shown on the line | `discount_policy` is gone. A `compute_price='percentage'` rule shows as a discount on sales lines when `sale.group_discount_per_so_line` is on |
| Reconciliation models | `account.reconcile.model` with `trigger`: `manual`, `auto_reconcile`; `rule_type` does not exist |
| Fiscal position tax mapping | on the replacement tax: `fiscal_position_ids` and `original_tax_ids` (the taxes it replaces). `account.fiscal.position.tax`, `tax_src_id` and `tax_dest_id` do not exist |
| Time off types | `hr.leave.type`; `requires_allocation` a boolean (`True`); `allocation_validation_type` `'hr'`, `'manager'`, `'both'`, `'no_validation'` |
| Expense reports | no report: `expense.action_submit()`, `expense.action_approve()`. `hr.expense.sheet` is gone |

## When unsure

Confirm against the installed source rather than memory:
`grep -rn "<name>" "$(python3 -c 'import odoo, os; print(os.path.dirname(odoo.__file__))')"`
(the framework and the standard modules are there). A usage in a standard module of the same version is the
best example to follow.

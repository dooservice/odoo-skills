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
| Access rights and record rules | `security/ir.access.csv` (`ir.access`, one model for ACLs and record rules): a record rule is an `ir.access` row with a `domain`, in the CSV or as `<record model="ir.access">`. `ir.model.access` and `ir.rule` do not exist |
| User groups | `group_ids` on `res.users` (groups given explicitly), `all_group_ids` with the implied ones: `user.write({'group_ids': [Command.link(group.id)]})`. `groups_id` is gone |
| System parameters | typed getters: `env['ir.config_parameter'].sudo().get_int('key', 14)`, `get_bool`, `get_float`, `get_str`; `set_int`, `set_bool`, `set_float`, `set_str` write. `get_param` and `set_param` do not exist |
| Route types | `'http'`, `'jsonrpc'` (`'json'` is a deprecated alias), `'json2'` |
| Route auth | `user`, `public`, `none`, `bearer` |
| Default test tags | `post_install` |
| QWeb output | `t-out` only; `t-esc` and `t-raw` are gone from server QWeb |
| Owl | Owl 3 (`signal`, `computed`) |
| JS module header | none needed |
| JS patch | `patch(Target.prototype, { ... })` |
| JS field registry | `registry.category("fields").add("x", { component: MyField, ... })` |
| JS RPC | `import { rpc } from "@web/core/network/rpc"`; `usePlugin(ORM)`, `ORM` from `@web/core/orm_plugin` |
| Shared logic | plugins: `class X extends Plugin` (`@odoo/owl`), `services.add(X)` (`@web/core/services`), used with `usePlugin(X)`; the `services` registry still starts, after the plugins, for code not moved yet |
| JS tests | hoot (`@odoo/hoot`), `*.test.js` in `web.assets_unit_tests` |

Business records, for `odoo-bin shell` scripts and data files (the `odoo-functional`
recipes give the whole flow):

| Topic | In 20.0 |
| --- | --- |
| Company and its contact persons | `company_type` is gone and `is_company` is computed: a partner without parent and with a real `vat` is a company. Create the company (with its `vat` when known), then its people as partners with `parent_id` set to it |
| Automation rules | `base.automation` with its actions in `action_server_ids` (their `base_automation_id`); trigger `on_create_or_write` (`on_write` is deprecated) or a value trigger such as `on_state_set` |
| Bank journal account | `account.journal` with `type='bank'` and `bank_account_number` (plus `bank_bic`), which creates the `res.partner.bank`; `bank_acc_number` is gone |
| Loading a chart of accounts | by code: `env['account.chart.template'].try_loading('generic_coa', company)` |
| Pricelist rules | `compute_price`: `fixed`, `discount` (with `price_discount`), `markup` (with `price_markup`); `applied_on` is computed. `percentage` and `percent_price` are gone |
| Pricelist discount shown on the line | a plain `compute_price='discount'` rule (`is_plain_discount`) shows as a discount on sales lines when `sale.group_discount_per_so_line` is on |
| Reconciliation models | `account.reconcile.model` with `trigger`: `manual`, `auto_reconcile`; `rule_type` is `reco_model` (default) or `matching_rule` |
| Fiscal position tax mapping | on the replacement tax: `fiscal_position_ids` and `original_tax_ids` (the taxes it replaces). `account.fiscal.position.tax`, `tax_src_id` and `tax_dest_id` do not exist |
| Time off types | `hr.work.entry.type` with `count_as='absence'`; `requires_allocation` a boolean; requests and allocations point to it with `work_entry_type_id`. `hr.leave.type` is gone |
| Expense reports | no report: `expense.action_submit()`, `expense.action_approve()`. `hr.expense.sheet` is gone |

## When unsure

Confirm against the installed source rather than memory:
`grep -rn "<name>" "$(python3 -c 'import odoo, os; print(os.path.dirname(odoo.__file__))')"`
(the framework and the standard modules are there). A usage in a standard module of the same version is the
best example to follow.

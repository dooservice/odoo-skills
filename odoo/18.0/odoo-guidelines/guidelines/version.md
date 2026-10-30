One row per API that differs between versions, grouped by area: find the group of what you are writing, then its row.

Sections of this file:

- [Python, models and the ORM](#python-models-and-the-orm)
- [Views and QWeb](#views-and-qweb)
- [Security](#security)
- [Routes and tests](#routes-and-tests)
- [Web client](#web-client)
- [Business records](#business-records)
- [When unsure](#when-unsure)

# What Odoo 18.0 has

These skills are for Odoo 18.0 and only 18.0. Write for it: an API from another version
fails at install or, worse, silently does nothing. Each row was checked against the
18.0 source.

## Python, models and the ORM

| Topic | In 18.0 |
| --- | --- |
| Python | 3.10 or newer |
| Record display name | override `_compute_display_name`; `name_get` does not exist |
| Grouped reads | `_read_group(domain, groupby, aggregates)`, returns tuples; `read_group` stays for the web client |
| Field aggregation | `aggregator='sum'` (`group_operator` is a deprecated alias) |
| SQL constraints and indexes | `_sql_constraints = [(name, definition, message)]`; indexes with `index=True` or `index='btree_not_null'`/`'trigram'` |
| Domains | lists; combine with `odoo.osv.expression.AND([...])` / `OR([...])` |
| Translations in Python | `self.env._("...")`; `_lt = LazyTranslate(__name__)` for module-level constants; bare `_` still works |
| System parameters | `env['ir.config_parameter'].sudo().get_param('key', default)` returns a string: convert it (`int(...)`); `set_param('key', value)` writes |

## Views and QWeb

| Topic | In 18.0 |
| --- | --- |
| View modifiers | Python expressions on the attribute itself: `invisible="state != 'draft'"`, `readonly=`, `required=`, `column_invisible=`. `attrs` and `states` are refused with a ValidationError |
| List view | `<list>`, view_mode `list`, xml id `<model>_view_list`. `<tree>` and `tree` are gone |
| Chatter | `<chatter/>` at the end of the form |
| QWeb output | `t-out`; `t-esc` still works, `t-raw` logs a deprecation warning |

## Security

| Topic | In 18.0 |
| --- | --- |
| Group categories | `category_id` on `res.groups` (an `ir.module.category`) |
| Access rights and record rules | `security/ir.model.access.csv` plus record rules as `<record model="ir.rule">` with `domain_force` and `groups` |
| User groups | `groups_id` on `res.users` (implied groups included): `user.write({'groups_id': [Command.link(group.id)]})` |

## Routes and tests

| Topic | In 18.0 |
| --- | --- |
| Route types | `type='http'` or `type='json'` |
| Route auth | `user`, `public`, `none`, `bearer` |
| Default test tags | `at_install`: write `@tagged('post_install', '-at_install')` on business tests |

## Web client

| Topic | In 18.0 |
| --- | --- |
| Owl | Owl 2 |
| JS module header | none needed |
| JS patch | `patch(Target.prototype, { ... })` |
| JS field registry | `registry.category("fields").add("x", { component: MyField, ... })` |
| JS RPC | `import { rpc } from "@web/core/network/rpc"`; `useService("orm")` |
| Shared logic | services: `registry.category("services").add("x", { dependencies, start })`, used with `useService("x")` |
| JS tests | hoot (`@odoo/hoot`), `*.test.js` in `web.assets_unit_tests`; QUnit only for legacy suites |

## Business records

For `odoo-bin shell` scripts and data files (the `odoo-functional` recipes give the
whole flow):

| Topic | In 18.0 |
| --- | --- |
| Company and its contact persons | `res.partner` with `is_company=True` (`company_type='company'` in the form); its people are partners with `parent_id` set to it |
| Automation rules | `base.automation` no longer inherits `ir.actions.server`: its actions are `ir.actions.server` records in `action_server_ids` (their `base_automation_id`); trigger `on_create_or_write` (`on_create` and `on_write` are deprecated) or a value trigger such as `on_state_set` |
| Bank journal account | `account.journal` with `type='bank'` and `bank_acc_number` (plus `bank_id`), which creates the `res.partner.bank` |
| Loading a chart of accounts | by code: `env['account.chart.template'].try_loading('generic_coa', company)` |
| Pricelist rules | `compute_price`: `fixed`, `percentage` (with `percent_price`), `formula`; `applied_on` written (`3_global`, `1_product`...) |
| Pricelist discount shown on the line | `discount_policy` is gone. A `compute_price='percentage'` rule shows as a discount on sales lines when `sale.group_discount_per_so_line` is on |
| Reconciliation models | `account.reconcile.model` with `rule_type`: `writeoff_button`, `writeoff_suggestion`, `invoice_matching` |
| Fiscal position tax mapping | lines on the position: `tax_ids` of `account.fiscal.position.tax` (`tax_src_id`, `tax_dest_id`) |
| Time off types | `hr.leave.type`; `requires_allocation` `'yes'`/`'no'`; `allocation_validation_type` `'hr'`, `'manager'`, `'both'`, `'no_validation'` |
| Expense reports | expenses are submitted in a report: `hr.expense.sheet`, then `sheet.action_submit_sheet()`; `expense.action_submit_expenses()` only creates a draft report |

## When unsure

Confirm against the installed source rather than memory:
`grep -rn "<name>" "$(python3 -c 'import odoo, os; print(os.path.dirname(odoo.__file__))')"`
(the framework and the standard modules are there). A usage in a standard module of the same version is the
best example to follow.

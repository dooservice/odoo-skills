One row per API that differs between versions, grouped by area: find the group of what you are writing, then its row.

Sections of this file:

- [Python, models and the ORM](#python-models-and-the-orm)
- [Views and QWeb](#views-and-qweb)
- [Security](#security)
- [Routes and tests](#routes-and-tests)
- [Web client](#web-client)
- [Business records](#business-records)
- [When unsure](#when-unsure)

# What Odoo 16.0 has

These skills are for Odoo 16.0 and only 16.0. Write for it: an API from another version
fails at install or, worse, silently does nothing. Each row was checked against the
16.0 source.

## Python, models and the ORM

| Topic | In 16.0 |
| --- | --- |
| Python | 3.7 or newer |
| Record display name | override `name_get()` (returns `[(id, name)]`) |
| Grouped reads | `read_group(domain, fields, groupby, lazy=...)`, returns dicts |
| Field aggregation | `group_operator='sum'` |
| SQL constraints and indexes | `_sql_constraints = [(name, definition, message)]`; indexes with `index=True` or `index='btree_not_null'`/`'trigram'` |
| Domains | lists; combine with `odoo.osv.expression.AND([...])` / `OR([...])` |
| Translations in Python | `from odoo import _, _lt`; `_("...")`, `_lt` for module-level constants |
| System parameters | `env['ir.config_parameter'].sudo().get_param('key', default)` returns a string: convert it (`int(...)`); `set_param('key', value)` writes |

## Views and QWeb

| Topic | In 16.0 |
| --- | --- |
| View modifiers | `attrs="{'invisible': [('state', '!=', 'draft')]}"` and `states="draft,sent"` |
| List view | `<tree>`, view_mode `tree`, xml id `<model>_view_tree` |
| Chatter | `<div class="oe_chatter">` with `message_follower_ids`, `activity_ids`, `message_ids` |
| QWeb output | `t-out`; `t-esc` still works, `t-raw` logs a deprecation warning |

## Security

| Topic | In 16.0 |
| --- | --- |
| Group categories | `category_id` on `res.groups` (an `ir.module.category`) |
| Access rights and record rules | `security/ir.model.access.csv` plus record rules as `<record model="ir.rule">` with `domain_force` and `groups` |
| User groups | `groups_id` on `res.users` (implied groups included): `user.write({'groups_id': [Command.link(group.id)]})` |

## Routes and tests

| Topic | In 16.0 |
| --- | --- |
| Route types | `type='http'` or `type='json'` |
| Route auth | `user`, `public`, `none` |
| Default test tags | `at_install`: write `@tagged('post_install', '-at_install')` on business tests |

## Web client

| Topic | In 16.0 |
| --- | --- |
| Owl | Owl 2 |
| JS module header | every file under `static/src` starts with `/** @odoo-module **/` |
| JS patch | `patch(Target.prototype, "module.name", { ... })` |
| JS field registry | `registry.category("fields").add("x", MyField)`, the component itself |
| JS RPC | `this.rpc = useService("rpc")`; `this.orm = useService("orm")` |
| Shared logic | services: `registry.category("services").add("x", { dependencies, start })`, used with `useService("x")` |
| JS tests | QUnit, under `static/tests/`, in the `web.qunit_suite_tests` bundle |

## Business records

For `odoo-bin shell` scripts and data files (the `odoo-functional` recipes give the
whole flow):

| Topic | In 16.0 |
| --- | --- |
| Company and its contact persons | `res.partner` with `is_company=True` (`company_type='company'` in the form); its people are partners with `parent_id` set to it |
| Automation rules | `base.automation` delegates to `ir.actions.server` (`action_server_id`, `delegate=True`): `state`, `code` and the other action fields go on the rule itself; trigger `on_write` or `on_create_or_write` with `filter_pre_domain` and `filter_domain` |
| Bank journal account | `account.journal` with `type='bank'` and `bank_acc_number` (plus `bank_id`), which creates the `res.partner.bank` |
| Loading a chart of accounts | on the template record: `env.ref('l10n_generic_coa.configurable_chart_template').try_loading(company=company)`; never a code string |
| Pricelist rules | `compute_price`: `fixed`, `percentage` (with `percent_price`), `formula`; `applied_on` written (`3_global`, `1_product`...) |
| Pricelist discount shown on the line | `discount_policy='without_discount'` on the pricelist, with the setting `group_discount_per_so_line` (in `product`) |
| Reconciliation models | `account.reconcile.model` with `rule_type`: `writeoff_button`, `writeoff_suggestion`, `invoice_matching` |
| Fiscal position tax mapping | lines on the position: `tax_ids` of `account.fiscal.position.tax` (`tax_src_id`, `tax_dest_id`) |
| Time off types | `hr.leave.type`; `requires_allocation` `'yes'`/`'no'`; `allocation_validation_type` `'officer'`/`'no'` |
| Expense reports | expenses are submitted in a report: `hr.expense.sheet` with `expense_line_ids`, then `sheet.action_submit_sheet()` |

## When unsure

Confirm against the installed source rather than memory:
`grep -rn "<name>" "$(python3 -c 'import odoo, os; print(os.path.dirname(odoo.__file__))')"`
(the framework and the standard modules are there). A usage in a standard module of the same version is the
best example to follow.

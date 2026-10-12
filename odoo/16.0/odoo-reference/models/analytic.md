# analytic — Analytic Accounting

Depends on: base, mail, uom.

## `account.analytic.account` (defines)

Analytic Account

Inherits: `mail.thread`

- `name` Char “Analytic Account” (required)
- `code` Char “Reference”
- `active` Boolean “Active”
- `plan_id` Many2one → `account.analytic.plan` “Plan” (required)
- `root_plan_id` Many2one → `account.analytic.plan` “Root Plan” (store, compute=_compute_root_plan)
- `color` Integer “Color Index” (related=plan_id.color)
- `line_ids` One2many → `account.analytic.line` “Analytic Lines”
- `company_id` Many2one → `res.company` “Company”
- `partner_id` Many2one → `res.partner` “Customer”
- `balance` Monetary “Balance” (compute=_compute_debit_credit_balance)
- `debit` Monetary “Debit” (compute=_compute_debit_credit_balance)
- `credit` Monetary “Credit” (compute=_compute_debit_credit_balance)
- `currency_id` Many2one “Currency” (related=company_id.currency_id)

Public methods: `copy_data`, `name_get`, `read_group`

Extension points: `_check_company_consistency`

## `account.analytic.distribution.model` (defines)

Analytic Distribution Model

Inherits: `analytic.mixin`

- `partner_id` Many2one → `res.partner` “Partner”
- `partner_category_id` Many2one → `res.partner.category` “Partner Category”
- `company_id` Many2one → `res.company` “Company”

Public methods: `action_read_distribution_model`

Extension points: `_check_company_accounts`, `_check_score`, `_create_domain`, `_get_distribution`, `_get_fields_to_check`

## `account.analytic.line` (defines)

Analytic Line

- `name` Char “Description” (required)
- `date` Date “Date” (required, index)
- `amount` Monetary “Amount” (required)
- `unit_amount` Float “Quantity”
- `product_uom_id` Many2one → `uom.uom` “Unit of Measure”
- `product_uom_category_id` Many2one “UoM Category” (readonly, related=product_uom_id.category_id)
- `account_id` Many2one → `account.analytic.account` (required, index)
- `partner_id` Many2one → `res.partner` “Partner”
- `user_id` Many2one → `res.users` “User” (index)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `currency_id` Many2one “Currency” (readonly, store, related=company_id.currency_id)
- `plan_id` Many2one → `account.analytic.plan` (readonly, store, related=account_id.plan_id)
- `category` Selection

Extension points: `_check_company_id`

## `analytic.mixin` (defines)

Analytic Mixin

- `analytic_distribution` Json “Analytic” (store, compute=_compute_analytic_distribution)
- `analytic_distribution_search` Json
- `analytic_precision` Integer

Public methods: `create`, `fields_get`, `init`, `read_group`, `write`

## `account.analytic.plan` (defines)

Analytic Plans

- `name` Char (required)
- `description` Text “Description”
- `parent_id` Many2one → `account.analytic.plan` “Parent”
- `parent_path` Char
- `children_ids` One2many → `account.analytic.plan` “Childrens”
- `children_count` Integer “Children Plans Count” (compute=_compute_children_count)
- `complete_name` Char “Complete Name” (store, compute=_compute_complete_name)
- `company_id` Many2one → `res.company` “Company”
- `account_ids` One2many → `account.analytic.account` “Accounts”
- `account_count` Integer “Analytic Accounts Count” (compute=_compute_analytic_account_count)
- `all_account_count` Integer “All Analytic Accounts Count” (compute=_compute_all_analytic_account_count)
- `color` Integer “Color”
- `default_applicability` Selection “Default Applicability” (required)
- `applicability_ids` One2many → `account.analytic.applicability` “Applicability”

Public methods: `action_view_analytical_accounts`, `action_view_children_plans`, `get_relevant_plans`

Extension points: `_get_applicability`, `_get_default`

## `account.analytic.applicability` (defines)

Analytic Plan's Applicabilities

- `analytic_plan_id` Many2one → `account.analytic.plan`
- `business_domain` Selection “Domain” (required)
- `applicability` Selection “Applicability” (required)

Extension points: `_get_score`

## `res.config.settings` (extends)

- `group_analytic_accounting` Boolean “Analytic Accounting”

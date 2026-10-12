# analytic — Analytic Accounting

Depends on: base, mail, uom.

## `account.analytic.account` (defines)

Analytic Account

Inherits: `mail.thread`

- `name` Char “Analytic Account” (required)
- `code` Char “Reference”
- `active` Boolean “Active”
- `plan_id` Many2one → `account.analytic.plan` “Plan” (required)
- `root_plan_id` Many2one → `account.analytic.plan` “Root Plan” (store, related=plan_id.root_id)
- `color` Integer “Color Index” (related=plan_id.color)
- `line_ids` One2many → `account.analytic.line` “Analytic Lines”
- `company_id` Many2one → `res.company` “Company”
- `partner_id` Many2one → `res.partner` “Customer”
- `balance` Monetary “Balance” (compute=_compute_debit_credit_balance)
- `debit` Monetary “Debit” (compute=_compute_debit_credit_balance)
- `credit` Monetary “Credit” (compute=_compute_debit_credit_balance)
- `currency_id` Many2one “Currency” (related=company_id.currency_id)

Public methods: `copy_data`, `write`

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
- `account_id` Many2one → `account.analytic.account` (index)
- `auto_account_id` Many2one → `account.analytic.account` “Analytic Account” (compute=_compute_auto_account)
- `partner_id` Many2one → `res.partner` “Partner”
- `user_id` Many2one → `res.users` “User” (index)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `currency_id` Many2one “Currency” (readonly, store, related=company_id.currency_id)
- `category` Selection

Public methods: `default_get`, `fields_get`

Extension points: `_get_view`

## `analytic.mixin` (defines)

Analytic Mixin

- `analytic_distribution` Json “Analytic Distribution” (store, compute=_compute_analytic_distribution)
- `analytic_distribution_search` Json
- `analytic_precision` Integer
- `distribution_analytic_account_ids` Many2many → `account.analytic.account` (compute=_compute_distribution_analytic_account_ids)

Public methods: `create`, `fields_get`, `filtered_domain`, `init`, `mapped`, `read_group`, `write`

Extension points: `_get_analytic_account_ids`

## `account.analytic.plan` (defines)

Analytic Plans

- `name` Char (required)
- `description` Text “Description”
- `parent_id` Many2one → `account.analytic.plan` “Parent”
- `parent_path` Char
- `root_id` Many2one → `account.analytic.plan` (compute=_compute_root_id)
- `children_ids` One2many → `account.analytic.plan` “Childrens”
- `children_count` Integer “Children Plans Count” (compute=_compute_children_count)
- `complete_name` Char “Complete Name” (store, compute=_compute_complete_name)
- `account_ids` One2many → `account.analytic.account` “Accounts”
- `account_count` Integer “Analytic Accounts Count” (compute=_compute_analytic_account_count)
- `all_account_count` Integer “All Analytic Accounts Count” (compute=_compute_all_analytic_account_count)
- `color` Integer “Color”
- `sequence` Integer
- `default_applicability` Selection “Default Applicability” (required, company_dependent)
- `applicability_ids` One2many → `account.analytic.applicability` “Applicability”

Public methods: `action_view_analytical_accounts`, `action_view_children_plans`, `get_relevant_plans`, `unlink`, `write`

Extension points: `_get_all_plans`, `_get_applicability`

## `account.analytic.applicability` (defines)

Analytic Plan's Applicabilities

- `analytic_plan_id` Many2one → `account.analytic.plan`
- `business_domain` Selection “Domain” (required)
- `applicability` Selection “Applicability” (required)
- `company_id` Many2one → `res.company` “Company”

Extension points: `_get_score`

## `ir.config_parameter` (extends)


Public methods: `write`

## `res.config.settings` (extends)

- `group_analytic_accounting` Boolean “Analytic Accounting”

## `account.analytic.account` (extends)


## `account.analytic.line` (extends)

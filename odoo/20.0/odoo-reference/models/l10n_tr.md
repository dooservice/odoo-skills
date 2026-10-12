# l10n_tr — Türkiye - Accounting

Depends on: account, contacts.

## `account.journal` (extends)

- `l10n_tr_default_sales_return_account_id` Many2one → `account.account` (store, compute=_compute_l10n_tr_default_sales_return_account_id)

## `account.move.line` (extends)


Public methods: `copy_data`

## `ir.http` (extends)


Public methods: `session_info`

## `l10n_tr.tax.office` (defines)

Turkish Tax Office

- `name` Char
- `code` Integer
- `state_id` Many2one → `res.country.state`
- `state_code` Char (related=state_id.code)

## `product.template` (extends)

- `l10n_tr_default_sales_return_account_id` Many2one → `account.account` (company_dependent)

Public methods: `create`

## `res.company` (extends)

- `l10n_tr_tax_office_id` Many2one (related=partner_id.l10n_tr_tax_office_id)

## `res.partner` (extends)

- `l10n_tr_tax_office_id` Many2one → `l10n_tr.tax.office` “Turkish Tax Office”

Extension points: `_get_tax_office_missing_message`, `_get_tax_office_name`

## `account.chart.template` (extends)


Extension points: `_get_tr_account_account`, `_get_tr_account_journal`, `_get_tr_res_company`, `_get_tr_template_data`

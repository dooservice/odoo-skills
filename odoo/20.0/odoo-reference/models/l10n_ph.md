# l10n_ph — Philippines - Accounting

Depends on: account, l10n_account_withholding_tax.

## `account.move` (extends)


Extension points: `_get_name_invoice_report`

## `account.payment` (extends)


Extension points: `_get_aggregated_bill_lines_with_totals`, `_get_payment_journal_entries_with_totals`

## `account.tax` (extends)

- `l10n_ph_atc` Char “Philippines ATC”

## `base.document.layout` (extends)

- `account_fiscal_country_id` Many2one (related=company_id.account_fiscal_country_id)
- `l10n_ph_is_vat_registered` Boolean (related=company_id.l10n_ph_is_vat_registered)

## `res.company` (extends)

- `l10n_ph_branch_code` Char “Company Branch Code” (related=partner_id.l10n_ph_branch_code)
- `l10n_ph_rdo` Char “RDO”
- `l10n_ph_is_vat_registered` Boolean “VAT Registered”

## `res.config.settings` (extends)

- `module_l10n_ph_invoice` Boolean “Discount Privileges on Invoices”
- `module_l10n_ph_sale` Boolean “Discount Privileges on Sale Orders”

## `res.partner` (extends)

- `l10n_ph_branch_code` Char “Branch Code” (store, compute=_compute_branch_code)
- `l10n_ph_entity_type` Selection “Type of Entity”
- `l10n_ph_first_name` Char “First Name” (compute=_l10n_ph_compute_split_name)
- `l10n_ph_middle_name` Char “Middle Name” (compute=_l10n_ph_compute_split_name)
- `l10n_ph_last_name` Char “Last Name” (compute=_l10n_ph_compute_split_name)

## `account.chart.template` (extends)


Extension points: `_get_ph_account_account`, `_get_ph_account_journal`, `_get_ph_res_company`, `_get_ph_template_data`

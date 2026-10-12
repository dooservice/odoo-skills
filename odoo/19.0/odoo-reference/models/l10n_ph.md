# l10n_ph — Philippines - Accounting

Depends on: account, base_vat, l10n_account_withholding_tax.

## `account.move` (extends)


Public methods: `action_open_l10n_ph_2307_wizard`

## `account.payment` (extends)


Public methods: `action_open_l10n_ph_2307_wizard`

## `account.tax` (extends)

- `l10n_ph_atc` Char “Philippines ATC”

## `res.company` (extends)

- `branch_code` Char “Company Branch Code” (related=partner_id.branch_code)
- `l10n_ph_rdo` Char (related=partner_id.l10n_ph_rdo)

## `res.partner` (extends)

- `branch_code` Char “Branch Code” (store, compute=_compute_branch_code)
- `first_name` Char “First Name”
- `middle_name` Char “Middle Name”
- `last_name` Char “Last Name”
- `l10n_ph_rdo` Char “RDO”

## `account.chart.template` (extends)


Extension points: `_get_ph_account_account`, `_get_ph_account_journal`, `_get_ph_res_company`, `_get_ph_template_data`

## `l10n_ph_2307.wizard` (defines)

Exports 2307 data to a XLS file.

- `moves_to_export` Many2many → `account.move` “Joural To Include”
- `xls_file` Binary “Generated file”

Public methods: `action_generate`

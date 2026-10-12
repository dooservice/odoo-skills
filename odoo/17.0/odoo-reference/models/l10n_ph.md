# l10n_ph — Philippines - Accounting

Depends on: account, base_vat.

## `account.move` (extends)


Public methods: `action_open_l10n_ph_2307_wizard`

## `account.payment` (extends)


Public methods: `action_open_l10n_ph_2307_wizard`

## `account.tax` (extends)

- `l10n_ph_atc` Char “Philippines ATC”

## `res.partner` (extends)

- `branch_code` Char “Branch Code” (store, compute=_compute_branch_code)
- `first_name` Char “First Name”
- `middle_name` Char “Middle Name”
- `last_name` Char “Last Name”

## `account.chart.template` (extends)


Extension points: `_get_ph_res_company`, `_get_ph_template_data`

## `l10n_ph_2307.wizard` (defines)

Exports 2307 data to a XLS file.

- `moves_to_export` Many2many → `account.move` “Joural To Include”
- `generate_xls_file` Binary “Generated file”

Public methods: `action_generate`

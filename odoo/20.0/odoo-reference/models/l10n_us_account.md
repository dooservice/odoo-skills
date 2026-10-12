# l10n_us_account — United States - Accounting

Depends on: l10n_us, account, base_address_extended.

## `account.chart.template` (extends)


Extension points: `_get_us_demo_account_move`, `_get_us_demo_account_tax`, `_get_us_demo_account_tax_group`, `_get_us_demo_res_partner`, `_post_load_demo_data`

## `account.tax` (extends)

- `l10n_us_jurisdiction_type` Selection “Jurisdiction Type”
- `l10n_us_state_id` Many2one → `res.country.state` “State”
- `l10n_us_county_id` Many2one → `l10n_us.res.county` “County”
- `l10n_us_city_id` Many2one → `res.city` “City”
- `l10n_us_exempt_tax_ids` One2many → `account.tax` “Exempt Tax”
- `l10n_us_nontaxable_tax_ids` One2many → `account.tax` “Nontaxable Tax”
- `l10n_us_exempt_parent_tax_id` Many2one → `account.tax` “Exempt For”
- `l10n_us_nontaxable_parent_tax_id` Many2one → `account.tax` “Nontaxable For”

Extension points: `_check_l10n_us_parent_tax_id`, `_prepare_base_line_tax_repartition_grouping_key`

## `res.config.settings` (extends)

- `module_l10n_us_direct_deposit` Boolean “U.S. Direct Deposit (via Wise)”

## `res.partner.bank` (extends)

- `intermediary_bank_bic` Char “Intermediary SWIFT”
- `show_intermediary_bank_bic` Boolean (compute=_compute_show_intermediary_bank_bic)

## `account.chart.template` (extends)


Extension points: `_get_accounts_data_values`, `_get_us_account_account`, `_get_us_res_company`, `_get_us_template_data`

# l10n_pk — Pakistan - Accounting

Depends on: account, account_tax_python, l10n_account_withholding_tax, product.

## `account.chart.template` (extends)


Extension points: `_post_load_demo_data`

## `account.journal` (extends)


Extension points: `_get_onboarding_action_data`

## `account.tax` (extends)

- `l10n_pk_is_further_tax` Boolean “Is Further Tax”

## `res.company` (extends)

- `l10n_pk_iap_server_ip` Char “Odoo Static IP Address” (compute=_compute_l10n_pk_iap_server_ip)

Extension points: `_get_iap_server_ip`

## `res.config.settings` (extends)

- `l10n_pk_iap_server_ip` Char (related=company_id.l10n_pk_iap_server_ip)

Public methods: `action_refresh_l10n_pk_iap_server_ip`

## `account.chart.template` (extends)


Extension points: `_get_account_parent_xmlid`, `_get_pk_account_account`, `_get_pk_res_company`, `_get_pk_template_data`

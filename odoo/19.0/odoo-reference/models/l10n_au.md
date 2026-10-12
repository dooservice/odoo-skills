# l10n_au — Australia - Accounting

Depends on: account.

## `account.move` (extends)


Extension points: `_get_automatic_balancing_account`, `_get_name_invoice_report`

## `account.payment` (extends)


## `res.company` (extends)

- `l10n_au_is_gst_registered` Boolean “Australia GST registered”
- `l10n_au_trading_name` Char “Trading Name”

## `res.partner` (extends)


Extension points: `_get_company_registry_labels`

## `res.partner.bank` (extends)

- `aba_bsb` Char “BSB”

Extension points: `_get_supported_account_types`

## `account.chart.template` (extends)


Extension points: `_get_au_account_account`, `_get_au_res_company`, `_get_au_template_data`

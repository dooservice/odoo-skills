# l10n_fi — Finnish Localization

Depends on: account, base_iban, base_vat.

## `account.journal` (extends)

- `invoice_reference_model` Selection

## `account.move` (extends)


Public methods: `compute_payment_reference_finnish`, `compute_payment_reference_finnish_rf`, `get_finnish_check_digit`, `get_rf_check_digits`, `number2numeric`

Extension points: `_get_invoice_reference_fi_invoice`, `_get_invoice_reference_fi_partner`, `_get_invoice_reference_fi_rf_invoice`, `_get_invoice_reference_fi_rf_partner`

# l10n_ec_sale — Ecuador - Sale

Depends on: l10n_ec, sale.

## `payment.method` (extends)

- `l10n_ec_sri_payment_id` Many2one → `l10n_ec.sri.payment` “SRI Payment Method”
- `fiscal_country_codes` Char

Extension points: `_get_fiscal_country_codes`

## `sale.order` (extends)

- `l10n_ec_sri_payment_id` Many2one → `l10n_ec.sri.payment` “Payment Method (SRI)”

Extension points: `_create_invoices`, `_prepare_invoice`

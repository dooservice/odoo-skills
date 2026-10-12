# l10n_ec_website_sale — Ecuadorian Website

Depends on: website_sale, l10n_ec.

## `payment.method` (extends)

- `l10n_ec_sri_payment_id` Many2one → `l10n_ec.sri.payment` “SRI Payment Method”
- `fiscal_country_codes` Char

Extension points: `_get_fiscal_country_codes`

## `sale.order` (extends)


Extension points: `_create_invoices`

## `website` (extends)

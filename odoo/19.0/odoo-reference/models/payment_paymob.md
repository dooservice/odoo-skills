# payment_paymob — Payment Provider: Paymob

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `paymob_account_country_id` Many2one → `res.country` “Paymob Account Country”
- `paymob_public_key` Char “Paymob Public Key”
- `paymob_secret_key` Char “Paymob Secret Key”
- `paymob_hmac_key` Char “Paymob HMAC Key”
- `paymob_api_key` Char “Paymob API Key”

Public methods: `action_sync_paymob_payment_methods`

Extension points: `_check_available_country_currency_ids`, `_get_default_payment_method_codes`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`

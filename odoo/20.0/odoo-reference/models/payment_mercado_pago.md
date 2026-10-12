# payment_mercado_pago — Payment Provider: Mercado Pago

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `mercado_pago_account_country_id` Many2one → `res.country` “Mercado Pago Account Country”
- `mercado_pago_access_token` Char “Mercado Pago Access Token”
- `mercado_pago_access_token_expiry` Datetime “Mercado Pago Access Token Expiry”
- `mercado_pago_refresh_token` Char “Mercado Pago Refresh Token”
- `mercado_pago_public_key` Char “Mercado Pago Public Key”

Public methods: `action_start_onboarding`

Extension points: `_check_currency_is_supported`, `_check_mercado_pago_credentials_are_set_before_allowing_tokenization`, `_check_mercado_pago_credentials_are_set_if_live`, `_get_default_payment_method_codes`, `_get_reset_values`

## `payment.token` (extends)

- `mercado_pago_customer_id` Char (readonly)

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`

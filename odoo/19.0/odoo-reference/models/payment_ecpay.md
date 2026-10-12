# payment_ecpay — Payment Provider: ECPay

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `ecpay_merchant_id` Char “ECPay Merchant ID”
- `ecpay_hash_key` Char “ECPay Secure Hash Key”
- `ecpay_hash_iv` Char “ECPay Secure Hash IV”

Extension points: `_check_currency_is_supported`, `_get_default_payment_method_codes`, `_get_supported_currencies`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`

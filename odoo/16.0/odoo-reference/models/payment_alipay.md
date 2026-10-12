# payment_alipay — Payment Provider: Alipay

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `alipay_payment_method` Selection “Account”
- `alipay_merchant_partner_id` Char “Merchant Partner ID”
- `alipay_md5_signature_key` Char “MD5 Signature Key”
- `alipay_seller_email` Char “Alipay Seller Email”

Extension points: `_get_compatible_providers`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`

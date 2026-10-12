# pos_bancontact_pay — POS Bancontact Pay & Wero

Depends on: point_of_sale.

## `account.journal` (extends)


Extension points: `_check_currency`

## `pos.config` (extends)


Extension points: `_check_bancontact_payment_methods`

## `pos.payment` (extends)

- `bancontact_id` Char “Bancontact ID” (readonly)

Extension points: `_get_additional_payment_fields`

## `pos.payment.method` (extends)

- `bancontact_api_key` Char “Bancontact API Key”
- `bancontact_ppid` Char “Bancontact PPID”
- `bancontact_test_mode` Boolean “Preprod”
- `bancontact_usage` Selection “QR Usage” (required)

Public methods: `cancel_bancontact_payment`, `create_bancontact_payment`, `download_bancontact_sticker`

Extension points: `_check_bancontact_currency`, `_check_bancontact_sticker_one_pos_config`, `_get_bancontact_api_url`, `_get_callback_url`, `_get_external_qr_provider_selection`, `_prepare_bancontact_payment_request`, `_prepare_display_payment_request`, `_prepare_sticker_payment_request`

## `res.company` (extends)


Extension points: `_check_currency`

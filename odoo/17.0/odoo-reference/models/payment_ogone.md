# payment_ogone — Payment Provider: Ogone

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `ogone_pspid` Char “PSPID”
- `ogone_userid` Char “API User ID”
- `ogone_password` Char “API User Password”
- `ogone_shakey_in` Char “SHA Key IN”
- `ogone_shakey_out` Char “SHA Key OUT”
- `ogone_hash_function` Selection “Hash function”

Public methods: `action_open_worldline_provider`

Extension points: `_get_compatible_providers`, `_get_default_payment_method_codes`

## `payment.token` (extends)


Public methods: `write`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`, `_get_tx_from_notification_data`

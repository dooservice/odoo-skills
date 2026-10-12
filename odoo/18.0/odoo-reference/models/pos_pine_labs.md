# pos_pine_labs — POS Pine Labs

Depends on: point_of_sale.

## `pos.payment` (extends)

- `pine_labs_plutus_transaction_ref` Char “Pine Labs PlutusTransactionReferenceID”

## `pos.payment.method` (extends)

- `pine_labs_merchant` Char “Pine Labs Merchant ID”
- `pine_labs_store` Char “Pine Labs Store ID”
- `pine_labs_client` Char “Pine Labs Client ID”
- `pine_labs_security_token` Char “Pine Labs Security Token”
- `pine_labs_allowed_payment_mode` Selection “Pine Labs Allowed Payment Modes”
- `pine_labs_test_mode` Boolean “Pine Labs Test Mode”

Public methods: `pine_labs_cancel_payment_request`, `pine_labs_fetch_payment_status`, `pine_labs_make_payment_request`

Extension points: `_check_pine_labs_terminal`, `_get_payment_terminal_selection`

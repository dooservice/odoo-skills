# pos_paytm — POS PayTM

Depends on: point_of_sale.

## `pos.payment.method` (extends)

- `paytm_tid` Char “PayTM Terminal ID”
- `channel_id` Char “PayTM Channel ID”
- `accept_payment` Selection
- `allowed_payment_modes` Selection
- `paytm_mid` Char “PayTM Merchant ID”
- `paytm_merchant_key` Char “PayTM Merchant API Key”
- `paytm_test_mode` Boolean “PayTM Test Mode”

Public methods: `paytm_fetch_payment_status`, `paytm_make_payment_request`

Extension points: `_check_paytm_terminal`, `_get_payment_terminal_selection`

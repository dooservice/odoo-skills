# pos_paytm — POS PayTM

Depends on: point_of_sale.

## `pos.payment` (extends)

- `paytm_authcode` Char “Paytm APPR Code”
- `paytm_issuer_card_no` Char “Paytm Issue Mask Card No.”
- `paytm_issuer_bank` Char “Paytm Issuer Bank”
- `paytm_payment_method` Char “Paytm Payment Method”
- `paytm_reference_no` Char “Paytm Merchant Reference No.”
- `paytm_card_scheme` Char “Paytm Card Scheme”

## `pos.order` (extends)


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

# pos_dpopay — PoS DPO Pay

Depends on: point_of_sale.

## `pos.payment` (extends)

- `dpopay_rrn` Char “RRN”
- `dpopay_transaction_ref` Char “Transaction Reference”
- `dpopay_mobile_money_phone` Char “Mobile Money Phone Number(Last 4 Digit)”

## `pos.payment.method` (extends)

- `dpopay_client_id` Char “DPO Pay Client ID”
- `dpopay_client_secret` Char “DPO Pay Client Secret”
- `dpopay_mid` Char “DPO Pay Merchant ID”
- `dpopay_tid` Char “DPO Pay Terminal ID”
- `dpopay_payment_mode` Selection
- `dpopay_chain_id` Char “DPO Pay Chain-ID”
- `dpopay_test_mode` Boolean “Enable Test Mode”
- `dpopay_bearer_token` Char

Public methods: `send_dpopay_request`

Extension points: `_get_dpopay_base_url`, `_get_terminal_provider_selection`, `_get_transaction_type`

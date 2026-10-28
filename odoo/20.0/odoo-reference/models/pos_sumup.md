# pos_sumup — POS SumUp

Depends on: point_of_sale.

## `pos.payment.method` (extends)

- `sumup_api_key` Char “SumUp API key”
- `sumup_merchant_code` Char
- `sumup_terminal_id` Char “Reader ID”
- `sumup_pairing_code` Char “Pairing Code”

Public methods: `create`, `sumup_cancel`, `sumup_get_checkout_status`, `sumup_pay`, `sumup_refund`, `write`

Extension points: `_check_sumup_access`, `_check_sumup_terminal_id`, `_get_terminal_provider_selection`

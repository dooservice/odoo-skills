# pos_qfpay — POS QFPay

Depends on: point_of_sale.

## `pos.payment.method` (extends)

- `qfpay_terminal_ip_address` Char “QFPay Terminal IP Address”
- `qfpay_pos_key` Char “QFPay POS Key”
- `qfpay_notification_key` Char “QFPay Notification Key”
- `qfpay_latest_response` Char
- `qfpay_payment_type` Selection

Public methods: `qfpay_sign_request`

Extension points: `_check_qfpay_terminal`, `_get_payment_terminal_selection`

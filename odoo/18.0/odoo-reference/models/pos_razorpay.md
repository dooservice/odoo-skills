# pos_razorpay — POS Razorpay

Depends on: point_of_sale.

## `pos.payment` (extends)

- `razorpay_reverse_ref_no` Char “Razorpay Reverse Reference No.”

## `pos.payment.method` (extends)

- `razorpay_tid` Char “Razorpay Device Serial No”
- `razorpay_allowed_payment_modes` Selection
- `razorpay_username` Char “Razorpay Username”
- `razorpay_api_key` Char “Razorpay API Key”
- `razorpay_test_mode` Boolean “Razorpay Test Mode”

Public methods: `razorpay_cancel_payment_request`, `razorpay_fetch_payment_status`, `razorpay_make_payment_request`

Extension points: `_check_razorpay_terminal`, `_get_payment_terminal_selection`

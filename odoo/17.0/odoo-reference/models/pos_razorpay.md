# pos_razorpay — POS Razorpay

Depends on: point_of_sale.

## `pos.payment` (extends)

- `razorpay_authcode` Char “Razorpay APPR Code”
- `razorpay_issuer_card_no` Char “Razorpay Issue Card No Last 4 digits”
- `razorpay_issuer_bank` Char “Razorpay Issuer Bank”
- `razorpay_payment_method` Char “Razorpay Payment Method”
- `razorpay_reference_no` Char “Razorpay Merchant Reference No.”
- `razorpay_reverse_ref_no` Char “Razorpay Reverse Reference No.”
- `razorpay_card_scheme` Char “Razorpay Card Scheme”
- `razorpay_card_owner_name` Char “Razorpay Card Owner Name”

## `pos.order` (extends)


## `pos.payment.method` (extends)

- `razorpay_tid` Char “Razorpay Device Serial No”
- `razorpay_allowed_payment_modes` Selection
- `razorpay_username` Char “Razorpay Username”
- `razorpay_api_key` Char “Razorpay API Key”
- `razorpay_test_mode` Boolean “Razorpay Test Mode”

Public methods: `razorpay_cancel_payment_request`, `razorpay_fetch_payment_status`, `razorpay_make_payment_request`

Extension points: `_check_razorpay_terminal`, `_get_payment_terminal_selection`

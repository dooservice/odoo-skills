# pos_stripe — POS Stripe

Depends on: point_of_sale, payment_stripe.

## `pos.payment.method` (extends)

- `stripe_serial_number` Char

Public methods: `action_stripe_key`, `stripe_capture_payment`, `stripe_connection_token`, `stripe_payment_intent`, `stripe_refund`

Extension points: `_check_stripe_serial_number`, `_get_stripe_payment_provider`, `_get_terminal_provider_selection`

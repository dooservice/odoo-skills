# pos_mollie — POS Mollie

Depends on: point_of_sale, payment_mollie.

## `pos.payment.method` (extends)

- `mollie_terminal_id` Char “Mollie Terminal ID”
- `mollie_payment_provider_id` Many2one → `payment.provider`

Public methods: `mollie_cancel_payment`, `mollie_create_payment`, `mollie_create_refund`, `mollie_get_payment`

Extension points: `_get_payment_terminal_selection`

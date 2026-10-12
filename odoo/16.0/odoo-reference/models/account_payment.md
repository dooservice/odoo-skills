# account_payment — Payment - Account

Depends on: account, payment.

## `account.journal` (extends)


Extension points: `_get_available_payment_method_lines`

## `account.move` (extends)

- `transaction_ids` Many2many → `payment.transaction` “Transactions” (readonly)
- `authorized_transaction_ids` Many2many → `payment.transaction` “Authorized Transactions” (readonly, compute=_compute_authorized_transaction_ids)
- `amount_paid` Monetary “Amount paid” (compute=_compute_amount_paid)

Public methods: `action_view_payment_transactions`, `get_portal_last_transaction`, `payment_action_capture`, `payment_action_void`

Extension points: `_get_default_payment_link_values`

## `account.payment` (extends)

- `payment_transaction_id` Many2one → `payment.transaction` “Payment Transaction” (readonly)
- `payment_token_id` Many2one → `payment.token` “Saved Payment Token”
- `amount_available_for_refund` Monetary (compute=_compute_amount_available_for_refund)
- `suitable_payment_token_ids` Many2many → `payment.token` (compute=_compute_suitable_payment_token_ids)
- `use_electronic_payment_method` Boolean (compute=_compute_use_electronic_payment_method)
- `source_payment_id` Many2one → `account.payment` “Source Payment” (readonly, store, related=payment_transaction_id.source_transaction_id.payment_id)
- `refunds_count` Integer “Refunds Count” (compute=_compute_refunds_count)

Public methods: `action_post`, `action_refund_wizard`, `action_view_refunds`

Extension points: `_create_payment_transaction`, `_get_payment_refund_wizard_values`, `_prepare_payment_transaction_vals`

## `account.payment.method` (extends)


Extension points: `_get_payment_method_information`

## `account.payment.method.line` (extends)

- `payment_provider_id` Many2one → `payment.provider` (store, compute=_compute_payment_provider_id)
- `payment_provider_state` Selection (related=payment_provider_id.state)

Public methods: `action_open_provider_form`

## `payment.provider` (extends)

- `journal_id` Many2one → `account.journal` “Payment Journal” (compute=_compute_journal_id)

Extension points: `_check_existing_payment_method_lines`, `_get_default_payment_method_id`, `_get_provider_payment_method`

## `payment.transaction` (extends)

- `payment_id` Many2one → `account.payment` “Payment” (readonly)
- `invoice_ids` Many2many → `account.move` “Invoices” (readonly)
- `invoices_count` Integer “Invoices Count” (compute=_compute_invoices_count)

Public methods: `action_view_invoices`

Extension points: `_create_payment`

## `account.payment.register` (extends)

- `payment_token_id` Many2one → `payment.token` “Saved payment token” (store, compute=_compute_payment_token_id)
- `suitable_payment_token_ids` Many2many → `payment.token` (compute=_compute_suitable_payment_token_ids)
- `use_electronic_payment_method` Boolean (compute=_compute_use_electronic_payment_method)
- `payment_method_code` Char (related=payment_method_line_id.code)

Extension points: `_create_payment_vals_from_wizard`

## `payment.link.wizard` (extends)


Extension points: `_get_additional_link_values`

## `payment.refund.wizard` (defines)

Payment Refund Wizard

- `payment_id` Many2one → `account.payment` “Payment” (readonly)
- `transaction_id` Many2one “Payment Transaction” (related=payment_id.payment_transaction_id)
- `payment_amount` Monetary “Payment Amount” (related=payment_id.amount)
- `refunded_amount` Monetary “Refunded Amount” (compute=_compute_refunded_amount)
- `amount_available_for_refund` Monetary “Maximum Refund Allowed” (related=payment_id.amount_available_for_refund)
- `amount_to_refund` Monetary “Refund Amount” (store, compute=_compute_amount_to_refund)
- `currency_id` Many2one “Currency” (related=transaction_id.currency_id)
- `support_refund` Selection (related=transaction_id.provider_id.support_refund)
- `has_pending_refund` Boolean “Has a pending refund” (compute=_compute_has_pending_refund)

Public methods: `action_refund`

Extension points: `_check_amount_to_refund_within_boundaries`

# account_payment — Payment - Account

Depends on: account, payment.

## `account.bank.statement.line` (extends)


Extension points: `_get_partial_amounts`

## `account.journal` (extends)


Extension points: `_get_available_payment_method_lines`

## `account.move` (extends)

- `transaction_ids` Many2many → `payment.transaction` “Transactions” (readonly)
- `authorized_transaction_ids` Many2many → `payment.transaction` “Authorized Transactions” (readonly, compute=_compute_authorized_transaction_ids)
- `transaction_count` Integer “Transaction Count” (compute=_compute_transaction_count)
- `amount_paid` Monetary “Amount paid” (compute=_compute_amount_paid)

Public methods: `action_view_payment_transactions`, `get_portal_last_transaction`, `payment_action_capture`, `payment_action_void`

Extension points: `_get_default_payment_link_values`, `_get_online_payment_error`, `_get_portal_payment_link`

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

Extension points: `_check_existing_payment`, `_get_payment_method_outstanding_account_id`, `_get_provider_payment_method`

## `payment.transaction` (extends)

- `payment_id` Many2one → `account.payment` “Payment” (readonly)
- `invoice_ids` Many2many → `account.move` “Invoices” (readonly)
- `invoices_count` Integer “Invoices Count” (compute=_compute_invoices_count)

Public methods: `action_view_invoices`

Extension points: `_create_payment`, `_get_invoices_to_notify`, `_post_process`

## `account.payment.register` (extends)

- `payment_token_id` Many2one → `payment.token` “Saved payment token” (store, compute=_compute_payment_token_id)
- `suitable_payment_token_ids` Many2many → `payment.token` (compute=_compute_suitable_payment_token_ids)
- `use_electronic_payment_method` Boolean (compute=_compute_use_electronic_payment_method)

Extension points: `_create_payment_vals_from_wizard`

## `payment.link.wizard` (extends)

- `invoice_amount_due` Monetary “Amount Due” (compute=_compute_invoice_amount_due)
- `open_installments` Json
- `open_installments_preview` Html (compute=_compute_open_installments_preview)
- `display_open_installments` Boolean (compute=_compute_display_open_installments)
- `has_eligible_epd` Boolean
- `discount_date` Date
- `epd_info` Char “Early Payment Discount Information” (compute=_compute_epd_info)

Extension points: `_prepare_access_token`, `_prepare_anchor`, `_prepare_query_params`, `_prepare_url`

## `payment.refund.wizard` (defines)

Payment Refund Wizard

- `payment_id` Many2one → `account.payment` “Payment” (readonly)
- `transaction_id` Many2one “Payment Transaction” (related=payment_id.payment_transaction_id)
- `payment_amount` Monetary “Payment Amount” (related=payment_id.amount)
- `refunded_amount` Monetary “Refunded Amount” (compute=_compute_refunded_amount)
- `amount_available_for_refund` Monetary “Maximum Refund Allowed” (related=payment_id.amount_available_for_refund)
- `amount_to_refund` Monetary “Refund Amount” (store, compute=_compute_amount_to_refund)
- `currency_id` Many2one “Currency” (related=transaction_id.currency_id)
- `support_refund` Selection “Refund” (compute=_compute_support_refund)
- `has_pending_refund` Boolean “Has a pending refund” (compute=_compute_has_pending_refund)

Public methods: `action_refund`

Extension points: `_check_amount_to_refund_within_boundaries`

## `res.config.settings` (extends)

- `pay_invoices_online` Boolean

# payment — Payment Engine

Depends on: onboarding, portal.

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`

## `ir.websocket` (extends)


Extension points: `_get_transaction_from_channel`

## `payment.data` (defines)

Pending payment data payload to process

- `transaction_id` Many2one → `payment.transaction` “Transaction” (required, index)
- `payload` Json “Payload” (required)
- `errored` Boolean “Failed”
- `error_traceback` Text “Error Traceback”

Extension points: `_post_process_transaction`

## `payment.method` (defines)

Payment Method

- `name` Char “Name” (required)
- `code` Char “Code” (required)
- `sequence` Integer “Sequence”
- `primary_payment_method_id` Many2one → `payment.method` “Primary Payment Method”
- `brand_ids` One2many → `payment.method` “Brands”
- `is_primary` Boolean “Is Primary Payment Method” (compute=_compute_is_primary)
- `provider_id` Many2one → `payment.provider` “Provider” (required, index)
- `active` Boolean “Active”
- `image` Image “Image” (required)
- `image_payment_form` Image “The resized image displayed on the payment form.” (store, related=image)
- `support_tokenization` Boolean “Tokenization”
- `support_express_checkout` Boolean “Express Checkout”
- `support_manual_capture` Selection “Manual Capture” (required)
- `support_refund` Selection “Refund” (required)
- `supported_country_ids` Many2many → `res.country` “Countries”
- `supported_currency_ids` Many2many → `res.currency` “Currencies”
- `allow_amount_selection` Boolean “Amount Selection”

Public methods: `write`

Extension points: `_check_manual_capture_supported_by_provider`

## `payment.provider` (defines)

Payment Provider

- `name` Char “Name” (required)
- `code` Selection “Code” (required)
- `is_live` Boolean “Live”
- `is_published` Boolean “Published”
- `active` Boolean “Active”
- `sequence` Integer “Sequence”
- `image_128` Image “Logo”
- `payment_method_ids` One2many → `payment.method` “Supported Payment Methods”
- `primary_payment_method_ids` One2many → `payment.method` “Primary Payment Methods” (compute=_compute_primary_payment_method_ids)
- `payment_transaction_ids` One2many → `payment.transaction` “Payment Transactions”
- `processed_amount` Monetary “Processed Amount” (compute=_compute_processed_amount)
- `transaction_count` Integer “Transaction Count” (compute=_compute_transaction_count)
- `payment_token_ids` One2many → `payment.token` “Payment Tokens”
- `token_count` Integer “Token Count” (compute=_compute_token_count)
- `support_tokenization` Boolean “Tokenization” (compute=_compute_feature_support_fields)
- `support_express_checkout` Boolean “Express Checkout” (compute=_compute_feature_support_fields)
- `support_manual_capture` Selection “Manual Capture Supported” (compute=_compute_feature_support_fields)
- `support_refund` Selection “Refund” (compute=_compute_feature_support_fields)
- `allow_tokenization` Boolean “Allow Saving Payment Methods”
- `allow_express_checkout` Boolean “Allow Express Checkout”
- `capture_manually` Boolean “Capture Amount Manually”
- `company_id` Many2one → `res.company` “Company” (required, index)
- `main_currency_id` Many2one (related=company_id.currency_id)
- `minimum_amount` Monetary “Minimum Amount”
- `maximum_amount` Monetary “Maximum Amount”
- `available_currency_ids` Many2many → `res.currency` “Currencies” (store, compute=_compute_available_currency_ids)
- `available_country_ids` Many2many → `res.country` “Countries”
- `pre_msg` Html “Help Message”
- `pending_msg` Html “Pending Message”
- `auth_msg` Html “Authorize Message”
- `done_msg` Html “Done Message”
- `cancel_msg` Html “Cancelled Message”
- `redirect_form_view_id` Many2one → `ir.ui.view` “Redirect Form Template”
- `inline_form_view_id` Many2one → `ir.ui.view` “Inline Form Template”
- `token_inline_form_view_id` Many2one → `ir.ui.view` “Token Inline Form Template”
- `express_checkout_form_view_id` Many2one → `ir.ui.view` “Express Checkout Form Template”
- `module_id` Many2one → `ir.module.module` “Corresponding Module”
- `module_state` Selection “Installation State” (related=module_id.state)
- `module_to_buy` Boolean “Odoo Enterprise Module” (related=module_id.to_buy)

Public methods: `action_add_payment_method`, `action_reset_credentials`, `action_start_onboarding`, `action_toggle_is_published`, `action_view_payment_tokens`, `action_view_payment_transactions`, `button_immediate_install`, `copy`, `copy_data`, `create`, `write`

Extension points: `_check_manual_capture_supported_by_payment_methods`, `_check_required_if_provider`, `_get_code`, `_get_default_payment_method_codes`, `_get_pm_from_code`, `_get_provider_domain`, `_get_redirect_form_view`, `_get_removal_values`, `_get_reset_values`, `_get_supported_currencies`, `_get_validation_amount`, `_get_validation_currency`

## `payment.token` (defines)

Payment Token

- `provider_id` Many2one → `payment.provider` “Provider” (required, index)
- `provider_code` Selection “Provider Code” (related=provider_id.code)
- `company_id` Many2one (store, index, related=provider_id.company_id)
- `payment_method_id` Many2one → `payment.method` “Payment Method” (required, readonly, index)
- `payment_method_code` Char “Payment Method Code” (related=payment_method_id.code)
- `payment_details` Char “Payment Details”
- `partner_id` Many2one → `res.partner` “Partner” (required, index)
- `provider_ref` Char “Provider Reference” (required)
- `transaction_ids` One2many → `payment.transaction` “Payment Transactions”
- `active` Boolean “Active”

Public methods: `create`, `get_linked_records_info`, `write`

Extension points: `_check_partner_is_never_public`, `_get_specific_create_values`

## `payment.transaction` (defines)

Payment Transaction

Inherits: `bus.listener.mixin`

- `provider_id` Many2one → `payment.provider` “Provider” (required, readonly, index)
- `provider_code` Selection “Provider Code” (related=provider_id.code)
- `capture_manually` Boolean (related=provider_id.capture_manually)
- `company_id` Many2one (store, index, related=provider_id.company_id)
- `payment_method_id` Many2one → `payment.method` “Payment Method” (required, readonly, index)
- `payment_method_code` Char “Payment Method Code” (related=payment_method_id.code)
- `primary_payment_method_id` Many2one → `payment.method` “Primary Payment Method” (compute=_compute_primary_payment_method_id)
- `reference` Char “Reference” (required, readonly)
- `provider_reference` Char “Provider Reference” (readonly)
- `amount` Monetary “Amount” (required, readonly)
- `currency_id` Many2one → `res.currency` “Currency” (required, readonly)
- `token_id` Many2one → `payment.token` “Payment Token” (readonly)
- `state` Selection “Status” (required, readonly, index)
- `state_message` Text “Message” (readonly)
- `last_state_change` Datetime “Last State Change Date” (readonly)
- `operation` Selection “Operation” (readonly, index)
- `is_live` Boolean “Production Environment”
- `payment_data_ids` One2many → `payment.data` “Pending Updates”
- `payment_data_count` Integer (compute=_compute_payment_data_count)
- `source_transaction_id` Many2one → `payment.transaction` “Source Transaction” (readonly)
- `child_transaction_ids` One2many → `payment.transaction` “Child Transactions” (readonly)
- `refunds_count` Integer “Refunds Count” (compute=_compute_refunds_count)
- `child_transaction_count` Integer (compute=_compute_child_transaction_count)
- `is_post_processed` Boolean “Is Post-processed”
- `tokenize` Boolean “Create Token”
- `landing_route` Char “Landing Route”
- `partner_id` Many2one → `res.partner` “Customer” (required, readonly)
- `partner_name` Char “Partner Name”
- `partner_lang` Selection “Language”
- `partner_email` Char “Email”
- `partner_address` Char “Address”
- `partner_zip` Char “Zip Code”
- `partner_city` Char “City”
- `partner_state_id` Many2one → `res.country.state` “State”
- `partner_country_id` Many2one → `res.country` “Country”
- `partner_phone` Char “Phone”

Public methods: `action_capture`, `action_confirm`, `action_post_process`, `action_refund`, `action_view_child_transactions`, `action_view_payment_data`, `action_view_refunds`, `action_void`, `create`, `write`

Extension points: `_check_state_authorized_supported`, `_check_token_is_active`, `_create_child_transaction`, `_get_last`, `_get_mandate_values`, `_get_processing_values`, `_get_received_message`, `_get_sent_message`, `_get_specific_create_values`, `_get_specific_processing_values`, `_get_specific_rendering_values`, `_get_status_message`, `_post_process`, `_post_process_with_lock`

## `portal.entry` (extends)


## `res.company` (extends)

- `onboarding_payment_module` Selection “Onboarding Payment Module” (compute=_compute_onboarding_payment_module)
- `pay_now_label` Char “Pay Now Label”
- `pay_later_label` Char “Pay Later Label”

Public methods: `create`

## `res.country` (extends)

- `is_mercado_pago_supported_country` Boolean (compute=_compute_provider_support)
- `is_stripe_supported_country` Boolean (compute=_compute_provider_support)

## `res.partner` (extends)

- `payment_token_ids` One2many → `payment.token` “Payment Tokens”
- `payment_token_count` Integer “Payment Token Count” (compute=_compute_payment_token_count)

Extension points: `_get_payment_tokens`

## `payment.capture.wizard` (defines)

Payment Capture Wizard

- `transaction_ids` Many2many → `payment.transaction` (readonly)
- `authorized_amount` Monetary “Authorized Amount” (compute=_compute_authorized_amount)
- `captured_amount` Monetary “Already Captured” (compute=_compute_captured_amount)
- `voided_amount` Monetary “Already Voided” (compute=_compute_voided_amount)
- `available_amount` Monetary “Maximum Capture Allowed” (compute=_compute_available_amount)
- `amount_to_capture` Monetary (store, compute=_compute_amount_to_capture)
- `is_amount_to_capture_valid` Boolean (compute=_compute_is_amount_to_capture_valid)
- `void_remaining_amount` Boolean
- `currency_id` Many2one (related=transaction_ids.currency_id)
- `support_partial_capture` Boolean (compute=_compute_support_partial_capture)
- `has_draft_children` Boolean (compute=_compute_has_draft_children)
- `has_remaining_amount` Boolean (compute=_compute_has_remaining_amount)

Public methods: `action_capture`

Extension points: `_check_amount_to_capture_within_boundaries`

## `payment.link.wizard` (defines)

Generate Payment Link

- `res_model` Char “Related Document Model” (required)
- `res_id` Integer “Related Document ID” (required)
- `amount` Monetary (required)
- `currency_id` Many2one → `res.currency`
- `partner_id` Many2one → `res.partner`
- `partner_email` Char (related=partner_id.email)
- `link` Char “Payment Link” (compute=_compute_link)
- `company_id` Many2one → `res.company` (compute=_compute_company_id)
- `warning_message` Char (compute=_compute_warning_message)

Public methods: `default_get`

Extension points: `_prepare_access_token`, `_prepare_anchor`, `_prepare_query_params`, `_prepare_url`

## `res.config.settings` (extends)

- `installed_provider_id` Many2one → `payment.provider` “Installed Provider” (compute=_compute_installed_provider_id)
- `onboarding_payment_module` Selection (related=company_id.onboarding_payment_module)

Public methods: `action_view_installed_provider`

Extension points: `_get_installed_providers_domain`

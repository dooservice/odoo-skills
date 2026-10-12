# payment — Payment Engine

Depends on: portal.

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`

## `payment.icon` (defines)

Payment Icon

- `name` Char “Name”
- `provider_ids` Many2many → `payment.provider` “Providers”
- `image` Image “Image”
- `image_payment_form` Image “Image displayed on the payment form” (store, related=image)
- `sequence` Integer “Sequence”

## `payment.provider` (defines)

Payment Provider

- `name` Char “Name” (required)
- `sequence` Integer “Sequence”
- `code` Selection “Code” (required)
- `state` Selection “State” (required)
- `is_published` Boolean “Published”
- `company_id` Many2one → `res.company` “Company” (required, index)
- `main_currency_id` Many2one (related=company_id.currency_id)
- `payment_icon_ids` Many2many → `payment.icon` “Supported Payment Icons”
- `allow_tokenization` Boolean “Allow Saving Payment Methods”
- `capture_manually` Boolean “Capture Amount Manually”
- `allow_express_checkout` Boolean “Allow Express Checkout”
- `redirect_form_view_id` Many2one → `ir.ui.view` “Redirect Form Template”
- `inline_form_view_id` Many2one → `ir.ui.view` “Inline Form Template”
- `token_inline_form_view_id` Many2one → `ir.ui.view` “Token Inline Form Template”
- `express_checkout_form_view_id` Many2one → `ir.ui.view` “Express Checkout Form Template”
- `available_country_ids` Many2many → `res.country` “Countries”
- `maximum_amount` Monetary “Maximum Amount”
- `fees_active` Boolean “Add Extra Fees”
- `fees_dom_fixed` Float “Fixed domestic fees”
- `fees_dom_var` Float “Variable domestic fees (in percents)”
- `fees_int_fixed` Float “Fixed international fees”
- `fees_int_var` Float “Variable international fees (in percents)”
- `display_as` Char “Displayed as”
- `pre_msg` Html “Help Message”
- `pending_msg` Html “Pending Message”
- `auth_msg` Html “Authorize Message”
- `done_msg` Html “Done Message”
- `cancel_msg` Html “Canceled Message”
- `support_tokenization` Boolean “Tokenization Supported” (compute=_compute_feature_support_fields)
- `support_manual_capture` Boolean “Manual Capture Supported” (compute=_compute_feature_support_fields)
- `support_express_checkout` Boolean “Express Checkout Supported” (compute=_compute_feature_support_fields)
- `support_refund` Selection “Type of Refund Supported” (compute=_compute_feature_support_fields)
- `support_fees` Boolean “Fees Supported” (compute=_compute_feature_support_fields)
- `image_128` Image “Image”
- `color` Integer “Color” (store, compute=_compute_color)
- `module_id` Many2one → `ir.module.module` “Corresponding Module”
- `module_state` Selection “Installation State” (store, related=module_id.state)
- `module_to_buy` Boolean “Odoo Enterprise Module” (related=module_id.to_buy)
- `show_credentials_page` Boolean (compute=_compute_view_configuration_fields)
- `show_allow_tokenization` Boolean (compute=_compute_view_configuration_fields)
- `show_allow_express_checkout` Boolean (compute=_compute_view_configuration_fields)
- `show_payment_icon_ids` Boolean (compute=_compute_view_configuration_fields)
- `show_pre_msg` Boolean (compute=_compute_view_configuration_fields)
- `show_pending_msg` Boolean (compute=_compute_view_configuration_fields)
- `show_auth_msg` Boolean (compute=_compute_view_configuration_fields)
- `show_done_msg` Boolean (compute=_compute_view_configuration_fields)
- `show_cancel_msg` Boolean (compute=_compute_view_configuration_fields)

Public methods: `action_toggle_is_published`, `button_immediate_install`, `create`, `write`

Extension points: `_check_fee_var_within_boundaries`, `_check_required_if_provider`, `_get_compatible_providers`, `_get_redirect_form_view`, `_get_removal_values`, `_get_validation_amount`, `_get_validation_currency`

## `payment.token` (defines)

Payment Token

- `provider_id` Many2one → `payment.provider` “Provider” (required)
- `provider_code` Selection (related=provider_id.code)
- `payment_details` Char “Payment Details”
- `partner_id` Many2one → `res.partner` “Partner” (required)
- `company_id` Many2one (store, index, related=provider_id.company_id)
- `provider_ref` Char “Provider Reference” (required)
- `transaction_ids` One2many → `payment.transaction` “Payment Transactions”
- `verified` Boolean “Verified”
- `active` Boolean “Active”

Public methods: `create`, `get_linked_records_info`, `name_get`, `write`

Extension points: `_get_specific_create_values`

## `payment.transaction` (defines)

Payment Transaction

- `provider_id` Many2one → `payment.provider` “Provider” (required, readonly)
- `provider_code` Selection (related=provider_id.code)
- `company_id` Many2one (store, index, related=provider_id.company_id)
- `reference` Char “Reference” (required, readonly)
- `provider_reference` Char “Provider Reference” (readonly)
- `amount` Monetary “Amount” (required, readonly)
- `currency_id` Many2one → `res.currency` “Currency” (required, readonly)
- `fees` Monetary “Fees” (readonly)
- `token_id` Many2one → `payment.token` “Payment Token” (readonly)
- `state` Selection “Status” (required, readonly, index)
- `state_message` Text “Message” (readonly)
- `last_state_change` Datetime “Last State Change Date” (readonly)
- `operation` Selection “Operation” (readonly, index)
- `source_transaction_id` Many2one → `payment.transaction` “Source Transaction” (readonly)
- `child_transaction_ids` One2many → `payment.transaction` “Child Transactions” (readonly)
- `refunds_count` Integer “Refunds Count” (compute=_compute_refunds_count)
- `is_post_processed` Boolean “Is Post-processed”
- `tokenize` Boolean “Create Token”
- `landing_route` Char “Landing Route”
- `callback_model_id` Many2one → `ir.model` “Callback Document Model”
- `callback_res_id` Integer “Callback Record ID”
- `callback_method` Char “Callback Method”
- `callback_hash` Char “Callback Hash”
- `callback_is_done` Boolean “Callback Done” (readonly)
- `partner_id` Many2one → `res.partner` “Customer” (required, readonly)
- `partner_name` Char “Partner Name”
- `partner_lang` Selection “Language”
- `partner_email` Char “Email”
- `partner_address` Char “Address”
- `partner_zip` Char “Zip”
- `partner_city` Char “City”
- `partner_state_id` Many2one → `res.country.state` “State”
- `partner_country_id` Many2one → `res.country` “Country”
- `partner_phone` Char “Phone”

Public methods: `action_capture`, `action_refund`, `action_view_refunds`, `action_void`, `create`

Extension points: `_check_state_authorized_supported`, `_check_token_is_active`, `_create_refund_transaction`, `_get_last`, `_get_post_processing_values`, `_get_processing_values`, `_get_received_message`, `_get_sent_message`, `_get_specific_create_values`, `_get_specific_processing_values`, `_get_specific_rendering_values`, `_get_tx_from_notification_data`

## `res.company` (extends)

- `payment_provider_onboarding_state` Selection “State of the onboarding payment provider step”
- `payment_onboarding_payment_method` Selection “Selected onboarding payment method”

Public methods: `get_account_invoice_onboarding_steps_states_names`

## `res.partner` (extends)

- `payment_token_ids` One2many → `payment.token` “Payment Tokens”
- `payment_token_count` Integer “Payment Token Count” (compute=_compute_payment_token_count)

## `payment.link.wizard` (defines)

Generate Payment Link

- `res_model` Char “Related Document Model” (required)
- `res_id` Integer “Related Document ID” (required)
- `amount` Monetary (required)
- `amount_max` Monetary
- `currency_id` Many2one → `res.currency`
- `partner_id` Many2one → `res.partner`
- `partner_email` Char (related=partner_id.email)
- `description` Char “Payment Ref”
- `link` Char “Payment Link” (compute=_compute_link)
- `company_id` Many2one → `res.company` (compute=_compute_company_id)
- `available_provider_ids` Many2many → `payment.provider` “Payment Providers Available” (compute=_compute_available_provider_ids)
- `has_multiple_providers` Boolean “Has Multiple Providers” (compute=_compute_has_multiple_providers)
- `payment_provider_selection` Selection “Allow Payment Provider” (required)

Public methods: `default_get`

Extension points: `_get_access_token`, `_get_additional_link_values`, `_get_payment_provider_available`

## `payment.provider.onboarding.wizard` (defines)

Payment provider onboarding wizard

- `payment_method` Selection “Payment Method”
- `paypal_user_type` Selection “Paypal User Type”
- `paypal_email_account` Char “Email”
- `paypal_seller_account` Char “Merchant Account ID”
- `paypal_pdt_token` Char “PDT Identity Token”
- `manual_name` Char “Method”
- `journal_name` Char “Bank Name”
- `acc_number` Char “Account Number”
- `manual_post_msg` Html “Payment Instructions”
- `_data_fetched` Boolean

Public methods: `add_payment_methods`

Extension points: `_get_default_payment_provider_onboarding_value`, `_get_manual_payment_provider`

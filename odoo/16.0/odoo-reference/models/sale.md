# sale — Sales

Depends on: sales_team, account_payment, utm.

## `account.move` (extends)

Inherits: `utm.mixin`

- `team_id` Many2one → `crm.team` “Sales Team” (store, compute=_compute_team_id)
- `campaign_id` Many2one
- `medium_id` Many2one
- `source_id` Many2one
- `sale_order_count` Integer “Sale Order Count” (compute=_compute_origin_so_count)

Public methods: `action_post`, `action_view_source_sale_orders`, `button_cancel`, `button_draft`, `unlink`

Extension points: `_action_invoice_ready_to_be_sent`

## `account.move.line` (extends)

- `is_downpayment` Boolean
- `sale_line_ids` Many2many → `sale.order.line` “Sales Order Lines” (readonly)

Extension points: `_get_downpayment_lines`, `_prepare_analytic_lines`

## `account.analytic.line` (extends)

- `so_line` Many2one → `sale.order.line` “Sales Order Item”

## `account.analytic.applicability` (extends)

Analytic Plan's Applicabilities

- `business_domain` Selection

## `crm.team` (extends)

- `use_quotations` Boolean “Quotations”
- `invoiced` Float “Invoiced This Month” (readonly, compute=_compute_invoiced)
- `invoiced_target` Float “Invoicing Target”
- `quotations_count` Integer “Number of quotations to invoice” (readonly, compute=_compute_quotations_to_invoice)
- `quotations_amount` Float “Amount of quotations to invoice” (readonly, compute=_compute_quotations_to_invoice)
- `sales_to_invoice_count` Integer “Number of sales to invoice” (readonly, compute=_compute_sales_to_invoice)
- `sale_order_count` Integer “# Sale Orders” (compute=_compute_sale_order_count)

Public methods: `action_primary_channel_button`, `update_invoiced_target`

## `payment.provider` (extends)

- `so_reference_type` Selection “Communication”

## `payment.transaction` (extends)

- `sale_order_ids` Many2many → `sale.order` “Sales Orders” (readonly)
- `sale_order_ids_nbr` Integer “# of Sales Orders” (compute=_compute_sale_order_ids_nbr)

Public methods: `action_view_sales_orders`

Extension points: `_check_amount_and_confirm_order`

## `product.product` (extends)

- `sales_count` Float “Sold” (compute=_compute_sales_count)

Public methods: `action_view_sales`

Extension points: `_get_combination_info_variant`, `_get_invoice_policy`

## `product.attribute.custom.value` (extends)

- `sale_order_line_id` Many2one → `sale.order.line` “Sales Order Line” (required)

## `product.packaging` (extends)

- `sales` Boolean “Sales”

## `product.template` (extends)

- `service_type` Selection “Track Service” (store, compute=_compute_service_type)
- `sale_line_warn` Selection (required)
- `sale_line_warn_msg` Text “Message for Sales Order Line”
- `expense_policy` Selection “Re-Invoice Expenses” (store, compute=_compute_expense_policy)
- `visible_expense_policy` Boolean “Re-Invoice Policy visible” (compute=_compute_visible_expense_policy)
- `sales_count` Float “Sold” (compute=_compute_sales_count)
- `visible_qty_configurator` Boolean “Quantity visible in configurator” (compute=_compute_visible_qty_configurator)
- `invoice_policy` Selection “Invoicing Policy” (store, compute=_compute_invoice_policy)

Public methods: `action_view_sales`, `create_product_variant`, `get_import_templates`

Extension points: `_check_sale_product_company`, `_get_combination_info`, `_get_current_company_fallback`

## `res.company` (extends)

- `portal_confirmation_sign` Boolean “Online Signature”
- `portal_confirmation_pay` Boolean “Online Payment”
- `quotation_validity_days` Integer “Default Quotation Validity (Days)”
- `sale_quotation_onboarding_state` Selection “State of the sale onboarding panel”
- `sale_onboarding_order_confirmation_state` Selection “State of the onboarding confirmation order step”
- `sale_onboarding_sample_quotation_state` Selection “State of the onboarding sample quotation step”
- `sale_onboarding_payment_method` Selection “Sale onboarding selected payment method”

Public methods: `action_close_sale_quotation_onboarding`, `action_open_sale_onboarding_payment_provider`, `action_open_sale_onboarding_sample_quotation`, `get_and_update_sale_quotation_onboarding_state`

Extension points: `_get_sample_sales_order`

## `res.config.settings` (extends)

- `default_invoice_policy` Selection
- `group_auto_done_setting` Boolean “Lock Confirmed Sales”
- `group_proforma_sales` Boolean “Pro-Forma Invoice”
- `group_warning_sale` Boolean “Sale Order Warnings”
- `automatic_invoice` Boolean “Automatic Invoice”
- `deposit_default_product_id` Many2one → `product.product`
- `invoice_mail_template_id` Many2one → `mail.template` “Invoice Email Template”
- `use_quotation_validity_days` Boolean “Default Quotation Validity”
- `quotation_validity_days` Integer “Default Quotation Validity (Days)” (related=company_id.quotation_validity_days)
- `portal_confirmation_sign` Boolean “Online Signature” (related=company_id.portal_confirmation_sign)
- `portal_confirmation_pay` Boolean “Online Payment” (related=company_id.portal_confirmation_pay)
- `module_delivery` Boolean “Delivery Methods”
- `module_delivery_bpost` Boolean “bpost Connector”
- `module_delivery_dhl` Boolean “DHL Express Connector”
- `module_delivery_easypost` Boolean “Easypost Connector”
- `module_delivery_sendcloud` Boolean “Sendcloud Connector”
- `module_delivery_fedex` Boolean “FedEx Connector”
- `module_delivery_ups` Boolean “UPS Connector”
- `module_delivery_usps` Boolean “USPS Connector”
- `module_product_email_template` Boolean “Specific Email”
- `module_sale_amazon` Boolean “Amazon Sync”
- `module_sale_loyalty` Boolean “Coupons & Loyalty”
- `module_sale_margin` Boolean “Margins”

Public methods: `set_values`

## `res.partner` (extends)

- `sale_order_count` Integer “Sale Order Count” (compute=_compute_sale_order_count)
- `sale_order_ids` One2many → `sale.order`
- `sale_warn` Selection
- `sale_warn_msg` Text “Message for Sales Order”

Public methods: `action_view_sale_order`, `can_edit_vat`

Extension points: `_get_sale_order_domain_count`

## `sale.order` (defines)

Sales Order

Inherits: `portal.mixin`, `mail.thread`, `mail.activity.mixin`, `utm.mixin`

- `name` Char “Order Reference” (required, readonly)
- `company_id` Many2one → `res.company` (required, index)
- `partner_id` Many2one → `res.partner` “Customer” (required, index)
- `state` Selection “Status” (readonly, index)
- `client_order_ref` Char “Customer Reference”
- `create_date` Datetime “Creation Date” (readonly, index)
- `commitment_date` Datetime “Delivery Date”
- `date_order` Datetime “Order Date” (required)
- `origin` Char “Source Document”
- `reference` Char “Payment Ref.”
- `require_signature` Boolean “Online Signature” (store, compute=_compute_require_signature)
- `require_payment` Boolean “Online Payment” (store, compute=_compute_require_payment)
- `signature` Image “Signature”
- `signed_by` Char “Signed By”
- `signed_on` Datetime “Signed On”
- `validity_date` Date “Expiration” (store, compute=_compute_validity_date)
- `note` Html “Terms and conditions” (store, compute=_compute_note)
- `partner_invoice_id` Many2one → `res.partner` “Invoice Address” (required, store, compute=_compute_partner_invoice_id)
- `partner_shipping_id` Many2one → `res.partner` “Delivery Address” (required, store, compute=_compute_partner_shipping_id)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position” (store, compute=_compute_fiscal_position_id)
- `payment_term_id` Many2one → `account.payment.term` “Payment Terms” (store, compute=_compute_payment_term_id)
- `pricelist_id` Many2one → `product.pricelist` “Pricelist” (required, store, compute=_compute_pricelist_id)
- `currency_id` Many2one (store, related=pricelist_id.currency_id)
- `currency_rate` Float “Currency Rate” (store, compute=_compute_currency_rate)
- `user_id` Many2one → `res.users` “Salesperson” (store, index, compute=_compute_user_id)
- `team_id` Many2one → `crm.team` “Sales Team” (store, compute=_compute_team_id)
- `order_line` One2many → `sale.order.line` “Order Lines”
- `amount_untaxed` Monetary “Untaxed Amount” (store, compute=_compute_amounts)
- `amount_tax` Monetary “Taxes” (store, compute=_compute_amounts)
- `amount_total` Monetary “Total” (store, compute=_compute_amounts)
- `invoice_count` Integer “Invoice Count” (compute=_get_invoiced)
- `invoice_ids` Many2many → `account.move` “Invoices” (compute=_get_invoiced)
- `invoice_status` Selection “Invoice Status” (store, compute=_compute_invoice_status)
- `transaction_ids` Many2many → `payment.transaction` “Transactions” (readonly)
- `authorized_transaction_ids` Many2many → `payment.transaction` “Authorized Transactions” (compute=_compute_authorized_transaction_ids)
- `campaign_id` Many2one
- `medium_id` Many2one
- `source_id` Many2one
- `analytic_account_id` Many2one → `account.analytic.account` “Analytic Account”
- `tag_ids` Many2many → `crm.tag` “Tags”
- `amount_undiscounted` Float “Amount Before Discount” (compute=_compute_amount_undiscounted)
- `country_code` Char “Country code” (related=company_id.account_fiscal_country_id.code)
- `expected_date` Datetime “Expected Date” (compute=_compute_expected_date)
- `is_expired` Boolean “Is Expired” (compute=_compute_is_expired)
- `partner_credit_warning` Text (compute=_compute_partner_credit_warning)
- `tax_country_id` Many2one → `res.country` (compute=_compute_tax_country_id)
- `tax_totals` Binary (compute=_compute_tax_totals)
- `terms_type` Selection (related=company_id.terms_type)
- `type_name` Char “Type Name” (compute=_compute_type_name)
- `show_update_fpos` Boolean “Has Fiscal Position Changed”
- `show_update_pricelist` Boolean “Has Pricelist Changed”

Public methods: `action_cancel`, `action_confirm`, `action_done`, `action_draft`, `action_preview_sale_order`, `action_quotation_send`, `action_quotation_sent`, `action_unlock`, `action_update_prices`, `action_update_taxes`, `action_view_invoice`, `add_option_to_order_with_taxcloud`, `copy_data`, `create`, `get_empty_list_help`, `get_portal_last_transaction`, `init`, `message_post`, `name_get`, `payment_action_capture`, `payment_action_void`, `validate_taxes_on_sales_order`

Extension points: `_action_cancel`, `_action_confirm`, `_check_order_line_company_id`, `_create_analytic_account`, `_create_invoices`, `_create_upsell_activity`, `_get_confirmation_template`, `_get_default_payment_link_values`, `_get_forbidden_state_confirm`, `_get_invoice_grouping_keys`, `_get_invoiceable_lines`, `_get_invoiced`, `_get_lang`, `_get_note_url`, `_get_order_lines_to_report`, `_get_portal_return_action`, `_get_report_base_filename`, `_get_update_prices_lines`, `_prepare_analytic_account_data`, `_prepare_confirmation_values`, `_prepare_down_payment_section_line`, `_prepare_invoice`

## `sale.order.line` (defines)

Sales Order Line

Inherits: `analytic.mixin`

- `order_id` Many2one → `sale.order` “Order Reference” (required, index)
- `sequence` Integer “Sequence”
- `company_id` Many2one (store, index, related=order_id.company_id)
- `currency_id` Many2one (store, related=order_id.currency_id)
- `order_partner_id` Many2one “Customer” (store, index, related=order_id.partner_id)
- `salesman_id` Many2one “Salesperson” (store, related=order_id.user_id)
- `state` Selection “Order Status” (store, related=order_id.state)
- `display_type` Selection
- `is_downpayment` Boolean “Is a down payment”
- `is_expense` Boolean “Is expense”
- `product_id` Many2one → `product.product` “Product”
- `product_template_id` Many2one → `product.template` “Product Template” (compute=_compute_product_template_id)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `product_custom_attribute_value_ids` One2many → `product.attribute.custom.value` “Custom Values” (store, compute=_compute_custom_attribute_values)
- `product_no_variant_attribute_value_ids` Many2many → `product.template.attribute.value` “Extra Values” (store, compute=_compute_no_variant_attribute_values)
- `name` Text “Description” (required, store, compute=_compute_name)
- `product_uom_qty` Float “Quantity” (required, store, compute=_compute_product_uom_qty)
- `product_uom` Many2one → `uom.uom` “Unit of Measure” (store, compute=_compute_product_uom)
- `tax_id` Many2many → `account.tax` “Taxes” (store, compute=_compute_tax_id)
- `pricelist_item_id` Many2one → `product.pricelist.item` (compute=_compute_pricelist_item_id)
- `price_unit` Float “Unit Price” (required, store, compute=_compute_price_unit)
- `discount` Float “Discount (%)” (store, compute=_compute_discount)
- `price_reduce` Float “Price Reduce” (store, compute=_compute_price_reduce)
- `price_subtotal` Monetary “Subtotal” (store, compute=_compute_amount)
- `price_tax` Float “Total Tax” (store, compute=_compute_amount)
- `price_total` Monetary “Total” (store, compute=_compute_amount)
- `price_reduce_taxexcl` Monetary “Price Reduce Tax excl” (store, compute=_compute_price_reduce_taxexcl)
- `price_reduce_taxinc` Monetary “Price Reduce Tax incl” (store, compute=_compute_price_reduce_taxinc)
- `product_packaging_id` Many2one → `product.packaging` “Packaging” (store, compute=_compute_product_packaging_id)
- `product_packaging_qty` Float “Packaging Quantity” (store, compute=_compute_product_packaging_qty)
- `customer_lead` Float “Lead Time” (required, store, compute=_compute_customer_lead)
- `qty_delivered_method` Selection “Method to update delivered qty” (store, compute=_compute_qty_delivered_method)
- `qty_delivered` Float “Delivery Quantity” (store, compute=_compute_qty_delivered)
- `qty_invoiced` Float “Invoiced Quantity” (store, compute=_compute_qty_invoiced)
- `qty_to_invoice` Float “Quantity To Invoice” (store, compute=_compute_qty_to_invoice)
- `analytic_line_ids` One2many → `account.analytic.line` “Analytic lines”
- `invoice_lines` Many2many → `account.move.line` “Invoice Lines”
- `invoice_status` Selection “Invoice Status” (store, compute=_compute_invoice_status)
- `untaxed_amount_invoiced` Monetary “Untaxed Invoiced Amount” (store, compute=_compute_untaxed_amount_invoiced)
- `untaxed_amount_to_invoice` Monetary “Untaxed Amount To Invoice” (store, compute=_compute_untaxed_amount_to_invoice)
- `product_type` Selection (related=product_id.detailed_type)
- `product_updatable` Boolean “Can Edit Product” (compute=_compute_product_updatable)
- `product_uom_readonly` Boolean (compute=_compute_product_uom_readonly)

Public methods: `compute_uom_qty`, `create`, `name_get`, `write`

Extension points: `_check_line_unlink`, `_get_custom_compute_tax_cache_key`, `_get_delivered_quantity_by_analytic`, `_get_display_price`, `_get_downpayment_line_price_unit`, `_get_downpayment_state`, `_get_invoice_line_sequence`, `_get_invoice_lines`, `_get_order_date`, `_get_pricelist_price`, `_get_pricelist_price_before_discount`, `_get_product_price_context`, `_get_protected_fields`, `_get_sale_order_line_multiline_description_sale`, `_get_sale_order_line_multiline_description_variants`, `_prepare_invoice_line`, `_prepare_procurement_values`

## `utm.campaign` (extends)

UTM Campaign

- `quotation_count` Integer “Quotation Count” (compute=_compute_quotation_count)
- `invoiced_amount` Integer “Revenues generated by the campaign” (compute=_compute_sale_invoiced_amount)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `currency_id` Many2one → `res.currency` “Currency” (related=company_id.currency_id)

Public methods: `action_redirect_to_invoiced`, `action_redirect_to_quotations`

## `product.product` (extends)


## `product.attribute` (extends)


## `product.attribute.value` (extends)


## `sale.order` (extends)


## `sale.order.line` (extends)


## `account.invoice.report` (extends)

- `team_id` Many2one → `crm.team` “Sales Team”

## `sale.report` (defines)

Sales Analysis Report

- `name` Char “Order Reference” (readonly)
- `date` Datetime “Order Date” (readonly)
- `product_id` Many2one → `product.product` (readonly)
- `product_uom` Many2one → `uom.uom` (readonly)
- `product_uom_qty` Float “Qty Ordered” (readonly)
- `qty_to_deliver` Float “Qty To Deliver” (readonly)
- `qty_delivered` Float “Qty Delivered” (readonly)
- `qty_to_invoice` Float “Qty To Invoice” (readonly)
- `qty_invoiced` Float “Qty Invoiced” (readonly)
- `partner_id` Many2one → `res.partner` (readonly)
- `company_id` Many2one → `res.company` (readonly)
- `user_id` Many2one → `res.users` (readonly)
- `price_total` Float “Total” (readonly)
- `price_subtotal` Float “Untaxed Total” (readonly)
- `untaxed_amount_to_invoice` Float “Untaxed Amount To Invoice” (readonly)
- `untaxed_amount_invoiced` Float “Untaxed Amount Invoiced” (readonly)
- `product_tmpl_id` Many2one → `product.template` (readonly)
- `categ_id` Many2one → `product.category` (readonly)
- `nbr` Integer “# of Lines” (readonly)
- `pricelist_id` Many2one → `product.pricelist` (readonly)
- `analytic_account_id` Many2one → `account.analytic.account` (readonly)
- `team_id` Many2one → `crm.team` (readonly)
- `country_id` Many2one → `res.country` (readonly)
- `industry_id` Many2one → `res.partner.industry` (readonly)
- `commercial_partner_id` Many2one → `res.partner` (readonly)
- `state` Selection “Status” (readonly)
- `weight` Float “Gross Weight” (readonly)
- `volume` Float “Volume” (readonly)
- `discount` Float “Discount %” (readonly)
- `discount_amount` Float “Discount Amount” (readonly)
- `campaign_id` Many2one → `utm.campaign` (readonly)
- `medium_id` Many2one → `utm.medium` (readonly)
- `source_id` Many2one → `utm.source` (readonly)
- `order_id` Many2one → `sale.order` (readonly)

Extension points: `_get_done_states`

## `account.payment.register` (extends)


Extension points: `_create_payment_vals_from_wizard`

## `mail.compose.message` (extends)


Extension points: `_action_send_mail`

## `payment.link.wizard` (extends)

Generate Sales Payment Link


Extension points: `_get_additional_link_values`, `_get_payment_provider_available`

## `sale.payment.provider.onboarding.wizard` (defines)

Sale Payment provider onboarding wizard

Inherits: `payment.provider.onboarding.wizard`

- `payment_method` Selection

Public methods: `add_payment_methods`

Extension points: `_get_default_payment_method`

## `sale.advance.payment.inv` (defines)

Sales Advance Payment Invoice

- `advance_payment_method` Selection “Create Invoice” (required)
- `count` Integer “Order Count” (compute=_compute_count)
- `sale_order_ids` Many2many → `sale.order`
- `has_down_payments` Boolean “Has down payments” (compute=_compute_has_down_payments)
- `deduct_down_payments` Boolean “Deduct down payments”
- `product_id` Many2one → `product.product` “Down Payment Product” (store, compute=_compute_product_id)
- `amount` Float “Down Payment Amount”
- `fixed_amount` Monetary “Down Payment Amount (Fixed)”
- `currency_id` Many2one → `res.currency` (store, compute=_compute_currency_id)
- `company_id` Many2one → `res.company` (store, compute=_compute_company_id)
- `deposit_account_id` Many2one → `account.account` “Income Account”
- `deposit_taxes_id` Many2many → `account.tax` “Customer Taxes”

Public methods: `create_invoices`

Extension points: `_check_amount_is_positive`, `_check_down_payment_product_is_valid`, `_create_invoices`, `_get_down_payment_amount`, `_get_down_payment_description`, `_prepare_down_payment_product_values`, `_prepare_down_payment_section_values`, `_prepare_invoice_values`, `_prepare_so_line_values`

## `sale.order.cancel` (defines)

Sales Order Cancel

Inherits: `mail.composer.mixin`

- `email_from` Char “From”
- `author_id` Many2one → `res.partner` “Author” (index)
- `recipient_ids` Many2many → `res.partner` “Recipients” (compute=_compute_recipient_ids)
- `order_id` Many2one → `sale.order` “Sale Order” (required)
- `display_invoice_alert` Boolean “Invoice Alert” (compute=_compute_display_invoice_alert)

Public methods: `action_cancel`, `action_send_mail_and_cancel`

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

Extension points: `_action_invoice_ready_to_be_sent`, `_get_partner_credit_warning_exclude_amount`, `_get_sale_order_invoiced_amount`

## `account.move.line` (extends)

- `is_downpayment` Boolean
- `sale_line_ids` Many2many → `sale.order.line` “Sales Order Lines” (readonly)

Extension points: `_get_discount_lines`, `_get_downpayment_lines`, `_prepare_analytic_lines`

## `account.analytic.line` (extends)

- `so_line` Many2one → `sale.order.line` “Sales Order Item”

## `account.analytic.applicability` (extends)

Analytic Plan's Applicabilities

- `business_domain` Selection

## `account.chart.template` (extends)


Extension points: `_get_property_accounts`

## `crm.team` (extends)

- `invoiced` Float “Invoiced This Month” (readonly, compute=_compute_invoiced)
- `invoiced_target` Float “Invoicing Target”
- `quotations_count` Integer “Number of quotations to invoice” (readonly, compute=_compute_quotations_to_invoice)
- `quotations_amount` Float “Amount of quotations to invoice” (readonly, compute=_compute_quotations_to_invoice)
- `sales_to_invoice_count` Integer “Number of sales to invoice” (readonly, compute=_compute_sales_to_invoice)
- `sale_order_count` Integer “# Sale Orders” (compute=_compute_sale_order_count)

Public methods: `action_primary_channel_button`, `update_invoiced_target`

## `ir.config_parameter` (extends)


Public methods: `create`, `unlink`, `write`

## `mail.scheduled.message` (extends)


Extension points: `_post_message`

## `payment.provider` (extends)

- `so_reference_type` Selection “Communication”

## `payment.transaction` (extends)

- `sale_order_ids` Many2many → `sale.order` “Sales Orders” (readonly)
- `sale_order_ids_nbr` Integer “# of Sales Orders” (compute=_compute_sale_order_ids_nbr)

Public methods: `action_view_sales_orders`

Extension points: `_check_amount_and_confirm_order`, `_post_process`

## `product.category` (extends)

- `property_account_downpayment_categ_id` Many2one → `account.account` “Downpayment Account” (company_dependent)

## `product.document` (extends)

- `attached_on_sale` Selection “Sale : Visible at” (required)

## `product.product` (extends)

- `sales_count` Float “Sold” (compute=_compute_sales_count)
- `product_catalog_product_is_in_sale_order` Boolean (compute=_compute_product_is_in_sale_order)

Public methods: `action_view_sales`

Extension points: `_get_backend_root_menu_ids`, `_get_invoice_policy`

## `product.attribute.custom.value` (extends)

- `sale_order_line_id` Many2one → `sale.order.line` “Sales Order Line”

## `product.packaging` (extends)

- `sales` Boolean “Sales”

## `product.template` (extends)

- `service_type` Selection “Track Service” (store, compute=_compute_service_type)
- `sale_line_warn` Selection “Sales Order Line” (required)
- `sale_line_warn_msg` Text “Message for Sales Order Line”
- `expense_policy` Selection “Re-Invoice Costs” (store, compute=_compute_expense_policy)
- `visible_expense_policy` Boolean “Re-Invoice Policy visible” (compute=_compute_visible_expense_policy)
- `sales_count` Float “Sold” (compute=_compute_sales_count)
- `invoice_policy` Selection “Invoicing Policy” (store, compute=_compute_invoice_policy)
- `optional_product_ids` Many2many → `product.template` “Optional Products”

Public methods: `action_view_sales`, `get_import_templates`, `get_single_product_variant`

Extension points: `_check_incompatible_types`, `_check_sale_product_company`, `_get_additional_configurator_data`, `_get_backend_root_menu_ids`, `_get_configurator_display_price`, `_get_configurator_price`, `_get_incompatible_types`, `_get_product_accounts`, `_get_saleable_tracking_types`, `_prepare_invoicing_tooltip`, `_prepare_service_tracking_tooltip`, `_prepare_tooltip`

## `res.company` (extends)

- `portal_confirmation_sign` Boolean “Online Signature”
- `portal_confirmation_pay` Boolean “Online Payment”
- `prepayment_percent` Float “Prepayment percentage”
- `quotation_validity_days` Integer “Default Quotation Validity”
- `sale_discount_product_id` Many2one → `product.product` “Discount Product”
- `sale_onboarding_payment_method` Selection “Sale onboarding selected payment method”

Extension points: `_check_prepayment_percent`

## `res.partner` (extends)

- `sale_order_count` Integer “Sale Order Count” (compute=_compute_sale_order_count)
- `sale_order_ids` One2many → `sale.order`
- `sale_warn` Selection
- `sale_warn_msg` Text “Message for Sales Order”

Public methods: `action_view_sale_order`, `can_edit_vat`

Extension points: `_get_sale_order_domain_count`

## `sale.order` (defines)

Sales Order

Inherits: `portal.mixin`, `product.catalog.mixin`, `mail.thread`, `mail.activity.mixin`, `utm.mixin`

- `name` Char “Order Reference” (required)
- `company_id` Many2one → `res.company` (required, index)
- `partner_id` Many2one → `res.partner` “Customer” (required, index)
- `state` Selection “Status” (readonly, index)
- `locked` Boolean
- `has_archived_products` Boolean (compute=_compute_has_archived_products)
- `client_order_ref` Char “Customer Reference”
- `create_date` Datetime “Creation Date” (readonly, index)
- `commitment_date` Datetime “Delivery Date”
- `date_order` Datetime “Order Date” (required)
- `origin` Char “Source Document”
- `reference` Char “Payment Ref.”
- `require_signature` Boolean “Online signature” (store, compute=_compute_require_signature)
- `require_payment` Boolean “Online payment” (store, compute=_compute_require_payment)
- `prepayment_percent` Float “Prepayment percentage” (store, compute=_compute_prepayment_percent)
- `signature` Image “Signature”
- `signed_by` Char “Signed By”
- `signed_on` Datetime “Signed On”
- `validity_date` Date “Expiration” (store, compute=_compute_validity_date)
- `journal_id` Many2one → `account.journal` “Invoicing Journal” (store, compute=_compute_journal_id)
- `note` Html “Terms and conditions” (store, compute=_compute_note)
- `partner_invoice_id` Many2one → `res.partner` “Invoice Address” (required, store, compute=_compute_partner_invoice_id)
- `partner_shipping_id` Many2one → `res.partner` “Delivery Address” (required, store, compute=_compute_partner_shipping_id)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position” (store, compute=_compute_fiscal_position_id)
- `payment_term_id` Many2one → `account.payment.term` “Payment Terms” (store, compute=_compute_payment_term_id)
- `pricelist_id` Many2one → `product.pricelist` “Pricelist” (store, compute=_compute_pricelist_id)
- `currency_id` Many2one → `res.currency` (store, compute=_compute_currency_id)
- `currency_rate` Float “Currency Rate” (store, compute=_compute_currency_rate)
- `user_id` Many2one → `res.users` “Salesperson” (store, index, compute=_compute_user_id)
- `team_id` Many2one → `crm.team` “Sales Team” (store, index, compute=_compute_team_id)
- `order_line` One2many → `sale.order.line` “Order Lines”
- `amount_untaxed` Monetary “Untaxed Amount” (store, compute=_compute_amounts)
- `amount_tax` Monetary “Taxes” (store, compute=_compute_amounts)
- `amount_total` Monetary “Total” (store, compute=_compute_amounts)
- `amount_to_invoice` Monetary “Un-invoiced Balance” (compute=_compute_amount_to_invoice)
- `amount_invoiced` Monetary “Already invoiced” (compute=_compute_amount_invoiced)
- `invoice_count` Integer “Invoice Count” (compute=_get_invoiced)
- `invoice_ids` Many2many → `account.move` “Invoices” (compute=_get_invoiced)
- `invoice_status` Selection “Invoice Status” (store, compute=_compute_invoice_status)
- `transaction_ids` Many2many → `payment.transaction` “Transactions” (readonly)
- `authorized_transaction_ids` Many2many → `payment.transaction` “Authorized Transactions” (compute=_compute_authorized_transaction_ids)
- `amount_paid` Float “Payment Transactions Amount” (compute=_compute_amount_paid)
- `campaign_id` Many2one
- `medium_id` Many2one
- `source_id` Many2one
- `tag_ids` Many2many → `crm.tag` “Tags”
- `amount_undiscounted` Float “Amount Before Discount” (compute=_compute_amount_undiscounted)
- `country_code` Char “Country code” (related=company_id.account_fiscal_country_id.code)
- `company_price_include` Selection (related=company_id.account_price_include)
- `duplicated_order_ids` Many2many → `sale.order` (compute=_compute_duplicated_order_ids)
- `expected_date` Datetime “Expected Date” (compute=_compute_expected_date)
- `is_expired` Boolean “Is Expired” (compute=_compute_is_expired)
- `partner_credit_warning` Text (compute=_compute_partner_credit_warning)
- `tax_calculation_rounding_method` Selection (related=company_id.tax_calculation_rounding_method)
- `tax_country_id` Many2one → `res.country` (compute=_compute_tax_country_id)
- `tax_totals` Binary (compute=_compute_tax_totals)
- `terms_type` Selection (related=company_id.terms_type)
- `type_name` Char “Type Name” (compute=_compute_type_name)
- `show_update_fpos` Boolean “Has Fiscal Position Changed”
- `has_active_pricelist` Boolean (compute=_compute_has_active_pricelist)
- `show_update_pricelist` Boolean “Has Pricelist Changed”

Public methods: `action_cancel`, `action_confirm`, `action_draft`, `action_lock`, `action_open_business_doc`, `action_open_discount_wizard`, `action_preview_sale_order`, `action_quotation_send`, `action_quotation_sent`, `action_unlock`, `action_update_prices`, `action_update_taxes`, `action_view_invoice`, `copy_data`, `create`, `create_document_from_attachment`, `get_empty_list_help`, `get_portal_last_transaction`, `init`, `message_post`, `onchange`, `payment_action_capture`, `payment_action_void`, `write`

Extension points: `_action_cancel`, `_action_confirm`, `_check_order_line_company_id`, `_check_prepayment_percent`, `_create_account_invoices`, `_create_invoices`, `_create_order_from_attachment`, `_create_upsell_activity`, `_get_action_add_from_catalog_extra_context`, `_get_confirmation_template`, `_get_copiable_order_lines`, `_get_default_payment_link_values`, `_get_invoice_grouping_keys`, `_get_invoiceable_lines`, `_get_invoiced`, `_get_lang`, `_get_model_description`, `_get_name_portal_content_view`, `_get_name_tax_totals_view`, `_get_note_url`, `_get_order_edi_decoder`, `_get_order_lines_to_report`, `_get_portal_return_action`, `_get_prepayment_required_amount`, `_get_priced_lines`, `_get_product_catalog_domain`, `_get_product_catalog_order_data`, `_get_product_catalog_record_lines`, `_get_product_documents`, `_get_report_base_filename`, `_get_update_prices_lines`, `_prepare_analytic_account_data`, `_prepare_confirmation_values`, `_prepare_down_payment_section_line`, `_prepare_invoice`

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
- `tax_country_id` Many2one (related=order_id.tax_country_id)
- `display_type` Selection
- `is_configurable_product` Boolean “Is the product configurable?” (related=product_template_id.has_configurable_attributes)
- `is_downpayment` Boolean “Is a down payment”
- `is_expense` Boolean “Is expense”
- `product_id` Many2one → `product.product` “Product”
- `product_template_id` Many2one → `product.template` “Product Template” (compute=_compute_product_template_id)
- `product_uom_category_id` Many2one (related=product_id.uom_id.category_id)
- `product_template_attribute_value_ids` Many2many (related=product_id.product_template_attribute_value_ids)
- `product_custom_attribute_value_ids` One2many → `product.attribute.custom.value` “Custom Values” (store, compute=_compute_custom_attribute_values)
- `product_no_variant_attribute_value_ids` Many2many → `product.template.attribute.value` “Extra Values” (store, compute=_compute_no_variant_attribute_values)
- `is_product_archived` Boolean (compute=_compute_is_product_archived)
- `name` Text “Description” (required, store, compute=_compute_name)
- `translated_product_name` Text (compute=_compute_translated_product_name)
- `product_uom_qty` Float “Quantity” (required, store, compute=_compute_product_uom_qty)
- `product_uom` Many2one → `uom.uom` “Unit of Measure” (store, compute=_compute_product_uom)
- `linked_line_id` Many2one → `sale.order.line` “Linked Order Line” (index)
- `linked_line_ids` One2many → `sale.order.line` “Linked Order Lines”
- `virtual_id` Char
- `linked_virtual_id` Char
- `selected_combo_items` Char
- `combo_item_id` Many2one → `product.combo.item`
- `tax_id` Many2many → `account.tax` “Taxes” (store, compute=_compute_tax_id)
- `pricelist_item_id` Many2one → `product.pricelist.item` (compute=_compute_pricelist_item_id)
- `price_unit` Float “Unit Price” (required, store, compute=_compute_price_unit)
- `technical_price_unit` Float
- `discount` Float “Discount (%)” (store, compute=_compute_discount)
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
- `qty_invoiced_posted` Float “Invoiced Quantity (posted)” (compute=_compute_qty_invoiced_posted)
- `qty_to_invoice` Float “Quantity To Invoice” (store, compute=_compute_qty_to_invoice)
- `analytic_line_ids` One2many → `account.analytic.line` “Analytic lines”
- `invoice_lines` Many2many → `account.move.line` “Invoice Lines”
- `invoice_status` Selection “Invoice Status” (store, compute=_compute_invoice_status)
- `untaxed_amount_invoiced` Monetary “Untaxed Invoiced Amount” (store, compute=_compute_untaxed_amount_invoiced)
- `amount_invoiced` Monetary “Invoiced Amount” (compute=_compute_amount_invoiced)
- `untaxed_amount_to_invoice` Monetary “Untaxed Amount To Invoice” (store, compute=_compute_untaxed_amount_to_invoice)
- `amount_to_invoice` Monetary “Un-invoiced Balance” (compute=_compute_amount_to_invoice)
- `product_type` Selection (related=product_id.type)
- `service_tracking` Selection (related=product_id.service_tracking)
- `product_updatable` Boolean “Can Edit Product” (compute=_compute_product_updatable)
- `product_uom_readonly` Boolean (compute=_compute_product_uom_readonly)
- `tax_calculation_rounding_method` Selection “Tax calculation rounding method” (readonly, related=company_id.tax_calculation_rounding_method)
- `company_price_include` Selection (related=company_id.account_price_include)

Public methods: `action_add_from_catalog`, `compute_uom_qty`, `create`, `has_valued_move_ids`, `write`

Extension points: `_check_combo_item_id`, `_check_line_unlink`, `_get_combo_item_display_price`, `_get_custom_compute_tax_cache_key`, `_get_delivered_quantity_by_analytic`, `_get_discounted_price`, `_get_display_price`, `_get_display_price_ignore_combo`, `_get_downpayment_description`, `_get_downpayment_line_price_unit`, `_get_downpayment_state`, `_get_invoice_line_sequence`, `_get_invoice_lines`, `_get_lines_with_price`, `_get_linked_line`, `_get_linked_lines`, `_get_order_date`, `_get_partner_display`, `_get_pricelist_price`, `_get_pricelist_price_before_discount`, `_get_pricelist_price_context`, `_get_product_catalog_lines_data`, `_get_product_price_context`, `_get_protected_fields`, `_get_sale_order_line_multiline_description_sale`, `_get_sale_order_line_multiline_description_variants`, `_prepare_base_line_for_taxes_computation`, `_prepare_invoice_line`, `_prepare_procurement_values`

## `utm.campaign` (extends)

UTM Campaign

- `quotation_count` Integer “Quotation Count” (compute=_compute_quotation_count)
- `invoiced_amount` Integer “Revenues generated by the campaign” (compute=_compute_sale_invoiced_amount)
- `company_id` Many2one → `res.company` “Company”
- `currency_id` Many2one → `res.currency` “Currency” (related=company_id.currency_id)

Public methods: `action_redirect_to_invoiced`, `action_redirect_to_quotations`

## `account.invoice.report` (extends)

- `team_id` Many2one → `crm.team` “Sales Team”

## `sale.report` (defines)

Sales Analysis Report

- `name` Char “Order Reference” (readonly)
- `date` Datetime “Order Date” (readonly)
- `partner_id` Many2one → `res.partner` “Customer” (readonly)
- `company_id` Many2one → `res.company` (readonly)
- `pricelist_id` Many2one → `product.pricelist` (readonly)
- `team_id` Many2one → `crm.team` “Sales Team” (readonly)
- `user_id` Many2one → `res.users` “Salesperson” (readonly)
- `state` Selection “Status” (readonly)
- `invoice_status` Selection “Order Invoice Status” (readonly)
- `campaign_id` Many2one → `utm.campaign` “Campaign” (readonly)
- `medium_id` Many2one → `utm.medium` “Medium” (readonly)
- `source_id` Many2one → `utm.source` “Source” (readonly)
- `commercial_partner_id` Many2one → `res.partner` “Customer Entity” (readonly)
- `country_id` Many2one → `res.country` “Customer Country” (readonly)
- `industry_id` Many2one → `res.partner.industry` “Customer Industry” (readonly)
- `partner_zip` Char “Customer ZIP” (readonly)
- `state_id` Many2one → `res.country.state` “Customer State” (readonly)
- `order_reference` Reference “Order”
- `categ_id` Many2one → `product.category` “Product Category” (readonly)
- `product_id` Many2one → `product.product` “Product Variant” (readonly)
- `product_tmpl_id` Many2one → `product.template` “Product” (readonly)
- `product_uom` Many2one → `uom.uom` “Unit of Measure” (readonly)
- `product_uom_qty` Float “Qty Ordered” (readonly)
- `qty_to_deliver` Float “Qty To Deliver” (readonly)
- `qty_delivered` Float “Qty Delivered” (readonly)
- `qty_to_invoice` Float “Qty To Invoice” (readonly)
- `qty_invoiced` Float “Qty Invoiced” (readonly)
- `price_subtotal` Monetary “Untaxed Total” (readonly)
- `price_total` Monetary “Total” (readonly)
- `untaxed_amount_to_invoice` Monetary “Untaxed Amount To Invoice” (readonly)
- `untaxed_amount_invoiced` Monetary “Untaxed Amount Invoiced” (readonly)
- `line_invoice_status` Selection “Invoice Status” (readonly)
- `weight` Float “Gross Weight” (readonly)
- `volume` Float “Volume” (readonly)
- `price_unit` Float “Unit Price” (readonly)
- `discount` Float “Discount %” (readonly)
- `discount_amount` Monetary “Discount Amount” (readonly)
- `nbr` Integer “# of Lines” (readonly)
- `currency_id` Many2one → `res.currency` (compute=_compute_currency_id)

Public methods: `action_open_order`

Extension points: `_get_done_states`, `_get_order_reference`

## `base.document.layout` (extends)


Extension points: `_get_preview_template`, `_get_render_information`

## `mail.compose.message` (extends)


Public methods: `action_schedule_message`

Extension points: `_prepare_mail_values_rendered`

## `sale.mass.cancel.orders` (defines)

Cancel multiple quotations

- `sale_order_ids` Many2many → `sale.order` “Sale orders to cancel”
- `sale_orders_count` Integer (compute=_compute_sale_orders_count)
- `has_confirmed_order` Boolean (compute=_compute_has_confirmed_order)

Public methods: `action_mass_cancel`

## `payment.link.wizard` (extends)

Generate Sales Payment Link

- `amount_paid` Monetary “Already Paid” (readonly)
- `confirmation_message` Char (compute=_compute_confirmation_message)

Extension points: `_prepare_query_params`

## `sale.payment.provider.onboarding.wizard` (defines)

Sale Payment provider onboarding wizard

Inherits: `payment.provider.onboarding.wizard`

- `payment_method` Selection

Public methods: `add_payment_methods`

Extension points: `_get_default_payment_method`

## `res.config.settings` (extends)

- `default_invoice_policy` Selection “Invoicing Policy”
- `group_auto_done_setting` Boolean “Lock Confirmed Sales”
- `group_discount_per_so_line` Boolean “Discounts”
- `group_proforma_sales` Boolean “Pro-Forma Invoice”
- `group_warning_sale` Boolean “Sale Order Warnings”
- `automatic_invoice` Boolean “Automatic Invoice”
- `invoice_mail_template_id` Many2one → `mail.template` “Invoice Email Template”
- `quotation_validity_days` Integer (related=company_id.quotation_validity_days)
- `portal_confirmation_sign` Boolean (related=company_id.portal_confirmation_sign)
- `portal_confirmation_pay` Boolean (related=company_id.portal_confirmation_pay)
- `prepayment_percent` Float (related=company_id.prepayment_percent)
- `module_delivery` Boolean “Delivery Methods”
- `module_delivery_bpost` Boolean “bpost Connector”
- `module_delivery_dhl` Boolean “DHL Express Connector”
- `module_delivery_easypost` Boolean “Easypost Connector”
- `module_delivery_fedex` Boolean “FedEx Connector”
- `module_delivery_sendcloud` Boolean “Sendcloud Connector”
- `module_delivery_shiprocket` Boolean “Shiprocket Connector”
- `module_delivery_ups` Boolean “UPS Connector”
- `module_delivery_usps` Boolean “USPS Connector”
- `module_delivery_starshipit` Boolean “Starshipit Connector”
- `module_product_email_template` Boolean “Specific Email”
- `module_sale_amazon` Boolean “Amazon Sync”
- `module_sale_loyalty` Boolean “Coupons & Loyalty”
- `module_sale_margin` Boolean “Margins”
- `module_sale_product_matrix` Boolean “Sales Grid Entry”
- `module_sale_pdf_quote_builder` Boolean “PDF Quote builder”
- `module_sale_commission` Boolean “Commissions”

Public methods: `set_values`

## `sale.advance.payment.inv` (defines)

Sales Advance Payment Invoice

- `advance_payment_method` Selection “Create Invoice” (required)
- `count` Integer “Order Count” (compute=_compute_count)
- `sale_order_ids` Many2many → `sale.order`
- `has_down_payments` Boolean “Has down payments” (compute=_compute_has_down_payments)
- `deduct_down_payments` Boolean “Deduct down payments”
- `amount` Float “Down Payment”
- `fixed_amount` Monetary “Down Payment Amount (Fixed)”
- `currency_id` Many2one → `res.currency` (store, compute=_compute_currency_id)
- `company_id` Many2one → `res.company` (store, compute=_compute_company_id)
- `amount_invoiced` Monetary “Already invoiced” (compute=_compute_invoice_amounts)
- `amount_to_invoice` Monetary “Amount to invoice” (compute=_compute_invoice_amounts)
- `display_draft_invoice_warning` Boolean (compute=_compute_display_draft_invoice_warning)
- `display_invoice_amount_warning` Boolean (compute=_compute_display_invoice_amount_warning)
- `consolidated_billing` Boolean “Consolidated Billing”

Public methods: `create_invoices`, `view_draft_invoices`

Extension points: `_check_amount_is_positive`, `_create_invoices`, `_get_down_payment_description`, `_prepare_base_downpayment_line_values`, `_prepare_down_payment_lines_values`, `_prepare_down_payment_section_values`, `_prepare_invoice_values`

## `sale.order.cancel` (defines)

Sales Order Cancel

Inherits: `mail.composer.mixin`

- `author_id` Many2one → `res.partner` “Author” (index)
- `recipient_ids` Many2many → `res.partner` “Recipients” (compute=_compute_recipient_ids)
- `order_id` Many2one → `sale.order` “Sale Order” (required)
- `display_invoice_alert` Boolean “Invoice Alert” (compute=_compute_display_invoice_alert)

Public methods: `action_cancel`, `action_send_mail_and_cancel`

## `sale.order.discount` (defines)

Discount Wizard

- `sale_order_id` Many2one → `sale.order` (required)
- `company_id` Many2one (related=sale_order_id.company_id)
- `currency_id` Many2one (related=sale_order_id.currency_id)
- `discount_amount` Monetary “Amount”
- `discount_percentage` Float “Percentage”
- `discount_type` Selection
- `tax_ids` Many2many → `account.tax` “Taxes”

Public methods: `action_apply_discount`

Extension points: `_check_discount_amount`, `_create_discount_lines`, `_get_discount_product`, `_prepare_discount_line_values`, `_prepare_discount_product_values`

# sale — Sales

Depends on: sales_team, account_payment, utm.

## `account.analytic.applicability` (extends)

Analytic Plan's Applicabilities

- `business_domain` Selection

## `account.analytic.line` (extends)

- `reinvoice_move_id` Many2one → `account.move` “Invoice” (readonly)
- `so_line` Many2one → `sale.order.line` “Sales Order Item” (store, compute=_compute_so_line)
- `order_id` Many2one → `sale.order` “Customer Order” (store, index, compute=_compute_order_id)

Public methods: `create`, `write`

Extension points: `_check_can_write`, `_create_so_line`, `_get_existing_so_line`, `_get_invoiced_line_delete_error`, `_get_invoiced_line_write_error`

## `account.move` (extends)

Inherits: `utm.mixin`

- `team_id` Many2one → `crm.team` “Sales Team” (store, compute=_compute_team_id)
- `campaign_id` Many2one
- `medium_id` Many2one
- `source_id` Many2one
- `sale_order_count` Integer “Sale Order Count” (compute=_compute_origin_so_count)
- `sale_warning_text` Text “Sale Warning” (compute=_compute_sale_warning_text)
- `service_line_count` Integer (compute=_compute_service_line_count)

Public methods: `action_post`, `action_view_services_analytic_lines`, `action_view_source_sale_orders`, `button_cancel`, `button_draft`, `unlink`

Extension points: `_action_invoice_ready_to_be_sent`, `_get_partner_credit_warning_exclude_amount`, `_get_reinvoiced_analytic_lines_to_link`, `_get_sale_order_invoiced_amount`

## `account.move.line` (extends)

- `is_downpayment` Boolean
- `sale_line_ids` Many2many → `sale.order.line` “Sales Order Lines” (readonly)
- `sale_line_warn_msg` Text (compute=_compute_sale_line_warn_msg)

Extension points: `_get_discount_lines`, `_get_downpayment_lines`, `_prepare_analytic_lines`

## `crm.team` (extends)

- `sale_order_count` Integer “# Sale Orders” (compute=_compute_sale_order_count)

Public methods: `action_primary_channel_button`

## `ir.actions.report` (extends)


## `ir.config_parameter` (extends)


Public methods: `create`, `unlink`, `write`

Extension points: `_get_param_cron_mapping`

## `payment.provider` (extends)

- `so_reference_type` Selection “Communication”

## `payment.transaction` (extends)

- `sale_order_ids` Many2many → `sale.order` “Sales Orders” (readonly)
- `sale_order_ids_nbr` Integer “# of Sales Orders” (compute=_compute_sale_order_ids_nbr)

Public methods: `action_view_sales_orders`

Extension points: `_check_amount_and_confirm_order`, `_post_process`

## `product.category` (extends)

- `property_account_invoices_to_issue_id` Many2one → `account.account` (company_dependent)
- `property_account_invoices_to_issue_active` Boolean “Invoices to be Issued Account Active” (related=property_account_invoices_to_issue_id.active)
- `property_account_invoiced_not_delivered_id` Many2one → `account.account` (company_dependent)
- `property_account_invoiced_not_delivered_active` Boolean “Invoiced Not Delivered Account Active” (related=property_account_invoiced_not_delivered_id.active)

## `product.document` (extends)

- `attached_on_sale` Selection “Accessible” (required)

## `product.pricelist.item` (extends)


## `product.product` (extends)

- `sales_count` Float “Sold” (compute=_compute_sales_count)
- `previously_bought_by_customer` Boolean

Public methods: `action_view_sales`

Extension points: `_get_backend_root_menu_ids`, `_get_invoice_policy`

## `product.attribute.custom.value` (extends)

- `sale_order_line_id` Many2one → `sale.order.line` “Sales Order Line”

## `product.template` (extends)

- `service_type` Selection “Track Service” (store, compute=_compute_service_type)
- `sale_line_warn_msg` Text “Sales Order Line Warning”
- `reinvoice_policy` Selection “Re-Invoice Costs” (store, compute=_compute_reinvoice_policy)
- `visible_reinvoice_policy` Boolean “Re-Invoice Policy visible” (compute=_compute_visible_reinvoice_policy)
- `sales_count` Float “Sold” (compute=_compute_sales_count)
- `invoice_policy` Selection “Invoicing Policy” (required, store, compute=_compute_invoice_policy)
- `optional_product_ids` Many2many → `product.template` “Optional Products”
- `sale_delay` Integer “Delivery Time” (company_dependent)

Public methods: `action_view_sales`, `get_import_templates`, `get_single_product_variant`

Extension points: `_check_incompatible_types`, `_check_sale_product_company`, `_get_additional_configurator_data`, `_get_backend_root_menu_ids`, `_get_configurator_display_price`, `_get_configurator_price`, `_get_incompatible_types`, `_get_product_accounts`, `_get_saleable_tracking_types`, `_prepare_invoicing_tooltip`, `_prepare_service_tracking_tooltip`, `_prepare_tooltip`

## `res.company` (extends)

- `account_invoices_to_issue_id` Many2one → `account.account` “Invoices to be Issued Account”
- `account_invoiced_not_delivered_id` Many2one → `account.account` “Invoiced Not Delivered Account”
- `portal_confirmation_sign` Boolean “Online Signature”
- `portal_confirmation_pay` Boolean “Online Payment”
- `prepayment_percent` Float “Prepayment”
- `display_product_images_on_so` Boolean “Display Product Images”
- `quotation_validity_days` Integer “Default Quotation Validity”
- `sale_discount_product_id` Many2one → `product.product` “Discount Product”
- `sale_onboarding_payment_method` Selection “Sale onboarding selected payment method”
- `downpayment_account_id` Many2one → `account.account` “Downpayment Account”
- `show_sol_numbers` Boolean “Line Numbers”
- `sale_invoice_policy` Selection “Invoicing Policy” (required)
- `sale_automatic_invoice` Boolean “Automatic Invoicing”

Public methods: `create`, `write`

Extension points: `_check_prepayment_percent`, `_get_accrual_candidate_lines`

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `res.partner` (extends)

- `sale_order_count` Integer “Sale Order Count” (compute=_compute_sale_order_count)
- `sale_order_ids` One2many → `sale.order`
- `sale_warn_msg` Text “Message for Sales Order”
- `incoterm_id` Many2one → `account.incoterms` “Incoterm”
- `incoterm_location` Char “Incoterm Location”

Extension points: `_get_sale_order_domain_count`

## `sale.order` (defines)

Sales Order

Inherits: `account.document.import.mixin`, `mail.activity.mixin`, `mail.thread.subject.suggested`, `portal.mixin`, `product.catalog.mixin`, `utm.mixin`

- `name` Char “Order Reference” (required)
- `company_id` Many2one → `res.company` (required, index)
- `partner_id` Many2one → `res.partner` “Customer” (required, index)
- `state` Selection “Status” (readonly, index)
- `locked` Boolean
- `invoicing_closed` Boolean “Manually Closed For Invoicing”
- `has_archived_products` Boolean (compute=_compute_has_archived_products)
- `client_order_ref` Char “Customer Reference”
- `create_date` Datetime “Creation Date” (readonly, index)
- `commitment_date` Datetime “Promised Delivery”
- `delivery_date` Datetime “Delivery Date” (compute=_compute_delivery_date)
- `date_order` Datetime “Order Date” (required)
- `origin` Char “Source Document”
- `reference` Char “Payment Ref.”
- `pending_email_template_id` Many2one → `mail.template` “Pending Email Template” (readonly)
- `require_signature` Boolean “Online signature” (store, compute=_compute_require_signature)
- `prepayment_percent` Float “Prepayment” (store, compute=_compute_prepayment_percent)
- `prepayment_amount` Monetary “Prepayment Amount” (compute=_compute_prepayment_amount)
- `signature` Image “Signature”
- `signed_by` Char “Signed By”
- `signed_on` Datetime “Signed On”
- `validity_date` Date “Expiration” (store, compute=_compute_validity_date)
- `journal_id` Many2one → `account.journal` “Journal” (store, compute=_compute_journal_id)
- `document_tax_mode` Selection (required, store, compute=_compute_document_tax_mode)
- `note` Html “Terms and conditions” (store, compute=_compute_note)
- `partner_invoice_id` Many2one → `res.partner` “Invoice Address” (required, store, compute=_compute_partner_invoice_id)
- `partner_shipping_id` Many2one → `res.partner` “Delivery Address” (required, store, compute=_compute_partner_shipping_id)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position” (store, compute=_compute_fiscal_position_id)
- `payment_term_id` Many2one → `account.payment.term` “Payment Terms” (store, compute=_compute_payment_term_id)
- `preferred_payment_method_line_id` Many2one → `account.payment.method.line` “Payment Method” (store, compute=_compute_preferred_payment_method_line_id)
- `pricelist_id` Many2one → `product.pricelist` “Pricelist” (store, compute=_compute_pricelist_id)
- `currency_id` Many2one → `res.currency` (store, compute=_compute_currency_id)
- `currency_rate` Float “Currency Rate” (store, compute=_compute_currency_rate)
- `user_id` Many2one → `res.users` “Salesperson” (store, index, compute=_compute_user_id)
- `team_id` Many2one → `crm.team` “Sales Team” (store, index, compute=_compute_team_id)
- `incoterm` Many2one → `account.incoterms` “Incoterm” (store, compute=_compute_incoterm)
- `incoterm_location` Char “Incoterm Location” (store, compute=_compute_incoterm_location)
- `order_line` One2many → `sale.order.line` “Order Lines”
- `amount_untaxed` Monetary “Untaxed Amount” (store, compute=_compute_amounts)
- `amount_tax` Monetary “Taxes” (store, compute=_compute_amounts)
- `amount_total` Monetary “Total” (store, compute=_compute_amounts)
- `amount_to_invoice` Monetary “Un-invoiced Balance” (compute=_compute_amount_to_invoice)
- `amount_invoiced` Monetary “Already invoiced” (compute=_compute_amount_invoiced)
- `invoice_count` Integer “Invoice Count” (compute=_get_invoiced)
- `invoice_ids` Many2many → `account.move` “Invoices” (compute=_get_invoiced)
- `invoice_status` Selection “Invoice Status” (store, compute=_compute_invoice_status)
- `sale_warning_text` Text “Sale Warning” (compute=_compute_sale_warning_text)
- `show_sol_numbers` Boolean (related=company_id.show_sol_numbers)
- `transaction_count` Integer (compute=_compute_transaction_count)
- `transaction_ids` Many2many → `payment.transaction` “Transactions” (readonly)
- `authorized_transaction_ids` Many2many → `payment.transaction` “Authorized Transactions” (compute=_compute_authorized_transaction_ids)
- `has_authorized_transaction_ids` Boolean “Has Authorized Transactions” (compute=_compute_authorized_transaction_ids)
- `amount_paid` Float “Payment Transactions Amount” (compute=_compute_amount_paid)
- `amount_unpaid` Monetary “Amount Remaining” (store, compute=_compute_amount_unpaid)
- `campaign_id` Many2one
- `medium_id` Many2one
- `source_id` Many2one
- `tag_ids` Many2many → `crm.tag` “Tags”
- `country_code` Char “Country code” (related=company_id.account_fiscal_country_id.code)
- `company_price_include` Selection (related=company_id.account_price_include)
- `delivery_status` Selection “Delivery Status” (store, compute=_compute_delivery_status)
- `duplicated_order_ids` Many2many → `sale.order` (compute=_compute_duplicated_order_ids)
- `expected_date` Datetime “Expected Date” (compute=_compute_expected_date)
- `extra_total_fields` Json (compute=_compute_extra_total_fields)
- `is_expired` Boolean “Is Expired” (compute=_compute_is_expired)
- `is_unfulfilled` Boolean “Unfulfilled Orders”
- `partner_credit_warning` Text (compute=_compute_partner_credit_warning)
- `show_ship_button` Boolean (compute=_compute_show_ship_button)
- `tax_calculation_rounding_method` Selection (related=company_id.tax_calculation_rounding_method)
- `tax_country_id` Many2one → `res.country` (compute=_compute_tax_country_id)
- `tax_totals` Json (compute=_compute_tax_totals)
- `terms_type` Selection (related=company_id.terms_type)
- `type_name` Char “Type Name” (compute=_compute_type_name)
- `has_overages` Boolean (compute=_compute_has_overages)
- `invoice_overages` Boolean
- `has_active_pricelist` Boolean (compute=_compute_has_active_pricelist)
- `analytic_account_id` Many2one → `account.analytic.account` “Analytic Account”

Public methods: `action_cancel`, `action_close_invoicing`, `action_confirm`, `action_draft`, `action_lock`, `action_open_business_doc`, `action_open_discount_wizard`, `action_preview_sale_order`, `action_quotation_send`, `action_quotation_sent`, `action_reopen_order`, `action_unlock`, `action_view_invoice`, `action_view_payment_transaction`, `batch_onchange_sol`, `copy_data`, `create`, `create_document_from_attachment`, `deliver_sold_quantity`, `get_empty_list_help`, `get_import_templates`, `get_portal_last_transaction`, `message_post`, `onchange`, `payment_action_capture`, `payment_action_void`, `retrieve_sale_dashboard`, `write`

Extension points: `_action_cancel`, `_action_confirm`, `_check_not_partially_paid`, `_check_order_line_company_id`, `_check_prepayment_percent`, `_create_account_invoices`, `_create_down_payment_lines_from_base_lines`, `_create_down_payment_section_line_if_needed`, `_create_invoices`, `_create_upsell_activity`, `_get_action_add_from_catalog_extra_context`, `_get_advantages`, `_get_catalog_currency`, `_get_confirmation_template`, `_get_copiable_order_lines`, `_get_default_payment_link_values`, `_get_edi_builders`, `_get_invoice_grouping_keys`, `_get_invoiceable_lines`, `_get_invoiced`, `_get_lang`, `_get_model_description`, `_get_name_portal_content_view`, `_get_name_tax_totals_view`, `_get_note_url`, `_get_or_create_analytic_account`, `_get_order_lines_to_report`, `_get_period_domain`, `_get_portal_return_action`, `_get_prepayment_required_amount`, `_get_priced_lines`, `_get_product_catalog_default_prices`, `_get_product_catalog_domain`, `_get_product_catalog_product_data`, `_get_product_documents`, `_get_report_base_filename`, `_get_sale_period_totals`, `_get_update_prices_lines`, `_prepare_analytic_account_data`, `_prepare_confirmation_values`, `_prepare_down_payment_line_section_values`, `_prepare_down_payment_line_values_from_base_line`, `_prepare_down_payment_section_line`, `_prepare_invoice`

## `sale.order.line` (defines)

Sales Order Line

Inherits: `analytic.mixin`, `res.currency.rate.consolidation.mixin`, `product.catalog.line.mixin`

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
- `product_template_attribute_value_ids` Many2many (related=product_id.product_template_attribute_value_ids)
- `product_custom_attribute_value_ids` One2many → `product.attribute.custom.value` “Custom Values” (store, compute=_compute_custom_attribute_values)
- `product_no_variant_attribute_value_ids` Many2many → `product.template.attribute.value` “Extra Values” (store, compute=_compute_no_variant_attribute_values)
- `is_product_archived` Boolean (compute=_compute_is_product_archived)
- `name` Text “Description” (store, compute=_compute_name)
- `label` Text “Label” (compute=_compute_label)
- `product_uom_qty` Float “Quantity” (required, store, compute=_compute_product_uom_qty)
- `product_uom_id` Many2one → `uom.uom` “Unit” (store, compute=_compute_product_uom_id)
- `allowed_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_uom_ids)
- `qty_available_today` Float (compute=_compute_qty_at_date)
- `virtual_available_at_date` Float (compute=_compute_qty_at_date)
- `display_qty_widget` Boolean (compute=_compute_display_qty_widget)
- `is_storable` Boolean (related=product_id.is_storable)
- `scheduled_date` Datetime “Delivery Date” (compute=_compute_qty_at_date)
- `linked_line_id` Many2one → `sale.order.line` “Linked Order Line” (index)
- `linked_line_ids` One2many → `sale.order.line` “Linked Order Lines”
- `categ_id` Many2one (related=product_id.categ_id)
- `virtual_id` Char
- `linked_virtual_id` Char
- `selected_combo_items` Char
- `combo_item_id` Many2one → `product.combo.item`
- `tax_ids` Many2many → `account.tax` “Taxes” (store, compute=_compute_tax_ids)
- `document_tax_mode` Selection (related=order_id.document_tax_mode)
- `pricelist_item_id` Many2one → `product.pricelist.item` (compute=_compute_pricelist_item_id)
- `price_unit` Float “Unit Price” (required, store, compute=_compute_price_unit)
- `technical_price_unit` Float
- `discount` Float “Discount (%)” (store, compute=_compute_discount)
- `price_subtotal` Monetary “Subtotal” (store, compute=_compute_amount)
- `price_tax` Float “Total Tax” (store, compute=_compute_amount)
- `price_total` Monetary “Total” (store, compute=_compute_amount)
- `price_reduce_taxexcl` Monetary “Price Reduce Tax excl” (store, compute=_compute_price_reduce_taxexcl)
- `price_reduce_taxinc` Monetary “Price Reduce Tax incl” (store, compute=_compute_price_reduce_taxinc)
- `customer_lead` Integer “Lead Time” (required, store, compute=_compute_customer_lead)
- `qty_delivered_method` Selection “Method to update delivered qty” (store, compute=_compute_qty_delivered_method)
- `qty_delivered` Float “Delivery Quantity” (store, compute=_compute_qty_delivered)
- `qty_delivered_percent` Float “Delivered (%)” (compute=_compute_qty_delivered_percent)
- `qty_overage` Float (compute=_compute_qty_overage)
- `invoice_policy` Selection “Invoicing Policy” (compute=_compute_invoice_policy)
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
- `amount_to_invoice_at_date` Float “Amount” (compute=_compute_amount_to_invoice_at_date)
- `accrual_move_ids` Many2many → `account.move` “Accrual Entries”
- `qty_delivered_at_date` Float “Delivered” (compute=_compute_qty_delivered_at_date)
- `qty_invoiced_at_date` Float “Invoiced” (compute=_compute_qty_invoiced_at_date)
- `deferred_revenue` Boolean “Deferred Revenue”
- `invoice_to_be_issued` Boolean “Invoice to be Issued”
- `extra_tax_data` Json
- `product_type` Selection (related=product_id.type)
- `service_tracking` Selection (related=product_id.service_tracking)
- `product_updatable` Boolean “Can Edit Product” (compute=_compute_product_updatable)
- `product_uom_readonly` Boolean (compute=_compute_product_uom_readonly)
- `tax_calculation_rounding_method` Selection “Tax calculation rounding method” (readonly, related=company_id.tax_calculation_rounding_method)
- `company_price_include` Selection (related=company_id.account_price_include)
- `sale_line_warn_msg` Text (compute=_compute_sale_line_warn_msg)
- `parent_id` Many2one → `sale.order.line` “Parent Section Line” (compute=_compute_parent_id)
- `collapse_prices` Boolean “Collapse Prices”
- `collapse_composition` Boolean “Collapse Composition”
- `mandatory_product` Boolean “Is Product Mandatory” (compute=_compute_mandatory_product)
- `section_qty` Float “Section Quantity” (store, compute=_compute_section_qty)
- `section_uom_id` Many2one → `uom.uom` “Section Unit of Measure” (store, compute=_compute_section_uom_id)

Public methods: `action_add_from_catalog`, `compute_uom_qty`, `create`, `onchange`, `write`

Extension points: `_check_combo_item_id`, `_check_line_unlink`, `_get_accrual_domain`, `_get_accrual_line_ids`, `_get_catalog_unit_price`, `_get_combo_item_display_price`, `_get_combo_totals`, `_get_consu_qty_delivered_method`, `_get_custom_compute_tax_cache_key`, `_get_delivered_quantity_by_analytic`, `_get_delivered_quantity_by_analytic_domain`, `_get_discounted_price`, `_get_display_price`, `_get_display_price_ignore_combo`, `_get_downpayment_description`, `_get_downpayment_line_price_unit`, `_get_downpayment_state`, `_get_grouped_section_summary`, `_get_invoice_line_sequence`, `_get_invoice_lines`, `_get_lines_with_price`, `_get_linked_line`, `_get_linked_lines`, `_get_linked_lines_by_line`, `_get_order_date`, `_get_partner_display`, `_get_pricelist_kwargs`, `_get_pricelist_price`, `_get_pricelist_price_before_discount`, `_get_pricelist_price_context`, `_get_product_catalog_lines_data`, `_get_product_price_context`, `_get_product_uom_field`, `_get_protected_fields`, `_get_quantity_field`, `_get_rounding`, `_get_sale_order_line_multiline_description_sale`, `_get_sale_order_line_multiline_description_variants`, `_get_section_lines`, `_get_section_totals`, `_prepare_base_line_for_taxes_computation`, `_prepare_invoice_line`, `_prepare_invoice_lines_vals_list`, `_prepare_procurement_values`, `_prepare_qty_delivered`, `_prepare_qty_invoiced`

## `utm.campaign` (extends)

- `quotation_count` Integer “Quotation Count” (compute=_compute_quotation_count)
- `invoiced_amount` Monetary “Revenues generated by the campaign” (compute=_compute_sale_invoiced_amount)
- `currency_id` Many2one → `res.currency` “Currency” (compute=_compute_currency_id)

Public methods: `action_redirect_to_invoiced`, `action_redirect_to_quotations`

## `account.invoice.report` (extends)

- `team_id` Many2one → `crm.team` “Sales Team”
- `source_id` Many2one → `utm.source` “Source” (readonly)

## `sale.report` (defines)

Sales Analysis Report

- `name` Char “Order Reference” (readonly)
- `line_name` Char “Order Line Name” (readonly)
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
- `utm_reference` Reference “UTM Reference”
- `commercial_partner_id` Many2one → `res.partner` “Customer Entity” (readonly)
- `country_id` Many2one → `res.country` “Customer Country” (readonly)
- `industry_id` Many2one → `res.partner.industry` “Customer Industry” (readonly)
- `partner_zip` Char “Customer ZIP” (readonly)
- `state_id` Many2one → `res.country.state` “Customer State” (readonly)
- `partner_tag_ids` Many2many “Customer Tags” (readonly, related=partner_id.category_id)
- `order_reference` Reference “Order”
- `categ_id` Many2one → `product.category` “Product Category” (readonly)
- `product_id` Many2one → `product.product` “Product Variant” (readonly)
- `product_tmpl_id` Many2one → `product.template` “Product” (readonly)
- `product_uom_id` Many2one → `uom.uom` “Unit” (readonly)
- `product_uom_qty` Float “Qty Ordered” (readonly)
- `qty_to_deliver` Float “Qty To Deliver” (readonly)
- `qty_delivered` Float “Qty Delivered” (readonly)
- `qty_to_invoice` Float “Qty To Invoice” (readonly)
- `qty_invoiced` Float “Qty Invoiced” (readonly)
- `price_subtotal` Monetary “Untaxed Total” (readonly)
- `price_total` Monetary “Total” (readonly)
- `untaxed_amount_to_invoice` Monetary “Untaxed Amount To Invoice” (readonly)
- `untaxed_amount_invoiced` Monetary “Untaxed Amount Invoiced” (readonly)
- `untaxed_delivered_amount` Monetary “Untaxed Amount Delivered” (readonly)
- `line_invoice_status` Selection “Invoice Status” (readonly)
- `weight` Float “Gross Weight” (readonly)
- `volume` Float “Volume” (readonly)
- `price_unit` Monetary “Unit Price” (readonly)
- `discount` Float “Discount %” (readonly)
- `discount_amount` Monetary “Discount Amount” (readonly)
- `nbr` Integer “# of Lines” (readonly)
- `currency_id` Many2one → `res.currency` (readonly)

Public methods: `action_open_order`

Extension points: `_get_done_states`, `_get_order_reference`

## `account.accrued.orders.wizard` (extends)


Extension points: `_get_accrual_main_line_vals`, `_get_accrual_pending_cogs_vals`, `_get_accrual_qty_price_and_amount`

## `base.document.layout` (extends)


Extension points: `_get_preview_template`, `_get_render_information`

## `sale.mass.cancel.orders` (defines)

Cancel multiple quotations

- `sale_order_ids` Many2many → `sale.order` “Sale orders to cancel”
- `sale_orders_count` Integer (compute=_compute_sale_orders_count)
- `has_confirmed_order` Boolean (compute=_compute_has_confirmed_order)

Public methods: `action_mass_cancel`

## `payment.link.wizard` (extends)

Generate Sales Payment Link

- `amount_paid` Monetary “Already Paid” (readonly)
- `prepayment_amount` Monetary “Prepayment Amount”
- `confirmation_message` Char “Confirmation Message” (compute=_compute_confirmation_message)

Extension points: `_prepare_access_token`, `_prepare_query_params`, `_prepare_url`

## `res.config.settings` (extends)

- `group_auto_done_setting` Boolean “Lock Confirmed Sales”
- `group_discount_per_so_line` Boolean “Discounts”
- `group_proforma_sales` Boolean “Pro Forma Invoice”
- `group_warning_sale` Boolean “Sale Order Warnings”
- `group_services_and_material` Boolean “Services & Materials”
- `invoice_mail_template_id` Many2one → `mail.template` “Email Template”
- `sale_order_mandatory_product` Boolean “Mandatory Product”
- `quotation_validity_days` Integer (related=company_id.quotation_validity_days)
- `portal_confirmation_sign` Boolean (related=company_id.portal_confirmation_sign)
- `portal_confirmation_pay` Boolean (related=company_id.portal_confirmation_pay)
- `prepayment_percent` Float (related=company_id.prepayment_percent)
- `display_product_images_on_so` Boolean (related=company_id.display_product_images_on_so)
- `downpayment_account_id` Many2one (related=company_id.downpayment_account_id)
- `downpayment_account_active` Boolean “Down payment Account Active” (related=downpayment_account_id.active)
- `sale_invoice_policy` Selection (related=company_id.sale_invoice_policy)
- `sale_automatic_invoice` Boolean (related=company_id.sale_automatic_invoice)
- `show_sol_numbers` Boolean “Line Numbers” (related=company_id.show_sol_numbers)
- `module_delivery` Boolean “Delivery Methods”
- `module_product_email_template` Boolean “Specific Email”
- `module_sale_amazon` Boolean “Amazon Sync”
- `module_sale_commission` Boolean “Commissions”
- `module_sale_gelato` Boolean “Gelato”
- `module_sale_loyalty` Boolean “Coupons & Loyalty”
- `module_sale_pdf_quote_builder` Boolean “PDF Quote builder”
- `module_sale_product_matrix` Boolean “Sales Grid Entry”
- `module_sale_shopee` Boolean “Shopee Sync”

Public methods: `action_sale_start_payment_onboarding`, `set_values`

## `sale.advance.payment.inv` (defines)

Sales Advance Payment Invoice

- `advance_payment_method` Selection “Create Invoice” (required)
- `count` Integer “Order Count” (compute=_compute_count)
- `sale_order_ids` Many2many → `sale.order`
- `allow_invoice_overages` Boolean (compute=_compute_allow_invoice_overages)
- `invoice_overages` Boolean (compute=_compute_invoice_overages)
- `has_down_payments` Boolean “Has down payments” (compute=_compute_has_down_payments)
- `deduct_down_payments` Boolean “Deduct down payments”
- `amount` Float “Down Payment”
- `fixed_amount` Monetary “Down Payment Amount (Fixed)”
- `currency_id` Many2one → `res.currency` (store, compute=_compute_currency_id)
- `company_id` Many2one → `res.company` (store, compute=_compute_company_id)
- `amount_invoiced` Monetary “Already invoiced” (compute=_compute_invoice_amounts)
- `display_draft_invoice_warning` Boolean (compute=_compute_display_draft_invoice_warning)
- `consolidated_billing` Boolean “Consolidated Billing”

Public methods: `create_invoices`, `view_draft_invoices`

Extension points: `_check_amount_is_positive`, `_create_invoices`, `_get_down_payment_account`, `_prepare_down_payment_invoice_line_values`, `_prepare_down_payment_invoice_values`

## `sale.order.discount` (defines)

Discount Wizard

- `sale_order_id` Many2one → `sale.order` (required)
- `company_id` Many2one (related=sale_order_id.company_id)
- `currency_id` Many2one (related=sale_order_id.currency_id)
- `discount_amount` Monetary “Amount”
- `discount_percentage` Float “Percentage”
- `discount_type` Selection

Public methods: `action_apply_discount`

Extension points: `_check_discount_amount`, `_create_discount_lines`, `_get_discount_product`, `_get_discountable_order_lines`, `_prepare_discount_product_values`, `_prepare_global_discount_so_lines`

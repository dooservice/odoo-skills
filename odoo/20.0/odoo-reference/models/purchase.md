# purchase — Purchase

Depends on: account.

## `account.move` (extends)

- `purchase_vendor_bill_id` Many2one → `purchase.bill.union`
- `purchase_id` Many2one → `purchase.order` “Purchase Order”
- `purchase_order_count` Integer “Purchase Order Count” (compute=_compute_origin_po_count)
- `display_auto_complete_field` Boolean (compute=_compute_display_auto_complete)
- `purchase_order_name` Char (compute=_compute_purchase_order_name)
- `is_purchase_matched` Boolean (compute=_compute_is_purchase_matched)
- `purchase_matched_ratio` Float “Purchase Matched Ratio” (compute=_compute_is_purchase_matched)
- `purchase_warning_text` Text “Purchase Warning” (compute=_compute_purchase_warning_text)

Public methods: `action_purchase_matching`, `action_view_source_purchase_orders`, `create`, `write`

Extension points: `_get_action_add_from_catalog_extra_context`

## `account.move.line` (extends)

- `is_downpayment` Boolean
- `purchase_line_id` Many2one → `purchase.order.line`
- `purchase_order_id` Many2one → `purchase.order` (readonly, related=purchase_line_id.order_id)
- `purchase_matching_issue_msg` Char (compute=_compute_purchase_matching_issue_msg)
- `purchase_line_warn_msg` Text (compute=_compute_purchase_line_warn_msg)

Extension points: `_prepare_line_values_for_purchase`

## `account.tax` (extends)

- `purchase_order_line_ids` Many2many → `purchase.order.line` (readonly)

## `account.analytic.account` (extends)

- `purchase_order_count` Integer “Purchase Order Count” (compute=_compute_purchase_order_count)

Public methods: `action_view_purchase_orders`

## `account.analytic.applicability` (extends)

- `business_domain` Selection

## `ir.actions.report` (extends)


## `product.template` (extends)

- `purchased_product_qty` Float “Purchased” (compute=_compute_purchased_product_qty)
- `purchase_method` Selection “Control Policy” (store, compute=_compute_purchase_method)
- `purchase_line_warn_msg` Text “Message for Purchase Order Line”

Public methods: `action_view_po`, `get_import_templates`

Extension points: `_get_backend_root_menu_ids`, `_get_product_accounts`

## `product.product` (extends)

- `purchased_product_qty` Float “Purchased” (compute=_compute_purchased_product_qty)
- `sold_by_vendor_id` Many2one → `res.partner` “Vendor”

Public methods: `action_view_po`

Extension points: `_get_backend_root_menu_ids`, `_get_last_po_line`, `_get_last_po_seller_info`

## `product.supplierinfo` (extends)


Extension points: `_get_filtered_supplier`

## `product.category` (extends)

- `property_account_bills_to_receive_id` Many2one → `account.account` (company_dependent)
- `property_account_bills_to_receive_active` Boolean “Bills to Receive Account Active” (related=property_account_bills_to_receive_id.active)
- `property_account_billed_not_received_id` Many2one → `account.account` (company_dependent)
- `property_account_billed_not_received_active` Boolean “Billed Not Received Account Active” (related=property_account_billed_not_received_id.active)

## `purchase.bill.line.match` (defines)

Purchase Line and Vendor Bill line matching view

- `pol_id` Many2one → `purchase.order.line` (readonly)
- `matching_id` Integer “Matching” (readonly)
- `aml_id` Many2one → `account.move.line` (readonly)
- `company_id` Many2one → `res.company` (readonly)
- `partner_id` Many2one → `res.partner` (readonly)
- `product_id` Many2one → `product.product` (readonly)
- `line_qty` Float (readonly)
- `line_uom_id` Many2one → `uom.uom` (readonly)
- `qty_invoiced` Float (readonly)
- `qty_to_invoice` Float “Qty to invoice” (readonly)
- `qty_to_invoice_raw` Float “Qty not invoiced” (readonly)
- `purchase_order_id` Many2one → `purchase.order` (readonly)
- `account_move_id` Many2one → `account.move` (readonly)
- `line_amount_untaxed` Monetary (readonly)
- `currency_id` Many2one → `res.currency` (readonly)
- `state` Char (readonly)
- `date` Date (readonly)
- `display_matching_tag` Boolean (compute=_compute_display_matching_tag)
- `product_uom_id` Many2one → `uom.uom` (related=product_id.uom_id)
- `product_uom_qty` Float (compute=_compute_product_uom_qty)
- `product_uom_qty_to_invoice` Float (compute=_compute_product_uom_qty_to_invoice)
- `product_uom_price` Float (compute=_compute_product_uom_price)
- `billed_amount_untaxed` Monetary (compute=_compute_amount_untaxed_fields)
- `purchase_amount_untaxed` Monetary (compute=_compute_amount_untaxed_fields)
- `reference` Char (readonly)
- `description` Char (readonly)

Public methods: `action_add_to_po`, `action_match_lines`, `action_open_line`, `action_unmatch_lines`

Extension points: `_action_create_bill_from_po_lines`

## `purchase.order` (defines)

Purchase Order

Inherits: `portal.mixin`, `product.catalog.mixin`, `mail.thread`, `mail.activity.mixin`, `account.document.import.mixin`

- `name` Char “Order Reference” (required)
- `priority` Selection (index)
- `origin` Char “Source”
- `partner_ref` Char “Vendor Reference”
- `date_order` Datetime “Order Deadline” (required, index)
- `date_approve` Datetime “Order Date” (readonly, index)
- `partner_id` Many2one → `res.partner` “Vendor” (required, index)
- `dest_address_id` Many2one → `res.partner` “Dropship Address”
- `currency_id` Many2one → `res.currency` (required, store, compute=_compute_currency_id)
- `state` Selection “Status” (readonly, index)
- `locked` Boolean
- `lock_confirmed_po` Selection (related=company_id.po_lock)
- `order_line` One2many → `purchase.order.line` “Order Lines”
- `acknowledged` Boolean “Acknowledged”
- `note` Html “Terms and Conditions”
- `partner_bill_count` Integer (related=partner_id.supplier_invoice_count)
- `bill_matched_ratio` Float “Bill Matched Ratio” (compute=_compute_bill_matched_ratio)
- `invoice_count` Integer “Bill Count” (store, compute=_compute_invoice)
- `invoice_ids` Many2many → `account.move` “Bills” (store, compute=_compute_invoice)
- `invoice_status` Selection “Billing Status” (readonly, store, compute=_get_invoiced)
- `date_planned` Datetime “Expected Arrival” (store, index, compute=_compute_date_planned)
- `date_calendar_start` Datetime (readonly, store, compute=_compute_date_calendar_start)
- `amount_untaxed` Monetary “Untaxed Amount” (readonly, store, compute=_amount_all)
- `tax_totals` Json (compute=_compute_tax_totals)
- `amount_tax` Monetary “Taxes” (readonly, store, compute=_amount_all)
- `amount_total` Monetary “Total” (readonly, store, compute=_amount_all)
- `amount_total_cc` Monetary “Total in currency” (readonly, store, compute=_amount_all)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position”
- `tax_country_id` Many2one → `res.country` (compute=_compute_tax_country_id)
- `tax_calculation_rounding_method` Selection “Tax calculation rounding method” (readonly, related=company_id.tax_calculation_rounding_method)
- `document_tax_mode` Selection (required, store, compute=_compute_document_tax_mode)
- `payment_term_id` Many2one → `account.payment.term`
- `incoterm_id` Many2one → `account.incoterms` (store, compute=_compute_incoterm_id)
- `incoterm_location` Char “Incoterm Location” (store, compute=_compute_incoterm_location)
- `product_id` Many2one → `product.product` “Product” (related=order_line.product_id)
- `user_id` Many2one → `res.users` “Buyer” (index)
- `company_id` Many2one → `res.company` (required, index)
- `company_currency_id` Many2one “Company Currency” (related=company_id.currency_id)
- `country_code` Char “Country code” (related=company_id.account_fiscal_country_id.code)
- `company_price_include` Selection (related=company_id.account_price_include)
- `currency_rate` Float “Currency Rate” (store, compute=_compute_currency_rate)
- `duplicated_order_ids` Many2many → `purchase.order` (compute=_compute_duplicated_order_ids)
- `receipt_status` Selection “Receipt Status” (store, compute=_compute_receipt_status)
- `receipt_reminder_email` Boolean “Receipt Reminder” (store, compute=_compute_receipt_reminder_email)
- `reminder_date_before_receipt` Integer “Days Before Receipt” (store, compute=_compute_receipt_reminder_email)
- `is_late` Boolean “Is Late”
- `show_comparison` Boolean “Show Comparison” (compute=_compute_show_comparison)
- `show_receive_button` Boolean (compute=_compute_show_receive_button)
- `purchase_warning_text` Text “Purchase Warning” (compute=_compute_purchase_warning_text)

Public methods: `action_acknowledge`, `action_add_from_catalog`, `action_bill_matching`, `action_create_invoice`, `action_merge`, `action_open_business_doc`, `action_purchase_comparison`, `action_receive`, `action_rfq_send`, `action_view_invoice`, `button_approve`, `button_cancel`, `button_confirm`, `button_draft`, `button_lock`, `button_reset_date_order`, `button_unlock`, `copy`, `create`, `create_document_from_attachment`, `get_acknowledge_url`, `get_confirm_url`, `get_import_templates`, `get_localized_date_planned`, `get_order_timezone`, `get_update_url`, `message_post`, `onchange`, `onchange_date_planned`, `onchange_partner_id`, `retrieve_dashboard`, `send_reminder_preview`

Extension points: `_check_order_line_company_id`, `_create_downpayments`, `_create_update_date_activity`, `_get_action_add_from_catalog_extra_context`, `_get_catalog_currency`, `_get_domain_is_late`, `_get_edi_builders`, `_get_invoiced`, `_get_orders_to_remind`, `_get_product_catalog_default_unit_price`, `_get_product_catalog_domain`, `_get_product_catalog_product_data`, `_get_product_catalog_seller_data`, `_get_product_catalog_uom_data`, `_get_product_price_type`, `_get_report_base_filename`, `_prepare_down_payment_section_values`, `_prepare_grouped_data`, `_prepare_invoice`

## `purchase.order.line` (defines)

Purchase Order Line

Inherits: `analytic.mixin`, `res.currency.rate.consolidation.mixin`, `product.catalog.line.mixin`

- `name` Text “Description” (store, compute=_compute_price_unit_and_date_planned_and_name)
- `label` Text “Label” (compute=_compute_label)
- `sequence` Integer “Sequence”
- `product_qty` Float “Quantity” (required)
- `product_uom_qty` Float “Total Quantity” (store, compute=_compute_product_uom_qty)
- `date_planned` Datetime “Expected Arrival” (store, index, compute=_compute_price_unit_and_date_planned_and_name)
- `discount` Float “Discount (%)” (store, compute=_compute_price_unit_and_date_planned_and_name)
- `tax_ids` Many2many → `account.tax` “Taxes”
- `document_tax_mode` Selection (related=order_id.document_tax_mode)
- `allowed_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_uom_ids)
- `uom_id` Many2one → `uom.uom` “Unit”
- `product_id` Many2one → `product.product` “Product”
- `product_type` Selection (readonly, related=product_id.type)
- `price_unit` Float “Unit Price” (required, store, compute=_compute_price_unit_and_date_planned_and_name)
- `price_unit_product_uom` Float “Unit Price Product UoM” (store, compute=_compute_price_unit_product_uom)
- `price_unit_discounted` Float “Unit Price (Discounted)” (compute=_compute_price_unit_discounted)
- `price_subtotal` Monetary “Subtotal” (store, compute=_compute_amount)
- `price_subtotal_to_invoice` Monetary “To Invoice” (compute=_compute_price_subtotal_to_invoice)
- `price_total` Monetary “Total” (store, compute=_compute_amount)
- `price_tax` Float “Tax” (store, compute=_compute_amount)
- `non_deductible_tax` Float (store, compute=_compute_amount)
- `order_id` Many2one → `purchase.order` “Order Reference” (required, index)
- `company_id` Many2one → `res.company` “Company” (readonly, store, index, related=order_id.company_id)
- `state` Selection (related=order_id.state)
- `invoice_lines` One2many → `account.move.line` “Bill Lines” (readonly)
- `matched_invoice_count` Integer “Matched Invoices Count” (compute=_compute_matched_invoice_count)
- `qty_invoiced` Float “Billed Qty” (store, compute=_compute_qty_invoiced)
- `qty_received_method` Selection “Received Qty Method” (store, compute=_compute_qty_received_method)
- `qty_received` Float “Received Qty” (store, compute=_compute_qty_received)
- `qty_received_manual` Float “Manual Received Qty”
- `qty_to_invoice` Float “To Invoice Quantity” (readonly, store, compute=_compute_qty_invoiced)
- `qty_to_invoice_raw` Float “Not Invoiced Quantity” (store, compute=_compute_qty_to_invoice_raw)
- `qty_received_at_date` Float “Received” (compute=_compute_qty_received_at_date)
- `qty_invoiced_at_date` Float “Billed” (compute=_compute_qty_invoiced_at_date)
- `amount_to_invoice_at_date` Float “Amount” (compute=_compute_amount_to_invoice_at_date)
- `accrual_move_ids` Many2many → `account.move` “Accrual Entries”
- `prepaid_expense` Boolean “Prepaid Expense”
- `bill_to_receive` Boolean “Bill to Receive”
- `partner_id` Many2one → `res.partner` “Partner” (readonly, store, related=order_id.partner_id)
- `currency_id` Many2one “Currency” (related=order_id.currency_id)
- `date_order` Datetime “Order Deadline” (readonly, related=order_id.date_order)
- `date_approve` Datetime “Confirmation Date” (readonly, related=order_id.date_approve)
- `tax_calculation_rounding_method` Selection “Tax calculation rounding method” (readonly, related=company_id.tax_calculation_rounding_method)
- `display_type` Selection
- `is_downpayment` Boolean
- `selected_seller_id` Many2one → `product.supplierinfo` (compute=_compute_selected_seller_id)
- `product_template_attribute_value_ids` Many2many (readonly, related=product_id.product_template_attribute_value_ids)
- `product_no_variant_attribute_value_ids` Many2many → `product.template.attribute.value` “Product attribute values that do not create variants”
- `purchase_line_warn_msg` Text (compute=_compute_purchase_line_warn_msg)
- `parent_id` Many2one → `purchase.order.line` “Parent Section Line” (compute=_compute_parent_id)
- `technical_price_unit` Float (store, compute=_compute_price_unit_and_date_planned_and_name)

Public methods: `action_add_from_catalog`, `action_open_invoices`, `action_open_order`, `create`, `onchange_product_id`, `write`

Extension points: `_get_accrual_domain`, `_get_accrual_line_ids`, `_get_catalog_unit_price`, `_get_date_planned`, `_get_gross_price_unit`, `_get_invoice_lines`, `_get_product_display_name`, `_get_product_purchase_description`, `_get_product_uom_field`, `_get_qty_to_invoice_at_date`, `_get_quantity_field`, `_get_rounding`, `_get_section_lines`, `_get_section_totals`, `_get_select_sellers_params`, `_get_seller_info`, `_prepare_account_move_line`, `_prepare_add_missing_fields`, `_prepare_base_line_for_taxes_computation`, `_prepare_purchase_order_line`, `_prepare_qty_invoiced`, `_prepare_qty_received`

## `res.company` (extends)

- `account_bills_to_receive_id` Many2one → `account.account` “Bills to Receive Account”
- `account_billed_not_received_id` Many2one → `account.account` “Billed Not Received Account”
- `po_lock` Selection “Purchase Order Modification”
- `po_double_validation` Selection “Levels of Approvals”
- `po_double_validation_amount` Monetary “Double validation amount”

Extension points: `_get_accrual_candidate_lines`

## `res.config.settings` (extends)

- `lock_confirmed_po` Boolean “Lock Confirmed Orders”
- `po_lock` Selection “Purchase Order Modification *” (related=company_id.po_lock)
- `po_order_approval` Boolean “Purchase Order Approval”
- `po_double_validation` Selection “Levels of Approvals *” (related=company_id.po_double_validation)
- `po_double_validation_amount` Monetary “Minimum Amount” (related=company_id.po_double_validation_amount)
- `company_currency_id` Many2one → `res.currency` “Company Currency” (readonly, related=company_id.currency_id)
- `group_warning_purchase` Boolean “Purchase Warnings”
- `module_account_3way_match` Boolean “3-way matching: purchases, receptions and bills”
- `module_purchase_requisition` Boolean “Purchase Agreements”
- `module_purchase_alternative` Boolean “Purchase Alternative”
- `module_purchase_product_matrix` Boolean “Purchase Grid Entry”
- `group_send_reminder` Boolean “Receipt Reminder”

Public methods: `set_values`

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `res.partner` (extends)

- `property_purchase_currency_id` Many2one → `res.currency` “Supplier Currency” (company_dependent)
- `purchase_order_count` Integer “Purchase Order Count” (compute=_compute_purchase_order_count)
- `purchase_warn_msg` Text “Message for Purchase Order”
- `receipt_reminder_email` Boolean “Receipt Reminder” (company_dependent)
- `reminder_date_before_receipt` Integer “Days Before Receipt” (company_dependent)
- `buyer_id` Many2one → `res.users` “Buyer”
- `purchase_incoterm_location` Char “Vendor Incoterm Location”
- `purchase_incoterm_id` Many2one → `account.incoterms` “Vendor Incoterm”

Public methods: `write`

## `purchase.bill.union` (defines)

Purchases & Bills Union

- `name` Char “Reference” (readonly)
- `reference` Char “Source” (readonly)
- `partner_id` Many2one → `res.partner` “Vendor” (readonly)
- `date` Date “Date” (readonly)
- `amount` Float “Amount” (readonly)
- `currency_id` Many2one → `res.currency` “Currency” (readonly)
- `company_id` Many2one → `res.company` (readonly)
- `vendor_bill_id` Many2one → `account.move` “Vendor Bill” (readonly)
- `purchase_order_id` Many2one → `purchase.order` “Purchase Order” (readonly)

## `purchase.report` (defines)

Purchase Report

- `date_order` Datetime “Order Deadline” (readonly)
- `state` Selection (readonly)
- `product_id` Many2one → `product.product` (readonly)
- `partner_id` Many2one → `res.partner` (readonly)
- `date_approve` Datetime “Confirmation Date” (readonly)
- `uom_id` Many2one → `uom.uom` (readonly)
- `company_id` Many2one → `res.company` (readonly)
- `currency_id` Many2one → `res.currency` (readonly)
- `user_id` Many2one → `res.users` (readonly)
- `delay` Float “Days to Confirm” (readonly)
- `delay_pass` Float “Days to Receive” (readonly)
- `price_total` Monetary “Total” (readonly)
- `price_average` Monetary “Average Cost” (readonly)
- `nbr_lines` Integer “# of Lines” (readonly)
- `category_id` Many2one → `product.category` (readonly)
- `product_tmpl_id` Many2one → `product.template` (readonly)
- `country_id` Many2one → `res.country` (readonly)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position” (readonly)
- `commercial_partner_id` Many2one → `res.partner` (readonly)
- `weight` Float “Gross Weight” (readonly)
- `volume` Float “Volume” (readonly)
- `order_id` Many2one → `purchase.order` (readonly)
- `untaxed_total` Monetary “Untaxed Total” (readonly)
- `qty_ordered` Float “Qty Ordered” (readonly)
- `qty_received` Float “Qty Received” (readonly)
- `qty_billed` Float “Qty Billed” (readonly)
- `qty_to_be_billed` Float “Qty to be Billed” (readonly)

Public methods: `action_open_purchase_order`

## `account.accrued.orders.wizard` (extends)


Extension points: `_get_accrual_main_line_vals`, `_get_accrual_pending_cogs_vals`, `_get_purchase_accrual_amounts_and_label`, `_get_purchase_accrual_qty_and_price_unit`

## `bill.to.po.wizard` (defines)

Bill to Purchase Order

- `purchase_order_id` Many2one → `purchase.order`
- `partner_id` Many2one → `res.partner`

Public methods: `action_add_downpayment`, `action_add_to_po`

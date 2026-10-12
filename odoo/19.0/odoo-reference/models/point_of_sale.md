# point_of_sale — Point of Sale

Depends on: resource, stock_account, barcodes, html_editor, digest, phone_validation, partner_autocomplete, iot_base, google_address_autocomplete.

## `account.account` (extends)

Inherits: `pos.load.mixin`


## `account.bank.statement.line` (extends)

- `pos_session_id` Many2one → `pos.session` “Session”

## `account.cash.rounding` (extends)


## `account.fiscal.position` (extends)

Inherits: `pos.load.mixin`


Public methods: `action_archive`

## `account.journal` (extends)

- `pos_payment_method_ids` One2many → `pos.payment.method` “Point of Sale Payment Methods”

Public methods: `action_archive`

Extension points: `_check_no_active_payments`, `_check_type`, `_get_journal_inbound_outstanding_payment_accounts`

## `account.move` (extends)

Inherits: `pos.load.mixin`

- `pos_order_ids` One2many → `pos.order`
- `pos_payment_ids` One2many → `pos.payment`
- `pos_refunded_invoice_ids` Many2many → `account.move`
- `reversed_pos_order_id` Many2one → `pos.order` “Reversed POS Order”
- `pos_session_ids` One2many → `pos.session`
- `pos_order_count` Integer “POS Order Count” (compute=_compute_origin_pos_count)

Public methods: `action_view_source_pos_orders`, `button_draft`

Extension points: `_get_invoiced_lot_values`

## `account.move.line` (extends)


Extension points: `_get_cogs_value`

## `account.payment` (extends)

- `pos_payment_method_id` Many2one → `pos.payment.method`
- `force_outstanding_account_id` Many2one → `account.account`
- `pos_session_id` Many2one → `pos.session`

Extension points: `_get_payment_method_codes_to_exclude`

## `account.tax` (extends)

Inherits: `pos.load.mixin`

- `pos_order_line_ids` Many2many → `pos.order.line` (readonly)

Public methods: `write`

## `account.tax.group` (extends)

Inherits: `pos.load.mixin`


## `barcode.rule` (extends)

- `type` Selection

## `decimal.precision` (extends)

Inherits: `pos.load.mixin`


## `digest.digest` (extends)

- `kpi_pos_total` Boolean “POS Sales”
- `kpi_pos_total_value` Monetary (compute=_compute_kpi_pos_total_value)

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`

## `ir.module.module` (extends)

Inherits: `pos.load.mixin`


## `ir.sequence` (extends)


## `pos.bill` (defines)

Coins/Bills

Inherits: `pos.load.mixin`

- `name` Char “Name”
- `value` Float “Value” (required)
- `pos_config_ids` Many2many → `pos.config` “Point of Sales”

Public methods: `name_create`

## `pos.bus.mixin` (defines)

Bus Mixin

- `access_token` Char “Security Token”

Public methods: `create`

## `pos.category` (defines)

Point of Sale Category

Inherits: `pos.load.mixin`

- `name` Char “Category Name” (required)
- `parent_id` Many2one → `pos.category` “Parent Category” (index)
- `child_ids` One2many → `pos.category` “Children Categories”
- `sequence` Integer
- `image_512` Image “Image”
- `image_128` Image “Image 128” (store, related=image_512)
- `color` Integer “Color”
- `hour_until` Float “Availability Until”
- `hour_after` Float “Availability After”
- `has_image` Boolean (compute=_compute_has_image)

Public methods: `get_default_color`

Extension points: `_check_category_recursion`, `_check_hour`, `_get_descendants`, `_get_hierarchy`

## `pos.config` (defines)

Point of Sale Configuration

Inherits: `pos.bus.mixin`, `pos.load.mixin`

- `name` Char “Point of Sale” (required)
- `printer_ids` Many2many → `pos.printer` “Order Printers”
- `is_order_printer` Boolean “Order Printer”
- `is_installed_account_accountant` Boolean “Is the Full Accounting Installed” (compute=_compute_is_installed_account_accountant)
- `picking_type_id` Many2one → `stock.picking.type` “Operation Type” (required)
- `journal_id` Many2one → `account.journal` “Point of Sale Journal”
- `invoice_journal_id` Many2one → `account.journal` “Invoice Journal”
- `currency_id` Many2one → `res.currency` “Currency” (store, compute=_compute_currency)
- `order_seq_id` Many2one → `ir.sequence` “Order Sequence” (readonly)
- `order_backend_seq_id` Many2one → `ir.sequence` “Order Backend Sequence” (readonly)
- `order_line_seq_id` Many2one → `ir.sequence` “Order Line Sequence” (readonly)
- `device_seq_id` Many2one → `ir.sequence` “Device Sequence” (readonly)
- `iface_cashdrawer` Boolean “Cashdrawer”
- `iface_electronic_scale` Boolean “Electronic Scale”
- `iface_print_via_proxy` Boolean “Print via Proxy”
- `iface_scan_via_proxy` Boolean “Scan via Proxy”
- `iface_big_scrollbars` Boolean “Large Scrollbars”
- `iface_group_by_categ` Boolean “Group products by categories”
- `iface_print_auto` Boolean “Automatic Receipt Printing”
- `iface_print_skip_screen` Boolean “Skip Preview Screen”
- `iface_tax_included` Selection “Tax Display” (required)
- `iface_available_categ_ids` Many2many → `pos.category` “Available PoS Product Categories”
- `customer_display_bg_img` Image “Background Image”
- `customer_display_bg_img_name` Char “Background Image Name”
- `restrict_price_control` Boolean “Restrict Price Modifications to Managers”
- `is_margins_costs_accessible_to_every_user` Boolean “Margins & Costs”
- `cash_control` Boolean “Advanced Cash Control” (compute=_compute_cash_control)
- `set_maximum_difference` Boolean “Set Maximum Difference”
- `receipt_header` Text “Receipt Header”
- `receipt_footer` Text “Receipt Footer”
- `basic_receipt` Boolean “Basic Receipt”
- `proxy_ip` Char “IP Address”
- `active` Boolean
- `uuid` Char (readonly)
- `session_ids` One2many → `pos.session` “Sessions”
- `current_session_id` Many2one → `pos.session` “Current Session” (compute=_compute_current_session)
- `current_session_state` Char (compute=_compute_current_session)
- `number_of_rescue_session` Integer “Number of Rescue Session” (compute=_compute_current_session)
- `last_session_closing_cash` Float (compute=_compute_last_session)
- `last_session_closing_date` Date (compute=_compute_last_session)
- `pos_session_username` Char (compute=_compute_current_session_user)
- `pos_session_state` Char (compute=_compute_current_session_user)
- `pos_session_duration` Char (compute=_compute_current_session_user)
- `pricelist_id` Many2one → `product.pricelist` “Default Pricelist”
- `available_pricelist_ids` Many2many → `product.pricelist` “Available Pricelists”
- `company_id` Many2one → `res.company` “Company” (required)
- `group_pos_manager_id` Many2one → `res.groups` “Point of Sale Manager Group”
- `group_pos_user_id` Many2one → `res.groups` “Point of Sale User Group”
- `iface_tipproduct` Boolean “Product tips”
- `tip_product_id` Many2one → `product.product` “Tip Product”
- `fiscal_position_ids` Many2many → `account.fiscal.position` “Fiscal Positions”
- `default_fiscal_position_id` Many2one → `account.fiscal.position` “Default Fiscal Position”
- `default_bill_ids` Many2many → `pos.bill` “Coins/Bills”
- `use_pricelist` Boolean “Use a pricelist.”
- `use_presets` Boolean “Use Presets”
- `default_preset_id` Many2one → `pos.preset` “Default Preset”
- `available_preset_ids` Many2many → `pos.preset` “Available Presets”
- `tax_regime_selection` Boolean “Tax Regime Selection value”
- `limit_categories` Boolean “Restrict Categories”
- `module_pos_restaurant` Boolean “Is a Bar/Restaurant”
- `module_pos_avatax` Boolean “AvaTax PoS Integration”
- `module_pos_discount` Boolean “Global Discounts”
- `module_pos_appointment` Boolean “Online Booking”
- `is_posbox` Boolean “PosBox”
- `is_header_or_footer` Boolean “Custom Header & Footer”
- `module_pos_hr` Boolean
- `amount_authorized_diff` Float “Amount Authorized Difference”
- `payment_method_ids` Many2many → `pos.payment.method` “Payment Methods”
- `company_has_template` Boolean “Company has chart of accounts” (compute=_compute_company_has_template)
- `current_user_id` Many2one → `res.users` “Current Session Responsible” (compute=_compute_current_session_user)
- `other_devices` Boolean “Other Devices”
- `rounding_method` Many2one → `account.cash.rounding` “Cash rounding”
- `cash_rounding` Boolean “Cash Rounding”
- `only_round_cash_method` Boolean “Only apply rounding on cash”
- `has_active_session` Boolean (compute=_compute_current_session)
- `manual_discount` Boolean “Line Discounts”
- `ship_later` Boolean “Ship Later”
- `warehouse_id` Many2one → `stock.warehouse` (store, compute=_compute_warehouse_id)
- `route_id` Many2one → `stock.route` “Spefic route for products delivered later.”
- `picking_policy` Selection “Shipping Policy” (required)
- `auto_validate_terminal_payment` Boolean
- `trusted_config_ids` Many2many → `pos.config` “Trusted Point of Sale Configurations”
- `access_token` Char “Access Token”
- `show_product_images` Boolean “Show Product Images”
- `show_category_images` Boolean “Show Category Images”
- `note_ids` Many2many → `pos.note` “Note Models”
- `module_pos_sms` Boolean “SMS Enabled”
- `is_closing_entry_by_product` Boolean “Closing Entry by product”
- `order_edit_tracking` Boolean “Track orders edits”
- `last_data_change` Datetime “Last Write Date” (readonly, store, compute=_compute_local_data_integrity)
- `fallback_nomenclature_id` Many2one → `barcode.nomenclature` “Fallback Nomenclature”
- `epson_printer_ip` Char “Epson Printer IP”
- `use_fast_payment` Boolean “Fast Payment Validation”
- `fast_payment_method_ids` Many2many → `pos.payment.method` “Fast Payment Methods” (store, compute=_compute_fast_payment_method_ids)
- `statistics_for_current_session` Json “Session Statistics” (compute=_compute_statistics_for_session)

Public methods: `action_pos_config_modal_edit`, `close_ui`, `create`, `execute`, `get_limited_partners_loading`, `get_limited_product_count`, `get_pos_kanban_view_state`, `get_product_loading_info`, `get_record_by_ref`, `get_statistics_for_session`, `install_pos_restaurant`, `load_demo_data`, `load_onboarding_bakery_scenario`, `load_onboarding_clothes_scenario`, `load_onboarding_furniture_scenario`, `load_onboarding_retail_scenario`, `notify_synchronisation`, `open_existing_session_cb`, `open_opened_rescue_session_form`, `open_ui`, `read_config_open_orders`, `register_new_device_identifier`, `unlink`, `update_customer_display`, `write`

Extension points: `_action_to_open_ui`, `_check_before_creating_new_session`, `_check_companies`, `_check_company_has_fiscal_country`, `_check_company_has_template`, `_check_company_payment`, `_check_currencies`, `_check_groups_implied`, `_check_header_footer`, `_check_modules_to_install`, `_check_payment_method_ids`, `_check_payment_method_ids_journal`, `_check_pos_manager_access`, `_check_pricelists`, `_check_profit_loss_cash_journal`, `_check_rounding_method_strategy`, `_check_trusted_config_ids_currency`, `_create_cash_payment_method`, `_create_journal_and_payment_methods`, `_create_sequences`, `_get_available_pricelists`, `_get_customer_display_data`, `_get_default_demo_data_xml_id`, `_get_default_tip_product`, `_get_demo_data_loader_methods`, `_get_display_device_ip`, `_get_forbidden_change_fields`, `_get_group_pos_manager`, `_get_group_pos_user`, `_get_limited_partner_count`, `_get_next_order_refs`, `_get_payment_method`, `_get_special_products`, `_get_suffixed_ref_name`, `_get_url_to_cache`

## `pos.load.mixin` (defines)

PoS data loading mixin


## `pos.note` (defines)

PoS Note

Inherits: `pos.load.mixin`

- `name` Char (required)
- `sequence` Integer “Sequence”
- `color` Integer “Color”

## `pos.order` (defines)

Point of Sale Orders

Inherits: `portal.mixin`, `pos.bus.mixin`, `pos.load.mixin`, `mail.thread`

- `name` Char “Order Ref” (required, readonly)
- `last_order_preparation_change` Char “Last preparation change”
- `date_order` Datetime “Date” (readonly, index)
- `user_id` Many2one → `res.users` “Employee”
- `amount_difference` Monetary “Difference” (readonly)
- `amount_tax` Monetary “Taxes” (required, readonly)
- `amount_total` Monetary “Total” (required, readonly)
- `amount_paid` Monetary “Paid” (required)
- `amount_return` Monetary “Returned” (required, readonly)
- `margin` Monetary “Margin” (compute=_compute_margin)
- `margin_percent` Float “Margin (%)” (compute=_compute_margin)
- `is_total_cost_computed` Boolean (compute=_compute_is_total_cost_computed)
- `lines` One2many → `pos.order.line` “Order Lines”
- `company_id` Many2one → `res.company` “Company” (required, readonly, index)
- `country_code` Char (related=company_id.account_fiscal_country_id.code)
- `pricelist_id` Many2one → `product.pricelist` “Pricelist”
- `partner_id` Many2one → `res.partner` “Customer”
- `sequence_number` Integer “Sequence Number”
- `session_id` Many2one → `pos.session` “Session” (index)
- `config_id` Many2one → `pos.config` “Point of Sale” (store, compute=_compute_order_config_id)
- `currency_id` Many2one → `res.currency` “Currency” (related=config_id.currency_id)
- `currency_rate` Float “Currency Rate” (readonly, store, compute=_compute_currency_rate)
- `is_refund` Boolean “Is Refund” (readonly)
- `state` Selection (readonly, index)
- `account_move` Many2one → `account.move` “Invoice” (readonly)
- `picking_ids` One2many → `stock.picking`
- `picking_count` Integer (compute=_compute_picking_count)
- `failed_pickings` Boolean (compute=_compute_picking_count)
- `picking_type_id` Many2one → `stock.picking.type` “Operation Type” (related=session_id.config_id.picking_type_id)
- `stock_reference_ids` Many2many → `stock.reference` “Reference”
- `preset_id` Many2one → `pos.preset` “Preset”
- `floating_order_name` Char “Order Name”
- `general_customer_note` Text “General Customer Note”
- `internal_note` Text “Internal Note”
- `nb_print` Integer “Number of Print” (readonly)
- `pos_reference` Char “Receipt Number” (readonly, index)
- `sale_journal` Many2one → `account.journal` “Sales Journal” (readonly, store, related=session_id.config_id.journal_id)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position”
- `payment_ids` One2many → `pos.payment` “Payments”
- `session_move_id` Many2one → `account.move` “Session Journal Entry” (readonly, related=session_id.move_id)
- `to_invoice` Boolean “To invoice”
- `shipping_date` Date “Shipping Date”
- `preset_time` Datetime “Hour”
- `is_invoiced` Boolean “Is Invoiced” (compute=_compute_is_invoiced)
- `is_tipped` Boolean “Is this already tipped?” (readonly)
- `tip_amount` Monetary “Tip Amount” (readonly)
- `refund_orders_count` Integer “Number of Refund Orders” (compute=_compute_refund_related_fields)
- `refunded_order_id` Many2one → `pos.order` (compute=_compute_refund_related_fields)
- `has_refundable_lines` Boolean “Has Refundable Lines” (compute=_compute_has_refundable_lines)
- `ticket_code` Char
- `tracking_number` Char “Order Number” (readonly)
- `uuid` Char “Uuid” (readonly)
- `email` Char “Email” (store, compute=_compute_contact_details)
- `mobile` Char “Mobile” (store, compute=_compute_contact_details)
- `is_edited` Boolean “Edited” (compute=_compute_is_edited)
- `has_deleted_line` Boolean “Has Deleted Line”
- `order_edit_tracking` Boolean (readonly, related=config_id.order_edit_tracking)
- `available_payment_method_ids` Many2many → `pos.payment.method` “Available Payment Methods” (readonly, related=config_id.payment_method_ids)
- `invoice_status` Selection “Invoice Status” (compute=_compute_invoice_status)
- `reversed_move_ids` One2many → `account.move` “Reversal Account Moves”
- `source` Selection “Origin”

Public methods: `action_create_invoices`, `action_pos_order_cancel`, `action_pos_order_invoice`, `action_pos_order_paid`, `action_send_mail`, `action_send_receipt`, `action_stock_picking`, `action_view_invoice`, `action_view_refund_orders`, `action_view_refunded_order`, `add_payment`, `create`, `get_preparation_change`, `get_reference_last_part`, `get_stock_reports_to_print`, `read_pos_data`, `read_pos_data_uuid`, `read_pos_orders`, `refund`, `remove_from_ui`, `search_paid_order_ids`, `sync_from_ui`, `write`

Extension points: `_create_invoice`, `_create_misc_reversal_move`, `_create_order_picking`, `_create_pm_change_log`, `_get_invoice_lines_values`, `_get_invoice_post_context`, `_get_mail_attachments`, `_get_open_order`, `_get_order_log_representation`, `_get_order_name_from_pos_reference`, `_get_partner_bank_id`, `_get_payments`, `_get_pos_anglo_saxon_price_unit`, `_get_refunded_orders`, `_get_rounded_amount`, `_get_valid_session`, `_prepare_aml_values_list_per_nature`, `_prepare_invoice_lines`, `_prepare_invoice_vals`, `_prepare_mail_values`, `_prepare_pos_log`, `_prepare_product_aml_dict`, `_prepare_refund_values`, `_prepare_tax_base_line_values`

## `pos.order.line` (defines)

Point of Sale Order Lines

Inherits: `pos.load.mixin`

- `company_id` Many2one → `res.company` “Company” (store, related=order_id.company_id)
- `name` Char “Line No” (required)
- `notice` Char “Discount Notice”
- `product_id` Many2one → `product.product` “Product” (required)
- `attribute_value_ids` Many2many → `product.template.attribute.value` “Selected Attributes”
- `custom_attribute_value_ids` One2many → `product.attribute.custom.value` “Custom Values” (store)
- `price_unit` Float “Unit Price”
- `qty` Float “Quantity”
- `price_subtotal` Monetary “Tax Excl.” (required, readonly)
- `price_subtotal_incl` Monetary “Tax Incl.” (required, readonly)
- `price_extra` Float “Price extra”
- `price_type` Selection “Price Type”
- `margin` Monetary “Margin” (compute=_compute_margin)
- `margin_percent` Float “Margin (%)” (compute=_compute_margin)
- `total_cost` Float “Total cost” (readonly)
- `is_total_cost_computed` Boolean
- `discount` Float “Discount (%)”
- `order_id` Many2one → `pos.order` “Order Ref” (required, index)
- `tax_ids` Many2many → `account.tax` “Taxes” (readonly)
- `tax_ids_after_fiscal_position` Many2many → `account.tax` “Taxes to Apply” (compute=_get_tax_ids_after_fiscal_position)
- `pack_lot_ids` One2many → `pos.pack.operation.lot` “Lot/serial Number”
- `product_uom_id` Many2one → `uom.uom` “Product Unit” (related=product_id.uom_id)
- `currency_id` Many2one → `res.currency` (related=order_id.currency_id)
- `full_product_name` Char “Full Product Name”
- `customer_note` Char “Customer Note”
- `refund_orderline_ids` One2many → `pos.order.line`
- `refunded_orderline_id` Many2one → `pos.order.line`
- `refunded_qty` Float “Refunded Quantity” (compute=_compute_refund_qty)
- `uuid` Char “Uuid” (readonly)
- `note` Char “Product Note”
- `combo_parent_id` Many2one → `pos.order.line` “Combo Parent”
- `combo_line_ids` One2many → `pos.order.line` “Combo Lines”
- `combo_item_id` Many2one → `product.combo.item` “Combo Item”
- `is_edited` Boolean “Edited”
- `extra_tax_data` Json

Public methods: `create`, `get_existing_lots`, `isRefund`, `unlink`, `write`

Extension points: `_get_discount_amount`, `_get_discount_amount_for_report`, `_get_product_cost_with_moves`, `_get_stock_moves_to_consider`, `_get_tax_ids_after_fiscal_position`, `_prepare_base_line_for_taxes_computation`, `_prepare_procurement_values`, `_prepare_reference_vals`, `_prepare_refund_data`, `_prepare_tax_base_line_values`

## `pos.pack.operation.lot` (defines)

Specify product lot/serial number in pos order line

Inherits: `pos.load.mixin`

- `pos_order_line_id` Many2one → `pos.order.line`
- `order_id` Many2one → `pos.order` (related=pos_order_line_id.order_id)
- `lot_name` Char “Lot Name”
- `product_id` Many2one → `product.product` (related=pos_order_line_id.product_id)

## `account.cash.rounding` (extends)

Inherits: `pos.load.mixin`


Extension points: `_check_session_state`

## `pos.payment` (defines)

Point of Sale Payments

Inherits: `pos.load.mixin`

- `name` Char “Label” (readonly)
- `pos_order_id` Many2one → `pos.order` “Order” (required, index)
- `amount` Monetary “Amount” (required)
- `payment_method_id` Many2one → `pos.payment.method` “Payment Method” (required)
- `payment_date` Datetime “Date” (required, readonly)
- `currency_id` Many2one → `res.currency` “Currency” (related=pos_order_id.currency_id)
- `currency_rate` Float “Conversion Rate” (related=pos_order_id.currency_rate)
- `partner_id` Many2one → `res.partner` “Customer” (related=pos_order_id.partner_id)
- `session_id` Many2one → `pos.session` “Session” (store, index, related=pos_order_id.session_id)
- `user_id` Many2one → `res.users` “Employee” (related=session_id.user_id)
- `company_id` Many2one → `res.company` “Company” (store, related=pos_order_id.company_id)
- `card_type` Char “Type of card used”
- `card_brand` Char “Brand of card”
- `card_no` Char “Card Number(Last 4 Digit)”
- `cardholder_name` Char “Card Owner name”
- `payment_ref_no` Char “Payment reference number”
- `payment_method_authcode` Char “Payment APPR Code”
- `payment_method_issuer_bank` Char “Payment Issuer Bank”
- `payment_method_payment_mode` Char “Payment Mode”
- `transaction_id` Char “Payment Transaction ID”
- `payment_status` Char “Payment Status”
- `ticket` Char “Payment Receipt Info”
- `is_change` Boolean “Is this payment change?”
- `account_move_id` Many2one → `account.move`
- `uuid` Char “Uuid” (readonly)

Extension points: `_check_amount`, `_check_payment_method_id`, `_create_payment_moves`, `_get_receivable_lines_for_invoice_reconciliation`

## `pos.payment.method` (defines)

Point of Sale Payment Methods

Inherits: `pos.load.mixin`

- `name` Char “Method” (required)
- `sequence` Integer
- `outstanding_account_id` Many2one → `account.account` “Outstanding Account”
- `receivable_account_id` Many2one → `account.account` “Intermediary Account”
- `is_cash_count` Boolean “Cash” (store, compute=_compute_is_cash_count)
- `journal_id` Many2one → `account.journal` “Journal”
- `split_transactions` Boolean “Identify Customer”
- `open_session_ids` Many2many → `pos.session` “Pos Sessions” (compute=_compute_open_session_ids)
- `config_ids` Many2many → `pos.config` “Point of Sale”
- `company_id` Many2one → `res.company` “Company”
- `default_pos_receivable_account_name` Char “Default Receivable Account Name” (related=company_id.account_default_pos_receivable_account_id.display_name)
- `use_payment_terminal` Selection “Use a Payment Terminal”
- `hide_use_payment_terminal` Boolean (compute=_compute_hide_use_payment_terminal)
- `active` Boolean
- `type` Selection (compute=_compute_type)
- `image` Image “Image”
- `payment_method_type` Selection “Integration” (required)
- `default_qr` Char (compute=_compute_qr)
- `qr_code_method` Selection “QR Code Format”
- `hide_qr_code_method` Boolean (compute=_compute_hide_qr_code_method)

Public methods: `copy_data`, `create`, `get_provider_status`, `get_qr_code`, `write`

Extension points: `_check_cash_method_single_shop`, `_check_company_config`, `_check_payment_method`, `_get_payment_method_type`, `_get_payment_terminal_selection`

## `pos.preset` (defines)

Easily load a set of configuration options

Inherits: `pos.load.mixin`

- `name` Char “Label” (required)
- `pricelist_id` Many2one → `product.pricelist` “Pricelist”
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position”
- `identification` Selection “Identification” (required)
- `is_return` Boolean “Return mode”
- `color` Integer “Color”
- `image_512` Image “Image”
- `image_128` Image “Image 128” (store, related=image_512)
- `has_image` Boolean (compute=_compute_has_image)
- `count_linked_orders` Integer (compute=_compute_count_linked_orders)
- `count_linked_config` Integer (compute=_compute_count_linked_config)
- `use_timing` Boolean “Manage orders by time”
- `resource_calendar_id` Many2one → `resource.calendar`
- `attendance_ids` One2many “Attendances” (related=resource_calendar_id.attendance_ids)
- `slots_per_interval` Integer “Capacity”
- `interval_time` Integer “Interval time (in min)”

Public methods: `action_open_linked_config`, `action_open_linked_orders`, `get_available_slots`

Extension points: `_check_slots`

## `pos.printer` (defines)

Point of Sale Printer

Inherits: `pos.load.mixin`

- `name` Char “Printer Name” (required)
- `printer_type` Selection “Printer Type”
- `proxy_ip` Char “Proxy IP Address”
- `product_categories_ids` Many2many → `pos.category` “Printed Product Categories”
- `company_id` Many2one → `res.company` “Company” (required)
- `pos_config_ids` Many2many → `pos.config`
- `epson_printer_ip` Char “Epson Printer IP Address”

Public methods: `use_local_network_access`

## `pos.session` (defines)

Point of Sale Session

Inherits: `mail.thread`, `mail.activity.mixin`, `pos.bus.mixin`, `pos.load.mixin`

- `company_id` Many2one → `res.company` “Company” (readonly, related=config_id.company_id)
- `config_id` Many2one → `pos.config` “Point of Sale” (required, index)
- `name` Char “Session ID” (readonly)
- `user_id` Many2one → `res.users` “Opened By” (required, index)
- `currency_id` Many2one → `res.currency` “Currency” (related=config_id.currency_id)
- `start_at` Datetime “Opening Date” (readonly)
- `stop_at` Datetime “Closing Date” (readonly)
- `state` Selection “Status” (required, readonly, index)
- `opening_notes` Text “Opening Notes”
- `closing_notes` Text “Closing Notes”
- `cash_control` Boolean “Has Cash Control” (compute=_compute_cash_control)
- `cash_journal_id` Many2one → `account.journal` “Cash Journal” (store, compute=_compute_cash_journal)
- `cash_register_balance_end_real` Monetary “Ending Balance” (readonly)
- `cash_register_balance_start` Monetary “Starting Balance” (readonly)
- `cash_register_balance_end` Monetary “Theoretical Closing Balance” (readonly, compute=_compute_cash_balance)
- `cash_register_difference` Monetary “Before Closing Difference” (readonly, compute=_compute_cash_balance)
- `cash_real_transaction` Monetary “Transaction” (readonly)
- `order_ids` One2many → `pos.order` “Orders”
- `order_count` Integer (compute=_compute_order_count)
- `statement_line_ids` One2many → `account.bank.statement.line` “Cash Lines” (readonly)
- `failed_pickings` Boolean (compute=_compute_picking_count)
- `picking_count` Integer (compute=_compute_picking_count)
- `picking_ids` One2many → `stock.picking`
- `rescue` Boolean “Recovery Session” (readonly)
- `move_id` Many2one → `account.move` “Journal Entry” (index)
- `payment_method_ids` Many2many → `pos.payment.method` “Payment Methods” (related=config_id.payment_method_ids)
- `total_payments_amount` Float “Total Payments Amount” (compute=_compute_total_payments_amount)
- `is_in_company_currency` Boolean “Is Using Company Currency” (compute=_compute_is_in_company_currency)
- `update_stock_at_closing` Boolean “Stock should be updated at closing”
- `bank_payment_ids` One2many → `account.payment`

Public methods: `action_pos_session_close`, `action_pos_session_closing_control`, `action_pos_session_open`, `action_pos_session_validate`, `action_show_payments_list`, `action_stock_picking`, `action_view_order`, `close_session_from_ui`, `create`, `delete_cash_in_out`, `delete_opening_control_session`, `filter_local_data`, `find_product_by_barcode`, `get_cash_in_out_list`, `get_closing_control_data`, `get_pos_ui_product_pricelist_item_by_product`, `get_session_orders`, `get_total_discount`, `load_data`, `load_data_params`, `log_partner_message`, `open_frontend_cb`, `post_close_register_message`, `post_closing_cash_details`, `set_opening_control`, `show_cash_register`, `show_journal_items`, `try_cash_in_out`, `unlink`, `update_closing_control_state_session`, `write`

Extension points: `_check_if_no_draft_orders`, `_check_invoices_are_posted`, `_check_pos_config`, `_check_start_date`, `_create_account_move`, `_create_balancing_line`, `_create_bank_payment_moves`, `_create_cash_statement_lines_and_cash_move_lines`, `_create_combine_account_payment`, `_create_diff_account_move_for_split_payment_method`, `_create_invoice_receivable_lines`, `_create_non_reconciliable_move_lines`, `_create_pay_later_receivable_lines`, `_create_picking_at_end_of_session`, `_create_split_account_payment`, `_create_split_account_payments`, `_create_stock_valuation_lines`, `_get_attributes_by_ptal_id`, `_get_balancing_account`, `_get_captured_payments_domain`, `_get_cash_move_cashier_name`, `_get_closed_orders`, `_get_combine_receivable_vals`, `_get_combine_statement_line_vals`, `_get_diff_account_move_ref`, `_get_diff_vals`, `_get_invoice_receivable_vals`, `_get_invoice_total_list`, `_get_other_related_moves`, `_get_partners_domain`, `_get_receivable_account`, `_get_related_account_moves`, `_get_rounding_difference_vals`, `_get_sale_key`, `_get_sale_vals`, `_get_split_account_payment_vals`, `_get_split_receivable_vals`, `_get_split_statement_line_vals`, `_get_stock_expense_vals`, `_get_stock_valuation_vals`, `_get_tax_vals`, `_get_total_invoice`, `_post_cash_details_message`, `_post_statement_difference`, `_prepare_account_bank_statement_line_vals`, `_prepare_balancing_line_vals`, `_prepare_cash_diff_line_ids`, `_prepare_statement_line_amount_values`

## `stock.rule` (extends)


Extension points: `_get_scheduler_tasks_to_do`

## `product.attribute` (extends)

Inherits: `pos.load.mixin`


## `product.attribute.custom.value` (extends)

Inherits: `pos.load.mixin`

- `pos_order_line_id` Many2one → `pos.order.line` “PoS Order Line”

## `product.template.attribute.line` (extends)

Inherits: `pos.load.mixin`


## `product.template.attribute.value` (extends)

Inherits: `pos.load.mixin`


## `product.template.attribute.exclusion` (extends)

Inherits: `pos.load.mixin`


## `product.category` (extends)

Inherits: `pos.load.mixin`


## `product.combo` (extends)

Inherits: `pos.load.mixin`

- `qty_max` Integer “Maximum quantity”
- `qty_free` Integer “Free quantity”

Extension points: `_check_qty_free`, `_check_qty_max`, `_check_qty_max_greater_than_qty_free`

## `product.combo.item` (extends)

Inherits: `pos.load.mixin`


## `product.pricelist` (extends)

Inherits: `pos.load.mixin`


## `product.pricelist.item` (extends)

Inherits: `pos.load.mixin`


## `product.product` (extends)

Inherits: `pos.load.mixin`


Public methods: `action_archive`

## `product.removal` (extends)

Inherits: `pos.load.mixin`


## `product.tag` (extends)

Inherits: `pos.load.mixin`

- `pos_description` Html “Description”
- `has_image` Boolean (compute=_compute_has_image)

Public methods: `write`

## `product.template` (extends)

Inherits: `pos.load.mixin`

- `available_in_pos` Boolean “Available in POS”
- `to_weight` Boolean “To Weigh With Scale”
- `pos_categ_ids` Many2many → `pos.category` “Point of Sale Category”
- `public_description` Html “Product Description”
- `pos_optional_product_ids` Many2many → `product.template` “POS Optional Products”
- `color` Integer “Color Index” (store, compute=_compute_color)
- `pos_sequence` Integer “POS Sequence”

Public methods: `action_archive`, `create_product_variant_from_pos`, `get_product_info_pos`, `load_product_from_pos`, `write`

Extension points: `_check_combo_inclusions`, `_check_is_special_product`

## `product.uom` (extends)

Inherits: `pos.load.mixin`


## `report.point_of_sale.report_saledetails` (defines)

Point of Sale Details


Public methods: `get_sale_details`

Extension points: `_get_date_start_and_date_stop`, `_get_domain`, `_get_product_total_amount`, `_get_products_and_taxes_dict`, `_get_report_values`, `_get_taxes_info`, `_get_total_and_qty_per_category`, `_prepare_get_sale_details_args_kwargs`

## `res.company` (extends)

Inherits: `pos.load.mixin`

- `point_of_sale_update_stock_quantities` Selection “Update quantities in stock”
- `point_of_sale_use_ticket_qr_code` Boolean “Self-service invoicing”
- `point_of_sale_ticket_unique_code` Boolean “Generate a code on ticket”
- `point_of_sale_ticket_portal_url_display_mode` Selection “Print” (required)

Public methods: `validate_lock_dates`

## `res.config.settings` (extends)

- `pos_config_id` Many2one → `pos.config` “Point of Sale”
- `sale_tax_id` Many2one → `account.tax` “Default Sale Tax” (related=company_id.account_sale_tax_id)
- `module_pos_adyen` Boolean “Adyen Payment Terminal”
- `module_pos_stripe` Boolean “Stripe Payment Terminal”
- `module_pos_viva_com` Boolean “Viva.com Payment Terminal”
- `module_pos_razorpay` Boolean “Razorpay Payment Terminal”
- `module_pos_mercado_pago` Boolean “Mercado Pago Payment Terminal”
- `module_pos_pine_labs` Boolean “Pine Labs Payment Terminal”
- `module_pos_qfpay` Boolean “QFPay Payment Terminal”
- `module_pos_pricer` Boolean “Pricer electronic price tags”
- `update_stock_quantities` Selection (related=company_id.point_of_sale_update_stock_quantities)
- `account_default_pos_receivable_account_id` Many2one “Default Account Receivable (PoS)” (related=company_id.account_default_pos_receivable_account_id)
- `barcode_nomenclature_id` Many2one → `barcode.nomenclature` (related=company_id.nomenclature_id)
- `is_kiosk_mode` Boolean “Is Kiosk Mode”
- `pos_customer_display_bg_img` Image (related=pos_config_id.customer_display_bg_img)
- `pos_customer_display_bg_img_name` Char (related=pos_config_id.customer_display_bg_img_name)
- `pos_use_presets` Boolean (related=pos_config_id.use_presets)
- `pos_default_preset_id` Many2one → `pos.preset` (related=pos_config_id.default_preset_id)
- `pos_available_preset_ids` Many2many → `pos.preset` (related=pos_config_id.available_preset_ids)
- `pos_module_pos_discount` Boolean (related=pos_config_id.module_pos_discount)
- `pos_module_pos_hr` Boolean (related=pos_config_id.module_pos_hr)
- `pos_module_pos_restaurant` Boolean (related=pos_config_id.module_pos_restaurant)
- `pos_module_pos_appointment` Boolean (related=pos_config_id.module_pos_appointment)
- `pos_module_pos_avatax` Boolean (related=pos_config_id.module_pos_avatax)
- `pos_is_order_printer` Boolean (store, compute=_compute_pos_printer)
- `pos_printer_ids` Many2many (related=pos_config_id.printer_ids)
- `pos_allowed_pricelist_ids` Many2many → `product.pricelist` (compute=_compute_pos_allowed_pricelist_ids)
- `pos_amount_authorized_diff` Float (related=pos_config_id.amount_authorized_diff)
- `pos_available_pricelist_ids` Many2many → `product.pricelist` “Available Pricelists” (store, compute=_compute_pos_pricelist_id)
- `pos_cash_control` Boolean (related=pos_config_id.cash_control)
- `pos_cash_rounding` Boolean “Cash Rounding (PoS)” (related=pos_config_id.cash_rounding)
- `pos_company_has_template` Boolean (related=pos_config_id.company_has_template)
- `pos_default_bill_ids` Many2many (related=pos_config_id.default_bill_ids)
- `pos_default_fiscal_position_id` Many2one → `account.fiscal.position` “Default Fiscal Position” (store, compute=_compute_pos_fiscal_positions)
- `pos_fiscal_position_ids` Many2many → `account.fiscal.position` “Fiscal Positions” (store, compute=_compute_pos_fiscal_positions)
- `pos_has_active_session` Boolean (related=pos_config_id.has_active_session)
- `pos_iface_available_categ_ids` Many2many → `pos.category` “Available PoS Product Categories” (store, compute=_compute_pos_iface_available_categ_ids)
- `pos_iface_big_scrollbars` Boolean (related=pos_config_id.iface_big_scrollbars)
- `pos_iface_group_by_categ` Boolean (related=pos_config_id.iface_group_by_categ)
- `pos_iface_cashdrawer` Boolean “Cashdrawer” (store, compute=_compute_pos_iface_cashdrawer)
- `pos_iface_electronic_scale` Boolean “Electronic Scale” (store, compute=_compute_pos_iface_electronic_scale)
- `pos_iface_print_auto` Boolean (related=pos_config_id.iface_print_auto)
- `pos_iface_print_skip_screen` Boolean (related=pos_config_id.iface_print_skip_screen)
- `pos_iface_print_via_proxy` Boolean “Print via Proxy” (store, compute=_compute_pos_iface_print_via_proxy)
- `pos_iface_scan_via_proxy` Boolean “Scan via Proxy” (store, compute=_compute_pos_iface_scan_via_proxy)
- `pos_iface_tax_included` Selection (related=pos_config_id.iface_tax_included)
- `pos_iface_tipproduct` Boolean (related=pos_config_id.iface_tipproduct)
- `pos_invoice_journal_id` Many2one (related=pos_config_id.invoice_journal_id)
- `pos_is_header_or_footer` Boolean (related=pos_config_id.is_header_or_footer)
- `pos_is_margins_costs_accessible_to_every_user` Boolean (related=pos_config_id.is_margins_costs_accessible_to_every_user)
- `pos_is_posbox` Boolean (related=pos_config_id.is_posbox)
- `pos_journal_id` Many2one (related=pos_config_id.journal_id)
- `pos_limit_categories` Boolean (related=pos_config_id.limit_categories)
- `pos_manual_discount` Boolean (related=pos_config_id.manual_discount)
- `pos_only_round_cash_method` Boolean (related=pos_config_id.only_round_cash_method)
- `pos_other_devices` Boolean (related=pos_config_id.other_devices)
- `pos_payment_method_ids` Many2many (related=pos_config_id.payment_method_ids)
- `pos_picking_policy` Selection (related=pos_config_id.picking_policy)
- `pos_picking_type_id` Many2one (related=pos_config_id.picking_type_id)
- `pos_pricelist_id` Many2one → `product.pricelist` “Default Pricelist” (store, compute=_compute_pos_pricelist_id)
- `pos_proxy_ip` Char “IP Address” (related=pos_config_id.proxy_ip)
- `pos_receipt_footer` Text “Receipt Footer” (store, compute=_compute_pos_receipt_header_footer)
- `pos_receipt_header` Text “Receipt Header” (store, compute=_compute_pos_receipt_header_footer)
- `pos_restrict_price_control` Boolean (related=pos_config_id.restrict_price_control)
- `pos_rounding_method` Many2one (related=pos_config_id.rounding_method)
- `pos_route_id` Many2one (related=pos_config_id.route_id)
- `pos_selectable_categ_ids` Many2many → `pos.category` (compute=_compute_pos_selectable_categ_ids)
- `pos_set_maximum_difference` Boolean (related=pos_config_id.set_maximum_difference)
- `pos_ship_later` Boolean (related=pos_config_id.ship_later)
- `pos_tax_regime_selection` Boolean (related=pos_config_id.tax_regime_selection)
- `pos_tip_product_id` Many2one → `product.product` “Tip Product” (store, compute=_compute_pos_tip_product_id)
- `pos_use_pricelist` Boolean (related=pos_config_id.use_pricelist)
- `pos_warehouse_id` Many2one “Warehouse (PoS)” (related=pos_config_id.warehouse_id)
- `point_of_sale_use_ticket_qr_code` Boolean (related=company_id.point_of_sale_use_ticket_qr_code)
- `pos_auto_validate_terminal_payment` Boolean “Automatically validates orders paid with a payment terminal.” (related=pos_config_id.auto_validate_terminal_payment)
- `pos_trusted_config_ids` Many2many (related=pos_config_id.trusted_config_ids)
- `point_of_sale_ticket_unique_code` Boolean (related=company_id.point_of_sale_ticket_unique_code)
- `pos_show_product_images` Boolean (related=pos_config_id.show_product_images)
- `pos_show_category_images` Boolean (related=pos_config_id.show_category_images)
- `point_of_sale_ticket_portal_url_display_mode` Selection (required, related=company_id.point_of_sale_ticket_portal_url_display_mode)
- `pos_note_ids` Many2many (related=pos_config_id.note_ids)
- `pos_module_pos_sms` Boolean (related=pos_config_id.module_pos_sms)
- `pos_is_closing_entry_by_product` Boolean (related=pos_config_id.is_closing_entry_by_product)
- `pos_order_edit_tracking` Boolean (related=pos_config_id.order_edit_tracking)
- `pos_basic_receipt` Boolean (related=pos_config_id.basic_receipt)
- `pos_fallback_nomenclature_id` Many2one (related=pos_config_id.fallback_nomenclature_id)
- `group_pos_preset` Boolean “Presets”
- `pos_epson_printer_ip` Char (related=pos_config_id.epson_printer_ip)
- `pos_use_fast_payment` Boolean (related=pos_config_id.use_fast_payment)
- `pos_fast_payment_method_ids` Many2many (related=pos_config_id.fast_payment_method_ids)

Public methods: `action_pos_config_create_new`, `action_pos_printer_dialog`, `create`, `open_payment_method_form`, `pos_close_ui`, `pos_open_ui`, `set_values`

## `res.country` (extends)

Inherits: `pos.load.mixin`


## `res.country.state` (extends)

Inherits: `pos.load.mixin`


## `res.currency` (extends)

Inherits: `pos.load.mixin`


## `res.lang` (extends)

Inherits: `pos.load.mixin`


## `res.partner` (extends)

Inherits: `pos.load.mixin`

- `pos_order_count` Integer (compute=_compute_pos_order)
- `pos_order_ids` One2many → `pos.order` (readonly)
- `pos_contact_address` Char “PoS Address” (compute=_compute_pos_contact_address)
- `invoice_emails` Char (readonly, compute=_compute_invoice_emails)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Automatic Fiscal Position” (compute=_compute_fiscal_position_id)

Public methods: `action_view_pos_order`, `get_new_partner`, `open_commercial_entity`

## `res.users` (extends)

Inherits: `pos.load.mixin`


## `resource.calendar.attendance` (extends)

Inherits: `pos.load.mixin`


## `stock.picking` (extends)

- `pos_session_id` Many2one → `pos.session` (index)
- `pos_order_id` Many2one → `pos.order` (index)

Extension points: `_create_move_from_pos_order_lines`, `_create_picking_from_pos_order_lines`, `_prepare_picking_vals`, `_prepare_stock_move_vals`

## `stock.picking.type` (extends)

Inherits: `pos.load.mixin`

- `has_stock_reports_to_print` Boolean (compute=_compute_has_stock_reports_to_print)

Extension points: `_check_active`

## `stock.move` (extends)


Extension points: `_create_production_lots_for_pos_order`, `_get_lot_line_qty`, `_get_new_picking_values`, `_prepare_lines_data_dict`

## `stock.reference` (extends)

- `pos_order_ids` Many2many → `pos.order` “PoS Orders”

## `stock.warehouse` (extends)

- `pos_type_id` Many2one → `stock.picking.type` “Point of Sale Operation Type”

Extension points: `_create_missing_pos_picking_types`, `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_sequence_values`

## `uom.uom` (extends)

Inherits: `pos.load.mixin`

- `is_pos_groupable` Boolean “Group Products in POS”

## `report.point_of_sale.report_invoice` (defines)

Point of Sale Invoice Report


Extension points: `_get_report_values`

## `report.pos.order` (defines)

Point of Sale Orders Report

- `date` Datetime “Order Date” (readonly)
- `order_id` Many2one → `pos.order` “Order” (readonly)
- `partner_id` Many2one → `res.partner` “Customer” (readonly)
- `product_id` Many2one → `product.product` “Product” (readonly)
- `product_tmpl_id` Many2one → `product.template` “Product Template” (readonly)
- `state` Selection “Status” (readonly)
- `user_id` Many2one → `res.users` “User” (readonly)
- `price_total` Float “Total Price” (readonly)
- `price_sub_total` Float “Subtotal w/o discount” (readonly)
- `price_subtotal_excl` Float “Subtotal w/o Tax” (readonly)
- `total_discount` Float “Total Discount” (readonly)
- `average_price` Float “Average Price” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `nbr_lines` Integer “Sale Line Count” (readonly)
- `product_qty` Integer “Product Quantity” (readonly)
- `journal_id` Many2one → `account.journal` “Journal” (readonly)
- `delay_validation` Integer “Delay Validation” (readonly)
- `product_categ_id` Many2one → `product.category` “Product Category” (readonly)
- `pos_categ_id` Many2one → `pos.category` “Point of Sale Category” (readonly)
- `invoiced` Boolean (readonly)
- `config_id` Many2one → `pos.config` “Point of Sale” (readonly)
- `pricelist_id` Many2one → `product.pricelist` “Pricelist” (readonly)
- `session_id` Many2one → `pos.session` “Session” (readonly)
- `margin` Float “Margin” (readonly)
- `payment_method_id` Many2one → `pos.payment.method` “Payment Method” (readonly)

Public methods: `init`

## `pos.close.session.wizard` (defines)

Close Session Wizard

- `amount_to_balance` Float “Amount to balance”
- `account_id` Many2one → `account.account`
- `account_readonly` Boolean “Destination account is readonly”
- `message` Text “Information message”

Public methods: `close_session`

## `pos.confirmation.wizard` (defines)

Confirmation Wizard

- `message` Text (readonly)

Public methods: `action_confirm`, `get_selected_orders`

## `pos.daily.sales.reports.wizard` (defines)

Point of Sale Daily Report

- `pos_session_id` Many2one → `pos.session` (required)

Public methods: `generate_report`

Extension points: `_get_report_data`

## `pos.details.wizard` (defines)

Point of Sale Details Report

- `start_date` Datetime (required)
- `end_date` Datetime (required)
- `pos_config_ids` Many2many → `pos.config`

Public methods: `generate_report`

## `pos.make.invoice` (defines)

Multiple order invoice creation

- `consolidated_billing` Boolean “Consolidated Billing”
- `count` Integer “Order Count” (compute=_compute_order_count)

Public methods: `action_create_invoices`

## `pos.make.payment` (defines)

Point of Sale Make Payment Wizard

- `config_id` Many2one → `pos.config` “Point of Sale Configuration” (required)
- `amount` Float (required)
- `payment_method_id` Many2one → `pos.payment.method` “Payment Method” (required)
- `payment_name` Char “Payment Reference”
- `payment_date` Datetime “Payment Date” (required)

Public methods: `check`, `launch_payment`

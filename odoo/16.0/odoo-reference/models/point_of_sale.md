# point_of_sale — Point of Sale

Depends on: stock_account, barcodes, web_editor, digest.

## `account.bank.statement.line` (extends)

- `pos_session_id` Many2one → `pos.session` “Session”

## `account.cash.rounding` (extends)


## `account.journal` (extends)

- `pos_payment_method_ids` One2many → `pos.payment.method` “Point of Sale Payment Methods”

Public methods: `action_archive`

Extension points: `_check_no_active_payments`, `_check_type`, `_get_journal_inbound_outstanding_payment_accounts`

## `account.move` (extends)

- `pos_order_ids` One2many → `pos.order`
- `pos_payment_ids` One2many → `pos.payment`

Extension points: `_get_invoiced_lot_values`

## `account.move.line` (extends)


## `account.payment` (extends)

- `pos_payment_method_id` Many2one → `pos.payment.method`
- `force_outstanding_account_id` Many2one → `account.account`
- `pos_session_id` Many2one → `pos.session`

Extension points: `_get_valid_liquidity_accounts`

## `account.tax` (extends)


Public methods: `write`

## `barcode.rule` (extends)

- `type` Selection

## `account.chart.template` (extends)


## `digest.digest` (extends)

- `kpi_pos_total` Boolean “POS Sales”
- `kpi_pos_total_value` Monetary (compute=_compute_kpi_pos_total_value)

## `pos.bill` (defines)

Coins/Bills

- `name` Char “Name”
- `value` Float “Coin/Bill Value” (required)
- `pos_config_ids` Many2many → `pos.config` “Point of Sales”

Public methods: `name_create`

## `pos.category` (defines)

Point of Sale Category

- `name` Char “Category Name” (required)
- `parent_id` Many2one → `pos.category` “Parent Category” (index)
- `child_id` One2many → `pos.category` “Children Categories”
- `sequence` Integer
- `image_128` Image “Image”
- `has_image` Boolean (compute=_compute_has_image)

Public methods: `name_get`

Extension points: `_check_category_recursion`

## `pos.config` (defines)

Point of Sale Configuration

- `name` Char “Point of Sale” (required)
- `is_installed_account_accountant` Boolean “Is the Full Accounting Installed” (compute=_compute_is_installed_account_accountant)
- `picking_type_id` Many2one → `stock.picking.type` “Operation Type” (required)
- `journal_id` Many2one → `account.journal` “Point of Sale Journal”
- `invoice_journal_id` Many2one → `account.journal` “Invoice Journal”
- `currency_id` Many2one → `res.currency` “Currency” (compute=_compute_currency)
- `iface_cashdrawer` Boolean “Cashdrawer”
- `iface_electronic_scale` Boolean “Electronic Scale”
- `iface_customer_facing_display` Boolean (compute=_compute_customer_facing_display)
- `iface_customer_facing_display_via_proxy` Boolean “Customer Facing Display”
- `iface_customer_facing_display_local` Boolean “Local Customer Facing Display”
- `iface_print_via_proxy` Boolean “Print via Proxy”
- `iface_scan_via_proxy` Boolean “Scan via Proxy”
- `iface_big_scrollbars` Boolean “Large Scrollbars”
- `iface_print_auto` Boolean “Automatic Receipt Printing”
- `iface_print_skip_screen` Boolean “Skip Preview Screen”
- `iface_tax_included` Selection “Tax Display” (required)
- `iface_start_categ_id` Many2one → `pos.category` “Initial Category”
- `iface_available_categ_ids` Many2many → `pos.category` “Available PoS Product Categories”
- `restrict_price_control` Boolean “Restrict Price Modifications to Managers”
- `is_margins_costs_accessible_to_every_user` Boolean “Margins & Costs”
- `cash_control` Boolean “Advanced Cash Control” (compute=_compute_cash_control)
- `set_maximum_difference` Boolean “Set Maximum Difference”
- `receipt_header` Text “Receipt Header”
- `receipt_footer` Text “Receipt Footer”
- `proxy_ip` Char “IP Address”
- `active` Boolean
- `uuid` Char (readonly)
- `sequence_id` Many2one → `ir.sequence` “Order IDs Sequence” (readonly)
- `sequence_line_id` Many2one → `ir.sequence` “Order Line IDs Sequence” (readonly)
- `session_ids` One2many → `pos.session` “Sessions”
- `current_session_id` Many2one → `pos.session` “Current Session” (compute=_compute_current_session)
- `current_session_state` Char (compute=_compute_current_session)
- `number_of_opened_session` Integer “Number of Opened Session” (compute=_compute_current_session)
- `last_session_closing_cash` Float (compute=_compute_last_session)
- `last_session_closing_date` Date (compute=_compute_last_session)
- `pos_session_username` Char (compute=_compute_current_session_user)
- `pos_session_state` Char (compute=_compute_current_session_user)
- `pos_session_duration` Char (compute=_compute_current_session_user)
- `pricelist_id` Many2one → `product.pricelist` “Default Pricelist” (required)
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
- `tax_regime_selection` Boolean “Tax Regime Selection value”
- `start_category` Boolean “Start Category”
- `limit_categories` Boolean “Restrict Categories”
- `module_pos_restaurant` Boolean “Is a Bar/Restaurant”
- `module_pos_discount` Boolean “Global Discounts”
- `module_pos_mercury` Boolean “Integrated Card Payments”
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
- `warehouse_id` Many2one → `stock.warehouse`
- `route_id` Many2one → `stock.route` “Spefic route for products delivered later.”
- `picking_policy` Selection “Shipping Policy” (required)
- `limited_products_loading` Boolean “Limited Product Loading”
- `limited_products_amount` Integer
- `product_load_background` Boolean
- `limited_partners_loading` Boolean “Limited Partners Loading”
- `limited_partners_amount` Integer
- `partner_load_background` Boolean

Public methods: `action_pos_config_modal_edit`, `assign_payment_journals`, `create`, `execute`, `generate_pos_journal`, `get_limited_partners_loading`, `get_limited_products_loading`, `name_get`, `open_existing_session_cb`, `open_opened_session_list`, `open_ui`, `post_install_pos_localisation`, `setup_defaults`, `setup_invoice_journal`, `unlink`, `write`

Extension points: `_action_to_open_ui`, `_check_before_creating_new_session`, `_check_companies`, `_check_company_invoice_journal`, `_check_company_journal`, `_check_company_payment`, `_check_currencies`, `_check_groups_implied`, `_check_header_footer`, `_check_limited_partners`, `_check_limited_products`, `_check_modules_to_install`, `_check_payment_method_ids`, `_check_pos_manager_access`, `_check_pricelists`, `_check_profit_loss_cash_journal`, `_check_rounding_method_strategy`, `_check_start_categ`, `_get_forbidden_change_fields`, `_get_group_pos_manager`, `_get_group_pos_user`

## `pos.order` (defines)

Point of Sale Orders

Inherits: `portal.mixin`

- `name` Char “Order Ref” (required, readonly)
- `date_order` Datetime “Date” (readonly, index)
- `user_id` Many2one → `res.users` “Responsible”
- `amount_tax` Float “Taxes” (required, readonly)
- `amount_total` Float “Total” (required, readonly)
- `amount_paid` Float “Paid” (required, readonly)
- `amount_return` Float “Returned” (required, readonly)
- `margin` Monetary “Margin” (compute=_compute_margin)
- `margin_percent` Float “Margin (%)” (compute=_compute_margin)
- `is_total_cost_computed` Boolean (compute=_compute_is_total_cost_computed)
- `lines` One2many → `pos.order.line` “Order Lines” (readonly)
- `company_id` Many2one → `res.company` “Company” (required, readonly, index)
- `pricelist_id` Many2one → `product.pricelist` “Pricelist” (required, readonly)
- `partner_id` Many2one → `res.partner` “Customer”
- `sequence_number` Integer “Sequence Number”
- `session_id` Many2one → `pos.session` “Session” (required, readonly, index)
- `config_id` Many2one → `pos.config` “Point of Sale” (related=session_id.config_id)
- `currency_id` Many2one → `res.currency` “Currency” (related=config_id.currency_id)
- `currency_rate` Float “Currency Rate” (readonly, store, compute=_compute_currency_rate)
- `state` Selection (readonly, index)
- `account_move` Many2one → `account.move` “Invoice” (readonly)
- `picking_ids` One2many → `stock.picking`
- `picking_count` Integer (compute=_compute_picking_count)
- `failed_pickings` Boolean (compute=_compute_picking_count)
- `picking_type_id` Many2one → `stock.picking.type` “Operation Type” (related=session_id.config_id.picking_type_id)
- `procurement_group_id` Many2one → `procurement.group`
- `note` Text “Internal Notes”
- `nb_print` Integer “Number of Print” (readonly)
- `pos_reference` Char “Receipt Number” (readonly, index)
- `sale_journal` Many2one → `account.journal` “Sales Journal” (readonly, store, related=session_id.config_id.journal_id)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position” (readonly)
- `payment_ids` One2many → `pos.payment` “Payments” (readonly)
- `session_move_id` Many2one → `account.move` “Session Journal Entry” (readonly, related=session_id.move_id)
- `to_invoice` Boolean “To invoice”
- `to_ship` Boolean “To ship”
- `is_invoiced` Boolean “Is Invoiced” (compute=_compute_is_invoiced)
- `is_tipped` Boolean “Is this already tipped?” (readonly)
- `tip_amount` Float “Tip Amount” (readonly)
- `refund_orders_count` Integer “Number of Refund Orders” (compute=_compute_refund_related_fields)
- `is_refunded` Boolean (compute=_compute_refund_related_fields)
- `refunded_order_ids` Many2many → `pos.order` (compute=_compute_refund_related_fields)
- `has_refundable_lines` Boolean “Has Refundable Lines” (compute=_compute_has_refundable_lines)
- `refunded_orders_count` Integer (compute=_compute_refund_related_fields)

Public methods: `action_pos_order_cancel`, `action_pos_order_invoice`, `action_pos_order_paid`, `action_receipt_to_customer`, `action_stock_picking`, `action_view_invoice`, `action_view_refund_orders`, `action_view_refunded_orders`, `add_payment`, `create`, `create_from_ui`, `export_for_ui`, `get_table_draft_orders`, `refund`, `search_paid_order_ids`, `write`

Extension points: `_create_invoice`, `_create_misc_reversal_move`, `_create_order_picking`, `_get_fields_for_order_line`, `_get_partner_bank_id`, `_get_pos_anglo_saxon_price_unit`, `_get_rounded_amount`, `_get_valid_session`, `_prepare_aml_values_list_per_nature`, `_prepare_invoice_line`, `_prepare_invoice_lines`, `_prepare_invoice_vals`, `_prepare_mail_values`, `_prepare_order_line`, `_prepare_refund_values`

## `pos.order.line` (defines)

Point of Sale Order Lines

- `company_id` Many2one → `res.company` “Company” (store, related=order_id.company_id)
- `name` Char “Line No” (required)
- `notice` Char “Discount Notice”
- `product_id` Many2one → `product.product` “Product” (required)
- `price_unit` Float “Unit Price”
- `qty` Float “Quantity”
- `price_subtotal` Float “Subtotal w/o Tax” (required, readonly)
- `price_subtotal_incl` Float “Subtotal” (required, readonly)
- `price_extra` Float “Price extra”
- `margin` Monetary “Margin” (compute=_compute_margin)
- `margin_percent` Float “Margin (%)” (compute=_compute_margin)
- `total_cost` Float “Total cost” (readonly)
- `is_total_cost_computed` Boolean
- `discount` Float “Discount (%)”
- `order_id` Many2one → `pos.order` “Order Ref” (required, index)
- `tax_ids` Many2many → `account.tax` “Taxes” (readonly)
- `tax_ids_after_fiscal_position` Many2many → `account.tax` “Taxes to Apply” (compute=_get_tax_ids_after_fiscal_position)
- `pack_lot_ids` One2many → `pos.pack.operation.lot` “Lot/serial Number”
- `product_uom_id` Many2one → `uom.uom` “Product UoM” (related=product_id.uom_id)
- `currency_id` Many2one → `res.currency` (related=order_id.currency_id)
- `full_product_name` Char “Full Product Name”
- `customer_note` Char “Customer Note”
- `refund_orderline_ids` One2many → `pos.order.line`
- `refunded_orderline_id` Many2one → `pos.order.line`
- `refunded_qty` Float “Refunded Quantity” (compute=_compute_refund_qty)

Public methods: `create`, `export_for_ui`, `write`

Extension points: `_get_procurement_group`, `_get_stock_moves_to_consider`, `_get_tax_ids_after_fiscal_position`, `_prepare_procurement_group_vals`, `_prepare_procurement_values`, `_prepare_refund_data`

## `pos.pack.operation.lot` (defines)

Specify product lot/serial number in pos order line

- `pos_order_line_id` Many2one → `pos.order.line`
- `order_id` Many2one → `pos.order` (related=pos_order_line_id.order_id)
- `lot_name` Char “Lot Name”
- `product_id` Many2one → `product.product` (related=pos_order_line_id.product_id)

Public methods: `export_for_ui`

## `report.point_of_sale.report_saledetails` (defines)

Point of Sale Details


Public methods: `get_sale_details`

Extension points: `_get_report_values`

## `account.cash.rounding` (extends)


Extension points: `_check_session_state`

## `pos.payment` (defines)

Point of Sale Payments

- `name` Char “Label” (readonly)
- `pos_order_id` Many2one → `pos.order` “Order” (required, index)
- `amount` Monetary “Amount” (required, readonly)
- `payment_method_id` Many2one → `pos.payment.method` “Payment Method” (required)
- `payment_date` Datetime “Date” (required, readonly)
- `currency_id` Many2one → `res.currency` “Currency” (related=pos_order_id.currency_id)
- `currency_rate` Float “Conversion Rate” (related=pos_order_id.currency_rate)
- `partner_id` Many2one → `res.partner` “Customer” (related=pos_order_id.partner_id)
- `session_id` Many2one → `pos.session` “Session” (store, index, related=pos_order_id.session_id)
- `company_id` Many2one → `res.company` “Company” (store, related=pos_order_id.company_id)
- `card_type` Char “Type of card used”
- `cardholder_name` Char “Cardholder Name”
- `transaction_id` Char “Payment Transaction ID”
- `payment_status` Char “Payment Status”
- `ticket` Char “Payment Receipt Info”
- `is_change` Boolean “Is this payment change?”
- `account_move_id` Many2one → `account.move`

Public methods: `export_for_ui`, `name_get`

Extension points: `_check_payment_method_id`, `_create_payment_move_entry`, `_create_payment_move_with_change`, `_create_payment_moves`, `_prepare_credit_line_payment`, `_prepare_debit_line_payment`

## `pos.payment.method` (defines)

Point of Sale Payment Methods

- `name` Char “Method” (required)
- `outstanding_account_id` Many2one → `account.account` “Outstanding Account”
- `receivable_account_id` Many2one → `account.account` “Intermediary Account”
- `is_cash_count` Boolean “Cash” (store, compute=_compute_is_cash_count)
- `journal_id` Many2one → `account.journal` “Journal”
- `split_transactions` Boolean “Identify Customer”
- `open_session_ids` Many2many → `pos.session` “Pos Sessions” (compute=_compute_open_session_ids)
- `config_ids` Many2many → `pos.config` “Point of Sale Configurations”
- `company_id` Many2one → `res.company` “Company”
- `use_payment_terminal` Selection “Use a Payment Terminal”
- `hide_use_payment_terminal` Boolean (compute=_compute_hide_use_payment_terminal)
- `active` Boolean
- `type` Selection (compute=_compute_type)

Public methods: `copy`, `write`

Extension points: `_get_payment_terminal_selection`

## `pos.session` (defines)

Point of Sale Session

Inherits: `mail.thread`, `mail.activity.mixin`

- `company_id` Many2one → `res.company` “Company” (readonly, related=config_id.company_id)
- `config_id` Many2one → `pos.config` “Point of Sale” (required, index)
- `name` Char “Session ID” (required, readonly)
- `user_id` Many2one → `res.users` “Opened By” (required, readonly, index)
- `currency_id` Many2one → `res.currency` “Currency” (related=config_id.currency_id)
- `start_at` Datetime “Opening Date” (readonly)
- `stop_at` Datetime “Closing Date” (readonly)
- `state` Selection “Status” (required, readonly, index)
- `sequence_number` Integer “Order Sequence Number”
- `login_number` Integer “Login Sequence Number”
- `opening_notes` Text “Opening Notes”
- `cash_control` Boolean “Has Cash Control” (compute=_compute_cash_all)
- `cash_journal_id` Many2one → `account.journal` “Cash Journal” (store, compute=_compute_cash_all)
- `cash_register_balance_end_real` Monetary “Ending Balance” (readonly)
- `cash_register_balance_start` Monetary “Starting Balance” (readonly)
- `cash_register_total_entry_encoding` Monetary “Total Cash Transaction” (readonly, compute=_compute_cash_balance)
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

Public methods: `action_pos_session_close`, `action_pos_session_closing_control`, `action_pos_session_open`, `action_pos_session_validate`, `action_show_payments_list`, `action_stock_picking`, `action_view_order`, `close_session_from_ui`, `create`, `find_product_by_barcode`, `get_closing_control_data`, `get_onboarding_data`, `get_pos_ui_product_pricelist_item_by_product`, `get_pos_ui_product_product_by_params`, `get_pos_ui_res_partner_by_params`, `load_pos_data`, `login`, `open_frontend_cb`, `post_closing_cash_details`, `set_cashbox_pos`, `show_cash_register`, `show_journal_items`, `try_cash_in_out`, `unlink`, `update_closing_control_state_session`

Extension points: `_check_if_no_draft_orders`, `_check_invoices_are_posted`, `_check_pos_config`, `_check_start_date`, `_create_account_move`, `_create_balancing_line`, `_create_bank_payment_moves`, `_create_cash_statement_lines_and_cash_move_lines`, `_create_combine_account_payment`, `_create_diff_account_move_for_split_payment_method`, `_create_invoice_receivable_lines`, `_create_non_reconciliable_move_lines`, `_create_pay_later_receivable_lines`, `_create_picking_at_end_of_session`, `_create_split_account_payment`, `_create_stock_output_lines`, `_get_attributes_by_ptal_id`, `_get_balancing_account`, `_get_captured_order_attachment`, `_get_combine_receivable_vals`, `_get_combine_statement_line_vals`, `_get_diff_account_move_ref`, `_get_diff_vals`, `_get_invoice_receivable_vals`, `_get_other_related_moves`, `_get_partners_domain`, `_get_pos_fallback_nomenclature`, `_get_pos_ui_account_cash_rounding`, `_get_pos_ui_account_fiscal_position`, `_get_pos_ui_account_fiscal_position_tax`, `_get_pos_ui_account_tax`, `_get_pos_ui_decimal_precision`, `_get_pos_ui_pos_bill`, `_get_pos_ui_pos_category`, `_get_pos_ui_pos_config`, `_get_pos_ui_pos_payment_method`, `_get_pos_ui_pos_session`, `_get_pos_ui_product_category`, `_get_pos_ui_product_packaging`, `_get_pos_ui_product_pricelist`, `_get_pos_ui_product_product`, `_get_pos_ui_res_company`, `_get_pos_ui_res_country`, `_get_pos_ui_res_country_state`, `_get_pos_ui_res_currency`, `_get_pos_ui_res_lang`, `_get_pos_ui_res_partner`, `_get_pos_ui_res_users`, `_get_pos_ui_stock_picking_type`, `_get_pos_ui_uom_uom`, `_get_receivable_account`, `_get_related_account_moves`, `_get_rounding_difference_vals`, `_get_sale_vals`, `_get_split_receivable_vals`, `_get_split_statement_line_vals`, `_get_stock_expense_vals`, `_get_stock_output_vals`, `_get_tax_vals`, `_get_unprocessed_pos_order_scheduled_activity`, `_post_cash_details_message`, `_post_statement_difference`, `_prepare_balancing_line_vals`, `_prepare_line`

## `procurement.group` (extends)


## `product.template` (extends)

- `available_in_pos` Boolean “Available in POS”
- `to_weight` Boolean “To Weigh With Scale”
- `pos_categ_id` Many2one → `pos.category` “Point of Sale Category”

## `product.product` (extends)


Public methods: `get_product_info_pos`

## `uom.category` (extends)

- `is_pos_groupable` Boolean “Group Products in POS”

## `uom.uom` (extends)

- `is_pos_groupable` Boolean (related=category_id.is_pos_groupable)

## `res.company` (extends)

- `point_of_sale_update_stock_quantities` Selection “Update quantities in stock”
- `point_of_sale_use_ticket_qr_code` Boolean “Use QR code on ticket”

Public methods: `validate_period_lock_date`

## `res.config.settings` (extends)

- `pos_config_id` Many2one → `pos.config` “Point of Sale”
- `sale_tax_id` Many2one → `account.tax` “Default Sale Tax” (related=company_id.account_sale_tax_id)
- `module_pos_mercury` Boolean “Vantiv Payment Terminal”
- `module_pos_adyen` Boolean “Adyen Payment Terminal”
- `module_pos_stripe` Boolean “Stripe Payment Terminal”
- `module_pos_six` Boolean “Six Payment Terminal”
- `update_stock_quantities` Selection (related=company_id.point_of_sale_update_stock_quantities)
- `account_default_pos_receivable_account_id` Many2one “Default Account Receivable (PoS)” (related=company_id.account_default_pos_receivable_account_id)
- `is_default_pricelist_displayed` Boolean (compute=_compute_pos_pricelist_id)
- `barcode_nomenclature_id` Many2one → `barcode.nomenclature` (related=company_id.nomenclature_id)
- `pos_module_pos_discount` Boolean (related=pos_config_id.module_pos_discount)
- `pos_module_pos_hr` Boolean (related=pos_config_id.module_pos_hr)
- `pos_module_pos_restaurant` Boolean (related=pos_config_id.module_pos_restaurant)
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
- `pos_iface_cashdrawer` Boolean “Cashdrawer” (store, compute=_compute_pos_iface_cashdrawer)
- `pos_iface_customer_facing_display_local` Boolean (related=pos_config_id.iface_customer_facing_display_local)
- `pos_iface_customer_facing_display_via_proxy` Boolean “Customer Facing Display” (store, compute=_compute_pos_iface_customer_facing_display_via_proxy)
- `pos_iface_electronic_scale` Boolean “Electronic Scale” (store, compute=_compute_pos_iface_electronic_scale)
- `pos_iface_print_auto` Boolean (related=pos_config_id.iface_print_auto)
- `pos_iface_print_skip_screen` Boolean (related=pos_config_id.iface_print_skip_screen)
- `pos_iface_print_via_proxy` Boolean “Print via Proxy” (store, compute=_compute_pos_iface_print_via_proxy)
- `pos_iface_scan_via_proxy` Boolean “Scan via Proxy” (store, compute=_compute_pos_iface_scan_via_proxy)
- `pos_iface_start_categ_id` Many2one → `pos.category` “Initial Category” (store, compute=_compute_pos_iface_start_categ_id)
- `pos_iface_tax_included` Selection (related=pos_config_id.iface_tax_included)
- `pos_iface_tipproduct` Boolean (related=pos_config_id.iface_tipproduct)
- `pos_invoice_journal_id` Many2one (related=pos_config_id.invoice_journal_id)
- `pos_is_header_or_footer` Boolean (related=pos_config_id.is_header_or_footer)
- `pos_is_margins_costs_accessible_to_every_user` Boolean (related=pos_config_id.is_margins_costs_accessible_to_every_user)
- `pos_is_posbox` Boolean (related=pos_config_id.is_posbox)
- `pos_journal_id` Many2one (related=pos_config_id.journal_id)
- `pos_limit_categories` Boolean (related=pos_config_id.limit_categories)
- `pos_limited_partners_amount` Integer (related=pos_config_id.limited_partners_amount)
- `pos_limited_partners_loading` Boolean (related=pos_config_id.limited_partners_loading)
- `pos_limited_products_amount` Integer (related=pos_config_id.limited_products_amount)
- `pos_limited_products_loading` Boolean (related=pos_config_id.limited_products_loading)
- `pos_manual_discount` Boolean (related=pos_config_id.manual_discount)
- `pos_only_round_cash_method` Boolean (related=pos_config_id.only_round_cash_method)
- `pos_other_devices` Boolean (related=pos_config_id.other_devices)
- `pos_partner_load_background` Boolean (related=pos_config_id.partner_load_background)
- `pos_payment_method_ids` Many2many (related=pos_config_id.payment_method_ids)
- `pos_picking_policy` Selection (related=pos_config_id.picking_policy)
- `pos_picking_type_id` Many2one (related=pos_config_id.picking_type_id)
- `pos_pricelist_id` Many2one → `product.pricelist` “Default Pricelist” (store, compute=_compute_pos_pricelist_id)
- `pos_product_load_background` Boolean (related=pos_config_id.product_load_background)
- `pos_proxy_ip` Char “IP Address” (store, compute=_compute_pos_proxy_ip)
- `pos_receipt_footer` Text “Receipt Footer” (store, compute=_compute_pos_receipt_header_footer)
- `pos_receipt_header` Text “Receipt Header” (store, compute=_compute_pos_receipt_header_footer)
- `pos_restrict_price_control` Boolean (related=pos_config_id.restrict_price_control)
- `pos_rounding_method` Many2one (related=pos_config_id.rounding_method)
- `pos_route_id` Many2one (related=pos_config_id.route_id)
- `pos_selectable_categ_ids` Many2many → `pos.category` (compute=_compute_pos_selectable_categ_ids)
- `pos_sequence_id` Many2one (related=pos_config_id.sequence_id)
- `pos_set_maximum_difference` Boolean (related=pos_config_id.set_maximum_difference)
- `pos_ship_later` Boolean (related=pos_config_id.ship_later)
- `pos_start_category` Boolean (related=pos_config_id.start_category)
- `pos_tax_regime_selection` Boolean (related=pos_config_id.tax_regime_selection)
- `pos_tip_product_id` Many2one → `product.product` “Tip Product” (store, compute=_compute_pos_tip_product_id)
- `pos_use_pricelist` Boolean (related=pos_config_id.use_pricelist)
- `pos_warehouse_id` Many2one “Warehouse (PoS)” (related=pos_config_id.warehouse_id)
- `point_of_sale_use_ticket_qr_code` Boolean (related=company_id.point_of_sale_use_ticket_qr_code)

Public methods: `action_pos_config_create_new`, `create`, `pos_open_ui`, `set_values`

## `res.partner` (extends)

- `pos_order_count` Integer (compute=_compute_pos_order)
- `pos_order_ids` One2many → `pos.order` (readonly)

Public methods: `action_view_pos_order`, `create_from_ui`

## `stock.picking` (extends)

- `pos_session_id` Many2one → `pos.session` (index)
- `pos_order_id` Many2one → `pos.order` (index)

Extension points: `_action_done`, `_create_move_from_pos_order_lines`, `_create_picking_from_pos_order_lines`, `_prepare_picking_vals`, `_prepare_stock_move_vals`

## `stock.picking.type` (extends)


Extension points: `_check_active`

## `procurement.group` (extends)

- `pos_order_id` Many2one → `pos.order`

## `stock.move` (extends)


Extension points: `_create_production_lots_for_pos_order`, `_get_new_picking_values`, `_prepare_lines_data_dict`

## `stock.rule` (extends)


Extension points: `_get_stock_move_values`

## `stock.warehouse` (extends)

- `pos_type_id` Many2one → `stock.picking.type` “Point of Sale Operation Type”

Extension points: `_create_missing_pos_picking_types`, `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_sequence_values`

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
- `total_discount` Float “Total Discount” (readonly)
- `average_price` Float “Average Price” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `nbr_lines` Integer “Sale Line Count” (readonly)
- `product_qty` Integer “Product Quantity” (readonly)
- `journal_id` Many2one → `account.journal` “Journal” (readonly)
- `delay_validation` Integer “Delay Validation” (readonly)
- `product_categ_id` Many2one → `product.category` “Product Category” (readonly)
- `invoiced` Boolean (readonly)
- `config_id` Many2one → `pos.config` “Point of Sale” (readonly)
- `pos_categ_id` Many2one → `pos.category` “PoS Category” (readonly)
- `pricelist_id` Many2one → `product.pricelist` “Pricelist” (readonly)
- `session_id` Many2one → `pos.session` “Session” (readonly)
- `margin` Float “Margin” (readonly)

Public methods: `init`

## `pos.close.session.wizard` (defines)

Close Session Wizard

- `amount_to_balance` Float “Amount to balance”
- `account_id` Many2one → `account.account`
- `account_readonly` Boolean “Destination account is readonly”
- `message` Text “Information message”

Public methods: `close_session`

## `pos.details.wizard` (defines)

Point of Sale Details Report

- `start_date` Datetime (required)
- `end_date` Datetime (required)
- `pos_config_ids` Many2many → `pos.config`

Public methods: `generate_report`

## `pos.make.payment` (defines)

Point of Sale Make Payment Wizard

- `config_id` Many2one → `pos.config` “Point of Sale Configuration” (required)
- `amount` Float (required)
- `payment_method_id` Many2one → `pos.payment.method` “Payment Method” (required)
- `payment_name` Char “Payment Reference”
- `payment_date` Datetime “Payment Date” (required)

Public methods: `check`, `launch_payment`

## `pos.session.check_product_wizard` (defines)

Verify if there are any products for the PoS


Public methods: `load_demo_products`, `open_ui`

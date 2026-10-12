# point_of_sale — XML ids

## barcode.rule

- `point_of_sale.barcode_rule_cashier`
- `point_of_sale.barcode_rule_client`
- `point_of_sale.barcode_rule_discount`
- `point_of_sale.barcode_rule_price_two_dec`

## digest.digest

- `digest.digest_digest_default`

## ir.actions.act_window

- `point_of_sale.action_pos_payment`
- `point_of_sale.action_report_pos_daily_sales_reports`
- `point_of_sale.action_confirm_action_wizard`
- `point_of_sale.action_pos_configuration`
- `point_of_sale.action_pos_note_model`
- `point_of_sale.action_pos_pos_form`
- `point_of_sale.action_pos_sale_graph`
- `point_of_sale.action_pos_order_line`
- `point_of_sale.action_pos_order_line_form`
- `point_of_sale.action_pos_order_line_day`
- `point_of_sale.action_pos_all_sales_lines`
- `point_of_sale.product_pos_category_action`
- `point_of_sale.product_template_action_pos_product`
- `point_of_sale.product_product_action`
- `point_of_sale.product_category_action`
- `point_of_sale.product_template_action_add_pos`
- `point_of_sale.product_template_action_edit_pos`
- `point_of_sale.action_pos_payment_method_form`
- `point_of_sale.action_payment_methods_tree`
- `point_of_sale.action_pos_payment_form`
- `point_of_sale.action_pos_config_kanban`
- `point_of_sale.action_pos_config_tree`
- `point_of_sale.action_pos_bill`
- `point_of_sale.action_pos_session`
- `point_of_sale.action_report_pos_order_all`
- `point_of_sale.action_report_pos_details`
- `point_of_sale.res_partner_action_edit_pos`
- `point_of_sale.action_pos_preset_form`
- `point_of_sale.action_pos_session_filtered`
- `point_of_sale.action_pos_order_filtered`
- `point_of_sale.action_report_pos_order_all_filtered`
- `point_of_sale.action_pos_printer_form`

## ir.actions.client

- `point_of_sale.action_client_pos_menu`
- `point_of_sale.action_client_product_menu`

## ir.actions.report

- `point_of_sale.report_user_label`
- `point_of_sale.sale_details_report`

## ir.actions.server

- `point_of_sale.pos_order_set_cancel`
- `point_of_sale.model_pos_order_send_mail`

## ir.filters

- `point_of_sale.filter_orders_per_session`

## ir.rule

- `point_of_sale.rule_pos_bank_statement_account_user`
- `point_of_sale.rule_pos_bank_statement_line_user`
- `point_of_sale.rule_pos_bank_statement_line_account_user`
- `point_of_sale.rule_pos_multi_company`
- `point_of_sale.rule_pos_order_line_multi_company`
- `point_of_sale.rule_pos_session_multi_company`
- `point_of_sale.rule_pos_config_multi_company`
- `point_of_sale.rule_pos_order_report_multi_company`
- `point_of_sale.rule_pos_payment_method_multi_company`
- `point_of_sale.rule_pos_payment_multi_company`
- `point_of_sale.rule_invoice_pos_user`
- `point_of_sale.rule_invoice_line_pos_user`

## ir.sequence

- `point_of_sale.seq_pos_session`

## ir.ui.menu

- `point_of_sale.menu_point_root` — Point of Sale
- `point_of_sale.menu_point_of_sale` — Orders
- `point_of_sale.menu_point_of_sale_customer` — Customers
- `point_of_sale.menu_point_rep` — Reporting
- `point_of_sale.menu_report_daily_details` — Session Report
- `point_of_sale.menu_point_config_product` — Configuration
- `point_of_sale.pos_menu_products_configuration` — Products
- `point_of_sale.menu_pos_global_settings` — Settings
- `point_of_sale.menu_pos_note_model`
- `point_of_sale.menu_point_ofsale`
- `point_of_sale.pos_config_menu_catalog` — Products
- `point_of_sale.menu_pos_products`
- `point_of_sale.pos_config_menu_action_product_product` — Product Variants
- `point_of_sale.menu_product_combo` — Combo Choices
- `point_of_sale.pos_config_menu_action_product_pricelist`
- `point_of_sale.menu_action_tax_form_open`
- `point_of_sale.menu_pos_payment_method`
- `point_of_sale.menu_pos_payment`
- `point_of_sale.menu_products_pos_category`
- `point_of_sale.pos_menu_products_attribute_action`
- `point_of_sale.menu_pos_dashboard` — Dashboard
- `point_of_sale.menu_point_of_sale_list` — Point of Sales
- `point_of_sale.menu_pos_bill` — Coins/Bills
- `point_of_sale.menu_pos_session_all`
- `point_of_sale.menu_report_pos_order_all` — Orders
- `point_of_sale.menu_report_order_details` — Sales Details
- `point_of_sale.menu_pos_preset`
- `point_of_sale.menu_pos_preparation_printer` — Preparation Printers
- `point_of_sale.pos_menu_products_tag_action`

## ir.ui.view

- `point_of_sale.view_pos_details_wizard` — on pos.details.wizard
- `point_of_sale.view_pos_payment` — on pos.make.payment
- `point_of_sale.view_form_pos_close_session_wizard` — on pos.close.session.wizard
- `point_of_sale.view_pos_daily_sales_reports_wizard` — on pos.daily.sales.reports.wizard
- `point_of_sale.view_confirm_action_wizard` — on pos.confirmation.wizard
- `point_of_sale.view_pos_make_invoice` — on pos.make.invoice
- `point_of_sale.index`
- `point_of_sale.view_pos_note_tree` — on pos.note
- `point_of_sale.view_pos_pos_form` — on pos.order
- `point_of_sale.view_pos_order_kanban` — on pos.order
- `point_of_sale.view_pos_order_pivot` — on pos.order
- `point_of_sale.view_pos_order_tree` — on pos.order
- `point_of_sale.view_pos_order_tree_no_session_id` — on pos.order inherits point_of_sale.view_pos_order_tree
- `point_of_sale.view_pos_order_search` — on pos.order
- `point_of_sale.view_pos_order_line` — on pos.order.line
- `point_of_sale.view_pos_order_line_form` — on pos.order.line
- `point_of_sale.view_pos_order_tree_all_sales_lines` — on pos.order.line
- `point_of_sale.view_pos_order_filter` — on pos.order
- `point_of_sale.pos_rounding_form_view_inherited` — on account.cash.rounding inherits account.rounding_form_view
- `point_of_sale.product_pos_category_form_view` — on pos.category
- `point_of_sale.product_pos_category_tree_view` — on pos.category
- `point_of_sale.view_pos_category_kanban` — on pos.category
- `point_of_sale.product_combo_view_form` — on product.combo inherits product.product_combo_view_form
- `point_of_sale.product_template_search_view_pos` — on product.template inherits product.product_template_search_view
- `point_of_sale.product_template_form_view` — on product.template inherits product.product_template_form_view
- `point_of_sale.product_template_only_form_view` — on product.template inherits product.product_template_only_form_view
- `point_of_sale.product_uom_form_view_inherit` — on uom.uom inherits uom.product_uom_form_view
- `point_of_sale.product_template_tree_view` — on product.template inherits product.product_template_tree_view
- `point_of_sale.product_template_tree_view_point_of_sale` — on product.template inherits point_of_sale.product_template_tree_view
- `point_of_sale.product_product_tree_view` — on product.product inherits product.product_product_tree_view
- `point_of_sale.product_template_view_form_normalized_pos` — on product.template
- `point_of_sale.pos_payment_method_view_form` — on pos.payment.method
- `point_of_sale.pos_payment_method_view_tree` — on pos.payment.method
- `point_of_sale.pos_payment_method_view_search` — on pos.payment.method
- `point_of_sale.view_pos_payment_form` — on pos.payment
- `point_of_sale.view_pos_payment_tree` — on pos.payment
- `point_of_sale.view_pos_payment_search` — on pos.payment
- `point_of_sale.pos_config_view_form` — on pos.config
- `point_of_sale.view_pos_config_tree` — on pos.config
- `point_of_sale.view_pos_config_search` — on pos.config
- `point_of_sale.view_pos_bill_form` — on pos.bill
- `point_of_sale.view_pos_bill_tree` — on pos.bill
- `point_of_sale.view_pos_session_form` — on pos.session
- `point_of_sale.view_pos_session_tree` — on pos.session
- `point_of_sale.view_pos_session_kanban` — on pos.session
- `point_of_sale.view_pos_session_search` — on pos.session
- `point_of_sale.view_report_pos_order_pivot` — on report.pos.order
- `point_of_sale.view_report_pos_order_graph` — on report.pos.order
- `point_of_sale.report_pos_order_view_tree` — on report.pos.order
- `point_of_sale.view_report_pos_order_search` — on report.pos.order
- `point_of_sale.digest_digest_view_form` — on digest.digest inherits digest.digest_digest_view_form
- `point_of_sale.view_partner_property_form` — on res.partner inherits base.view_partner_form
- `point_of_sale.report_userlabel`
- `point_of_sale.pos_daily_sales_report_layout`
- `point_of_sale.pos_daily_sales_html_container`
- `point_of_sale.report_saledetails`
- `point_of_sale.view_pos_preset_form` — on pos.preset
- `point_of_sale.view_pos_preset_tree` — on pos.preset
- `point_of_sale.view_pos_config_kanban` — on pos.config
- `point_of_sale.report_invoice_document` — inherits account.report_invoice_document
- `point_of_sale.view_pos_printer_form` — on pos.printer
- `point_of_sale.view_pos_printer` — on pos.printer
- `point_of_sale.ticket_validation_screen`
- `point_of_sale.ticket_request_with_code`
- `point_of_sale.res_config_settings_view_form` — on res.config.settings inherits base.res_config_settings_view_form
- `point_of_sale.customer_display_index`
- `point_of_sale.view_account_journal_pos_user_form` — on account.move inherits account.view_move_form
- `point_of_sale.pos_session_sales_details`
- `point_of_sale.product_tag_form_view_inherit_point_of_sale` — on product.tag inherits product.product_tag_form_view
- `point_of_sale.stock_reference_pos_view_form` — on stock.reference inherits stock.stock_reference_form_view

## mail.activity.type

- `point_of_sale.mail_activity_old_session`

## mail.template

- `point_of_sale.email_template_pos_receipt`

## pos.bill

- `point_of_sale.0_05`
- `point_of_sale.0_10`
- `point_of_sale.0_20`
- `point_of_sale.0_25`
- `point_of_sale.0_50`
- `point_of_sale.1_00`
- `point_of_sale.2_00`
- `point_of_sale.5_00`
- `point_of_sale.10_00`
- `point_of_sale.20_00`
- `point_of_sale.50_00`
- `point_of_sale.100_00`
- `point_of_sale.200_00`

## pos.note

- `point_of_sale.pos_note_wait`
- `point_of_sale.pos_note_serve`
- `point_of_sale.pos_note_emergency`
- `point_of_sale.pos_note_no_dressing`

## product.category

- `point_of_sale.product_category_food`

## product.product

- `point_of_sale.product_product_tip`

## res.groups

- `point_of_sale.group_pos_user`
- `point_of_sale.group_pos_manager`
- `point_of_sale.group_pos_preset`

## res.groups.privilege

- `point_of_sale.res_groups_privilege_point_of_sale`

## uom.uom

- `uom.product_uom_unit`
- `uom.product_uom_kgm`
- `uom.product_uom_pack_6`
- `uom.product_uom_dozen`

## web_tour.tour

- `point_of_sale.point_of_sale_tour`

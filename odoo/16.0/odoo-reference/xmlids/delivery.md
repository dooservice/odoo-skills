# delivery — XML ids

## delivery.carrier

- `delivery.free_delivery_carrier`

## ir.actions.act_window

- `delivery.action_delivery_carrier_form`
- `delivery.action_delivery_zip_prefix_list`
- `delivery.act_delivery_trackers_url`

## ir.rule

- `delivery.delivery_carrier_comp_rule`

## ir.ui.menu

- `delivery.menu_action_delivery_carrier_form`
- `delivery.sale_menu_action_delivery_carrier_form`
- `delivery.menu_delivery_zip_prefix`

## ir.ui.view

- `delivery.product_template_hs_code` — on product.template inherits product.product_template_form_view
- `delivery.view_delivery_carrier_tree` — on delivery.carrier
- `delivery.view_delivery_carrier_search` — on delivery.carrier
- `delivery.view_delivery_carrier_form` — on delivery.carrier
- `delivery.view_delivery_price_rule_form` — on delivery.price.rule
- `delivery.view_delivery_price_rule_tree` — on delivery.price.rule
- `delivery.view_picking_withcarrier_out_form` — on stock.picking inherits stock.view_picking_form
- `delivery.view_picking_withweight_internal_move_form` — on stock.move inherits stock.view_move_form
- `delivery.view_move_line_tree_detailed_delivery` — on stock.move.line inherits stock.view_move_line_tree_detailed
- `delivery.view_quant_package_weight_form` — on stock.quant.package inherits stock.view_quant_package_form
- `delivery.view_order_form_with_carrier` — on sale.order inherits sale.view_order_form
- `delivery.delivery_tracking_url_warning_form` — on stock.picking
- `delivery.vpicktree_view_tree` — on stock.picking inherits stock.vpicktree
- `delivery.view_partner_property_form` — on res.partner inherits base.view_partner_form
- `delivery.sale_order_portal_content_inherit_sale_stock_inherit_website_sale_delivery` — inherits sale_stock.sale_order_portal_content_inherit_sale_stock
- `delivery.report_shipping2` — inherits stock.report_picking
- `delivery.report_delivery_document2` — inherits stock.report_delivery_document
- `delivery.stock_report_delivery_has_serial_move_line_inherit_delivery` — inherits stock.stock_report_delivery_has_serial_move_line
- `delivery.stock_report_delivery_aggregated_move_lines_inherit_delivery` — inherits stock.stock_report_delivery_aggregated_move_lines
- `delivery.stock_report_delivery_package_section_line_inherit_delivery` — inherits stock.stock_report_delivery_package_section_line
- `delivery.delivery_stock_report_delivery_no_package_section_line` — inherits stock.stock_report_delivery_no_package_section_line
- `delivery.label_package_template_view_delivery` — inherits stock.label_package_template_view
- `delivery.report_package_barcode_delivery` — inherits stock.report_package_barcode
- `delivery.report_package_barcode_small_delivery` — inherits stock.report_package_barcode_small
- `delivery.res_config_settings_view_form` — on res.config.settings inherits sale.res_config_settings_view_form
- `delivery.choose_delivery_package_view_form` — on choose.delivery.package
- `delivery.choose_delivery_carrier_view_form` — on choose.delivery.carrier
- `delivery.stock_package_type_form_delivery` — on stock.package.type inherits stock.stock_package_type_form
- `delivery.stock_package_type_tree_delivery` — on stock.package.type inherits stock.stock_package_type_tree
- `delivery.view_picking_type_form_delivery` — on stock.picking.type inherits stock.view_picking_type_form
- `delivery.view_stock_rule_form_delivery` — on stock.rule inherits stock.view_stock_rule_form
- `delivery.stock_move_line_view_search_delivery` — on stock.move.line inherits stock.stock_move_line_view_search
- `delivery.delivery_report_saleorder_document` — inherits sale.report_saleorder_document

## product.category

- `delivery.product_category_deliveries`

## product.product

- `delivery.product_product_delivery`

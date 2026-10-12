# stock_delivery — XML ids

## ir.actions.act_window

- `stock_delivery.open_shipping_labels_report`
- `stock_delivery.open_export_docs_report`
- `stock_delivery.act_delivery_trackers_url`

## ir.actions.report

- `stock_delivery.action_report_shipping_labels`
- `stock_delivery.action_report_shipping_docs`

## ir.ui.menu

- `stock_delivery.menu_action_delivery_carrier_form`
- `stock_delivery.menu_delivery_zip_prefix`
- `stock_delivery.cached_printers_section` — Reporting
- `stock_delivery.manage_printers_action` — Manage Printers
- `stock_delivery.cached_printers_action` — Reset Linked Printers
- `stock.menu_stock_config_settings`
- `stock.menu_product_in_config_stock`

## ir.ui.view

- `stock_delivery.report_shipping_labels`
- `stock_delivery.report_shipping_docs`
- `stock_delivery.product_template_hs_code` — on product.template inherits stock.product_template_form_view_stock
- `stock_delivery.product_product_hs_code` — on product.product inherits product.product_normal_form_view
- `stock_delivery.product_product_hs_code_list` — on product.product inherits product.product_product_tree_view
- `stock_delivery.view_delivery_carrier_form_inherit_stock_delivery` — on delivery.carrier inherits delivery.view_delivery_carrier_form
- `stock_delivery.view_picking_withcarrier_out_form` — on stock.picking inherits stock.view_picking_form
- `stock_delivery.view_picking_withweight_internal_move_form` — on stock.move inherits stock.view_move_form
- `stock_delivery.view_move_line_tree_detailed_delivery` — on stock.move.line inherits stock.view_move_line_tree_detailed
- `stock_delivery.stock_package_view_form` — on stock.package inherits stock.stock_package_view_form
- `stock_delivery.delivery_tracking_url_warning_form` — on stock.picking
- `stock_delivery.vpicktree_view_tree` — on stock.picking inherits stock.vpicktree
- `stock_delivery.sale_order_portal_content_inherit_sale_stock_inherit_website_sale` — inherits sale_stock.sale_order_portal_content_inherit_sale_stock
- `stock_delivery.report_shipping2` — inherits stock.report_picking
- `stock_delivery.report_delivery_document2` — inherits stock.report_delivery_document
- `stock_delivery.stock_report_delivery_has_serial_move_line_inherit_delivery` — inherits stock.stock_report_delivery_has_serial_move_line
- `stock_delivery.stock_report_delivery_aggregated_move_lines_inherit_delivery` — inherits stock.stock_report_delivery_aggregated_move_lines
- `stock_delivery.stock_report_delivery_package_section_line_inherit_delivery` — inherits stock.stock_report_delivery_package_section_line
- `stock_delivery.delivery_stock_report_delivery_no_package_section_line` — inherits stock.stock_report_delivery_no_package_section_line
- `stock_delivery.report_package_barcode_delivery` — inherits stock.report_package_barcode
- `stock_delivery.package_zpl_label_delivery` — inherits stock.package_zpl_label
- `stock_delivery.package_pdf_label_delivery` — inherits stock.package_pdf_label
- `stock_delivery.choose_delivery_carrier_view_form` — on choose.delivery.carrier inherits delivery.choose_delivery_carrier_view_form
- `stock_delivery.pay_on_delivery_form` — on pay.on.delivery
- `stock_delivery.stock_put_in_pack_form` — on stock.put.in.pack inherits stock.stock_put_in_pack_form
- `stock_delivery.stock_package_type_form_delivery` — on stock.package.type inherits stock.stock_package_type_form
- `stock_delivery.stock_package_type_tree_delivery` — on stock.package.type inherits stock.stock_package_type_tree
- `stock_delivery.view_picking_type_form_delivery` — on stock.picking.type inherits stock.view_picking_type_form
- `stock_delivery.view_stock_rule_form_delivery` — on stock.rule inherits stock.view_stock_rule_form
- `stock_delivery.stock_location_route_view_form_inherit_stock_delivery` — on stock.route inherits stock.stock_location_route_form_view
- `stock_delivery.stock_move_line_view_search_delivery` — on stock.move.line inherits stock.stock_move_line_view_search
- `stock_delivery.barcode_normal_label` — inherits product.barcode_normal_label
- `stock_delivery.barcode_alternative_label` — inherits product.barcode_alternative_label

## mail.template

- `delivery.mail_template_data_delivery_note`

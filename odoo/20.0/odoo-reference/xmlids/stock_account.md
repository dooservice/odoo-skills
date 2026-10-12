# stock_account — XML ids

## ir.actions.act_window

- `stock_account.product_value_action`
- `stock_account.product_value_list_action`
- `stock_account.stock_move_valuation_action`
- `stock_account.stock_avco_report_action`

## ir.actions.server

- `stock_account.stock_move_action_adjust_valuation`

## ir.filters

- `stock_account.filter_stock_move_aging_report`
- `stock_account.filter_stock_move_intercompany_deliveries`
- `stock_account.filter_invoice_inventory_valuation`

## ir.ui.menu

- `stock_account.valuation_adjustments_menu` — Valuation Adjustments

## ir.ui.view

- `stock_account.view_move_form` — on account.move inherits account.view_move_form
- `stock_account.res_config_settings_view_form` — on res.config.settings inherits stock.res_config_settings_view_form
- `stock_account.stock_account_report_invoice_document` — inherits account.report_invoice_document
- `stock_account.view_stock_quant_tree_inherit` — on stock.quant inherits stock.view_stock_quant_tree
- `stock_account.view_stock_quant_tree_editable_inherit` — on stock.quant inherits stock.view_stock_quant_tree_editable
- `stock_account.view_stock_quant_tree_inventory_editable_inherit_stock_account` — on stock.quant inherits stock.view_stock_quant_tree_inventory_editable
- `stock_account.product_template_tree_view` — on product.template inherits product.product_template_tree_view
- `stock_account.product_template_form_view_stock_account` — on product.template inherits stock.product_template_form_view_stock
- `stock_account.product_product_stock_tree_inherit_stock_account` — on product.product inherits stock.product_product_stock_tree
- `stock_account.product_value_form_view` — on product.value
- `stock_account.product_value_list_view` — on product.value
- `stock_account.product_value_search_view` — on product.value
- `stock_account.view_location_form_inherit` — on stock.location inherits stock.view_location_form
- `stock_account.view_production_lot_form_stock_account` — on stock.lot inherits stock.view_production_lot_form
- `stock_account.stock_move_view_list` — on stock.move inherits stock.view_move_tree
- `stock_account.stock_move_view_pivot` — on stock.move inherits stock.view_move_pivot
- `stock_account.view_move_search` — on stock.move inherits stock.view_move_search
- `stock_account.stock_move_view_list_valuation` — on stock.move
- `stock_account.stock_inventory_adjustment_name_form_view_inherit_stock_account` — on stock.inventory.adjustment.name inherits stock.stock_inventory_adjustment_name_form_view
- `stock_account.stock_avco_report_view_list` — on stock.avco.report

## res.groups

- `stock_account.group_lot_on_invoice`

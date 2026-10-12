# delivery — XML ids

## delivery.carrier

- `delivery.free_delivery_carrier`

## ir.actions.act_window

- `delivery.action_delivery_carrier_form`
- `delivery.action_delivery_zip_prefix_list`

## ir.rule

- `delivery.delivery_carrier_comp_rule`

## ir.ui.menu

- `delivery.sale_menu_action_delivery_carrier_form`

## ir.ui.view

- `delivery.delivery_report_saleorder_document` — inherits sale.report_saleorder_document
- `delivery.view_delivery_carrier_tree` — on delivery.carrier
- `delivery.view_delivery_carrier_search` — on delivery.carrier
- `delivery.view_delivery_carrier_form` — on delivery.carrier
- `delivery.view_delivery_price_rule_form` — on delivery.price.rule
- `delivery.view_delivery_price_rule_tree` — on delivery.price.rule
- `delivery.view_partner_property_form` — on res.partner inherits base.view_partner_form
- `delivery.view_order_form_with_carrier` — on sale.order inherits sale.view_order_form
- `delivery.res_config_settings_view_form` — on res.config.settings inherits sale.res_config_settings_view_form
- `delivery.choose_delivery_carrier_view_form` — on choose.delivery.carrier

## product.category

- `delivery.product_category_deliveries`

## product.product

- `delivery.product_product_delivery`

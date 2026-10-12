# delivery — XML ids

## delivery.carrier

- `delivery.free_delivery_carrier`

## ir.actions.act_window

- `delivery.action_delivery_carrier_form`
- `delivery.action_delivery_zip_prefix_list`

## ir.actions.report

- `delivery.action_report_delivery_note`

## ir.sequence

- `delivery.seq_delivery_note`

## ir.ui.menu

- `delivery.sale_menu_action_delivery_carrier_form` — Deliveries

## ir.ui.view

- `delivery.delivery_report_saleorder_document` — inherits sale.report_saleorder_document
- `delivery.report_delivery_note`
- `delivery.view_delivery_carrier_tree` — on delivery.carrier
- `delivery.view_delivery_carrier_so_list` — on delivery.carrier
- `delivery.view_delivery_carrier_search` — on delivery.carrier
- `delivery.view_delivery_carrier_form` — on delivery.carrier
- `delivery.view_delivery_price_rule_form` — on delivery.price.rule
- `delivery.view_delivery_price_rule_tree` — on delivery.price.rule
- `delivery.delivery_provider_module_list` — on ir.module.module inherits base.module_tree
- `delivery.delivery_provider_module_kanban` — on ir.module.module inherits base.module_view_kanban
- `delivery.delivery_submit_button` — inherits payment.submit_button
- `delivery.payment_provider_form` — on payment.provider inherits payment_custom.payment_provider_form
- `delivery.state_header` — inherits payment.state_header
- `delivery.view_partner_property_form` — on res.partner inherits sale.res_partner_view_form_property_inherit
- `delivery.view_order_form_with_carrier` — on sale.order inherits sale.view_order_form
- `delivery.res_config_settings_view_form` — on res.config.settings inherits sale.res_config_settings_view_form
- `delivery.choose_delivery_carrier_view_form` — on choose.delivery.carrier
- `delivery.delivery_note_list_view` — on delivery.note.wizard.line
- `delivery.delivery_note_form_view` — on delivery.note.wizard

## mail.template

- `delivery.mail_template_data_delivery_note`

## payment.method

- `delivery.payment_method_cash_on_delivery`

## payment.provider

- `delivery.payment_provider_cod`

## product.category

- `delivery.product_category_deliveries`

## product.product

- `delivery.product_product_delivery`

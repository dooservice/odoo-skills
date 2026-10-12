# pos_sale — XML ids

## crm.team

- `sales_team.pos_sales_team`

## ir.actions.act_window

- `pos_sale.pos_session_action_from_crm_team`

## ir.rule

- `pos_sale.pos_sale_rule_pos_channel_pos_manager`

## ir.ui.view

- `pos_sale.report_invoice_document` — inherits account.report_invoice_document
- `pos_sale.view_order_form_inherit_pos_sale` — on sale.order inherits sale.view_order_form
- `pos_sale.view_pos_order_form_inherit_pos_sale` — on pos.order inherits point_of_sale.view_pos_pos_form
- `pos_sale.product_template_form_view` — on product.template inherits sale.product_template_form_view
- `pos_sale.view_pos_session_search_inherit_pos_sale` — on pos.session inherits point_of_sale.view_pos_session_search
- `pos_sale.view_pos_config_search_inherit_pos_sale` — on pos.config inherits point_of_sale.view_pos_config_search
- `pos_sale.crm_team_view_kanban_dashboard` — on crm.team inherits sales_team.crm_team_view_kanban_dashboard
- `pos_sale.res_config_settings_view_form` — on res.config.settings inherits point_of_sale.res_config_settings_view_form
- `pos_sale.message_body` — inherits stock.message_body

## product.product

- `pos_sale.default_downpayment_product`

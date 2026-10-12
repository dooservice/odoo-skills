# sale — XML ids

## ir.actions.act_window

- `sale.action_account_invoice_report_salesteam`
- `sale.action_order_report_all`
- `sale.action_order_report_salesperson`
- `sale.action_order_report_products`
- `sale.action_order_report_customers`
- `sale.report_all_channels_sales_action`
- `sale.action_order_report_quotation_salesteam`
- `sale.action_order_report_so_salesteam`
- `sale.action_accrued_revenue_entry`
- `sale.action_mass_cancel_orders`
- `sale.action_sale_order_generate_link`
- `sale.action_sale_config_settings`
- `sale.action_view_sale_advance_payment_inv`
- `sale.action_orders`
- `sale.action_quotations_with_onboarding`
- `sale.action_quotations`
- `sale.action_orders_to_invoice`
- `sale.action_orders_upselling`
- `sale.action_invoice_salesteams`
- `sale.action_quotations_salesteams`
- `sale.action_quotation_form`
- `sale.action_orders_salesteams`
- `sale.action_orders_to_invoice_salesteams`
- `sales_team.mail_activity_type_action_config_sales`
- `sale.mail_activity_type_action_config_sale`
- `sale.mail_activity_plan_action_sale_order`
- `sale.product_template_action`
- `sale.act_res_partner_2_sale_order`

## ir.actions.act_window.view

- `sale.sale_order_action_view_order_tree`
- `sale.sale_order_action_view_order_kanban`
- `sale.sale_order_action_view_order_form`
- `sale.sale_order_action_view_order_calendar`
- `sale.sale_order_action_view_order_pivot`
- `sale.sale_order_action_view_order_graph`
- `sale.sale_order_action_view_quotation_tree`
- `sale.sale_order_action_view_quotation_kanban`
- `sale.sale_order_action_view_quotation_form`
- `sale.sale_order_action_view_quotation_calendar`
- `sale.sale_order_action_view_quotation_pivot`
- `sale.sale_order_action_view_quotation_graph`
- `sale.action_invoice_salesteams_view_tree`
- `sale.action_invoice_salesteams_view_form`

## ir.actions.report

- `sale.action_report_saleorder`
- `sale.action_report_pro_forma_invoice`

## ir.actions.server

- `sale.model_sale_order_action_quotation_sent`
- `sale.model_sale_order_action_share`

## ir.config_parameter

- `sale.default_confirmation_template`
- `sale.default_invoice_email_template`

## ir.cron

- `sale.send_invoice_cron`

## ir.rule

- `sale.sale_order_comp_rule`
- `sale.sale_order_line_comp_rule`
- `sale.sale_order_report_comp_rule`
- `sale.sale_order_rule_portal`
- `sale.sale_order_line_rule_portal`
- `sale.sale_order_personal_rule`
- `sale.sale_order_see_all`
- `sale.sale_order_report_personal_rule`
- `sale.sale_order_report_see_all`
- `sale.sale_order_line_personal_rule`
- `sale.sale_order_line_see_all`
- `sale.account_invoice_report_rule_see_personal`
- `sale.account_invoice_report_rule_see_all`
- `sale.payment_transaction_salesman_rule`
- `sale.payment_token_salesman_rule`
- `sale.account_invoice_rule_see_personal`
- `sale.account_invoice_rule_see_all`
- `sale.account_invoice_line_rule_see_personal`
- `sale.account_invoice_line_rule_see_all`
- `sale.account_invoice_send_rule_see_personal`
- `sale.account_invoice_send_rule_see_all`
- `sale.sale_payment_provider_onboarding_wizard_rule`
- `sale.sale_advance_payment_inv_rule`
- `sale.sale_order_cancel_rule`
- `sale.sale_mass_cancel_orders_rule`
- `sale.mail_plan_rule_group_sale_manager`
- `sale.mail_plan_template_rule_group_sale_manager`

## ir.sequence

- `sale.seq_sale_order`

## ir.ui.menu

- `sale.sale_menu_root` — Sales

## ir.ui.view

- `sale.view_account_invoice_report_search_inherit` — on account.invoice.report inherits account.view_account_invoice_report_search
- `sale.account_invoice_report_view_tree` — on account.invoice.report inherits account.account_invoice_report_view_tree
- `sale.report_saleorder_document`
- `sale.report_saleorder_raw`
- `sale.report_saleorder`
- `sale.report_saleorder_pro_forma`
- `sale.document_tax_totals` — inherits account.document_tax_totals_template
- `sale.view_order_product_pivot` — on sale.report
- `sale.view_order_product_graph` — on sale.report
- `sale.sale_report_graph_pie` — on sale.report inherits view_order_product_graph
- `sale.sale_report_graph_bar` — on sale.report inherits view_order_product_graph
- `sale.sale_report_view_tree` — on sale.report
- `sale.view_order_product_search` — on sale.report
- `sale.mass_cancel_orders_view_form` — on sale.mass.cancel.orders
- `sale.payment_link_wizard_view_form` — on payment.link.wizard inherits payment.payment_link_wizard_view_form
- `sale.res_config_settings_view_form` — on res.config.settings inherits base.res_config_settings_view_form
- `sale.view_sale_advance_payment_inv` — on sale.advance.payment.inv
- `sale.sale_order_cancel_view_form` — on sale.order.cancel
- `sale.sale_order_line_wizard_form` — on sale.order.discount
- `sale.sale_order_view_activity` — on sale.order
- `sale.view_sale_order_calendar` — on sale.order
- `sale.view_sale_order_graph` — on sale.order
- `sale.view_sale_order_pivot` — on sale.order
- `sale.view_sale_order_kanban` — on sale.order
- `sale.sale_order_tree` — on sale.order
- `sale.view_order_tree` — on sale.order inherits sale_order_tree
- `sale.view_quotation_tree` — on sale.order inherits sale_order_tree
- `sale.view_quotation_tree_with_onboarding` — on sale.order inherits view_quotation_tree
- `sale.view_order_form` — on sale.order
- `sale.view_sales_order_filter` — on sale.order
- `sale.sale_order_view_search_inherit_quotation` — on sale.order inherits sale.view_sales_order_filter
- `sale.sale_order_view_search_inherit_sale` — on sale.order inherits sale.view_sales_order_filter
- `sale.account_invoice_groupby_inherit` — on account.move inherits account.view_account_invoice_filter
- `sale.account_invoice_view_tree` — on account.move inherits account.view_invoice_tree
- `sale.account_invoice_form` — on account.move inherits account.view_move_form
- `sale.crm_team_salesteams_view_form` — on crm.team inherits sales_team.crm_team_view_form
- `sale.crm_team_view_kanban_dashboard` — on crm.team inherits sales_team.crm_team_view_kanban_dashboard
- `sale.payment_provider_form` — on payment.provider inherits payment.payment_provider_form
- `sale.transaction_form_inherit_sale` — on payment.transaction inherits payment.payment_transaction_form
- `sale.product_document_form` — on product.document inherits product.product_document_form
- `sale.product_document_kanban` — on product.document inherits product.product_document_kanban
- `sale.product_document_list` — on product.document inherits product.product_document_list
- `sale.product_document_search` — on product.document inherits product.product_document_search
- `sale.product_packaging_form_view_sale` — on product.packaging inherits product.product_packaging_form_view
- `sale.product_packaging_tree_view_sale` — on product.packaging inherits product.product_packaging_tree_view
- `sale.product_template_form_view` — on product.template inherits product.product_template_form_view
- `sale.product_form_view_sale_order_button` — on product.product inherits product.product_normal_form_view
- `sale.product_template_form_view_sale_order_button` — on product.template inherits product.product_template_only_form_view
- `sale.product_view_kanban_catalog` — on product.product inherits product.product_view_kanban_catalog
- `sale.product_view_search_catalog` — on product.product inherits product.product_view_search_catalog
- `sale.crm_lead_partner_kanban_view` — on res.partner inherits base.res_partner_kanban_view
- `sale.res_partner_view_buttons` — on res.partner inherits base.view_partner_form
- `sale.res_partner_view_form_payment_defaultcreditcard` — on res.partner inherits payment.view_partners_form_payment_defaultcreditcard
- `sale.res_partner_view_form_property_inherit` — on res.partner inherits account.view_partner_property_form
- `sale.view_order_line_tree` — on sale.order.line
- `sale.sale_order_line_view_form_readonly` — on sale.order.line
- `sale.view_sales_order_line_filter` — on sale.order.line
- `sale.sale_order_line_view_kanban` — on sale.order.line
- `sale.portal_my_home_menu_sale` — inherits portal.portal_breadcrumbs
- `sale.portal_my_home_sale` — inherits portal.portal_my_home
- `sale.portal_my_quotations`
- `sale.portal_my_orders`
- `sale.sale_order_portal_template` — inherits portal.portal_sidebar
- `sale.sale_order_portal_content`
- `sale.sale_order_portal_content_totals_table`
- `sale.utm_campaign_view_kanban` — on utm.campaign inherits utm.utm_campaign_view_kanban
- `sale.utm_campaign_view_form` — on utm.campaign inherits utm.utm_campaign_view_form

## mail.activity.type

- `sale.mail_act_sale_upsell`

## mail.message.subtype

- `sale.mt_order_sent`
- `sale.mt_order_confirmed`
- `sale.mt_salesteam_order_sent`
- `sale.mt_salesteam_order_confirmed`
- `sale.mt_salesteam_invoice_created`
- `sale.mt_salesteam_invoice_confirmed`

## mail.template

- `sale.email_template_edi_sale`
- `sale.mail_template_sale_confirmation`
- `sale.mail_template_sale_payment_executed`
- `sale.mail_template_sale_cancellation`

## onboarding.onboarding

- `sale.onboarding_onboarding_sale_quotation`

## onboarding.onboarding.step

- `sale.onboarding_onboarding_step_sale_order_confirmation`
- `sale.onboarding_onboarding_step_sample_quotation`

## res.groups

- `sale.group_auto_done_setting`
- `sale.group_warning_sale`
- `sale.group_proforma_sales`

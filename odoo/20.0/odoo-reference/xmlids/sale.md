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
- `sale.action_mass_cancel_orders`
- `sale.action_sale_order_generate_link`
- `sale.action_sale_config_settings`
- `sale.action_view_sale_advance_payment_inv`
- `sale.action_orders`
- `sale.action_quotations_with_onboarding`
- `sale.action_quotations`
- `sale.mail_followers_edit_action_from_sale`
- `sale.action_invoice_salesteams`
- `sale.action_service_material`
- `sale.action_quotations_salesteams`
- `sale.action_quotation_form`
- `sale.action_orders_salesteams`
- `sale.action_orders_to_invoice_salesteams`
- `sales_team.mail_activity_type_action_config_sales`
- `sale.mail_activity_type_action_config_sale`
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
- `sale.action_quotations_tree`
- `sale.action_quotations_kanban`
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

- `sale.action_accrued_revenue_entry_sale_order_line`
- `sale.model_sale_order_action_quotation_sent`
- `sale.model_sale_order_action_quotation_confirm`
- `sale.model_sale_order_action_share`
- `sale.model_sale_order_action_deliver_sold_quantity`
- `sale.model_sale_order_send_mail`
- `sale.model_sale_order_action_close_invoicing`

## ir.config_parameter

- `sale.default_confirmation_template`
- `sale.default_invoice_email_template`
- `sale.async_emails`

## ir.cron

- `sale.send_invoice_cron`
- `sale.send_pending_emails_cron`

## ir.sequence

- `sale.seq_sale_order`

## ir.ui.menu

- `sale.sale_menu_root` — Sales
- `sale.sale_order_menu` — Orders
- `sale.menu_sale_quotations`
- `sale.menu_sale_order` — Orders
- `sale.menu_service_material`
- `sale.res_partner_menu`
- `sale.product_menu_catalog` — Products
- `sale.menu_product_template_action`
- `sale.menu_product_attribute_action`
- `sale.menu_product_pricelist_main` — Pricelists
- `sale.menu_sale_marketplaces` — Marketplaces
- `sale.menu_sale_report` — Reporting
- `sale.menu_reporting_sales` — Sales
- `sale.menu_reporting_salespeople` — Salespersons
- `sale.menu_reporting_product` — Products
- `sale.menu_reporting_customer` — Customers
- `sale.menu_sale_config` — Configuration
- `sale.menu_sale_general_settings` — Settings
- `sale.sales_team_config` — Teams
- `sale.payment_provider_menu` — Payments
- `sale.menu_sales_config` — Sales Orders

## ir.ui.view

- `sale.view_account_invoice_report_search_inherit` — on account.invoice.report inherits account.view_account_invoice_report_search
- `sale.account_invoice_report_view_tree` — on account.invoice.report inherits account.account_invoice_report_view_tree
- `sale.report_saleorder_document`
- `sale.report_saleorder_raw`
- `sale.report_saleorder`
- `sale.report_saleorder_pro_forma`
- `sale.document_tax_totals` — inherits account.document_tax_totals_template
- `sale.quote_document_layout_preview`
- `sale.view_order_product_pivot` — on sale.report
- `sale.view_order_product_graph` — on sale.report
- `sale.sale_report_graph_pie` — on sale.report inherits view_order_product_graph
- `sale.sale_report_graph_bar` — on sale.report inherits view_order_product_graph
- `sale.sale_report_view_tree` — on sale.report
- `sale.view_order_product_search` — on sale.report
- `sale.mass_cancel_orders_view_form` — on sale.mass.cancel.orders
- `sale.payment_link_wizard_view_form` — on payment.link.wizard inherits payment.payment_link_wizard_view_form
- `sale.res_config_settings_view_form` — on res.config.settings inherits base.res_config_settings_view_form
- `sale.res_config_settings_view_form_sale_inherit` — on res.config.settings inherits account.res_config_settings_view_form
- `sale.view_sale_advance_payment_inv` — on sale.advance.payment.inv
- `sale.sale_order_line_wizard_form` — on sale.order.discount
- `sale.sale_order_view_activity` — on sale.order
- `sale.view_sale_order_calendar` — on sale.order
- `sale.view_sale_order_graph` — on sale.order
- `sale.view_sale_order_pivot` — on sale.order
- `sale.view_sale_order_kanban` — on sale.order
- `sale.sale_order_kanban_upload` — on sale.order inherits view_sale_order_kanban
- `sale.sale_order_tree` — on sale.order
- `sale.view_order_tree` — on sale.order inherits sale_order_tree
- `sale.sale_order_list_upload` — on sale.order inherits view_order_tree
- `sale.view_quotation_tree` — on sale.order inherits sale_order_tree
- `sale.view_quotation_tree_with_onboarding` — on sale.order inherits view_quotation_tree
- `sale.view_quotation_kanban_with_onboarding` — on sale.order inherits view_sale_order_kanban
- `sale.view_order_form` — on sale.order
- `sale.view_order_form_mandatory_product` — on sale.order inherits sale.view_order_form
- `sale.view_sales_order_filter` — on sale.order
- `sale.sale_order_view_search_inherit_quotation` — on sale.order inherits sale.view_sales_order_filter
- `sale.sale_order_view_search_inherit_sale` — on sale.order inherits sale.view_sales_order_filter
- `sale.sale_order_list_with_dashboard` — on sale.order inherits sale.view_quotation_tree
- `sale.sale_order_kanban_with_dashboard` — on sale.order inherits sale.view_sale_order_kanban
- `sale.account_invoice_groupby_inherit` — on account.move inherits account.view_account_invoice_filter
- `sale.account_invoice_view_tree` — on account.move inherits account.view_invoice_tree
- `sale.account_invoice_form` — on account.move inherits account.view_move_form
- `sale.view_analytic_lines_service_search` — on account.analytic.line
- `sale.view_analytic_lines_service_list` — on account.analytic.line
- `sale.crm_team_view_kanban_dashboard` — on crm.team inherits sales_team.crm_team_view_kanban_dashboard
- `sale.payment_provider_form` — on payment.provider inherits payment.payment_provider_form
- `sale.transaction_form_inherit_sale` — on payment.transaction inherits payment.payment_transaction_form
- `sale.product_document_form` — on product.document inherits product.product_document_form
- `sale.product_document_kanban` — on product.document inherits product.product_document_kanban
- `sale.product_document_list` — on product.document inherits product.product_document_list
- `sale.product_document_search` — on product.document inherits product.product_document_search
- `sale.product_template_view_form` — on product.template inherits product.product_template_form_view
- `sale.product_template_form_view_sale` — on product.template inherits product.product_template_form_view
- `sale.product_template_form_view` — on product.template inherits product.product_template_form_view
- `sale.product_form_view_sale_order_button` — on product.product inherits product.product_normal_form_view
- `sale.product_template_form_view_sale_order_button` — on product.template inherits product.product_template_only_form_view
- `sale.product_view_kanban_catalog` — on product.product inherits product.product_view_kanban_catalog
- `sale.product_view_search_catalog` — on product.product inherits product.product_view_search_catalog
- `sale.product_template_sale_tree_view` — on product.product inherits product.product_template_tree_view
- `sale.product_product_sale_tree_view` — on product.product inherits product.product_product_tree_view
- `sale.view_category_property_form` — on product.category inherits account.view_category_property_form
- `sale.res_partner_view_buttons` — on res.partner inherits base.view_partner_form
- `sale.res_partner_view_form_payment_defaultcreditcard` — on res.partner inherits payment.view_partners_form_payment_defaultcreditcard
- `sale.res_partner_view_form_property_inherit` — on res.partner inherits account.view_partner_property_form
- `sale.view_partner_tree_inherit` — on res.partner inherits base.view_partner_tree
- `sale.view_order_line_tree` — on sale.order.line
- `sale.sale_order_line_view_form_readonly` — on sale.order.line
- `sale.view_sales_order_line_filter` — on sale.order.line
- `sale.sale_order_line_view_kanban` — on sale.order.line
- `sale.portal_my_home_menu_sale` — inherits portal.portal_breadcrumbs
- `sale.portal_my_quotations`
- `sale.portal_my_orders`
- `sale.sale_order_portal_template` — inherits portal.portal_sidebar
- `sale.sale_order_portal_sign_modal`
- `sale.sale_order_portal_pay_modal`
- `sale.sale_order_portal_pay_modal_amount_selector`
- `sale.sale_order_portal_content`
- `sale.payment_form_hide_tokens_heading` — inherits payment.form
- `sale.sale_order_portal_content_totals_table`
- `sale.utm_campaign_view_kanban` — on utm.campaign inherits utm.utm_campaign_view_kanban
- `sale.utm_campaign_view_form` — on utm.campaign inherits utm.utm_campaign_view_form

## mail.message.subtype

- `sale.mt_order_sent`
- `sale.mt_order_confirmed`
- `sale.mt_order_viewed`
- `sale.mt_salesteam_order_sent`
- `sale.mt_salesteam_order_viewed`
- `sale.mt_salesteam_order_confirmed`
- `sale.mt_salesteam_invoice_paid`
- `sale.mt_salesteam_invoice_posted`

## mail.template

- `sale.email_template_edi_sale`
- `sale.email_template_proforma`
- `sale.mail_template_sale_confirmation`
- `sale.mail_template_sale_payment_executed`

## portal.entry

- `sale.portal_quotations_to_review`
- `sale.portal_your_orders`

## res.groups

- `sale.group_auto_done_setting`
- `sale.group_discount_per_so_line`
- `sale.group_warning_sale`
- `sale.group_proforma_sales`
- `sale.group_services_and_material`

## web_tour.tour

- `sale.sale_tour`

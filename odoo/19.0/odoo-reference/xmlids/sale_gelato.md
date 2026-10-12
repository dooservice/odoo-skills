# sale_gelato — XML ids

## delivery.carrier

- `sale_gelato.standard_delivery`
- `sale_gelato.express_delivery`

## ir.ui.view

- `sale_gelato.delivery_carrier_form` — on delivery.carrier inherits delivery.view_delivery_carrier_form
- `sale_gelato.product_document_form` — on product.document
- `sale_gelato.product_product_normal_form` — on product.product inherits product.product_normal_form_view
- `sale_gelato.product_product_easy_form` — on product.product inherits product.product_variant_easy_edit_view
- `sale_gelato.product_template_form` — on product.template inherits product.product_template_only_form_view
- `sale_gelato.res_config_settings_form` — on res.config.settings inherits sale.res_config_settings_view_form

## mail.template

- `sale_gelato.order_status_update`

## product.product

- `sale_gelato.standard_delivery_product`
- `sale_gelato.express_delivery_product`

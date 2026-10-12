# product — XML ids

## decimal.precision

- `product.decimal_price`
- `product.decimal_discount`
- `product.decimal_stock_weight`
- `product.decimal_volume`

## ir.actions.act_window

- `product.action_open_label_layout`
- `product.product_tag_action`
- `product.product_variant_edit_qty_action`
- `product.product_template_action_all`
- `product.product_variant_action`
- `product.attribute_action`
- `product.base_unit_action`
- `product.product_category_action_form`
- `product.product_pricelist_action2`
- `product.product_pricelist_item_action`
- `product.product_supplierinfo_type_action`
- `product.product_template_action`
- `product.product_uom_action_view_list`

## ir.actions.report

- `product.action_report_product_label_pdf`
- `product.action_report_pricelist`
- `product.action_report_product_label_dymo`
- `product.report_product_template_label_zpl`

## ir.actions.server

- `product.action_product_print_labels`
- `product.action_product_price_list_report`
- `product.action_product_template_print_labels`
- `product.action_product_template_price_list_report`
- `product.action_product_uom_print_labels`

## ir.ui.view

- `product.product_label_layout_form` — on product.label.layout
- `product.update_product_attribute_value_form` — on update.product.attribute.value
- `product.product_tag_form_view` — on product.tag
- `product.product_tag_tree_view` — on product.tag
- `product.product_view_list_qty` — on product.product
- `product.product_template_form_view` — on product.template
- `product.product_template_search_view` — on product.template
- `product.product_search_form_view` — on product.product inherits product.product_template_search_view
- `product.product_product_tree_view` — on product.product
- `product.product_template_view_tree_tag` — on product.template
- `product.product_normal_form_view` — on product.product inherits product.product_template_form_view
- `product.product_product_view_form_normalized` — on product.product
- `product.product_kanban_view` — on product.product
- `product.product_product_view_activity` — on product.product
- `product.product_view_kanban_catalog` — on product.product
- `product.product_view_search_catalog` — on product.product
- `product.res_config_settings_view_form` — on res.config.settings inherits base_setup.res_config_settings_view_form
- `product.attribute_tree_view` — on product.attribute
- `product.product_attribute_view_form` — on product.attribute
- `product.product_template_attribute_line_form` — on product.template.attribute.line
- `product.product_template_attribute_value_view_tree` — on product.template.attribute.value
- `product.product_template_attribute_value_view_form` — on product.template.attribute.value
- `product.product_template_attribute_value_view_search` — on product.template.attribute.value
- `product.product_attribute_search` — on product.attribute
- `product.product_attribute_value_list` — on product.attribute.value
- `product.product_attribute_value_form` — on product.attribute.value
- `product.product_category_form_view` — on product.category
- `product.product_category_list_view` — on product.category
- `product.product_category_search_view` — on product.category
- `product.product_combo_view_form` — on product.combo
- `product.product_combo_view_tree` — on product.combo
- `product.product_document_form` — on product.document
- `product.product_document_kanban` — on product.document
- `product.product_document_list` — on product.document
- `product.product_document_search` — on product.document
- `product.product_pricelist_item_view_search` — on product.pricelist.item
- `product.product_pricelist_item_tree_view` — on product.pricelist.item
- `product.product_pricelist_item_tree_view_from_product` — on product.pricelist.item
- `product.product_pricelist_item_form_view` — on product.pricelist.item
- `product.product_pricelist_item_product_template_form_view` — on product.pricelist.item inherits product.product_pricelist_item_form_view
- `product.product_pricelist_item_product_product_form_view` — on product.pricelist.item inherits product.product_pricelist_item_product_template_form_view
- `product.product_pricelist_item_form_multi_create` — on product.pricelist.item inherits product.product_pricelist_item_form_view
- `product.product_pricelist_item_calendar` — on product.pricelist.item
- `product.product_pricelist_view_search` — on product.pricelist
- `product.product_pricelist_view_tree` — on product.pricelist
- `product.product_pricelist_view_kanban` — on product.pricelist
- `product.product_pricelist_view` — on product.pricelist
- `product.product_supplierinfo_form_view` — on product.supplierinfo
- `product.product_supplierinfo_search_view` — on product.supplierinfo
- `product.product_supplierinfo_view_kanban` — on product.supplierinfo
- `product.product_supplierinfo_tree_view` — on product.supplierinfo
- `product.product_template_attribute_line_view_tree` — on product.template.attribute.line
- `product.product_template_tree_view` — on product.template
- `product.product_template_list_view_sellable` — on product.template inherits product.product_template_tree_view
- `product.product_template_list_view_purchasable` — on product.template inherits product.product_template_tree_view
- `product.product_template_only_form_view` — on product.template inherits product.product_template_form_view
- `product.product_template_kanban_view` — on product.template
- `product.product_template_view_activity` — on product.template
- `product.inherits_website_sale_country_group_form` — on res.country.group inherits base.view_country_group_form
- `product.view_partner_property_form` — on res.partner inherits base.view_partner_form
- `product.product_uom_view_form` — on product.uom
- `product.product_uom_list_view` — on product.uom
- `product.uom_uom_view_form` — on uom.uom inherits uom.uom_uom_view_form
- `product.report_label_contour_marks`
- `product.report_label_barcode`
- `product.report_label_value_block`
- `product.barcode_2x7_label`
- `product.qr_2x7_label`
- `product.barcode_4x7_label`
- `product.qr_4x7_label`
- `product.barcode_4x12_label`
- `product.qr_4x12_label`
- `product.barcode_dymo_label`
- `product.qr_dymo_label`
- `product.report_productlabel_pdf`
- `product.report_productlabel_dymo`
- `product.barcode_normal_label`
- `product.qr_normal_label`
- `product.barcode_alternative_label`
- `product.qr_alternative_label`
- `product.barcode_small_label`
- `product.qr_small_label`
- `product.barcode_jewelry_label`
- `product.qr_jewelry_label`
- `product.report_productlabel_zpl`
- `product.report_product_label_pdf`
- `product.report_product_label_dymo`
- `product.report_product_label_zpl`
- `product.report_pricelist_page`
- `product.report_pricelist`

## product.attribute

- `product.pa_brand`
- `product.pa_size`
- `product.pa_color`
- `product.pa_material`
- `product.pa_pattern`

## product.category

- `product.product_category_goods`
- `product.product_category_expenses`
- `product.product_category_services`

## report.paperformat

- `product.paperformat_label_sheet`
- `product.paperformat_label_sheet_dymo`

## res.groups

- `product.group_product_pricelist`
- `product.group_product_variant`
- `product.group_product_manager`
- `product.group_show_uom_price`

## res.groups.privilege

- `product.res_groups_privilege_product`

## res.users

- `base.user_admin`

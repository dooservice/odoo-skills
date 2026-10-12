# product — Products & Pricelists

Depends on: base, mail, uom.

## `ir.attachment` (extends)


Public methods: `create`

## `product.attribute` (defines)

Product Attribute

- `name` Char “Attribute” (required)
- `active` Boolean
- `create_variant` Selection “Variant Creation” (required)
- `display_type` Selection (required)
- `sequence` Integer “Sequence” (index)
- `value_ids` One2many → `product.attribute.value` “Values”
- `template_value_ids` One2many → `product.template.attribute.value` “Template Values”
- `attribute_line_ids` One2many → `product.template.attribute.line` “Lines”
- `product_tmpl_ids` Many2many → `product.template` “Related Products” (store, compute=_compute_products)
- `number_related_products` Integer (compute=_compute_number_related_products)

Public methods: `action_archive`, `action_open_product_template_attribute_lines`, `write`

## `product.attribute.custom.value` (defines)

Product Attribute Custom Value

- `name` Char “Name” (compute=_compute_name)
- `custom_product_template_attribute_value_id` Many2one → `product.template.attribute.value` “Attribute Value” (required)
- `custom_value` Char “Custom Value”

## `product.attribute.value` (defines)

Attribute Value

- `name` Char “Value” (required)
- `sequence` Integer “Sequence” (index)
- `attribute_id` Many2one → `product.attribute` “Attribute” (required, index)
- `pav_attribute_line_ids` Many2many → `product.template.attribute.line` “Lines”
- `default_extra_price` Float
- `is_custom` Boolean “Free text”
- `html_color` Char “Color”
- `display_type` Selection (related=attribute_id.display_type)
- `color` Integer “Color Index”
- `image` Image “Image”
- `active` Boolean
- `is_used_on_products` Boolean “Used on Products” (compute=_compute_is_used_on_products)
- `default_extra_price_changed` Boolean (compute=_compute_default_extra_price_changed)

Public methods: `action_add_to_products`, `action_update_prices`, `check_is_used_on_products`, `unlink`, `write`

Extension points: `_get_default_color`

## `product.catalog.mixin` (defines)

Product Catalog Mixin


Public methods: `action_add_from_catalog`

Extension points: `_get_action_add_from_catalog_extra_context`, `_get_product_catalog_domain`, `_get_product_catalog_order_data`, `_get_product_catalog_order_line_info`, `_get_product_catalog_record_lines`

## `product.category` (defines)

Product Category

Inherits: `mail.thread`

- `name` Char “Name” (required)
- `complete_name` Char “Complete Name” (store, compute=_compute_complete_name)
- `parent_id` Many2one → `product.category` (index)
- `parent_path` Char (index)
- `child_id` One2many → `product.category`
- `product_count` Integer “# Products” (compute=_compute_product_count)
- `product_properties_definition` PropertiesDefinition “Product Properties”

Public methods: `copy_data`, `name_create`

Extension points: `_check_category_recursion`

## `product.combo` (defines)

Product Combo

- `name` Char “Name” (required)
- `sequence` Integer
- `company_id` Many2one → `res.company` “Company” (index)
- `combo_item_ids` One2many → `product.combo.item`
- `combo_item_count` Integer “Product Count” (compute=_compute_combo_item_count)
- `currency_id` Many2one → `res.currency` (compute=_compute_currency_id)
- `base_price` Float “Combo Price” (compute=_compute_base_price)

Extension points: `_check_combo_item_ids_no_duplicates`, `_check_combo_item_ids_not_empty`, `_check_company_id`

## `product.combo.item` (defines)

Product Combo Item

- `company_id` Many2one (store, related=combo_id.company_id)
- `combo_id` Many2one → `product.combo` (required, index)
- `product_id` Many2one → `product.product` “Options” (required)
- `currency_id` Many2one → `res.currency` (related=product_id.currency_id)
- `lst_price` Float “Original Price” (related=product_id.lst_price)
- `extra_price` Float “Extra Price”

Extension points: `_check_product_id_no_combo`

## `product.document` (defines)

Product Document

- `ir_attachment_id` Many2one → `ir.attachment` “Related attachment” (required)
- `active` Boolean
- `sequence` Integer

Public methods: `copy_data`, `create`, `unlink`

## `product.pricelist` (defines)

Pricelist

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Pricelist Name” (required)
- `active` Boolean “Active”
- `sequence` Integer
- `currency_id` Many2one → `res.currency` (required)
- `company_id` Many2one → `res.company`
- `country_group_ids` Many2many → `res.country.group` “Country Groups”
- `item_ids` One2many → `product.pricelist.item` “Pricelist Rules”

Public methods: `action_open_pricelist_report`, `copy_data`, `get_import_templates`, `write`

Extension points: `_get_applicable_rules`, `_get_applicable_rules_domain`, `_get_country_pricelist_multi`, `_get_partner_pricelist_multi`, `_get_partner_pricelist_multi_filter_hook`, `_get_partner_pricelist_multi_search_domain_hook`, `_get_product_price`, `_get_product_price_rule`, `_get_product_rule`, `_get_products_price`

## `product.pricelist.item` (defines)

Pricelist Rule

- `pricelist_id` Many2one → `product.pricelist` “Pricelist” (index)
- `is_pricelist_required` Boolean (compute=_compute_is_pricelist_required)
- `company_id` Many2one → `res.company` (store, compute=_compute_company_id)
- `currency_id` Many2one → `res.currency` (store, compute=_compute_currency_id)
- `date_start` Datetime “Start Date”
- `date_end` Datetime “End Date”
- `min_quantity` Float “Min. Quantity”
- `applied_on` Selection “Apply On” (required)
- `display_applied_on` Selection (required)
- `categ_id` Many2one → `product.category` “Category”
- `product_tmpl_id` Many2one → `product.template` “Product”
- `product_id` Many2one → `product.product` “Variant”
- `product_uom_name` Char (related=product_tmpl_id.uom_name)
- `product_variant_count` Integer (related=product_tmpl_id.product_variant_count)
- `base` Selection “Based on” (required)
- `base_pricelist_id` Many2one → `product.pricelist`
- `compute_price` Selection (required, index)
- `fixed_price` Float “Fixed Price”
- `percent_price` Float “Percentage Price”
- `price_discount` Float “Price Discount”
- `price_round` Float “Price Rounding”
- `price_surcharge` Float “Extra Fee”
- `price_markup` Float “Markup” (store, compute=_compute_price_markup)
- `price_min_margin` Float “Min. Price Margin”
- `price_max_margin` Float “Max. Price Margin”
- `name` Char “Name” (compute=_compute_name)
- `price` Char “Price” (compute=_compute_price_label)
- `rule_tip` Char (compute=_compute_rule_tip)

Public methods: `create`, `write`

Extension points: `_check_base_pricelist_id`, `_check_date_range`, `_check_margin`, `_check_pricelist_recursion`, `_check_product_consistency`, `_get_displayed_discount`, `_get_integer`, `_get_price_label_base_str`

## `product.product` (defines)

Product Variant

Inherits: `mail.thread`, `mail.activity.mixin`

- `price_extra` Float “Variant Price Extra” (compute=_compute_product_price_extra)
- `lst_price` Float “Sales Price” (compute=_compute_product_lst_price)
- `default_code` Char “Internal Reference” (index)
- `code` Char “Reference” (compute=_compute_product_code)
- `partner_ref` Char “Customer Ref” (compute=_compute_partner_ref)
- `active` Boolean “Active”
- `product_tmpl_id` Many2one → `product.template` (required, index)
- `barcode` Char “Barcode”
- `product_uom_ids` One2many → `product.uom` (store)
- `product_template_attribute_value_ids` Many2many → `product.template.attribute.value` “Attribute Values”
- `product_template_variant_value_ids` Many2many → `product.template.attribute.value` “Variant Values”
- `import_attribute_values` Char “Product Values” (compute=_compute_import_attribute_values)
- `combination_indices` Char (store, index, compute=_compute_combination_indices)
- `is_product_variant` Boolean (compute=_compute_is_product_variant)
- `standard_price` Float “Cost” (company_dependent)
- `volume` Float “Volume”
- `weight` Float “Weight”
- `pricelist_rule_ids` One2many → `product.pricelist.item` “Pricelist Rules” (compute=_compute_pricelist_rule_ids)
- `product_document_ids` One2many → `product.document` “Documents”
- `product_document_count` Integer “Documents Count” (compute=_compute_product_document_count)
- `additional_product_tag_ids` Many2many → `product.tag` “Variant Tags”
- `all_product_tag_ids` Many2many → `product.tag` (compute=_compute_all_product_tag_ids)
- `image_variant_1920` Image “Variant Image”
- `image_variant_1024` Image “Variant Image 1024” (store, related=image_variant_1920)
- `image_variant_512` Image “Variant Image 512” (store, related=image_variant_1920)
- `image_variant_256` Image “Variant Image 256” (store, related=image_variant_1920)
- `image_variant_128` Image “Variant Image 128” (store, related=image_variant_1920)
- `can_image_variant_1024_be_zoomed` Boolean “Can Variant Image 1024 be zoomed” (store, compute=_compute_can_image_variant_1024_be_zoomed)
- `image_1920` Image “Image” (compute=_compute_image_1920)
- `image_1024` Image “Image 1024” (compute=_compute_image_1024)
- `image_512` Image “Image 512” (compute=_compute_image_512)
- `image_256` Image “Image 256” (compute=_compute_image_256)
- `image_128` Image “Image 128” (compute=_compute_image_128)
- `can_image_1024_be_zoomed` Boolean “Can Image 1024 be zoomed” (compute=_compute_can_image_1024_be_zoomed)
- `write_date` Datetime (store, compute=_compute_write_date)
- `is_favorite` Boolean (store, related=product_tmpl_id.is_favorite)
- `is_in_selected_section_of_order` Boolean

Public methods: `action_archive`, `action_open_documents`, `action_open_label_layout`, `action_unarchive`, `copy`, `create`, `get_contextual_price`, `get_empty_list_help`, `get_product_multiline_description_sale`, `load`, `name_search`, `open_product_template`, `unlink`, `view_header_get`, `write`

Extension points: `_check_barcode_uniqueness`, `_check_company_id`, `_check_duplicated_packaging_barcodes`, `_check_duplicated_product_barcodes`, `_get_attributes_extra_price`, `_get_barcode_search_domain`, `_get_barcodes_by_company`, `_get_contextual_discount`, `_get_contextual_price`, `_get_filtered_sellers`, `_get_invoice_policy`, `_get_no_variant_attributes_price_extra`, `_get_placeholder_filename`, `_get_product_placeholder_filename`, `_get_product_price_context`, `_prepare_sellers`

## `product.supplierinfo` (defines)

Supplier Pricelist

- `partner_id` Many2one → `res.partner` (required)
- `product_name` Char “Vendor Product Name”
- `product_code` Char “Vendor Product Code”
- `sequence` Integer “Sequence”
- `product_uom_id` Many2one → `uom.uom` (required, store, compute=_compute_product_uom_id)
- `min_qty` Float “Quantity” (required)
- `price` Float “Unit Price”
- `price_discounted` Float “Discounted Price” (compute=_compute_price_discounted)
- `company_id` Many2one → `res.company`
- `currency_id` Many2one → `res.currency` (required)
- `date_start` Date “Start Date”
- `date_end` Date “End Date”
- `product_id` Many2one → `product.product` (store, compute=_compute_product_id)
- `product_tmpl_id` Many2one → `product.template` (required, store, index, compute=_compute_product_tmpl_id)
- `product_variant_count` Integer “Variant Count” (related=product_tmpl_id.product_variant_count)
- `delay` Integer “Lead Time” (required)
- `discount` Float “Discount (%)”

Public methods: `create`, `get_import_templates`, `write`

Extension points: `_get_filtered_supplier`

## `product.tag` (defines)

Product Tag

- `name` Char “Name” (required)
- `sequence` Integer
- `color` Char “Color”
- `product_template_ids` Many2many → `product.template` “Product Templates”
- `product_product_ids` Many2many → `product.product` “Product Variants”
- `product_ids` Many2many → `product.product` “All Product Variants using this Tag” (compute=_compute_product_ids)
- `visible_to_customers` Boolean “Visible to customers”
- `image` Image “Image”

Public methods: `copy_data`

Extension points: `_get_default_template_id`, `_get_default_variant_id`

## `product.template` (defines)

Product

Inherits: `mail.thread`, `mail.activity.mixin`, `image.mixin`

- `name` Char “Name” (required)
- `sequence` Integer “Sequence”
- `description` Html “Description”
- `description_purchase` Text “Purchase Description”
- `description_sale` Text “Sales Description”
- `type` Selection “Product Type” (required)
- `combo_ids` Many2many → `product.combo` “Combo Choices”
- `service_tracking` Selection “Create on Order” (required, store, compute=_compute_service_tracking)
- `categ_id` Many2one → `product.category` “Product Category”
- `currency_id` Many2one → `res.currency` (compute=_compute_currency_id)
- `cost_currency_id` Many2one → `res.currency` (compute=_compute_cost_currency_id)
- `list_price` Float “Sales Price”
- `standard_price` Float “Cost” (compute=_compute_standard_price)
- `volume` Float “Volume” (store, compute=_compute_volume)
- `volume_uom_name` Char “Volume unit of measure label” (compute=_compute_volume_uom_name)
- `weight` Float “Weight” (store, compute=_compute_weight)
- `weight_uom_name` Char “Weight unit of measure label” (compute=_compute_weight_uom_name)
- `sale_ok` Boolean “Sales”
- `purchase_ok` Boolean “Purchase” (store, compute=_compute_purchase_ok)
- `uom_id` Many2one → `uom.uom` (required)
- `uom_ids` Many2many → `uom.uom` “Packagings”
- `uom_name` Char “Unit Name” (readonly, related=uom_id.name)
- `company_id` Many2one → `res.company` (index)
- `seller_ids` One2many → `product.supplierinfo`
- `variant_seller_ids` One2many → `product.supplierinfo`
- `active` Boolean “Active”
- `color` Integer “Color Index”
- `is_product_variant` Boolean “Is a product variant” (compute=_compute_is_product_variant)
- `attribute_line_ids` One2many → `product.template.attribute.line`
- `valid_product_template_attribute_line_ids` Many2many → `product.template.attribute.line` “Valid Product Attribute Lines” (compute=_compute_valid_product_template_attribute_line_ids)
- `import_attribute_values` Char “Product Values” (compute=_compute_import_attribute_values)
- `product_variant_ids` One2many → `product.product` (required)
- `product_variant_id` Many2one → `product.product` (compute=_compute_product_variant_id)
- `product_variant_count` Integer “# Product Variants” (compute=_compute_product_variant_count)
- `barcode` Char “Barcode” (compute=_compute_barcode)
- `default_code` Char “Internal Reference” (store, compute=_compute_default_code)
- `pricelist_rule_ids` One2many → `product.pricelist.item` “Pricelist Rules”
- `product_document_ids` One2many → `product.document` “Documents”
- `product_document_count` Integer “Documents Count” (compute=_compute_product_document_count)
- `can_image_1024_be_zoomed` Boolean “Can Image 1024 be zoomed” (store, compute=_compute_can_image_1024_be_zoomed)
- `has_configurable_attributes` Boolean “Is a configurable product” (store, compute=_compute_has_configurable_attributes)
- `is_dynamically_created` Boolean “Is Dynamically Created” (compute=_compute_is_dynamically_created)
- `product_tooltip` Char (compute=_compute_product_tooltip)
- `is_favorite` Boolean “Favorite”
- `product_tag_ids` Many2many → `product.tag` “Tags”
- `product_properties` Properties “Properties”

Public methods: `action_open_documents`, `action_open_label_layout`, `copy`, `copy_data`, `create`, `default_get`, `get_contextual_price`, `get_empty_list_help`, `get_import_templates`, `get_single_product_variant`, `has_dynamic_attributes`, `load`, `name_search`, `write`

Extension points: `_check_barcode_uniqueness`, `_check_combo_ids_not_empty`, `_check_sale_combo_ids`, `_create_first_product_variant`, `_create_product_variant`, `_create_variant_ids`, `_get_attribute_exclusions`, `_get_attributes_extra_price`, `_get_available_uoms`, `_get_closest_possible_combination`, `_get_closest_possible_combinations`, `_get_contextual_price`, `_get_contextual_pricelist`, `_get_default_uom_id`, `_get_first_possible_combination`, `_get_first_possible_variant_id`, `_get_length_uom_id_from_ir_config_parameter`, `_get_length_uom_name_from_ir_config_parameter`, `_get_list_price`, `_get_mapped_attribute_names`, `_get_own_attribute_exclusions`, `_get_parent_attribute_exclusions`, `_get_placeholder_filename`, `_get_possible_combinations`, `_get_possible_variants`, `_get_product_document_domain`, `_get_product_placeholder_filename`, `_get_product_price_context`, `_get_related_fields_variant_template`, `_get_variant_for_combination`, `_get_variant_id_for_combination`, `_get_volume_uom_id_from_ir_config_parameter`, `_get_volume_uom_name_from_ir_config_parameter`, `_get_weight_uom_id_from_ir_config_parameter`, `_get_weight_uom_name_from_ir_config_parameter`, `_prepare_tooltip`, `_prepare_variant_values`

## `product.template.attribute.exclusion` (defines)

Product Template Attribute Exclusion

- `product_template_attribute_value_id` Many2one → `product.template.attribute.value` “Attribute Value” (index)
- `product_tmpl_id` Many2one → `product.template` “Product Template” (required, index)
- `value_ids` Many2many → `product.template.attribute.value` “Attribute Values”

Public methods: `create`, `unlink`, `write`

## `product.template.attribute.line` (defines)

Product Template Attribute Line

- `active` Boolean
- `product_tmpl_id` Many2one → `product.template` “Product Template” (required, index)
- `sequence` Integer “Sequence”
- `attribute_id` Many2one → `product.attribute` “Attribute” (required, index)
- `value_ids` Many2many → `product.attribute.value` “Values”
- `value_count` Integer (store, compute=_compute_value_count)
- `product_template_value_ids` One2many → `product.template.attribute.value` “Product Attribute Values”

Public methods: `action_open_attribute_values`, `create`, `unlink`, `write`

Extension points: `_check_valid_values`

## `product.template.attribute.value` (defines)

Product Template Attribute Value

- `ptav_active` Boolean “Active”
- `name` Char “Value” (related=product_attribute_value_id.name)
- `product_attribute_value_id` Many2one → `product.attribute.value` “Attribute Value” (required, index)
- `attribute_line_id` Many2one → `product.template.attribute.line` (required, index)
- `price_extra` Float “Extra Price”
- `currency_id` Many2one (related=attribute_line_id.product_tmpl_id.currency_id)
- `exclude_for` One2many → `product.template.attribute.exclusion` “Exclude for”
- `product_tmpl_id` Many2one (store, index, related=attribute_line_id.product_tmpl_id)
- `attribute_id` Many2one (store, index, related=attribute_line_id.attribute_id)
- `ptav_product_variant_ids` Many2many → `product.product` “Related Variants” (readonly)
- `html_color` Char “HTML Color Index” (related=product_attribute_value_id.html_color)
- `is_custom` Boolean (related=product_attribute_value_id.is_custom)
- `display_type` Selection (related=product_attribute_value_id.display_type)
- `color` Integer “Color”
- `image` Image (related=product_attribute_value_id.image)

Public methods: `create`, `unlink`, `write`

Extension points: `_check_valid_values`, `_get_combination_name`, `_get_default_color`

## `product.uom` (defines)

Link between products and their UoMs

- `uom_id` Many2one → `uom.uom` (required, index)
- `product_id` Many2one → `product.product` (required, index)
- `barcode` Char (required)
- `company_id` Many2one → `res.company`

Extension points: `_check_barcode_uniqueness`

## `res.company` (extends)


Public methods: `create`, `write`

Extension points: `_get_default_pricelist_vals`

## `res.config.settings` (extends)

- `group_uom` Boolean “Units of Measure & Packagings”
- `group_product_variant` Boolean “Variants”
- `module_loyalty` Boolean “Promotions, Coupons, Gift Card & Loyalty Program”
- `group_product_pricelist` Boolean “Pricelists”
- `product_weight_in_lbs` Selection
- `product_volume_volume_in_cubic_feet` Selection

Public methods: `set_values`

## `res.country.group` (extends)

- `pricelist_ids` Many2many → `product.pricelist` “Pricelists”

## `res.currency` (extends)


Public methods: `write`

## `res.partner` (extends)

- `property_product_pricelist` Many2one → `product.pricelist` “Pricelist” (compute=_compute_product_pricelist)
- `specific_property_product_pricelist` Many2one → `product.pricelist` (company_dependent)

## `uom.uom` (extends)

- `product_uom_ids` One2many → `product.uom` “Barcodes”

Public methods: `action_open_packaging_barcodes`

## `report.product.report_producttemplatelabel2x7` (defines)

Product Label Report 2x7


Extension points: `_get_report_values`

## `report.product.report_producttemplatelabel4x7` (defines)

Product Label Report 4x7


Extension points: `_get_report_values`

## `report.product.report_producttemplatelabel4x12` (defines)

Product Label Report 4x12


Extension points: `_get_report_values`

## `report.product.report_producttemplatelabel4x12noprice` (defines)

Product Label Report 4x12 No Price


Extension points: `_get_report_values`

## `report.product.report_producttemplatelabel_dymo` (defines)

Product Label Report


Extension points: `_get_report_values`

## `report.product.report_pricelist` (defines)

Pricelist Report


Public methods: `get_html`

Extension points: `_get_product_data`, `_get_report_data`, `_get_report_values`

## `product.label.layout` (defines)

Choose the sheet layout to print the labels

- `print_format` Selection “Format” (required)
- `custom_quantity` Integer “Copies” (required)
- `product_ids` Many2many → `product.product`
- `product_tmpl_ids` Many2many → `product.template`
- `extra_html` Html “Extra Content”
- `rows` Integer (compute=_compute_dimensions)
- `columns` Integer (compute=_compute_dimensions)
- `pricelist_id` Many2one → `product.pricelist` “Pricelist”

Public methods: `process`

Extension points: `_prepare_report_data`

## `update.product.attribute.value` (defines)

Update product attribute value

- `attribute_value_id` Many2one → `product.attribute.value` (required)
- `mode` Selection
- `message` Char (compute=_compute_message)
- `product_count` Integer (compute=_compute_product_count)

Public methods: `action_confirm`

# purchase_product_matrix — Purchase Matrix

Depends on: purchase, product_matrix.

## `purchase.order` (extends)

- `report_grids` Boolean “Print Variant Grids”
- `grid_product_tmpl_id` Many2one → `product.template`
- `grid_update` Boolean
- `grid` Char

Public methods: `get_report_matrixes`

Extension points: `_get_matrix`

## `purchase.order.line` (extends)

- `product_template_id` Many2one → `product.template` “Product Template” (related=product_id.product_tmpl_id)
- `is_configurable_product` Boolean “Is the product configurable?” (related=product_template_id.has_configurable_attributes)
- `product_template_attribute_value_ids` Many2many (readonly, related=product_id.product_template_attribute_value_ids)
- `product_no_variant_attribute_value_ids` Many2many → `product.template.attribute.value` “Product attribute values that do not create variants”

Extension points: `_get_product_purchase_description`

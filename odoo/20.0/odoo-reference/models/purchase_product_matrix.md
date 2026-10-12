# purchase_product_matrix — Purchase Matrix

Depends on: purchase, product_matrix.

## `purchase.order` (extends)

- `grid_product_tmpl_id` Many2one → `product.template`
- `grid_update` Boolean
- `grid` Char

Public methods: `get_report_matrixes`

Extension points: `_get_matrix`

## `purchase.order.line` (extends)

- `product_template_id` Many2one → `product.template` “Product Template” (related=product_id.product_tmpl_id)
- `is_configurable_product` Boolean “Is the product configurable?” (related=product_template_id.has_configurable_attributes)
- `product_template_attribute_value_ids` Many2many (readonly, related=product_id.product_template_attribute_value_ids)

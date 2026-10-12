# sale_product_matrix — Sale Matrix

Depends on: sale, product_matrix, sale_product_configurator.

## `product.template` (extends)

- `product_add_mode` Selection “Add product mode”

Public methods: `get_single_product_variant`

## `sale.order` (extends)

- `report_grids` Boolean “Print Variant Grids”
- `grid_product_tmpl_id` Many2one → `product.template`
- `grid_update` Boolean
- `grid` Char “Matrix local storage”

Public methods: `get_report_matrixes`

Extension points: `_get_matrix`

## `sale.order.line` (extends)

- `product_add_mode` Selection (related=product_template_id.product_add_mode)

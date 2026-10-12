# sale_product_configurator — Sale Product Configurator

Depends on: sale.

## `product.template` (extends)

- `optional_product_ids` Many2many → `product.template` “Optional Products”

Public methods: `get_single_product_variant`

## `sale.order.line` (extends)

- `is_configurable_product` Boolean “Is the product configurable?” (related=product_template_id.has_configurable_attributes)
- `product_template_attribute_value_ids` Many2many (related=product_id.product_template_attribute_value_ids)

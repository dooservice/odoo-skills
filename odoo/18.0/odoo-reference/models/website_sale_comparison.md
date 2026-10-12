# website_sale_comparison — Product Comparison

Depends on: website_sale.

## `product.attribute` (extends)

- `category_id` Many2one → `product.attribute.category` “eCommerce Category” (index)

## `product.attribute.category` (defines)

Product Attribute Category

- `name` Char “Category Name” (required)
- `sequence` Integer “Sequence” (index)
- `attribute_ids` One2many → `product.attribute` “Related Attributes”

## `product.product` (extends)


Extension points: `_prepare_categories_for_display`

## `product.template.attribute.line` (extends)


Extension points: `_prepare_categories_for_display`

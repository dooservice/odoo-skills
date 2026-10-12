# product_margin — Margins by Products

Depends on: account.

## `product.product` (extends)

- `date_from` Date “Margin Date From” (compute=_compute_product_margin_fields_values)
- `date_to` Date “Margin Date To” (compute=_compute_product_margin_fields_values)
- `invoice_state` Selection “Invoice State” (readonly, compute=_compute_product_margin_fields_values)
- `sale_avg_price` Float “Avg. Sale Unit Price” (compute=_compute_product_margin_fields_values)
- `purchase_avg_price` Float “Avg. Purchase Unit Price” (compute=_compute_product_margin_fields_values)
- `sale_num_invoiced` Float “# Invoiced in Sale” (compute=_compute_product_margin_fields_values)
- `purchase_num_invoiced` Float “# Invoiced in Purchase” (compute=_compute_product_margin_fields_values)
- `sales_gap` Float “Sales Gap” (compute=_compute_product_margin_fields_values)
- `purchase_gap` Float “Purchase Gap” (compute=_compute_product_margin_fields_values)
- `turnover` Float “Turnover” (compute=_compute_product_margin_fields_values)
- `total_cost` Float “Total Cost” (compute=_compute_product_margin_fields_values)
- `sale_expected` Float “Expected Sale” (compute=_compute_product_margin_fields_values)
- `normal_cost` Float “Normal Cost” (compute=_compute_product_margin_fields_values)
- `total_margin` Float “Total Margin” (compute=_compute_product_margin_fields_values)
- `expected_margin` Float “Expected Margin” (compute=_compute_product_margin_fields_values)
- `total_margin_rate` Float “Total Margin Rate(%)” (compute=_compute_product_margin_fields_values)
- `expected_margin_rate` Float “Expected Margin (%)” (compute=_compute_product_margin_fields_values)

Public methods: `read_group`

## `product.margin` (defines)

Product Margin

- `from_date` Date “From”
- `to_date` Date “To”
- `invoice_state` Selection (required)

Public methods: `action_open_window`

# sale_quotation_builder — Quotation Builder

Depends on: website, sale_management, website_mail.

## `product.template` (extends)

- `quotation_only_description` Html “Quotation Only Description”
- `quotation_description` Html “Quotation Description” (compute=_compute_quotation_description)

## `res.company` (extends)


## `sale.order` (extends)

- `website_description` Html “Website Description” (store, compute=_compute_website_description)

## `sale.order.line` (extends)

- `website_description` Html “Website Description” (store, compute=_compute_website_description)

## `sale.order.option` (extends)

- `website_description` Html “Website Description” (store, compute=_compute_website_description)

Extension points: `_get_values_to_add_to_order`

## `sale.order.template` (extends)

- `website_description` Html “Website Description”

Public methods: `action_open_template`

## `sale.order.template.line` (extends)

- `website_description` Html “Website Description” (store, compute=_compute_website_description)

Extension points: `_prepare_order_line_values`

## `sale.order.template.option` (extends)

- `website_description` Html “Website Description” (store, compute=_compute_website_description)

Extension points: `_prepare_option_line_values`

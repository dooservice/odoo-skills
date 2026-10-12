# website_sale_digital — Digital Products

Depends on: attachment_indexation, website_sale.

## `account.move.line` (extends)


Public methods: `get_digital_purchases`

## `ir.attachment` (extends)

- `product_downloadable` Boolean “Downloadable from product portal”

## `product.template` (extends)

- `attachment_count` Integer “File” (compute=_compute_attachment_count)

Public methods: `action_open_attachments`

## `product.product` (extends)

- `attachment_count` Integer “File” (compute=_compute_attachment_count)

Public methods: `action_open_attachments`

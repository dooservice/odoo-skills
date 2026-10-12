# l10n_gcc_pos — Gulf Cooperation Council - Point of Sale

Depends on: point_of_sale, l10n_gcc_invoice.

## `pos.config` (extends)

- `l10n_gcc_dual_language_receipt` Boolean “GCC Formatted Receipts”

## `res.config.settings` (extends)

- `l10n_gcc_dual_language_receipt` Boolean (related=pos_config_id.l10n_gcc_dual_language_receipt)

## `pos.order.receipt` (extends)

Point of Sale Order Receipt Generator


Public methods: `order_receipt_generate_data`

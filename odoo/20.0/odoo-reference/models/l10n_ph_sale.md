# l10n_ph_sale — Philippines - Discount Privileges on Sale Orders

Depends on: l10n_ph_invoice, sale.

## `sale.order` (extends)

- `l10n_ph_has_discount_privilege` Boolean (compute=_compute_l10n_ph_has_discount_privilege)

Public methods: `action_open_discount_privilege_wizard`

## `sale.order.line` (extends)

Inherits: `l10n_ph.discount.privilege.line.mixin`

- `l10n_ph_original_tax_ids` Many2many

Extension points: `_prepare_invoice_line`

## `l10n_ph.discount.privilege.wizard` (extends)

- `order_id` Many2one → `sale.order` “Sale Order”

Public methods: `create`

Extension points: `_check_can_modify`, `_get_document_fields`

## `l10n_ph.discount.privilege.wizard.line` (extends)

- `sale_order_line_id` Many2one → `sale.order.line` “Sale Order Line”

Extension points: `_get_line_source`

## `sale.order.discount` (extends)


Extension points: `_get_discountable_order_lines`

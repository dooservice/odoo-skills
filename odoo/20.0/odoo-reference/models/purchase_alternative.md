# purchase_alternative — Purchase Alternative

Depends on: purchase.

## `purchase.order.group` (defines)

Technical model to group PO for call to tenders

- `order_ids` One2many → `purchase.order`

Public methods: `write`

## `purchase.order` (extends)

- `purchase_group_id` Many2one → `purchase.order.group`
- `alternative_po_ids` One2many → `purchase.order` “Alternative POs” (related=purchase_group_id.order_ids)

Public methods: `action_compare_alternative_lines`, `action_create_alternative`, `button_confirm`, `create`, `get_tender_best_lines`, `write`

## `purchase.order.line` (extends)

- `price_total_cc` Monetary “Company Subtotal” (store, compute=_compute_price_total_cc)
- `company_currency_id` Many2one “Company Currency” (related=company_id.currency_id)

Public methods: `action_choose`, `action_clear_quantities`

## `purchase.alternative.create` (defines)

Wizard to preset values for alternative PO

- `origin_po_id` Many2one → `purchase.order`
- `partner_ids` Many2many → `res.partner` “Vendor” (required)
- `purchase_warn_msg` Text “Warning Messages” (compute=_compute_purchase_warn_msg)
- `copy_products` Boolean “Copy Products”

Public methods: `action_create_alternative`

Extension points: `_get_alternative_line_value`, `_get_alternative_values`

## `purchase.alternative.warning` (defines)

Wizard in case PO still has open alternative requests for quotation

- `po_ids` Many2many → `purchase.order` “POs to Confirm”
- `alternative_po_ids` Many2many → `purchase.order` “Alternative POs”

Public methods: `action_cancel_alternatives`, `action_keep_alternatives`

Extension points: `_action_done`

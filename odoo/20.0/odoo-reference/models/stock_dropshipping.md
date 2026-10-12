# stock_dropshipping — Drop Shipping

Depends on: sale_purchase_stock.

## `account.move.line` (extends)


## `product.product` (extends)


Extension points: `_get_description`

## `purchase.order` (extends)

- `dropship_picking_count` Integer “Dropship Count” (compute=_compute_incoming_picking_count)

Public methods: `action_view_dropship`, `action_view_picking`

Extension points: `_create_picking`, `_get_allowed_picking_code`, `_prepare_reference_vals`

## `purchase.order.line` (extends)


## `res.company` (extends)


Public methods: `create_missing_dropship_picking_type`, `create_missing_dropship_rule`, `create_missing_dropship_sequence`

Extension points: `_create_dropship_picking_type`, `_create_dropship_rule`, `_create_dropship_sequence`, `_create_per_company_picking_types`, `_create_per_company_rules`, `_create_per_company_sequences`

## `sale.order` (extends)

- `dropship_picking_count` Integer “Dropship Count” (compute=_compute_picking_ids)

Public methods: `action_view_delivery`, `action_view_dropship`

## `sale.order.line` (extends)


Extension points: `_get_qty_procurement`

## `stock.rule` (extends)


Extension points: `_get_procurements_to_merge_groupby`, `_get_rule_domain`

## `stock.picking` (extends)

- `is_dropship` Boolean “Is a Dropship” (compute=_compute_is_dropship)

## `stock.picking.type` (extends)

- `code` Selection

## `stock.lot` (extends)


Extension points: `_get_outgoing_domain`

## `stock.move.line` (extends)


Extension points: `_action_done`, `_get_lot_partner`

## `stock.replenish.mixin` (extends)


Extension points: `_get_allowed_route_domain`

# mrp_subcontracting_dropshipping — Dropship and Subcontracting Management

Depends on: mrp_subcontracting, stock_dropshipping.

## `purchase.order` (extends)

- `default_location_dest_id_is_subcontracting_loc` Boolean (compute=_compute_default_location_dest_id_is_subcontracting_loc)

Public methods: `onchange_picking_type_id`

Extension points: `_get_destination_location`

## `res.company` (extends)

- `dropship_subcontractor_pick_type_id` Many2one → `stock.picking.type`

Extension points: `_create_missing_subcontracting_dropshipping_picking_type`, `_create_missing_subcontracting_dropshipping_rules`, `_create_missing_subcontracting_dropshipping_sequence`, `_create_per_company_picking_types`, `_create_per_company_rules`, `_create_per_company_sequences`, `_create_subcontracting_dropshipping_picking_type`, `_create_subcontracting_dropshipping_rules`, `_create_subcontracting_dropshipping_sequence`

## `stock.move` (extends)


Extension points: `_get_partner_id`, `_get_value_from_account_move`

## `stock.warehouse.orderpoint` (extends)


Extension points: `_prepare_procurement_values`

## `stock.picking` (extends)


Extension points: `_get_warehouse`, `_prepare_subcontract_mo_vals`

## `stock.replenish.mixin` (extends)


Extension points: `_get_allowed_route_domain`

## `stock.rule` (extends)


Extension points: `_prepare_purchase_order`

## `stock.warehouse` (extends)

- `subcontracting_dropshipping_pull_id` Many2one → `stock.rule`

Public methods: `create`, `update_global_route_dropship_subcontractor`, `write`

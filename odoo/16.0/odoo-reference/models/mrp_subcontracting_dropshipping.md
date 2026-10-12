# mrp_subcontracting_dropshipping — Dropship and Subcontracting Management

Depends on: mrp_subcontracting, stock_dropshipping.

## `purchase.order` (extends)

- `default_location_dest_id_is_subcontracting_loc` Boolean (related=picking_type_id.default_location_dest_id.is_subcontracting_location)

Public methods: `onchange_picking_type_id`

Extension points: `_get_destination_location`

## `res.company` (extends)

- `dropship_subcontractor_pick_type_id` Many2one → `stock.picking.type`

Extension points: `_create_missing_subcontracting_dropshipping_picking_type`, `_create_missing_subcontracting_dropshipping_rules`, `_create_missing_subcontracting_dropshipping_sequence`, `_create_per_company_picking_types`, `_create_per_company_rules`, `_create_per_company_sequences`, `_create_subcontracting_dropshipping_picking_type`, `_create_subcontracting_dropshipping_rules`, `_create_subcontracting_dropshipping_sequence`

## `stock.move` (extends)


Extension points: `_prepare_procurement_values`

## `stock.warehouse.orderpoint` (extends)


Extension points: `_prepare_procurement_values`

## `stock.picking` (extends)


Extension points: `_action_done`, `_get_warehouse`, `_prepare_subcontract_mo_vals`

## `stock.rule` (extends)


Extension points: `_prepare_purchase_order`

## `stock.warehouse` (extends)

- `subcontracting_dropshipping_to_resupply` Boolean “Dropship Subcontractors”
- `subcontracting_dropshipping_pull_id` Many2one → `stock.rule`

Public methods: `create`, `update_global_route_dropship_subcontractor`, `write`

Extension points: `_get_global_route_rules_values`

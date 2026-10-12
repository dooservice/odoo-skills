# mrp_subcontracting_purchase — Purchase and Subcontracting Management

Depends on: mrp_subcontracting, purchase_mrp.

## `purchase.order` (extends)

- `subcontracting_resupply_picking_count` Integer “Count of Subcontracting Resupply” (compute=_compute_subcontracting_resupply_picking_count)

Public methods: `action_view_subcontracting_resupply`

Extension points: `_get_mrp_productions`, `_get_subcontracting_resupplies`

## `stock.move` (extends)


## `stock.picking` (extends)

- `subcontracting_source_purchase_count` Integer “Number of subcontracting PO Source” (compute=_compute_subcontracting_source_purchase_count)

Public methods: `action_view_subcontracting_source_purchase`

Extension points: `_get_subcontracting_source_purchase`

## `report.mrp.report_bom_structure` (extends)

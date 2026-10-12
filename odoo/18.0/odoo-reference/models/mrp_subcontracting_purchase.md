# mrp_subcontracting_purchase — Purchase and Subcontracting Management

Depends on: mrp_subcontracting, purchase_mrp.

## `account.move.line` (extends)


Extension points: `_get_price_unit_val_dif_and_relevant_qty`, `_get_valued_in_moves`

## `purchase.order` (extends)

- `subcontracting_resupply_picking_count` Integer “Count of Subcontracting Resupply” (compute=_compute_subcontracting_resupply_picking_count)

Public methods: `action_view_subcontracting_resupply`

Extension points: `_get_mrp_productions`, `_get_subcontracting_resupplies`

## `stock.move` (extends)


## `stock.picking` (extends)

- `subcontracting_source_purchase_count` Integer “Number of subcontracting PO Source” (compute=_compute_subcontracting_source_purchase_count)

Public methods: `action_view_subcontracting_source_purchase`

Extension points: `_get_subcontracting_source_purchase`

## `stock.rule` (extends)


Extension points: `_get_lead_days`

## `stock.valuation.layer` (extends)


Extension points: `_get_layer_price_unit`

## `report.mrp.report_bom_structure` (extends)


Extension points: `_get_resupply_availability`

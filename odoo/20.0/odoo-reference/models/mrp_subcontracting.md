# mrp_subcontracting — MRP Subcontracting

Depends on: mrp.

## `mrp.bom` (extends)

- `type` Selection
- `subcontractor_ids` Many2many → `res.partner` “Subcontractors”

Extension points: `_check_subcontracting_no_operation`

## `mrp.production` (extends)

- `move_line_raw_ids` One2many → `stock.move.line` “Detail Component” (compute=_compute_move_line_raw_ids)
- `subcontractor_id` Many2one → `res.partner` “Subcontractor”
- `bom_product_ids` Many2many → `product.product` (compute=_compute_bom_product_ids)
- `incoming_picking` Many2one (related=move_finished_ids.move_dest_ids.picking_id)

Public methods: `action_merge`, `action_split_subcontracting`, `pre_button_mark_done`, `write`

Extension points: `_get_subcontract_move`, `_get_writeable_fields_portal_user`

## `mrp.production` (extends)


Public methods: `button_unbuild`

## `product.supplierinfo` (extends)

- `is_subcontractor` Boolean “Subcontracted” (compute=_compute_is_subcontractor)

## `product.product` (extends)


Extension points: `_prepare_sellers`

## `res.company` (extends)

- `subcontracting_location_id` Many2one → `stock.location`

Extension points: `_create_missing_subcontracting_location`, `_create_per_company_locations`, `_create_subcontracting_location`

## `res.partner` (extends)

- `property_stock_subcontractor` Many2one → `stock.location` “Subcontractor Location” (company_dependent)
- `is_subcontractor` Boolean “Subcontractor” (compute=_compute_is_subcontractor)
- `bom_ids` Many2many → `mrp.bom` “BoMs for which the Partner is one of the subcontractors” (compute=_compute_bom_ids)
- `production_ids` Many2many → `mrp.production` “MRP Productions for which the Partner is the subcontractor” (compute=_compute_production_ids)
- `picking_ids` Many2many → `stock.picking` “Stock Pickings for which the Partner is the subcontractor” (compute=_compute_picking_ids)

## `stock.location` (extends)

- `subcontractor_ids` One2many → `res.partner`

Public methods: `is_subcontract`

Extension points: `_check_access_putaway`, `_check_subcontracting_location`

## `stock.move` (extends)

- `is_subcontract` Boolean “The move is a subcontract receipt”
- `show_subcontracting_details_visible` Boolean (compute=_compute_show_subcontracting_details_visible)

Public methods: `action_show_details`, `action_show_subcontract_details`, `copy_data`, `create`, `write`

Extension points: `_action_cancel`, `_action_confirm`, `_check_access_if_subcontractor`, `_get_available_move_lines`, `_get_partner_id`, `_get_production_assignation_domain`, `_get_subcontract_bom`, `_get_subcontract_production`, `_prepare_move_split_vals`, `_prepare_procurement_values`

## `stock.move.line` (extends)


Public methods: `create`, `unlink`, `write`

## `stock.picking` (extends)

- `show_subcontracting_details_visible` Boolean (compute=_compute_show_subcontracting_details_visible)

Public methods: `action_show_subcontract_details`

Extension points: `_action_done`, `_get_subcontract_mo_confirmation_ctx`, `_get_subcontract_production`, `_get_warehouse`, `_prepare_return_move_default_values`, `_prepare_return_picking_default_values`, `_prepare_subcontract_mo_vals`

## `stock.quant` (extends)

- `is_subcontract` Boolean

## `stock.rule` (extends)


Extension points: `_get_moves_to_assign_domain`, `_get_stock_move_values`

## `stock.warehouse` (extends)

- `subcontracting_to_resupply` Boolean “Resupply Subcontractors”
- `subcontracting_mto_pull_id` Many2one → `stock.rule`
- `subcontracting_pull_id` Many2one → `stock.rule`
- `subcontracting_route_id` Many2one → `stock.route`
- `subcontracting_type_id` Many2one → `stock.picking.type`
- `subcontracting_resupply_type_id` Many2one → `stock.picking.type`

Public methods: `create`, `get_rules_dict`, `write`

Extension points: `_get_picking_type_create_values`, `_get_picking_type_update_values`, `_get_routes_values`, `_get_sequence_values`, `_get_subcontracting_location`, `_get_subcontracting_locations`

## `report.mrp.report_bom_structure` (extends)


Extension points: `_get_bom_array_lines`, `_get_bom_data`, `_get_component_available_qty`, `_get_component_data`, `_get_component_forecast_available_qty`, `_get_pdf_doc`, `_get_quantities_info`, `_get_resupply_availability`, `_get_subcontracting_line`

## `report.mrp.report_mo_overview` (extends)


Extension points: `_get_components_data`, `_get_location_ids`, `_get_mo_summary`

## `change.production.qty` (extends)


## `mrp.production.serials` (extends)


Public methods: `action_apply`

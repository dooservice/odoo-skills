# stock_fleet — Stock Transport

Depends on: stock, fleet.

## `fleet.vehicle.model.category` (extends)

- `weight_capacity` Float “Max Weight”
- `weight_capacity_uom_name` Char “Weight unit of measure label” (compute=_compute_weight_capacity_uom_name)
- `volume_capacity` Float “Max Volume”
- `volume_capacity_uom_name` Char “Volume unit of measure label” (compute=_compute_volume_capacity_uom_name)

## `stock.picking.type` (extends)

- `auto_print_cmr_report` Boolean “Auto Print Consignment Note (CMR)”
- `dispatch_management` Boolean “Dispatch Management”
- `dock_ids` Many2many → `stock.location` (store, compute=_compute_dock_ids)

## `stock.picking` (extends)

- `zip` Char “Zip” (related=partner_id.zip)

Public methods: `write`

Extension points: `_get_autoprint_report_actions`

## `stock.picking.batch` (extends)

- `vehicle_id` Many2one → `fleet.vehicle` “Vehicle”
- `vehicle_category_id` Many2one → `fleet.vehicle.model.category` “Vehicle Category” (store, compute=_compute_vehicle_category_id)
- `allowed_dock_ids` Many2many “Allowed Docks” (related=picking_type_id.dock_ids)
- `dock_id` Many2one → `stock.location` “Dock” (store, compute=_compute_dock_id)
- `vehicle_weight_capacity` Float “Vehcilce Payload Capacity” (related=vehicle_category_id.weight_capacity)
- `weight_uom_name` Char “Weight unit of measure label” (compute=_compute_weight_uom_name)
- `vehicle_volume_capacity` Float “Max Volume (m³)” (related=vehicle_category_id.volume_capacity)
- `volume_uom_name` Char “Volume unit of measure label” (compute=_compute_volume_uom_name)
- `driver_id` Many2one → `res.partner` “Driver” (store, compute=_compute_driver_id)
- `used_weight_percentage` Float “Weight %” (compute=_compute_capacity_percentage)
- `used_volume_percentage` Float “Volume %” (compute=_compute_capacity_percentage)
- `end_date` Datetime “End Date” (store, compute=_compute_end_date)
- `has_dispatch_management` Boolean “Dispatch Management” (related=picking_type_id.dispatch_management)

Public methods: `create`, `order_on_zip`, `write`

Extension points: `_get_merged_batch_vals`

## `stock.warehouse` (extends)


Extension points: `_get_picking_type_update_values`

## `report.stock_fleet.report_cmr_batch` (defines)

CMR Batch Report


Extension points: `_get_report_values`

## `report.stock_fleet.report_cmr` (defines)

CMR Report


Extension points: `_get_pickings_data`, `_get_report_values`

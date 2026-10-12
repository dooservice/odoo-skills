# stock_fleet — Stock Transport

Depends on: stock_picking_batch, fleet.

## `fleet.vehicle.model.category` (extends)

- `weight_capacity` Float “Max Weight”
- `weight_capacity_uom_name` Char “Weight unit of measure label” (compute=_compute_weight_capacity_uom_name)
- `volume_capacity` Float “Max Volume”
- `volume_capacity_uom_name` Char “Volume unit of measure label” (compute=_compute_volume_capacity_uom_name)

## `stock.location` (extends)

- `is_a_dock` Boolean “Is a Dock Location”

## `stock.picking` (extends)

- `zip` Char “Zip” (related=partner_id.zip)

Public methods: `write`

## `stock.picking.batch` (extends)

- `vehicle_id` Many2one → `fleet.vehicle` “Vehicle”
- `vehicle_category_id` Many2one → `fleet.vehicle.model.category` “Vehicle Category” (store, compute=_compute_vehicle_category_id)
- `dock_id` Many2one → `stock.location` “Dock Location” (store, compute=_compute_dock_id)
- `vehicle_weight_capacity` Float “Vehcilce Payload Capacity” (related=vehicle_category_id.weight_capacity)
- `weight_uom_name` Char “Weight unit of measure label” (compute=_compute_weight_uom_name)
- `vehicle_volume_capacity` Float “Max Volume (m³)” (related=vehicle_category_id.volume_capacity)
- `volume_uom_name` Char “Volume unit of measure label” (compute=_compute_volume_uom_name)
- `driver_id` Many2one → `res.partner` “Driver” (store, compute=_compute_driver_id)
- `used_weight_percentage` Float “Weight %” (compute=_compute_capacity_percentage)
- `used_volume_percentage` Float “Volume %” (compute=_compute_capacity_percentage)
- `end_date` Datetime “End Date”

Public methods: `create`, `order_on_zip`, `write`

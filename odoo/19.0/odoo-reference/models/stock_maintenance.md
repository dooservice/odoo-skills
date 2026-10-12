# stock_maintenance — Stock - Maintenance

Depends on: stock, maintenance.

## `maintenance.equipment` (extends)

- `location_id` Many2one → `stock.location`
- `match_serial` Boolean (compute=_compute_match_serial)

Public methods: `action_open_matched_serial`

## `stock.location` (extends)

- `equipment_count` Integer “Equipment Count” (compute=_compute_equipment_count)

Public methods: `action_view_equipments_records`

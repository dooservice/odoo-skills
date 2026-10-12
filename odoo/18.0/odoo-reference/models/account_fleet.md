# account_fleet — Accounting/Fleet bridge

Depends on: fleet, account.

## `account.move` (extends)


## `account.move.line` (extends)

- `vehicle_id` Many2one → `fleet.vehicle` “Vehicle”
- `need_vehicle` Boolean (compute=_compute_need_vehicle)
- `vehicle_log_service_ids` One2many → `fleet.vehicle.log.services`

Public methods: `unlink`, `write`

Extension points: `_prepare_fleet_log_service`

## `fleet.vehicle` (extends)

- `bill_count` Integer “Bills Count” (compute=_compute_move_ids)
- `account_move_ids` One2many → `account.move` (compute=_compute_move_ids)

Public methods: `action_view_bills`

## `fleet.vehicle.log.services` (extends)

- `account_move_line_id` Many2one → `account.move.line`
- `account_move_state` Selection (related=account_move_line_id.parent_state)
- `amount` Monetary “Cost” (store, compute=_compute_amount)
- `vehicle_id` Many2one → `fleet.vehicle` “Vehicle” (required, store, compute=_compute_vehicle_id)

Public methods: `action_open_account_move`

## `account.automatic.entry.wizard` (extends)


Extension points: `_get_move_line_dict_vals_change_period`

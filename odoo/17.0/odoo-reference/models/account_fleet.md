# account_fleet — Accounting/Fleet bridge

Depends on: fleet, account.

## `account.move` (extends)


## `account.move.line` (extends)

- `vehicle_id` Many2one → `fleet.vehicle` “Vehicle”
- `need_vehicle` Boolean (compute=_compute_need_vehicle)

Extension points: `_prepare_fleet_log_service`

## `fleet.vehicle` (extends)

- `bill_count` Integer “Bills Count” (compute=_compute_move_ids)
- `account_move_ids` One2many → `account.move` (compute=_compute_move_ids)

Public methods: `action_view_bills`

## `account.automatic.entry.wizard` (extends)


Extension points: `_get_move_line_dict_vals_change_period`

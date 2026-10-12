# spreadsheet_dashboard — Spreadsheet dashboard

Depends on: spreadsheet.

## `spreadsheet.dashboard` (defines)

Spreadsheet Dashboard

- `name` Char (required)
- `dashboard_group_id` Many2one → `spreadsheet.dashboard.group` (required)
- `data` Binary (required)
- `raw` Binary (compute=_compute_raw)
- `thumbnail` Binary
- `sequence` Integer
- `group_ids` Many2many → `res.groups`

Public methods: `copy`

## `spreadsheet.dashboard.group` (defines)

Group of dashboards

- `name` Char (required)
- `dashboard_ids` One2many → `spreadsheet.dashboard`
- `sequence` Integer

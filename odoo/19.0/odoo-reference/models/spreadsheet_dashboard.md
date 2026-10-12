# spreadsheet_dashboard — Spreadsheet dashboard

Depends on: spreadsheet.

## `spreadsheet.dashboard` (defines)

Spreadsheet Dashboard

Inherits: `spreadsheet.mixin`

- `name` Char (required)
- `dashboard_group_id` Many2one → `spreadsheet.dashboard.group` (required, index)
- `sequence` Integer
- `sample_dashboard_file_path` Char
- `is_published` Boolean
- `company_ids` Many2many → `res.company` “Companies”
- `group_ids` Many2many → `res.groups`
- `favorite_user_ids` Many2many → `res.users` “Favorite Users”
- `is_favorite` Boolean “Is Favorite” (compute=_compute_is_favorite)
- `main_data_model_ids` Many2many → `ir.model`

Public methods: `action_toggle_favorite`, `copy_data`

Extension points: `_get_dashboard_translation_namespace`, `_get_sample_dashboard`, `_get_serialized_readonly_dashboard`

## `spreadsheet.dashboard.group` (defines)

Group of dashboards

- `name` Char (required)
- `dashboard_ids` One2many → `spreadsheet.dashboard`
- `published_dashboard_ids` One2many → `spreadsheet.dashboard`
- `sequence` Integer

## `spreadsheet.dashboard.share` (defines)

Copy of a shared dashboard

Inherits: `spreadsheet.mixin`

- `dashboard_id` Many2one → `spreadsheet.dashboard` (required)
- `excel_export` Binary
- `access_token` Char (required)
- `full_url` Char “URL” (compute=_compute_full_url)
- `name` Char (related=dashboard_id.name)

Public methods: `action_get_share_url`

Extension points: `_check_dashboard_access`, `_check_token`

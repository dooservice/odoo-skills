# spreadsheet_dashboard — Spreadsheet dashboard

Depends on: spreadsheet.

## `spreadsheet.dashboard` (defines)

Spreadsheet Dashboard

Inherits: `spreadsheet.mixin`

- `name` Char (required)
- `dashboard_group_id` Many2one → `spreadsheet.dashboard.group` “Section” (required, index)
- `sequence` Integer
- `sample_dashboard_file_path` Char
- `is_published` Boolean “Published”
- `company_ids` Many2many → `res.company` “Companies”
- `group_ids` Many2many → `res.groups` “Access Groups”
- `favorite_user_ids` Many2many → `res.users` “Favorite Users”
- `is_favorite` Boolean “Is Favorite” (compute=_compute_is_favorite)
- `main_data_model_ids` Many2many → `ir.model`
- `allowed_user_ids` Many2many → `res.users` “Allowed Users”

Public methods: `action_open_dashboard`, `action_toggle_favorite`

Extension points: `_get_dashboard_translation_namespace`, `_get_sample_dashboard`, `_get_serialized_readonly_dashboard`

## `spreadsheet.dashboard.favorite.filters` (defines)

Dashboard Favorite Filter

- `name` Char “Filter Name” (required)
- `user_ids` Many2many → `res.users` “Users”
- `dashboard_id` Many2one → `spreadsheet.dashboard` “Dashboard” (required, index)
- `is_default` Boolean “Default Filter”
- `global_filters` Json
- `active` Boolean

## `spreadsheet.dashboard.group` (defines)

Group of dashboards

- `name` Char (required)
- `dashboard_ids` One2many → `spreadsheet.dashboard`
- `published_dashboard_ids` One2many → `spreadsheet.dashboard`
- `sequence` Integer

## `spreadsheet.dashboard.share` (defines)

Copy of a shared dashboard

Inherits: `spreadsheet.mixin`

- `dashboard_id` Many2one → `spreadsheet.dashboard` (required, index)
- `dashboard_group_id` Many2one (related=dashboard_id.dashboard_group_id)
- `excel_export` Binary
- `active` Boolean
- `access_token` Char (required)
- `full_url` Char “URL” (compute=_compute_full_url)
- `name` Char (required, store, compute=_compute_name)

Public methods: `action_get_share_url`

Extension points: `_check_dashboard_access`, `_check_token`

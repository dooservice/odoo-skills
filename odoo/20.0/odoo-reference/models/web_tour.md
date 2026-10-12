# web_tour — Tours

Depends on: web.

## `ir.http` (extends)


Public methods: `session_info`

## `res.users` (extends)

- `tour_enabled` Boolean “Onboarding” (store, compute=_compute_tour_enabled)

Public methods: `switch_tour_enabled`

## `web_tour.tour` (defines)

Tour

- `name` Char (required)
- `active` Boolean
- `step_ids` One2many → `web_tour.tour.step`
- `url` Char “Starting URL”
- `sharing_url` Char “Sharing URL” (compute=_compute_sharing_url)
- `rainbow_man_message` Html
- `sequence` Integer
- `custom` Boolean “Custom”
- `user_consumed_ids` Many2many → `res.users`

Public methods: `consume`, `export_js_file`, `get_current_tour`, `get_tour_json_by_name`

Extension points: `_get_tour_json`

## `web_tour.tour.step` (defines)

Tour's step

- `trigger` Char (required)
- `content` Char
- `tooltip_position` Selection
- `tour_id` Many2one → `web_tour.tour` (required, index)
- `run` Char
- `sequence` Integer

Public methods: `get_steps_json`

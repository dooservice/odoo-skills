# l10n_in_hr_holidays — India - Time Off

Depends on: hr_holidays.

## `hr.employee` (extends)


Public methods: `get_special_days_data`

Extension points: `_get_optional_holidays_data`

## `hr.leave` (extends)

- `l10n_in_contains_sandwich_leaves` Boolean

Public methods: `action_approve`, `action_refuse`

Extension points: `_action_user_cancel`, `_get_durations`, `_get_max_allowed_absence_hours`

## `hr.work.entry.type` (extends)

- `l10n_in_is_sandwich_leave` Boolean “Is Sandwich Leave”
- `l10n_in_sandwich_policy` Selection “Sandwich Leave Policy”
- `l10n_in_is_limited_to_optional_days` Boolean “Is Limited To Optional Days”

## `l10n.in.hr.leave.optional.holiday` (defines)

Optional Holidays

- `name` Char (required)
- `date` Date (required)
- `company_id` Many2one → `res.company` (required)

Public methods: `default_get`

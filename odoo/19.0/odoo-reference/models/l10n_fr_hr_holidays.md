# l10n_fr_hr_holidays — France - Time Off

Depends on: hr_holidays.

## `hr.leave` (extends)

- `l10n_fr_date_to_changed` Boolean

Extension points: `_get_durations`, `_get_fr_date_from_to`

## `res.company` (extends)

- `l10n_fr_reference_leave_type` Many2one → `hr.leave.type` “Company Paid Time Off Type”

Extension points: `_get_fr_reference_leave_type`

## `res.config.settings` (extends)

- `l10n_fr_reference_leave_type` Many2one → `hr.leave.type` (related=company_id.l10n_fr_reference_leave_type)

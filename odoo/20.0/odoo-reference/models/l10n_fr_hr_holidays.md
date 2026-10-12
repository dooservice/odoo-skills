# l10n_fr_hr_holidays — France - Time Off

Depends on: hr_holidays.

## `hr.leave` (extends)

- `l10n_fr_date_to_changed` Boolean

Extension points: `_get_durations`, `_get_fr_date_from_to`

## `hr.version` (extends)


Extension points: `_get_version_work_entries_values`

## `res.company` (extends)

- `l10n_fr_reference_work_entry_type` Many2one → `hr.work.entry.type` “Company Paid Time Type”

Extension points: `_get_fr_reference_work_entry_type`

## `res.config.settings` (extends)

- `l10n_fr_reference_work_entry_type` Many2one → `hr.work.entry.type` (related=company_id.l10n_fr_reference_work_entry_type)

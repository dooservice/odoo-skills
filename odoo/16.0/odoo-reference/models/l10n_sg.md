# l10n_sg — Singapore - Accounting

Depends on: base, account.

## `account.move` (extends)

- `l10n_sg_permit_number` Char “Permit No.”
- `l10n_sg_permit_number_date` Date “Date of permit number”

## `account.chart.template` (extends)


## `res.company` (extends)

Companies

- `l10n_sg_unique_entity_number` Char “UEN” (related=partner_id.l10n_sg_unique_entity_number)

Extension points: `_get_view`

## `res.partner` (extends)

- `l10n_sg_unique_entity_number` Char “UEN”

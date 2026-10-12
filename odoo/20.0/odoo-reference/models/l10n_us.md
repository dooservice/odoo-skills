# l10n_us — United States - Localizations

Depends on: base, base_address_extended.

## `l10n_us.res.county` (defines)

US County

- `name` Char (required)
- `state_id` Many2one → `res.country.state` (required)

## `res.city` (extends)

- `l10n_us_county_id` Many2one → `l10n_us.res.county` “County”

## `res.partner.bank` (extends)

- `l10n_us_bank_account_type` Selection “Bank Account Type” (required)

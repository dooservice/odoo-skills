# spreadsheet — Spreadsheet

Depends on: bus, web, portal.

## `res.currency` (extends)


Public methods: `get_company_currency_for_spreadsheet`, `get_currencies_for_spreadsheet`

## `res.currency.rate` (extends)


Public methods: `get_rates_for_spreadsheet`

Extension points: `_get_rate_for_spreadsheet`

## `res.lang` (extends)


Public methods: `get_locales_for_spreadsheet`

Extension points: `_get_user_spreadsheet_locale`

## `spreadsheet.mixin` (defines)

Spreadsheet mixin

- `spreadsheet_binary_data` Binary “Spreadsheet file” (required)
- `spreadsheet_data` Text (compute=_compute_spreadsheet_data)
- `thumbnail` Binary

Extension points: `_get_file_content`

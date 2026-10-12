# spreadsheet — Spreadsheet

Depends on: bus, web, portal.

## `ir.http` (extends)


Public methods: `session_info`

## `res.currency` (extends)


Public methods: `get_company_currency_for_spreadsheet`

## `res.currency.rate` (extends)


Public methods: `get_rates_for_spreadsheet`

Extension points: `_get_rate_for_spreadsheet`

## `res.lang` (extends)


Public methods: `get_locales_for_spreadsheet`

Extension points: `_get_user_spreadsheet_locale`

## `spreadsheet.mixin` (defines)

Spreadsheet mixin

- `spreadsheet_binary_data` Binary “Spreadsheet file”
- `spreadsheet_data` Text (compute=_compute_spreadsheet_data)
- `spreadsheet_file_name` Char (compute=_compute_spreadsheet_file_name)
- `thumbnail` Binary

Public methods: `get_display_names_for_spreadsheet`

Extension points: `_check_spreadsheet_data`, `_get_file_content`

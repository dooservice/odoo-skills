# printer — Printer

Depends on: base.

## `ir.actions.report` (extends)

- `printer_ids` Many2many → `printer.printer` “Printers”

Public methods: `get_print_jobs`, `get_select_printer_wizard`, `report_action`

Extension points: `_get_readable_fields`

## `printer.printer` (defines)

External Printer

- `name` Char (required)
- `ip_address` Char “IP Address”
- `report_ids` Many2many → `ir.actions.report` “Linked Reports”
- `type` Selection “Type” (required)

## `select.printers.wizard` (defines)

Select printers to print the report on

- `printer_ids` Many2many → `printer.printer`
- `do_not_ask_again` Boolean “Do not ask me again”

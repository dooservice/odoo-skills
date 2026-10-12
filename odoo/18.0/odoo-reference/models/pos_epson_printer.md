# pos_epson_printer — POS Epson Printer

Depends on: point_of_sale.

## `pos.config` (extends)

- `epson_printer_ip` Char “Epson Printer IP”

## `pos.printer` (extends)

- `printer_type` Selection
- `epson_printer_ip` Char “Epson Printer IP Address”

## `res.config.settings` (extends)

- `pos_epson_printer_ip` Char (store, compute=_compute_pos_epson_printer_ip)

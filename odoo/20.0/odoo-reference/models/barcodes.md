# barcodes — Barcode

Depends on: web.

## `barcode.nomenclature` (defines)

Barcode Nomenclature

- `name` Char “Barcode Nomenclature” (required)
- `rule_ids` One2many → `barcode.rule` “Rules”
- `upc_ean_conv` Selection “UPC/EAN Conversion” (required)

Public methods: `match_pattern`, `parse_barcode`, `parse_nomenclature_barcode`, `parse_uri`, `sanitize_ean`, `sanitize_upc`

## `barcode.rule` (defines)

Barcode Rule

- `name` Char “Rule Name” (required)
- `barcode_nomenclature_id` Many2one → `barcode.nomenclature` “Barcode Nomenclature”
- `sequence` Integer “Sequence”
- `encoding` Selection “Encoding” (required)
- `type` Selection “Type” (required)
- `pattern` Char “Barcode Pattern” (required)
- `alias` Char “Alias” (required)

Extension points: `_check_pattern`

## `ir.http` (extends)


Public methods: `session_info`

## `res.company` (extends)

- `nomenclature_id` Many2one → `barcode.nomenclature` “Nomenclature”

Extension points: `_get_default_nomenclature`

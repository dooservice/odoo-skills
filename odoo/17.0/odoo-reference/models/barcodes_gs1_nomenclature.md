# barcodes_gs1_nomenclature — Barcode - GS1 Nomenclature

Depends on: barcodes, uom.

## `barcode.nomenclature` (extends)

- `is_gs1_nomenclature` Boolean “Is GS1 Nomenclature”
- `gs1_separator_fnc1` Char “FNC1 Separator”

Public methods: `gs1_date_to_date`, `gs1_decompose_extanded`, `parse_barcode`, `parse_gs1_rule_pattern`

Extension points: `_check_pattern`

## `barcode.rule` (extends)

- `encoding` Selection
- `type` Selection
- `is_gs1_nomenclature` Boolean (related=barcode_nomenclature_id.is_gs1_nomenclature)
- `gs1_content_type` Selection “GS1 Content Type”
- `gs1_decimal_usage` Boolean “Decimal”
- `associated_uom_id` Many2one → `uom.uom`

Extension points: `_check_pattern`

## `ir.http` (extends)


Public methods: `session_info`

# uom — Units of measure

Depends on: base.

## `uom.category` (defines)

Product UoM Categories

- `name` Char “Unit of Measure Category” (required)
- `uom_ids` One2many → `uom.uom`
- `reference_uom_id` Many2one → `uom.uom`

## `uom.uom` (defines)

Product Unit of Measure

- `name` Char “Unit of Measure” (required)
- `category_id` Many2one → `uom.category` (required)
- `factor` Float “Ratio” (required)
- `factor_inv` Float “Bigger Ratio” (required, readonly, compute=_compute_factor_inv)
- `rounding` Float “Rounding Precision” (required)
- `active` Boolean “Active”
- `uom_type` Selection (required)
- `ratio` Float “Combined Ratio” (compute=_compute_ratio)
- `color` Integer “Color” (compute=_compute_color)

Public methods: `create`, `name_create`, `write`

Extension points: `_check_category_reference_uniqueness`

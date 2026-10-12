# uom — Units of measure

Depends on: base.

## `uom.uom` (defines)

Product Unit of Measure

- `name` Char “Unit Name” (required)
- `sequence` Integer (store, compute=_compute_sequence)
- `relative_factor` Float “Contains” (required)
- `rounding` Float “Rounding Precision” (compute=_compute_rounding)
- `active` Boolean “Active”
- `relative_uom_id` Many2one → `uom.uom`
- `related_uom_ids` One2many → `uom.uom`
- `factor` Float “Absolute Quantity” (store, compute=_compute_factor)
- `parent_path` Char (index)

Public methods: `compare`, `is_zero`, `round`

Extension points: `_check_factor`, `_check_qty`

# base_sparse_field — Sparse Fields

Depends on: base.

## `base` (extends)


## `ir.model.fields` (extends)

- `ttype` Selection
- `serialization_field_id` Many2one → `ir.model.fields` “Serialization Field”

Public methods: `write`

## `sparse_fields.test` (defines)

Sparse fields Test

- `data` Serialized
- `boolean` Boolean
- `integer` Integer
- `float` Float
- `char` Char
- `selection` Selection
- `partner` Many2one → `res.partner`

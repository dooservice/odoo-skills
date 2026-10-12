# account_tax_python — Define Taxes as Python Code

Depends on: account.

## `account.tax` (extends)

- `amount_type` Selection
- `formula` Text “Formula”
- `formula_decoded_info` Json (compute=_compute_formula_decoded_info)

Extension points: `_check_amount_type_code_formula`, `_check_and_normalize_formula`

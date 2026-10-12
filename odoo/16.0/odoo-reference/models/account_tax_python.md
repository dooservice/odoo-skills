# account_tax_python — Define Taxes as Python Code

Depends on: account.

## `account.tax` (extends)

- `amount_type` Selection
- `python_compute` Text “Python Code”
- `python_applicable` Text “Applicable Code”

Public methods: `compute_all`

## `account.tax.template` (extends)

- `amount_type` Selection
- `python_compute` Text “Python Code”
- `python_applicable` Text “Applicable Code”

Extension points: `_get_tax_vals`

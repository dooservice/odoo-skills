# l10n_in_pos — Indian - Point of Sale

Depends on: l10n_in, point_of_sale.

## `account.move` (extends)


## `account.move.line` (extends)


Extension points: `_get_l10n_in_gstr_section`

## `account.tax` (extends)


## `pos.bill` (extends)


## `pos.config` (extends)


## `pos.order` (extends)


Extension points: `_prepare_product_aml_dict`

## `pos.order.line` (extends)

- `l10n_in_hsn_code` Char “HSN/SAC Code” (store, compute=_compute_l10n_in_hsn_code)

Extension points: `_prepare_base_line_for_taxes_computation`

## `pos.session` (extends)


Public methods: `set_missing_hsn_codes_in_pos_orders`

Extension points: `_get_sale_key`, `_get_sale_vals`

## `product.product` (extends)

- `l10n_in_hsn_missing_in_pos` Boolean “HSN Missing in POS”

Public methods: `l10n_in_get_hsn_code_action`

## `product.template` (extends)


## `res.company` (extends)


## `res.partner` (extends)

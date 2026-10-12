# l10n_in_pos — Indian - Point of Sale

Depends on: l10n_in, point_of_sale.

## `account.move` (extends)


## `account.move.line` (extends)


Extension points: `_get_l10n_in_gstr_section`

## `account.tax` (extends)


## `pos.bill` (extends)


## `pos.config` (extends)


## `pos.order` (extends)


Extension points: `_prepare_account_move_line_data`, `_prepare_move_line_vals_from_base_line`

## `pos.order.line` (extends)

- `l10n_in_hsn_code` Char “HSN/SAC Code” (store, compute=_compute_l10n_in_hsn_code)

Extension points: `_prepare_base_lines_for_taxes_computation`

## `pos.payment.method` (extends)

- `upi_identifier` Char “UPI ID”
- `qr_payment_icon_ids` Many2many → `ir.attachment` “QR Payment Icons”

Public methods: `get_qr_code_value`

## `pos.session` (extends)


Public methods: `set_missing_hsn_codes_in_pos_orders`

Extension points: `_prepare_account_move_line_commands_for_reversal`

## `product.product` (extends)

- `l10n_in_hsn_missing_in_pos` Boolean “HSN Missing in POS”

Public methods: `l10n_in_get_hsn_code_action`

## `product.template` (extends)


## `res.company` (extends)


## `res.partner.bank` (extends)


Extension points: `_get_available_qr_methods`, `_get_qr_code_generation_params`

## `pos.order.receipt` (extends)

Point of Sale Order Receipt Generator


Public methods: `order_receipt_generate_data`

# l10n_tw_edi_ecpay_pos — Taiwan - E-invoicing Pos

Depends on: point_of_sale, l10n_tw_edi_ecpay.

## `account.tax` (extends)


## `pos.config` (extends)

- `is_ecpay_enabled` Boolean “Is Ecpay Enabled” (compute=_compute_is_ecpay_enabled)

Public methods: `get_limited_partners_loading`

## `pos.order` (extends)

- `l10n_tw_edi_is_print` Boolean “Print”
- `l10n_tw_edi_love_code` Char “Love Code”
- `l10n_tw_edi_carrier_type` Selection “Carrier Type”
- `l10n_tw_edi_carrier_number` Char “Carrier Number”
- `l10n_tw_edi_carrier_number_2` Char “Carrier Number 2”
- `l10n_tw_edi_is_b2b` Boolean “Is B2B” (compute=_compute_l10n_tw_edi_is_b2b)

Public methods: `l10n_tw_edi_get_uniform_invoice`

Extension points: `_prepare_invoice_vals`

## `pos.session` (extends)


Public methods: `l10n_tw_edi_check_love_code`, `l10n_tw_edi_check_mobile_barcode`

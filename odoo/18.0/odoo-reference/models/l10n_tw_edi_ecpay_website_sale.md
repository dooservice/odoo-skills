# l10n_tw_edi_ecpay_website_sale — Taiwan - E-invoicing Ecommerce

Depends on: website_sale, l10n_tw_edi_ecpay.

## `res.partner` (extends)

- `l10n_tw_edi_require_paper_format` Boolean “Require Paper Format”

## `sale.order` (extends)

- `l10n_tw_edi_is_print` Boolean “Print”
- `l10n_tw_edi_love_code` Char “Love Code”
- `l10n_tw_edi_carrier_type` Selection “Carrier Type”
- `l10n_tw_edi_carrier_number` Char “Carrier Number”
- `l10n_tw_edi_carrier_number_2` Char “Carrier Number 2”

Extension points: `_prepare_invoice`

## `website` (extends)


Extension points: `_get_checkout_step_list`

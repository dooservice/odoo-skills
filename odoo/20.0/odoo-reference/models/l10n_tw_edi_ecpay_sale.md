# l10n_tw_edi_ecpay_sale — Taiwan - E-invoicing Sales

Depends on: sale, l10n_tw_edi_ecpay.

## `sale.order` (extends)

- `l10n_tw_edi_is_print` Boolean “Get Printed Version” (store, compute=_compute_is_print)
- `l10n_tw_edi_love_code` Char “Love Code” (store, compute=_compute_love_code)
- `l10n_tw_edi_carrier_type` Selection “Carrier Type” (store, compute=_compute_carrier_info)
- `l10n_tw_edi_carrier_number` Char “Carrier Number” (store, compute=_compute_carrier_info)
- `l10n_tw_edi_carrier_number_2` Char “Carrier Number 2” (store, compute=_compute_carrier_info)
- `l10n_tw_edi_so_ecpay_tab_invisible` Boolean (compute=_compute_l10n_tw_edi_so_ecpay_tab_invisible)

Extension points: `_prepare_invoice`

# l10n_pl_jpk — Poland - JPK_VAT Community

Depends on: l10n_pl.

## `account.move` (extends)

- `l10n_pl_vat_b_spv` Boolean “B_SPV”
- `l10n_pl_vat_b_spv_dostawa` Boolean “B_SPV_Dostawa”
- `l10n_pl_vat_b_mpv_prowizja` Boolean “B_MPV_Prowizja”
- `l10n_pl_delivery_date` Date “PL Delivery Date” (readonly)
- `l10n_pl_show_delivery_date` Boolean (compute=_compute_l10n_pl_show_delivery_date)

## `l10n_pl_tax_office` (defines)

Tax Office in Poland

- `code` Char “Code” (required)
- `name` Char “Description” (required)

Public methods: `name_get`

## `product.template` (extends)

- `l10n_pl_vat_gtu` Selection “GTU Codes”

## `res.company` (extends)

- `l10n_pl_reports_tax_office_id` Many2one → `l10n_pl_tax_office` “Tax Office”

## `res.config.settings` (extends)

- `l10n_pl_reports_tax_office_id` Many2one (related=company_id.l10n_pl_reports_tax_office_id)

## `res.partner` (extends)

- `l10n_pl_links_with_customer` Boolean “Links With Company”

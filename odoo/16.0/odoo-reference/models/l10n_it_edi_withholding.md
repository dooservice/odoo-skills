# l10n_it_edi_withholding — Italy - E-invoicing (Withholding)

Depends on: l10n_it_edi.

## `account.chart.template` (extends)


## `account.edi.format` (extends)


## `account.move` (extends)

- `l10n_it_amount_vat_signed` Monetary “VAT” (compute=_compute_amount_extended)
- `l10n_it_amount_pension_fund_signed` Monetary “Pension Fund” (compute=_compute_amount_extended)
- `l10n_it_amount_withholding_signed` Monetary “Withholding” (compute=_compute_amount_extended)
- `l10n_it_amount_before_withholding_signed` Monetary “Total Before Withholding” (compute=_compute_amount_extended)

Extension points: `_prepare_fatturapa_export_values`

## `account.tax.template` (extends)

- `l10n_it_withholding_type` Selection “Withholding tax type (Italy)”
- `l10n_it_withholding_reason` Selection “Withholding tax reason (Italy)”
- `l10n_it_pension_fund_type` Selection “Pension fund type (Italy)”

Extension points: `_get_tax_vals`

## `account.tax` (extends)

- `l10n_it_withholding_type` Selection “Withholding tax type (Italy)”
- `l10n_it_withholding_reason` Selection “Withholding tax reason (Italy)”
- `l10n_it_pension_fund_type` Selection “Pension fund type (Italy)”

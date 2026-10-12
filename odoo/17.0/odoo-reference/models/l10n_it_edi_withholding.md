# l10n_it_edi_withholding — Italy - E-invoicing (Withholding)

Depends on: l10n_it_edi.

## `account.chart.template` (extends)


Extension points: `_get_it_withholding_account_account`, `_get_it_withholding_account_tax`, `_get_it_withholding_account_tax_group`

## `account.move` (extends)

- `l10n_it_amount_vat_signed` Monetary “VAT” (compute=_compute_amount_extended)
- `l10n_it_amount_pension_fund_signed` Monetary “Pension Fund” (compute=_compute_amount_extended)
- `l10n_it_amount_withholding_signed` Monetary “Withholding” (compute=_compute_amount_extended)
- `l10n_it_amount_before_withholding_signed` Monetary “Total Before Withholding” (compute=_compute_amount_extended)

Public methods: `get_tag`

Extension points: `_get_l10_it_edi_get_taxable_amount_from_summary_data`, `_get_pension_fund_tax_for_line`

## `account.tax` (extends)

- `l10n_it_withholding_type` Selection “Withholding tax type (Italy)”
- `l10n_it_withholding_reason` Selection “Withholding tax reason (Italy)”
- `l10n_it_pension_fund_type` Selection “Pension fund type (Italy)”

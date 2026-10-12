# l10n_it_edi_pa — Italy - E-invoicing (PA)

Depends on: l10n_it_edi.

## `account.edi.format` (extends)


## `account.move` (extends)

- `l10n_it_origin_document_type` Selection “Origin Document Type” (readonly)
- `l10n_it_origin_document_name` Char “Origin Document Name” (readonly)
- `l10n_it_origin_document_date` Date “Origin Document Date” (readonly)
- `l10n_it_cig` Char “CIG” (readonly)
- `l10n_it_cup` Char “CUP” (readonly)
- `l10n_it_partner_pa` Boolean (compute=_compute_l10n_it_partner_pa)

Extension points: `_prepare_fatturapa_export_values`

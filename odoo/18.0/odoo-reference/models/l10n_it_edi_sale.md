# l10n_it_edi_sale — Italy - Sale E-invoicing

Depends on: l10n_it_edi, sale.

## `sale.order` (extends)

- `l10n_it_origin_document_type` Selection “Origin Document Type”
- `l10n_it_origin_document_name` Char “Origin Document Name”
- `l10n_it_origin_document_date` Date “Origin Document Date”
- `l10n_it_cig` Char “CIG”
- `l10n_it_cup` Char “CUP”
- `l10n_it_partner_pa` Boolean (compute=_compute_l10n_it_partner_pa)

Extension points: `_prepare_invoice`

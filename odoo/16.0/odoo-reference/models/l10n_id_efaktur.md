# l10n_id_efaktur — Indonesia E-faktur

Depends on: l10n_id.

## `account.move` (extends)

- `l10n_id_tax_number` Char “Tax Number”
- `l10n_id_replace_invoice_id` Many2one → `account.move` “Replace Invoice”
- `l10n_id_attachment_id` Many2one → `ir.attachment` (readonly)
- `l10n_id_csv_created` Boolean “CSV Created” (compute=_compute_csv_created)
- `l10n_id_kode_transaksi` Selection “Kode Transaksi” (store, compute=_compute_kode_transaksi)
- `l10n_id_need_kode_transaksi` Boolean (compute=_compute_need_kode_transaksi)

Public methods: `download_csv`, `download_efaktur`, `reset_efaktur`

Extension points: `_prepare_etax`

## `l10n_id_efaktur.efaktur.range` (defines)

Available E-faktur range

- `company_id` Many2one → `res.company` (required)
- `max` Char (store, compute=_compute_default)
- `min` Char (store, compute=_compute_default)
- `available` Integer (store, compute=_compute_available)

Public methods: `pop_number`, `push_number`, `push_numbers`

## `res.partner` (extends)

- `l10n_id_pkp` Boolean “ID PKP” (store, compute=_compute_l10n_id_pkp)
- `l10n_id_nik` Char “NIK”
- `l10n_id_tax_address` Char “Tax Address”
- `l10n_id_tax_name` Char “Tax Name”
- `l10n_id_kode_transaksi` Selection “Kode Transaksi”

## `res.config.settings` (extends)

- `l10n_id_tax_address` Char “Tax Address” (related=company_id.partner_id.l10n_id_tax_address)
- `l10n_id_tax_name` Char “Tax Name” (related=company_id.partner_id.l10n_id_tax_address)

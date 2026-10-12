# l10n_id_efaktur — Indonesia E-faktur

Depends on: l10n_id.

## `account.move` (extends)

- `l10n_id_tax_number` Char “Tax Number”
- `l10n_id_replace_invoice_id` Many2one → `account.move` “Replace Invoice”
- `l10n_id_efaktur_document` Many2one → `l10n_id_efaktur.document` “e-Faktur Document” (readonly)
- `l10n_id_kode_transaksi` Selection “Kode Transaksi” (store, compute=_compute_kode_transaksi)
- `l10n_id_efaktur_range` Many2one → `l10n_id_efaktur.efaktur.range` “E-faktur Range”
- `l10n_id_need_kode_transaksi` Boolean (compute=_compute_need_kode_transaksi)
- `l10n_id_available_range_count` Integer (compute=_compute_available_range_count)
- `l10n_id_show_kode_transaksi` Boolean (compute=_compute_show_kode_transaksi)

Public methods: `button_draft`, `download_csv`, `download_efaktur`, `reset_efaktur`

Extension points: `_prepare_etax`

## `l10n_id_efaktur.efaktur.range` (defines)

Available E-faktur range

- `company_id` Many2one → `res.company` (required)
- `max` Char (required)
- `min` Char (required)
- `available` Integer (readonly)
- `next_num` Integer (compute=_compute_next_num)

Public methods: `create`, `pop_number`, `push_number`, `write`

## `l10n_id_efaktur.document` (defines)

E-faktur Document

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char (required, store, compute=_compute_name)
- `company_id` Many2one → `res.company` (required, readonly)
- `active` Boolean “Active”
- `invoice_ids` One2many → `account.move`
- `attachment_id` Many2one → `ir.attachment` (readonly)

Public methods: `action_download`, `action_regenerate`

## `res.partner` (extends)

- `l10n_id_pkp` Boolean “Is PKP” (store, compute=_compute_l10n_id_pkp)
- `l10n_id_nik` Char “NIK”
- `l10n_id_kode_transaksi` Selection “Invoice Transaction Code”

## `account.move.reversal` (extends)

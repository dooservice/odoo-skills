# l10n_id_efaktur_coretax — Indonesia E-faktur (Coretax)

Depends on: l10n_id.

## `account.move` (extends)

- `l10n_id_coretax_add_info_07` Selection (store, compute=_compute_l10n_id_coretax_add_info)
- `l10n_id_coretax_facility_info_07` Selection (store, compute=_compute_l10n_id_coretax_facility_info)
- `l10n_id_coretax_add_info_08` Selection (store, compute=_compute_l10n_id_coretax_add_info)
- `l10n_id_coretax_facility_info_08` Selection (store, compute=_compute_l10n_id_coretax_facility_info)
- `l10n_id_coretax_efaktur_available` Boolean (compute=_compute_l10n_id_coretax_efaktur_available)
- `l10n_id_coretax_document` Many2one → `l10n_id_efaktur_coretax.document` “e-Faktur Document (Coretax)” (readonly)
- `l10n_id_coretax_custom_doc` Char
- `l10n_id_coretax_custom_doc_month_year` Date “Custom Document Month and Year”
- `l10n_id_kode_transaksi` Selection “Kode Transaksi” (store, compute=_compute_kode_transaksi)

Public methods: `download_efaktur`, `download_xml`, `prepare_efaktur_vals`

## `account.move.line` (extends)


## `l10n_id_efaktur_coretax.document` (defines)

E-Faktur Document

Inherits: `mail.thread.main.attachment`, `mail.activity.mixin`

- `name` Char (store, compute=_compute_name)
- `company_id` Many2one → `res.company` (required, readonly)
- `active` Boolean “Active”
- `invoice_ids` One2many → `account.move`
- `attachment_id` Many2one → `ir.attachment` (readonly)

Public methods: `action_download`, `action_regenerate`

## `l10n_id_efaktur_coretax.product.code` (defines)

Product categorization according to E-Faktur

- `code` Char
- `description` Text

## `product.template` (extends)

- `l10n_id_product_code` Many2one → `l10n_id_efaktur_coretax.product.code` “E-Faktur Product Code” (store, compute=_compute_l10n_id_product_code)

## `res.partner` (extends)

- `l10n_id_tku` Char “TKU”
- `l10n_id_buyer_document_type` Selection “Document Type”
- `l10n_id_buyer_document_number` Char “Document Number”
- `l10n_id_nik` Char “NIK”
- `l10n_id_pkp` Boolean “Is PKP” (store, compute=_compute_l10n_id_pkp)
- `l10n_id_kode_transaksi` Selection “Invoice Transaction Code”

## `l10n_id_efaktur_coretax.uom.code` (defines)

UOM categorization according to E-Faktur

- `code` Char
- `name` Char

## `uom.uom` (extends)

- `l10n_id_uom_code` Many2one → `l10n_id_efaktur_coretax.uom.code` “E-Faktur UoM code”

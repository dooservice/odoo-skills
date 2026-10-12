# l10n_tr_nilvera — Türkiye - Nilvera

Depends on: l10n_tr, account_edi_ubl_cii.

## `account.journal` (extends)

- `l10n_tr_nilvera_api_key` Char (related=company_id.l10n_tr_nilvera_api_key)
- `is_nilvera_journal` Boolean “Journal used for Nilvera”

## `l10n_tr.nilvera.alias` (defines)

Customer Alias on Nilvera

- `name` Char
- `partner_id` Many2one → `res.partner`

## `res.company` (extends)

- `l10n_tr_nilvera_api_key` Char “Nilvera API key”
- `l10n_tr_nilvera_use_test_env` Boolean “Use testing environment” (required)
- `l10n_tr_nilvera_purchase_journal_id` Many2one → `account.journal` “Nilvera Purchase Journal” (store, compute=_compute_l10n_tr_nilvera_purchase_journal_id)

## `res.config.settings` (extends)

- `l10n_tr_nilvera_api_key` Char “Nilvera API key” (related=company_id.l10n_tr_nilvera_api_key)
- `l10n_tr_nilvera_use_test_env` Boolean “Use testing environment” (required, related=company_id.l10n_tr_nilvera_use_test_env)
- `l10n_tr_nilvera_purchase_journal_id` Many2one (related=company_id.l10n_tr_nilvera_purchase_journal_id)
- `l10n_tr_nilvera_vat` Char “Nilvera VAT” (related=company_id.vat)

Public methods: `nilvera_ping`

## `res.partner` (extends)

- `invoice_edi_format` Selection
- `l10n_tr_nilvera_customer_status` Selection “Nilvera Status” (readonly)
- `l10n_tr_nilvera_customer_alias_id` Many2one → `l10n_tr.nilvera.alias` “Alias” (store, compute=_compute_nilvera_customer_alias_id)
- `l10n_tr_nilvera_customer_alias_ids` One2many → `l10n_tr.nilvera.alias`

Public methods: `l10n_tr_check_nilvera_customer`

Extension points: `_check_nilvera_customer`, `_get_edi_builder`, `_get_suggested_invoice_edi_format`, `_get_ubl_cii_formats_info`

## `uom.uom` (extends)


Extension points: `_get_unece_code`

# l10n_pl_edi — Polish E-Invoicing FA(3)

Depends on: l10n_pl, certificate.

## `account.move` (extends)

- `l10n_pl_edi_status` Selection “KSeF Status” (readonly)
- `l10n_pl_edi_ref` Char “KSeF Reference Number” (readonly)
- `l10n_pl_edi_register` Boolean (related=company_id.l10n_pl_edi_register)
- `l10n_pl_edi_header` Html (readonly)
- `l10n_pl_edi_number` Char “KSeF Number” (readonly, index)
- `l10n_pl_edi_session_id` Char “KSeF Session Number used for sending” (readonly)
- `l10n_pl_edi_attachment_file` Binary
- `l10n_pl_edi_attachment_id` Many2one → `ir.attachment` “KSeF Attachment”
- `l10n_pl_edi_upo_file` Binary
- `l10n_pl_edi_upo_id` Many2one → `ir.attachment` “UPO Attachment”

Public methods: `action_l10n_pl_edi_get_invoice_UPO`, `action_l10n_pl_edi_import_from_ksef`, `action_l10n_pl_edi_update_invoice_status`, `button_draft`, `l10n_pl_edi_get_ksef_bill_vals_from_xml`

Extension points: `_get_edi_decoder`, `_get_fields_to_detach`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`

## `res.company` (extends)

- `l10n_pl_edi_register` Boolean “KSeF Integration Enabled” (compute=_compute_l10n_pl_edi_register)
- `l10n_pl_edi_certificate` Many2one → `certificate.certificate` (store)
- `l10n_pl_edi_access_token` Char “KSeF Token” (readonly)
- `l10n_pl_edi_refresh_token` Char “KSeF Token Expiration” (readonly)
- `l10n_pl_edi_session_id` Char “Reference number” (readonly)
- `l10n_pl_edi_session_key` Binary “Session key” (readonly)
- `l10n_pl_edi_session_iv` Binary “Session iv” (readonly)

Public methods: `l10n_pl_edi_has_access_to_ksef`

## `res.config.settings` (extends)

- `l10n_pl_edi_certificate` Many2one → `certificate.certificate` (compute=_compute_l10n_pl_edi_certificate)
- `l10n_pl_edi_access_token` Char “KSeF Access Token” (readonly, related=company_id.l10n_pl_edi_access_token)
- `l10n_pl_edi_register` Boolean “Allow KSeF integration” (related=company_id.l10n_pl_edi_register)

## `res.partner` (extends)

- `invoice_edi_format` Selection

Extension points: `_get_suggested_invoice_edi_format`

# l10n_it_edi — Italy - E-invoicing

Depends on: l10n_it, account_edi_proxy_client.

## `account_edi_proxy_client.user` (extends)

- `proxy_type` Selection

Extension points: `_get_iap_params`, `_get_proxy_identification`, `_get_proxy_urls`

## `account.move` (extends)

- `l10n_it_edi_state` Selection “SDI State”
- `l10n_it_edi_header` Html (readonly)
- `l10n_it_edi_transaction` Char “FatturaPA Transaction”
- `l10n_it_edi_attachment_file` Binary
- `l10n_it_edi_attachment_id` Many2one → `ir.attachment` “FatturaPA Attachment”
- `l10n_it_edi_is_self_invoice` Boolean (compute=_compute_l10n_it_edi_is_self_invoice)
- `l10n_it_stamp_duty` Float “Dati Bollo”
- `l10n_it_ddt_id` Many2one → `l10n_it.ddt` “DDT”
- `l10n_it_origin_document_type` Selection “Origin Document Type”
- `l10n_it_origin_document_name` Char “Origin Document Name”
- `l10n_it_origin_document_date` Date “Origin Document Date”
- `l10n_it_cig` Char “CIG”
- `l10n_it_cup` Char “CUP”
- `l10n_it_partner_pa` Boolean (compute=_compute_l10n_it_partner_pa)
- `l10n_it_partner_is_public_administration` Boolean (compute=_compute_l10n_it_partner_is_public_administration)

Public methods: `action_check_l10n_it_edi`, `action_invoice_download_fatturapa`, `action_l10n_it_edi_send`, `button_draft`, `cron_l10n_it_edi_download_and_update`, `get_extra_print_items`

Extension points: `_get_edi_decoder`, `_get_fields_to_detach`, `_get_invoice_legal_documents`, `_get_prediction_cache_value`, `_prepare_product_base_line_for_taxes_computation`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`, `_get_invoice_extra_attachments`

## `l10n_it.ddt` (defines)

Transport Document

- `invoice_id` One2many → `account.move` “Invoice Reference”
- `name` Char “Numero DDT” (required)
- `date` Date “Data DDT” (required)

## `ir.attachment` (extends)


Extension points: `_get_edi_supported_formats`

## `res.company` (extends)

- `l10n_it_codice_fiscale` Char “Codice Fiscale” (store, related=partner_id.l10n_it_codice_fiscale)
- `l10n_it_tax_system` Selection “Tax System”
- `l10n_it_edi_proxy_user_id` Many2one → `account_edi_proxy_client.user` (compute=_compute_l10n_it_edi_proxy_user_id)
- `l10n_it_has_eco_index` Boolean
- `l10n_it_eco_index_office` Many2one → `res.country.state` “Province of the register-of-companies office”
- `l10n_it_eco_index_number` Char “Number in register of companies”
- `l10n_it_eco_index_share_capital` Float “Share capital actually paid up”
- `l10n_it_eco_index_sole_shareholder` Selection “Shareholder”
- `l10n_it_eco_index_liquidation_state` Selection “Liquidation state”
- `l10n_it_has_tax_representative` Boolean
- `l10n_it_tax_representative_partner_id` Many2one → `res.partner` “Tax representative partner”

Extension points: `_check_eco_admin_index`, `_check_eco_incorporated`, `_check_tax_representative`

## `res.config.settings` (extends)

- `is_edi_proxy_active` Boolean (compute=_compute_is_edi_proxy_active)
- `company_parent_id` Many2one (readonly, related=company_id.parent_id)
- `use_root_proxy_user` Boolean (compute=_compute_use_root_proxy_user)
- `l10n_it_edi_proxy_current_state` Char (compute=_compute_l10n_it_edi_proxy_current_state)
- `l10n_it_edi_register` Boolean (compute=_compute_l10n_it_edi_register)
- `l10n_it_edi_demo_mode` Selection (compute=_compute_l10n_it_edi_demo_mode)

Public methods: `button_create_proxy_user`

Extension points: `_create_proxy_user`

## `res.partner` (extends)

- `invoice_edi_format` Selection
- `l10n_it_pec_email` Char “PEC e-mail”
- `l10n_it_codice_fiscale` Char “Codice Fiscale”
- `l10n_it_pa_index` Char “Destination Code”

Public methods: `create_company`, `validate_codice_fiscale`

Extension points: `_get_suggested_invoice_edi_format`

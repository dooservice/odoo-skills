# l10n_it_edi — Italy - E-invoicing

Depends on: l10n_it, account_edi_proxy_client, account_debit_note.

## `account.chart.template` (extends)


## `account.chart.template` (extends)


Extension points: `_get_it_account_tax`

## `account_edi_proxy_client.user` (extends)

- `proxy_type` Selection

Extension points: `_get_iap_params`, `_get_proxy_identification`, `_get_proxy_urls`

## `account.move` (extends)

- `l10n_it_edi_state` Selection “SDI State”
- `l10n_it_edi_transaction` Char “SDI Transaction ID”
- `l10n_it_edi_attachment_file` Binary “Attachment File”
- `l10n_it_edi_attachment_name` Char “FatturaPA Attachment Name”
- `l10n_it_edi_proxy_mode` Selection (related=company_id.l10n_it_edi_proxy_user_id.edi_mode)
- `l10n_it_edi_button_label` Char (compute=_compute_l10n_it_edi_button_label)
- `l10n_it_edi_is_self_invoice` Boolean (compute=_compute_l10n_it_edi_is_self_invoice)
- `l10n_it_stamp_duty` Float “Stamp Duty”
- `l10n_it_ddt_id` Many2one → `l10n_it.ddt` “DDT”
- `l10n_it_origin_document_type` Selection “Italian SDI Origin Document Type”
- `l10n_it_origin_document_name` Char “Italian SDI Origin Document Number”
- `l10n_it_origin_document_date` Date “Document Issue Date”
- `l10n_it_cig` Char “CIG”
- `l10n_it_cup` Char “CUP”
- `l10n_it_partner_pa` Boolean (compute=_compute_l10n_it_partner_pa)
- `l10n_it_partner_is_public_administration` Boolean (compute=_compute_l10n_it_partner_is_public_administration)
- `l10n_it_invoice_cause` Text “Payment Reason and Notes”
- `l10n_it_payment_method` Selection (store, compute=_compute_l10n_it_payment_method)
- `l10n_it_document_type` Many2one → `l10n_it.document.type` (store, compute=_compute_l10n_it_document_type)
- `l10n_it_available_document_type_ids` Many2many → `l10n_it.document.type` (compute=_compute_l10n_it_available_document_type_ids)
- `l10n_it_convention_code` Char “Order/Convention Code”

Public methods: `action_check_l10n_it_edi`, `action_invoice_download_fatturapa`, `action_l10n_it_edi_send`, `button_draft`, `cron_l10n_it_edi_download_and_update`, `get_extra_print_items`

Extension points: `_check_draftable`, `_check_l10n_it_edi_xml_content`, `_check_l10n_it_invoice_cause`, `_get_edi_decoder`, `_get_fields_to_detach`, `_get_import_file_type`, `_get_invoice_legal_documents`, `_get_l10_it_edi_get_taxable_amount_from_summary_data`, `_get_pension_fund_tax_for_line`, `_get_prediction_cache_value`, `_get_xml_tree`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`, `_get_invoice_extra_attachments`

## `account.payment.method.line` (extends)

- `l10n_it_payment_method` Selection “Italian Payment Method” (store, compute=_compute_l10n_it_payment_method)

Extension points: `_get_l10n_it_payment_method_selection_code`

## `account.tax` (extends)

- `l10n_it_withholding_type` Selection “Withholding tax type (Italy)”
- `l10n_it_withholding_reason` Selection “Withholding tax reason (Italy)”
- `l10n_it_pension_fund_type` Selection “Pension fund type (Italy)”

## `l10n_it.ddt` (defines)

Transport Document

- `invoice_id` One2many → `account.move` “Invoice Reference”
- `name` Char “Numero DDT” (required)
- `date` Date “Data DDT” (required)

## `l10n_it.document.type` (defines)

Italian Document Type

- `name` Char (required)
- `code` Char (required)
- `move_types` Json

Extension points: `_check_code_unique`

## `res.company` (extends)

- `l10n_it_codice_fiscale` Char “Codice Fiscale” (store, related=partner_id.l10n_it_codice_fiscale)
- `l10n_it_tax_system` Selection “Tax System”
- `l10n_it_edi_proxy_user_id` Many2one → `account_edi_proxy_client.user` (compute=_compute_l10n_it_edi_proxy_user_id)
- `l10n_it_edi_register` Boolean
- `l10n_it_edi_purchase_journal_id` Many2one → `account.journal` “Italian Default Purchase Journal” (store, compute=_compute_l10n_it_edi_purchase_journal_id)
- `l10n_it_has_eco_index` Boolean
- `l10n_it_eco_index_office` Many2one → `res.country.state` “Province of the register-of-companies office”
- `l10n_it_eco_index_number` Char “Number in register of companies”
- `l10n_it_eco_index_share_capital` Float “Share capital actually paid up”
- `l10n_it_eco_index_sole_shareholder` Selection “Shareholder”
- `l10n_it_eco_index_liquidation_state` Selection “Liquidation state”
- `l10n_it_has_tax_representative` Boolean
- `l10n_it_tax_representative_partner_id` Many2one → `res.partner` “Tax representative partner”

Extension points: `_check_eco_admin_index`, `_check_eco_incorporated`, `_check_l10n_it_edi_purchase_journal_id`, `_check_tax_representative`

## `res.config.settings` (extends)

- `l10n_it_edi_register` Boolean (compute=_compute_l10n_it_edi_register)
- `l10n_it_edi_purchase_journal_id` Many2one (related=company_id.l10n_it_edi_purchase_journal_id)
- `l10n_it_edi_show_purchase_journal_id` Boolean (compute=_compute_l10n_it_edi_show_purchase_journal_id)
- `use_root_proxy_user` Boolean (compute=_compute_use_root_proxy_user)

Extension points: `_create_proxy_user`

## `res.partner` (extends)

- `invoice_edi_format` Selection
- `l10n_it_pec_email` Char “PEC e-mail”
- `l10n_it_codice_fiscale` Char “Codice Fiscale”
- `l10n_it_pa_index` Char “Destination Code (SDI)”

Public methods: `validate_codice_fiscale`

Extension points: `_create_parent_from_name`, `_get_frontend_writable_fields`, `_get_suggested_invoice_edi_format`

## `account.payment.register` (extends)

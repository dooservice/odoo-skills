# l10n_it_edi — Italy - E-invoicing

Depends on: l10n_it, account_edi, account_edi_proxy_client.

## `account.chart.template` (extends)


## `account.edi.format` (extends)


Extension points: `_check_filename_is_fattura_pa`, `_check_move_configuration`, `_create_invoice_from_binary`, `_create_invoice_from_xml_tree`, `_get_move_applicability`, `_get_proxy_identification`, `_post_fattura_pa`, `_post_invoice_edi`, `_prepare_invoice_report`

## `account.move` (extends)

- `l10n_it_edi_transaction` Char “FatturaPA Transaction”
- `l10n_it_edi_attachment_id` Many2one → `ir.attachment` “FatturaPA Attachment”
- `l10n_it_stamp_duty` Float “Dati Bollo” (readonly)
- `l10n_it_ddt_id` Many2one → `l10n_it.ddt` “DDT” (readonly)
- `l10n_it_einvoice_name` Char (compute=_compute_l10n_it_einvoice)
- `l10n_it_einvoice_id` Many2one → `ir.attachment` “Electronic invoice” (compute=_compute_l10n_it_einvoice)

Public methods: `invoice_generate_xml`

Extension points: `_get_l10n_it_amount_split_payment`, `_prepare_fatturapa_export_values`

## `account.tax` (extends)

- `l10n_it_vat_due_date` Selection “VAT due date”
- `l10n_it_has_exoneration` Boolean “Has exoneration of tax (Italy)”
- `l10n_it_kind_exoneration` Selection “Exoneration”
- `l10n_it_law_reference` Char “Law Reference”

Extension points: `_check_exoneration_with_no_tax`

## `l10n_it.ddt` (defines)

Transport Document

- `invoice_id` One2many → `account.move` “Invoice Reference”
- `name` Char “Numero DDT” (required)
- `date` Date “Data DDT” (required)

Public methods: `name_get`

## `mail.template` (extends)


Extension points: `_get_edi_attachments`

## `res.company` (extends)

- `l10n_it_codice_fiscale` Char “Codice Fiscale” (store, related=partner_id.l10n_it_codice_fiscale)
- `l10n_it_tax_system` Selection “Tax System”
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
- `l10n_it_edi_proxy_current_state` Char (compute=_compute_l10n_it_edi_proxy_current_state)
- `l10n_it_edi_sdicoop_register` Boolean (compute=_compute_l10n_it_edi_sdicoop_register)
- `l10n_it_edi_sdicoop_demo_mode` Selection (compute=_compute_l10n_it_edi_sdicoop_demo_mode)

Public methods: `button_create_proxy_user`

Extension points: `_create_proxy_user`

## `res.partner` (extends)

- `l10n_it_pec_email` Char “PEC e-mail”
- `l10n_it_codice_fiscale` Char “Codice Fiscale”
- `l10n_it_pa_index` Char “Destination Code”

Public methods: `validate_codice_fiscale`

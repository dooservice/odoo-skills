# l10n_ar — Argentina - Accounting

Depends on: l10n_latam_invoice_document, account.

## `account.chart.template` (extends)


Extension points: `_get_ar_demo_partner`, `_get_demo_data_attachment`, `_get_demo_data_mail_activity`, `_get_demo_data_mail_message`, `_get_demo_data_move`, `_get_demo_data_statement`, `_get_demo_data_transactions`, `_post_load_demo_data`

## `account.account` (extends)

- `l10n_ar_arca_activity_id` Many2one → `l10n_ar.arca.activity` “Associated ARCA Activity”

## `account.chart.template` (extends)


Public methods: `try_loading`

Extension points: `_get_ar_responsibility_match`

## `account.fiscal.position` (extends)

- `l10n_ar_afip_responsibility_type_ids` Many2many → `l10n_ar.afip.responsibility.type` “ARCA Responsibility Types”

Extension points: `_get_fpos_validation_functions`

## `account.journal` (extends)

- `l10n_ar_afip_pos_system` Selection “ARCA POS System” (store, compute=_compute_l10n_ar_afip_pos_system)
- `l10n_ar_afip_pos_number` Integer “ARCA POS Number”
- `company_partner` Many2one → `res.partner` (related=company_id.partner_id)
- `l10n_ar_afip_pos_partner_id` Many2one → `res.partner`
- `l10n_ar_is_pos` Boolean “Is ARCA POS?” (store, compute=_compute_l10n_ar_is_pos)

Public methods: `write`

Extension points: `_check_afip_pos_number`, `_check_afip_pos_system`, `_get_codes_per_journal_type`, `_get_journal_codes_domain`, `_get_journal_letter`, `_get_l10n_ar_afip_pos_types_selection`

## `account.move` (extends)

- `l10n_ar_afip_responsibility_type_id` Many2one → `l10n_ar.afip.responsibility.type` “ARCA Responsibility Type”
- `l10n_ar_afip_concept` Selection “ARCA Concept” (compute=_compute_l10n_ar_afip_concept)
- `l10n_ar_afip_service_start` Date “ARCA Service Start Date”
- `l10n_ar_afip_service_end` Date “ARCA Service End Date”

Extension points: `_check_argentinean_invoice_taxes`, `_check_invoice_type_document_type`, `_check_moves_use_documents`, `_get_afip_invoice_concepts`, `_get_alerts`, `_get_concept`, `_get_formatted_sequence`, `_get_l10n_ar_codes_used_for_inv_and_ref`, `_get_l10n_latam_documents_domain`, `_get_last_sequence_domain`, `_get_name_invoice_report`, `_get_starting_sequence`, `_get_vat`

## `account.move.line` (extends)


## `account.tax.group` (extends)

- `l10n_ar_tribute_afip_code` Selection “Tribute ARCA Code” (readonly, index)
- `l10n_ar_vat_afip_code` Selection “VAT ARCA Code” (readonly, index)

Public methods: `check_uninstall_required`

## `l10n_ar.afip.responsibility.type` (defines)

ARCA Responsibility Type

- `name` Char (required)
- `sequence` Integer
- `code` Char (required, index)
- `active` Boolean

## `l10n_ar.arca.activity` (defines)

ARCA Activity

- `code` Char (required)
- `name` Char (required)

## `l10n_latam.document.type` (extends)

- `l10n_ar_letter` Selection “Letters”
- `purchase_aliquots` Selection

Extension points: `_get_l10n_ar_letters`

## `res.company` (extends)

- `l10n_ar_gross_income_number` Char “Gross Income Number” (related=partner_id.l10n_ar_gross_income_number)
- `l10n_ar_gross_income_type` Selection “Gross Income” (related=partner_id.l10n_ar_gross_income_type)
- `l10n_ar_afip_responsibility_type_id` Many2one (related=partner_id.l10n_ar_afip_responsibility_type_id)
- `l10n_ar_company_requires_vat` Boolean “Company Requires Vat?” (compute=_compute_l10n_ar_company_requires_vat)
- `l10n_ar_afip_start_date` Date “Activities Start”
- `l10n_ar_arca_activity_id` Many2one → `l10n_ar.arca.activity` “Principal Activity”

Public methods: `onchange_country`

## `res.config.settings` (extends)

- `l10n_ar_arca_activity_id` Many2one → `l10n_ar.arca.activity` (related=company_id.l10n_ar_arca_activity_id)

## `res.country` (extends)

- `l10n_ar_afip_code` Char “ARCA Code”
- `l10n_ar_natural_vat` Char “Natural Person VAT”
- `l10n_ar_legal_entity_vat` Char “Legal Entity VAT”
- `l10n_ar_other_vat` Char “Other VAT”

## `res.currency` (extends)

- `l10n_ar_afip_code` Char “ARCA Code”

## `res.partner` (extends)

- `l10n_ar_formatted_vat` Char “Formatted VAT” (compute=_compute_l10n_ar_formatted_vat)
- `l10n_ar_gross_income_number` Char “Gross Income Number”
- `l10n_ar_gross_income_type` Selection
- `l10n_ar_afip_responsibility_type_id` Many2one → `l10n_ar.afip.responsibility.type` “ARCA Responsibility Type”
- `l10n_ar_afip_code` Char “AFIP Identification Code” (store, compute=_compute_l10n_ar_afip_identification)
- `l10n_ar_afip_id_value` Char “AFIP Identification Number” (store, compute=_compute_l10n_ar_afip_identification)

Public methods: `ensure_vat`, `write`

Extension points: `_check_l10n_ar_state`, `_create_parent_from_name`, `_get_all_additional_identifiers_metadata`, `_get_frontend_writable_fields`, `_get_id_number_sanitize`, `_get_mandatory_billing_address_fields`

## `res.partner.bank` (extends)

- `account_type` Selection

Public methods: `retrieve_account_type`

## `account.chart.template` (extends)


Extension points: `_get_account_parent_xmlid`, `_get_accounts_data_values`, `_get_ar_account_journal`, `_get_ar_base_account_account`, `_get_ar_base_res_company`, `_get_ar_base_template_data`

## `account.chart.template` (extends)


Extension points: `_get_ar_ex_res_company`, `_get_ar_ex_template_data`

## `account.chart.template` (extends)


Extension points: `_get_ar_ri_res_company`, `_get_ar_ri_template_data`

## `uom.uom` (extends)

- `l10n_ar_afip_code` Char “Code”

## `account.invoice.report` (extends)

- `l10n_ar_state_id` Many2one → `res.country.state` (readonly)
- `date` Date “Accounting Date” (readonly)

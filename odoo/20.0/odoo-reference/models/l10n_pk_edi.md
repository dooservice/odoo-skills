# l10n_pk_edi — Pakistan - E-invoicing

Depends on: account_debit_note, iap, l10n_pk, stock_delivery.

## `account.move` (extends)

- `l10n_pk_edi_reference` Char “FBR Reference Number” (readonly)
- `l10n_pk_edi_refund_reason` Char “Refund Reason”
- `l10n_pk_edi_status` Selection “E-Invoice Status” (readonly)
- `l10n_pk_edi_enable` Boolean (related=company_id.l10n_pk_edi_enable)

Public methods: `button_draft`

Extension points: `_get_l10n_pk_edi_invoice_type`, `_get_l10n_pk_edi_line_details`, `_get_name_invoice_report`

## `account.move.line` (extends)

- `l10n_pk_edi_sale_type` Selection “Sale Type” (store, compute=_compute_l10n_pk_edi_from_product)
- `l10n_pk_edi_sro_id` Many2one → `l10n_pk_edi.sro` “SRO Schedule” (store, compute=_compute_l10n_pk_edi_from_product)
- `l10n_pk_edi_sro_item_id` Many2one → `l10n_pk_edi.sro.item` “SRO Item” (store, compute=_compute_l10n_pk_edi_from_product)
- `l10n_pk_edi_filter_sro_item_ids` One2many (related=l10n_pk_edi_sro_id.sro_item_ids)

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`

## `account.tax` (extends)


## `iap.account` (extends)


## `l10n_pk_edi.sro` (defines)

Pakistan Statutory Regulatory Order

- `name` Char “Statutory Regulatory Order Schedule”
- `sro_item_ids` One2many → `l10n_pk_edi.sro.item` “Statutory Regulatory Order Items”
- `l10n_pk_edi_sale_type` Selection “Sale Type” (required)

## `l10n_pk_edi.sro.item` (defines)

Pakistan Statutory Regulatory Order Item

- `name` Char
- `sro_id` Many2one → `l10n_pk_edi.sro` “Statutory Regulatory Order Schedule”

## `product.product` (extends)


## `product.template` (extends)

- `l10n_pk_edi_sale_type` Selection “Sale Type” (required)
- `l10n_pk_edi_sro_id` Many2one → `l10n_pk_edi.sro` “Statutory Regulatory Order Schedule”
- `l10n_pk_edi_sro_item_id` Many2one → `l10n_pk_edi.sro.item` “Statutory Regulatory Order Item”
- `l10n_pk_edi_filter_sro_item_ids` One2many (related=l10n_pk_edi_sro_id.sro_item_ids)
- `l10n_pk_edi_uom_code` Selection (related=uom_id.l10n_pk_edi_uom_code)

## `res.company` (extends)

- `l10n_pk_edi_enable` Boolean “Enable E-Invoicing(PK)”
- `l10n_pk_edi_whitelisted` Boolean “FBR IP Whitelisted”
- `l10n_pk_edi_production_auth_token` Char “E-invoice(PK) Production Authentication Token”
- `l10n_pk_edi_test_auth_token` Char “E-invoice(PK) Testing Authentication Token” (compute=_compute_l10n_pk_edi_system_params)
- `l10n_pk_edi_test_vat` Char “Registered Business Identification Number” (compute=_compute_l10n_pk_edi_system_params)

Public methods: `l10n_pk_edi_run_test_scenarios`

Extension points: `_get_l10n_pk_edi_auth_token`

## `res.config.settings` (extends)

- `l10n_pk_edi_enable` Boolean (related=company_id.l10n_pk_edi_enable)
- `l10n_pk_edi_production_auth_token` Char (related=company_id.l10n_pk_edi_production_auth_token)
- `l10n_pk_edi_test_auth_token` Char (related=company_id.l10n_pk_edi_test_auth_token)
- `l10n_pk_edi_whitelisted` Boolean (related=company_id.l10n_pk_edi_whitelisted)
- `l10n_pk_edi_test_vat` Char (related=company_id.l10n_pk_edi_test_vat)
- `l10n_pk_edi_company_email` Char “Authorized Email” (related=company_id.email)

Public methods: `action_l10n_pk_edi_run_sandbox_tests`

## `res.partner` (extends)

- `l10n_pk_edi_enable` Boolean (compute=_compute_l10n_pk_edi_enable)
- `l10n_pk_edi_fbr_customer_status` Selection

Public methods: `button_check_fbr_customer_registration`

## `uom.uom` (extends)

- `l10n_pk_edi_uom_code` Selection “FBR UoM Code”

## `account.debit.note` (extends)


Extension points: `_prepare_default_values`

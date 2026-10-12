# l10n_sg — Singapore - Accounting

Depends on: account_qr_code_emv, account, account_edi_ubl_cii, account_peppol.

## `account_edi_proxy_client.user` (extends)


## `account.move` (extends)

- `l10n_sg_permit_number` Char “Permit No.”
- `l10n_sg_permit_number_date` Date “Date of permit number”
- `l10n_sg_customer_accounting_gst_amount` Monetary (compute=_compute_l10n_sg_customer_accounting_gst_amount)

Extension points: `_get_name_invoice_report`

## `account.tax` (extends)

- `ubl_cii_tax_category_code` Selection

## `base.document.layout` (extends)

- `l10n_sg_unique_entity_number` Char (related=company_id.l10n_sg_unique_entity_number)

## `res.partner.bank` (extends)

- `proxy_type` Selection

Extension points: `_check_for_qr_code_errors`, `_check_sg_proxy`, `_get_additional_data_field`, `_get_emv_qr_code_names`, `_get_error_messages_for_qr`, `_get_merchant_account_info`

## `res.company` (extends)

- `l10n_sg_unique_entity_number` Char “UEN” (related=partner_id.l10n_sg_unique_entity_number)

## `res.partner` (extends)

- `l10n_sg_unique_entity_number` Char “UEN” (compute=_compute_l10n_sg_unique_entity_number)

## `account.chart.template` (extends)


Extension points: `_get_account_parent_xmlid`, `_get_sg_account_account`, `_get_sg_account_journal`, `_get_sg_res_company`, `_get_sg_template_data`

# l10n_sg — Singapore - Accounting

Depends on: account_qr_code_emv, account.

## `account.move` (extends)

- `l10n_sg_permit_number` Char “Permit No.”
- `l10n_sg_permit_number_date` Date “Date of permit number”

## `res.partner.bank` (extends)

- `proxy_type` Selection

Extension points: `_check_for_qr_code_errors`, `_check_sg_proxy`, `_get_additional_data_field`, `_get_error_messages_for_qr`, `_get_merchant_account_info`

## `res.company` (extends)

Companies

- `l10n_sg_unique_entity_number` Char “UEN” (related=partner_id.l10n_sg_unique_entity_number)

Extension points: `_get_view`

## `res.partner` (extends)

- `l10n_sg_unique_entity_number` Char “UEN”

## `account.chart.template` (extends)


Extension points: `_get_sg_account_account`, `_get_sg_res_company`, `_get_sg_template_data`

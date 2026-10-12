# l10n_th — Thailand - Accounting

Depends on: account_qr_code_emv.

## `account.move` (extends)


Extension points: `_get_name_invoice_report`

## `ir.actions.report` (extends)


## `res.partner.bank` (extends)

- `proxy_type` Selection

Extension points: `_check_for_qr_code_errors`, `_check_th_proxy`, `_get_error_messages_for_qr`, `_get_merchant_account_info`

## `res.partner` (extends)

- `l10n_th_branch_name` Char (compute=_l10n_th_get_branch_name)

## `account.chart.template` (extends)


Extension points: `_get_th_res_company`, `_get_th_template_data`

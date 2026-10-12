# l10n_my_edi_extended — Malaysia - E-invoicing Extended Features

Depends on: l10n_my_edi.

## `account.edi.xml.ubl_myinvois_my` (extends)


Extension points: `_get_delivery_vals_list`, `_get_invoice_line_item_vals`

## `account.move` (extends)

- `l10n_my_edi_invoice_long_id` Char “MyInvois Long ID” (readonly)
- `l10n_my_invoice_need_edi` Boolean (compute=_compute_l10n_my_invoice_need_edi)

Public methods: `action_invoice_sent`, `action_l10n_my_edi_send_invoice`

Extension points: `_get_name_invoice_report`

## `account.move.line` (extends)

- `l10n_my_edi_classification_code` Selection “Malaysian classification code” (store, compute=_compute_l10n_my_edi_classification_code)

## `account.move.send` (extends)


## `res.partner` (extends)

- `l10n_my_edi_industrial_classification` Many2one → `l10n_my_edi.industry_classification` “Ind. Classification” (store, compute=_compute_l10n_my_edi_industrial_classification)
- `l10n_my_edi_malaysian_tin` Char “Malaysian TIN”

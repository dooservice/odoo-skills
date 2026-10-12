# l10n_gr_edi_e_invoo — Greece - myDATA E-invoicing through e-invoo

Depends on: account_edi_proxy_client, l10n_gr_edi.

## `account_edi_proxy_client.user` (extends)

- `proxy_type` Selection

Extension points: `_get_proxy_identification`, `_get_proxy_urls`

## `account.move` (extends)

- `l10n_gr_edi_state` Selection

Public methods: `l10n_gr_edi_try_send_invoices`

Extension points: `_check_draftable`

## `account.move.send` (extends)


## `l10n_gr_edi.document` (extends)

- `state` Selection
- `mydata_uid` Char “myDATA UID”
- `mydata_authentication_code` Char “myDATA Authentication Code”
- `provider_uid` Char
- `provider_invoice_identifier` Char “Invoice Identifier”
- `provider_qr_url` Char “Provider QR URL”
- `provider_pdf_state` Selection “Final PDF Status”
- `provider_pdf_error` Text

## `res.company` (extends)

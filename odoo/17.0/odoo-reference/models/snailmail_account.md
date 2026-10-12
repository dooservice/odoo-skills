# snailmail_account — Snail Mail - Account

Depends on: account, snailmail.

## `account.move` (extends)


Extension points: `_get_pdf_and_send_invoice_vals`

## `res.company` (extends)

- `invoice_is_snailmail` Boolean “Send by Post”

## `res.config.settings` (extends)

- `invoice_is_snailmail` Boolean “Send by Post” (related=company_id.invoice_is_snailmail)

## `account.move.send` (extends)

- `enable_send_by_post` Boolean (compute=_compute_enable_send_by_post)
- `checkbox_send_by_post` Boolean “By Post” (store, compute=_compute_checkbox_send_by_post)
- `send_by_post_cost` Integer “Stamps” (compute=_compute_send_by_post_extra_fields)
- `send_by_post_warning_message` Text (compute=_compute_send_by_post_extra_fields)
- `send_by_post_readonly` Boolean (compute=_compute_send_by_post_extra_fields)

Extension points: `_get_wizard_vals_restrict_to`, `_get_wizard_values`, `_prepare_snailmail_letter_values`

# snailmail_account — snailmail_account

Depends on: account, snailmail.

## `res.company` (extends)

- `invoice_is_snailmail` Boolean “Send by Post”

## `res.config.settings` (extends)

- `invoice_is_snailmail` Boolean “Send by Post” (related=company_id.invoice_is_snailmail)

## `account.invoice.send` (extends)

Account Invoice Send

- `partner_id` Many2one → `res.partner` “Partner” (compute=_get_partner)
- `snailmail_is_letter` Boolean “Send by Post”
- `snailmail_cost` Float “Stamp(s)” (readonly, compute=_compute_snailmail_cost)
- `invalid_addresses` Integer “Invalid Addresses Count” (compute=_compute_invalid_addresses)
- `invalid_invoices` Integer “Invalid Invoices Count” (compute=_compute_invalid_addresses)
- `invalid_partner_ids` Many2many → `res.partner` “Invalid Addresses” (compute=_compute_invalid_addresses)

Public methods: `invalid_addresses_action`, `notify_invalid_addresses`, `send_and_print`, `send_and_print_action`, `snailmail_print_action`

Extension points: `_get_partner`

## `snailmail.confirm.invoice` (defines)

Snailmail Confirm Invoice

Inherits: `snailmail.confirm`

- `invoice_send_id` Many2one → `account.invoice.send`

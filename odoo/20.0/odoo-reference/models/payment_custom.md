# payment_custom — Payment Provider: Custom Payment Modes

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `custom_mode` Selection “Custom Mode”
- `qr_code` Boolean “Enable QR Codes”
- `company_partner_id` Many2one → `res.partner` (related=company_id.partner_id)
- `partner_bank_id` Many2one → `res.partner.bank` “Bank Account” (store, compute=_compute_partner_bank_id)

Public methods: `copy_data`

Extension points: `_get_custom_bank_account`, `_get_default_payment_method_codes`, `_get_provider_domain`, `_get_removal_values`

## `payment.transaction` (extends)


Extension points: `_get_communication`, `_get_custom_qr_code`, `_get_sent_message`, `_get_specific_rendering_values`, `_get_status_message`

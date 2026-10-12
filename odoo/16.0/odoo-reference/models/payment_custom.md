# payment_custom — Payment Provider: Custom Payment Modes

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `custom_mode` Selection “Custom Mode”
- `qr_code` Boolean “Enable QR Codes”

Extension points: `_get_removal_values`

## `payment.transaction` (extends)


Extension points: `_get_communication`, `_get_sent_message`, `_get_specific_rendering_values`, `_get_tx_from_notification_data`

# payment_demo — Payment Provider: Demo

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection

Extension points: `_check_provider_state`

## `payment.token` (extends)

- `demo_simulated_state` Selection “Simulated State”

## `payment.transaction` (extends)

- `capture_manually` Boolean (related=provider_id.capture_manually)

Public methods: `action_demo_set_canceled`, `action_demo_set_done`, `action_demo_set_error`

Extension points: `_get_tx_from_notification_data`

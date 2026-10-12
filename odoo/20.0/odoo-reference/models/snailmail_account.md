# snailmail_account — Snail Mail - Account

Depends on: account, snailmail.

## `account.move` (extends)


Public methods: `unlink_snailmail_letters`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_prepare_snailmail_letter_values`

## `res.partner` (extends)

- `invoice_sending_method` Selection

## `account.move.send.batch.wizard` (extends)

- `send_by_post_stamps` Integer (compute=_compute_send_by_post_stamps)

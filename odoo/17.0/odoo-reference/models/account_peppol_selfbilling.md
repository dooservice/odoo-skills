# account_peppol_selfbilling — Peppol Self Billing

Depends on: account_peppol.

## `account_edi_proxy_client.user` (extends)


## `account.edi.xml.ubl_bis3` (extends)


## `account.journal` (extends)

- `is_self_billing` Boolean “Self Billing”

## `account.move` (extends)

- `can_send_as_self_invoice` Boolean (compute=_compute_can_send_as_self_invoice)

Extension points: `_get_last_sequence_domain`, `_get_mail_template`, `_get_starting_sequence`

## `account.move.send` (extends)


Extension points: `_get_move_constraints`

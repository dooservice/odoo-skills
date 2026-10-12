# account_peppol_response — Peppol Business Response

Depends on: account_peppol.

## `account_edi_proxy_client.user` (extends)


## `account.move` (extends)

- `peppol_move_state` Selection
- `peppol_response_ids` One2many → `account.peppol.response`
- `peppol_can_send_response` Boolean (compute=_compute_peppol_can_send_response)

Public methods: `action_open_peppol_reponses`, `action_peppol_open_rejection_wizard`, `action_peppol_send_approval_response`, `button_cancel`

## `account.peppol.clarification` (defines)

Peppol clarifications used for rejection

- `list_identifier` Selection “List identifier”
- `code` Char
- `name` Char
- `description` Char

## `account.peppol.response` (defines)

Business Level Responses for Peppol

- `peppol_message_uuid` Char “Peppol UUID”
- `response_code` Selection (required)
- `peppol_state` Selection “Peppol status”
- `move_id` Many2one → `account.move`
- `company_id` Many2one (related=move_id.company_id)

## `res.company` (extends)


## `res.partner` (extends)

- `peppol_supported_documents` Json “Supported Peppol Documents”
- `peppol_response_support` Boolean “Peppol Response Service” (compute=_compute_response_support)

Public methods: `button_account_peppol_check_partner_endpoint`

## `account.peppol.rejection.wizard` (defines)

Peppol Rejection wizard

- `move_ids` Many2many → `account.move` (required)
- `reason_ids` Many2many → `account.peppol.clarification` “Rejection reasons” (required)
- `action_ids` Many2many → `account.peppol.clarification` “Rejection actions”

Public methods: `button_send`

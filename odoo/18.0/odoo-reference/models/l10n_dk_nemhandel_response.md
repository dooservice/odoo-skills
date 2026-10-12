# l10n_dk_nemhandel_response — Nemhandel Business Response

Depends on: l10n_dk_nemhandel.

## `account_edi_proxy_client.user` (extends)


## `account.move` (extends)

- `nemhandel_move_state` Selection
- `nemhandel_response_ids` One2many → `nemhandel.response`
- `nemhandel_can_send_response` Boolean (compute=_compute_nemhandel_can_send_response)

Public methods: `action_nemhandel_open_rejection_wizard`, `action_nemhandel_send_approval_response`, `action_open_nemhandel_reponses`, `button_cancel`

## `nemhandel.response` (defines)

Business Level Responses for Nemhandel

- `nemhandel_message_uuid` Char “Nemhandel UUID”
- `response_code` Selection (required)
- `nemhandel_state` Selection “Nemhandel status”
- `move_id` Many2one → `account.move`
- `company_id` Many2one (related=move_id.company_id)

## `res.partner` (extends)

- `nemhandel_supported_documents` Json “Supported Nemhandel Documents”
- `nemhandel_response_support` Boolean “Nemhandel Response Service” (compute=_compute_nemhandel_response_support)

Public methods: `button_nemhandel_check_partner_endpoint`

## `nemhandel.rejection.wizard` (defines)

Nemhandel Rejection wizard

- `move_ids` Many2many → `account.move` (required)
- `note` Text “Additional note”

Public methods: `button_send`

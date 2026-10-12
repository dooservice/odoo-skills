# l10n_in_edi — Indian - E-invoicing

Depends on: account_edi, l10n_in.

## `account.edi.format` (extends)


Extension points: `_check_move_configuration`, `_get_l10n_in_edi_line_details`, `_get_l10n_in_edi_partner_details`, `_get_l10n_in_edi_saler_buyer_party`, `_get_l10n_in_gst_tags`, `_get_l10n_in_non_taxable_tags`, `_get_l10n_in_tax_details_by_line_code`, `_get_move_applicability`

## `account.move` (extends)

- `l10n_in_edi_cancel_reason` Selection “Cancel reason”
- `l10n_in_edi_cancel_remarks` Char “Cancel remarks”
- `l10n_in_edi_show_cancel` Boolean “E-invoice(IN) is sent?” (compute=_compute_l10n_in_edi_show_cancel)

Public methods: `action_retry_edi_documents_error`, `button_cancel_posted_moves`

Extension points: `_get_l10n_in_edi_response_json`

## `res.company` (extends)

- `l10n_in_edi_username` Char “E-invoice (IN) Username”
- `l10n_in_edi_password` Char “E-invoice (IN) Password”
- `l10n_in_edi_token` Char “E-invoice (IN) Token”
- `l10n_in_edi_token_validity` Datetime “E-invoice (IN) Valid Until”

## `res.config.settings` (extends)

- `l10n_in_edi_username` Char “Indian EDI username” (related=company_id.l10n_in_edi_username)
- `l10n_in_edi_password` Char “Indian EDI password” (related=company_id.l10n_in_edi_password)

Public methods: `l10n_in_check_gst_number`, `l10n_in_edi_test`

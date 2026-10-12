# account_debit_note — Debit Notes

Depends on: account.

## `account.move` (extends)

- `debit_origin_id` Many2one → `account.move` (readonly)
- `debit_note_ids` One2many → `account.move`
- `debit_note_count` Integer “Number of Debit Notes” (compute=_compute_debit_count)

Public methods: `action_debit_note`, `action_view_debit_notes`

Extension points: `_get_debit_note_origin`

## `account.debit.note` (defines)

Add Debit Note wizard

- `move_ids` Many2many → `account.move`
- `date` Date “Debit Note Date” (required)
- `reason` Char “Reason”
- `journal_id` Many2one → `account.journal` “Use Specific Journal”
- `copy_lines` Boolean “Copy Lines”
- `move_type` Char (compute=_compute_from_moves)
- `journal_type` Char (compute=_compute_from_moves)
- `country_code` Char (related=move_ids.company_id.country_id.code)

Public methods: `create_debit`, `default_get`

Extension points: `_prepare_default_values`

# account_debit_note — Debit Notes

Depends on: account.

## `account.journal` (extends)

- `debit_sequence` Boolean “Dedicated Debit Note Sequence” (store, compute=_compute_debit_sequence)

## `account.move` (extends)

- `debit_origin_id` Many2one → `account.move` (readonly)
- `debit_origin_move_type` Selection “Debit Origin Move Type” (related=debit_origin_id.move_type)
- `debit_note_ids` One2many → `account.move`
- `debit_note_count` Integer “Number of Debit Notes” (compute=_compute_debit_count)

Public methods: `action_debit_note`, `action_open_debit_note_origin_entry`, `action_view_debit_notes`

Extension points: `_get_last_sequence_domain`, `_get_starting_sequence`

## `account.debit.note` (defines)

Add Debit Note wizard

- `move_ids` Many2many → `account.move`
- `date` Date “Debit Note Date” (required)
- `reason` Char “Reason”
- `journal_id` Many2one → `account.journal` “Use Specific Journal”
- `copy_lines` Boolean “Copy Lines”
- `move_type` Char (compute=_compute_from_moves)
- `journal_type` Char (compute=_compute_journal_type)
- `country_code` Char (related=move_ids.company_id.country_id.code)

Public methods: `create_debit`, `default_get`

Extension points: `_prepare_default_values`

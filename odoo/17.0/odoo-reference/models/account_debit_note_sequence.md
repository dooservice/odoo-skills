# account_debit_note_sequence — Debit Note Sequence

Depends on: account_debit_note.

## `account.journal` (extends)

- `debit_sequence` Boolean “Dedicated Debit Note Sequence” (store, compute=_compute_debit_sequence)

## `account.move` (extends)


Extension points: `_get_last_sequence_domain`, `_get_starting_sequence`

# l10n_fr_fec — France - FEC Export

Depends on: l10n_fr, account.

## `account.fr.fec` (defines)

Ficher Echange Informatise

- `date_from` Date “Start Date” (required)
- `date_to` Date “End Date” (required)
- `fec_data` Binary “FEC File” (readonly)
- `filename` Char “Filename” (readonly)
- `test_file` Boolean
- `export_type` Selection “Export Type” (required)
- `excluded_journal_ids` Many2many → `account.journal` “Excluded Journals”

Public methods: `generate_fec`

Extension points: `_get_company_legal_data`, `_get_fec_stream`, `_get_where_query`

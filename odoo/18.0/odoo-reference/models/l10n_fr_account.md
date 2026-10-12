# l10n_fr_account — France - Accounting

Depends on: base_iban, base_vat, account, l10n_fr.

## `account.move` (extends)

- `l10n_fr_is_company_french` Boolean (compute=_compute_l10n_fr_is_company_french)

Extension points: `_get_view`

## `res.company` (extends)

- `l10n_fr_rounding_difference_loss_account_id` Many2one → `account.account`
- `l10n_fr_rounding_difference_profit_account_id` Many2one → `account.account`

## `account.chart.template` (extends)


Extension points: `_get_fr_account_journal`, `_get_fr_reconcile_model`, `_get_fr_res_company`, `_get_fr_template_data`

## `account.chart.template` (extends)


Extension points: `_get_mc_template_data`

## `l10n_fr.fec.export.wizard` (defines)

Fichier Echange Informatise

- `date_from` Date “Start Date” (required)
- `date_to` Date “End Date” (required)
- `filename` Char “Filename” (readonly)
- `test_file` Boolean
- `exclude_zero` Boolean “Exclude lines at 0”
- `export_type` Selection “Export Type” (required)
- `excluded_journal_ids` Many2many → `account.journal` “Excluded Journals”

Public methods: `create_fec_report_action`, `generate_fec`

Extension points: `_get_base_domain`, `_get_company_legal_data`, `_get_fec_stream`

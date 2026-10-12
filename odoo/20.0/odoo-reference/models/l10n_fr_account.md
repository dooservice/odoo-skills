# l10n_fr_account — France - Accounting

Depends on: account, account_edi_ubl_cii, l10n_fr.

## `account.move` (extends)

- `l10n_fr_is_company_french` Boolean (compute=_compute_l10n_fr_is_company_french)

Extension points: `_get_view`

## `base.document.layout` (extends)

- `report_footer` Html

## `res.company` (extends)

- `l10n_fr_siret` Char (related=partner_id.l10n_fr_siret)
- `l10n_fr_siren` Char (related=partner_id.l10n_fr_siren)
- `l10n_fr_rounding_difference_loss_account_id` Many2one → `account.account`
- `l10n_fr_rounding_difference_profit_account_id` Many2one → `account.account`

## `res.partner` (extends)

- `l10n_fr_siret` Char (compute=_compute_l10n_fr_siret)
- `l10n_fr_siren` Char (compute=_compute_l10n_fr_siren)

Extension points: `_get_identifier_fields`

## `account.chart.template` (extends)


Extension points: `_get_bank_fees_reco_account`, `_get_fr_account_account`, `_get_fr_account_journal`, `_get_fr_res_company`, `_get_fr_template_data`

## `account.chart.template` (extends)


Extension points: `_get_fr_asso_res_company`, `_get_fr_asso_template_data`

## `account.chart.template` (extends)


Extension points: `_get_fr_comp_account_account`, `_get_fr_comp_res_company`, `_get_fr_comp_template_data`

## `account.chart.template` (extends)


Extension points: `_get_gf_template_data`

## `account.chart.template` (extends)


Extension points: `_get_gp_template_data`

## `account.chart.template` (extends)


Extension points: `_get_mc_template_data`

## `account.chart.template` (extends)


Extension points: `_get_mq_template_data`

## `account.chart.template` (extends)


Extension points: `_get_re_template_data`

## `account.chart.template` (extends)


Extension points: `_get_yt_template_data`

## `l10n_fr.fec.export.wizard` (defines)

Fichier Echange Informatise

- `date_from` Date “Start Date” (required)
- `date_to` Date “End Date” (required)
- `filename` Char “Filename” (readonly)
- `test_file` Boolean
- `export_type` Selection “Export Type” (required)
- `excluded_journal_ids` Many2many → `account.journal` “Excluded Journals”

Public methods: `create_fec_report_action`, `generate_fec`

Extension points: `_get_base_domain`, `_get_company_legal_data`, `_get_fec_stream`

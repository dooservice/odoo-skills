# l10n_ca — Canada - Accounting

Depends on: account.

## `res.company` (extends)

- `l10n_ca_pst` Char “PST Number” (related=partner_id.l10n_ca_pst)

Public methods: `write`

## `base.document.layout` (extends)

- `l10n_ca_pst` Char (readonly, related=company_id.l10n_ca_pst)
- `account_fiscal_country_id` Many2one (readonly, related=company_id.account_fiscal_country_id)

## `res.config.settings` (extends)

- `module_l10n_ca_payment_cpa005` Boolean “Canadian CPA005 Payments (EFT/PAD)”

## `res.partner` (extends)

- `l10n_ca_pst` Char “PST number”

## `account.chart.template` (extends)


Extension points: `_get_accounts_data_values`, `_get_ca_account_account`, `_get_ca_account_fiscal_position`, `_get_ca_account_journal`, `_get_ca_res_company`, `_get_ca_template_data`

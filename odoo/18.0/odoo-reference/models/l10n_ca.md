# l10n_ca — Canada - Accounting

Depends on: account, base_iban.

## `res.company` (extends)

- `l10n_ca_pst` Char “PST Number” (related=partner_id.l10n_ca_pst)

## `base.document.layout` (extends)

- `l10n_ca_pst` Char (readonly, related=company_id.l10n_ca_pst)
- `account_fiscal_country_id` Many2one (readonly, related=company_id.account_fiscal_country_id)

## `res.partner` (extends)

- `l10n_ca_pst` Char “PST number”

## `account.chart.template` (extends)


Extension points: `_get_ca_res_company`, `_get_ca_template_data`

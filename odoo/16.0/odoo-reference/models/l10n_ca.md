# l10n_ca — Canada - Accounting

Depends on: account, base_iban, l10n_multilang.

## `res.company` (extends)

- `l10n_ca_pst` Char “PST” (related=partner_id.l10n_ca_pst)

## `base.document.layout` (extends)

- `l10n_ca_pst` Char (readonly, related=company_id.l10n_ca_pst)
- `account_fiscal_country_id` Many2one (readonly, related=company_id.account_fiscal_country_id)

## `res.partner` (extends)

- `l10n_ca_pst` Char “PST”

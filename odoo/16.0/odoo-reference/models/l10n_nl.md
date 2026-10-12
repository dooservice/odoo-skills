# l10n_nl — Netherlands - Accounting

Depends on: account, base_iban, base_vat.

## `account.chart.template` (extends)


Extension points: `_create_liquidity_journal_suspense_account`

## `account.journal` (extends)


Extension points: `_prepare_liquidity_account_vals`

## `res.company` (extends)

- `l10n_nl_kvk` Char (related=partner_id.l10n_nl_kvk)
- `l10n_nl_oin` Char (related=partner_id.l10n_nl_oin)

## `res.partner` (extends)

- `l10n_nl_kvk` Char “KVK-nummer”
- `l10n_nl_oin` Char “Organisatie Indentificatie Nummer”

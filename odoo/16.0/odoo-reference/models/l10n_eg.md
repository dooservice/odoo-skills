# l10n_eg — Egypt - Accounting

Depends on: account, l10n_multilang.

## `account.chart.template` (extends)


Extension points: `_prepare_all_journals`

## `l10n_eg.eta.account.tax.mixin` (defines)

ETA tax codes mixin

- `l10n_eg_eta_code` Selection “ETA Code (Egypt)”

## `account.tax` (extends)

Inherits: `l10n_eg.eta.account.tax.mixin`


## `account.tax.template` (extends)

Inherits: `l10n_eg.eta.account.tax.mixin`


Extension points: `_get_tax_vals`

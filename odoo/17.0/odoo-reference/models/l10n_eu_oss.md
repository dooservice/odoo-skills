# l10n_eu_oss — EU One Stop Shop (OSS)

Depends on: account.

## `res.company` (extends)


Extension points: `_get_country_from_vat`, `_get_country_specific_account_tax_fields`, `_get_oss_account`, `_get_oss_tags`, `_get_repartition_lines_oss`

## `res.config.settings` (extends)

- `l10n_eu_oss_eu_country` Boolean “Is European country?” (compute=_compute_l10n_eu_oss_european_country)

Public methods: `refresh_eu_tax_mapping`

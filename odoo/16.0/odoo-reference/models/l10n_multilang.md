# l10n_multilang — Multi Language Chart of Accounts

Depends on: account.

## `account.account.tag` (extends)

- `name` Char

## `account.account.template` (extends)

- `name` Char

## `account.account` (extends)

- `name` Char

## `account.group.template` (extends)

- `name` Char

## `account.group` (extends)

- `name` Char

## `account.tax` (extends)

- `name` Char
- `description` Char

## `account.tax.template` (extends)

- `name` Char
- `description` Char

## `account.chart.template` (extends)

- `name` Char
- `spoken_languages` Char “Spoken Languages”

## `account.fiscal.position` (extends)

- `name` Char
- `note` Html

## `account.fiscal.position.template` (extends)

- `name` Char
- `note` Text

## `account.journal` (extends)

- `name` Char

## `account.analytic.account` (extends)

- `name` Char

## `account.chart.template` (extends)


Public methods: `process_coa_translations`, `process_translations`

Extension points: `_get_langs`, `_get_template_from_model`

## `base.language.install` (extends)


Public methods: `lang_install`

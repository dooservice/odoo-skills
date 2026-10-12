# transifex — Transifex integration

Depends on: base, web.

## `base` (extends)


Public methods: `get_field_translations`

## `transifex.code.translation` (defines)

Code Translation

- `source` Text “Code”
- `value` Text “Translation Value”
- `module` Char
- `lang` Selection “Language”
- `transifex_url` Char “Transifex URL” (compute=_compute_transifex_url)

Public methods: `reload`

Extension points: `_get_languages`

## `transifex.translation` (defines)

Transifex Translation


Extension points: `_get_transifex_projects`

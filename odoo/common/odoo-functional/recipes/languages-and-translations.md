# Languages and translations

A language is a `res.lang` record: inactive until installed, then usable on users and
partners. Installing it also loads the translated terms of every installed module. Each
user works in their `lang`, each partner receives documents and emails in theirs, and
translatable fields (product names, payment terms, email templates) keep one value per
active language. The language also sets date and number formats.

```python
print(env['res.lang'].search_read([('active', '=', True)], ['code', 'name', 'date_format', 'decimal_point', 'thousands_sep']))
print(env['res.lang'].with_context(active_test=False).search([('code', '=', 'es_MX')]).read(['active']))
print(env.user.lang, partner.lang)
```

## Install a language

```python
lang = env['res.lang'].with_context(active_test=False).search([('code', '=', 'nl_BE')])
env['base.language.install'].create({'lang_ids': [(6, 0, lang.ids)], 'overwrite': False}).lang_install()
env.cr.commit()
```

- Same wizard and fields in 16.0 to 20.0: `lang_ids` (Many2many), `overwrite`.
  `lang_install()` activates the languages and calls `_update_translations` on all
  installed modules.
- `overwrite=True` replaces terms already customised in that language with the
  module's ones. Default is `True`: ask before keeping it.
- `env['res.lang']._activate_lang('fr_BE')` only activates, without loading module
  terms; 18.0+ also has `_activate_and_install_lang(code)`.
- Codes: `es_ES` (Spain, XML id `base.lang_es`), `es_MX`, `fr_BE`, `nl_BE`, `en_IN`,
  `hi_IN`. The XML id is `base.lang_<code>` except for a few main variants: search by
  `code`.

## Users and partners

```python
env['res.users'].browse(user_ids).write({'lang': 'es_MX'})
env['res.partner'].search([('country_id', '=', env.ref('base.mx').id), ('lang', '!=', 'es_MX')]).write({'lang': 'es_MX'})
env.cr.commit()
```

- `lang` accepts only active languages. A user's `lang` is their partner's.
- Changing `lang` on many partners changes the language of their next documents and
  emails: count them and ask.

## Translated fields

From 16.0, a translatable field is stored in its own column as JSON, one key per
language (`{"en_US": "Chair", "es_ES": "Silla"}`). There is no `ir.translation` table.

```python
product.with_context(lang='es_ES').write({'name': 'Silla de oficina'})
product.with_context(lang='fr_BE').write({'name': 'Chaise de bureau'})
print(product.with_context(lang='es_ES').name)
env.cr.commit()
```

- A write without `lang` in the context goes to the environment's language (the
  user's in a session; often `en_US` in a shell). Always say which language you write.
- `en_US` is the fallback: a language without its own value shows the `en_US` one.
- Several at once: `record.update_field_translations('name', {'es_ES': '...', 'fr_BE': '...'})`;
  read them with `record.get_field_translations('name')`. 18.0+ adds an optional
  `source_lang`.
- Fields translated term by term (HTML of email templates, views) take
  `{lang: {old_term: new_term}}` in `update_field_translations`.

## Date and number formats

On `res.lang`: `date_format`, `time_format` (strftime, e.g. `%d/%m/%Y`), `decimal_point`,
`thousands_sep`, `grouping` (`[3,0]`; Indian `en_IN` uses `[3,2,0]`), `week_start`
(`1` Monday to `7` Sunday), `direction` (`ltr`, `rtl`). 18.0 also has
`short_time_format`.

```python
env.ref('base.lang_en_IN').write({'date_format': '%d-%m-%Y'})
env.cr.commit()
```

- These affect every user of that language. Prefer a change the whole team agrees on.

## Updating module terms

- Reload the terms of one language after a module update:
  `env['ir.module.module'].search([('state', '=', 'installed')])._update_translations(['es_MX'], overwrite=False)`.
  `overwrite=True` discards the user's own wording: ask.
- Export (`base.language.export`: `lang`, `format` `po`/`csv`/`tgz`, `modules`;
  `act_getfile()`) and import (`base.language.import`: `name`, `code`, `data` base64,
  `filename`, `overwrite`; `import_lang()`) move terms between databases. 17.0+ can
  also export one model (`export_type` `model`).
- A term wrong in the standard translation should be fixed for the customer with
  `update_field_translations` and reported upstream, not patched in the module files.

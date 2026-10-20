# Languages and translations

A language is a `res.lang` record: inactive until added, then usable on users and
partners. Adding it also loads the translated terms of every installed module. Each
user works in their `lang`, each partner receives documents and emails in theirs, and
translatable fields (product names, payment terms, email templates) keep one value per
active language. The language also sets date and number formats. Website page
translation is left out.

## Before you start

- Apps: `base` (always installed). Nothing else to install.
- Settings: none to turn on. The Settings ‣ Translations menu (Languages, Application
  Terms, Import / Export) needs developer mode in every version; from 19.0 Settings ‣
  Languages ‣ Manage Languages opens the list without it.
- Pick the language by `name` with the user, never from memory; `<lang code>` below is a
  `code` from the list (like `en_US`).
- Read first:

```python
print(env['res.lang'].search_read([('active', '=', True)], ['code', 'name', 'date_format', 'decimal_point', 'thousands_sep']))
print(env['res.lang'].with_context(active_test=False).search([]).mapped(lambda l: (l.code, l.name, l.active)))
print(env.user.lang, partner.lang)
```

## The standard flow

1. **Add the language.** Settings ‣ General Settings ‣ Languages ‣ Add Languages
   (or the globe icon next to Language in My Profile), select the languages, Add.

   ```python
   lang = env['res.lang'].with_context(active_test=False).search([('code', '=', '<lang code>')])
   env['base.language.install'].create({'lang_ids': [(6, 0, lang.ids)], 'overwrite': False}).lang_install()
   env.cr.commit()
   ```

   - Same wizard and fields in 16.0 to 20.0: `lang_ids` (Many2many), `overwrite`.
     `lang_install()` activates the languages and calls `_update_translations` on all
     installed modules.
   - `overwrite=True` replaces terms already customised in that language with the
     module's ones. The default is `True`: ask before keeping it.
   - The XML id is `base.lang_<code>` except for main variants, which drop the territory
     (`base.lang_<language>`): search by `code`, not by XML id.

   Leaves the language active, with every installed module's terms loaded.

2. **Set the users' language.** Settings ‣ Users & Companies ‣ Users (Manage Users),
   open the user, Preferences tab, Language. Each user can also change their own in My
   Profile.

   ```python
   env['res.users'].browse(user_ids).write({'lang': '<lang code>'})
   env.cr.commit()
   ```

   A user's `lang` is their partner's. Emails and documents to that user are sent in it.

   Leaves those users working in the language from their next page load.

3. **Set the customers' language.** The contact's Language field decides the language of
   the documents and emails they receive.

   ```python
   env['res.partner'].search([('country_id', '=', env.ref('base.<country code>').id), ('lang', '!=', '<lang code>')]).write({'lang': '<lang code>'})
   env.cr.commit()
   ```

   Changing `lang` on many partners changes the language of their next documents and
   emails: count them and ask.

   Leaves the next documents and emails to those contacts in that language.

4. **Translate the business data.** On a translatable field (product name, payment term,
   email template), the language button (`EN`) opens one value per active language.

   ```python
   product.with_context(lang='<lang code>').write({'name': '<name in that language>'})
   product.with_context(lang='<other lang code>').write({'name': '<name in that language>'})
   print(product.with_context(lang='<lang code>').name)
   env.cr.commit()
   ```

   - From 16.0, a translatable field is stored in its own column as JSON, one key per
     language (`{"en_US": "Chair", "<lang code>": "..."}`). There is no `ir.translation`
     table.
   - A write without `lang` in the context goes to the environment's language (the
     user's in a session; often `en_US` in a shell). Always say which language you write.
   - `en_US` is the fallback: a language without its own value shows the `en_US` one.
   - Several at once: `record.update_field_translations('name', {'<lang code>': '...', '<other lang code>': '...'})`;
     read them with `record.get_field_translations('name')`. 18.0+ adds an optional
     `source_lang`.
   - Fields translated term by term (view `arch_db`, website HTML fields) take
     `{lang: {old_term: new_term}}` in `update_field_translations`; the terms are the
     `source` values of `get_field_translations`. Email template bodies (`body_html`,
     `subject`) are translated as a whole value: pass a string.

   Leaves one value per language on that record.

5. **Adjust date and number formats, only if the team asks.** Settings ‣ Translations ‣
   Languages (developer mode), or Settings ‣ Languages ‣ Manage Languages from 19.0;
   open the language.

   ```python
   env['res.lang'].search([('code', '=', '<lang code>')]).write({'date_format': '%d-%m-%Y'})
   env.cr.commit()
   ```

   On `res.lang`: `date_format`, `time_format` (strftime, e.g. `%d/%m/%Y`),
   `decimal_point`, `thousands_sep`, `grouping` (digits per group from the right,
   `[3,0]` by default), `week_start` (`1` Monday to `7` Sunday), `direction` (`ltr`,
   `rtl`). 18.0 only also has `short_time_format`. Each language ships with its usual
   formats; the country's localization decides any legal format; see its localization
   skill if installed.

   Leaves every user of that language seeing the new format.

## Variations

- **Only activate, without loading terms.** `env['res.lang']._activate_lang('<lang code>')`
  activates the language without module terms; 18.0+ also has
  `_activate_and_install_lang(code)`. Choose it only when the terms are loaded right
  after, for example by importing a file.
- **Reload the terms of one language after a module update.**
  `env['ir.module.module'].search([('state', '=', 'installed')])._update_translations(['<lang code>'], overwrite=False)`.
  `overwrite=True` discards the user's own wording: ask.
- **Move terms between databases.** Settings ‣ Translations ‣ Import / Export ‣ Export
  Translation and Import Translation (developer mode). Export: `base.language.export` (`lang`, `format`
  `po`/`csv`/`tgz`, `modules`; `act_getfile()`); import: `base.language.import`
  (`name`, `code`, `data` base64, `filename`, `overwrite`; `import_lang()`). Write
  `data` as a base64 string; the export's `data` is base64 up to 19.0 and raw bytes in
  20.0. 17.0+ can also export one model (`export_type` `model`).
- **A wrong standard term.** Fix it for the customer with `update_field_translations` and
  report it upstream, not in the module files.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Add Languages | Settings ‣ General Settings ‣ Languages | same | same | same | same |
| Languages menu (developer mode) | Settings ‣ Translations ‣ Languages | same | same | same | same |
| Manage Languages in Settings ‣ Languages | - | - | - | yes | yes |
| Import / Export menu (developer mode) | Settings ‣ Translations ‣ Import / Export | same | same | same | same |
| `lang` with an inactive code | rejected | rejected | stored silently | stored silently | stored silently |
| `source_lang` in `update_field_translations` | - | - | yes | yes | yes |
| `_activate_and_install_lang` | - | - | yes | yes | yes |
| `short_time_format` | - | - | yes | - | - |
| Export `data` | base64 | base64 | base64 | base64 | raw bytes |
| Export one model | - | yes | yes | yes | yes |

## Verify

```python
print(env['res.lang'].search([('code', '=', '<lang code>')]).read(['active', 'date_format']))
print(env['res.users'].browse(user_ids).mapped('lang'))
print(product.get_field_translations('name'))
```

Then open a document of a partner in that language and print it.

## Pitfalls

- **Inactive language code.** 16.0 and 17.0 reject it; 18.0+ store it silently and the
  user gets untranslated documents: check `active` first.
- **`overwrite=True` by default** in the add wizard replaces terms the customer
  customised. Pass `overwrite=False` unless the user wants them back.
- **Writing without `lang`** changes the shell's language (often `en_US`), which is also
  the fallback for every other language.
- **Formats changed for one user's taste** change them for every user of that language.
- **A term fixed in the module files** is lost at the next update; fix it in the database.

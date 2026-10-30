Key names in 16.0: `.po` files in `i18n/`; `_(...)` and `from odoo import _lt`; `translate=True`, `html_translate`; export with `--i18n-export`, activate a language with `--load-language=fr_FR`.

Sections of this file:

- [Ship translations as .po files in i18n/](#ship-translations-as-po-files-in-i18n)
- [Know which terms are translatable](#know-which-terms-are-translatable)
- [Declare translatable fields with translate](#declare-translatable-fields-with-translate)
- [Export terms with odoo-bin, never by hand](#export-terms-with-odoo-bin-never-by-hand)

# Ship translations as .po files in i18n/

A module's translations live in its `i18n/` folder: `library.pot`, the template of every
translatable term, and one `<lang>.po` per language (`fr.po`, `fr_BE.po`, `es_419.po`).

- Generate the `.pot` from a database where the module is installed (see
  [Export terms with odoo-bin, never by hand](#export-terms-with-odoo-bin-never-by-hand)),
  and start each `.po` from it; Odoo itself loads only `.po` files.
- For a language such as `fr_BE`, Odoo loads `fr.po` and then `fr_BE.po`: put the
  common translation in `fr.po` and only the differences in `fr_BE.po`.
- `.po` files are loaded when the module is installed or updated in a database where the
  language is active, and when a language is activated.
- Never edit a `.pot` by hand: a term that is not in the code or the data is never
  looked up.

# Know which terms are translatable

- Model terms, exported from the data the module loads: field `string`, `help` and
  `selection` labels, view and QWeb template text, menu and action names, and the values
  of `translate=True` fields in data files.
- Code terms: literals passed to `_(...)` in Python (see
  [Translate only static literals](python.md#translate-only-static-literals)) and to
  `_t(...)` in JavaScript.
- Module-level constants use a lazy translation, resolved when the value is used:
  `from odoo import _lt`, then `LABEL = _lt('Overdue')`.
- The exporter finds terms by the name of the call: a translation function bound to
  any other name (`gettext = _`) exports nothing.
- Code terms are read from the `.po` files the first time a language needs them and
  kept in memory: after changing a `.po`, restart the server. Model terms are copied
  into the database by `-u`.

# Declare translatable fields with translate

- `fields.Char(translate=True)` and `fields.Text(translate=True)` store one value per
  language, in a JSONB column (`{"en_US": "Book", "fr_FR": "Livre"}`).
- An `Html` field takes `translate=html_translate` (from `odoo.tools.translate`): each
  text block is translated on its own, so a translator never sees the markup. A field
  holding XML (a view architecture) takes `xml_translate`.
- Reads and writes use the language of the context: `book.with_context(lang='fr_FR').name`
  reads French, and a write in that context changes the French value. Set several languages
  at once with `book.update_field_translations('name', {'fr_FR': 'Livre', 'es_ES': 'Libro'})`;
  `get_field_translations('name')` returns them all.
- A search on a translated field matches the value in the context language, falling
  back to `en_US` where that language has no value.
- Never make a field translatable that code compares or groups by (a code, a key): each
  language would hold a different value.

# Export terms with odoo-bin, never by hand

```sh
odoo-bin -c odoo.conf -d library_dev --i18n-export=library/i18n/library.pot --modules=library
odoo-bin -c odoo.conf -d library_dev -l fr_FR --i18n-export=library/i18n/fr.po --modules=library
odoo-bin -c odoo.conf -d library_dev -l fr_FR --i18n-import=library/i18n/fr.po --i18n-overwrite
```

- `--i18n-export` writes the file and exits: `.pot` without `-l`, `.po` with it (the
  language must be active, `--load-language=fr_FR` activates it). `--modules` limits
  the export to the module; without it every installed module is exported.
- `--i18n-import` loads a `.po` into the database and exits; `-l` is required.
- Commit the `.pot` together with the change that adds or changes terms; translators
  work from it.
- After an update that changes existing translations, `-u library --i18n-overwrite`
  replaces the translations already in the database with those of the `.po` files;
  without it, terms translated in the database are kept.

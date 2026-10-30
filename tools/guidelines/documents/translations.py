"""`odoo-guidelines/guidelines/translations.md`: i18n files, translatable terms and fields, export."""

from __future__ import annotations

from ..version import OdooVersion
from .lead import GuidedDocument


class Translations(GuidedDocument):
    path = "odoo-guidelines/guidelines/translations.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "es419": version.pick(
                v16="",
                v17_="\n- A Latin American Spanish such as `es_AR` loads `es.po`, `es_419.po`, then\n  `es_AR.po`.",
            ),
            "lazy": version.pick(
                v16_17="`from odoo import _lt`, then `LABEL = _lt('Overdue')`",
                v18_="`_lt = LazyTranslate(__name__)` (from `odoo.tools`), then\n  `LABEL = _lt('Overdue')`",
            ),
            "export": self.export(version),
        }

    def export(self, version: OdooVersion) -> str:
        return version.pick(
            v16_18="```sh\n"
            "odoo-bin -c odoo.conf -d library_dev --i18n-export=library/i18n/library.pot --modules=library\n"
            "odoo-bin -c odoo.conf -d library_dev -l fr_FR --i18n-export=library/i18n/fr.po --modules=library\n"
            "odoo-bin -c odoo.conf -d library_dev -l fr_FR --i18n-import=library/i18n/fr.po --i18n-overwrite\n"
            "```\n\n"
            "- `--i18n-export` writes the file and exits: `.pot` without `-l`, `.po` with it (the\n"
            "  language must be active, `--load-language=fr_FR` activates it). `--modules` limits\n"
            "  the export to the module; without it every installed module is exported.\n"
            "- `--i18n-import` loads a `.po` into the database and exits; `-l` is required.",
            v19_="```sh\n"
            "odoo-bin i18n export -c odoo.conf -d library_dev library\n"
            "odoo-bin i18n export -c odoo.conf -d library_dev library -l fr_FR\n"
            "odoo-bin i18n loadlang -c odoo.conf -d library_dev -l fr_FR\n"
            "odoo-bin i18n import -c odoo.conf -d library_dev -l fr_FR -w library/i18n/fr.po\n"
            "```\n\n"
            "- `i18n export` writes into the module's `i18n/` folder: `library.pot` by default (`-l pot`),\n"
            "  `<iso code>.po` for each language given with `-l`; `-o <file>` writes one file instead.\n"
            "  The module must be installed and the language active (`i18n loadlang` activates it).\n"
            "- `i18n import` loads `.po` files into the database; `-w` overwrites terms already\n"
            "  translated there.\n"
            "- The `--i18n-export`, `--i18n-import` and `--modules` options of earlier versions no\n"
            "  longer exist.",
        )

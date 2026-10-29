"""The `odoo-bin` subcommands of each version, one line each."""

from __future__ import annotations

from ..version import OdooVersion


class CommandList:
    def render(self, version: OdooVersion) -> str:
        lines = [
            "- `server`: the default when no command is given; runs the HTTP server.",
            "- `shell`: a Python console on a database (see above).",
            "- `scaffold library ./addons`: creates a module skeleton (`-t` names another template).",
            version.pick(
                v16_18="- `db load|dump|duplicate|rename|drop`: manages a database together with its\n"
                "  filestore; `db load -n` neutralizes the restored copy.",
                v19_="- `db init|load|dump|duplicate|rename|drop`: manages a database together with its\n"
                "  filestore; `db init library_dev --with-demo` creates one, `db load -n` neutralizes\n"
                "  the restored copy.",
            ),
            ("- `neutralize -d library_copy`: on a copy of production, disables mail servers and\n"
            "  scheduled actions and runs the `data/neutralize.sql` of every installed module;\n"
            "  `--stdout` prints the SQL instead."),
            "- `cloc -d library_dev` (or `-p <module path>`): counts the lines of custom code.",
            version.pick(
                v16_17="- `populate -d library_dev --models library.book --size medium`: fills a database\n"
                "  with generated records, from each model's `_populate_factories`; never on production.",
                v18_19="- `populate -d library_dev --models library.book --factors 10`: multiplies existing\n"
                "  records by duplicating them, for performance tests; never on production.",
                v20="- `duplicate -d library_dev --models library.book --factors 10`: multiplies existing\n"
                "  records by duplicating them, for performance tests; never on production.",
            ),
            version.pick(
                v16_17="",
                v18_="- `upgrade_code --addons-path ./addons --dry-run`: rewrites module source to the APIs\n"
                "  of this version with the scripts shipped in `odoo/upgrade_code` (`--from` and `--to`\n"
                "  select them); a best effort, so review its diff.",
            ),
            version.pick(
                v16_18="",
                v19_="- `i18n export|import|loadlang`: translation files and languages (see\n"
                "  [Export terms with odoo-bin, never by hand](translations.md#export-terms-with-odoo-bin-never-by-hand)).",
            ),
            version.pick(
                v16_18="",
                v19="- `module install|upgrade|uninstall|force-demo`: changes modules of a database\n"
                "  without starting the server.",
                v20="- `module install|upgrade|uninstall|force-demo|list`: changes or lists the modules of\n"
                "  a database without starting the server.",
            ),
            ("- `deploy <module path> <url>`: uploads a module to a running server through\n"
            "  `base_import_module`, which loads its data files, never its Python code."),
            ("- `obfuscate`: encrypts the values of chosen fields in a database copy before it is\n"
            "  shared, and decrypts them with `--unobfuscate`."),
            "- `start`: starts a server on the modules of the current folder, for a quick trial.",
            version.pick(
                v16_18="- `genproxytoken` and `tsconfig` are for Odoo's own tooling.",
                v19_="- `help`: lists the commands.",
            ),
        ]
        return "\n".join(line for line in lines if line)

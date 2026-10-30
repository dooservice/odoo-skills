"""`odoo-guidelines/guidelines/command_line.md`: odoo-bin options, the shell and the subcommands."""

from __future__ import annotations

from ..version import OdooVersion
from .command_line_commands import CommandList
from .lead import GuidedDocument


class CommandLine(GuidedDocument):
    path = "odoo-guidelines/guidelines/command_line.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        save = version.pick(v16_19="`-s`/`--save`", v20="`--save`")
        return {
            **super().values(version),
            "config_sources": version.pick(
                v16_18="Without `-c`, `odoo-bin` reads the file named by\n"
                f"  `ODOO_RC`, else `~/.odoorc`; {save} writes the current options to it.",
                v19_="Without `-c`, `odoo-bin` reads the file named by\n"
                f"  `ODOO_RC`, else `~/.odoorc`; {save} writes the current options to it. Each\n"
                "  option of the file can also come from an `ODOO_<OPTION>` environment variable\n"
                "  (`ODOO_ADDONS_PATH`), and the connection from `PGHOST`, `PGUSER`, `PGDATABASE`.",
            ),
            "reinit": version.pick(
                v16_18="",
                v19_="\n- `--reinit library` reloads the data files of the module and of the modules that\n"
                "  depend on it as on install, `noupdate` records included: what users changed in them\n"
                "  is lost.",
            ),
            "demo_option": version.pick(
                v16_18="A new database gets demo data unless `-i` runs with `--without-demo=all` (or a\n"
                "  comma-separated list of modules).",
                v19_="A new database gets no demo data unless created with `--with-demo`;\n"
                "  `odoo-bin module force-demo` adds it later.",
            ),
            "dev_option": version.pick(
                v16_18="`--dev=all` while developing, never on production: `reload` restarts the server\n"
                "  when Python files change, `xml` reads views and templates from the files instead\n"
                "  of the database, `qweb` logs the compiled template on a QWeb error.",
                v19_="`--dev=all` (or `ODOO_DEV=all`) while developing, never on production: `reload`\n"
                "  restarts the server when Python files change, `xml` reads views and templates\n"
                "  from the files instead of the database, `qweb` logs the compiled template on a\n"
                "  QWeb error, `access` logs the traceback of access errors; `replica` (not part of\n"
                "  `all`) simulates a read-only database replica.",
            ),
            "shell_file": version.pick(
                v16_18="",
                v19_="\n- `--shell-file=startup.py` runs a file before the console opens.",
            ),
            "commands": CommandList().render(version),
        }

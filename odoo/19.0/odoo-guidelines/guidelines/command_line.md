Key names in 19.0: `odoo-bin -c odoo.conf -d library_dev -u library --stop-after-init`; no demo data unless `--with-demo`; `ODOO_<OPTION>` environment variables; `--reinit`; `odoo-bin shell` then roll back; subcommands `db`, `module`, `i18n`, `upgrade_code`.

Sections of this file:

- [Run odoo-bin with explicit options](#run-odoo-bin-with-explicit-options)
- [Inspect a database with odoo-bin shell, then roll back](#inspect-a-database-with-odoo-bin-shell-then-roll-back)
- [Use the odoo-bin subcommand made for the task](#use-the-odoo-bin-subcommand-made-for-the-task)

# Run odoo-bin with explicit options

Pass the configuration file, the database and the modules on every command: an
`odoo-bin` that falls back on defaults may update another database, or load another
copy of the module.

```sh
odoo-bin -c odoo.conf -d library_dev -u library --stop-after-init
```

- `-c odoo.conf` reads the options from the `[options]` section of that file; its keys
  are the option names with underscores (`addons_path`, `db_name`, `http_port`,
  `workers`). Without `-c`, `odoo-bin` reads the file named by
  `ODOO_RC`, else `~/.odoorc`; `-s`/`--save` writes the current options to it. Each
  option of the file can also come from an `ODOO_<OPTION>` environment variable
  (`ODOO_ADDONS_PATH`), and the connection from `PGHOST`, `PGUSER`, `PGDATABASE`.
- `--addons-path` lists every folder holding modules, comma-separated, the `addons`
  folder of the Odoo repository included; when two folders hold a module of the same
  name, the first one wins.
- `-d` names the database. `-i library` installs and `-u library` updates
  (comma-separated lists; `all` updates every installed module); both need `-d`.
- `--reinit library` reloads the data files of the module and of the modules that
  depend on it as on install, `noupdate` records included: what users changed in them
  is lost.
- `--stop-after-init` exits once the modules are loaded (and the tests run): use it in
  scripts and CI, never leave a server running by accident.
- A new database gets no demo data unless created with `--with-demo`;
  `odoo-bin module force-demo` adds it later.
- `--log-level=debug` (or `debug_sql`, `debug_rpc`, `warn`, `error`) sets the root
  level; `--log-handler=odoo.addons.library:DEBUG` raises one logger only, which keeps the
  log readable.
- `--dev=all` (or `ODOO_DEV=all`) while developing, never on production: `reload`
  restarts the server when Python files change, `xml` reads views and templates
  from the files instead of the database, `qweb` logs the compiled template on a
  QWeb error, `access` logs the traceback of access errors; `replica` (not part of
  `all`) simulates a read-only database replica.
- `--test-enable` and `--test-tags` run tests (see
  [Select tests with test tags](tests.md#select-tests-with-test-tags)).

# Inspect a database with odoo-bin shell, then roll back

`odoo-bin shell -c odoo.conf -d library_dev` opens a Python console with `env` (the
superuser) and `self` (`env.user`).

- Every change is rolled back when the console exits. Persist one only on purpose,
  with `env.cr.commit()`, and never on production without a backup.
- Run a script with `odoo-bin shell -c odoo.conf -d library_dev < fix_books.py`: the
  script gets the same `env`, and its changes are rolled back too unless it commits.
- `--shell-file=startup.py` runs a file before the console opens.
- `--shell-interface=ipython` (or `ptpython`, `bpython`, `python`) picks the console.
- Prefer a migration script to a shell fix for anything every database needs; a shell
  fix is for one database.

# Use the odoo-bin subcommand made for the task

`odoo-bin <command> --help` lists each command's options. The commands of this version:

- `server`: the default when no command is given; runs the HTTP server.
- `shell`: a Python console on a database (see above).
- `scaffold library ./addons`: creates a module skeleton (`-t` names another template).
- `db init|load|dump|duplicate|rename|drop`: manages a database together with its
  filestore; `db init library_dev --with-demo` creates one, `db load -n` neutralizes
  the restored copy.
- `neutralize -d library_copy`: on a copy of production, disables mail servers and
  scheduled actions and runs the `data/neutralize.sql` of every installed module;
  `--stdout` prints the SQL instead.
- `cloc -d library_dev` (or `-p <module path>`): counts the lines of custom code.
- `populate -d library_dev --models library.book --factors 10`: multiplies existing
  records by duplicating them, for performance tests; never on production.
- `upgrade_code --addons-path ./addons --dry-run`: rewrites module source to the APIs
  of this version with the scripts shipped in `odoo/upgrade_code` (`--from` and `--to`
  select them); a best effort, so review its diff.
- `i18n export|import|loadlang`: translation files and languages (see
  [Export terms with odoo-bin, never by hand](translations.md#export-terms-with-odoo-bin-never-by-hand)).
- `module install|upgrade|uninstall|force-demo`: changes modules of a database
  without starting the server.
- `deploy <module path> <url>`: uploads a module to a running server through
  `base_import_module`, which loads its data files, never its Python code.
- `obfuscate`: encrypts the values of chosen fields in a database copy before it is
  shared, and decrypts them with `--unobfuscate`.
- `start`: starts a server on the modules of the current folder, for a quick trial.
- `help`: lists the commands.

# Run odoo-bin with explicit options

Pass the configuration file, the database and the modules on every command: an
`odoo-bin` that falls back on defaults may update another database, or load another
copy of the module.

```sh
odoo-bin -c odoo.conf -d library_dev -u library --stop-after-init
```

- `-c odoo.conf` reads the options from the `[options]` section of that file; its keys
  are the option names with underscores (`addons_path`, `db_name`, `http_port`,
  `workers`). $config_sources
- `--addons-path` lists every folder holding modules, comma-separated, the `addons`
  folder of the Odoo repository included; when two folders hold a module of the same
  name, the first one wins.
- `-d` names the database. `-i library` installs and `-u library` updates
  (comma-separated lists; `all` updates every installed module); both need `-d`.$reinit
- `--stop-after-init` exits once the modules are loaded (and the tests run): use it in
  scripts and CI, never leave a server running by accident.
- $demo_option
- `--log-level=debug` (or `debug_sql`, `debug_rpc`, `warn`, `error`) sets the root
  level; `--log-handler=odoo.addons.library:DEBUG` raises one logger only, which keeps the
  log readable.
- $dev_option
- `--test-enable` and `--test-tags` run tests (see
  [Select tests with test tags](tests.md#select-tests-with-test-tags)).

# Inspect a database with odoo-bin shell, then roll back

`odoo-bin shell -c odoo.conf -d library_dev` opens a Python console with `env` (the
superuser) and `self` (`env.user`).

- Every change is rolled back when the console exits. Persist one only on purpose,
  with `env.cr.commit()`, and never on production without a backup.
- Run a script with `odoo-bin shell -c odoo.conf -d library_dev < fix_books.py`: the
  script gets the same `env`, and its changes are rolled back too unless it commits.$shell_file
- `--shell-interface=ipython` (or `ptpython`, `bpython`, `python`) picks the console.
- Prefer a migration script to a shell fix for anything every database needs; a shell
  fix is for one database.

# Use the odoo-bin subcommand made for the task

`odoo-bin <command> --help` lists each command's options. The commands of this version:

$commands

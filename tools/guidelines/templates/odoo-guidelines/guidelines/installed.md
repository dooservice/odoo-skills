# Changes to an installed module

A module that is installed in a database that matters (production, or a clone of it)
already has its tables, its XML records and its users' data. A change has to work on
that database after `odoo-bin -u <module>`, not only on a fresh install. What a fix
may change without a new module version is in
[Changes in a stable version](stable.md#changes-in-a-stable-version).

- Bump `version` in the manifest whenever the change needs a migration script or a
  data fix, and write the script (see
  [Write a migration script for every data change between two versions](migrations.md#write-a-migration-script-for-every-data-change-between-two-versions)).
  A renamed field without a script loses its data: the update drops the old column
  and creates an empty one.
- Never rename or remove a stored field, a model or an XML id that data may
  reference without a migration. Prefer adding a new field and computing it from
  the old one.
- Changing a `required=True` or a `selection` on a field with data: check the
  existing rows first (`odoo-bin shell`, a `search_count`), or the update fails
  or leaves invalid records.
- Public model methods (no `_` prefix) may be called by other modules or
  integrations: don't change their signature without checking every caller.
- Test the update on a copy of real data, such as a neutralized clone of production
  (`odoo-bin neutralize -d library_copy`), before it reaches production.
- A module that calls an external service or sends anything on its own ships
  `data/neutralize.sql`, which `odoo-bin neutralize` runs on every copy to disable its
  credentials and scheduled actions. It is not listed in the manifest: a listed `.sql`
  file would run on the production database too.

# List data files in the order they reference each other

`-i` and `-u` load the manifest's `data` files in the order listed, then its `demo`
files. A file that references an XML id (`ref="..."`, `%(action_library_book)d`) loaded
by a later file fails on a new database, even when it works on yours.

- Order them: groups, then `security/ir.model.access.csv`, then record rules, then
  `data/`, then `views/` (each action before the menus that open it), then wizards and
  reports.
- A CSV file is named after its model (`ir.model.access.csv`, `library.genre.csv`) and
  needs an `id` column, or an update cannot match its rows.
- Every `-u` reloads every listed file: data records are rewritten from the XML, and
  records of the module whose XML id is no longer in any of its files are deleted,
  unless they are `noupdate`.
- No `.sql` data files: they run again on every update, outside the ORM.

# Mark records that users may change as noupdate

Wrap data that users are expected to edit (sequences, mail templates, default
configuration, stages) in `<odoo noupdate="1">` or `<data noupdate="1">`. Without it,
every `-u` overwrites their changes with the XML.

- A `noupdate` record is created on install and never written again, even when its XML
  changes: fix an installed one in a `post-` migration script.
- A `noupdate` record that a user deleted is created again by the next update; add
  `forcecreate="0"` on the `<record>` to leave it deleted.
- `<function>` inside a `noupdate` block runs on install only; outside one, it runs on
  every update, so make it safe to run twice.
- `<delete>` runs on every load of its file, `noupdate` or not: a
  `<delete model="library.genre" search="[('name', '=', 'Old')]"/>` also removes the
  matching records users created. Delete by `id` instead.

# Keep demo data out of what the module needs

Files under the manifest's `demo` key load only into a database created with demo
data$demo_default. They are always loaded as `noupdate`.

- Code, views and data files never depend on a demo record: on a database without demo
  data the reference fails.
- Demo records get their own XML ids, never the ids of data records.
- Tests create their own records instead of reading demo data
  (see [Tests](tests.md#tests)).$force_demo

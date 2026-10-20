# Changes to an installed module

A module that is installed in a database that matters (production, or a clone of it)
already has its tables, its XML records and its users' data. A change has to work on
that database after `odoo-bin -u <module>`, not only on a fresh install.

- Bump `version` in the manifest whenever the change needs a migration script or a
  data fix, and write the script (see the `odoo-upgrade` skill). A renamed field
  without a script loses its data: the ORM drops the old column and creates an
  empty one.
- Never rename or remove a stored field, a model or an XML id that data may
  reference without a migration. Prefer adding a new field and computing it from
  the old one.
- Records inside `noupdate="1"` are created once and never updated again: changing
  them in the XML has no effect on an installed database. Fix them in a migration
  script, or tell the user what to change by hand.
- Changing a `required=True` or a `selection` on a field with data: check the
  existing rows first (`odoo-bin shell`, a `search_count`), or the update fails
  or leaves invalid records.
- Public model methods (no `_` prefix) may be called by other modules or
  integrations: don't change their signature without checking every caller.
- Don't modify existing translatable source terms for a typo: that breaks their
  translations. Add the new term and leave the old one when wording matters.
- Test the update on a copy of real data, such as a neutralized clone of production,
  before it reaches production.

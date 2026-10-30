Key names in 16.0: a fix to a stable version is minimal: no change to a public method signature, no stored field added, removed, renamed or retyped, existing XML ids kept, `noupdate="1"` records fixed by a migration script, source terms left as they are.

Sections of this file:

- [Changes in a stable version](#changes-in-a-stable-version)

# Changes in a stable version

A stable version is a module version that is already installed in a database that
matters (production, or a clone of it). Code reaches that database first and the
module update (`odoo-bin -u <module>`) may come later, or on another day for another
database. A change to a stable version is a bug fix; an improvement or a feature goes
to a new module version, shipped with its migration (see
[Changes to an installed module](installed.md#changes-to-an-installed-module)).

- Value over risk: keep the change minimal and strictly about the bug. If the risk is
  high or the value low, it belongs in the next module version, not in the fix.
- No improvements, technical or functional, and no purely cosmetic changes
  (formatting, PEP 8, restyling). Match the surrounding code's style.
- Public model methods (no `_` prefix) are API for other modules, integrations and
  RPC clients: never change their signature. Avoid changing private signatures too,
  extension modules override them.
- No data-model change: never add, remove, or rename a stored field, and never change
  its type. Until the module is updated, the code reads a column the table lacks
  and every read of the model's records fails; once it is updated, a removed or
  renamed field has its column dropped with its data, and a type change is a
  PostgreSQL cast that stops the update when the cast fails. Compatible tweaks (`ondelete`, `size`) are allowed
  when needed; a non-stored computed field may be added if really necessary.
- Keep the XML ids of existing data, and don't delete data records that user data may
  reference, unless essential and the records were `noupdate` from the start: the
  update deletes every record of the module whose XML id is no longer loaded and is
  not `noupdate`.
- Records inside `noupdate="1"` are created once and never updated again: changing
  them in the XML has no effect on an installed database. Fix them in a migration
  script, or tell the user what to change by hand.
- Change XML (views, menus, default data) only when inevitable, and then the Python
  code must not depend on the change: a database that has not been updated must
  keep working.
- A fix may need an explicit module update as long as users who don't run it are
  safe. A critical security fix must work with a code deploy and restart alone.
- Don't modify existing translatable source terms, even for a typo: that breaks
  their translations. Correct a term in the next module version, or add an
  English-to-English translation in the fix. Adding or deleting terms is fine.

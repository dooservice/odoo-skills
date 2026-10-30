Key names in $version:

$essentials

Sections of this file:

$sections

# Registries in $version

A registry is a named, ordered map that the web client reads to find its extensions:
the field widgets, the views, the services, the systray items. Adding an entry is how
an addon extends the client without patching it. `registry` comes from
`@web/core/registry`, and each kind of extension is a category of it:
`registry.category("systray")`.

- `add(key, value, { sequence, force })` adds an entry and returns the category, so calls
  chain. `sequence` orders the entries (lower first, default 50).
- Adding a key that already exists throws `DuplicatedKeyError`. Replace an entry only
  with `force: true`, and only when replacing is the point; without `sequence`, the
  replaced entry keeps its old one.
- `get(key)` throws `KeyNotFoundError` for a missing key; `get(key, defaultValue)` returns
  the default instead. `contains(key)` tests, `remove(key)` deletes.
- `getAll()` returns the values and `getEntries()` the `[key, value]` pairs, both sorted
  by sequence.
- Every `add` and `remove` triggers an `UPDATE` event (`detail` holds `operation`, `key`
  and `value`); listen with `addEventListener("UPDATE", ...)` to follow late additions.$registry_validation
- A category can have subcategories: `registry.category("debug").category("form")`.

# Prefix every registry key with the module

Write `registry.category("fields").add("my_module_rating", ...)`, never a bare
`add("rating", ...)`. Keys are global across all installed modules: a bare key collides
with Odoo's own entries or another addon's, and the collision throws at load time, or
silently replaces the other entry when `force` is set.

Exception: a key that the framework looks up by a fixed name, such as a field widget
named in a view arch, an action `tag`, or a server exception name in
`category("error_dialogs")`, is that name; prefix the name itself
(`widget="my_module_rating"`, `tag="my_module.dashboard"`).

# Fields, views and view widgets

These three are detailed in [views.md](views.md); in short:

$view_entries
- `category("form_compilers")` holds `{ selector, fn }`: when the form compiler meets an
  arch node matching `selector`, `fn(node, params)` (with `this` the compiler) returns
  the compiled element. Entries are tried before the built-in form compilers, and the
  first match wins. Use it for a custom arch tag in form views
  (`registry.category("form_compilers").add("my_module_gauge", { selector: "my_gauge", fn: compileGauge })`).

# Control panel menus

$search_menus

# Formatters, parsers and the sample server

- `category("formatters")` maps a field type to a function `(value, options) => string`
  that renders it as text, and `category("parsers")` maps a type to a function that turns
  the user's text back into a value and throws on invalid input. Read them through the
  registry, not by import, so an addon's override applies:
  `registry.category("formatters").get(field.type, (value) => value)(value, { digits })`.
  $formatter_extras
- `category("sample_server")` answers the RPCs of the sample data shown in an empty view
  (`sample="1"` on the arch). The key is `"<model>/<method>"` or `"<method>"`, and the
  entry a function called with the RPC params that returns fake data; add one when a
  custom view calls a method the sample server does not know, or the sample view shows
  an error.

# Frontend registries

$frontend_registries

# Registries of this version only

$version_registries

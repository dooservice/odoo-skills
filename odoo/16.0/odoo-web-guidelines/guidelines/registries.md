Key names in 16.0:

- API: `registry` from `@web/core/registry`, `add(key, value, { sequence, force })`, `DuplicatedKeyError`, `KeyNotFoundError`, `getAll`, `getEntries`.
- Keys are prefixed with the module.
- Categories here: `fields` (the component class), `views`, `view_widgets`, control panel menus, `formatters`, `parsers`, `sample_server`, the frontend registries and those of this version only.
- Navbar, actions, command palette, debug menu, errors and effects: [registries_webclient.md](registries_webclient.md).

Sections of this file:

- Registries in 16.0
- Prefix every registry key with the module
- Fields, views and view widgets
- Control panel menus
- Formatters, parsers and the sample server
- Frontend registries
- Registries of this version only

# Registries in 16.0

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
  and `value`); listen with `addEventListener("UPDATE", ...)` to follow late additions.
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

- `category("fields")` maps a field widget name (the `widget` of `<field>`) or a field
  type to the component class that renders it; the class carries its own statics
  (`supportedTypes`, `extractProps`, `displayName`).
- `category("views")` maps a view type, or a `js_class` named on the arch root, to the
  view descriptor (`type`, `Controller`, `Renderer`, `Model`, `ArchParser`, `props`, ...).
  A `js_class` that is not registered is ignored without a warning.
- `category("view_widgets")` maps the `name` of a `<widget name="..."/>` to its component
  class, which may carry a static `extractProps({ attrs })`.
- `category("form_compilers")` holds `{ selector, fn }`: when the form compiler meets an
  arch node matching `selector`, `fn(node, params)` (with `this` the compiler) returns
  the compiled element. Entries are tried before the built-in form compilers, and the
  first match wins. Use it for a custom arch tag in form views
  (`registry.category("form_compilers").add("my_module_gauge", { selector: "my_gauge", fn: compileGauge })`).

# Control panel menus

- `category("action_menus")` adds items to the Action menu of a view: `{ Component,
  getProps(props, env) }`, where `getProps` returns the item's props, or a falsy value to
  hide it.
- `category("favoriteMenu")` adds items to the Favorites menu: `{ Component, groupNumber,
  isDisplayed }`. `isDisplayed(env)` is called without `await`: make it synchronous,
  because a promise always counts as true.

# Formatters, parsers and the sample server

- `category("formatters")` maps a field type to a function `(value, options) => string`
  that renders it as text, and `category("parsers")` maps a type to a function that turns
  the user's text back into a value and throws on invalid input. Read them through the
  registry, not by import, so an addon's override applies:
  `registry.category("formatters").get(field.type, (value) => value)(value, { digits })`.
  A formatter receives its options from the caller; nothing reads them from the arch.
- `category("sample_server")` answers the RPCs of the sample data shown in an empty view
  (`sample="1"` on the arch). The key is `"<model>/<method>"` or `"<method>"`, and the
  entry a function called with the RPC params that returns fake data; add one when a
  custom view calls a method the sample server does not know, or the sample view shows
  an error.

# Frontend registries

The frontend (website, portal, login) has its own registries, loaded by
`web.assets_frontend`.

- `category("public_root_widgets")` holds `{ Widget, selector }`: the public root
  instantiates `Widget` on every element matching `selector`. It is the low-level hook
  behind public widgets; write a public widget (`publicWidget.registry`, see
  [website.md](website.md)) rather than an entry here.
- `category("error_notifications")` turns server errors into notifications for visitors
  (see Error handling in [registries_webclient.md](registries_webclient.md)).

# Registries of this version only

- `category("wowlToLegacyServiceMappers")` maps a legacy service name to a function
  `(legacyEnv) => service` that exposes an Owl service to the legacy widgets still in
  this version. Add to it only when a legacy widget must call a new service.
- `category("preloadedData")` holds `{ loadOnTypes, preload(orm, record, fieldName),
  extraMemoizationKey }`, keyed by a widget or field type: data a field needs before it
  renders (the options of a selection, the stages of a status bar), loaded with the
  record.
- `category("domain_selector/fields")` maps a field type to the component that edits a
  value of that type in the domain editor, and `category("domain_selector/operator")`
  holds the operators it offers (`{ category, label, value, onDidChange, matches }`).

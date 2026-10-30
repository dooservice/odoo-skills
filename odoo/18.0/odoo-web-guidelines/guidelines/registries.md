Key names in 18.0:

- API: `registry` from `@web/core/registry`, `add(key, value, { sequence, force })`, `DuplicatedKeyError`, `KeyNotFoundError`, `getAll`, `getEntries`, `addValidation` (an Owl props-style schema), `useRegistry`.
- Keys are prefixed with the module.
- Categories here: `fields`, `views`, `view_widgets`, `form_compilers`, `cogMenu`, `favoriteMenu`, `formatters`, `parsers`, `sample_server`, the frontend registries and those of this version only.
- Navbar, actions, command palette, debug menu, errors and effects: [registries_webclient.md](registries_webclient.md).

Sections of this file:

- Registries in 18.0
- Prefix every registry key with the module
- Fields, views and view widgets
- Control panel menus
- Formatters, parsers and the sample server
- Frontend registries
- Registries of this version only

# Registries in 18.0

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
- `addValidation(schema)` sets an Owl props-style schema that every entry must match
  (`{ component: { type: Function }, ... }`); it is checked only in debug mode, so run
  with `?debug=1` while developing. The categories `services`, `main_components`,
  `fields`, `views` and `view_widgets` have one.
- `useRegistry(category)` (`@web/core/registry_hook`) gives a component a reactive
  `{ entries }` that follows additions and removals, but not a replaced key.
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
  type to a descriptor `{ component, supportedTypes, extractProps, ... }`.
- `category("views")` maps a view type, or a `js_class` named on the arch root, to the
  view descriptor (`type`, `Controller`, `Renderer`, `Model`, `ArchParser`, `props`, ...).
  A `js_class` that is not registered throws once the lazy bundle is loaded.
- `category("view_widgets")` maps the `name` of a `<widget name="..."/>` to a descriptor
  `{ component, extractProps, ... }`.
- `category("form_compilers")` holds `{ selector, fn }`: when the form compiler meets an
  arch node matching `selector`, `fn(node, params)` (with `this` the compiler) returns
  the compiled element. Entries are tried before the built-in form compilers, and the
  first match wins. Use it for a custom arch tag in form views
  (`registry.category("form_compilers").add("my_module_gauge", { selector: "my_gauge", fn: compileGauge })`).

# Control panel menus

- `category("cogMenu")` adds items to the gear menu next to the breadcrumb: `{ Component,
  groupNumber, isDisplayed }`. `isDisplayed(env)` may be async (`env.config.viewType ===
  "list"` is the usual test), and `groupNumber` places the item in a group:
  `STATIC_ACTIONS_GROUP_NUMBER` (1) or `ACTIONS_GROUP_NUMBER` (100), both from
  `@web/search/action_menus/action_menus`. Items are keyed by their component's class
  name, so two entries must not share a component class name.
- `category("favoriteMenu")` adds items to the Favorites part of the search menu:
  `{ Component, groupNumber, isDisplayed }`. Here `isDisplayed(env)` is called without
  `await`: make it synchronous, because a promise always counts as true.

# Formatters, parsers and the sample server

- `category("formatters")` maps a field type to a function `(value, options) => string`
  that renders it as text, and `category("parsers")` maps a type to a function that turns
  the user's text back into a value and throws on invalid input. Read them through the
  registry, not by import, so an addon's override applies:
  `registry.category("formatters").get(field.type, (value) => value)(value, { digits })`.
  A formatter may carry a static `extractOptions({ attrs, options })` that turns the
  arch attributes into its options.
- `category("sample_server")` answers the RPCs of the sample data shown in an empty view
  (`sample="1"` on the arch). The key is `"<model>/<method>"` or `"<method>"`, and the
  entry a function called with the RPC params that returns fake data; add one when a
  custom view calls a method the sample server does not know, or the sample view shows
  an error.

# Frontend registries

The frontend (website, portal, login) has its own registries, loaded by
`web.assets_frontend`.

- `category("public_components")` holds Owl components that a page mounts with
  `<owl-component name="my_module.book_card" props='{"bookId": 4}'/>`: the key is the
  `name` attribute and the props are the JSON of `props`. The `public_component` service
  mounts them when the page starts. Use it to put an Owl component in a QWeb page.
- Public widgets are registered in `publicWidget.registry`, not in a category (see
  [website.md](website.md)).
- `category("error_notifications")` turns server errors into notifications for visitors
  (see Error handling in [registries_webclient.md](registries_webclient.md)).

# Registries of this version only

- `category("kanban_header_config_items")` holds the entries of the gear menu of a
  kanban column: `{ label, method, isVisible, class }`, where `method` names a method
  of the kanban header and `isVisible` may be a function of `{ permissions, props }`.

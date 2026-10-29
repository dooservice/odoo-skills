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

# Systray, user menu and main components

- `category("systray")` holds the items at the right of the navbar: `{ Component, props,
  isDisplayed }`, where `isDisplayed(env)` hides the item when it returns false. Items
  are shown in reverse order of sequence: a higher sequence is further left, and the
  user menu sits at sequence 0, rightmost.
  `registry.category("systray").add("my_module.timer", { Component: Timer }, { sequence: 30 })`.
- `category("user_menuitems")` holds functions that build the entries of the user menu
  each time it opens: `(env) => entry`, called with the environment. The entry is
  `{ type: "item", id, description, callback, href, sequence }`, where `type` is
  `"item"`, `"switch"` (with `isChecked`) or `"separator"`. The menu is
  sorted by the `sequence` the function returns (default 100), not by the registry
  sequence.
- `category("main_components")` holds the components mounted once at the root of the
  client, next to the action: `{ Component, props }`. Use it for an overlay that lives
  for the whole session (a call window, a global banner), not for a dialog.

# Client actions and action handlers

- `category("actions")` maps the `tag` of an `ir.actions.client` to what runs it. A
  component class is mounted as the main content and receives `action` (its `params`
  under `action.params`) in its props.
  A function `(env, action) => ...`
  runs instead, and an action it returns is executed next. A component can set `static target = "new"` to open in a
  dialog.
- `category("action_handlers")` maps a new action `type` to a function
  `({ env, action, options }) => ...`. The standard types (`ir.actions.act_window`,
  `ir.actions.server`, ...) never reach it; it exists for a module that defines its own
  `ir.actions.*` model.
- `category("ir.actions.report handlers")` holds functions
  `(action, options, env) => ...` called before a report action is run; one that
  returns a truthy value has handled the report and stops the default download. Use it
  to print to a device or to open a preview.

# Command palette

- `category("command_provider")` holds `{ namespace, provide }`, where
  `provide(env, options)` (`options.searchValue` is what the user typed) returns the commands to list, each `{ name, action, category }`. `namespace` is the prefix the
  user types (`"/"` for menus, `"#"` or `"@"` in some modules); without it the provider
  feeds the default list.
- `category("command_categories")` holds `{ namespace, name }` keyed by the `category`
  a command names; the registry sequence orders the groups.
- `category("command_setup")` holds the setup of a namespace, keyed by it:
  `{ placeholder, emptyMessage, name }`.

# Debug menu

- `category("debug")` has one subcategory per context: `"default"` (always), `"action"`,
  `"view"`, `"form"`. Each entry is a function
  `({ env, accessRights, ...context }) => item` that returns `null` to hide the item.
  The item is `{ type: "item", description, callback, sequence }` or
  `{ type: "component", Component, props, sequence }`, or
  `{ type: "separator" }`;
  items are sorted by sequence, default 1000. `accessRights` holds
  `canEditView`, `canSeeRecordRules` and `canSeeModelAccess`.
  `registry.category("debug").category("form").add("my_module.recompute", recomputeItem)`.
- Debug items are not grouped in this version: a `{ type: "separator" }` item separates
  them.

# Error handling

- `category("error_handlers")` holds functions `(env, error, originalError) => boolean`,
  tried in sequence order on every uncaught error; the first one that returns true
  stops the chain. Give a custom handler an explicit sequence: at the default 50 it
  runs before the RPC handler (97) and the default handler (100).
  A handler that throws breaks error handling: return false instead.
- `category("error_dialogs")` maps a server exception, by its Python dotted name, to the
  dialog that shows it:
  `registry.category("error_dialogs").add("odoo.addons.my_module.models.library_book.LendError", LendErrorDialog)`.
  The dialog receives `name`, `message`, `traceback`, `exceptionName` and `data`. The
  session-expired key is `odoo.http.SessionExpiredException`.
- `category("error_notifications")` maps an exception name to notification options
  (`{ title, message, type, sticky }`) shown instead of a dialog; it is checked before
  `error_dialogs` and is only filled in the frontend bundle, so website visitors get a
  notification where a user would get a dialog.

# Effects, dialogs and lazy components

- `category("effects")` holds functions `(env, params)`
  that return `{ Component, props }`, shown by
  `effect.add({ type: "my_module_confetti", ... })`; returning nothing shows nothing. The built-in `rainbow_man` is the default type.
- Dialogs have no registry in this version: open one with the `dialog` service.
- `category("lazy_components")` holds components that live in a lazily loaded bundle.
  `<LazyComponent bundle="'my_module.assets_heavy'" Component="'my_module.Chart'"
  props="..."/>` loads the bundle, then mounts the entry its files added with
  `registry.category("lazy_components").add("my_module.Chart", Chart)`. Use it for a big
  library (a chart engine, an editor) the client should not load at startup.

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
  (see Error handling).

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

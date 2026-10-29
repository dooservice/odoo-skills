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

# Systray, user menu and main components

- `category("systray")` holds the items at the right of the navbar: `{ Component, props,
  isDisplayed }`, where `isDisplayed(env)` hides the item when it returns false. Items
  are shown in reverse order of sequence: a higher sequence is further left, and the
  user menu sits at sequence 0, rightmost.
  `registry.category("systray").add("my_module.timer", { Component: Timer }, { sequence: 30 })`.
- `category("user_menuitems")` holds functions that build the entries of the user menu
  each time it opens: $user_menuitem. The entry is
  `{ type: "item", id, description, callback, href, sequence }`, where `type` is
  `"item"`, `"switch"` (with `isChecked`) or `"separator"`$user_menu_types. The menu is
  sorted by the `sequence` the function returns (default 100), not by the registry
  sequence.
- `category("main_components")` holds the components mounted once at the root of the
  client, next to the action: `{ Component, props }`. Use it for an overlay that lives
  for the whole session (a call window, a global banner), not for a dialog.

# Client actions and action handlers

- `category("actions")` maps the `tag` of an `ir.actions.client` to what runs it. A
  component class is mounted as the main content and receives `action` (its `params`
  under `action.params`) in its props$action_props.
  A function $action_function
  runs instead, and an action it returns is executed next.$action_static
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
  $command_provide returns the commands to list, each `{ name, action, category }`. `namespace` is the prefix the
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
  `{ type: "component", Component, props, sequence }`$debug_item;
  items are sorted by sequence, default 1000. `accessRights` holds
  $debug_rights.
  `registry.category("debug").category("form").add("my_module.recompute", recomputeItem)`.
- $debug_section

# Error handling

- `category("error_handlers")` holds functions `(env, error, originalError) => boolean`,
  tried in sequence order on every uncaught error; the first one that returns true
  stops the chain. Give a custom handler an explicit sequence: at the default 50 it
  runs before the RPC handler (97) and the default handler (100).
  $error_handler_throw
- `category("error_dialogs")` maps a server exception, by its Python dotted name, to the
  dialog that shows it:
  `registry.category("error_dialogs").add("odoo.addons.my_module.models.library_book.LendError", LendErrorDialog)`.
  The dialog receives `name`, `message`, `traceback`, `exceptionName` and `data`. The
  session-expired key is `$session_expired`.
- `category("error_notifications")` maps an exception name to notification options
  (`{ title, message, type, sticky }`) shown instead of a dialog; it is checked before
  `error_dialogs` and is only filled in the frontend bundle, so website visitors get a
  notification where a user would get a dialog.

# Effects, dialogs and lazy components

- `category("effects")` holds functions $effect_signature
  that return `{ Component, props }`, shown by
  `effect.add({ type: "my_module_confetti", ... })`; returning nothing shows nothing. The built-in `rainbow_man` is the default type.
- $dialogs
- `category("lazy_components")` holds components that live in a lazily loaded bundle.
  `<LazyComponent bundle="'my_module.assets_heavy'" Component="'my_module.Chart'"
  props="..."/>` loads the bundle, then mounts the entry its files added with
  `registry.category("lazy_components").add("my_module.Chart", Chart)`. Use it for a big
  library (a chart engine, an editor) the client should not load at startup.

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

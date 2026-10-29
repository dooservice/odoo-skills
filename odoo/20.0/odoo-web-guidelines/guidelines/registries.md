# Registries in 20.0

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
- `addValidation(schema)` sets an Owl 3 type (`t.object({ component: t.component() })`)
  that every entry must match; it is checked only in debug mode, so run with `?debug=1`
  while developing. The categories `services`, `main_components`, `fields`, `views` and
  `view_widgets` have one.
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

# Systray, user menu and main components

- `category("systray")` holds the items at the right of the navbar: `{ Component, props,
  isDisplayed }`, where `isDisplayed(env)` hides the item when it returns false. Items
  are shown in reverse order of sequence: a higher sequence is further left, and the
  user menu sits at sequence 0, rightmost.
  `registry.category("systray").add("my_module.timer", { Component: Timer }, { sequence: 30 })`.
- `category("user_menuitems")` holds functions that build the entries of the user menu
  each time it opens: `() => entry`, run inside the menu's scope, so they read services with
  `useService` instead of an `env` argument. The entry is
  `{ type: "item", id, description, callback, href, sequence }`, where `type` is
  `"item"`, `"switch"` (with `isChecked`) or `"separator"`, or
  `"component"` (with `contentComponent`). The menu is
  sorted by the `sequence` the function returns (default 100), not by the registry
  sequence.
- `category("main_components")` holds the components mounted once at the root of the
  client, next to the action: `{ Component, props }`. Use it for an overlay that lives
  for the whole session (a call window, a global banner), not for a dialog.

# Client actions and action handlers

- `category("actions")` maps the `tag` of an `ir.actions.client` to what runs it. A
  component class is mounted as the main content and receives `action` (its `params`
  under `action.params`) in its props;
  spread `standardActionServiceProps` (`@web/webclient/actions/action_plugin`) into
  its props.
  A function `(env, action, options) => ...`, run in the action's scope so it can
  call hooks,
  runs instead, and an action it returns is executed next. A component can set `static target = "new"` to open in a
  dialog, `static path = "my-dashboard"` to get a readable URL (`/odoo/my-dashboard`)
  that reopens it, `static displayName` for the breadcrumb, and
  `static extractProps(action)` to turn the action into props.
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
  `provide(options)` (`options.searchValue` is what the user typed) runs in
  the palette's scope, reads services with `useService`, and returns the commands to list, each `{ name, action, category }`. `namespace` is the prefix the
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
  `{ type: "component", Component, props, sequence }`, each with an
  optional `section`;
  items are sorted by sequence, default 1000. `accessRights` holds
  `canEditView` and `canSeeAccess`.
  `registry.category("debug").category("form").add("my_module.recompute", recomputeItem)`.
- `category("debug_section")` names the groups of the debug menu: `{ label,
  sequence }` keyed by the `section` an item names. The built-in sections are `record`,
  `records`, `ui`, `security`, `testing` and `tools`; add a section only when none of them
  fits.

# Error handling

- `category("error_handlers")` holds functions `(env, error, originalError) => boolean`,
  tried in sequence order on every uncaught error; the first one that returns true
  stops the chain. Give a custom handler an explicit sequence: at the default 50 it
  runs before the RPC handler (97) and the default handler (100).
  A handler that throws is logged and stops the chain: return false instead.
- `category("error_dialogs")` maps a server exception, by its Python dotted name, to the
  dialog that shows it:
  `registry.category("error_dialogs").add("odoo.addons.my_module.models.library_book.LendError", LendErrorDialog)`.
  The dialog receives `name`, `message`, `traceback`, `exceptionName` and `data`. The
  session-expired key is `odoo.http.session.SessionExpiredException`.
- `category("error_notifications")` maps an exception name to notification options
  (`{ title, message, type, sticky }`) shown instead of a dialog; it is checked before
  `error_dialogs` and is only filled in the frontend bundle, so website visitors get a
  notification where a user would get a dialog.

# Effects, dialogs and lazy components

- `category("effects")` holds functions `(params)`, with no `env` (they run in the effect's scope and
  call hooks),
  that return `{ Component, props }`, shown by
  `effect.add({ type: "my_module_confetti", ... })`; returning nothing shows nothing. The built-in `rainbow_man` is the default type.
- `category("dialogs")` holds dialogs that core code opens by key without importing
  them; web uses it for `select_create`, the dialog that searches and creates records.
  Open your own dialogs with the `dialog` service instead.
- `category("lazy_components")` holds components that live in a lazily loaded bundle.
  `<LazyComponent bundle="'my_module.assets_heavy'" Component="'my_module.Chart'"
  props="..."/>` loads the bundle, then mounts the entry its files added with
  `registry.category("lazy_components").add("my_module.Chart", Chart)`. Use it for a big
  library (a chart engine, an editor) the client should not load at startup.

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

- `category("public.interactions")` holds `Interaction` subclasses (`@web/public/interaction`):
  each is started on every element matching its `static selector`, and stopped when the
  element leaves the page. It replaces public widgets for new code; see
  [website.md](website.md). The registry is read once when the page starts: add entries
  from a file of the bundle, never later.
  `registry.category("public.interactions").add("my_module.book_card", BookCard)`.
- `category("public_components")` holds Owl components that a page mounts with
  `<owl-component name="my_module.book_card" props='{"bookId": 4}'/>`: the key is the
  `name` attribute and the props are the JSON of `props`; an interaction mounts them.
  Use it to put an Owl component in a QWeb page.
- `category("error_notifications")` turns server errors into notifications for visitors
  (see Error handling).

# Registries of this version only

- `category("group_config_items")` holds the entries of the gear menu of a group header,
  in kanban columns and in grouped lists: `{ label, method, isVisible, class, icon }`,
  where `method` is a function or the name of a method of the menu, and `isVisible` may
  be a function of `{ permissions }`.
- `category("phone_call_handlers")` holds `{ isApplicable(env, params), execute(env,
  params, { fallback }) }`: when the user clicks a phone number, the first entry that is
  applicable places the call (a VoIP module); with none, the browser opens the `tel:`
  link. `params` holds `phoneNumber`, and `resModel` and `resId` when known.
- `category("share_target_items")` holds components extending `ShareTargetItem`
  (`static name`, `static sequence`): the apps offered when files are shared to the
  installed web app; the chosen item receives the `files`.

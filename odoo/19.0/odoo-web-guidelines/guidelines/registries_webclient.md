Key names in 19.0:

- The registry API and the module prefix of every key: [registries.md](registries.md).
- `systray`, `user_menuitems` (`(env) => entry`), `main_components`.
- `actions` (a component, or a function `(env, action, options) => ...`), `action_handlers`, `ir.actions.report handlers`.
- `command_provider` (`provide(env, options)`), `command_categories`, `command_setup`.
- `debug` with its subcategories, `debug_section`, `error_handlers`, `error_dialogs`, `error_notifications`.
- `effects` (`(env, params)`), `dialogs`, `lazy_components`.

Sections of this file:

- Systray, user menu and main components
- Client actions and action handlers
- Command palette
- Debug menu
- Error handling
- Effects, dialogs and lazy components

# Systray, user menu and main components

- `category("systray")` holds the items at the right of the navbar: `{ Component, props,
  isDisplayed }`, where `isDisplayed(env)` hides the item when it returns false. Items
  are shown in reverse order of sequence: a higher sequence is further left, and the
  user menu sits at sequence 0, rightmost.
  `registry.category("systray").add("my_module.timer", { Component: Timer }, { sequence: 30 })`.
- `category("user_menuitems")` holds functions that build the entries of the user menu
  each time it opens: `(env) => entry`, called with the environment. The entry is
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
  spread `standardActionServiceProps` (`@web/webclient/actions/action_service`) into
  its static props.
  A function `(env, action, options) => ...`
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
  `{ type: "component", Component, props, sequence }`, each with an
  optional `section`;
  items are sorted by sequence, default 1000. `accessRights` holds
  `canEditView`, `canSeeRecordRules` and `canSeeModelAccess`.
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
  session-expired key is `odoo.http.SessionExpiredException`.
- `category("error_notifications")` maps an exception name to notification options
  (`{ title, message, type, sticky }`) shown instead of a dialog; it is checked before
  `error_dialogs` and is only filled in the frontend bundle, so website visitors get a
  notification where a user would get a dialog.

# Effects, dialogs and lazy components

- `category("effects")` holds functions `(env, params)`
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

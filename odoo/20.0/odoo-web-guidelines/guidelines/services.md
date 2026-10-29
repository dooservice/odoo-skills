# Services in 20.0

Shared logic lives in plugins: Owl 3 classes extending `Plugin`, registered in the
`services` resource of `@web/core/services` and started once for the application. The
`orm` (`ORM`), `action` (`ActionPlugin`), `notification` (`NotificationPlugin`),
`dialog` (`DialogPlugin`), `effect`, `title`, `ui`, `hotkey`, `localization`,
`overlay` and `popover` are plugins in this version.

`registry.category("services")` still exists as a temporary bridge: a plugin that
replaced a service also registers a service of the old name that returns the plugin,
and services not converted yet (`field`, `name`, `view`, `menu`, `command`, `http`) are
still registry entries, started after the plugins. Use `usePlugin(X)` for a plugin and
`useService("name")` only for a service with no plugin yet.

# Get a service through its hook, never through a global

- In a component or a plugin, a plugin comes from `usePlugin(ORM)` (the class, imported
  from its module) in a field initializer or `setup`, and a service not converted yet
  from `useService("view")`. Both run in the component's scope: a call made after the
  component is destroyed never resolves.
- Registry functions that the framework calls (systray `isDisplayed`, user menu items,
  command providers, error handlers, effects) run in a scope too: call `useService` or
  `usePlugin` inside them instead of reading `env.services`.
- `env.services` holds only the bridged services, for code not converted yet.
- Never store a plugin or a service on `window` or a module-level variable: tests start
  a fresh application, and a global keeps the old one.

# Keep shared logic and shared state out of components

A plugin holds what several components need and what must outlive any one of them: a
cache, a connection, a shared reactive state.

```js
import { Plugin, signal, usePlugin } from "@odoo/owl";
import { ORM } from "@web/core/orm_plugin";
import { services } from "@web/core/services";

export class LibraryPlugin extends Plugin {
    orm = usePlugin(ORM);
    lentCount = signal(0);

    async refresh() {
        this.lentCount.set(await this.orm.searchCount("library.book", [["state", "=", "lent"]]));
    }
}

services.add(LibraryPlugin);
```

- A plugin is a class: its fields and `setup()` run once, and its methods are its API.
  It reaches other plugins with `usePlugin` in a field or in `setup`, which also orders
  their start.
- State is made of signals and proxies, so a component that reads
  `this.library.lentCount()` re-renders when it changes.
- `static sequence` (default 50) orders the start of plugins that do not depend on each
  other.
- Do not register a new `registry.category("services")` entry: that registry is the
  bridge for code written before plugins, and it goes away.
- A component that only one screen uses keeps its logic: a plugin is for what is
  shared.

# Call model methods with the `orm` service

The ORM is the `ORM` plugin (`@web/core/orm_plugin`): `orm = usePlugin(ORM)`, or
`useService("orm")` through the bridge. Methods: `call`, `create(model, records)`,
`read(model, ids, fields)`, `search`, `searchRead(model, domain, fields)`,
`searchCount`, `unlink`, `write(model, ids, values)`, `formattedReadGroup(model,
domain, groupby, aggregates)`, and the web methods `webRead(model, ids, {
specification })`, `webSearchRead(model, domain, { specification })`,
`webReadGroup(model, domain, groupby, aggregates)`, `webSave`, `webUnlink`.

- `orm.call(model, method, args, kwargs)` calls any public model method; the others
  are shortcuts. The context of the user is added for you: pass only the keys to change,
  in `kwargs.context`.
- `orm.silent.call(...)` does not show the loading indicator, for background refreshes.
- Never call a method whose name starts with `_`: the server refuses it. Expose a
  public method (with the access checks it needs) instead.

# Call a route with `rpc`

`import { rpc } from "@web/core/network/rpc"`, then
`await rpc("/my_module/books", { limit: 10 })`. It is a plain function, not a service:
there is no `useService("rpc")`. The third argument takes `silent`, `headers` and
`cache`, and the returned promise has `abort()`. It calls a route of
`type='jsonrpc'`.

- Use a route for what is not a model method: a controller of your module, a file, an
  external call proxied by the server.
- A failed call rejects with an `RPCError` (the server raised; `error.data` holds the
  exception name and message) or a `ConnectionLostError`, both from
  `@web/core/network/rpc`. Catch only the error you handle; the others reach the error
  handlers, which show the right dialog.
- Other HTTP calls (a GET that returns JSON, a form post) go through the `http` service
  (`get(route)`, `post(route, params)`),
  also exported as functions from `@web/core/network/http_service`.

# Open actions with the `action` service

- `action.doAction(actionRequest, options)` runs an action: an xml id
  (`"my_module.action_book"`), an id, or an action dictionary
  (`{ type: "ir.actions.act_window", res_model: "library.book", views: [[false, "form"]],
  res_id: bookId, target: "new" }`). Prefer the xml id: the action keeps its context,
  domain and views when someone edits it.
- Options: `additionalContext`, `clearBreadcrumbs`, `onClose` (called when a dialog
  action closes), `props`, `viewType`, `stackPosition` (`"replaceCurrentAction"`), and `newWindow` to open it in
  a new tab.
- `action.doActionButton(params)` runs what a `<button type="object">` would, and
  `action.switchView(viewType, props)` changes the view of the current action.
- A Python method that returns an action dictionary needs no JavaScript: the button
  that calls it runs the action.

# Notify with `notification`, ask with `dialog`

- `notification.add(message, { type, title, sticky, buttons, className })` shows a
  toast and returns a function that closes it. `type` is `"info"`, `"success"`,
  `"warning"` (the default) or `"danger"`; a notification that asks the user to act is
  `sticky: true` with `buttons` (`{ name, onClick, primary }`),
  and `autocloseDelay` sets how long a non-sticky one stays.
- `dialog.add(DialogComponent, props, { onClose })` opens a dialog and returns a
  function that closes it. Ask for confirmation with `ConfirmationDialog`
  (`@web/core/confirmation_dialog/confirmation_dialog`, props `title`, `body`,
  `confirm`, `cancel`) instead of writing a dialog.
- In a component, `useOwnedDialogs()` returns an `add` with the same signature whose
  dialogs close when the component is destroyed.
- The message is translated: `_t("Book lent to %s", partner)`, never a string built
  with `+`.

# Read the user and the companies

- `import { user } from "@web/core/user"`: `user.userId`, `user.partnerId`,
  `user.name`, `user.lang`, `user.tz`, `user.context`, `user.isAdmin`,
  `user.isInternalUser`, `await user.hasGroup("base.group_system")` and
  `user.checkAccessRight(model, operation)`. There is no `user` service.
- Companies are on the same object: `user.activeCompany`, `user.activeCompanies`,
  `user.allowedCompanies`, and `user.activateCompanies(companyIds)` switches them. The
  `company` service no longer exists.
- Pass `user.context` to calls that are not made through the `orm` (which adds it).

# Change the URL through the router

`import { router } from "@web/core/browser/router"` gives `router.current`, the
state of the URL as a flat object, and `router.pushState(state, { replace, reload })`.
There is no `router` service. The action service keeps the URL (`/odoo/...`) in sync
with the action; change it yourself only for state of your own client action (a
selected tab), with keys prefixed by your module.

# Read shared context from `env`, never write to it

The environment is almost empty in this version: plugins replace what it held.
`env.debug` and `env.isSmall` throw when read; use `usePlugin(DebugModePlugin)` (or
`odoo.debug` outside a component) and `useService("ui").isSmall`. `env.bus` and
`env.services` remain as bridges for code not ported. A view still adds `env.config`
and `env.model` for its subtree. Import `_t` from `@web/core/l10n/translation`.

Never assign a key to `env`: it reaches every component and hides where the value
comes from. Share it through a plugin instead.

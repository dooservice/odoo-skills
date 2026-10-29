# Services in 19.0

A service is a long-lived object that the web client starts once and every component
shares: the `orm` to call the server, `action` to open actions, `notification` and
`dialog` to talk to the user. Services are entries of `registry.category("services")`
and are started before the first component renders.

The main services of this version: `orm`, `action`, `notification`,
`dialog`, `effect`, `ui` (`isSmall`, `block`), `hotkey`, `title`, `localization`,
`menu`, `view`, `command`, `popover`, `http`, `field`, `name` and `overlay`.

# Get a service through its hook, never through a global

- In a component: `this.orm = useService("orm")` in `setup`. The hook protects the
  component: a call made after the component is destroyed never resolves, so a late
  answer does not update a dead component.
- Outside a component (another service, a registry function that receives the env):
  `env.services.orm`, or a dependency of your service.
- Never import a service's internals to reach it, and never store a service on
  `window` or a module-level variable: tests replace services, and a global keeps the
  real one.

# Keep shared logic and shared state out of components

A service holds what several components need and what must outlive any one of them: a
cache, a connection, a shared reactive state.

```js
import { reactive } from "@odoo/owl";
import { registry } from "@web/core/registry";

export const libraryService = {
    dependencies: ["orm"],
    start(env, { orm }) {
        const state = reactive({ lentCount: 0 });
        async function refresh() {
            state.lentCount = await orm.searchCount("library.book", [["state", "=", "lent"]]);
        }
        return { state, refresh };
    },
};

registry.category("services").add("my_module.library", libraryService);
```

- `dependencies` lists the services `start` receives; they are started first, and a
  missing one stops the client with an error naming it.
- `start(env, deps)` returns the service's public API; it may be async, and the
  services that depend on it wait.
- `async: ["refresh"]` names the methods that `useService` must protect when a
  component is destroyed.
- Components read shared state with `useState(service.state)`, so they re-render when
  it changes.
- A component that only one screen uses keeps its logic: a service is for what is
  shared.

# Call model methods with the `orm` service

Methods: `call`, `create(model, records)`, `read(model, ids, fields)`, `search`,
`searchRead(model, domain, fields)`, `searchCount`, `unlink`, `write(model, ids,
values)`, `formattedReadGroup(model, domain, groupby, aggregates)`, and the web methods
`webRead(model, ids, { specification })`, `webSearchRead(model, domain, {
specification })`, `webReadGroup(model, domain, groupby, aggregates)`, `webSave`.
`readGroup` no longer exists: use `formattedReadGroup`.

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

Every component has `this.env`, the same object for the whole client:
`env.services` (the started services), `env.bus` (the client-wide event bus),
`env.debug` (the debug mode string) and `env.isSmall` (mobile layout). `env._t` no
longer exists: import `_t` from `@web/core/l10n/translation`. A view adds `env.config`
(its type, the breadcrumbs) and `env.model` for its own subtree.

Never assign a key to `env`: it reaches every component and hides where the value
comes from. Share it through a service instead.

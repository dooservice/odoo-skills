Key names in $version:

$essentials

Sections of this file:

$sections

# Services in $version

$services_intro

# Get a service through its hook, never through a global

$use_service

# Keep shared logic and shared state out of components

$write_service

# Call model methods with the `orm` service

$orm

- `orm.call(model, method, args, kwargs)` calls any public model method; the others
  are shortcuts. The context of the user is added for you: pass only the keys to change,
  in `kwargs.context`.
- `orm.silent.call(...)` does not show the loading indicator, for background refreshes.
- Never call a method whose name starts with `_`: the server refuses it. Expose a
  public method (with the access checks it needs) instead.

# Call a route with `rpc`

$rpc

- Use a route for what is not a model method: a controller of your module, a file, an
  external call proxied by the server.
- A failed call rejects with an `RPCError` (the server raised; `error.data` holds the
  exception name and message) or a `ConnectionLostError`, both from
  `$rpc_errors`. Catch only the error you handle; the others reach the error
  handlers, which show the right dialog.
- Other HTTP calls (a GET that returns JSON, a form post) go through the `http` service
  (`get(route)`, `post(route, params)`)$http_functions.

# Open actions with the `action` service

- `action.doAction(actionRequest, options)` runs an action: an xml id
  (`"my_module.action_book"`), an id, or an action dictionary
  (`{ type: "ir.actions.act_window", res_model: "library.book", views: [[false, "form"]],
  res_id: bookId, target: "new" }`). Prefer the xml id: the action keeps its context,
  domain and views when someone edits it.
- Options: `additionalContext`, `clearBreadcrumbs`, `onClose` (called when a dialog
  action closes), `props`, `viewType`$do_action_options.
- `action.doActionButton(params)` runs what a `<button type="object">` would, and
  `action.switchView(viewType, props)` changes the view of the current action.
- A Python method that returns an action dictionary needs no JavaScript: the button
  that calls it runs the action.

# Notify with `notification`, ask with `dialog`

- `notification.add(message, { type, title, sticky, buttons, className })` shows a
  toast and returns a function that closes it. `type` is `"info"`, `"success"`,
  `"warning"` (the default) or `"danger"`; a notification that asks the user to act is
  `sticky: true` with `buttons` (`{ name, onClick, primary }`)$autoclose.
- `dialog.add(DialogComponent, props, { onClose })` opens a dialog and returns a
  function that closes it. Ask for confirmation with `ConfirmationDialog`
  (`@web/core/confirmation_dialog/confirmation_dialog`, props `title`, `body`,
  `confirm`, `cancel`) instead of writing a dialog.
- In a component, `useOwnedDialogs()` returns an `add` with the same signature whose
  dialogs close when the component is destroyed.
- The message is translated: `_t("Book lent to %s", partner)`, never a string built
  with `+`.

# Read the user and the companies

$user

# Change the URL through the router

$router

# Read shared context from `env`, never write to it

$env

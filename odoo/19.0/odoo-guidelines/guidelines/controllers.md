# Controllers

- Routes are methods decorated with `@route` on a `http.Controller` subclass.
  Always re-decorate an **override** with `@route` (an undecorated override
  still works: the framework auto-decorates it and logs a warning). An empty
  `@route()` keeps the parent's arguments and any argument overrides the
  parent's, except `type`, which an override can never change (ignored with
  a warning; an override that makes a read/write route `readonly`
  is set back to read/write, also with a warning).
- Set the right `auth` on each route (`user`, `bearer`, `public`, or `none`):
  a `public` route must not expose internal data or perform privileged writes
  (see the `odoo-security` skill).
  `auth='bearer'` authenticates with an API key in the `Authorization` header.
- Route `type` is `'http'`, `'jsonrpc'`, or `'json2'`; `type='json'` is a deprecated
  19.0 alias of `'jsonrpc'`.
- Keep controllers thin: parse and check the request, then call a model method
  that does the work. Models never read `odoo.http.request`.

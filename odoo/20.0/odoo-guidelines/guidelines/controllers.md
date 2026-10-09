# Controllers

- Routes are methods decorated with `@route` on a `http.Controller` subclass.
  Always re-decorate an **override** with `@route` (an undecorated override is
  not exposed reliably). An empty `@route()` keeps the parent's arguments and
  any argument overrides the parent's, except `type`, which an override can
  never change.
- Set the right `auth` on each route (`user`, `bearer`, `public`, or `none`): a `public` route must not expose
  internal data or perform privileged writes (see the `odoo-security` skill). `auth='bearer'` authenticates with an API key in the `Authorization` header.
- Route `type` is `'http'`, `'jsonrpc'`, or `'json2'`; `type='json'` is gone.
- Keep controllers thin: parse and check the request, then call a model method
  that does the work. Models never read `odoo.http.request`.

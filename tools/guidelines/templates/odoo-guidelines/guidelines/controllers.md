# Controllers

- Routes are methods decorated with `@route` on a `Controller` subclass
  (`from odoo.http import Controller, request, route`), in
  `controllers/<area>.py`, imported from `controllers/__init__.py`.
- Always re-decorate an **override** with `@route` (an undecorated override
  still works: the framework auto-decorates it and logs a warning). An empty
  `@route()` keeps the parent's arguments and any argument overrides the
  parent's, except `type`, which an override can never change (ignored with
  a warning$readonly).
- To change another module's route, inherit its controller class
  (`from odoo.addons.library.controllers.main import LibraryController`) and
  call `super()`. A new `Controller` subclass declaring the same path
  registers the URL twice, and module load order decides which one answers.
- Keep controllers thin: parse and check the request, then call a model method
  that does the work. Models never read `odoo.http.request`.
- $controller_env
- Name paths by resource, lowercase (`/library/books/<int:book_id>`); portal
  pages live under `/my/`.
- A method parameter receives the query string, form or JSON key of the same
  name. Keys the signature does not accept are dropped with a warning: end the
  signature with `**kw` when clients send extra keys.

# Choose the route type for the caller

Set `type` from who calls the route, not from what the method returns. `type`
defaults to `'http'`.

$route_types

A browser page, form or download is `type='http'`; the web client's own `rpc`
calls use the JSON-RPC type. Scripts and other servers call
$machine_type.

# Set `auth` on every route

Write `auth=` explicitly on every new route: $auth_modes.
The default is `'user'`, and a reader cannot tell a deliberate default from an
omission.

- `auth='user'`: a logged-in internal or portal user; the request runs with that
  user's rights. Without a session an `'http'` route redirects to `/web/login`
  and a JSON route returns a session-expired error.
- `auth='public'`: anyone; a visitor runs as the shared public user
  (`base.public_user`, in `base.group_public`). Branch on visitors with
  `request.env.user._is_public()`.
- `auth='none'`: no user, and possibly no database; `request.env.uid` is
  `None`. Use it only for endpoints that must work before login or without a
  database (health checks, webhooks that verify their own signature); every
  record access there needs an explicit `sudo()` and a reason.$bearer

A `public` or `none` route must not expose internal data or perform privileged
writes: search with the visitor's rights, or sudo only after checking an access
token or a signature (see the `odoo-security` skill).

# Route arguments

- `methods=['POST']` on every route that changes data: a `GET` that writes runs
  from any link, image tag or prefetch. Without `methods` every verb is accepted.
- `csrf` is on by default for `type='http'` routes and checked on every method
  except `GET`, `HEAD`, `OPTIONS` and `TRACE`; a form posts
  `<input type="hidden" name="csrf_token" t-att-value="request.csrf_token()"/>`.
  Set `csrf=False` only on a route that does not authenticate through the session
  cookie (a webhook signature, an API key). JSON routes never check it.
- `cors='*'` (or one origin) sets `Access-Control-Allow-Origin` and answers the
  `OPTIONS` preflight as `auth='none'`. Add it only to routes meant to be called
  from other sites.
- `save_session=False` keeps the response from setting the `session_id` cookie
  and from saving the session. Use it on stateless machine endpoints.$save_session_default$readonly_argument$max_content_length$captcha
- `website=True` (handled by `http_routing`, a dependency of `portal` and
  `website`) marks a frontend page: language prefix in the URL (`multilang`,
  on by default for website `'http'` routes), frontend error pages, and
  `request.website` when `website` is installed. Leave it off backend and
  machine endpoints.
- `sitemap` (read by `website`): `False` keeps the page out of `/sitemap.xml`;
  a function `sitemap(env, rule, qs)` yields the URLs of a route with
  converters. A public website `GET` route without `sitemap` logs a warning
  each time the sitemap is built.

# Read the request and answer through `request`

- Take parameters as method arguments. `request.params` holds them all,
  `request.httprequest` is the werkzeug request (headers, `remote_addr`, raw
  body), and `request.get_json_data()` parses a JSON body in a `type='http'`
  route.
- `request.env` is the environment of the authenticated user. Change it with
  `request.update_env(user=..., context=..., su=...)` or
  `request.update_context(**values)`, never by assigning `request.env`.
- A `type='http'` route returns `request.render('module.template', values)`
  (lazy: an override can still change the values after `super()`), a `str`, or
  a response from `request.make_response(data, headers=[...])`,
  `request.make_json_response(data, status=...)`, `request.redirect(url)` or
  `request.not_found()`. `request.redirect` stays on the same host unless
  `local=False`: never pass it a URL read from the request with `local=False`.
- A JSON route returns plain data (dict, list, ids), never a recordset.
- Serve a binary field or attachment with
  `request.env['ir.binary']._get_stream_from(record, 'field_name').get_response(as_attachment=True)`:
  it sets the type, file name, caching and range support that a hand-built
  response gets wrong.
- Raise `UserError`, `AccessError` or `werkzeug.exceptions.NotFound` for the
  client; the framework turns them into the error page or the error payload of
  the route type.
- `request.session` holds `uid`, `db` and `context`; keep secrets out of it.

# Check access on records reached through a route

Check a record id that arrives in the URL or the body with the caller's rights
before reading it, and use `sudo()` only after that check.

- Prefer the model converter: `/library/book/<model("library.book"):book>`
  passes a record browsed as the request user.
  $converter_check
- For an id in the body, browse it with `request.env` and call
  $check_access_call
  before any `sudo()` on it.
- Build the URLs that the converter reads back with
  $slug_call.

# Portal pages

Customer portal pages inherit `CustomerPortal`
(`from odoo.addons.portal.controllers.portal import CustomerPortal`) and the
model inherits `portal.mixin`.

- The model overrides `_compute_access_url` to set `access_url` to
  `/my/<things>/<id>`, and gets `access_token` (created by
  `_portal_ensure_token()`), `get_portal_url()` and `_get_share_url()`.
- A document route takes `access_token=None` and loads the record with
  `self._document_check_access('library.book', book_id, access_token=access_token)`.
  It returns the record **sudoed** when the user can read it or the token
  matches (compared with `consteq`), and raises `AccessError` or `MissingError`
  otherwise: catch both and `return request.redirect('/my')`. Never compare
  tokens with `==`.
- Pass page values through
  `self._get_page_view_values(record, access_token, values, 'my_books_history', False)`
  for breadcrumbs and previous/next links; paginate list pages with
  `portal_pager(url=..., total=..., page=..., step=self._items_per_page)`
  (`from odoo.addons.portal.controllers.portal import pager as portal_pager`).
$portal_counters
- Portal routes are `auth='user'` with `website=True`. The list domain filters
  on the user's commercial partner, and a record rule for `base.group_portal`
  enforces the same domain on every other access path.

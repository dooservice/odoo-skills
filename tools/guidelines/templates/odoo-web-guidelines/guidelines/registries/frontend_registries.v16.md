The frontend (website, portal, login) has its own registries, loaded by
`web.assets_frontend`.

- `category("public_root_widgets")` holds `{ Widget, selector }`: the public root
  instantiates `Widget` on every element matching `selector`. It is the low-level hook
  behind public widgets; write a public widget (`publicWidget.registry`, see
  [website.md](website.md)) rather than an entry here.
- `category("error_notifications")` turns server errors into notifications for visitors
  (see Error handling in [registries_webclient.md](registries_webclient.md)).

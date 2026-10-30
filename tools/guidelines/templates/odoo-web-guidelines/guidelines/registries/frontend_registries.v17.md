The frontend (website, portal, login) has its own registries, loaded by
`web.assets_frontend`.

- `category("public_components")` holds Owl components that a page mounts with
  `<owl-component name="my_module.book_card" props='{"bookId": 4}'/>`: the key is the
  `name` attribute and the props are the JSON of `props`. The `public_component` service
  mounts them when the page starts. Use it to put an Owl component in a QWeb page.
- `category("public_root_widgets")` holds `{ Widget, selector }`: the public root
  instantiates `Widget` on every element matching `selector`. It is the low-level hook
  behind public widgets; write a public widget (`publicWidget.registry`, see
  [website.md](website.md)) rather than an entry here.
- `category("error_notifications")` turns server errors into notifications for visitors
  (see Error handling in [registries_webclient.md](registries_webclient.md)).

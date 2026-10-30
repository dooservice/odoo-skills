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
  (see Error handling in [registries_webclient.md](registries_webclient.md)).

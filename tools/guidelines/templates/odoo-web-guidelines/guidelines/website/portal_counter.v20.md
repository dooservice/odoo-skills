A home card is a `portal.entry` record (data file): `name`, `url`, `category`,
  `sequence`, and `placeholder_count` naming a counter (`book_count`). The page asks
  `/my/counters` for the counters it shows, and the controller answers in
  `_prepare_portal_counter_values(counter)`, returning the model, the domain and the
  access to check (`"library.book", domain, "read"`) for its own counter and
  `super()` for the others; the count itself is done for you.
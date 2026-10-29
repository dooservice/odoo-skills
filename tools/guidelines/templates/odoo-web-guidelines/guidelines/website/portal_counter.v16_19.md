A home card is a `portal.portal_docs_entry` call added to `portal.portal_my_home`,
  with `placeholder_count` naming a counter (`book_count`). The page asks
  `/my/counters` for the counters it shows, and the controller answers in
  `_prepare_home_portal_values(counters)`: compute a value only when its key is in
  `counters`, with `search_count`, and only if the user has read access.
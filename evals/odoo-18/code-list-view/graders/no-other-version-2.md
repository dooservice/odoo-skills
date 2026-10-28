---
type: regex
target: { source: file, path: "views/library_book_views.xml" }
pattern: 'view_mode[^<]*\btree\b'
match: not_contains
---

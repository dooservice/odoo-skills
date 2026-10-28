---
type: regex
target: { source: file, path: "static/src/book_selection.js" }
pattern: 'extends Plugin|usePlugin|@web/core/services'
match: not_contains
---

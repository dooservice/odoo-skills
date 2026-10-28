---
type: regex
target: { source: file, path: "static/src/book_list.js" }
pattern: 'usePlugin|orm_plugin|\bsignal\('
match: not_contains
---

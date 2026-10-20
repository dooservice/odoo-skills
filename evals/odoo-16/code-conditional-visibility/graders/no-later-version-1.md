---
type: regex
target: { source: file, path: "views/library_book_form.xml" }
pattern: 'invisible=\"[^\"]*state\s*(==|!=|in)'
match: not_contains
---

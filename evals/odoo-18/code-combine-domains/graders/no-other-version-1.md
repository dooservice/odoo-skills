---
type: regex
target: { source: file, path: "models/library_book.py" }
pattern: '\bDomain[.(]|import Domain'
match: not_contains
---

---
type: regex
target: { source: file, path: "models/library_settings.py" }
pattern: 'get_(int|str|bool)\('
match: not_contains
---

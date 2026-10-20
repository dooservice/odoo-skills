---
type: regex
target: { source: file, path: "models/library_settings.py" }
pattern: 'get_param\('
match: not_contains
---

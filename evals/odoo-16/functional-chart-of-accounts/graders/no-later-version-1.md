---
type: regex
target: { source: file, path: "answer.py" }
pattern: 'try_loading\(\s*[''\"]'
match: not_contains
---

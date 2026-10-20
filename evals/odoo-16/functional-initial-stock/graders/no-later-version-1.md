---
type: regex
target: { source: file, path: "answer.py" }
pattern: 'write\(\{\s*[''\"]quantity[''\"]'
match: not_contains
---

---
type: regex
target: { source: file, path: "answer.py" }
pattern: 'requires_allocation[''\"]?\s*:\s*[''\"]'
match: not_contains
---

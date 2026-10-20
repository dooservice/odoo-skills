---
type: regex
target: { source: file, path: "answer.py" }
pattern: 'price_include[''\"]?\s*:\s*True'
match: not_contains
---

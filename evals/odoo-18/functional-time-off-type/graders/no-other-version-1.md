---
type: regex
target: { source: file, path: "answer.py" }
pattern: 'requires_allocation[''"]?\s*[:=]\s*True'
match: not_contains
---

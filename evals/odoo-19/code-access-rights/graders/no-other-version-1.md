---
type: regex
target: { source: file, path: "security/ir.model.access.csv" }
pattern: 'operation|ir\.access\b'
match: not_contains
---

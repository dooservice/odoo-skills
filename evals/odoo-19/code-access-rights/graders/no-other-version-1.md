---
type: regex
target: { source: file, path: "security/access_rights.csv" }
pattern: 'operation|ir\.access\b'
match: not_contains
---

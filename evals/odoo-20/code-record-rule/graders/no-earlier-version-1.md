---
type: regex
target: { source: file, path: "security/rules.xml" }
pattern: 'model=\"ir\.rule\"'
match: not_contains
---

---
type: regex
target: { source: file, path: "client.py" }
pattern: 'ServerProxy|xmlrpc\.client|import xmlrpc|[''\"]method[''\"]\s*:\s*[''\"]call[''\"]'
match: not_contains
---

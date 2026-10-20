---
type: regex
target: { source: file, path: "controllers/main.py" }
pattern: 'type\s*=\s*[''\"](jsonrpc|json2)[''\"]'
match: not_contains
---

---
type: regex
target: { source: file, path: "static/src/form_patch.js" }
pattern: 'patch\(\s*[\w.]+\s*,\s*\{'
match: not_contains
---

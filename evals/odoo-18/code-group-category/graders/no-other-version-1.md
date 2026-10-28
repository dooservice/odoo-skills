---
type: regex
target: { source: file, path: "security/library_groups.xml" }
pattern: 'privilege_id|res\.groups\.privilege'
match: not_contains
---

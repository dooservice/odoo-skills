---
type: regex
target: { source: file, path: "security/library_groups.xml" }
pattern: 'name="user_ids"'
match: not_contains
---

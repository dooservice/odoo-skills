---
type: regex
target: { source: file, path: "answer.py" }
pattern: 'price_markup|compute_price[^\n]*markup'
match: not_contains
---

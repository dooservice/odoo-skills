---
description: Odoo 16.0, code conditional visibility
max_turns: 15
runs: 2
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 16.0 project. Answer by writing the file, no explanation needed.

Write an inherited form view of `library.book` (base view `library.view_library_book_form`) that makes field `isbn` invisible while `state` is 'draft' and read-only when `state` is 'done'.

Write it to `views/library_book_form.xml`.

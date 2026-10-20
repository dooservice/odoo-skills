---
description: Odoo 20.0, code combine domains
max_turns: 15
runs: 3
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 20.0 project. Answer by writing the file, no explanation needed.

In model `library.book`, write a method `available_domain(self, author_ids)` that returns the domain of books in state 'available' AND (author in author_ids OR no author), combining two domains with Odoo's own helpers.

Write it to `models/library_book.py`.

---
description: Odoo 17.0, code read group
max_turns: 15
runs: 3
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 17.0 project. Answer by writing the file, no explanation needed.

In model `library.book`, write a method `count_by_author(self)` that returns a dict {author record id: number of books}, computed with a single grouped query of the ORM.

Write it to `models/library_book.py`.

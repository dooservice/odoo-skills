---
description: Odoo 19.0, code test tags
max_turns: 15
runs: 3
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 19.0 project. Answer by writing the file, no explanation needed.

Write a test for model `library.book` checking that a new book starts in state 'draft'. It must run after all modules are installed, not during the install of this addon.

Write it to `tests/test_library_book.py`.

---
description: Odoo 17.0, code translated error
max_turns: 15
runs: 3
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 17.0 project. Answer by writing the file, no explanation needed.

Write model `library.loan` with a method `action_return` that raises a translated UserError 'This loan is already returned.' when field `state` is 'returned'.

Write it to `models/library_loan.py`.

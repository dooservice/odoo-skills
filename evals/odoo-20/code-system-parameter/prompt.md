---
description: Odoo 20.0, code system parameter
max_turns: 15
runs: 3
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 20.0 project. Answer by writing the file, no explanation needed.

In model `library.book`, write a method `loan_days(self)` that returns the integer system parameter `library.loan_days`, 14 when it is not set.

Write it to `models/library_settings.py`.

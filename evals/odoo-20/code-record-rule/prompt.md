---
description: Odoo 20.0, code record rule
max_turns: 15
runs: 3
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 20.0 project. Answer by writing the file, no explanation needed.

Write a security rule so that users of `library.group_reader` only see books (`library.book`) whose `company_id` is in their companies.

Write it to `security/rules.xml`.

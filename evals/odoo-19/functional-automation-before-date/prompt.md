---
description: Odoo 19.0, functional automation before date
max_turns: 15
runs: 3
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 19.0 project. Answer by writing the file, no explanation needed.

Write an `odoo-bin shell` script that creates an automation rule that sends the email template 'Quotation reminder' to the customer 3 days before the expiration date (`validity_date`) of each quotation.

Write it to `answer.py`.

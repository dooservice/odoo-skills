---
description: Odoo 19.0, code external api
max_turns: 15
runs: 3
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 19.0 project. Answer by writing the file, no explanation needed.

Write a standalone Python script, run from another machine with an API key, that reads the names of the first 10 customers (`res.partner`) of the Odoo server https://odoo.example.com, database 'prod', using the API Odoo recommends for this version.

Write it to `client.py`.

---
description: Odoo 17.0, code group operator
max_turns: 15
runs: 3
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 17.0 project. Answer by writing the file, no explanation needed.

Write model `library.review` with fields book_id (many2one to `library.book`) and rating (float), so that grouped list and pivot views show the average rating instead of the sum.

Write it to `models/library_review.py`.

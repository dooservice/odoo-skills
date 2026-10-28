---
description: Odoo 18.0, code group category
max_turns: 15
runs: 3
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 18.0 project. Answer by writing the file, no explanation needed.

Write the security groups of addon `library` in XML: an application category 'Library', and two groups in it, User and Librarian, where Librarian includes User and the admin user (`base.user_admin`) is a librarian.

Write it to `security/library_groups.xml`.

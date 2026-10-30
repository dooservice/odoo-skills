---
description: Odoo 17.0, code js test
max_turns: 15
runs: 3
allowed_tools: [Read, Glob, Grep, Write, Skill]
---

You are working on an Odoo 17.0 project. Answer by writing the file, no explanation needed.

Write a JavaScript unit test file for a field widget `book_status` of this addon, checking that it renders the state label.

The widget is registered in the `fields` registry as `book_status` by `static/src/book_status_field.js` (not shown). It is used on the `state` selection field of `library.book` (`draft`: Draft, `available`: Available, `lent`: Lent) and shows the label of the current value. The project files are not needed: write the test from this description.

Write it to `static/tests/book_widget_tests.js`.

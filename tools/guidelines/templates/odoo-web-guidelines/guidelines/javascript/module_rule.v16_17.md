Every file under `static/src` and `static/tests` starts with `/** @odoo-module **/`:
without it the file is not transpiled, its `import`s stay as they are, and the bundle
fails to load with a syntax error in the browser. The header also takes
`alias=<name>` (a second, legacy name for the module) and `default=false`.
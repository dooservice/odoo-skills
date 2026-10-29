Files under `static/src` and `static/tests` are always transpiled as ES modules; the
`/** @odoo-module **/` header is no longer needed there, and Odoo removed it from its
own files. It is still needed for a module outside those folders, and
`/** @odoo-module ignore **/` keeps a file of `static/src` out of the transpiler (a
script meant to run as it is).
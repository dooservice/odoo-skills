The list and kanban card parsers do not pass the `js_class`, so a
`my_js_class.my_module_rating` key is only found in a form; a `kanban.` prefix is never
read, use `card.`.
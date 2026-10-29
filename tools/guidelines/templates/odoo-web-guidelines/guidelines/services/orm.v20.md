The ORM is the `ORM` plugin (`@web/core/orm_plugin`): `orm = usePlugin(ORM)`, or
`useService("orm")` through the bridge. Methods: `call`, `create(model, records)`,
`read(model, ids, fields)`, `search`, `searchRead(model, domain, fields)`,
`searchCount`, `unlink`, `write(model, ids, values)`, `formattedReadGroup(model,
domain, groupby, aggregates)`, and the web methods `webRead(model, ids, {
specification })`, `webSearchRead(model, domain, { specification })`,
`webReadGroup(model, domain, groupby, aggregates)`, `webSave`, `webUnlink`.
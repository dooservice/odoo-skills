`extractProps(fieldInfo, dynamicInfo)` receives the parsed `<field>` node as
`fieldInfo` (`attrs`, `options`, `string`, `widget`, `context`, `domain`, ...) and the
values that depend on the record as `dynamicInfo` (`readonly`, `required`, `context`,
`domain()`); it returns the extra props. It is called again when the record changes,
so read record-dependent values from `dynamicInfo`, never from the arch.
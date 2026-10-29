Options are part of the website builder: their template is added to
  `website.BuilderOptions` (an extension with an `xpath` after the
  `snippet_specific_options` node, `<MyOption template="my_module.MyOption"
  selector=".s_book_list"/>`), with builder controls (`BuilderSelect`,
  `BuilderCheckbox`) and `classAction` or `dataAttributeAction`. Options that compute
  something add a `Plugin` with `builder_actions`, registered in
  `registry.category("website-plugins")`.
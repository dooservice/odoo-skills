The XML files of a bundle are compiled into that bundle and registered when it loads,
through `registerTemplate` and `registerTemplateExtension` of `@web/core/templates`. A
component whose template sits in another bundle fails at render with a missing
template, so ship the `.xml` next to the `.js` that uses it and let the same glob take
both.
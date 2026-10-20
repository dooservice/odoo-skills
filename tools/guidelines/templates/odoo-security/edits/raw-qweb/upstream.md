- Server/QWeb: render with `t-out` (escapes by default). `t-raw` no longer
  exists in either server QWeb or OWL: flag any occurrence as broken legacy
  code; the raw-HTML vector today is a `Markup`/`markup()` value reaching
  `t-out`.

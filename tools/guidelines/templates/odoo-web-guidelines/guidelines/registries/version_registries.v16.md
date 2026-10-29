- `category("wowlToLegacyServiceMappers")` maps a legacy service name to a function
  `(legacyEnv) => service` that exposes an Owl service to the legacy widgets still in
  this version. Add to it only when a legacy widget must call a new service.
- `category("preloadedData")` holds `{ loadOnTypes, preload(orm, record, fieldName),
  extraMemoizationKey }`, keyed by a widget or field type: data a field needs before it
  renders (the options of a selection, the stages of a status bar), loaded with the
  record.
- `category("domain_selector/fields")` maps a field type to the component that edits a
  value of that type in the domain editor, and `category("domain_selector/operator")`
  holds the operators it offers (`{ category, label, value, onDidChange, matches }`).

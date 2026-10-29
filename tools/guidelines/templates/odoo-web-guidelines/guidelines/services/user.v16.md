- `useService("user")` gives `userId`, `partnerId`, `name`, `lang`, `tz`, `context`,
  `isAdmin`, `isSystem`, and `hasGroup("base.group_system")` (async).
- `useService("company")` gives `currentCompany`, `allowedCompanyIds` and
  `availableCompanies`, and `setCompanies(mode, ...ids)` switches the active ones.
- Pass `user.context` to calls that are not made through the `orm` (which adds it).
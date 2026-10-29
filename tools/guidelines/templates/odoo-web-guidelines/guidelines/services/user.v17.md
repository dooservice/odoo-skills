- `useService("user")` gives `userId`, `partnerId`, `name`, `lang`, `tz`, `context`,
  `isAdmin`, `isSystem`, `hasGroup("base.group_system")` (async) and
  `checkAccessRight(model, operation)`.
- `useService("company")` gives `currentCompany`, `activeCompanyIds`,
  `allowedCompanies`, and `setCompanies(companyIds)` switches the active ones.
- Pass `user.context` to calls that are not made through the `orm` (which adds it).
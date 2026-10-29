- `import { user } from "@web/core/user"`: `user.userId`, `user.partnerId`,
  `user.name`, `user.lang`, `user.tz`, `user.context`, `user.isAdmin`,
  `user.isInternalUser`, `await user.hasGroup("base.group_system")` and
  `user.checkAccessRight(model, operation)`. There is no `user` service.
- `useService("company")` gives `currentCompany`, `activeCompanyIds`,
  `allowedCompanies`, and `setCompanies(companyIds)` switches the active ones.
- Pass `user.context` to calls that are not made through the `orm` (which adds it).
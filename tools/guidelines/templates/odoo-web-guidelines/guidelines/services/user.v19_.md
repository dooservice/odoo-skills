- `import { user } from "@web/core/user"`: `user.userId`, `user.partnerId`,
  `user.name`, `user.lang`, `user.tz`, `user.context`, `user.isAdmin`,
  `user.isInternalUser`, `await user.hasGroup("base.group_system")` and
  `user.checkAccessRight(model, operation)`. There is no `user` service.
- Companies are on the same object: `user.activeCompany`, `user.activeCompanies`,
  `user.allowedCompanies`, and `user.activateCompanies(companyIds)` switches them. The
  `company` service no longer exists.
- Pass `user.context` to calls that are not made through the `orm` (which adds it).
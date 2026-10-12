# website_project — Online Task Submission

Depends on: website, project.

## `project.task` (extends)

- `email_from` Char “Email From”
- `partner_name` Char “Customer Name” (store, related=partner_id.name)
- `partner_phone` Char “Contact Number” (store, compute=_compute_partner_phone)
- `partner_company_name` Char “Company Name” (store, related=partner_id.company_name)

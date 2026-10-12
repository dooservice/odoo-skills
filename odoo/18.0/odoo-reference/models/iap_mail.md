# iap_mail — IAP / Mail

Depends on: iap, mail.

## `iap.account` (extends)

Inherits: `mail.thread`

- `company_ids` Many2many → `res.company`
- `warning_threshold` Float “Email Alert Threshold”
- `warning_user_ids` Many2many → `res.users` “Email Alert Recipients”

# phone_validation — Phone Numbers Validation

Depends on: base, mail.

## `mail.thread.phone` (defines)

Phone Blacklist Mixin

Inherits: `mail.thread`

- `phone_sanitized` Char “Sanitized Number” (store, compute=_compute_phone_sanitized)
- `phone_sanitized_blacklisted` Boolean “Phone Blacklisted” (compute=_compute_blacklisted)
- `phone_blacklisted` Boolean “Blacklisted Phone is Phone” (compute=_compute_blacklisted)
- `mobile_blacklisted` Boolean “Blacklisted Phone Is Mobile” (compute=_compute_blacklisted)
- `phone_mobile_search` Char “Phone/Mobile”

Public methods: `phone_action_blacklist_remove`, `phone_get_sanitized_number`, `phone_get_sanitized_numbers`

## `phone.blacklist` (defines)

Phone Blacklist

Inherits: `mail.thread`

- `number` Char “Phone Number” (required)
- `active` Boolean

Public methods: `action_add`, `action_remove_with_reason`, `add`, `create`, `phone_action_blacklist_remove`, `remove`, `write`

## `res.partner` (extends)


Public methods: `phone_get_sanitized_number`

## `res.users` (extends)


## `phone.blacklist.remove` (defines)

Remove phone from blacklist

- `phone` Char “Phone Number” (required, readonly)
- `reason` Char

Public methods: `action_unblacklist_apply`

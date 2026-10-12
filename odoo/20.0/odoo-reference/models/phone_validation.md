# phone_validation — Phone Numbers Validation

Depends on: base, mail.

## `mail.activity` (extends)


Extension points: `_get_phone_number_from_record`

## `mail.activity.mixin` (extends)


## `mail.thread.phone` (defines)

Phone Blacklist Mixin

Inherits: `mail.thread`

- `phone_sanitized` Char “Sanitized Number” (store, compute=_compute_phone_sanitized)
- `phone_formatted` Char “Formatted Number” (compute=_compute_phone_formatted)
- `phone_sanitized_blacklisted` Boolean “Phone Blacklisted” (compute=_compute_blacklisted)
- `phone_blacklisted` Boolean “Blacklisted Phone is Phone” (compute=_compute_blacklisted)
- `phone_mobile_search` Char “Phone Number”

Public methods: `init`, `phone_action_blacklist_remove`

## `base` (extends)


## `phone.blacklist` (defines)

Phone Blacklist

Inherits: `mail.thread`

- `number` Char “Phone Number” (required)
- `active` Boolean

Public methods: `action_add`, `add`, `create`, `phone_action_blacklist_remove`, `remove`, `write`

## `res.partner` (extends)

Inherits: `mail.thread.phone`


## `res.users` (extends)


## `mail.activity.schedule` (extends)

- `phone_formatted` Char (compute=_compute_phone_formatted)

Extension points: `_get_phone_number`, `_get_phone_number_for_activity`

## `phone.blacklist.remove` (defines)

Remove phone from blacklist

- `phone` Char “Phone Number” (required, readonly)
- `reason` Char

Public methods: `action_unblacklist_apply`

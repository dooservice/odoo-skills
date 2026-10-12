# auth_ldap — Authentication via LDAP

Depends on: base, base_setup.

## `res.company` (extends)

- `ldaps` One2many → `res.company.ldap` “LDAP Parameters”

## `res.company.ldap` (defines)

Company LDAP configuration

- `sequence` Integer
- `company` Many2one → `res.company` “Company” (required)
- `ldap_server` Char “LDAP Server address” (required)
- `ldap_server_port` Integer “LDAP Server port” (required)
- `ldap_binddn` Char “LDAP binddn”
- `ldap_password` Char “LDAP password”
- `ldap_filter` Char “LDAP filter” (required)
- `ldap_base` Char “LDAP base” (required)
- `user` Many2one → `res.users` “Template User”
- `create_user` Boolean
- `ldap_tls` Boolean “Use TLS”

Extension points: `_get_entry`, `_get_ldap_dicts`, `_get_or_create_user`

## `res.config.settings` (extends)

- `ldaps` One2many “LDAP Parameters” (related=company_id.ldaps)

## `res.users` (extends)


Public methods: `change_password`

Extension points: `_check_credentials`

# Authentication and security

How people prove who they are and what protects the database beyond groups and record
rules (`users-and-access.md`): password length (`auth_password_policy`), two-factor
authentication and its enforcement (`auth_totp`, `auth_totp_mail`,
`auth_totp_mail_enforce`), passkeys (`auth_passkey`), re-authentication after a timeout
(`auth_timeout`), login with Google or another OAuth provider (`auth_oauth`), LDAP
(`auth_ldap`), install requests from non-administrators (`base_install_request`),
importing a module as a zip (`base_import_module`), certificates and keys
(`certificate`) and attachments stored in a cloud bucket (`cloud_storage`). Every change
here can lock people out: ask the user before each step, and keep one administrator
able to log in with a password. Secrets come from the user; never invent or print them.

## Before you start

- Apps: `auth_password_policy`, `auth_totp`, `auth_totp_mail` are installed with the
  base apps. Settings ‣ General Settings, Integrations: `module_auth_oauth`,
  `module_auth_ldap`. Others from Apps: `auth_passkey` (18.0+), `auth_timeout` (19.0+),
  `certificate` (18.0+, usually installed by a localization), `cloud_storage_google`,
  `cloud_storage_azure`, `cloud_storage_migration` (18.0+).
- Settings (Settings ‣ General Settings, Permissions and Integrations): `minlength`,
  `auth_totp_enforce` with `auth_totp_policy`, `auth_oauth_google_enabled` with
  `auth_oauth_google_client_id`, `ldaps`; cloud storage `cloud_storage_provider`.
- Read first:

```python
icp = env['ir.config_parameter'].sudo()
print(icp.get_param('auth_password_policy.minlength'), icp.get_param('auth_totp.policy'))
users = env['res.users'].search([('share', '=', False)])
print(len(users), 'internal users,', len(users.filtered('totp_enabled')), 'with two-factor')
print(env['auth.oauth.provider'].search_read([], ['name', 'enabled']))
```

## The standard flow

1. **Password length.** Settings ‣ General Settings, Permissions, Minimum Password
   Length.

   ```python
   env['res.config.settings'].create({'minlength': 12}).execute()
   env.cr.commit()
   ```

   Applies to new passwords only; existing ones keep working.

2. **Two-factor for each user.** The user opens their own profile (avatar menu), Account
   Security tab, Enable two-factor authentication, and scans the code with an
   authenticator app. Only the user can do this. An administrator can
   invite them (user form ‣ Actions ‣ Invite to use two-factor authentication) or, when
   a phone is lost, turn it off.

   ```python
   user = env['res.users'].search([('login', '=', 'agent.a@example.com')])
   user.action_totp_invite()      # sends the invitation
   # user.action_totp_disable()   # removes it, after the user's request is confirmed
   env.cr.commit()
   ```

3. **Enforce two-factor.** Settings ‣ General Settings, Permissions, Enforce two-factor
   authentication, and for whom.

   ```python
   env['res.config.settings'].create({'auth_totp_enforce': True, 'auth_totp_policy': 'employee_required'}).execute()
   env.cr.commit()
   ```

   `auth_totp_policy`: `employee_required` (internal users) or `all_required` (portal
   users too). Users without an app receive a code by email at login. 16.0 to 18.0 this
   needs `auth_totp_mail_enforce`; from 19.0 it is in `auth_totp_mail`.

4. **Login with Google.** In the Google Cloud console the user creates an OAuth client
   (web application) with the redirect URI `<web.base.url>/auth_oauth/signin`. Then
   Settings ‣ General Settings, Integrations, OAuth Authentication, Google
   Authentication with the client ID.

   ```python
   env['res.config.settings'].create({'module_auth_oauth': True}).execute()   # installs it; ask first
   env['res.config.settings'].create({'auth_oauth_google_enabled': True,
                                      'auth_oauth_google_client_id': '<client id>'}).execute()
   env.cr.commit()
   ```

   Leaves a Log in with Google button. An existing user links their Google account by
   opening their invitation or reset-password link and choosing Google; afterwards
   `oauth_provider_id` and `oauth_uid` are set on the user. Other providers: Settings ‣
   Users & Companies ‣ OAuth Providers (developer mode), `auth.oauth.provider` with
   `client_id`, `auth_endpoint`, `validation_endpoint`, `scope`, `enabled`.

## Variations

- **LDAP** (`auth_ldap`). Settings ‣ General Settings, Integrations, LDAP
  Authentication ‣ LDAP Server: `res.company.ldap` with `ldap_server`,
  `ldap_server_port`, `ldap_binddn`, `ldap_password`, `ldap_base`, `ldap_filter` (for
  example `(uid=%s)`), `ldap_tls`, `create_user` and the template `user`. A user whose
  login is found in the directory logs in with the directory password; with
  `create_user` the Odoo user is created at first login.
- **Passkeys** (18.0+, `auth_passkey`). Each user adds one in their profile, Account
  Security tab (`auth.passkey.key`), and then logs in with the device's fingerprint,
  face or PIN.
- **Timeout** (19.0+, `auth_timeout`). On a group (Settings ‣ Users & Companies ‣
  Groups, developer mode): `lock_timeout` (minutes since login) and
  `lock_timeout_inactivity` (minutes idle) ask its users to authenticate again, with
  two-factor when `lock_timeout_mfa` or `lock_timeout_inactivity_mfa` is set.
- **Install requests** (`base_install_request`). A user who is not an administrator
  clicks Activate on an app and gets a request form (`base.module.install.request`);
  the administrators receive it by email and review it (`base.module.install.review`)
  before installing.
- **Import a module** (`base_import_module`). Apps ‣ Import Module (developer mode,
  administrators): a zip of a data module (XML data and static files only). Only
  import a zip from a source the user trusts.
- **Certificates and keys** (18.0+, `certificate`). Settings ‣ General Settings,
  Certificates and Keys ‣ Certificates: upload a PEM, DER or PKCS12 file
  (`certificate.certificate`: `content`, `pkcs12_password`), see `date_start`,
  `date_end` and `is_valid`; the localization modules that sign documents use them.
- **Cloud storage** (18.0+). `cloud_storage_google` or `cloud_storage_azure`, then
  Settings ‣ General Settings, Cloud Storage: `cloud_storage_provider` (`google`,
  `azure`), the bucket or container and its credentials, and the minimum size
  (`cloud_storage_min_file_size` in bytes; 19.0+ shown as
  `cloud_storage_min_file_size_mb`). New chatter attachments above the size go to the
  bucket; 20.0 `cloud_storage_upload_record_attachments` also sends record attachments.
  `cloud_storage_migration` moves existing attachments of the chosen models.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Enforce two-factor | `auth_totp_mail_enforce` | same | same | `auth_totp_mail` | same |
| Passkeys | no | no | yes | yes | yes |
| Group timeouts | no | no | no | `auth_timeout` | same |
| Certificates and Keys | no | no | yes | yes | yes |
| Cloud storage | no | no | yes | yes, size in MB | yes, record attachments |

## Verify

```python
icp = env['ir.config_parameter'].sudo()
print(icp.get_param('auth_password_policy.minlength'), icp.get_param('auth_totp.policy'))
print(env.ref('auth_oauth.provider_google').enabled, env.ref('auth_oauth.provider_google').client_id)
print([(u.login, u.totp_enabled) for u in env['res.users'].search([('share', '=', False)])])
```

Then ask the user to log in from a private window with each method they turned on.

## Pitfalls

- Enforcing two-factor for all users blocks portal customers without email access;
  start with `employee_required`.
- A wrong OAuth or LDAP setting does not stop password logins, but users who only know
  their Google or directory password cannot get in: test with one user first.
- The administrator account (`base.user_admin`) should keep a password and two-factor;
  never leave it as the only account able to change these settings.
- A copy of the database keeps the OAuth and LDAP settings; neutralizing it removes
  `cloud_storage_provider`, so new attachments stay local there.
- Importing a module zip can overwrite views and data of installed modules.

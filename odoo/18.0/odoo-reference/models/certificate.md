# certificate — Certificate

Depends on: base_setup.

## `certificate.certificate` (defines)

Certificate

- `name` Char “Name”
- `content` Binary “Certificate” (required)
- `pkcs12_password` Char “Certificate Password”
- `private_key_id` Many2one → `certificate.key` “Private Key” (store, compute=_compute_private_key)
- `public_key_id` Many2one → `certificate.key` “Public Key”
- `scope` Selection “Certificate scope”
- `content_format` Selection “Original certificate format” (store, compute=_compute_pem_certificate)
- `pem_certificate` Binary “Certificate in PEM format” (store, compute=_compute_pem_certificate)
- `subject_common_name` Char “Subject Name” (store, compute=_compute_pem_certificate)
- `serial_number` Char “Serial number” (store, compute=_compute_pem_certificate)
- `date_start` Datetime “Available date” (store, compute=_compute_pem_certificate)
- `date_end` Datetime “Expiration date” (store, compute=_compute_pem_certificate)
- `loading_error` Text “Loading error” (store, compute=_compute_pem_certificate)
- `is_valid` Boolean “Valid” (compute=_compute_is_valid)
- `active` Boolean
- `company_id` Many2one → `res.company` “Company” (required)
- `country_code` Char (related=company_id.country_code)
- `issuer_cert_id` Many2one → `certificate.certificate` “Issuer Certificate” (compute=_compute_issuer_cert_id)

Public methods: `create`, `write`

Extension points: `_get_authority_key_identifier`, `_get_certificate_chain`, `_get_common_name`, `_get_der_certificate_bytes`, `_get_fingerprint_bytes`, `_get_public_key_bytes`, `_get_public_key_numbers_bytes`, `_get_signature_bytes`, `_get_subject_key_identifier`

## `certificate.key` (defines)

Cryptographic Keys

- `name` Char “Name”
- `content` Binary “Key file” (required)
- `password` Char “Private key password”
- `pem_key` Binary “Key bytes in PEM format” (store, compute=_compute_pem_key)
- `public` Boolean “Public/Private key” (store, compute=_compute_pem_key)
- `loading_error` Text “Loading error” (store, compute=_compute_pem_key)
- `active` Boolean
- `company_id` Many2one → `res.company` “Company” (required)

Extension points: `_get_public_key_bytes`, `_get_public_key_numbers_bytes`

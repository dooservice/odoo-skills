# l10n_eg_edi_pos — Egypt E-Receipts (POS)

Depends on: point_of_sale, l10n_eg_edi_eta.

## `pos.config` (extends)

- `l10n_eg_edi_pos_enable` Boolean “Submit POS receipts to ETA”
- `l10n_eg_edi_pos_client_id` Char “POS ETA Client ID”
- `l10n_eg_edi_pos_client_secret` Char “POS ETA Client Secret”
- `l10n_eg_edi_pos_serial_number` Char “POS ETA Serial Number”
- `l10n_eg_edi_pos_preprod` Boolean “Use Pre-production Environment”
- `l10n_eg_edi_pos_access_token` Char (readonly)
- `l10n_eg_edi_pos_token_expiry` Datetime (readonly)
- `l10n_eg_edi_pos_last_uuid` Char (readonly)

## `pos.order` (extends)

- `l10n_eg_edi_pos_enable` Boolean (related=config_id.l10n_eg_edi_pos_enable)
- `l10n_eg_edi_pos_state` Selection “ETA State”
- `l10n_eg_edi_pos_uuid` Char “ETA UUID” (readonly)
- `l10n_eg_edi_pos_submission_uuid` Char “ETA Submission UUID” (readonly)
- `l10n_eg_edi_pos_error` Text “ETA Error” (readonly)
- `l10n_eg_edi_pos_qr` Char “ETA QR” (readonly)
- `l10n_eg_edi_pos_json_doc_file` Binary “ETA JSON Document”

Public methods: `action_l10n_eg_edi_pos_resend`, `action_pos_order_paid`, `download_l10n_eg_edi_pos_json_doc_file`

## `pos.payment.method` (extends)

- `country_code` Char (related=company_id.account_fiscal_country_id.code)
- `l10n_eg_edi_pos_payment_code` Selection “ETA Payment Code”

## `res.config.settings` (extends)

- `pos_l10n_eg_edi_pos_enable` Boolean (related=pos_config_id.l10n_eg_edi_pos_enable)
- `pos_l10n_eg_edi_pos_client_id` Char (related=pos_config_id.l10n_eg_edi_pos_client_id)
- `pos_l10n_eg_edi_pos_client_secret` Char (related=pos_config_id.l10n_eg_edi_pos_client_secret)
- `pos_l10n_eg_edi_pos_serial_number` Char (related=pos_config_id.l10n_eg_edi_pos_serial_number)
- `pos_l10n_eg_edi_pos_preprod` Boolean (related=pos_config_id.l10n_eg_edi_pos_preprod)

## `pos.order.receipt` (extends)


Public methods: `order_receipt_generate_data`

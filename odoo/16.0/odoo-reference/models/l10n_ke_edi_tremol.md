# l10n_ke_edi_tremol — Kenya Tremol Device EDI Integration

Depends on: l10n_ke.

## `account.move` (extends)

- `l10n_ke_cu_datetime` Datetime “CU Signing Date and Time”
- `l10n_ke_cu_serial_number` Char “CU Serial Number”
- `l10n_ke_cu_invoice_number` Char “CU Invoice Number”
- `l10n_ke_cu_qrcode` Char “CU QR Code”

Public methods: `l10n_ke_action_cu_post`, `l10n_ke_cu_response`

## `product.template` (extends)

- `l10n_ke_hsn_code` Char “KRA Item Code”
- `l10n_ke_hsn_name` Char “KRA Item Description”

## `product.product` (extends)

- `l10n_ke_hsn_code` Char “HSN code” (related=product_tmpl_id.l10n_ke_hsn_code)
- `l10n_ke_hsn_name` Char “HSN description” (related=product_tmpl_id.l10n_ke_hsn_name)

## `res.company` (extends)

- `l10n_ke_cu_proxy_address` Char “Fiscal Device Proxy Address”

## `res.config.settings` (extends)

- `l10n_ke_cu_proxy_address` Char (related=company_id.l10n_ke_cu_proxy_address)

## `res.partner` (extends)

- `l10n_ke_exemption_number` Char “Exemption Number”

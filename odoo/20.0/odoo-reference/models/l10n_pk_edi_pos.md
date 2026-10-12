# l10n_pk_edi_pos — Pakistan - Point of Sale

Depends on: l10n_pk, pos_discount, iap, stock_delivery.

## `account.move` (extends)


## `pos.config` (extends)

- `l10n_pk_edi_pos_enabled` Boolean “Pakistan electronic receipts (FBR)”
- `l10n_pk_edi_pos_identifier` Integer “Shop ID”
- `l10n_pk_edi_pos_test_identifier` Integer “Test Shop ID”
- `l10n_pk_edi_pos_token` Char “Shop Token”
- `l10n_pk_edi_pos_charge_service_fee` Boolean “Charge Service Fee”
- `l10n_pk_edi_pos_service_fee_product_id` Many2one → `product.product` “Service Fee Product”
- `l10n_pk_edi_pos_sandbox` Boolean “Use Sandbox Environment”

Extension points: `_create_cash_payment_method`, `_get_special_products`

## `pos.order` (extends)

- `l10n_pk_edi_pos_enabled` Boolean (related=config_id.l10n_pk_edi_pos_enabled)
- `l10n_pk_edi_pos_invoice_number` Char “FBR Invoice Number” (readonly)
- `l10n_pk_edi_pos_qr` Char “FBR QR” (readonly)
- `l10n_pk_edi_pos_error` Text “FBR Error” (readonly)
- `l10n_pk_edi_pos_state` Selection “FBR State” (readonly)
- `l10n_pk_edi_pos_payload` Binary “FBR Payload” (compute=_compute_l10n_pk_edi_pos_payload)

Public methods: `action_l10n_pk_edi_pos_resend`, `action_pos_order_paid`, `download_l10n_pk_edi_pos_payload`

## `pos.payment.method` (extends)

- `country_code` Char (related=company_id.country_id.code)
- `l10n_pk_edi_pos_fbr_payment_code` Selection “FBR Payment Code”

## `product.template` (extends)

- `l10n_pk_is_fbr_3rd_schedule` Boolean “Is FBR 3rd Schedule Product”

## `res.config.settings` (extends)

- `pos_l10n_pk_edi_pos_enabled` Boolean (related=pos_config_id.l10n_pk_edi_pos_enabled)
- `pos_l10n_pk_edi_pos_identifier` Integer (related=pos_config_id.l10n_pk_edi_pos_identifier)
- `pos_l10n_pk_edi_pos_test_identifier` Integer (related=pos_config_id.l10n_pk_edi_pos_test_identifier)
- `pos_l10n_pk_edi_pos_token` Char (related=pos_config_id.l10n_pk_edi_pos_token)
- `pos_l10n_pk_edi_pos_charge_service_fee` Boolean (related=pos_config_id.l10n_pk_edi_pos_charge_service_fee)
- `pos_l10n_pk_edi_pos_service_fee_product_id` Many2one (related=pos_config_id.l10n_pk_edi_pos_service_fee_product_id)
- `pos_l10n_pk_edi_pos_sandbox` Boolean (related=pos_config_id.l10n_pk_edi_pos_sandbox)

## `pos.order.receipt` (extends)


Public methods: `order_receipt_generate_data`

# pos_mercury — Vantiv Payment Services

Depends on: web, barcodes, point_of_sale.

## `barcode.rule` (extends)

- `type` Selection

## `pos_mercury.configuration` (defines)

Point of Sale Vantiv Configuration

- `name` Char (required)
- `merchant_id` Char “Merchant ID” (required)
- `merchant_pwd` Char “Merchant Password” (required)

## `pos.payment` (extends)

- `mercury_card_number` Char “Card Number”
- `mercury_prefixed_card_number` Char “Card Number Prefix” (compute=_compute_prefixed_card_number)
- `mercury_card_brand` Char “Card Brand”
- `mercury_card_owner_name` Char “Card Owner Name”
- `mercury_ref_no` Char “Vantiv reference number”
- `mercury_record_no` Char “Vantiv record number”
- `mercury_invoice_no` Char “Vantiv invoice number”

## `pos.payment.method` (extends)

- `pos_mercury_config_id` Many2one → `pos_mercury.configuration` “Vantiv Credentials”

Extension points: `_get_payment_terminal_selection`

## `pos.order` (extends)


## `pos_mercury.mercury_transaction` (defines)

Point of Sale Vantiv Transaction


Public methods: `do_payment`, `do_return`, `do_reversal`, `do_voidsale`

Extension points: `_get_pos_mercury_config_id`, `_get_pos_session`

## `pos.session` (extends)

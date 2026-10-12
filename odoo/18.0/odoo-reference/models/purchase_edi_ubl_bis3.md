# purchase_edi_ubl_bis3 — Import/Export electronic orders with UBL

Depends on: purchase, account_edi_ubl_cii.

## `account.move` (extends)


Extension points: `_check_move_for_group_ungroup_lines_by_tax`

## `purchase.edi.xml.ubl_bis3` (defines)

UBL BIS 3 Peppol Order transaction 3.4

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_anticipated_monetary_total_vals`, `_get_country_vals`, `_get_delivery_party_vals`, `_get_item_vals`, `_get_line_allowance_charge_vals`, `_get_line_item_price_vals`, `_get_order_lines`, `_get_partner_address_vals`, `_get_partner_contact_vals`, `_get_partner_party_legal_entity_vals`, `_get_partner_party_tax_scheme_vals`, `_get_partner_party_vals`, `_get_payment_terms_vals`, `_get_tax_category_vals`

## `purchase.order` (extends)


Extension points: `_get_edi_builders`

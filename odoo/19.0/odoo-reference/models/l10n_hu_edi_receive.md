# l10n_hu_edi_receive — Hungary - E-invoicing Receive Vendor Bills

Depends on: l10n_hu_edi.

## `account.move` (extends)


Extension points: `_get_edi_decoder`

## `res.company` (extends)


Public methods: `l10n_hu_edi_receive_inbound_invoices`, `l10n_hu_edi_show_nav_sync_button`

## `l10n_hu_edi_receive.bills.wizard` (defines)

Receive Bills Wizard

- `l10n_hu_edi_receive_from` Datetime
- `l10n_hu_edi_receive_to` Datetime

Public methods: `action_receive_bills`

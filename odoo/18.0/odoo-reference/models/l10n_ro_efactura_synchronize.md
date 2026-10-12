# l10n_ro_efactura_synchronize — Romania - Synchronize E-Factura

Depends on: l10n_ro_edi.

## `account.move` (extends)


Public methods: `action_l10n_ro_edi_fetch_invoices`

## `l10n_ro_edi.document` (extends)


## `res.company` (extends)

- `l10n_ro_edi_anaf_imported_inv_journal_id` Many2one → `account.journal` “Select journal for SPV imported bills” (store, compute=_compute_l10n_ro_edi_anaf_imported_inv_journal)

## `res.config.settings` (extends)

- `l10n_ro_edi_anaf_imported_inv_journal_id` Many2one (related=company_id.l10n_ro_edi_anaf_imported_inv_journal_id)

## `account.move.send.wizard` (extends)

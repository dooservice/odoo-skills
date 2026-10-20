# Odoo in Peru: what changes between versions

Community only, read in each version's source and run on a Peruvian test database of
that version. "same" means no change from the column on its left.

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| `l10n_pe` depends on | `base_vat`, `base_address_extended`, `l10n_latam_base`, `l10n_latam_invoice_document`, `account_debit_note` | same, plus `account` | same | same | `l10n_latam_invoice_document`, `account_debit_note`, `account` (no `l10n_latam_base`; `base_vat` no longer exists) |
| Installed with it | `l10n_latam_account_sequence` (auto) | none extra | none extra | none extra | none extra |
| `l10n_pe_pos` (auto with `point_of_sale`) | does not exist | yes | yes | yes | yes |
| `l10n_pe_website_sale` (auto with `website_sale`) | does not exist | yes | yes | does not exist: the checkout fields moved into `l10n_pe` (`controllers/portal.py`) | does not exist |
| Chart of accounts | template `l10n_pe.pe_chart_template` (XML) | template code `pe` (`data/template/*.csv`) | same | same, stock accounts set on the template's accounts | same, 1260 accounts (1228 before) |
| Tax XML ids | `l10n_pe.<company id>_sale_tax_igv_18` | `account.<company id>_sale_tax_igv_18` | same | same | same |
| Taxes created | 15: IGV 18% sale and purchase (also "included in price" copies), EXO, INA, GRA, EXP, ISC 0%, purchase IGV G NG and NG | 19: adds the free-transfer group `tax_free_group` and its 3 children; purchase `18% Levied and Not Taxed`, `18% Not Levied` and `0% EXP` are price-included | 17: the "included" copies are gone (use `price_include_override`); names become `VAT 18%`, `0% Exo`... ; nothing price-included | 18: adds `sale_tax_withholding_3` (3% IGV withholding, account 40114) | same |
| Export fiscal position | maps `18%` and `18% (Included in price)` to `0% EXP` (`tax_ids`) | same | maps `VAT 18%` to `0% Exp` | mapping on the tax: `0% Exp` has `original_tax_ids` = `VAT 18%`; every other tax is limited to LOCAL PERU | same |
| Fiscal position sequence | LOCAL PERU 15, EXPORT 10 (most specific wins) | same | same | LOCAL PERU 10, EXPORT 20 (first match wins) | same |
| Identification | `l10n_latam_identification_type_id` + `vat`; default type `l10n_latam_base.it_vat` | same | same | same | `vat` (RUC) and `additional_identifiers` (`PE_DNI`, `PASSPORT`...); computed `l10n_pe_sunat_id_code` and `l10n_pe_sunat_id_value` |
| RUC check | `check_vat_pe`, only when the type is RUC or VAT (`is_vat`) | same | same | same | `check_vat_pe` on `vat` |
| DNI check | none (any text) | same | same | same | `stdnum.pe.cui` (an invalid DNI is refused) |
| Sale document types offered | 01, 03, 07, 08 for every customer (by `internal_type`) | customers whose identification is not RUC (SUNAT code 6) get only Boleta, ND Boleta, NC Boleta on invoices | same | same | same, and a note offers only the subtype of the document it modifies (NC of a boleta: Nota de Crédito Boleta) |
| Credit and debit note exchange rate | the note's date | the date of the document it modifies | the note's date | same | same |
| Vendor bill number padding (`F001-32` to `F001-00000032`) | yes | yes | yes, and `name` is resynchronized | same | same |
| `l10n_pe_group_id` on journal items | yes | yes | removed | removed | removed |
| Peruvian banks (`res.bank`) | not loaded | loaded | loaded, with `l10n_pe_edi_code` | same | not loaded (`res.bank` is gone in 20.0) |
| Point of sale "Consumidor Final" | n/a | DNI `00000000` through the identification type | same | same | `additional_identifiers` `{'PE_DNI': '00000000'}` |

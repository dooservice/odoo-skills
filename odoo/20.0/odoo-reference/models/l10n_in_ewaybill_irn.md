# l10n_in_ewaybill_irn — Indian - E-waybill thru IRN

Depends on: l10n_in_ewaybill, l10n_in_edi.

## `l10n.in.ewaybill` (extends)

- `is_process_through_irn` Boolean (compute=_compute_is_process_through_irn)
- `is_sent_through_irn` Boolean (readonly)

Public methods: `action_generate_ewaybill`, `action_reset_to_pending`

Extension points: `_get_edi_irn_number`, `_prepare_ewaybill_transportation_json_payload`

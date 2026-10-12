# payment_dpo — Payment Provider: DPO

Depends on: payment.

## `payment.provider` (extends)

- `code` Selection
- `dpo_service_ref` Char “DPO Service ID”
- `dpo_company_token` Char “DPO Company Token”

Extension points: `_get_default_payment_method_codes`

## `payment.transaction` (extends)


Extension points: `_get_specific_rendering_values`

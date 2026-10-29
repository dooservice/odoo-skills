"""The rows of `version.md` about business flows: prices, accounting, time off, expenses."""

from __future__ import annotations

from ..version import OdooVersion


class FlowVersionNotes:
    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "pricelist_rules": version.pick(
                v16_19="`compute_price`: `fixed`, `percentage` (with `percent_price`), `formula`; "
                "`applied_on` written (`3_global`, `1_product`...)",
                v20="`compute_price`: `fixed`, `discount` (with `price_discount`), `markup` (with "
                "`price_markup`); `applied_on` is computed. `percentage` and `percent_price` are gone",
            ),
            "line_discount": version.pick(
                v16_17="`discount_policy='without_discount'` on the pricelist, with the setting "
                "`group_discount_per_so_line` (in `product`)",
                v18_19="`discount_policy` is gone. A `compute_price='percentage'` rule shows as a "
                "discount on sales lines when `sale.group_discount_per_so_line` is on",
                v20="a plain `compute_price='discount'` rule (`is_plain_discount`) shows as a "
                "discount on sales lines when `sale.group_discount_per_so_line` is on",
            ),
            "chart_loading": version.pick(
                v16="on the template record: `env.ref('l10n_generic_coa.configurable_chart_template')"
                ".try_loading(company=company)`; never a code string",
                v17_="by code: `env['account.chart.template'].try_loading('generic_coa', company)`",
            ),
            "reconcile_models": version.pick(
                v16_18="`account.reconcile.model` with `rule_type`: `writeoff_button`, "
                "`writeoff_suggestion`, `invoice_matching`",
                v19="`account.reconcile.model` with `trigger`: `manual`, `auto_reconcile`; "
                "`rule_type` does not exist",
                v20="`account.reconcile.model` with `trigger`: `manual`, `auto_reconcile`; "
                "`rule_type` is `reco_model` (default) or `matching_rule`",
            ),
            "tax_mapping": version.pick(
                v16_18="lines on the position: `tax_ids` of `account.fiscal.position.tax` "
                "(`tax_src_id`, `tax_dest_id`)",
                v19_="on the replacement tax: `fiscal_position_ids` and `original_tax_ids` (the taxes "
                "it replaces). `account.fiscal.position.tax`, `tax_src_id` and `tax_dest_id` do not exist",
            ),
            "time_off_types": version.pick(
                v16_17="`hr.leave.type`; `requires_allocation` `'yes'`/`'no'`; "
                "`allocation_validation_type` `'officer'`/`'no'`",
                v18="`hr.leave.type`; `requires_allocation` `'yes'`/`'no'`; "
                "`allocation_validation_type` `'hr'`, `'manager'`, `'both'`, `'no_validation'`",
                v19="`hr.leave.type`; `requires_allocation` a boolean (`True`); "
                "`allocation_validation_type` `'hr'`, `'manager'`, `'both'`, `'no_validation'`",
                v20="`hr.work.entry.type` with `count_as='absence'`; `requires_allocation` a boolean; "
                "requests and allocations point to it with `work_entry_type_id`. `hr.leave.type` is gone",
            ),
            "expense_reports": version.pick(
                v16_17="expenses are submitted in a report: `hr.expense.sheet` with "
                "`expense_line_ids`, then `sheet.action_submit_sheet()`",
                v18="expenses are submitted in a report: `hr.expense.sheet`, then "
                "`sheet.action_submit_sheet()`; `expense.action_submit_expenses()` only creates a draft report",
                v19_="no report: `expense.action_submit()`, `expense.action_approve()`. "
                "`hr.expense.sheet` is gone",
            ),
        }

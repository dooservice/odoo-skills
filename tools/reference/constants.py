"""What the reference builder reads and skips, and the shorthands it writes."""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
#: The Odoo versions the reference is built for, each from `.odoo/src/<version>`.
VERSIONS = ("16.0", "17.0", "18.0", "19.0", "20.0")
SKIPPED_PREFIXES = ("test_", "hw_", "theme_", "l10n_")

KINDS = {
    "Many2oneReference": "many2one_reference",
    "PropertiesDefinition": "properties_definition",
    "Image": "binary",
    "Id": "integer",
}

RELATIONAL = {"Many2one", "One2many", "Many2many"}
FLAGS = ("required", "readonly", "store", "index", "company_dependent")
HOOK_PREFIXES = ("_prepare_", "_get_", "_action_", "_create_", "_post_", "_check_")

SETTINGS_MODEL = "res.config.settings"
#: How a Settings field says where it keeps its value; the first keyword it has decides.
KEPT_AS = (
    ("compute", "computed by `{}`"),
    ("config_parameter", "parameter `{}`"),
    ("implied_group", "group `{}`"),
    ("related", "`{}`"),
)

SHORTHANDS = {"menuitem": "ir.ui.menu", "template": "ir.ui.view"}
#: Per version, the business names agents get wrong most, put in the skill's description: it
#: is the one part an agent always sees, whether it loads the skill or not.
BUSINESS_NAMES = {
    "16.0": (
        "sale lines `tax_id`; storable product `detailed_type='product'` (`type` follows "
        "it); taxes `price_include=True`; payment term lines `value` (`'balance'`, "
        "`'percent'`, `'fixed'`) with `days`; UoM "
        "`category_id`; fiscal position lines `account.fiscal.position.tax` (`tax_src_id`, "
        "`tax_dest_id`); pricelist `compute_price='percentage'`, "
        "`discount_policy='without_discount'` shows the discount on the line; time "
        "off `hr.leave.type`, `requires_allocation` `'yes'`/`'no'`; expenses in "
        "`hr.expense.sheet`; reconciliation models `rule_type`; bank journal "
        "`bank_acc_number`; users `groups_id`; scrap `stock.scrap`; chart of accounts "
        "`env.ref(...).try_loading(company=company)`."
    ),
    "17.0": (
        "sale lines `tax_id`; storable product `detailed_type='product'` (`type` follows "
        "it); taxes `price_include=True`; payment term lines `value` `'percent'` or "
        "`'fixed'` (no `'balance'`) with `nb_days` and `delay_type`; UoM "
        "`category_id`; fiscal position lines `account.fiscal.position.tax` (`tax_src_id`, "
        "`tax_dest_id`); pricelist `'percentage'`, `discount_policy='without_discount'` "
        "shows the discount on the line; time off "
        "`hr.leave.type`, `requires_allocation` `'yes'`/`'no'`; expenses in "
        "`hr.expense.sheet`; reconciliation models `rule_type`; bank journal "
        "`bank_acc_number`; users `groups_id`; automation actions in `action_server_ids`; "
        "scrap `stock.scrap`; chart of accounts `try_loading('generic_coa', company)`."
    ),
    "18.0": (
        "sale lines `tax_id`; product `type='consu'` with `is_storable=True` (no "
        "`detailed_type`); taxes `price_include_override='tax_included'`; payment term "
        "lines `nb_days` and `delay_type` (no `'balance'`); UoM "
        "`category_id`; fiscal position lines `account.fiscal.position.tax` (`tax_src_id`, "
        "`tax_dest_id`); pricelist `'percentage'`, no `discount_policy`; time off "
        "`hr.leave.type`, `requires_allocation` `'yes'`/`'no'`, validation `'hr'`; expenses "
        "in `hr.expense.sheet`, then `action_submit_sheet()`; reconciliation models "
        "`rule_type`; bank journal `bank_acc_number`; users `groups_id`; scrap "
        "`stock.scrap`; chart of accounts `try_loading('generic_coa', company)`."
    ),
    "19.0": (
        "sale lines `tax_ids`; product `is_storable`; taxes "
        "`price_include_override='tax_included'`; payment term lines `nb_days` and "
        "`delay_type` (no `'balance'`); UoM `relative_factor` and `relative_uom_id` "
        "(no `category_id`); "
        "fiscal positions: `fiscal_position_ids` and `original_tax_ids` on the replacement "
        "tax (no `account.fiscal.position.tax`); pricelist `'percentage'`; time off "
        "`hr.leave.type`, `requires_allocation=True`, validation `'hr'`; expenses "
        "`action_submit()`, no `hr.expense.sheet`; reconciliation models `trigger`, no "
        "`rule_type`; bank journal `bank_acc_number`; users `group_ids`; scrap `stock.scrap`."
    ),
    "20.0": (
        "sale lines `tax_ids`; product `is_storable`; taxes "
        "`price_include_override='tax_included'`; payment term lines `nb_days` (no "
        "`'balance'`); UoM `relative_factor`; fiscal "
        "positions: `original_tax_ids` on the replacement tax; pricelist "
        "`compute_price='discount'` with `price_discount` (no `'percentage'`); time off "
        "types are `hr.work.entry.type` with `count_as='absence'` (no `hr.leave.type`); "
        "expenses `action_submit()`; reconciliation models `trigger`; bank journal "
        "`bank_account_number`; companies: `is_company` is computed, no `company_type`; "
        "users `group_ids`; scrap: a `stock.move` with `is_scrap` (no `stock.scrap`); "
        "parameters `get_int`/`get_str`."
    ),
}

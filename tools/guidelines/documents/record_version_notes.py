"""The rows of `version.md` about base records: parameters, users, contacts, automations."""

from __future__ import annotations

from ..version import OdooVersion


class RecordVersionNotes:
    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "system_parameters": version.pick(
                v16_19="`env['ir.config_parameter'].sudo().get_param('key', default)` returns a string: "
                "convert it (`int(...)`); `set_param('key', value)` writes",
                v20="typed getters: `env['ir.config_parameter'].sudo().get_int('key', 14)`, `get_bool`, "
                "`get_float`, `get_str`; `set_int`, `set_bool`, `set_float`, `set_str` write. "
                "`get_param` and `set_param` do not exist",
            ),
            "user_groups": version.pick(
                v16_18="`groups_id` on `res.users` (implied groups included): "
                "`user.write({'groups_id': [Command.link(group.id)]})`",
                v19_="`group_ids` on `res.users` (groups given explicitly), `all_group_ids` with the "
                "implied ones: `user.write({'group_ids': [Command.link(group.id)]})`. `groups_id` is gone",
            ),
            "company_contacts": version.pick(
                v16_19="`res.partner` with `is_company=True` (`company_type='company'` in the form); "
                "its people are partners with `parent_id` set to it",
                v20="`company_type` is gone and `is_company` is computed: a partner without parent "
                "and with a real `vat` is a company. Create the company (with its `vat` when known), "
                "then its people as partners with `parent_id` set to it",
            ),
            "automation_rules": version.pick(
                v16="`base.automation` delegates to `ir.actions.server` (`action_server_id`, "
                "`delegate=True`): `state`, `code` and the other action fields go on the rule itself; "
                "trigger `on_write` or `on_create_or_write` with `filter_pre_domain` and `filter_domain`",
                v17_18="`base.automation` no longer inherits `ir.actions.server`: its actions are "
                "`ir.actions.server` records in `action_server_ids` (their `base_automation_id`); "
                "trigger `on_create_or_write` (`on_create` and `on_write` are deprecated) or a value "
                "trigger such as `on_state_set`",
                v19_="`base.automation` with its actions in `action_server_ids` (their "
                "`base_automation_id`); trigger `on_create_or_write` (`on_write` is deprecated) or a "
                "value trigger such as `on_state_set`",
            ),
            "bank_journal": version.pick(
                v16_19="`account.journal` with `type='bank'` and `bank_acc_number` (plus `bank_id`), "
                "which creates the `res.partner.bank`",
                v20="`account.journal` with `type='bank'` and `bank_account_number` (plus `bank_bic`), "
                "which creates the `res.partner.bank`; `bank_acc_number` is gone",
            ),
        }

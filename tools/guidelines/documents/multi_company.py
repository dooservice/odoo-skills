"""`odoo-guidelines/guidelines/multi_company.md`: `company_id`, company checks, rules and `with_company`."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class MultiCompany(Document):
    path = "odoo-guidelines/guidelines/multi_company.md"

    legacy_rule = """\
```xml
<record id="library_book_rule_company" model="ir.rule">
    <field name="name">Library books: multi-company</field>
    <field name="model_id" ref="model_library_book"/>
    <field name="domain_force">[('company_id', 'in', company_ids)]</field>
</record>
```

The rule has no `groups`, so it is global: it applies to every user, AND-ed
with every other rule."""

    unified_rule = """\
```
id,name,model_id,group_id/id,operation,domain
library_book_company,library.book multi-company,library.book,,crud,"[('company_id', 'in', company_ids)]"
```

The row has no group, so it is a restriction: it applies to every user, AND-ed
with every other row, and grants nothing by itself."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "company_rule_name": version.pick(v16_19="record rule", v20="restriction row"),
            "company_rule": version.pick(v16_19=self.legacy_rule, v20=self.unified_rule),
            "check_company_domain": version.pick(
                v16="`check_company=True` also gives the field the domain\n"
                "  `[('company_id', 'in', [company_id, False])]` in forms, but only when the\n"
                "  field declares no `domain` of its own: then add the company condition to\n"
                "  that domain yourself.",
                v17_="`check_company=True` also adds the company condition to the field's own\n"
                "  `domain` in forms, built from the comodel's `_check_company_domain`.",
            ),
            "company_domain_hook": version.pick(
                v16="",
                v17="\n- A comodel shared between a company and its branches sets\n"
                "  `_check_company_domain = models.check_company_domain_parent_of`.",
                v18_="\n- A comodel shared between a company and its branches sets\n"
                "  `_check_company_domain = models.check_company_domain_parent_of`; a comodel\n"
                "  with `company_ids` instead of `company_id` is handled as well.",
            ),
            "branches": version.pick(
                v16="",
                v17_="\n- Branches (`res.company.parent_id`) are separate companies: `company_ids`\n"
                "  holds a branch only when it is selected. To show a parent's records in its\n"
                "  branches, write the domain with `('company_id', 'parent_of', company_ids)`.",
            ),
            "company_dependent_storage": version.pick(
                v16_17="They are stored in `ir.property`, not in\n"
                "  the model's table: they cost a join to search or group by.",
                v18_="They are stored as a JSON column keyed by\n"
                "  company, with the `ir.default` value as fallback; a required or translated\n"
                "  company-dependent field is not supported.",
            ),
        }

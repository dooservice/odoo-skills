"""Groups of `security.md`: `privilege_id` replaced `category_id` in 19.0."""

from __future__ import annotations

from ..version import OdooVersion


class GroupBlocks:
    """How a module declares its groups: by category up to 18.0, by privilege from 19.0."""

    category_groups = """\
A module's groups belong to an application through `category_id` (an
`ir.module.category`), and each level implies the one below.

```xml
<record id="group_library_user" model="res.groups">
    <field name="name">User</field>
    <field name="category_id" ref="base.module_category_services"/>
    <field name="implied_ids" eval="[Command.link(ref('base.group_user'))]"/>
</record>
<record id="group_library_manager" model="res.groups">
    <field name="name">Administrator</field>
    <field name="category_id" ref="base.module_category_services"/>
    <field name="implied_ids" eval="[Command.link(ref('group_library_user'))]"/>
    <field name="users" eval="[Command.link(ref('base.user_admin'))]"/>
</record>
```

- Groups of one category that form an `implied_ids` chain show as one selection
  on the user form (generated fields `sel_groups_<ids>`); other groups show as
  check boxes (`in_group_<id>`). Never reference those generated fields: write
  `groups_id` on `res.users`, which also holds the implied groups.
- `users` on the group lists its members; `comment` explains what it grants."""

    privilege_groups = """\
A module's groups belong to an application through `privilege_id` (a
`res.groups.privilege`, itself in an `ir.module.category`), ordered by
`sequence`, and each level implies the one below.

```xml
<record id="res_groups_privilege_library" model="res.groups.privilege">
    <field name="name">Library</field>
    <field name="category_id" ref="base.module_category_services"/>
</record>
<record id="group_library_user" model="res.groups">
    <field name="name">User</field>
    <field name="sequence">10</field>
    <field name="privilege_id" ref="res_groups_privilege_library"/>
    <field name="implied_ids" eval="[Command.link(ref('base.group_user'))]"/>
</record>
<record id="group_library_manager" model="res.groups">
    <field name="name">Administrator</field>
    <field name="sequence">20</field>
    <field name="privilege_id" ref="res_groups_privilege_library"/>
    <field name="implied_ids" eval="[Command.link(ref('group_library_user'))]"/>
    <field name="user_ids" eval="[Command.link(ref('base.user_admin'))]"/>
</record>
```

- `res.users.group_ids` holds only the groups given explicitly, and
  `res.groups.user_ids` only the users given explicitly; search and compare on
  `all_group_ids` / `all_user_ids`, which add the implied ones.
- The user form shows one choice per privilege; there are no generated
  `sel_groups_`/`in_group_` fields any more.{everyone}"""

    def values(self, version: OdooVersion) -> dict[str, str]:
        everyone = version.pick(
            v16_19="",
            v20="\n- `base.group_everyone` is implied by the user, portal and public groups:\n"
            "  it is how a row grants something to every user.",
        )
        return {
            "groups": version.pick(
                v16_18=self.category_groups,
                v19_=self.privilege_groups.format(everyone=everyone),
            ),
        }

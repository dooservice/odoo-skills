# website_customer — Customer References

Depends on: website_crm_partner_assign, website_partner, website_google_map.

## `res.partner` (extends)

- `website_tag_ids` Many2many → `res.partner.tag` “Website tags”

Public methods: `get_backend_menu_id`

## `res.partner.tag` (defines)

Partner Tags - These tags can be used on website to find customers by sector, or ...

Inherits: `website.published.mixin`

- `name` Char “Category Name” (required)
- `partner_ids` Many2many → `res.partner` “Partners”
- `classname` Selection “get_selection_class” (required)
- `active` Boolean “Active”

Public methods: `get_selection_class`

## `website` (extends)


Public methods: `get_suggested_controllers`

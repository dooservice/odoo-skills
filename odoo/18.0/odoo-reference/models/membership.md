# membership — Members

Depends on: account.

## `account.move` (extends)


Public methods: `button_cancel`, `button_draft`, `write`

## `account.move.line` (extends)


Public methods: `create`, `write`

## `membership.membership_line` (defines)

Membership Line

- `partner` Many2one → `res.partner` “Partner” (index)
- `membership_id` Many2one → `product.product` “Membership” (required)
- `date_from` Date “From” (readonly)
- `date_to` Date “To” (readonly)
- `date_cancel` Date “Cancel date”
- `date` Date “Join Date”
- `member_price` Float “Membership Fee” (required)
- `account_invoice_line` Many2one → `account.move.line` “Account Invoice line” (readonly)
- `account_invoice_id` Many2one → `account.move` “Invoice” (readonly, related=account_invoice_line.move_id)
- `company_id` Many2one → `res.company` “Company” (readonly, store, related=account_invoice_line.move_id.company_id)
- `state` Selection “Membership Status” (store, compute=_compute_state)

## `res.partner` (extends)

- `associate_member` Many2one → `res.partner` “Associate Member”
- `member_lines` One2many → `membership.membership_line` “Membership”
- `free_member` Boolean “Free Member”
- `membership_amount` Float “Membership Amount”
- `membership_state` Selection “Current Membership Status” (store, compute=_compute_membership_state)
- `membership_start` Date “Membership Start Date” (store, compute=_compute_membership_state)
- `membership_stop` Date “Membership End Date” (store, compute=_compute_membership_state)
- `membership_cancel` Date “Cancel Membership Date” (store, compute=_compute_membership_state)

Public methods: `create_membership_invoice`

Extension points: `_check_recursion_associate_member`

## `product.template` (extends)

- `membership` Boolean
- `membership_date_from` Date “Membership Start Date”
- `membership_date_to` Date “Membership End Date”

## `report.membership` (defines)

Membership Analysis

- `start_date` Date “Start Date” (readonly)
- `date_to` Date “End Date” (readonly)
- `num_waiting` Integer “# Waiting” (readonly)
- `num_invoiced` Integer “# Invoiced” (readonly)
- `num_paid` Integer “# Paid” (readonly)
- `tot_pending` Float “Pending Amount” (readonly)
- `tot_earned` Float “Earned Amount” (readonly)
- `partner_id` Many2one → `res.partner` “Member” (readonly)
- `associate_member_id` Many2one → `res.partner` “Associate Member” (readonly)
- `membership_id` Many2one → `product.product` “Membership Product” (readonly)
- `membership_state` Selection “Current Membership State” (readonly)
- `user_id` Many2one → `res.users` “Salesperson” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `quantity` Integer (readonly)

Public methods: `init`

## `membership.invoice` (defines)

Membership Invoice

- `product_id` Many2one → `product.product` “Membership” (required)
- `member_price` Float “Member Price” (required)

Public methods: `membership_invoice`, `onchange_product`

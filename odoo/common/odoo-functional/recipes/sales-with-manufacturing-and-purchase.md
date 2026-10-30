# Selling what is bought or made on order

A sales order can trigger the work behind it: a request for quotation to a vendor, a
manufacturing order, a kit delivered as its components, or a purchase of a subcontracted
service. The link modules install themselves: `sale_purchase` (sales with `purchase`),
`sale_purchase_stock` (with `sale_stock` and `purchase_stock`) and `sale_mrp` (with `mrp`
and `sale_stock`). In 20.0, `crm_sale_project` creates a project from an opportunity and
`sale_project_margin` shows a project's forecast margin. From 18.0, `sale_gelato` sends
orders to the Gelato print-on-demand service. Dropshipping (`stock_dropshipping`) is left
out. Buying, receiving, manufacturing and invoicing themselves are in `purchase.md`,
`manufacturing.md`, `inventory.md` and `sales-and-crm.md`; this recipe covers what links
them to the sale.

**At a glance**

- Apps: `sale_stock` and `purchase_stock` for goods bought on order; `mrp` for goods made
  on order and kits; `sale_purchase` (with `sale` and `purchase`) for subcontracted
  services. `sale_purchase_stock` and `sale_mrp` are installed with them.
- Names that change by version: MTO by unarchiving the route up to 18.0, setting
  `replenish_on_order` 19.0+ (Buy, Manufacture on the warehouse); manufacturing order
  `sale_line_id` 18.0+; subcontracted service `service_to_purchase` up to 19.0,
  `service_tracking='subcontract'` 20.0; Gelato 18.0+.
- Sections: Before you start; The standard flow (1 turn on make to order, 2 give the
  product a vendor and the routes, 3 sell it, 4 buy it, 5 deliver and invoice);
  Variations; Versions; Verify; Pitfalls.

## Before you start

- Settings: make to order (MTO) is the route `stock.route_warehouse0_mto`, archived in a
  new database.

| Setting | Field | Versions |
|---|---|---|
| Replenish on Order (MTO) | `replenish_on_order` (Inventory settings), unarchives the route | 19.0+ |
| Multi-Step Routes | `group_stock_adv_location`: shows Inventory ‣ Configuration ‣ Warehouse Management ‣ Routes, where the route is unarchived | 16.0 to 18.0 |
| Gelato | `module_sale_gelato`; then `gelato_api_key`, `gelato_webhook_secret` (on the company) | 18.0+ |

- Read first:

```python
mto = env.ref('stock.route_warehouse0_mto')
print(mto.active, mto.sequence, mto.rule_ids.mapped('name'))
for t in env['product.template'].search([('route_ids', 'in', mto.ids)]):
    print(t.name, t.route_ids.mapped('name'), t.seller_ids.mapped('partner_id.name'), t.bom_ids.mapped('type'))
print(env['mrp.bom'].search_read([('type', '=', 'phantom')], ['product_tmpl_id']))
```

Drop the last line when `mrp` is not installed.

## The standard flow

Odoo's documentation sets up a product bought from a vendor for each sale: turn on make
to order, give the product a vendor and the routes, sell it, buy it, receive it, deliver
it.

1. **Turn on make to order.** 19.0 and 20.0: Inventory ‣ Configuration ‣ Settings,
   Replenish on Order (MTO). 16.0 to 18.0: Inventory ‣ Configuration ‣ Settings,
   Multi-Step Routes; then Inventory ‣ Configuration ‣ Warehouse Management ‣ Routes,
   filter Archived, select Replenish on Order (MTO), Unarchive.

   19.0 and 20.0:

   ```python
   env['res.config.settings'].create({'replenish_on_order': True}).execute()
   env.cr.commit()
   ```

   16.0 to 18.0:

   ```python
   env.ref('stock.route_warehouse0_mto').active = True
   env.cr.commit()
   ```

   Leaves the route active and selectable on products.

2. **Give the product a vendor and the routes.** The product form (Sales ‣ Products ‣
   Products), Purchase tab, a vendor line (`purchase.md` step 1); Inventory tab, Routes:
   tick Replenish on Order (MTO), and Buy in 16.0 to 18.0.

   ```python
   from odoo import Command
   tmpl = product.product_tmpl_id
   env['product.supplierinfo'].create({'product_tmpl_id': tmpl.id, 'partner_id': vendor.id, 'price': 40})
   mto = env.ref('stock.route_warehouse0_mto')
   tmpl.write({'route_ids': [Command.link(mto.id)]})
   env.cr.commit()
   ```

   This is 19.0 and 20.0. In 16.0 to 18.0 also link
   `env.ref('purchase_stock.route_warehouse0_buy')` in `route_ids`.

   Leaves a product that each sale buys. In 19.0 and 20.0 Buy is a route of the
   warehouse (`buy_to_resupply`), not of the product; a product with a bill of materials
   is manufactured instead.

3. **Sell it.** Sales ‣ Orders ‣ Quotations ‣ New, add the product, Confirm
   (`sales-and-crm.md` steps 4 to 6).

   ```python
   order = env['sale.order'].create({'partner_id': customer.id, 'order_line': [
       Command.create({'product_id': product.id, 'product_uom_qty': 3}),
   ]})
   order.action_confirm()
   env.cr.commit()
   print(order._get_purchase_orders().mapped(lambda p: (p.name, p.partner_id.name, p.state, p.origin)))
   ```

   Leaves the sales order in `sale`, a request for quotation in `draft` for the vendor
   with the order's name in `origin` (Purchase smart button on the order, Sale smart
   button on the request), and the delivery `waiting`. The request may be an existing
   draft of the same vendor that the line was added to.

4. **Buy it.** The order's Purchase smart button, the request's Confirm Order, then its
   Receipt, Validate (`purchase.md` steps 4 and 5).

   ```python
   po = order._get_purchase_orders()
   po.button_confirm()
   env.cr.commit()
   ```

   Leaves the purchase order in `purchase` and a receipt to validate. Validating the
   receipt makes the delivery `assigned`: the goods are reserved for this sale and no
   other.

5. **Deliver and invoice.** The order's Delivery smart button, Validate; then Create
   Invoice (`sales-and-crm.md` steps 8 and 9).

   Leaves the delivery `done` and the order invoiced as its invoicing policy allows.

## Variations

- **Manufacture on order** (`sale_mrp`). The product has a bill of materials of type
  Manufacture this product (`type='normal'`, `manufacturing.md` step 3) and the MTO route
  of step 2; in 16.0 to 18.0 it has Manufacture instead of Buy (`manufacturing.md`
  step 2). Confirming the sale creates a manufacturing order with the order's name in
  `origin`, shown in the order's Manufacturing smart button (`mrp_production_ids`); from
  18.0 it also carries `sale_line_id`. Producing it (`manufacturing.md` step 7) frees the
  delivery.

  ```python
  order.action_confirm()
  print(order.mrp_production_count, order.mrp_production_ids.mapped(lambda m: (m.name, m.state, m.origin)))
  ```

- **Kits** (`sale_mrp`). A bill of materials of type Kit (`type='phantom'`): the order
  shows the kit, the delivery moves its components, and the line's `qty_delivered`
  counts the kits whose components are all delivered. No route or manufacturing order.

  ```python
  env['mrp.bom'].create({'product_tmpl_id': kit.product_tmpl_id.id, 'type': 'phantom', 'bom_line_ids': [
      Command.create({'product_id': component.id, 'product_qty': 2}),
  ]})
  env.cr.commit()
  ```

- **Subcontracted service** (`sale_purchase`). A service another company performs:
  confirming the sale creates a purchase line for the service's vendor, linked to the sale
  line (`purchase_line_ids`, `sale_line_id` on the purchase line). 16.0 to 19.0: product
  form, Purchase tab, Subcontract Service (`service_to_purchase`, per company). 20.0:
  General Information tab, Create on Order, Subcontracting RFQ
  (`service_tracking='subcontract'`). The product needs a vendor line.

  20.0:

  ```python
  service.product_tmpl_id.write({'service_tracking': 'subcontract',
      'seller_ids': [Command.create({'partner_id': vendor.id, 'price': 300})]})
  env.cr.commit()
  ```

  16.0 to 19.0:

  ```python
  service.product_tmpl_id.with_company(company).write({'service_to_purchase': True, 'expense_policy': 'no',
      'seller_ids': [Command.create({'partner_id': vendor.id, 'price': 300})]})
  env.cr.commit()
  ```

  Raising the quantity on a confirmed sale updates the draft purchase line or creates a
  new request; lowering it or cancelling the sale schedules a warning activity on the
  purchase order for the buyer. The service's received quantity is set by hand on the
  purchase order (`purchase.md`).

- **Project from an opportunity** (20.0, `crm_sale_project`, installed with `crm` and
  `sale_project`). The opportunity's Actions menu, Create Project (project managers):
  choose the customer (new, existing or none) and a billable project template. The
  project is billable and linked to the opportunity (`lead_id`, Opportunity smart button
  on the project; Projects and Tasks on the opportunity). A quotation made from the
  opportunity afterwards takes the project (`project_id`) and becomes its sales order
  (`reinvoiced_sale_order_id`).

  ```python
  action = lead.action_create_project()
  wizard = env['project.template.create.wizard'].with_context(action['context']).create({})
  wizard.action_create_project_from_lead()
  env.cr.commit()
  print(lead.project_ids.mapped(lambda p: (p.name, p.partner_id.name, p.allow_billable)))
  ```

- **Forecast margin of a project** (20.0, `sale_project_margin`, with `sale_margin` and
  `sale_project`). The project's Estimated Costs smart button and Project ‣ Reporting ‣
  Forecast Margins (project managers) compare the sold amount with the cost
  (`purchase_price`) of the sales order lines of the project's open tasks.

  ```python
  print(project.estimated_cost, project.estimated_cost_ratio)
  ```

- **Print on demand with Gelato** (18.0+, `sale_gelato`; `website_sale_gelato` for the
  shop). Needs an account at Gelato and its API key: ask the user for them. Sales ‣
  Configuration ‣ Settings, Connectors, Gelato: tick, Save, then the API Key and Webhook
  Secret (the webhook URL is `<base url>/gelato/webhook`). On the product form, Sales
  tab, Gelato section: the Template Reference, Synchronize (creates the variants and the
  print image slots), then upload each print image. Sell it with a Gelato delivery
  method (Standard Delivery or Express Delivery, `delivery_type='gelato'`): confirming
  the order sends it to Gelato and logs it in the chatter; Gelato's status updates email
  the customer when the order ships and arrives. In the shop, a product cannot be
  published without its print images.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Turn on MTO | unarchive the route (Multi-Step Routes for the menu) | same | same | setting `replenish_on_order` | same |
| Routes on the product | MTO + Buy, or MTO + Manufacture | same | same | MTO only (Buy, Manufacture on the warehouse) | same |
| MTO purchase without vendor | confirming the sale fails | same | same | the sale confirms, the line is taken from stock, a message on the order names the salesperson | same |
| Manufacturing order `sale_line_id` | no | no | yes | yes | yes |
| Subcontracted service | `service_to_purchase` (Purchase tab, per company) | same | same | same | `service_tracking='subcontract'` (Create on Order) |
| Draft request reused for a subcontracted service | any draft of the vendor | same | same | only a draft already linked to the same sale | same |
| `crm_sale_project`, `sale_project_margin` | no | no | no | no | yes |
| Gelato (`sale_gelato`, `website_sale_gelato`) | no | no | yes, needs `sale_management` | yes, checks the shipping address on confirm | same, also warns while editing the order and checks address lengths |

## Verify

```python
print(order.state, [(l.product_id.display_name, l.product_uom_qty, l.qty_delivered, l.purchase_line_count) for l in order.order_line])
print(order._get_purchase_orders().mapped(lambda p: (p.name, p.state, p.origin)))
print(order.mrp_production_ids.mapped(lambda m: (m.name, m.state)))
print(order.picking_ids.mapped(lambda p: (p.name, p.state)))
```

`mrp_production_ids` comes from `sale_mrp`: drop that line when `mrp` is not installed.

Each line bought or made on order has its purchase or manufacturing order, with the sale's
name in `origin`; the delivery is `assigned` once they are received or produced.

## Pitfalls

- The MTO route archived (16.0 to 18.0) does not appear on the product: unarchive it
  first (step 1).
- A product with MTO but without Buy or Manufacture in 16.0 to 18.0 makes the sale fail
  on confirmation: add the route that supplies it.
- An MTO product without a vendor: in 16.0 to 18.0 the sale does not confirm; in 19.0+
  it confirms but the line is served from stock and nothing is bought. Read the order's
  chatter after confirming.
- The request for quotation is a draft: nobody is notified. Tell the buyer, or confirm it
  with the user's yes.
- A subcontracted service without a vendor cannot be saved; one with a re-invoice policy
  other than No (`expense_policy` up to 19.0, `reinvoice_policy` in 20.0) cannot be
  subcontracted: the product form turns Subcontract Service off (Create on Order back to
  Nothing in 20.0).
- Cancelling a sale bought on order does not cancel its purchase order: cancel or adjust
  it with the buyer; goods already received stay in stock.
- Gelato products cannot be mixed with other goods on one order or cart; the order
  fails on confirm when a print image is missing or, from 19.0, when the shipping
  address lacks the city, country, email, name, street or zip (20.0 also refuses fields
  that are too long).

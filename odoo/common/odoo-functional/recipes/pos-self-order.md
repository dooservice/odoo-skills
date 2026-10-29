# Point of Sale: self-ordering and online payment

Customers order by themselves from a QR code on their phone or from a kiosk, and pay by
card terminal, online, or later at the counter; the order lands in the shop's open session
like any POS order. A cashier can also take an online payment for a POS order: the customer
pays on a web page through a payment provider. Needs `point_of_sale` with `pos_self_order`
and `pos_online_payment` (both 17.0+; 16.0 has neither). Shops, payment methods and
sessions are in [point-of-sale.md](point-of-sale.md); restaurant floors and tables in
[pos-restaurant.md](pos-restaurant.md); payment terminals in
[pos-hardware.md](pos-hardware.md); payment providers (Stripe, Adyen, PayPal and others
on the web) in [website-and-ecommerce.md](website-and-ecommerce.md). The preparation
display and the IoT box are Enterprise and left out.

## Before you start

- Apps: `pos_self_order` (17.0+), `pos_online_payment` (17.0+, needs `account_payment`).
  Their bridges install by themselves: `pos_online_payment_self_order` (online payment
  in self-ordering), `pos_self_order_stripe` (Stripe terminal on a kiosk, 17.0 to 19.0),
  `pos_self_order_sale` (gives kiosk orders the `Kiosk Sale Team` when `pos_sale` is
  installed), `pos_self_order_sms` (20.0, SMS confirmation per preset).
- Settings: Point of Sale ‣ Configuration ‣ Settings, pick the shop, section Mobile
  self-order & Kiosk. The fields are the shop's own, written below on `pos.config`.
- Users: the self-order default user (`self_ordering_default_user_id`) must be a POS user;
  its rights apply when customers browse with no session open.
- Read first:

```python
for c in env['pos.config'].search([]):
    print(c.id, c.name, c.module_pos_restaurant, c.self_ordering_mode, c.self_ordering_service_mode,
          c.self_ordering_pay_after, c.self_ordering_default_user_id.login, c.current_session_state,
          c.self_order_online_payment_method_id.name)
print(env['pos.payment.method'].search_read([('type', '=', 'online')], ['name', 'online_payment_provider_ids', 'config_ids']))
print(env['payment.provider'].search_read([('state', 'in', ('enabled', 'test'))], ['name', 'code', 'state', 'is_published']))
```

That is 20.0; in 17.0 to 19.0 search the online methods with
`[('is_online_payment', '=', True)]`.

## The standard flow

Odoo's self-ordering documentation: choose the mode, the service and when the customer
pays, add the payment, print the QR codes or start the kiosk, then serve from the open
session.

1. **Choose the mode.** Settings ‣ Mobile self-order & Kiosk ‣ QR menu & Kiosk
   activation, Self Ordering Mode (`self_ordering_mode`): `consultation` (QR menu, read
   only), `mobile` (QR menu + Ordering), `kiosk`, `nothing` (off).

   ```python
   config.write({'self_ordering_mode': 'mobile', 'self_ordering_service_mode': 'table', 'self_ordering_pay_after': 'meal'})
   print(config.self_ordering_mode, config.self_ordering_service_mode, config.self_ordering_pay_after, config.self_ordering_url)
   env.cr.commit()
   ```

   Leaves the shop with its self-ordering URL (`self_ordering_url`).

2. **Service and payment moment.** Service (`self_ordering_service_mode`): `table` (the
   order goes to the customer's table, restaurant shops only), `counter` (Pickup zone),
   `dynamic_qr` (20.0: a QR code printed per order). Pay After (`self_ordering_pay_after`):
   `meal` (the waiter collects payment at the end) or `each` (the customer pays every
   order). Odoo forces `each` for `kiosk`, for `mobile` with `counter`, and for `mobile`
   in a shop that is not a restaurant; `meal` with `mobile` forces `table`.

3. **Payment.** For orders paid by the customer, give the shop a way to pay:
   - Online (QR menu + Ordering, Kiosk): create an online payment method (step 4) and set
     it in Settings ‣ Online Payment (`self_order_online_payment_method_id`); empty, the
     customer pays at the cashier.
   - Card terminal (Kiosk): add a terminal payment method of a provider with a kiosk
     bridge (see `## Versions`); device setup in [pos-hardware.md](pos-hardware.md).
   - Cash (Kiosk, 20.0 only): a cash method of the shop shows on the kiosk.

   From 19.0, `config.has_valid_self_payment_method()` tells whether the shop has one.

4. **Online payment method.** Point of Sale ‣ Configuration ‣ Payment Methods ‣ New, tick
   Online Payment (17.0 to 19.0) or set Type Online (20.0), and choose the Allowed
   Providers (empty means every published provider). The provider must be enabled and
   published (see [website-and-ecommerce.md](website-and-ecommerce.md)) and work in the
   shop's currency.

   20.0:

   ```python
   online_method = env['pos.payment.method'].create({
       'name': 'Online Payment', 'type': 'online', 'online_payment_provider_ids': [(6, 0, providers.ids)],
   })
   config.write({'payment_method_ids': [(4, online_method.id)], 'self_order_online_payment_method_id': online_method.id})
   print(online_method.journal_id, online_method.has_an_online_payment_provider)
   env.cr.commit()
   ```

   17.0 to 19.0: the same with `'is_online_payment': True` in place of `'type': 'online'`.

   Leaves a method without journal: Odoo clears the journal, the accounts and the terminal
   on it. A shop accepts one online method only.

5. **Home buttons, languages, look.** Settings: Home buttons (`pos_self_order.custom_link`:
   label, URL, shops), Language (`self_ordering_default_language_id`,
   `self_ordering_available_language_ids`), Splash screens
   (`self_ordering_image_home_ids`), Customize Header up to 19.0
   (`self_ordering_image_brand`), Background and Color in 20.0
   (`self_ordering_image_background_ids`, `self_ordering_primary_color`). Preview Web
   interface opens the customer view.

6. **Publish it.** QR modes: Settings ‣ Print QR Codes or Download QR Codes, one per table
   in a restaurant, one for the shop otherwise; the Dashboard card ‣ Mobile Menu opens the
   same page. Kiosk: Dashboard ‣ Start Kiosk opens a session and gives the kiosk URL to
   open on the device; Open Kiosk while it runs.

   ```python
   print(config.self_ordering_url)
   for table in config.floor_ids.table_ids:
       print(table.display_name, table.identifier)
   ```

7. **Serve.** Customers order only while the shop has an open session. Each order arrives
   in the POS as an order of the session (with its table in a restaurant); with `meal`,
   the waiter collects payment in the POS; with `each`, the order arrives paid. Close the
   session as in [point-of-sale.md](point-of-sale.md); a kiosk session closed from the
   POS deletes its unpaid draft orders.

   ```python
   orders = env['pos.order'].search([('session_id', '=', config.current_session_id.id)])
   print([(o.name, o.state, o.amount_total, o.amount_paid, o.source, o.table_id.display_name) for o in orders])
   ```

   That is 19.0 and 20.0 in a restaurant shop; 17.0 and 18.0 have no `source`, and a
   retail shop has no `table_id`: drop them from the print.

## Variations

- **Online payment at the counter (no self-ordering).** Add the online method to the shop.
  In the POS the cashier picks Online Payment; the customer scans the QR code shown and
  pays on the provider's page; the payment line is recorded once the transaction is done.
  The provider payment (`account.payment`, linked by `pos_order_id`) reaches the POS
  receivable and is cleared at session closing.
- **Eat in or take out.** 17.0: Eat in / Take out (`self_ordering_takeaway`) with the
  take-out fiscal position (`self_ordering_alternative_fp_id`). 18.0: Allow takeout order
  (`self_ordering_takeaway`), shown when the restaurant's own Eat in / Take out
  (`takeaway`) is on. 19.0+: presets (`pos.preset`, see
  [pos-restaurant.md](pos-restaurant.md)) are what the customer picks.
- **SMS confirmation (20.0).** On a preset, set SMS Receipt Template
  (`sms_receipt_template_id`, a `sms.template` of `pos.order`): a paid mobile or kiosk
  order with a phone number gets that SMS. Needs SMS credits (IAP).
- **Reset the QR codes** (developer mode, 17.0 to 19.0: Settings ‣ Reset QR Codes) when old
  printed codes must stop working.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Self-ordering and online payment | none | yes | yes | yes | yes |
| Service modes | | `counter`, `table` | same | same | adds `dynamic_qr` |
| Take-out | | `self_ordering_takeaway`, `self_ordering_alternative_fp_id` | `self_ordering_takeaway` | presets | presets |
| Online method flag | | `is_online_payment` | same | same | `type='online'` |
| Order origin field | | none | none | `source` (`mobile`, `kiosk`) | same |
| Kiosk terminals | | Adyen, Stripe | adds Razorpay | adds Pine Labs, QFPay, Viva.com | any method with a `payment_provider`; bridges for Razorpay, Pine Labs, QFPay, Bancontact Pay |
| Kiosk cash | | no | no | no | yes |
| SMS per preset | | | | | `pos_self_order_sms` |

## Verify

```python
config = env['pos.config'].browse(<shop id>)
print(config.self_ordering_mode, config.self_ordering_service_mode, config.self_ordering_pay_after, config.self_ordering_url)
print(config.current_session_state, config.payment_method_ids.mapped('name'))
```

Then open the URL on a phone (or the kiosk), place an order, and check it in the POS of
the open session; pay once online and check the payment on the order.

## Pitfalls

- Nothing can be ordered while the shop has no open session; the menu still shows.
- In Community, Odoo labels Pay After Each Order "require Odoo Enterprise". Kiosk and
  pickup-zone ordering run in that mode: tell the user before promising them on a
  Community database.
- `self_ordering_default_user_id` must be a POS user, or saving the settings fails.
- An online payment method whose providers are not published, or use another currency
  than the shop, is refused or shows no provider to the customer.
- Two online methods in one shop are refused (`The ... already has one online payment.`).
- Kiosk with no valid payment method: customers cannot finish; add an online or terminal
  method (or cash in 20.0).

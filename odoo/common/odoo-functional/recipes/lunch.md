# Lunch: vendors, orders and employee accounts

Employees order meals from lunch vendors (`lunch.supplier`) through the Lunch app; each
order line (`lunch.order`) is paid from the employee's lunch account, whose balance is
the sum of cash moves (`lunch.cashmove`: money the employee put in) minus their orders.
A lunch manager sends the day's orders to each vendor, marks them received when the food
arrives and notifies the employees. Alerts (`lunch.alert`) remind employees to order.
This recipe covers `lunch` (Community). Nothing here posts to accounting: the cash an
employee hands in is recorded only as a cash move.

## Before you start

- Apps: `lunch`.
- Access: Lunch: User : Order your meal (`lunch.group_lunch_user`) orders; Lunch:
  Administrator (`lunch.group_lunch_manager`) manages vendors, products, cash moves and
  today's orders. Up to 18.0 the default user template gets Administrator; check new
  users' groups.
- Settings (Lunch ‣ Configuration ‣ Settings):
  - `company_lunch_minimum_threshold`, Maximum Allowed Overdraft: how far below zero an
    account may go. At 0 an employee orders only with money already in the account.
  - `company_lunch_notify_message`: the message employees get when their order arrives.

```python
env['res.config.settings'].create({'company_lunch_minimum_threshold': 20.0}).execute()
env.cr.commit()
```

- Read first:

```python
print(env['lunch.supplier'].search_read([], ['name', 'send_by', 'automatic_email_time', 'available_today', 'available_location_ids']))
print(env['lunch.product'].search_read([], ['name', 'supplier_id', 'category_id', 'price', 'active']))
print(env['lunch.location'].search_read([], ['name', 'address']))
print(env.company.lunch_minimum_threshold)
print(env['lunch.cashmove'].get_wallet_balance(user))
```

## The standard flow

The order of Odoo's Lunch documentation: settings, locations, vendors, products, alerts;
then the employee's order and the manager's day.

1. **Location.** Lunch ‣ Configuration ‣ Locations ‣ New: where meals are delivered.

   ```python
   location = env['lunch.location'].create({'name': 'Office A', 'address': '<address>'})
   ```

2. **Vendor.** Lunch ‣ Configuration ‣ Vendors ‣ New: the vendor contact, the days it
   delivers, the locations it serves and how orders reach it.

   ```python
   supplier = env['lunch.supplier'].create({
       'partner_id': vendor.id, 'responsible_id': lunch_manager.id,
       'available_location_ids': [(6, 0, location.ids)],
       'mon': True, 'tue': True, 'wed': True, 'thu': True, 'fri': True, 'sat': False, 'sun': False,
       'send_by': 'mail', 'automatic_email_time': 11.0, 'tz': 'UTC',
       'topping_label_1': 'Extras', 'topping_quantity_1': '0_more',
   })
   env.cr.commit()
   ```

   That is 20.0, where Order Time runs from 0 to 24. In 16.0 to 19.0 it runs from 0 to
   12 and `moment` (`am`, `pm`) says which half of the day:

   ```python
   supplier = env['lunch.supplier'].create({
       'partner_id': vendor.id, 'responsible_id': lunch_manager.id,
       'available_location_ids': [(6, 0, location.ids)],
       'mon': True, 'tue': True, 'wed': True, 'thu': True, 'fri': True, 'sat': False, 'sun': False,
       'send_by': 'mail', 'automatic_email_time': 11.0, 'moment': 'am', 'tz': 'UTC',
       'topping_label_1': 'Extras', 'topping_quantity_1': '0_more',
   })
   env.cr.commit()
   ```

   `send_by` is `mail` or `phone` (the default).

   A `mail` vendor gets the day's orders by email at Order Time, sent by a scheduled
   action created with the vendor; after that time employees can no longer order from
   it that day. A `phone` vendor is called by the manager, who then clicks Send Orders.
   Extras (`lunch.topping`, three groups per vendor: `topping_ids_1` to `_3`) are
   priced add-ons such as drinks.

3. **Product.** Lunch ‣ Configuration ‣ Product Categories, then Products ‣ New.

   ```python
   category = env['lunch.product.category'].create({'name': 'Sandwiches'})
   product = env['lunch.product'].create({
       'name': 'Product A', 'category_id': category.id, 'supplier_id': supplier.id, 'price': 6.5,
   })
   ```

4. **Alert.** Lunch ‣ Configuration ‣ Alerts ‣ New: a message shown in the app
   (`mode='alert'`) or sent by chat (`chat`) at a time, on chosen days and locations.

   ```python
   env['lunch.alert'].create({
       'name': 'Order reminder', 'message': '<p>Order before 11:00.</p>', 'mode': 'chat',
       'recipients': 'everyone', 'notification_time': 10.0, 'location_ids': [(6, 0, location.ids)],
   })
   env.cr.commit()
   ```

   That is 20.0 (0 to 24). In 16.0 to 19.0 `notification_time` runs from 0 to 12: add
   `notification_moment` (`am`, `pm`).

5. **Money in.** Lunch ‣ Manager ‣ Cash Moves ‣ New, when an employee hands in cash.

   ```python
   env['lunch.cashmove'].create({'user_id': user.id, 'amount': 50.0, 'description': 'Cash top-up'})
   env.cr.commit()
   ```

6. **Order.** Lunch ‣ My Lunch ‣ New Order, by the employee: pick the product, extras and
   note, Add To Cart, then Order Now in the cart.

   ```python
   order = env['lunch.order'].with_user(user).create({
       'product_id': product.id, 'quantity': 1, 'note': '<note>',
       'lunch_location_id': location.id, 'date': '<YYYY-MM-DD>',
   })
   order.with_user(user).action_order()
   env.cr.commit()
   ```

   That is 18.0 to 20.0, where `date` may be a later day the vendor delivers (it
   defaults to today). In 16.0 and 17.0 leave `date` out: orders are for today.

   Add To Cart leaves the line `new` (To Order); Order Now leaves it `ordered` and takes
   its price off the account. It is refused when the account, plus the allowed
   overdraft, would go below zero, or when the vendor does not deliver that day.

7. **Send to the vendor.** Lunch ‣ Manager ‣ Today's Orders, Send Orders on the vendor's
   group (phone vendors; mail vendors are sent automatically).

   ```python
   supplier.action_send_orders()
   ```

   Leaves the day's `ordered` lines `sent`.

8. **Receive.** Today's Orders, Confirm Orders on the vendor's group when the food
   arrives (Receive on a single line).

   ```python
   supplier.action_confirm_orders()
   orders = env['lunch.order'].search([('supplier_id', '=', supplier.id), ('state', '=', 'confirmed'), ('notified', '=', False)])
   orders.action_notify()
   env.cr.commit()
   ```

   Leaves the lines `confirmed` (Received). Send Notification (`action_notify()`) sends
   each employee the notification message once.

9. **Control.** Lunch ‣ Manager ‣ Control Accounts (`lunch.cashmove.report`): every
   employee's cash moves and orders, the balance per employee; Control Vendors: all
   orders by vendor.

## Variations

- **Cancel**: Cancel on a line in Today's Orders (`order.action_cancel()`) gives the
  money back; Reset (`action_reset()`) makes it `ordered` again. An employee removes
  their own lines from the cart only before they are sent.
- **Re-order**: Re-order in My Order History (`order.action_reorder()`) copies a past
  line to today as `ordered`.
- **Correcting an account**: a negative cash move (`amount < 0`) takes money off, for
  example when an employee leaves and gets their balance back.
- **Favorites and new products**: employees star products (`is_favorite`); `new_until`
  marks a product as new until a date.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Vendor order time | 0-12 + `moment` AM/PM | same | same | same | 0-24, no `moment` |
| Alert time | `notification_time` + `notification_moment` | same | same | same | 0-24, no moment |
| Order for a later day | no, today only | no | yes, `date` on the order | yes | yes |
| Default user template | Lunch Administrator | same | same | not set (demo only) | default group gives Lunch User |
| User groups field | `groups_id` | same | same | `group_ids` | same |

## Verify

```python
print(env['lunch.cashmove'].get_wallet_balance(user, include_config=False))
print(env['lunch.order'].search_read([('user_id', '=', user.id)], ['date', 'name', 'supplier_id', 'price', 'state', 'notified'], order='date desc', limit=10))
print(env['lunch.cashmove.report'].search_read([('user_id', '=', user.id)], ['date', 'description', 'amount'], order='date desc', limit=10))
```

## Pitfalls

- With Maximum Allowed Overdraft at 0, nobody can order until a cash move puts money in
  their account; set the overdraft or record the money first.
- The balance counts lines `ordered` and `confirmed` only: between Send Orders and
  Receive a line is `sent` and its price is not counted, so the balance looks higher
  than it is. Receive the orders the same day.
- A `mail` vendor's order email goes to the vendor contact from the vendor's Responsible
  (`responsible_id`): both need an email address, or the email fails.
- Archiving a vendor archives its products; unarchiving it brings them back.
- The shell runs as superuser: create orders `with_user()` the employee, as above; the
  order belongs to the creating user.
- The vendor's `tz` decides when Order Time falls; set it to the office time zone.
- Grant the group on the user: `user.write({'group_ids': [(4, env.ref('lunch.group_lunch_user').id)]})`
  in 19.0 and 20.0; the field is `groups_id` in 16.0 to 18.0.

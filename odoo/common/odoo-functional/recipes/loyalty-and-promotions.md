# Loyalty and promotions: discounts, coupons, gift cards, eWallet

A program (`loyalty.program`) gives rewards (`loyalty.reward`) when an order meets its
conditional rules (`loyalty.rule`). Its `program_type` sets the defaults: promotions,
discount codes, coupons, buy X get Y, next order coupons, loyalty cards, gift cards and
eWallet. Points live on cards (`loyalty.card`): a coupon, a gift card, a customer's loyalty
card or eWallet. In Sales, `sale_loyalty` applies the rewards on quotations as reward lines;
`sale_loyalty_delivery` adds free shipping. The same programs work in Point of Sale
(`pos_loyalty`) and eCommerce (`website_sale_loyalty`), both summarised under Variations.
All of it is Community.

**At a glance**

- Apps: `loyalty`, `sale_loyalty`; `sale_loyalty_delivery` (16.0 also `loyalty_delivery`);
  `pos_loyalty`, `website_sale_loyalty`.
- Names that change by version: menu Sales ‣ Products up to 19.0, Sales ‣ Promotions 20.0;
  `date_from` and `pricelist_ids` 17.0+; quotation button Promotions up to 17.0, Reward
  18.0+; `loyalty.history` 18.0+; `applies_on` default `future` in 20.0; `expire_after`
  and `once_per_user` 20.0; POS `gift_card_settings` up to 17.0; reward line taxes
  `tax_id` up to 18.0, `tax_ids` 19.0+.
- Sections: Before you start; The standard flow (1 create the program, 2 set the
  conditional rules, 3 set the rewards, 4 apply the rewards on the quotation, 5 apply a
  code, 6 confirm the order); Variations; Versions; Verify; Pitfalls.

## Before you start

- Apps: `loyalty`, with `sale_loyalty` (installed automatically with `sale`).
  `sale_loyalty_delivery` adds the Free Shipping reward when `delivery` is installed (16.0
  also needs `loyalty_delivery`, installed automatically). `pos_loyalty` and
  `website_sale_loyalty` install themselves with Point of Sale and eCommerce.
- Settings: `module_loyalty` (Sales ‣ Configuration ‣ Settings ‣ Discounts, Loyalty & Gift
  Card; also in the Point of Sale and Website settings). It installs `loyalty`.

```python
env['res.config.settings'].create({'module_loyalty': True}).execute()
env.cr.commit()
```

- Users: the programs menu needs `sales_team.group_sale_manager`.
- Read first:

```python
print(env['ir.module.module'].search_read([('name', 'in', ['loyalty', 'sale_loyalty', 'sale_loyalty_delivery',
    'loyalty_delivery', 'pos_loyalty', 'website_sale_loyalty'])], ['name', 'state']))
for p in env['loyalty.program'].with_context(active_test=False).search([]):
    print(p.id, p.name, p.program_type, p.trigger, p.applies_on, p.active, p.company_id.name,
          p.date_to, p.sale_ok, p.coupon_count, p.rule_ids.mapped('code'), p.reward_ids.mapped('description'))
```

## The standard flow

Odoo's documentation (Sales ‣ Products and prices ‣ Discount and loyalty programs) creates a
program, sets its rules and rewards, then applies it on a quotation. The program menu is
Sales ‣ Products ‣ Discount & Loyalty up to 19.0 and Sales ‣ Promotions ‣ Discount & Loyalty
in 20.0; gift cards and eWallet have their own menu next to it, Gift cards & eWallet.

1. **Create the program.** Sales ‣ Products ‣ Discount & Loyalty ‣ New (20.0: Sales ‣
   Promotions ‣ Discount & Loyalty ‣ New), pick a template or set the Program Type.

   ```python
   program = env['loyalty.program'].create({
       'name': 'Spring promotion', 'program_type': 'promotion',
       'company_id': company.id, 'date_from': '2026-03-01', 'date_to': '2026-06-30',
   })
   print(program.trigger, program.applies_on, program.rule_ids.read(['minimum_amount']), program.reward_ids.mapped('description'))
   env.cr.commit()
   ```

   In 16.0 leave out `date_from`: the program has only `date_to`.

   Leaves an active program with the defaults of its type: `program_type` fills `trigger`
   (`auto`, `with_code`), `applies_on` (`current`, `future`, `both`), a first rule and a
   first reward. Passing `rule_ids` and `reward_ids` in the same `create` replaces those
   defaults.

   - Program types and what they default to:

     | `program_type` | Trigger | Applies on | Typical use |
     |---|---|---|---|
     | `promotion` | `auto` | `current` | Discount when the order meets the rule |
     | `promo_code` | `with_code` | `current` | Discount after typing a code on the rule |
     | `coupons` | `with_code` | `current` | Single-use codes generated in advance |
     | `buy_x_get_y` | `auto` | `current` | Free product per units bought |
     | `next_order_coupons` | `auto` | `future` | A coupon for the next order |
     | `loyalty` | `auto` | `both` (16.0-19.0), `future` (20.0) | Points per customer card |
     | `gift_card` | `auto` | `future` | Prepaid cards sold as a product |
     | `ewallet` | `auto` | `future` | Customer credit topped up by buying a product |

   - Limit it with `date_to` (17.0+: `date_from` too), `limit_usage` and `max_usage`, the
     company (`company_id`), the pricelists (`pricelist_ids`, 17.0+) and where it applies:
     `sale_ok` (Sales), `pos_ok` and `pos_config_ids` (Point of Sale), `ecommerce_ok` and
     `website_id` (eCommerce).

2. **Set the conditional rules.** The program's Rules section, one line per condition.

   ```python
   program.write({'rule_ids': [(5, 0, 0), (0, 0, {
       'minimum_amount': 100, 'minimum_amount_tax_mode': 'excl', 'minimum_qty': 0,
       'product_category_id': category.id,
       'reward_point_mode': 'order', 'reward_point_amount': 1,
   })]})
   env.cr.commit()
   ```

   Leaves a rule that grants `reward_point_amount` points `per order`, `per <currency>
   spent` (`money`) or `per unit paid` (`unit`) when the order reaches `minimum_qty` and
   `minimum_amount` on the products selected by `product_ids`, `product_category_id`,
   `product_tag_id` or `product_domain`.

   - `mode` `with_code` and `code` turn the rule into a discount code; a code is unique
     among active rules.
   - `minimum_amount_tax_mode` is `incl` by default: the minimum is compared with taxes.

3. **Set the rewards.** The program's Rewards section.

   ```python
   program.write({'reward_ids': [(5, 0, 0), (0, 0, {
       'reward_type': 'discount', 'discount': 10, 'discount_mode': 'percent',
       'discount_applicability': 'order', 'discount_max_amount': 50, 'required_points': 1,
   })]})
   print(program.reward_ids.discount_line_product_id.display_name)
   env.cr.commit()
   ```

   Leaves a reward with its own discount product (`discount_line_product_id`), created by
   Odoo and used on the reward line.

   - `reward_type`: `discount`, `product` (Free Product: `reward_product_id` or
     `reward_product_tag_id`, `reward_product_qty`) and, with `sale_loyalty_delivery`,
     `shipping` (Free Shipping, capped by `discount_max_amount`).
   - `discount_mode`: `percent`, `per_order` (a fixed amount) or `per_point` (an amount per
     point, used by gift cards and eWallet).
   - `discount_applicability`: `order`, `cheapest` (Cheapest Product) or `specific`
     (`discount_product_ids`, `discount_product_category_id`, `discount_product_tag_id`).
   - `required_points`: points the reward costs; `clear_wallet` spends all of them.
   - A program needs at least one reward.

4. **Apply the rewards on the quotation.** Create the quotation (`sales-and-crm.md`, step
   4), then its Promotions button (16.0, 17.0) or Reward button (18.0+). Automatic programs
   are not applied by saving the quotation: the button computes them.

   ```python
   action = order.action_open_reward_wizard()
   if isinstance(action, dict):
       wizard = env['sale.loyalty.reward.wizard'].with_context(active_id=order.id).create({})
       print(wizard.reward_ids.mapped('description'))
       wizard.selected_reward_id = wizard.reward_ids[:1]
       wizard.action_apply()
   print(order.order_line.filtered('is_reward_line').mapped(lambda l: (l.name, l.price_unit, l.tax_ids.ids)))
   env.cr.commit()
   ```

   In 16.0 to 18.0 the line's taxes are `tax_id`, not `tax_ids`.

   Leaves one negative reward line per tax group (`is_reward_line`, `reward_id`,
   `coupon_id`). When only one reward is claimable the button applies it without opening
   the wizard; with none it does nothing.

5. **Apply a code.** The quotation's Coupon Code button, for `promo_code` rules, coupons
   and gift cards.

   ```python
   status = order._try_apply_code('SPRING10')
   if 'error' in status:
       print(status['error'])
   else:
       for coupon, rewards in status.items():
           print(order._apply_program_reward(rewards[:1], coupon))
   env.cr.commit()
   ```

   Leaves the reward line on the quotation and the rule in `code_enabled_rule_ids` (a code
   rule) or the card in `applied_coupon_ids` (a coupon or gift card). The button does the
   same through `sale.loyalty.coupon.wizard` (`coupon_code`, `action_apply`) and then the
   reward wizard of step 4. Loyalty cards and eWallet cannot be applied by code: they are
   found from the customer.

6. **Confirm the order.** The Confirm button.

   ```python
   order.action_confirm()
   print([(c.program_id.name, c.code, c.partner_id.name, c.points) for c in order.coupon_point_ids.coupon_id])
   env.cr.commit()
   ```

   Leaves the order in `sale` and the points of each card updated: points earned are
   added, rewards used are deducted, and cards created by the order (next order coupons,
   gift cards bought) are sent by the program's communication plan. Unclaimed coupons of
   `current` programs are deleted. 18.0+ writes each movement in `loyalty.history`; 19.0+
   shows a Rewards Available notice when claimable rewards were left out.

## Variations

- **Coupons.** Program type `coupons`, then the program's Generate Coupons button
  (`loyalty.generate.wizard`): `mode` `anonymous` with `coupon_qty`, or `selected` with
  `customer_ids` / `customer_tag_ids`; `points_granted` and `valid_until`. Each coupon is a
  card with a unique `code`; the program's smart button lists them, and their Send button
  mails one.

  ```python
  env['loyalty.generate.wizard'].with_context(active_id=program.id).create({
      'mode': 'anonymous', 'coupon_qty': 20, 'points_granted': 1, 'valid_until': '2026-12-31',
  }).generate_coupons()
  print(program.coupon_ids.mapped('code')[:5])
  env.cr.commit()
  ```

- **Discount code.** Program type `promo_code`: the code is on the rule (`code`); the
  customer types it at step 5. 20.0 adds `once_per_user` (one use per customer, kept in
  `partner_ids`).
- **Buy X get Y.** Program type `buy_x_get_y`: a rule with `reward_point_mode` `unit` and
  `minimum_qty`, and a `product` reward whose `required_points` is the number of units to
  buy. Apply it at step 4.
- **Next order coupons.** Program type `next_order_coupons`: confirming an order that meets
  the rule creates a coupon for the customer and mails it; it is used on a later order at
  step 5.
- **Loyalty cards.** Program type `loyalty`: each customer gets a card (`partner_id`) that
  collects points on confirmed orders; rewards cost `required_points` and appear at step 4
  once the card has enough. 20.0 adds Points Validity (`expire_after`, in days); its card
  balance is computed from `loyalty.history`. From 17.0 the customer form has a loyalty
  cards smart button.
- **Gift cards.** Gift cards & eWallet ‣ New, type `gift_card` (17.0+ installs a Gift Cards
  program, `loyalty.gift_card_program`). Sell the trigger product (`loyalty.gift_card_product_50`,
  a service at 50, on the rule's `product_ids` with `reward_point_split`): confirming the
  order creates one card per unit with its value in points and mails it. Or print them in
  advance with Generate Gift Cards. The customer pays with it at step 5 (its code): the
  reward line deducts up to the card balance.
- **eWallet.** Gift cards & eWallet ‣ New, type `ewallet`: selling the top-up product
  (`loyalty.ewallet_product_50`) adds its amount to the customer's eWallet card; Generate
  eWallet credits chosen customers. The balance appears as a reward at step 4 for that
  customer.
- **Free shipping.** Add the delivery line first (the quotation's shipping button,
  `action_open_delivery_wizard`), then a `shipping` reward applies at step 4. Only one
  shipping reward per order.
- **Correct a balance.** 16.0, 17.0: edit `points` on the card. 18.0+: click the card's
  Balance, which opens Update Balance (`loyalty.card.update.balance`: `new_balance`,
  `description`) and records the change in the history.

  ```python
  wizard = env['loyalty.card.update.balance'].create({'card_id': card.id, 'new_balance': 120, 'description': 'Goodwill'})
  wizard.action_update_card_point()
  env.cr.commit()
  ```

- **Point of Sale.** The same programs with `pos_ok`; `pos_config_ids` limits them to some
  shops (empty means all). Rewards and codes are applied by the cashier in the session.
  Point of Sale ‣ Products ‣ Discount & Loyalty and ‣ Gift cards & eWallet open the same
  lists. 16.0, 17.0: the shop setting `gift_card_settings` chooses Generate PDF cards
  (`create_set`) or Scan existing cards (`scan_use`). See `point-of-sale.md`.
- **eCommerce (`website_sale_loyalty`).** Website ‣ eCommerce ‣ Loyalty ‣ Discount &
  Loyalty and ‣ Gift cards & eWallet open the same programs. See
  `website-and-ecommerce.md` for the shop itself.
  1. **Offer the program online.** `ecommerce_ok` (Available on Website, on by default)
     and `website_id` (empty: every website).

     ```python
     program = env['loyalty.program'].search([('name', '=', 'Summer promotion')], limit=1)
     program.write({'ecommerce_ok': True, 'website_id': False})
     ```

  2. **Codes.** The customer types a code in the cart's promotion field, which applies it
     to the cart order (`_try_apply_code`). A link `/coupon/<code>` stores the code in the
     session and applies it to the cart, or to the next cart once a product is added.
  3. **Automatic rewards.** Every visit to the cart and the payment step recomputes the
     programs (`_update_programs_and_rewards`, `_auto_apply_rewards`). A reward that needs
     a choice (several rewards, or a product to pick) is shown in the cart and claimed
     through `/shop/claimreward`.
  4. **eWallet top-up.** From 19.0, `/wallet/top_up` puts the program's top-up product
     (`trigger_product_ids`) in the cart; publish that product on the website first.
  5. **Progress in the cart.** 20.0 shows how far the cart is from each promotion, and the
     program form warns when a top-up product is not published
     (`show_non_published_product_warning`).

  Only `ecommerce_ok` programs apply on website orders; a code that works on a quotation
  but not in the shop is usually a program with `ecommerce_ok` off or another
  `website_id`.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Menu | Sales ‣ Products ‣ Discount & Loyalty, Gift cards & eWallet | same | same | same | Sales ‣ Promotions ‣ Discount & Loyalty, Gift cards & eWallet |
| eCommerce | codes, `/coupon/<code>`, rewards to claim in the cart | same | same | adds eWallet top-up from the shop | adds promotion progress in the cart |
| Validity | `date_to` | `date_from`, `date_to` | same | same | same |
| Pricelists on program | no | `pricelist_ids` | same | same | same |
| Quotation button for rewards | Promotions | Promotions | Reward | Reward | Reward |
| Loyalty `applies_on` default | `both` | `both` | `both` | `both` | `future` |
| Points history | none | none | `loyalty.history`, Update Balance | same | same; card `points` computed from history |
| Points validity | no | no | no | no | `expire_after` |
| Once per customer (codes) | no | no | no | no | `once_per_user` |
| Gift card program on install | demo only | `loyalty.gift_card_program` | same | same | same |
| Free shipping | `loyalty_delivery` + `sale_loyalty_delivery` | `sale_loyalty_delivery` | same | same | same |
| Customer smart button (cards) | no | yes | yes | yes | yes |
| Gift cards smart button on order | no | no | no | `action_view_gift_cards` | same |
| Rewards Available notice on confirm | no | no | no | yes | yes |
| POS `gift_card_settings` | yes | yes | no | no | no |
| Reward line taxes field | `tax_id` | `tax_id` | `tax_id` | `tax_ids` | `tax_ids` |

## Verify

```python
print(program.active, program.coupon_count, program.order_count, program.total_order_count)
print([(l.name, l.price_unit, l.reward_id.description, l.coupon_id.code, l.points_cost)
       for l in order.order_line.filtered('is_reward_line')])
for card in env['loyalty.card'].search([('program_id', '=', program.id)], limit=10):
    print(card.code, card.partner_id.name, card.points, card.expiration_date, card.use_count)
```

The order carries the reward lines, the program counts the order, and each card shows the
balance expected after the confirmation.

## Pitfalls

- An automatic promotion does not appear on a quotation until the Promotions / Reward
  button is pressed or the order is confirmed: press it before sending the quotation.
- `minimum_amount_tax_mode` defaults to `incl`: a minimum of 100 is reached by 87 plus
  taxes. Set `excl` when the minimum is meant before taxes.
- An active program cannot be deleted, and a program with cards cannot be deleted at all
  (`program_id` on the card is `ondelete='restrict'`): archive it.
- A rule code must be unique among active rules and must not be a card's code: reusing
  the code of an old program fails until that program is archived.
- Selling a gift card or an eWallet top-up books income on its product's income account;
  the accountant decides that account (`property_account_income_id` on the product)
  before the first sale.
- Points are counted on confirmation: cancelling a confirmed order removes the points it
  earned and frees the rewards it used.
- On a copy of production, coupons and gift cards created by confirmed orders queue their
  emails: outgoing mail is usually off there.

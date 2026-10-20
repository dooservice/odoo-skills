# Website and eCommerce

A database can run several websites (`website`), each with its domain, company,
languages and shop settings. The shop (`website_sale`) sells published products, grouped
in shop categories (`product.public.category`), priced with the website's pricelists,
delivered with delivery methods (`delivery.carrier`) and paid through payment providers
(`payment.provider`). Pages, menus, snippets and themes are edited by the user in the
website builder; that is outside this recipe.

## Before you start

- Apps: `website_sale`. 16.0 also needs `website_sale_delivery` for delivery methods at
  checkout (ask before installing); from 17.0 `website_sale` depends on `delivery`.
- Settings (Website ‣ Configuration ‣ Settings, per website): `account_on_checkout`,
  `auth_signup_uninvited`, `show_line_subtotals_tax_selection`, `group_product_pricelist`;
  18.0+ `ecommerce_access`. Pass `website_id` to `res.config.settings`, or the current
  website is used.
- Read first:

```python
mode = 'is_live' if 'is_live' in env['payment.provider'] else 'state'   # 20.0 / up to 19.0
print(env['website'].search_read([], ['name', 'domain', 'company_id', 'auth_signup_uninvited', 'account_on_checkout']))
print(env['product.template'].search_count([('is_published', '=', True)]), 'published products')
print(env['product.public.category'].search_read([], ['name', 'parent_id', 'website_id']))
print(env['delivery.carrier'].search_read([], ['name', 'delivery_type', 'is_published', 'website_id']))   # 16.0: needs website_sale_delivery
print(env['payment.provider'].search_read([('module_state', '=', 'installed')], ['name', 'code', mode, 'is_published', 'company_id']))
```

## The standard flow

1. **Shop settings.** Website ‣ Configuration ‣ Settings, choosing the website.

   ```python
   website = env['website'].search([('name', '=', '<website name>')])
   env['res.config.settings'].create({
       'website_id': website.id,
       'account_on_checkout': 'optional',
       'show_line_subtotals_tax_selection': 'tax_included',   # 16.0: see Versions
   }).execute()
   env.cr.commit()
   ```

   Leaves `website.account_on_checkout` `optional` and `auth_signup_uninvited` `b2c`:
   `optional` and `mandatory` set free sign-up, `disabled` (guest checkout only) sets
   sign-up on invitation (`b2b`). Prices show with taxes on this website.

2. **Shop categories.** Website ‣ eCommerce ‣ Products ‣ eCommerce Categories
   (20.0: ‣ Categories).

   ```python
   parent = env['product.public.category'].create({'name': '<category>'})
   child = env['product.public.category'].create({'name': '<subcategory>', 'parent_id': parent.id})
   env.cr.commit()
   ```

3. **Publish products.** Website ‣ eCommerce ‣ Products ‣ Products, the product's
   Published switch (or, in the list, the Is Published column).

   ```python
   product = env['product.template'].search([('default_code', '=', '<internal reference>')])
   product.write({'sale_ok': True, 'is_published': True, 'public_categ_ids': [(4, child.id)]})
   env.cr.commit()
   ```

   Leaves it visible to visitors of every website, or only of `website_id` when set.

4. **Delivery methods.** Website ‣ Configuration ‣ eCommerce ‣ Shipping Methods (16.0,
   17.0), Delivery Methods (18.0, 19.0), Deliveries (20.0); then New.

   ```python
   carrier = env['delivery.carrier'].create({
       'name': '<delivery method>', 'delivery_type': 'fixed', 'fixed_price': 5.0,
       'product_id': env.ref('delivery.product_product_delivery').id,
       'free_over': True, 'amount': 100.0, 'website_id': website.id, 'is_published': True,
   })
   env.cr.commit()
   ```

   Leaves a published method: 5.0 per order, free from 100.0. Only published methods are
   offered at checkout.

5. **Payment providers.** Website ‣ Configuration ‣ eCommerce ‣ Payment Providers
   (16.0–19.0), Payments (20.0); open the provider, enter its credentials, enable it.

   ```python
   provider = env.ref('payment.payment_provider_transfer')
   print(provider.module_id.name, provider.module_state)   # stop unless 'installed'
   provider.write({'state': 'enabled', 'is_published': True})   # 16.0-19.0
   provider.write({'is_live': True, 'is_published': True})      # 20.0
   env.cr.commit()
   ```

   Leaves the wire transfer offered at checkout; payments go to the provider's `journal_id`.
   The provider records exist before their module is installed (the wire transfer is
   `payment_custom`, not always installed). Never enable one whose `module_state` is not
   `installed`: its module holds the code that processes the payment. Ask the user before
   installing it (the form's Install button).

## Variations

- **Shop for logged-in users only** (18.0+): `ecommerce_access='logged_in'` (default
  `everyone`) in the same settings.
- **Accounts on invitation with mandatory login** (B2B): settings
  `account_on_checkout='mandatory'`, then a second settings record with
  `auth_signup_uninvited='b2b'` (the first one sets `b2c`).
- **A pricelist per website**: turn on `group_product_pricelist`, then Website ‣ eCommerce
  ‣ Products ‣ Pricelists, with `website_id` and `selectable` (the visitor may choose it).
  A pricelist without website is used only when `selectable` or with a promotion `code`.
  Rules: `pricelists.md`.
- **Delivery by rules**: `delivery_type='base_on_rule'` with `price_rule_ids`;
  `country_ids`, `state_ids`, `zip_prefix_ids` restrict where it ships. Carrier
  connectors add other types; several are Enterprise.
- **Other providers**: Community ships `payment_custom` (wire transfer and other manual
  methods), `payment_demo` (test only) and card or wallet gateways. `module_to_buy` True
  means Enterprise; `module_state` not `installed` means its module must be installed:
  ask first. Credentials come from the user; never invent them.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Delivery at checkout | `website_sale_delivery` | in `website_sale` | same | same | same |
| Tax display | company-wide, also back office: write `show_line_subtotals_tax_selection` with `group_show_line_subtotals_tax_included` True and `..._excluded` False | per website | per website | per website | per website; default from fiscal country; pricelist `tax_display` overrides |
| `ecommerce_access` | no | no | yes | yes | yes |
| Provider mode | `state`: `disabled`, `enabled`, `test` | same | same | same | `is_live` (False is test); archive to remove |
| `description_ecommerce` | no | yes | yes | yes | yes |

## Verify

```python
public = env.ref('base.public_user')
Products = env['product.template'].with_user(public).with_context(website_id=website.id)
domain = website.with_context(website_id=website.id).sale_product_domain() + [('is_published', '=', True)]
print(product.id in Products.search(domain).ids, product.website_url)
print(website.account_on_checkout, website.auth_signup_uninvited, carrier.is_published, provider.is_published)
```

Then ask the user to open the shop in a private window: find the product, add it to the
cart, check the price display, the delivery methods and the payment providers.

## Pitfalls

- `b2c` sign-up lets anyone create a portal account: ask before setting it.
- Publishing many products at once makes their prices and descriptions public: ask.
- The tax display only changes how prices show. Whether a price contains the tax is set
  on the tax (`taxes-and-journals.md`); the country's localization decides which taxes
  apply, see its localization skill if installed.
- A neutralized copy disables enabled providers (16.0–19.0) or puts them in test mode
  (20.0): no real payments there. Say so when the user tests in a copy. Never try a
  live provider with a real payment without the user's yes.
- Odoo's documentation for master still names a provider State field; 20.0 has `is_live`.

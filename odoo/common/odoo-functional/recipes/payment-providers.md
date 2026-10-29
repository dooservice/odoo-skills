# Payment providers and online payment of invoices

A payment provider (`payment.provider`) connects Odoo to a payment service (Stripe,
Adyen, PayPal and others) so customers pay online: invoices from the portal or a payment
link (`account_payment`), orders in the shop (`website-and-ecommerce.md`) and quotations
(`sales-and-crm.md`). Every provider follows the same setup: install its module, enter
the credentials the service gives, choose the payment methods, the journal, then switch
it from test to live. A successful transaction (`payment.transaction`) creates and
reconciles the payment in the provider's journal. `website_payment` adds the website
side (provider per website, the donation form up to 19.0), and
`account_payment_interco` (19.0+) lets one company collect invoices of another. All
providers listed here are in Community. Which providers work in which country and
currency is decided by each service: check it with the user.

## Before you start

- Apps: `account_payment` (installed by the setting below); the provider's module
  (`payment_<code>`), installed from the provider's form. Installing needs the user's
  yes.
- Settings (Invoicing ‣ Configuration ‣ Settings ‣ Customer Payments ‣ Invoice Online
  Payment):

```python
env['res.config.settings'].create({'module_account_payment': True}).execute()
env.cr.commit()
```

- Credentials come from the user's account at the payment service; never invent them,
  never paste them in chat logs or code.
- Read first:

```python
print(env['payment.provider'].search_read([], ['name', 'code', 'state', 'module_state', 'is_published', 'journal_id', 'company_id']))
print(env['payment.method'].search_read([('active', '=', True)], ['name', 'code']))
print(env['payment.transaction'].search_read([], ['reference', 'provider_id', 'amount', 'state'], limit=10, order='id desc'))
```

This is 17.0 to 19.0. In 20.0 replace `state` with `is_live` and `active`; 16.0 has no
`payment.method` (its icons are `payment.icon`).

## The standard flow

1. **Open the provider.** Invoicing ‣ Configuration ‣ Online Payments ‣ Payment
   Providers (menu by version in `## Versions`), the provider's card. If its module is
   not installed, the card shows Install (`button_immediate_install`).

   ```python
   provider = env.ref('payment.payment_provider_stripe')
   print(provider.module_id.name, provider.module_state, provider.module_to_buy)
   env.cr.commit()
   ```

   Stop unless `module_state` is `installed`, and ask before installing. `module_to_buy`
   True marks an Enterprise provider. The record exists before its module; the module
   holds the code that talks to the service.

2. **Enter the credentials.** The provider ‣ Credentials tab (in 20.0 the Credentials
   group of the Configuration tab): the fields in the table below. Stripe, and Razorpay, Mercado Pago, PayU and PayPal in recent versions, also
   offer a Connect button that fills them through the service's own sign-in; the user
   does it in the browser.

   ```python
   provider.write({'stripe_publishable_key': '<from the user>', 'stripe_secret_key': '<from the user>'})
   env.cr.commit()
   ```

3. **Choose payment methods** (17.0+). The provider ‣ Payment Methods (Configuration tab
   up to 19.0): activate the cards, wallets and local methods to offer. 16.0 shows
   payment icons only (`payment_icon_ids`), the service decides the methods.

   ```python
   cards = env.ref('payment.payment_method_card')
   provider.write({'payment_method_ids': [(4, cards.id)]})
   env.cr.commit()
   ```

   This is 17.0 to 19.0. In 20.0 each provider has its own methods
   (`payment.method` with `provider_id`): activate them with `active` True on
   `provider.with_context(active_test=False).payment_method_ids`.

4. **Set the journal and options.** The provider ‣ Configuration tab: Payment Journal
   (`journal_id`, a bank journal), `capture_manually` (authorize now, capture later,
   where `support_manual_capture`), `allow_tokenization` (save cards),
   `allow_express_checkout` (Apple Pay, Google Pay in the shop), `available_country_ids`,
   `available_currency_ids` (17.0+), `maximum_amount` (and `minimum_amount` in 20.0),
   and the Messages tab texts.

   ```python
   bank = env['account.journal'].search([('type', '=', 'bank'), ('company_id', '=', provider.company_id.id)], limit=1)
   provider.write({'journal_id': bank.id, 'capture_manually': False})
   env.cr.commit()
   ```

   Leaves payments posted in that journal, with the provider as payment method line.

5. **Test, then go live.** The provider ‣ State `test` with the service's test
   credentials; once a test payment succeeds, `enabled` with live credentials, and
   Published for the website.

   ```python
   provider.write({'state': 'test'})
   provider.write({'state': 'enabled', 'is_published': True})
   env.cr.commit()
   ```

   This is 16.0 to 19.0 (`state`: `disabled`, `test`, `enabled`). In 20.0 write
   `is_live` False for test, True for live, and archive (`active` False) to remove it.
   Going live takes real money: only with the user's yes.

6. **Let customers pay invoices.** A posted invoice shows Pay Now on the customer
   portal. To send a link: the invoice ‣ Actions ‣ Generate a Payment Link
   (`action_invoice_order_generate_link`).

   ```python
   wizard = env['payment.link.wizard'].with_context(active_model='account.move', active_id=invoice.id).create({})
   print(wizard.link)
   ```

   `amount` defaults to the amount due (or the next installment) and can be lowered
   for a partial payment. The link carries an access token: send it only to the
   customer.

7. **Follow the transaction.** When the service confirms, the transaction is `done`
   and a payment is created, posted and reconciled with the invoice (In Payment or Paid
   depending on the journal's outstanding account). Invoicing ‣ Configuration ‣ Online
   Payments ‣ Payment Transactions (20.0: the provider's Transactions smart button);
   the invoice's Payments smart button.

## Variations

- **Manual capture**: with `capture_manually`, the transaction stays `authorized`; the
  invoice or order shows Capture Transaction (`payment_action_capture`) and Void
  Transaction (`payment_action_void`). Authorizations expire at the service (often 7
  days).
- **Refund**: the payment ‣ Refund (`action_refund_wizard`, the wizard
  `payment.refund.wizard`, `amount_to_refund`), where the provider's `support_refund` is
  `full_only` or `partial`. It creates a refund transaction and a negative payment.
- **Saved cards**: with `allow_tokenization`, customers save a card (`payment.token`);
  Invoicing ‣ Configuration ‣ Online Payments ‣ Payment Tokens (20.0: the provider's
  Tokens smart button). Tokens are deleted by archiving.
- **Wire transfer and other manual methods**: `payment_custom` (the Wire Transfer
  provider, `custom_mode`), with instructions in the pending message;
  `payment_demo` only for tests.
- **A provider per website** (`website_payment`): the provider ‣ Website (`website_id`)
  limits it to one website. Website ‣ Configuration ‣ Settings shows the payment
  providers too.
- **Donations** (16.0 to 19.0, `website_payment`): the website editor's Donation block
  makes a form paid through the providers; payments carry `is_donation`. In 20.0
  donations are a product in the shop (`website_sale`).
- **Authorize.Net capture in the website settings** (16.0 to 18.0,
  `website_payment_authorize`): Website ‣ Configuration ‣ Settings ‣ Authorize.net:
  Payment Capture Method (`authorize_capture_method`: `auto`, `manual`) writes the
  provider's `capture_manually`.
- **One company collects for another** (19.0+, `account_payment_interco`): Invoicing ‣
  Configuration ‣ Settings ‣ Default Accounts ‣ Intercompany Clearing (multi-company
  only): `account_interco_clearing_journal_id`, `account_interco_payable_id`,
  `account_interco_receivable_id` on each company. A payment received by one company
  for another company's invoice then posts clearing entries in both and reconciles the
  invoice.

## Providers

The credentials are fields of `payment.provider`; those marked required must be filled
before the provider leaves `disabled` (16.0 to 19.0).

| Provider | Module | Required credentials | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|---|---|
| Adyen | `payment_adyen` | `adyen_merchant_account`, `adyen_api_key`, `adyen_client_key`, `adyen_hmac_key`; 16.0 `adyen_checkout_api_url`, `adyen_recurring_api_url`; 17.0 to 19.0 `adyen_api_url_prefix` | yes | yes | yes | yes | yes |
| Amazon Payment Services | `payment_aps` | `aps_merchant_identifier`, `aps_access_code`, `aps_sha_request`, `aps_sha_response` | yes | yes | yes | yes | yes |
| AsiaPay | `payment_asiapay` | `asiapay_merchant_id`, `asiapay_secure_hash_secret`, `asiapay_secure_hash_function`; 16.0 `asiapay_currency_id`; 17.0+ `asiapay_brand` | yes | yes | yes | yes | yes |
| Authorize.Net | `payment_authorize` | `authorize_login`, `authorize_transaction_key`, `authorize_signature_key`; 16.0 `authorize_payment_method_type` | yes | yes | yes | yes | yes |
| Buckaroo | `payment_buckaroo` | `buckaroo_website_key`, `buckaroo_secret_key` | yes | yes | yes | yes | yes |
| DPO | `payment_dpo` | `dpo_service_ref`, `dpo_company_token` | no | no | no | yes | yes |
| ECPay | `payment_ecpay` | `ecpay_merchant_id`, `ecpay_hash_key`, `ecpay_hash_iv` | no | no | no | yes | yes |
| Flutterwave | `payment_flutterwave` | `flutterwave_public_key`, `flutterwave_secret_key`, `flutterwave_webhook_secret` | yes | yes | yes | yes | yes |
| Iyzico | `payment_iyzico` | `iyzico_key_id`, `iyzico_key_secret` | no | no | no | yes | yes |
| Mercado Pago | `payment_mercado_pago` | up to 18.0 `mercado_pago_access_token`; from 19.0 `mercado_pago_account_country_id`, then Connect | yes | yes | yes | yes | yes |
| Mollie | `payment_mollie` | `mollie_api_key` | yes | yes | yes | yes | yes |
| Nuvei | `payment_nuvei` | `nuvei_merchant_identifier`, `nuvei_site_identifier`, `nuvei_secret_key` | no | no | yes | yes | yes |
| Paymob | `payment_paymob` | `paymob_account_country_id`, `paymob_public_key`, `paymob_secret_key`, `paymob_hmac_key`, `paymob_api_key` | no | no | no | yes | yes |
| PayPal | `payment_paypal` | `paypal_email_account`; 16.0, 17.0 also `paypal_pdt_token` (optional); 18.0, 19.0 `paypal_client_id`, `paypal_client_secret`; 20.0 Connect (onboarding) | yes | yes | yes | yes | yes |
| PayU | `payment_payu` | `payu_key_id`, `payu_merchant_salt`, or Connect | no | no | no | yes | yes |
| Razorpay | `payment_razorpay` | up to 18.0 `razorpay_key_id`, `razorpay_key_secret`, `razorpay_webhook_secret`; from 19.0 Connect (OAuth) or the same keys | yes | yes | yes | yes | yes |
| Razorpay OAuth | `payment_razorpay_oauth` | adds the Connect button to Razorpay (17.0, 18.0); in `payment_razorpay` from 19.0 | no | yes | yes | no | no |
| Redsys | `payment_redsys` | `redsys_merchant_code`, `redsys_merchant_terminal`, `redsys_secret_key` | no | no | no | yes | yes |
| Sips (Worldline) | `payment_sips` | `sips_merchant_id`, `sips_secret`, `sips_key_version`, `sips_test_url`, `sips_prod_url`, `sips_version` | yes | yes | no | no | no |
| Stripe | `payment_stripe` | `stripe_publishable_key`, `stripe_secret_key` (`stripe_webhook_secret` optional), or Connect | yes | yes | yes | yes | yes |
| Toss Payments | `payment_toss_payments` | `toss_payments_client_key`, `toss_payments_secret_key` | no | no | no | yes | yes |
| Worldline | `payment_worldline` | `worldline_pspid`, `worldline_api_key`, `worldline_api_secret`, `worldline_webhook_key`, `worldline_webhook_secret` | yes | yes | yes | yes | yes |
| Xendit | `payment_xendit` | `xendit_secret_key`, `xendit_webhook_token` (`xendit_public_key` from 18.0) | no | yes | yes | yes | yes |
| Wire transfer | `payment_custom` | none (`custom_mode`) | yes | yes | yes | yes | yes |
| Demo | `payment_demo` | none; test only | yes | yes | yes | yes | yes |

Alipay, Ogone, PayU Latam, PayUmoney (16.0, 17.0) are deprecated by Odoo: do not set up
new ones.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Provider mode | `state`: `disabled`, `test`, `enabled` | same | same | same | `is_live`, `active` |
| Payment methods | `payment.icon` | `payment.method`, shared (`provider_ids`) | same | same | one per provider (`provider_id`) |
| Menu: providers | Invoicing ‣ Configuration ‣ Payments ‣ Payment Providers | Invoicing ‣ Configuration ‣ Online Payments ‣ Payment Providers | same | same | Invoicing ‣ Configuration ‣ Online Payments |
| Menu: methods, tokens, transactions | ‣ Payment Icons, Payment Tokens, Payment Transactions | ‣ Payment Methods, Payment Tokens, Payment Transactions | same | same | smart buttons on the provider |
| `minimum_amount` | no | no | no | no | yes |
| Donation block | yes | yes | yes | yes | no (`website_sale`) |
| Intercompany clearing | no | no | no | `account_payment_interco` | same |

The same in every version: Invoicing ‣ Configuration ‣ Settings ‣ Customer Payments;
the invoice's Actions ‣ Generate a Payment Link; the payment's Refund button.

## Verify

```python
tx = env['payment.transaction'].search([('invoice_ids', 'in', invoice.ids)], order='id desc', limit=1)
print(tx.read(['reference', 'state', 'amount', 'payment_id']))
print(invoice.payment_state, tx.payment_id.journal_id.name)
```

The transaction is `done`, its payment is in the provider's journal, and the invoice is
`in_payment` or `paid`. Ask the user to pay a test invoice from the portal in test mode
before going live.

## Pitfalls

- A provider without `journal_id` takes payments that never reach the accounts:
  set it before enabling.
- Test credentials in an enabled provider (or live ones in test) fail every payment:
  check both together.
- Webhooks: services that notify Odoo need the public URL of the database; behind a
  private network the transaction stays `pending`. Set `web.base.url` right.
- A neutralized copy disables enabled providers (16.0 to 19.0) or puts them in test
  mode (20.0): no real payments there.
- Providers shipped by Odoo cannot be deleted (they have an external id): disable
  them (16.0 to 19.0) or archive them (20.0).
- Changing the company currency or country can make a provider unavailable: check
  `available_currency_ids` and `available_country_ids`.

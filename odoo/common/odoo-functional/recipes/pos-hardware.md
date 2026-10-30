# Point of Sale: card terminals, cash machines and printers

Devices the POS talks to without an IoT box: card terminals and QR payment providers
reached over the internet, cash machines and Epson or iMin printers on the shop's local
network. Each device is a `pos_<provider>` module; a terminal or a cash machine is a POS
payment method (`pos.payment.method`) linked to it, a printer is a receipt printer of the
shop or a `pos.printer`. Shops, payment methods and sessions are in
[point-of-sale.md](point-of-sale.md); kitchen printing in
[pos-restaurant.md](pos-restaurant.md); terminals on a kiosk in
[pos-self-order.md](pos-self-order.md). The IoT box and every device that needs it
(scales, IoT printers, `pos_iot_*` terminals) are Enterprise and left out.

**At a glance**

- Apps: the provider's `pos_<provider>` module (`module_pos_adyen`, `module_pos_stripe`,
  ... in the POS settings).
- Names that change by version: terminal link `use_payment_terminal` up to 17.0,
  `payment_method_type='terminal'` 18.0 and 19.0, `payment_method_type` +
  `payment_provider` 20.0; `type` required 20.0; cash machines 19.0+ (`cash_machine` in
  20.0); Epson receipt printer `pos_epson_printer` up to 18.0, in `point_of_sale` 19.0,
  `pos.printer` with `use_type='receipt'` 20.0; preparation printer `restaurant.printer`
  in 16.0, `pos.printer` 17.0+; HTTP forced for ePOS printers up to 18.0; local network
  access `point_of_sale.use_lna` 19.0, `use_lna` per device 20.0.
- Sections: Before you start; The standard flow (1 install the provider's module, 2 create
  the payment method, 3 add it to the shop, 4 pay, 5 close the session); Card terminals
  and QR providers; Cash machines; Printers; Variations; Versions; Verify; Pitfalls.

## Before you start

- Apps: the provider's module from the tables below. Point of Sale ‣ Configuration ‣
  Settings, section Payment Terminals, installs the common ones (`module_pos_adyen`,
  `module_pos_stripe`, ...); in 20.0 the payment method form also lists the providers to
  install. Ask before installing: the module needs the provider's account.
- Credentials: API keys, merchant and terminal identifiers come from the provider's
  portal. Never invent them; ask the user for each value and store it only in the method.
- Payment methods with a terminal use a `bank` journal; cash machines a `cash` journal.
- Read first:

```python
PM = env['pos.payment.method']
for pm in PM.search([]):
    print(pm.id, pm.name, pm.type, pm.journal_id.type, pm.payment_method_type, pm.payment_provider, pm.config_ids.mapped('name'))
print(PM._fields['payment_provider'].get_values(env))
print(env['ir.module.module'].search_read([('name', '=like', 'pos_%'), ('state', '=', 'installed')], ['name']))
```

That is 20.0. In 18.0 and 19.0 the provider is `use_payment_terminal`; in 16.0 and 17.0
it is `use_payment_terminal` and there is no `payment_method_type`.

## The standard flow

The same for every terminal; the device tables say which field links it and which
credentials it needs.

1. **Install the provider's module.** Point of Sale ‣ Configuration ‣ Settings ‣ Payment
   Terminals, tick the provider, Save. A provider not listed there: Apps.

   ```python
   module = env['ir.module.module'].search([('name', '=', '<module>')])
   print(module.state)   # install from Apps or Settings, with the user's yes, then restart the shell
   ```

2. **Create the payment method.** Point of Sale ‣ Configuration ‣ Payment Methods ‣ New:
   a name, a `bank` journal; 16.0, 17.0: Use a Payment Terminal; 18.0, 19.0: Integration
   Terminal, then the terminal; 20.0: Integration Terminal (or Quick Pay (QR Code), Cash
   Machine), then Integrate with.

   20.0:

   ```python
   method = PM.create({
       'name': 'Card (<provider>)', 'type': 'bank', 'journal_id': bank_journal.id, 'company_id': company.id,
       'payment_method_type': 'terminal', 'payment_provider': '<value>',
       '<credential field>': '<value from the user>',
   })
   env.cr.commit()
   ```

   18.0, 19.0:

   ```python
   method = PM.create({
       'name': 'Card (<provider>)', 'journal_id': bank_journal.id, 'company_id': company.id,
       'payment_method_type': 'terminal', 'use_payment_terminal': '<value>',
       '<credential field>': '<value from the user>',
   })
   env.cr.commit()
   ```

   16.0, 17.0:

   ```python
   method = PM.create({
       'name': 'Card (<provider>)', 'journal_id': bank_journal.id, 'company_id': company.id,
       'use_payment_terminal': '<value>',
       '<credential field>': '<value from the user>',
   })
   env.cr.commit()
   ```

   Leaves the method linked to the terminal. Fields that show a URL to paste in the
   provider's portal (`adyen_event_url`, `viva_com_webhook_endpoint`,
   `viva_wallet_webhook_endpoint`, `mp_webhook_endpoint`) are filled by Odoo: give them
   to the user.

3. **Add it to the shop.** Settings of the shop, section Payment ‣ Payment Methods, or:

   ```python
   config.write({'payment_method_ids': [(4, method.id)]})
   env.cr.commit()
   ```

   Refused while the shop has a session not closed.

4. **Pay.** In the POS, on the payment screen, pick the method: the amount goes to the
   terminal, the customer pays, the line turns paid. Cancel on the payment line while
   the terminal waits. A refund is a refund order in the POS paid back with the same
   method; whether the terminal reverses the card payment depends on the provider.

5. **Close the session.** As in [point-of-sale.md](point-of-sale.md): each terminal
   method posts one payment to its journal at closing, like any bank method.

## Card terminals and QR providers

`Value` is what goes in `use_payment_terminal` (16.0 to 19.0) or `payment_provider`
(20.0).

| Module | Versions | Value | Credentials and settings on the method |
|---|---|---|---|
| `pos_adyen` | 16.0+ | `adyen` | `adyen_api_key`, `adyen_terminal_identifier`, `adyen_test_mode`; `adyen_merchant_account` (with `pos_restaurant_adyen` up to 19.0, built in from 20.0); shop: `adyen_ask_customer_for_tip` |
| `pos_stripe` | 16.0+ | `stripe` | `stripe_serial_number`; the keys are those of the Stripe payment provider (`payment_stripe`) |
| `pos_six` | 16.0 to 18.0 | `six` | `six_terminal_ip`; removed in 19.0 |
| `pos_mercury` | 16.0, 17.0 | `mercury` (Vantiv) | `pos_mercury_config_id`: a Vantiv configuration (`merchant_id`, `merchant_pwd`) in Point of Sale ‣ Configuration ‣ Vantiv Configurations, developer mode |
| `pos_mercado_pago` | 17.0+ | `mercado_pago` | `mp_bearer_token`, `mp_webhook_secret_key`, `mp_id_point_smart` |
| `pos_razorpay` | 17.0+ | `razorpay` | `razorpay_tid`, `razorpay_username`, `razorpay_api_key`, `razorpay_allowed_payment_modes`, `razorpay_test_mode` |
| `pos_paytm` | 17.0, 18.0 | `paytm` | `paytm_tid`, `paytm_mid`, `paytm_merchant_key`, `channel_id`, `accept_payment`, `allowed_payment_modes`, `paytm_test_mode` |
| `pos_viva_wallet` | 17.0, 18.0 | `viva_wallet` | `viva_wallet_merchant_id`, `viva_wallet_api_key`, `viva_wallet_client_id`, `viva_wallet_client_secret`, `viva_wallet_terminal_id`, `viva_wallet_test_mode` |
| `pos_viva_com` | 19.0+ | `viva_com` | `viva_com_merchant_id`, `viva_com_api_key`, `viva_com_client_id`, `viva_com_client_secret`, `viva_com_terminal_id`, `viva_com_test_mode` |
| `pos_pine_labs` | 18.0+ | `pine_labs` | `pine_labs_merchant`, `pine_labs_store`, `pine_labs_client`, `pine_labs_security_token`, `pine_labs_allowed_payment_mode`, `pine_labs_test_mode` |
| `pos_qfpay` | 19.0+ | `qfpay` | `qfpay_terminal_ip_address`, `qfpay_pos_key`, `qfpay_notification_key`, `qfpay_payment_type` |
| `pos_mollie` | 19.0+ | `mollie` | `mollie_terminal_id`, `mollie_payment_provider_id` (the Mollie payment provider, `payment_mollie`) |
| `pos_dpopay` | 19.0+ | `dpopay` | `dpopay_client_id`, `dpopay_client_secret`, `dpopay_mid`, `dpopay_tid`, `dpopay_chain_id`, `dpopay_payment_mode`, `dpopay_test_mode` |
| `pos_safaricom` | 19.0+ | `safaricom` (M-Pesa) | `consumer_key`, `consumer_secret`, `business_short_code`, `passkey`, `safaricom_payment_type`, `safaricom_test_mode`; 20.0 adds `safaricom_till_number`, `safaricom_paybill_number`, `safaricom_identifier_type` |
| `pos_sumup` | 20.0 | `sumup` | `sumup_api_key`, `sumup_merchant_code`, `sumup_terminal_id`, `sumup_pairing_code` |
| `pos_bancontact_pay` | 20.0 | `bancontact_pay`, with `payment_method_type='external_qr'` | `bancontact_api_key`, `bancontact_ppid`, `bancontact_usage`, `bancontact_test_mode` |

## Cash machines

The machine counts the cash in and gives the change. Use a `cash` journal.

| Module | Versions | Link (19.0: `payment_method_type`; 20.0: `payment_method_type='cash_machine'` and `payment_provider`) | Settings on the method |
|---|---|---|---|
| `pos_cashdro` | 19.0+ | 19.0 `cashdro`; 20.0 `cashdro` | `cashdro_ip`, `cashdro_username`, `cashdro_password`, `cashdro_use_lna` |
| `pos_cashmatic` | 19.0+ | 19.0 `cashmatic`; 20.0 `cashmatic` | `cashmatic_ip`, `cashmatic_username`, `cashmatic_password`, `cashmatic_use_lna` |
| `pos_glory_cash` | 19.0+ | 19.0 `glory_cash`; 20.0 `glory` | `glory_websocket_address`, `glory_username`, `glory_password`; 20.0 `glory_use_lna` |

20.0:

```python
machine = PM.create({
    'name': 'Cash machine', 'type': 'cash', 'journal_id': cash_journal.id, 'company_id': company.id,
    'payment_method_type': 'cash_machine', 'payment_provider': 'cashdro',
    'cashdro_ip': '<IP from the user>', 'cashdro_username': '<user>', 'cashdro_password': '<password>',
})
config.write({'payment_method_ids': [(4, machine.id)]})
env.cr.commit()
```

19.0: the same without `type` and `payment_provider`, with `'payment_method_type':
'cashdro'`.

## Printers

Receipt printers print the customer receipt and open the cash drawer; preparation
printers print the kitchen and bar tickets ([pos-restaurant.md](pos-restaurant.md)).
Community drives Epson printers with ePOS and iMin devices from the browser.

| | Module | Where | Fields |
|---|---|---|---|
| Epson receipt printer, 16.0 to 18.0 | `pos_epson_printer` | Settings ‣ ePos Printer | shop: `other_devices`, `epson_printer_ip`, `iface_cashdrawer` (Link Cashdrawer) |
| Epson receipt printer, 19.0 | `point_of_sale` | Settings ‣ ePos Printer | same fields, now in `point_of_sale` |
| Receipt printers, 20.0 | `point_of_sale` | Settings ‣ Receipt Printers; Configuration ‣ Printers | shop: `other_devices`, `receipt_printer_ids`; printer: `use_type='receipt'`, `printer_type`, `printer_ip`, `paper_size`, `use_cashdrawer`, `use_lna`, `timeout` |
| Epson kitchen printer, 16.0 | `pos_epson_printer_restaurant` | Configuration ‣ Order Printers (developer mode) | `restaurant.printer`: `printer_type='epson_epos'`, `epson_printer_ip`, `product_categories_ids` |
| Epson preparation printer, 17.0, 18.0 | `pos_epson_printer` | Orders ‣ Preparation Printers | `pos.printer`: `printer_type='epson_epos'`, `epson_printer_ip`, `product_categories_ids` |
| Epson preparation printer, 19.0 | `point_of_sale` | same | same |
| Preparation printers, 20.0 | `point_of_sale` | Configuration ‣ Printers | `pos.printer`: `use_type='preparation'`, `printer_ip`, `product_categories_ids`, `is_split_per_product` |
| iMin built-in printer, 19.0 | `pos_imin` | run the POS on the iMin device; Settings ‣ ePos Printer shows Link Cashdrawer | shop: `other_devices`, `iface_cashdrawer` |
| iMin printer, 20.0 | `pos_imin` | Configuration ‣ Printers | `pos.printer`: `printer_type='imin'`, receipt only |

The receipt printer, 20.0:

```python
printer = env['pos.printer'].create({
    'name': 'Counter', 'use_type': 'receipt', 'printer_type': 'epson_epos',
    'printer_ip': '<printer IP or serial>', 'paper_size': '80', 'use_cashdrawer': True,
})
config.write({'other_devices': True, 'receipt_printer_ids': [(4, printer.id)]})
env.cr.commit()
```

16.0 to 19.0 (`pos_epson_printer` up to 18.0):

```python
config.write({'other_devices': True, 'epson_printer_ip': '<printer IP>', 'iface_cashdrawer': True})
env.cr.commit()
```

Then print a test receipt from the POS (or the test button next to the IP in Settings).

## Variations

- **Tip on the terminal (Adyen).** Shop setting Add tip through payment terminal
  (`adyen_ask_customer_for_tip`) needs Tips on (`iface_tipproduct`, `tip_product_id`);
  tip after payment is in [pos-restaurant.md](pos-restaurant.md).
- **Backend reports on a network printer (20.0, `printer`).** Installed with
  `stock_delivery`. Inventory ‣ Configuration ‣ Reporting ‣ Manage Printers: a printer
  (`printer.printer`: `name`, `type` `zpl` or `epos`, `ip_address`) and its Linked Reports
  (`report_ids`). Printing a linked report sends it to the printer (ZPL labels as they
  are, PDF reports as an image for ePOS); the first time, the user picks the printers and
  can tick Do not ask me again; Reset Linked Printers forgets that choice.

  ```python
  label_printer = env['printer.printer'].create({'name': 'Shipping labels', 'type': 'zpl', 'ip_address': '<printer IP>',
                                                 'report_ids': [(6, 0, report.ids)]})
  env.cr.commit()
  ```

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Terminal link field | `use_payment_terminal` | same | `payment_method_type='terminal'` + `use_payment_terminal` | same | `payment_method_type` + `payment_provider` |
| `type` on the method | computed from the journal | same | same | same | required (`cash`, `bank`, `pay_later`) |
| Cash machines | none | none | none | `payment_method_type` | `cash_machine` + `payment_provider` |
| Epson receipt printer | `pos_epson_printer` | same | same | in `point_of_sale` | `pos.printer`, `use_type='receipt'` |
| Preparation printer model | `restaurant.printer` | `pos.printer` | same | same | same, `use_type='preparation'` |
| POS forced to HTTP for ePOS printers | yes (`point_of_sale.enforce_https` turns it off) | same | same | no | no |
| Local network access | | | | `point_of_sale.use_lna` parameter | `use_lna` per printer and cash machine |

## Verify

```python
config = env['pos.config'].browse(<shop id>)
print([(m.name, m.payment_provider, m.journal_id.name) for m in config.payment_method_ids])
print(config.other_devices, config.receipt_printer_ids.mapped('name'))
```

That is 20.0. Up to 19.0 read `m.use_payment_terminal` and, for the receipt printer,
`config.epson_printer_ip`.

Then ask the cashier to pay one order with each terminal and print a receipt; check the
payment line shows the terminal's transaction.

## Pitfalls

- A terminal method on a journal that is not `bank`, or a cash machine on one that is not
  `cash`, is refused or hidden.
- Payment methods of a shop with an open session cannot be changed: close it first.
- Test mode (`*_test_mode`) left on in production takes no real payment; turn it off with
  the user once the test passes.
- An Epson printer reached from an HTTPS page: up to 18.0 Odoo opens the POS over HTTP
  (unless `point_of_sale.enforce_https` is set); from 19.0 give the printer's serial
  number instead of its IP (Odoo turns it into the Epson certificate domain) or use Local
  Network Access.
- Stripe terminals need the Stripe payment provider of the company configured; Mollie
  terminals the Mollie provider.
- The provider's webhook or event URL must be pasted in its portal, or payments stay
  waiting.

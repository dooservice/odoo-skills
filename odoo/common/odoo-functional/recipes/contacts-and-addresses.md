# Contacts, addresses and working schedules

What completes the contacts of `partners-and-imports.md`: addresses split into street
name and number with a city list (`base_address_extended`), coordinates of an address
(`base_geolocalize`), phone numbers formatted per country and a phone blacklist
(`phone_validation`), finding and removing a person's data on request
(`privacy_lookup`), and, up to 18.0, product pictures fetched by barcode
(`product_images`). It also covers working schedules (`resource.calendar`) and public
holidays, which every app that counts working time uses (`resource`). Time off of
employees is in `employees-and-expenses.md`.

**At a glance**

- Apps: `contacts`, `resource`, `phone_validation`, `privacy_lookup`;
  `base_geolocalize`, `base_address_extended`; `product_images` (16.0 to 18.0).
- Names that change by version: Working Schedules menu under Settings ‣ Technical (16.0),
  Employees ‣ Configuration ‣ Employee (17.0-19.0), ‣ Time Management (20.0); `tz` on the
  schedule (16.0-19.0), on the resource with `calendar_type` (20.0); Public Holidays
  (16.0-19.0), Company Holidays (20.0); `day_period` `lunch` (17.0+), `full_day` (19.0+);
  `product_images` (16.0-18.0).
- Sections: Before you start; The standard flow (1 working schedule, 2 public holidays,
  3 extended addresses, 4 geolocate contacts); Variations; Versions; Verify; Pitfalls.

## Before you start

- Apps: `contacts`. `resource`, `phone_validation` and `privacy_lookup` install with
  other apps. Settings ‣ General Settings, Integrations: `module_base_geolocalize`
  (Geolocation), `module_product_images` (16.0 to 18.0). `base_address_extended` from
  Apps (localizations install it). Ask before installing.
- Settings: `geoloc_provider_id` (OpenStreetMap or Google, with
  `geoloc_provider_googlemap_key`); `google_custom_search_key`, `google_pse_id`
  (product images). Keys come from the user's Google account.
- Read first:

```python
print(env['resource.calendar'].search_read([], ['name', 'company_id', 'hours_per_day']))
print(env.company.resource_calendar_id.name)
print(env['resource.calendar.leaves'].search_read([('resource_id', '=', False)], ['name', 'date_from', 'date_to', 'calendar_id'], limit=20))
```

## The standard flow

1. **Working schedule.** Employees ‣ Configuration ‣ Employee ‣ Working Schedules
   (20.0: ‣ Time Management ‣ Working Schedules); without Employees, Settings ‣
   Technical ‣ Resource ‣ Working Schedules (developer mode). One line per day and
   period.

   20.0:

   ```python
   cal = env['resource.calendar'].create({'name': 'Standard 40 hours', 'company_id': env.company.id})
   print([(a.dayofweek, a.hour_from, a.hour_to) for a in cal.attendance_ids])
   env.cr.commit()
   ```

   19.0, 18.0, 17.0, 16.0:

   ```python
   cal = env['resource.calendar'].create({'name': 'Standard 40 hours', 'company_id': env.company.id,
                                          'tz': env.user.tz or 'UTC'})
   print([(a.dayofweek, a.hour_from, a.hour_to) for a in cal.attendance_ids])
   env.cr.commit()
   ```

   Leaves a schedule filled with the default week (Monday to Friday, 8 hours). Change a
   day with `attendance_ids` lines: `dayofweek` `'0'` (Monday) to `'6'`, `hour_from`,
   `hour_to`, `day_period` (`morning`, `afternoon`; 17.0+ also `lunch`, 19.0+
   `full_day`). The company default is `env.company.resource_calendar_id` (Employees
   settings). 20.0 puts the timezone on each resource and adds `calendar_type`
   (`fixed`, `variable`, `undefined`); up to 19.0 `tz` is on the schedule.

2. **Public holidays.** Time Off ‣ Configuration ‣ Public Holidays (20.0: Company
   Holidays); without Time Off, Settings ‣ Technical ‣ Resource ‣ Resource Time Off.

   ```python
   env['resource.calendar.leaves'].create({'name': 'New Year', 'company_id': env.company.id,
                                          'date_from': '2027-01-01 00:00:00', 'date_to': '2027-01-01 23:59:59'})
   env.cr.commit()
   ```

   Without `resource_id` it applies to everyone; with `calendar_id` only to that
   schedule. Dates are UTC.

3. **Extended addresses.** Contacts ‣ Configuration ‣ Localization ‣ Countries, the
   country: Enforce Cities (`enforce_cities`) and an address format with
   `%(street_name)s`, `%(street_number)s`, `%(street_number2)s`. Cities in Contacts ‣
   Configuration ‣ Localization ‣ Cities (17.0+; 16.0 has no menu, create them through
   the ORM).

   ```python
   country = env['res.country'].search([('code', '=', '<country code>')])
   env['res.city'].create({'name': '<city>', 'zipcode': '<zip>', 'country_id': country.id})
   env.cr.commit()
   ```

   Leaves the contact form asking street name, number and door, and the city from the
   list (`city_id`) for that country.

4. **Geolocate contacts.** Contacts ‣ the contact, Partner Assignment tab ‣
   Compute based on address (`geo_localize`).

   ```python
   partners = env['res.partner'].search([('city', '!=', False), ('partner_latitude', '=', 0)], limit=50)
   partners.geo_localize()
   env.cr.commit()
   ```

   Leaves `partner_latitude`, `partner_longitude` and `date_localization`. OpenStreetMap
   needs no key and limits requests per second.

## Variations

- **Phone numbers** (`phone_validation`). Numbers typed in contact forms are formatted
  in international form from the contact's country (or the company's). The Phone
  Blacklist (Settings ‣ Technical ‣ Phone / SMS ‣ Phone Blacklist) stops SMS mailings to
  a number.
- **Privacy lookup** (`privacy_lookup`). Contacts ‣ the contact ‣ Actions ‣ Privacy
  Lookup (also on users): name and email are searched in every model; from the result
  list, archive or delete each record, or all of them. Each run is logged in Settings ‣
  Technical ‣ Privacy ‣ Privacy Logs.
- **Product images** (16.0 to 18.0, `product_images`). Products list, select products
  with a barcode ‣ Actions ‣ Get Pictures: images found by Google Custom Search for the
  barcode.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Working Schedules menu | Settings ‣ Technical | Employees ‣ Configuration ‣ Employee | same | same | Employees ‣ Configuration ‣ Time Management |
| Schedule `tz` | on schedule | same | same | same | on resource; `calendar_type` |
| Public holidays menu | Public Holidays | same | same | same | Company Holidays |
| `product_images` | yes | yes | yes | no | no |

## Verify

```python
print(cal.name, cal.hours_per_day, len(cal.attendance_ids))
print(env['res.city'].search_count([('country_id', '=', country.id)]), country.enforce_cities)
print(partners[:5].mapped(lambda p: (p.name, p.partner_latitude, p.partner_longitude)))
```

## Pitfalls

- Changing a schedule used by employees changes past and future working time
  computations (time off durations, planning); create a new schedule instead.
- Holidays entered without `company_id` apply to every company.
- `enforce_cities` with an empty city list blocks every address of that country: load
  the cities first.
- Privacy lookup deletes for good; prefer archiving and ask the user for each model.

# Website content

The content of a website besides the shop: pages (`website.page`) and their menu
(`website.menu`), redirects (`website.rewrite`), a blog (`website_blog`), a forum
(`website_forum`) with user profiles and karma (`website_profile`), customer references
(`website_customer`), public partner pages (`website_partner`), maps
(`website_google_map`), email discussion groups (`mail_group`, `website_mail_group`) and
the protections and helpers of forms: reCAPTCHA (`google_recaptcha`), Cloudflare
Turnstile (`website_cf_turnstile`), address autocomplete, Unsplash images
(`web_unsplash`), SMS to visitors (`website_sms`). Designing a page with building blocks
and themes is done by the user in the website editor; this recipe gives the records
behind it. The shop is in `website-and-ecommerce.md` and `ecommerce-extras.md`; website
languages in `languages-and-translations.md`; the newsletter blocks in
`email-and-sms-marketing.md`.

**At a glance**

- Apps: `website`; Blog, Forum and others install from Apps or from the website's
  `+New` menu. Ask before installing.
- Names that change by version: Turnstile 17.0+; `enable_recaptcha` 19.0+; address
  autocomplete `website_sale_autocomplete` up to 19.0, `website_address_autocomplete`
  20.0; `website_twitter` up to 17.0; Technical Pages 19.0, System Pages 20.0.
- Sections: Before you start; The standard flow (1 create a page, 2 arrange the menu, 3
  redirect old addresses, 4 publish a blog post, 5 open a forum); Variations; Versions;
  Verify; Pitfalls.

## Before you start

- Settings: Settings ‣ General Settings, Integrations: `module_google_recaptcha`,
  `module_website_cf_turnstile` (17.0+), `module_web_unsplash`,
  `module_google_address_autocomplete` (19.0+). Website ‣ Configuration ‣ Settings,
  per website (pass `website_id`): domain, languages, `website_cookies_bar`, analytics.
- Read first:

```python
print(env['website'].search_read([], ['name', 'domain', 'default_lang_id', 'homepage_url']))
print(env['website.page'].search_read([], ['name', 'url', 'website_id', 'is_published'], limit=30))
print(env['website.menu'].search_read([('parent_id.parent_id', '=', False)], ['name', 'url', 'website_id', 'parent_id']))
```

## The standard flow

1. **Create a page.** Website ‣ Site ‣ Content ‣ Pages ‣ New, or `+New` ‣ Page on the
   website; the user designs it in the editor.

   ```python
   website = env['website'].search([('name', '=', '<website name>')])
   res = env['website'].with_context(website_id=website.id).new_page('About us', add_menu=True)
   page = env['website.page'].search([('url', '=', res['url']), ('website_id', '=', website.id)])
   env.cr.commit()
   ```

   Leaves the page at `/about-us` with a menu entry. Publish it with its Published
   switch (`page.write({'is_published': True})`).

2. **Arrange the menu.** Website ‣ Site ‣ Menu Editor on the website, or Website ‣
   Configuration ‣ Menus.

   ```python
   top = website.menu_id
   env['website.menu'].create({'name': 'Contact', 'url': '/contactus', 'parent_id': top.id,
                               'website_id': website.id, 'sequence': 90})
   env.cr.commit()
   ```

   Each website has its own top menu (`website.menu_id`); entries must have it as
   parent, or a child of it, and the same `website_id`.

3. **Redirect old addresses.** Website ‣ Configuration ‣ Redirects ‣ New.

   ```python
   env['website.rewrite'].create({'name': 'Old about page', 'url_from': '/old-about',
                                  'url_to': page.url, 'redirect_type': '301', 'website_id': website.id})
   env.cr.commit()
   ```

   `redirect_type`: `301` (permanent), `302` (temporary), `308` (permanent, keeps the
   method), `404` (not found).

4. **Publish a blog post.** Website ‣ Configuration ‣ Blogs ‣ Blogs (Blog from 17.0) for
   the blog, then Website ‣ Site ‣ Content ‣ Blog Posts, or `+New` ‣ Blog Post.

   ```python
   blog = env['blog.blog'].create({'name': 'News', 'website_id': website.id})
   post = env['blog.post'].create({'blog_id': blog.id, 'name': 'Product A is here',
                                   'content': '<p>What is new.</p>', 'is_published': True})
   env.cr.commit()
   print(post.website_url)
   ```

   `post_date` schedules the publication; tags in Website ‣ Configuration ‣ Blog ‣ Tags.

5. **Open a forum.** Website ‣ Configuration ‣ Forum ‣ Forums ‣ New.

   ```python
   forum = env['forum.forum'].create({'name': 'Help', 'mode': 'questions', 'privacy': 'public',
                                      'website_id': website.id})
   env.cr.commit()
   ```

   `mode`: `questions` (one accepted answer) or `discussions`. `privacy`: `public`,
   `connected` (signed-in users), `private` (one group, `authorized_group_id`). Karma
   thresholds on the forum's Karma tab decide who may post, edit, vote and moderate.
   Posts are under Website ‣ Site ‣ Content ‣ Forum Posts; ranks and badges under
   Website ‣ Configuration ‣ Forum.

## Variations

- **User profiles** (`website_profile`). Public pages of users who earn karma in forums
  and courses; `karma_profile_min` on the website (default 150) is the karma needed to
  see other profiles.
- **Customer references** (`website_customer`, it needs `website_crm_partner_assign`).
  A published customer whose Implemented by (`assigned_partner_id`) is set shows on
  `/customers`, filtered by Website Tags (Contacts ‣ Configuration ‣ Website Tags,
  `website_tag_ids`). `website_partner` gives each published partner a page
  (`website_description`, `website_short_description`).
- **Map** (`website_google_map`). `/google_map` shows the partners on Google Maps. The
  key (`google_maps_api_key`, on the website) is asked by the editor when a Map block is
  added; it comes from the user's Google account.
- **Email discussion groups** (`mail_group`). Website ‣ Configuration ‣ Mailing Lists ‣
  Mailing Lists (Settings ‣ Technical ‣ Discuss ‣ Mail Groups without website): a
  `mail.group` with an email alias, `access_mode` (`public`, `members`, `groups`),
  `moderation` with moderators. Members join on `/groups`; a mail to the alias reaches
  every member.
- **Bot protection.** reCAPTCHA v3: `recaptcha_public_key`, `recaptcha_private_key`,
  `recaptcha_min_score` (19.0+ also `enable_recaptcha`). Turnstile (17.0+):
  `turnstile_site_key`, `turnstile_secret_key`. Both protect the website forms, sign-up
  and newsletter. Keys come from the user's Google or Cloudflare account.
- **Address autocomplete with Google Places.** Forms suggest addresses as the visitor
  types. Up to 19.0 at checkout, `website_sale_autocomplete`: Website ‣ Configuration ‣
  Settings, `google_places_api_key` (19.0: `website_google_places_api_key`). 19.0+
  `google_address_autocomplete` in the back end (Settings ‣ General Settings,
  `google_places_api_key`); 20.0 `website_address_autocomplete` for the website forms
  (`website_google_places_api_key`).
- **Unsplash images** (`web_unsplash`). `unsplash_access_key` and `unsplash_app_id` let
  the editor search free photos.
- **SMS to visitors** (`website_sms`). Website ‣ Reporting ‣ Visitors, a visitor with a
  mobile number ‣ Send SMS (`action_send_sms`).
- **Twitter feed** (16.0, 17.0, `website_twitter`): `twitter_api_key`,
  `twitter_api_secret`, `twitter_screen_name` for the Twitter scroller block. Removed
  in 18.0.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Blog configuration menu | Blogs | Blog | Blog | Blog | Blog |
| Turnstile | no | yes | yes | yes | yes |
| `enable_recaptcha` | no | no | no | yes | yes |
| Address autocomplete | `website_sale_autocomplete` | same | same | same, plus `google_address_autocomplete` | `website_address_autocomplete`, `google_address_autocomplete` |
| `website_twitter` | yes | yes | no | no | no |
| Technical Pages menu | no | no | no | Technical Pages | System Pages |

## Verify

```python
print(page.url, page.is_published, page.menu_ids.mapped('name'))
print(post.is_published, post.website_url, forum.mode, forum.privacy)
print(env['website.rewrite'].search_read([('website_id', '=', website.id)], ['url_from', 'url_to', 'redirect_type']))
```

Then ask the user to open the pages in a private window.

## Pitfalls

- A page or menu without `website_id` shows on every website of the database.
- Deleting a page leaves its menu entries and links pointing to a 404: add a redirect.
- A `301` is cached by browsers and search engines; use `302` while testing.
- A public forum without karma thresholds attracts spam; keep the defaults and turn on
  reCAPTCHA or Turnstile.
- Changing a website's domain breaks its sessions and the links already sent in emails.

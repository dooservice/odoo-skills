# Contributing

Corrections are welcome, above all for versions other than 20.0, where Odoo's own skills
say less.

## The rule: check it in the source

Every version-specific statement must be true in that branch of
[odoo/odoo](https://github.com/odoo/odoo). Before you change one, check it in the source
of that version, and say in the pull request where (file and line, or a link).

## Where to change what

| To change | Edit |
|---|---|
| `odoo/<version>/odoo-guidelines`, `odoo-web-guidelines`, `odoo-security`, `odoo-review`, `odoo-git` | the template in `tools/guidelines/templates/`, or its class in `tools/guidelines/documents/` for what differs per version, then regenerate |
| `odoo/<version>/odoo-reference` | `tools/reference/`, then regenerate with `tools/build_reference.py` |
| `odoo/common/odoo-upgrade` | the files directly |
| `odoo/common/odoo-functional` | the files directly; check every version difference against each branch's source |
| `localization/<country code>/` | the files directly; see [Add your country](#add-your-country) |

Do not edit generated files by hand: the next regeneration overwrites them. The README
explains how to check out Odoo's source and regenerate.

## How a recipe is written

Every recipe of `odoo-functional` has the same parts, in this order, so an agent always
knows where to look:

````markdown
# <Area, in business words>

<One paragraph: what it covers, which apps it needs, what is Enterprise and left out.>

## Before you start

- Apps: `<module>` (and from which version, when that changes).
- Settings: the switches it needs, by their `res.config.settings` field.
- Read first:

```python
<a snippet that shows the current state>
```

## The standard flow

The way Odoo does it, in the order a user does it in the interface. Each step names the
menu, gives the ORM equivalent, and says the state it leaves:

1. **<Step>.** <App> ‣ <Menu> ‣ <Item>.

   ```python
   <the same through the ORM>
   ```

   Leaves the <document> in `<state>`.

## Variations

<The common alternatives to the standard flow, each with when to choose it.>

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| <what differs> | | | | | |

## Verify

```python
<a snippet that proves the result>
```

## Pitfalls

- <What goes wrong in real databases, with its fix.>
````

Two rules decide what a recipe says:

- **The flow is Odoo's.** It follows Odoo's documentation of that version
  (`odoo.com/documentation/<version>/applications/...`) and the menus of that version,
  read from a running Odoo (`env.ref('<menu xml id>').complete_name`). A recipe never
  invents a shortcut Odoo does not offer.
- **Every snippet runs.** It is run on a database of each version it claims, and its
  effect is read back. A step that differs between versions says so where it happens and
  in `## Versions`.

## Add your country

A localization tells an agent what a functional consultant in that country knows: which
`l10n_*` modules to install, the chart of accounts and taxes, how contacts are
identified, electronic invoicing, legal reports, and what breaks in production.

1. Copy `localization/template/odoo-l10n-xx/` to `localization/<country code>/odoo-l10n-<country code>/`,
   with the country's ISO code in lowercase, as Odoo names its modules (`l10n_pe` is `pe`).
2. Rename `xx` and `<Country>` everywhere, including the `name` in `SKILL.md`.
3. Replace each instruction with what is true in your country, and delete the
   instructions. Keep the sections and their order: the check refuses a localization
   without them.
4. `versions.md`: what changes between 16.0 and 20.0 for this country.
5. `MAINTAINERS.md`: at least one person who will review changes to it.
6. Run `python3 tools/build_catalog.py`, which checks it and adds its plugin, and commit
   `.claude-plugin/marketplace.json` with it.

Every statement about Odoo is checked in the source of the version it names, like the rest
of this repository; every legal rule cites its official source under `## Sources`. Nothing
country-specific goes into `odoo-functional` or the other skills: it goes here.

Changes to a country's folder are reviewed by its maintainers.

## Pull requests

- One change per pull request, for every version it applies to.
- Commit messages in English, one line, saying what the change fixes:
  `fix(17.0): odoo-guidelines uses _sql_constraints, not models.Constraint`.
- Run the generators and commit their output together with your change.

## Sign your commits

Every commit must carry a `Signed-off-by` line, which says you wrote the change or have
the right to submit it under this project's license, as the
[Developer Certificate of Origin](https://developercertificate.org) describes. Add it with
`git commit -s`.

## Code of conduct

Everyone taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md). Report unacceptable
behaviour to [soporte@apiservicesac.com](mailto:soporte@apiservicesac.com).

## License

By contributing, you agree that your contribution is licensed under the
[LGPL-3.0](LICENSE), like the rest of the repository.

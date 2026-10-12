# Email templates

A template is a `mail.template` on a model: the quotation, invoice or delivery email.
Find the standard one by XML id (`grep "mail.template" odoo-reference/xmlids/<addon>.md`)
rather than by name.

```python
template = env.ref('sale.email_template_edi_sale')
template.write({'subject': 'Your quotation {{ object.name }} from {{ object.company_id.name }}'})
env.cr.commit()
```

- `subject` and `email_to` use `{{ }}` expressions; `body_html` is QWeb (`t-out`). Change
  the words, keep the expressions; read the current body before writing a new one.
- Translations: each language keeps its own text. Write it with
  `template.with_context(lang='es_ES').write({...})` for that language.
- Editing a standard template is kept through updates, but a module update may bring a
  new version of it: say so, and prefer a copy (`template.copy()`) for big changes.

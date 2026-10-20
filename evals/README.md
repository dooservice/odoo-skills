# Measuring what the skills change

`odoo-16/` holds 20 tasks an agent gets on an Odoo 16.0 project: 10 that write code
(views, models, controllers, JavaScript) and 10 that configure Odoo with a script
(products, automations, payment terms, taxes, users, stock). Each one checks the file the
agent writes: that it uses what Odoo 16.0 has (`<tree>`, `attrs`, `name_get`,
`detailed_type`...) and none of what only later versions have (`<list>`,
`models.Constraint`, `is_storable`...). No model judges the answers.

Every task runs twice: with the `odoo-16` skills and without them, so the difference is
what the skills add.

## Run it

`claude plugin eval` needs a plugin folder, so put the 16.0 skills and these cases in one:

```bash
plugin=$(mktemp -d)/odoo-16
mkdir -p "$plugin/.claude-plugin" "$plugin/skills"
cp -r odoo/16.0/* odoo/common/* "$plugin/skills/"
cp -r evals "$plugin/evals"
echo '{"name": "odoo-16", "version": "1.0.0"}' > "$plugin/.claude-plugin/plugin.json"

claude plugin eval "$plugin" --eval-dir evals/odoo-16 --allow-tools Write \
  --runs 3 --model claude-sonnet-5-5 --max-cost-usd 10 --threshold 0
```

It costs about 0.06 USD per task and run with Sonnet, both sides included.

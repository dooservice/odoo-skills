---
name: dooservice-console
description: >-
  How to work in a dooservice development console: the dooservice command
  (install, update, test, shell, restart, logs, publish), what survives the
  session, deploy holds, database locks, and how changes reach the remote. Use
  when installing, updating or testing modules, restarting the environment,
  reading its logs, committing or publishing work.
---

# Working in a dooservice console

This container is attached to one development environment. The environment's Odoo
server and database run in their own container, which keeps running after the console
closes. This one is created when the console opens and destroyed when it closes.

## Commands

| Command | What it does |
| --- | --- |
| `dooservice install <mod>[,<mod>]` | install modules (`odoo-bin -i ... --stop-after-init`) |
| `dooservice update <mod>[,<mod>]` | update modules after a change (`-u`), `all` for everything |
| `dooservice test <mod>` | update installed modules and run their tests (`-u ... --test-enable`) |
| `dooservice shell` | Odoo shell on this database (`env` is ready) |
| `dooservice restart` | restart the environment's Odoo so it loads changed Python |
| `dooservice logs -n 200` / `-f` | the environment's Odoo log |
| `dooservice status` | whether the environment is running |
| `dooservice storage` | what the repository, filestore and database occupy |
| `dooservice publish --title ... --body-file -` | push what was committed and open its pull requests |

`odoo-bin` is a wrapper that injects the database, its host, the addons path, the data
directory and `--workers=0`: never pass those, and never `cd` before calling it. Use it
directly for other options, e.g. `odoo-bin --test-tags /mod:Class.test_x --stop-after-init`.

## The loop

1. Edit in `/mnt/addons`.
2. `dooservice update <mod>` (or `install` the first time). XML and data are live after it.
3. After Python changes, also `dooservice restart`: the running server does not reload.
4. `dooservice logs -n 200` when the update or the restart says something went wrong.
5. `dooservice test <mod>`.
6. Ask the user to check it in the browser: `echo $DOOSERVICE_BUILD_URL`.

Show command output as it streams; do not wait for a long command to finish silently.

## Locks

The running server holds connections to the same database: an update can hit a lock
(`could not obtain lock`, `canceling statement due to lock timeout`). Wait a few
seconds and retry; if it persists, tell the user rather than restarting things on
your own.

## What survives

- **Survives:** the repository on the server, committed or not, until the next deploy;
  the conversation, for this person and this environment.
- **Lost when the console closes:** the home directory, anything installed with `pip`
  (only the repository's `requirements.txt` is installed on the environment), files
  outside `/mnt/addons`.
- **Lost at the next deploy:** every commit not published. A deploy resets the
  repository to the remote branch. While the console is open the platform holds the
  environment's deploys; they resume when it closes.

So: commit as you go, and publish before the session ends.

## Publishing

`git push` has no credentials here on purpose. Commit following `odoo-git` (a change
inside a submodule is committed in the submodule first, then in the project), then
publish. `dooservice publish` refuses a pull request that breaks the rules below and
says what to fix, before anything is pushed: fix it and publish again.

### Title

Odoo's commit header: `[TAG] module: summary`.

- `TAG` is one of `FIX IMP ADD REF REM MOV REV PERF I18N MIG`.
- `module` is the technical name, lowercase; several separated by commas
  (`acme_sale, acme_stock`), `*` for many.
- The summary is imperative, without a final period. The whole title is 80 characters
  at most. It stays in English when the commits are in English.

### Description

These sections, in this order, headed in the language of `$DOOSERVICE_LANGUAGE`
(`es` Spanish, anything else English). Every section has content; only the last may be
empty, and a risk-free change says so (`Ninguno.` / `None.`).

| English | Español | What goes in it |
| --- | --- | --- |
| `## Summary` | `## Resumen` | what changes, 1 to 3 lines |
| `## Why` | `## Motivo` | the problem or the request, for whom |
| `## Changes` | `## Cambios` | a bullet per module: what changed in it |
| `## How to test` | `## Cómo probar` | numbered steps on this environment, with the expected result |
| `## Deployment` | `## Despliegue` | modules to update (`-u`), migrations, new `requirements.txt` lines, restart |
| `## Risks` | `## Riesgos` | what could break and for whom, or none |
| `## References` | `## Referencias` | ticket or task, only when the user gave one; never invented |

Write it from what you did and verified, plainly and technically: no marketing, no
emoji, no closing line. The platform signs every pull request
(`🤖 Generado con Dooservice` / `🤖 Generated with Dooservice`) and every commit made by
an AI session gets `Co-authored-by: Dooservice` by itself: do not add either.

```bash
dooservice publish --title "[FIX] acme_sale: keep the delivery date on duplicate" --body-file - <<'BODY'
## Resumen
Al duplicar un pedido confirmado se conserva la fecha de entrega prometida.

## Motivo
La copia salía con la fecha de hoy y el cliente recibía una fecha equivocada.

## Cambios
- acme_sale: `commitment_date` se copia al duplicar; las plantillas la limpian en su `copy()`.

## Cómo probar
1. Ventas → un pedido confirmado con fecha de entrega → Acción → Duplicar.
2. La copia tiene la misma fecha de entrega.

## Despliegue
`dooservice update acme_sale`. Sin migraciones ni dependencias nuevas.

## Riesgos
Ninguno: solo afecta a pedidos duplicados.

## Referencias
BODY
```

It pushes everything committed to a new branch `dooservice/<environment>-<timestamp>`,
opens one pull request per changed submodule (into that submodule's default branch)
and one for the project (into `$DOOSERVICE_BRANCH`), and prints their links: give them
to the user. Nothing reaches any environment until somebody merges.

If it answers that this session cannot publish, give the user the commits as patches:
`git format-patch origin/$DOOSERVICE_BRANCH --stdout`.

## The other skills' commands here

The Odoo skills use plain `odoo-bin`; here prefer the wrappers: `odoo-bin -i` is
`dooservice install`, `odoo-bin -u` is `dooservice update`, `-u ... --test-enable` is
`dooservice test`, `odoo-bin shell` is `dooservice shell`. The Odoo source is in
`/usr/lib/python3/dist-packages/odoo`.

## Environment variables

`DOOSERVICE_ENVIRONMENT`, `DOOSERVICE_PROJECT`, `DOOSERVICE_SERVER`, `DOOSERVICE_BRANCH`,
`DOOSERVICE_BUILD_URL`, `DOOSERVICE_LANGUAGE`, `ODOO_VERSION`, `ADDONS_PATH`. The
database connection is in the `PGHOST`/`PGUSER`/`PGDATABASE`... variables, already used by `psql` and `odoo-bin`.

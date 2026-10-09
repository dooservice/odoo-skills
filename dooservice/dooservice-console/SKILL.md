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
inside a submodule is committed in the submodule first, then in the project), then:

```bash
dooservice publish --title "<one line, imperative>" --body-file - <<'BODY'
<why, the modules touched, how to test it, module updates needed, risks>
BODY
```

It pushes everything committed to a new branch `dooservice/<environment>-<timestamp>`,
opens one pull request per changed submodule (into that submodule's default branch)
and one for the project (into `$DOOSERVICE_BRANCH`), and prints their links: give them
to the user. Write the title and description in the user's language. Nothing reaches
any environment until somebody merges.

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

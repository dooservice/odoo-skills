A service is a long-lived object that the web client starts once and every component
shares: the `orm` to call the server, `action` to open actions, `notification` and
`dialog` to talk to the user. Services are entries of `registry.category("services")`
and are started before the first component renders.

The main services of this version: `orm`, `action`, `notification`,
`dialog`, `effect`, `ui` (`isSmall`, `block`), `hotkey`, `title`, `localization`,
`menu`, `view`, `command`, `popover`, `http`, `field`, `name` and `overlay`.

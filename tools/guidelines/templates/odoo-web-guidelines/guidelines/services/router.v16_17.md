`useService("router")` gives `current` (`{ pathname, search, hash }`, with `hash`
and `search` parsed) and `pushState(hash, { replace })`, which merges the keys into the
URL hash. The action service keeps the URL in sync with the action; change it yourself
only for state of your own client action (a selected tab), with keys prefixed by your
module.
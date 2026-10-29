`_t("Book lent")` translates at call time, so it must run after the translations are
loaded: inside a function or a component, never at module level. A string defined at
module level (a label in a registry entry, a constant) uses `_lt("Book lent")`, which
translates when it is displayed. `_t` takes no values: format with `sprintf` from
`@web/core/utils/strings` (`sprintf(_t("Lent to %s"), name)`).
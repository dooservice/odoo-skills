`_t("Book lent")` may be called anywhere, at module level too: before the translations
are loaded it returns a lazy string that translates when displayed. Values are passed
after the string: `_t("Lent to %s", name)`. `_lt` is only an alias of `_t` kept for old
code.
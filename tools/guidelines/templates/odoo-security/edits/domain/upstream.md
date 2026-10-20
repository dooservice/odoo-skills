- Build/extend domains with `fields.Domain` (`domain &= Domain(...)`), never
  by concatenating a user-provided list onto a security domain (a user could
  inject `['|', ...]` to widen access).

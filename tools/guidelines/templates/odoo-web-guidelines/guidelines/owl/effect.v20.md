`useEffect(() => { ... })` runs again whenever a signal or proxy value it read
  changes, with no dependency list; it is the place for work that follows state. The
  Owl 2 form with a dependency list is `useLayoutEffect(fn, () => [deps])` from
  `@web/owl2/utils`, kept only for code not ported yet.
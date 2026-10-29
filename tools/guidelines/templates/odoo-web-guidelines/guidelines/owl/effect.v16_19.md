`useEffect(() => { ...; return cleanup; }, () => [this.state.bookId])` runs after
  render when one of the listed dependencies changed, and runs the cleanup first; it is
  the place for DOM work that depends on state.
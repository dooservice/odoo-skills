Template expressions reach the component through `this`: `this.props.title`,
  `this.state.count`, `t-on-click="this.onLend"`; a bare `props.title` is not the
  component's prop. `t-on-click="() => this.lend(book)"` passes an argument.
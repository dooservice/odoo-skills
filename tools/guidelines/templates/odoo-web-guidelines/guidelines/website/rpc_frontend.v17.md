the `rpc` service: `this.rpc = this.bindService("rpc")` in a public widget, then
  `this.rpc("/my_module/books", { limit: 10 })`
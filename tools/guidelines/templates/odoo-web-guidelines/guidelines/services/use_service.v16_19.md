- In a component: `this.orm = useService("orm")` in `setup`. The hook protects the
  component: a call made after the component is destroyed never resolves, so a late
  answer does not update a dead component.
- Outside a component (another service, a registry function that receives the env):
  `env.services.orm`, or a dependency of your service.
- Never import a service's internals to reach it, and never store a service on
  `window` or a module-level variable: tests replace services, and a global keeps the
  real one.

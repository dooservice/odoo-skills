`useSubEnv({ bookModel })` adds keys to the environment of the component and its
  children, and `useChildSubEnv` to its children only. Use it for a context a whole
  subtree needs, such as the model of a view.
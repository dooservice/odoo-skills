- `category("group_config_items")` holds the entries of the gear menu of a group header,
  in kanban columns and in grouped lists: `{ label, method, isVisible, class, icon }`,
  where `method` is a function or the name of a method of the menu, and `isVisible` may
  be a function of `{ permissions }`.
- `category("phone_call_handlers")` holds `{ isApplicable(env, params), execute(env,
  params, { fallback }) }`: when the user clicks a phone number, the first entry that is
  applicable places the call (a VoIP module); with none, the browser opens the `tel:`
  link. `params` holds `phoneNumber`, and `resModel` and `resId` when known.
- `category("share_target_items")` holds components extending `ShareTargetItem`
  (`static name`, `static sequence`): the apps offered when files are shared to the
  installed web app; the chosen item receives the `files`.

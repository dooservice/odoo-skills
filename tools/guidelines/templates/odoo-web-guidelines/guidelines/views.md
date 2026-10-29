# Views on the client side in $version

A view is an arch from the server turned into components: an `ArchParser` reads the
arch, a `Model` loads the records, a `Renderer` draws them and a `Controller` holds the
control panel and the buttons. Each view type is a descriptor in
`registry.category("views")`, each field widget an entry of
`registry.category("fields")`, and each `<widget>` an entry of
`registry.category("view_widgets")`.

- Change how one field looks or edits: a field widget, named in the arch with
  `widget="my_module_rating"`.
- Add something to a view that is not a field (a banner, a button bar): a view widget,
  `<widget name="my_module_banner"/>`.
- Change how a whole view behaves (a button in the control panel, a different load):
  a new view descriptor, named with `js_class` on the arch root.
- Change one standard widget or view everywhere: `patch` its component, as a last
  resort.

# Write a field widget as a component plus a registry entry

$field_widget

# Read arch attributes and options in `extractProps`

$extract_props

- Name the options in `snake_case` in the arch (`options="{'max_stars': 3}"`) and turn
  them into `camelCase` props in `extractProps`; the component never reads the arch.
- Give every prop a default, so the widget works without options.
- Declare what the widget accepts, so Studio and the field documentation show it:
  $supported_info.

# Prefix a widget key with a view type to change it in one view only

The field registry is searched from the most specific key to the least:
$lookup_order.

Register `list.my_module_rating` to give the list a lighter version of the widget, and
keep `my_module_rating` for the other views.

$lookup_trap

# Extend a view with `js_class`, never by patching it for one model

```js
$list_view_import
import { ListController } from "@web/views/list/list_controller";
import { registry } from "@web/core/registry";

export class BookListController extends ListController {
    static template = "my_module.BookListController";
    async onClickLendAll() {
        ...
    }
}

registry.category("views").add("my_module_book_list", {
    ...listView,
    Controller: BookListController,
});
```

```xml
<$list_tag js_class="my_module_book_list">
```

- Spread the standard descriptor and replace only the part that changes (`Controller`,
  `Renderer`, `Model`, `ArchParser`, `buttonTemplate`); the others stay in sync with
  Odoo's code at each upgrade.
- The controller's template extends the standard one with `t-inherit` and
  `t-inherit-mode="primary"`, so it can add a button next to the standard ones.
- $js_class_missing
- Patching `ListController.prototype` instead changes every list of the database; do it
  only when that is the goal.

# Add a `<widget>` to a view through `view_widgets`

$view_widget

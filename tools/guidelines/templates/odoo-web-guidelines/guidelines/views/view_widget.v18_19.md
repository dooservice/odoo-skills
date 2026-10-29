A view widget is a component that receives the `record`; it renders in the arch where
`<widget name="my_module_banner"/>` stands, in form, list and kanban views.

```js
export class BookBanner extends Component {
    static template = "my_module.BookBanner";
    static props = { ...standardWidgetProps, text: { type: String, optional: true } };
}
registry.category("view_widgets").add("my_module_banner", {
    component: BookBanner,
    extractProps: ({ attrs }) => ({ text: attrs.title }),
});
```

`standardWidgetProps` (`@web/views/widgets/standard_widget_props`) holds `record` and
`readonly`. The descriptor also takes `fieldDependencies` for the fields the widget
reads, which are then loaded even when the arch does not show them.

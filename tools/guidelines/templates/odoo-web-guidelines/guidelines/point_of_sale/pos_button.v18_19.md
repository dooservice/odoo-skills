The buttons under the order are the `ControlButtons` component
(`@point_of_sale/app/screens/product_screen/control_buttons/control_buttons`). Add a
button by extending its template and patching the component for the handler:

```xml
<t t-name="my_module.ControlButtons" t-inherit="point_of_sale.ControlButtons" t-inherit-mode="extension">
    <xpath expr="//t[@t-if='props.showRemainingButtons']" position="inside">
        <button class="btn btn-light" t-on-click="onClickLendBook">Lend</button>
    </xpath>
</t>
```

```js
patch(ControlButtons.prototype, {
    async onClickLendBook() {
        ...
    },
});
```

A component the button needs is added with `patch(ControlButtons, { components: {
...ControlButtons.components, LendDialog } })`.

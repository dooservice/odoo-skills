`category("dialogs")` holds dialogs that core code opens by key without importing
  them; web uses it for `select_create`, the dialog that searches and creates records.
  Open your own dialogs with the `dialog` service instead.
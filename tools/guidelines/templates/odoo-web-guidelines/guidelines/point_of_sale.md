Key names in $version:

$essentials

Sections of this file:

$sections

# The Point of Sale in $version

The Point of Sale is a separate web application (`/pos/ui`), not a view of the backend
client. It loads its data once when a session opens, keeps it in the browser, and works
offline: sales are recorded in the browser and synchronized with the server later.
Every extension has to respect that.

$pos_intro

# Load a field into the Point of Sale from Python

The POS only knows the records and fields that the session loads at start; a field
added to a model is invisible there until the loading code names it.

$pos_loading

# Extend Point of Sale models and screens without replacing them

$pos_models

# Add a button to the product screen through its extension point

$pos_button

# Keep the Point of Sale working offline

- Never call the server in the middle of a sale (on a click of the product screen, on
  each order line): the session may be offline, and every call slows the cashier down.
  Load what the sale needs at start, and compute in the browser.
- A call to the server is for an action that needs it anyway (validating a payment
  with a terminal, printing to an IoT box), and its error path tells the cashier what
  happened instead of losing the sale.
- Business rules that must hold (taxes, stock, accounting) are enforced on the server
  when the order is synchronized; the browser only previews them.

# Test the Point of Sale with tours

$pos_tests

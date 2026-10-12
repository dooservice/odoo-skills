# pos_glory_cash — POS Glory Cash Machines

Depends on: point_of_sale.

## `pos.payment.method` (extends)

- `glory_websocket_address` Char “Cash Machine IP”
- `glory_username` Char “Cash Machine Username”
- `glory_password` Char “Cash Machine Password”
- `glory_use_lna` Boolean “Cash Machine Local Network Access”

Extension points: `_get_cash_machine_selection`

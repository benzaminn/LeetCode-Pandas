/*
Input: 
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+
Output: 
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
Explanation: 
The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
So the result is customer_number 3.  */

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:

    max_order = orders.groupby("customer_number")["order_number"].count().reset_index()

    return max_order[max_order["order_number"] == max_order["order_number"].max()][["customer_number"]]


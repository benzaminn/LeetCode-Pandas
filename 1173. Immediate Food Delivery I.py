'''
If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

Find the percentage of immediate orders in the table, rounded to 2 decimal places.

The result format is in the following example.

Example 1:

Input: 
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 5           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-11                  |
| 4           | 3           | 2019-08-24 | 2019-08-26                  |
| 5           | 4           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
+-------------+-------------+------------+-----------------------------+
Output: 
+----------------------+
| immediate_percentage |
+----------------------+
| 33.33                |
+----------------------+  '''


import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    df = delivery[delivery['order_date']==delivery['customer_pref_delivery_date']]
    cent = round(df.shape[0]*100/delivery.shape[0],2)
    return pd.DataFrame({'immediate_percentage':[cent]})









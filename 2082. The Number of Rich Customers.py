''' 

Report the number of customers who had at least one bill with an amount strictly greater than 500.

The result format is in the following example.

 

Example 1:

Input: 
Store table:
+---------+-------------+--------+
| bill_id | customer_id | amount |
+---------+-------------+--------+
| 6       | 1           | 549    |
| 8       | 1           | 834    |
| 4       | 2           | 394    |
| 11      | 3           | 657    |
| 13      | 3           | 257    |
+---------+-------------+--------+
Output: 
+------------+
| rich_count |
+------------+
| 2          |
+------------+ '''


import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:

    df = store[store['amount']>500]
    cnt = df['customer_id'].nunique()
    result = pd.DataFrame({'rich_count':[cnt]})
    return result



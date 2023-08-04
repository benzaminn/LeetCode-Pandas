'''
Calculate the number of bank accounts of each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
Output: 
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+ '''


import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    low = accounts[accounts['income']  < 20000].shape[0]
    avg = accounts[(accounts['income']>=20000) & (accounts.income <=50000)].shape[0]
    high = accounts[accounts.income > 50000].shape[0]
    data  = {'category': ['Low Salary','Average Salary','High Salary'],
            'accounts_count':[low, avg, high]}
    df = pd.DataFrame(data)
    return df



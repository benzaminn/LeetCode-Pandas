'''
Find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+ '''


import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    df = employee['salary'].sort_values(ascending=False).drop_duplicates()

    if len(df) > 1:
        second_highest = df.iloc[1]
    else:
        second_highest = None

    return pd.DataFrame({'SecondHighestSalary':[second_highest]})


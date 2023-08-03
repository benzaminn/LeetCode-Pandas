'''
Find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

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
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+ '''


import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    df_unique = employee['salary'].unique()

    if len(df_unique) < N:
        return pd.DataFrame([np.NaN],columns =[f'getMthHighestSalary({N})'])
    else:
        salary = sorted(df_unique,reverse=True)[N-1]

        return pd.DataFrame([salary],columns = [f'getMthHighestSalary({N})'])



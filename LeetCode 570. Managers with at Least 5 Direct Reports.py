'''
Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | None      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+ '''


import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    df = employee.merge(employee,how="inner",left_on="id",right_on="managerId")

    df = df.groupby(["id_x","name_x"])["id_y"].count().reset_index().rename(columns={"name_x":"name"})

    return df[df["id_y"] >=5][["name"]]




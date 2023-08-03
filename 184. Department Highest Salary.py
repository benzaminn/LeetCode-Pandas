'''
Find employees who have the highest salary in each of the departments.

Return the result table in any order.

The result format is in the following example.


Example 1:

Input: 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+ '''



import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    data = pd.merge(employee,department,left_on='departmentId',right_on='id',how='left')
    df = data.groupby('name_y').apply(lambda x:x[x['salary']==x['salary'].max()])
    df = df.rename(columns={'name_y':'Department','name_x':'Employee'})
    df = df.drop(columns=['id_x','id_y'])

    return df[['Department','Employee','salary']]



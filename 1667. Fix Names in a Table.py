'''

Fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

The result format is in the following example.

 

Example 1:

Input: 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
Output: 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+ '''



import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    users['name'] = users['name'].apply(lambda x:x.capitalize())
    users.sort_values(by='user_id',inplace=True)

    return users



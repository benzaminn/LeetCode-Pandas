
'''
Find the patient_id, patient_name and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Patients table:
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
+------------+--------------+--------------+
Output: 
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 | 
+------------+--------------+--------------+ '''



import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    # df   = patients[patients['conditions'].str.contains(r'(^DIAB1)|( DIAB1)')]

    df = patients[patients['conditions'].str.contains(r'\bDIAB1')]

    # The \b in the pattern is a word boundary assertion that ensures 'DIAB1' is a separate word and not part of another word


    return df



